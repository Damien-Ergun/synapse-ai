from __future__ import annotations

import importlib.util
from pathlib import Path

import pytest


def load_checker(project_root: Path):
    path = project_root / "scripts/check_gitignore.py"
    spec = importlib.util.spec_from_file_location("check_gitignore", path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


@pytest.mark.integration
def test_every_expected_ignored_path(project_root: Path) -> None:
    checker = load_checker(project_root)
    for path in checker.IGNORED:
        ignored, _ = checker.is_ignored(project_root, path)
        assert ignored, path


@pytest.mark.integration
def test_every_policy_file_is_trackable(project_root: Path) -> None:
    checker = load_checker(project_root)
    for path in checker.TRACKABLE:
        ignored, _ = checker.is_ignored(project_root, path)
        assert not ignored, path
