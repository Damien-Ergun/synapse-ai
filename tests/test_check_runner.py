from __future__ import annotations

from pathlib import Path

import pytest

from raman_bacteria_prototype.checks import (
    CommandResult,
    build_command_specs,
    normalize_for_comparison,
    run_checks,
)


def result(check_id: str, argv: tuple[str, ...], code: int = 0) -> CommandResult:
    return CommandResult(
        check_id,
        argv,
        "2026-07-20T00:00:00+00:00",
        "2026-07-20T00:00:01+00:00",
        1.0,
        code,
        "PASS" if code == 0 else "FAIL",
        "out",
        "err" if code else "",
    )


@pytest.mark.unit
def test_exact_command_order(project_root: Path) -> None:
    specs = build_command_specs(project_root, "uv", "python")
    assert [spec.check_id for spec in specs] == [
        "LOCK",
        "ENVIRONMENT",
        "GITIGNORE",
        "DOCUMENTATION",
        "TESTS",
        "RUFF",
        "BLACK",
    ]
    assert specs[0].argv == ("uv", "lock", "--check")
    assert "--cov-fail-under=90" in specs[4].argv


@pytest.mark.unit
def test_all_success_returns_zero(project_root: Path, tmp_path: Path) -> None:
    seen: list[str] = []

    def fake(spec, cwd):
        assert cwd == project_root
        seen.append(spec.check_id)
        return result(spec.check_id, spec.argv)

    code, payload = run_checks(
        root=project_root,
        output_path=tmp_path / "result.json",
        executor=fake,
        which=lambda name: "uv" if name == "uv" else None,
        python_executable="python",
    )
    assert code == 0
    assert payload["overall_status"] == "PASS"
    assert seen == [
        "LOCK",
        "ENVIRONMENT",
        "GITIGNORE",
        "DOCUMENTATION",
        "TESTS",
        "RUFF",
        "BLACK",
    ]
    assert (tmp_path / "result.json").is_file()


@pytest.mark.unit
def test_child_failure_propagates_but_all_checks_run(
    project_root: Path, tmp_path: Path
) -> None:
    seen: list[str] = []

    def fake(spec, cwd):
        seen.append(spec.check_id)
        return result(spec.check_id, spec.argv, 1 if spec.check_id == "TESTS" else 0)

    code, payload = run_checks(
        root=project_root,
        output_path=tmp_path / "result.json",
        executor=fake,
        which=lambda _: "uv",
        python_executable="python",
    )
    assert code == 1
    assert payload["overall_status"] == "FAIL"
    assert len(seen) == 7


@pytest.mark.unit
def test_missing_uv_is_127_child_and_overall_failure(
    project_root: Path, tmp_path: Path
) -> None:
    code, payload = run_checks(
        root=project_root,
        output_path=tmp_path / "result.json",
        which=lambda _: None,
    )
    assert code == 1
    assert payload["results"][0]["exit_code"] == 127
    assert payload["overall_status"] == "FAIL"


@pytest.mark.unit
def test_unexpected_exception_returns_two(project_root: Path) -> None:
    def broken(spec, cwd):
        raise RuntimeError("boom")

    code, payload = run_checks(
        root=project_root,
        output_path=Path("/not-used"),
        executor=broken,
        which=lambda _: "uv",
    )
    assert code == 2
    assert payload["overall_status"] == "ERROR"


@pytest.mark.unit
def test_normalized_payload_is_deterministic() -> None:
    payload = {
        "started_at_utc": "a",
        "finished_at_utc": "b",
        "results": [
            {
                "check_id": "LOCK",
                "started_at_utc": "c",
                "finished_at_utc": "d",
                "duration_seconds": 1.0,
                "exit_code": 0,
            }
        ],
    }
    assert normalize_for_comparison(payload) == {
        "results": [{"check_id": "LOCK", "exit_code": 0}]
    }


@pytest.mark.integration
def test_run_subprocess_captures_stdout_and_stderr(project_root: Path) -> None:
    import sys

    from raman_bacteria_prototype.checks import CommandSpec, run_subprocess

    spec = CommandSpec(
        "STREAM",
        (
            sys.executable,
            "-c",
            "import sys; print('hello'); print('problem', file=sys.stderr)",
        ),
    )
    observed = run_subprocess(spec, project_root)
    assert observed.exit_code == 0
    assert observed.status == "PASS"
    assert observed.stdout == "hello\n"
    assert observed.stderr == "problem\n"


@pytest.mark.unit
def test_run_subprocess_missing_executable_returns_127(project_root: Path) -> None:
    from raman_bacteria_prototype.checks import CommandSpec, run_subprocess

    observed = run_subprocess(
        CommandSpec("MISSING", ("definitely-not-an-executable-raman",)),
        project_root,
    )
    assert observed.exit_code == 127
    assert observed.status == "FAIL"
    assert observed.stderr


@pytest.mark.unit
def test_command_specs_use_locked_uv_for_every_tool(project_root: Path) -> None:
    specs = build_command_specs(project_root, "uv", "python")
    assert specs[0].argv == ("uv", "lock", "--check")
    for spec in specs[1:]:
        assert spec.argv[:3] == ("uv", "run", "--locked")
