from __future__ import annotations

import tomllib
from pathlib import Path

import pytest

from raman_bacteria_prototype.environment import REQUIRED_PATHS


@pytest.mark.integration
def test_required_repository_paths_exist(project_root: Path) -> None:
    missing = [path for path in REQUIRED_PATHS if not (project_root / path).exists()]
    assert missing == []


@pytest.mark.unit
def test_pyproject_contract(project_root: Path) -> None:
    with (project_root / "pyproject.toml").open("rb") as handle:
        data = tomllib.load(handle)
    assert data["project"]["name"] == "raman-bacteria-prototype"
    assert data["project"]["version"] == "0.1.0"
    assert data["project"]["requires-python"] == ">=3.11,<3.12"
    assert data["build-system"]["build-backend"] == "uv_build"
    assert data["tool"]["uv"]["required-version"] == "==0.11.29"
    assert data["tool"]["coverage"]["report"]["fail_under"] == 90
    assert data["tool"]["ruff"]["line-length"] == 88
    assert data["tool"]["black"]["line-length"] == 88


@pytest.mark.unit
def test_no_public_license(project_root: Path) -> None:
    assert not (project_root / "LICENSE").exists()
