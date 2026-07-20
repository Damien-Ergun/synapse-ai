"""Pure and CLI-friendly environment validation."""

from __future__ import annotations

import importlib.util
import json
import re
import shutil
import subprocess
import sys
import tomllib
from collections.abc import Iterable, Sequence
from dataclasses import asdict, dataclass
from pathlib import Path

SUPPORTED_MAJOR_MINOR = (3, 11)
REQUIRED_UV_VERSION = "0.11.29"
REQUIRED_PATHS = (
    ".github/workflows/ci.yml",
    ".python-version",
    ".gitignore",
    "README.md",
    "pyproject.toml",
    "uv.lock",
    "configs/README.md",
    "data/README.md",
    "docs/architecture.md",
    "docs/decision_log.md",
    "docs/programme/12_week_roadmap.md",
    "docs/weekly_plans/week_1_work_plan.md",
    "models/README.md",
    "notebooks/README.md",
    "reports/README.md",
    "scripts/run_checks.py",
    "src/raman_bacteria_prototype/__init__.py",
    "tests",
)


@dataclass(frozen=True)
class CheckResult:
    """One deterministic validation result."""

    check_id: str
    passed: bool
    message: str

    def to_dict(self) -> dict[str, object]:
        return asdict(self)


def is_supported_python(version_info: Sequence[int]) -> bool:
    """Return whether a version tuple has the supported major and minor."""
    return tuple(version_info[:2]) == SUPPORTED_MAJOR_MINOR


def find_repository_root(start: Path | None = None) -> Path:
    """Find the project root without trusting the current working directory."""
    origin = (start or Path(__file__)).resolve()
    current = origin if origin.is_dir() else origin.parent
    for candidate in (current, *current.parents):
        if (candidate / "pyproject.toml").is_file() and (
            candidate / "docs/weekly_plans/week_1_work_plan.md"
        ).is_file():
            return candidate
    raise FileNotFoundError("Repository root markers were not found.")


def load_project_metadata(root: Path) -> dict[str, object]:
    """Load and minimally validate project TOML metadata."""
    path = root / "pyproject.toml"
    with path.open("rb") as handle:
        data = tomllib.load(handle)
    project = data.get("project")
    if not isinstance(project, dict):
        raise ValueError("[project] table is missing or malformed.")
    if project.get("name") != "raman-bacteria-prototype":
        raise ValueError("Unexpected project name.")
    if project.get("requires-python") != ">=3.11,<3.12":
        raise ValueError("Unexpected Python support constraint.")
    return data


def parse_uv_version(output: str) -> str | None:
    """Extract a semantic uv version from `uv --version` output."""
    match = re.search(r"\buv\s+(\d+\.\d+\.\d+)\b", output)
    return match.group(1) if match else None


def get_uv_version(uv_executable: str | None = None) -> str | None:
    """Return the current uv version, or None if uv cannot be invoked."""
    executable = uv_executable or shutil.which("uv")
    if executable is None:
        return None
    try:
        completed = subprocess.run(
            [executable, "--version"],
            check=False,
            capture_output=True,
            text=True,
            timeout=30,
        )
    except (OSError, subprocess.SubprocessError):
        return None
    if completed.returncode != 0:
        return None
    return parse_uv_version(completed.stdout)


def evaluate_environment(
    root: Path,
    *,
    version_info: Sequence[int] | None = None,
    uv_version: str | None = None,
    required_paths: Iterable[str] = REQUIRED_PATHS,
) -> list[CheckResult]:
    """Evaluate repository, interpreter, metadata, and import preconditions."""
    results: list[CheckResult] = []
    observed = tuple(version_info or sys.version_info)
    results.append(
        CheckResult(
            "ENV-PYTHON",
            is_supported_python(observed),
            f"Observed Python {observed[0]}.{observed[1]}.{observed[2]}",
        )
    )
    observed_uv = uv_version if uv_version is not None else get_uv_version()
    results.append(
        CheckResult(
            "ENV-UV",
            observed_uv == REQUIRED_UV_VERSION,
            f"Observed uv {observed_uv or 'unavailable'}; required {REQUIRED_UV_VERSION}",
        )
    )
    try:
        load_project_metadata(root)
    except (OSError, tomllib.TOMLDecodeError, ValueError) as exc:
        results.append(CheckResult("ENV-PROJECT", False, str(exc)))
    else:
        results.append(CheckResult("ENV-PROJECT", True, "Project metadata is valid."))

    for relative in required_paths:
        exists = (root / relative).exists()
        results.append(
            CheckResult(
                f"ENV-PATH:{relative}",
                exists,
                f"{relative}: {'present' if exists else 'missing'}",
            )
        )

    package_spec = importlib.util.find_spec("raman_bacteria_prototype")
    results.append(
        CheckResult(
            "ENV-IMPORT",
            package_spec is not None,
            (
                "Package import is discoverable."
                if package_spec
                else "Package import failed."
            ),
        )
    )
    return results


def run_environment_checks(root: Path | None = None) -> tuple[int, dict[str, object]]:
    """Run all environment checks and return CLI exit code and stable payload."""
    try:
        resolved = root.resolve() if root else find_repository_root()
        results = evaluate_environment(resolved)
        passed = all(item.passed for item in results)
        return (0 if passed else 1), {
            "status": "PASS" if passed else "FAIL",
            "repository_root": str(resolved),
            "checks": [item.to_dict() for item in results],
        }
    except Exception as exc:  # pragma: no cover - final defensive boundary
        return 2, {"status": "ERROR", "error": f"{type(exc).__name__}: {exc}"}


def print_environment_report(payload: dict[str, object]) -> None:
    """Print a stable JSON environment report."""
    print(json.dumps(payload, indent=2, sort_keys=True))
