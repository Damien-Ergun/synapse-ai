from __future__ import annotations

import importlib.util
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
