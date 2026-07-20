"""Canonical aggregate validation runner."""

from __future__ import annotations

import json
import queue
import shutil
import subprocess
import sys
import threading
import time
from collections.abc import Callable
from dataclasses import asdict, dataclass
from datetime import UTC, datetime
from pathlib import Path
from typing import TextIO

from .environment import find_repository_root


@dataclass(frozen=True)
class CommandSpec:
    """One mandatory validation command."""

    check_id: str
    argv: tuple[str, ...]


@dataclass(frozen=True)
class CommandResult:
    """Captured result for one validation command."""

    check_id: str
    argv: tuple[str, ...]
    started_at_utc: str
    finished_at_utc: str
    duration_seconds: float
    exit_code: int
    status: str
    stdout: str
    stderr: str

    def to_dict(self) -> dict[str, object]:
        """Return a JSON-serializable representation."""
        return asdict(self)


def utc_now() -> str:
    """Return an ISO-8601 UTC timestamp."""
    return datetime.now(UTC).isoformat()


def build_command_specs(
    root: Path,
    uv_executable: str,
    python_executable: str,
) -> tuple[CommandSpec, ...]:
    """Return the authoritative seven-check sequence.

    Every Python or tool command is executed through ``uv run --locked`` so
    validation cannot silently refresh the lockfile.
    """
    locked_run = (uv_executable, "run", "--locked")
    return (
        CommandSpec("LOCK", (uv_executable, "lock", "--check")),
        CommandSpec(
            "ENVIRONMENT",
            (
                *locked_run,
                python_executable,
                str(root / "scripts/check_environment.py"),
            ),
        ),
        CommandSpec(
            "GITIGNORE",
            (*locked_run, python_executable, str(root / "scripts/check_gitignore.py")),
        ),
        CommandSpec(
            "DOCUMENTATION",
            (
                *locked_run,
                python_executable,
                str(root / "scripts/check_documentation.py"),
            ),
        ),
        CommandSpec(
            "TESTS",
            (
                *locked_run,
                "pytest",
                "-q",
                "--cov=raman_bacteria_prototype",
                "--cov-branch",
                "--cov-report=term-missing",
                "--cov-report=xml:coverage.xml",
                "--cov-fail-under=90",
            ),
        ),
        CommandSpec("RUFF", (*locked_run, "ruff", "check", ".")),
        CommandSpec("BLACK", (*locked_run, "black", "--check", ".")),
    )


def _reader(
    stream: TextIO,
    channel: str,
    events: queue.Queue[tuple[str, str | None]],
) -> None:
    try:
        for line in iter(stream.readline, ""):
            events.put((channel, line))
    finally:
        events.put((channel, None))


def run_subprocess(spec: CommandSpec, cwd: Path) -> CommandResult:
    """Run a child process, stream both channels, and retain their content."""
    started = utc_now()
    start_clock = time.monotonic()
    try:
        process = subprocess.Popen(
            spec.argv,
            cwd=cwd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            encoding="utf-8",
            errors="replace",
            bufsize=1,
        )
    except FileNotFoundError as exc:
        finished = utc_now()
        return CommandResult(
            spec.check_id,
            spec.argv,
            started,
            finished,
            round(time.monotonic() - start_clock, 6),
            127,
            "FAIL",
            "",
            str(exc),
        )

    assert process.stdout is not None
    assert process.stderr is not None
    events: queue.Queue[tuple[str, str | None]] = queue.Queue()
    threads = [
        threading.Thread(
            target=_reader,
            args=(process.stdout, "stdout", events),
            daemon=True,
        ),
        threading.Thread(
            target=_reader,
            args=(process.stderr, "stderr", events),
            daemon=True,
        ),
    ]
    for thread in threads:
        thread.start()

    buffers: dict[str, list[str]] = {"stdout": [], "stderr": []}
    completed_channels = 0
    while completed_channels < 2:
        channel, line = events.get()
        if line is None:
            completed_channels += 1
            continue
        buffers[channel].append(line)
        destination = sys.stdout if channel == "stdout" else sys.stderr
        destination.write(line)
        destination.flush()

    for thread in threads:
        thread.join()
    exit_code = process.wait()
    finished = utc_now()
    return CommandResult(
        spec.check_id,
        spec.argv,
        started,
        finished,
        round(time.monotonic() - start_clock, 6),
        exit_code,
        "PASS" if exit_code == 0 else "FAIL",
        "".join(buffers["stdout"]),
        "".join(buffers["stderr"]),
    )


def normalize_for_comparison(payload: dict[str, object]) -> dict[str, object]:
    """Remove volatile timing fields for deterministic test comparisons."""
    normalized = json.loads(json.dumps(payload))
    for result in normalized.get("results", []):
        result.pop("started_at_utc", None)
        result.pop("finished_at_utc", None)
        result.pop("duration_seconds", None)
    normalized.pop("started_at_utc", None)
    normalized.pop("finished_at_utc", None)
    return normalized


def run_checks(
    *,
    root: Path | None = None,
    output_path: Path | None = None,
    executor: Callable[[CommandSpec, Path], CommandResult] = run_subprocess,
    which: Callable[[str], str | None] = shutil.which,
    python_executable: str = sys.executable,
) -> tuple[int, dict[str, object]]:
    """Run every mandatory check and return the overall exit code and summary."""
    overall_started = utc_now()
    try:
        repository_root = root.resolve() if root else find_repository_root()
        uv_executable = which("uv")
        if uv_executable is None:
            missing = CommandResult(
                "LOCK",
                ("uv", "lock", "--check"),
                overall_started,
                utc_now(),
                0.0,
                127,
                "FAIL",
                "",
                "Required executable 'uv' was not found.",
            )
            results = [missing]
        else:
            specs = build_command_specs(
                repository_root,
                uv_executable,
                python_executable,
            )
            results = [executor(spec, repository_root) for spec in specs]

        passed = len(results) == 7 and all(item.exit_code == 0 for item in results)
        payload: dict[str, object] = {
            "schema_version": "1",
            "repository_root": str(repository_root),
            "started_at_utc": overall_started,
            "finished_at_utc": utc_now(),
            "overall_status": "PASS" if passed else "FAIL",
            "results": [item.to_dict() for item in results],
        }
        destination = (
            output_path or repository_root / "reports/logs/week_1/check-results.json"
        )
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_text(
            json.dumps(payload, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )
        return (0 if passed else 1), payload
    except Exception as exc:
        payload = {
            "schema_version": "1",
            "started_at_utc": overall_started,
            "finished_at_utc": utc_now(),
            "overall_status": "ERROR",
            "error": f"{type(exc).__name__}: {exc}",
            "results": [],
        }
        return 2, payload
