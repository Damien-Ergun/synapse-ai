from __future__ import annotations

import shutil
from pathlib import Path

import pytest


@pytest.fixture
def project_root() -> Path:
    return Path(__file__).resolve().parents[1]


@pytest.fixture
def minimal_repo(tmp_path: Path, project_root: Path) -> Path:
    for relative in (
        "pyproject.toml",
        "uv.lock",
        "docs/weekly_plans/week_1_work_plan.md",
    ):
        source = project_root / relative
        target = tmp_path / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, target)
    return tmp_path
