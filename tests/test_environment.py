from __future__ import annotations

import shutil
import tomllib
from pathlib import Path

import pytest

from raman_bacteria_prototype.environment import (
    REQUIRED_PATHS,
    evaluate_environment,
    find_repository_root,
    is_supported_python,
    load_project_metadata,
    parse_uv_version,
    run_environment_checks,
)


@pytest.mark.unit
@pytest.mark.parametrize(
    ("version", "expected"),
    [((3, 11, 15), True), ((3, 10, 14), False), ((3, 12, 0), False)],
)
def test_supported_python_is_injectable(
    version: tuple[int, ...], expected: bool
) -> None:
    assert is_supported_python(version) is expected


@pytest.mark.unit
def test_parse_uv_version() -> None:
    assert parse_uv_version("uv 0.11.29 (abc)") == "0.11.29"
    assert parse_uv_version("unexpected") is None


@pytest.mark.unit
def test_find_repository_root_from_nested_path(project_root: Path) -> None:
    assert find_repository_root(project_root / "tests") == project_root


@pytest.mark.unit
def test_find_repository_root_fails_without_markers(tmp_path: Path) -> None:
    with pytest.raises(FileNotFoundError):
        find_repository_root(tmp_path)


@pytest.mark.unit
def test_load_project_metadata(project_root: Path) -> None:
    assert (
        load_project_metadata(project_root)["project"]["name"]
        == "raman-bacteria-prototype"
    )


@pytest.mark.unit
def test_load_project_metadata_rejects_malformed(tmp_path: Path) -> None:
    (tmp_path / "pyproject.toml").write_text("[project\n", encoding="utf-8")
    with pytest.raises(tomllib.TOMLDecodeError):
        load_project_metadata(tmp_path)


@pytest.mark.unit
def test_evaluate_environment_success(project_root: Path) -> None:
    results = evaluate_environment(
        project_root,
        version_info=(3, 11, 15),
        uv_version="0.11.29",
    )
    assert results
    assert all(result.passed for result in results)


@pytest.mark.unit
def test_evaluate_environment_reports_missing_path(
    project_root: Path, tmp_path: Path
) -> None:
    shutil.copytree(
        project_root,
        tmp_path / "repo",
        dirs_exist_ok=True,
        ignore=shutil.ignore_patterns(".venv", ".git"),
    )
    root = tmp_path / "repo"
    (root / "uv.lock").unlink()
    results = evaluate_environment(
        root,
        version_info=(3, 11, 15),
        uv_version="0.11.29",
    )
    assert any(
        result.check_id == "ENV-PATH:uv.lock" and not result.passed
        for result in results
    )


@pytest.mark.unit
def test_evaluate_environment_reports_bad_python_and_uv(project_root: Path) -> None:
    results = evaluate_environment(
        project_root, version_info=(3, 12, 0), uv_version="0.1.0"
    )
    assert not next(
        result for result in results if result.check_id == "ENV-PYTHON"
    ).passed
    assert not next(result for result in results if result.check_id == "ENV-UV").passed


@pytest.mark.unit
def test_custom_required_paths(project_root: Path) -> None:
    results = evaluate_environment(
        project_root,
        version_info=(3, 11, 15),
        uv_version="0.11.29",
        required_paths=("does-not-exist",),
    )
    assert not next(
        result for result in results if result.check_id.startswith("ENV-PATH")
    ).passed


@pytest.mark.integration
def test_run_environment_checks_explicit_root(
    project_root: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    import raman_bacteria_prototype.environment as environment

    monkeypatch.setattr(environment.sys, "version_info", (3, 11, 15))
    monkeypatch.setattr(environment, "get_uv_version", lambda: "0.11.29")
    code, payload = run_environment_checks(project_root)
    assert code == 0
    assert payload["status"] == "PASS"
    assert len(payload["checks"]) >= len(REQUIRED_PATHS)


@pytest.mark.unit
def test_load_project_metadata_requires_project_table(tmp_path: Path) -> None:
    (tmp_path / "pyproject.toml").write_text("[tool.pytest]\n", encoding="utf-8")
    with pytest.raises(ValueError, match="project"):
        load_project_metadata(tmp_path)


@pytest.mark.unit
@pytest.mark.parametrize(
    "metadata",
    (
        '[project]\nname = "wrong"\nrequires-python = ">=3.11,<3.12"\n',
        '[project]\nname = "raman-bacteria-prototype"\nrequires-python = ">=3.12"\n',
    ),
)
def test_load_project_metadata_rejects_wrong_contract(
    tmp_path: Path, metadata: str
) -> None:
    (tmp_path / "pyproject.toml").write_text(metadata, encoding="utf-8")
    with pytest.raises(ValueError):
        load_project_metadata(tmp_path)


@pytest.mark.unit
def test_get_uv_version_missing(monkeypatch: pytest.MonkeyPatch) -> None:
    import raman_bacteria_prototype.environment as environment

    monkeypatch.setattr(environment.shutil, "which", lambda _: None)
    assert environment.get_uv_version() is None


@pytest.mark.unit
def test_get_uv_version_success(monkeypatch: pytest.MonkeyPatch) -> None:
    import raman_bacteria_prototype.environment as environment

    class Completed:
        returncode = 0
        stdout = "uv 0.11.29\n"

    monkeypatch.setattr(
        environment.subprocess, "run", lambda *args, **kwargs: Completed()
    )
    assert environment.get_uv_version("uv") == "0.11.29"


@pytest.mark.unit
def test_get_uv_version_command_failure(monkeypatch: pytest.MonkeyPatch) -> None:
    import raman_bacteria_prototype.environment as environment

    class Completed:
        returncode = 1
        stdout = ""

    monkeypatch.setattr(
        environment.subprocess, "run", lambda *args, **kwargs: Completed()
    )
    assert environment.get_uv_version("uv") is None


@pytest.mark.unit
def test_get_uv_version_oserror(monkeypatch: pytest.MonkeyPatch) -> None:
    import raman_bacteria_prototype.environment as environment

    def fail(*args, **kwargs):
        raise OSError("unavailable")

    monkeypatch.setattr(environment.subprocess, "run", fail)
    assert environment.get_uv_version("uv") is None


@pytest.mark.unit
def test_evaluate_environment_reports_malformed_project(
    project_root: Path, tmp_path: Path
) -> None:
    shutil.copytree(
        project_root,
        tmp_path / "repo",
        dirs_exist_ok=True,
        ignore=shutil.ignore_patterns(".venv", ".git"),
    )
    root = tmp_path / "repo"
    (root / "pyproject.toml").write_text("[project\n", encoding="utf-8")
    results = evaluate_environment(
        root,
        version_info=(3, 11, 15),
        uv_version="0.11.29",
    )
    assert not next(
        result for result in results if result.check_id == "ENV-PROJECT"
    ).passed


@pytest.mark.unit
def test_run_environment_checks_error_boundary(
    project_root: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    import raman_bacteria_prototype.environment as environment

    def fail(*args, **kwargs):
        raise RuntimeError("boom")

    monkeypatch.setattr(environment, "evaluate_environment", fail)
    code, payload = run_environment_checks(project_root)
    assert code == 2
    assert payload["status"] == "ERROR"
