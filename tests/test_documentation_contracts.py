from __future__ import annotations

import importlib.util
import shutil
from pathlib import Path

import pytest


def load_checker(project_root: Path):
    path = project_root / "scripts/check_documentation.py"
    spec = importlib.util.spec_from_file_location("check_documentation", path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


@pytest.mark.integration
def test_documentation_contracts_pass(project_root: Path) -> None:
    checker = load_checker(project_root)
    assert checker.validate() == []


@pytest.mark.integration
def test_missing_definition_document_returns_structured_failure(
    project_root: Path,
    tmp_path: Path,
    capsys: pytest.CaptureFixture[str],
) -> None:
    repo_copy = tmp_path / "repo"

    shutil.copytree(
        project_root,
        repo_copy,
        ignore=shutil.ignore_patterns(
            ".git",
            ".venv",
            "__pycache__",
            ".pytest_cache",
            ".ruff_cache",
            "logs",
            "generated",
        ),
    )

    missing_relative = "docs/product/open_questions_register.md"
    missing_document = repo_copy / missing_relative

    assert missing_document.is_file()
    missing_document.unlink()

    checker = load_checker(repo_copy)

    assert checker.main() == 1

    captured = capsys.readouterr()

    assert f"Missing definition document for OQ: {missing_relative}" in captured.err
    assert "Traceback" not in captured.err


@pytest.mark.unit
def test_required_identifiers_exist(project_root: Path) -> None:
    decisions = (project_root / "docs/decision_log.md").read_text(encoding="utf-8")
    assert all(f"DEC-{number:03d}" in decisions for number in range(1, 23))
    claims = (project_root / "docs/governance/claims_register.md").read_text(
        encoding="utf-8"
    )
    assert all(
        identifier in claims
        for identifier in (
            "CLAIM-101",
            "CLAIM-102",
            "CLAIM-103",
            "CLAIM-104",
            "CLAIM-105",
            "CLAIM-106",
        )
    )


@pytest.mark.unit
def test_architecture_statuses_do_not_claim_scientific_implementation(
    project_root: Path,
) -> None:
    text = (project_root / "docs/architecture.md").read_text(encoding="utf-8")
    for package in ("Data loading", "Spectral QC", "Preprocessing", "Modelling"):
        line = next(line for line in text.splitlines() if f"| {package} |" in line)
        assert "IMPLEMENTED" not in line
