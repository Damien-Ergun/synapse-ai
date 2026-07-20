"""Validate the structural contracts of committed Markdown documents."""

from __future__ import annotations

import re
import sys
from collections import Counter
from pathlib import Path

REQUIRED_DOCS: dict[str, tuple[str, ...]] = {
    "README.md": (
        "# Raman Bacteria Prototype 0",
        "## Environment",
        "## Evidence limitations",
    ),
    "docs/architecture.md": (
        "# Architecture",
        "## 9. Week 2 contract definitions",
        "### `SpectrumBatch`",
    ),
    "docs/metrics_contract.md": ("# Metric contract v0.1", "## Global rules"),
    "docs/data_governance.md": (
        "# Data governance",
        "## 3. Dataset split permissions",
    ),
    "docs/decision_log.md": ("# Decision log", "## Decisions"),
    "docs/product/target_product_profile_v0.md": (
        "# Target Product Profile v0",
        "## Falsifiable future intended-use hypothesis",
    ),
    "docs/product/evidence_ladder.md": ("# Evidence ladder",),
    "docs/governance/claims_register.md": (
        "# Claims register",
        "## Forbidden claims",
    ),
    "docs/governance/dataset_rights.md": (
        "# Dataset rights record",
        "## Authorization decision",
    ),
    "docs/governance/risk_scoring_policy.md": (
        "# Risk scoring policy",
        "## Blocker rules",
    ),
    "docs/traceability/week_1_coverage_matrix.md": ("# Week 1 coverage matrix",),
    "docs/weekly_checklist/week_1_completion_checklist.md": (
        "# Week 1 completion checklist",
        "## Ready for Week 2",
    ),
}
ID_PATTERNS = {
    "DEC": re.compile(r"\bDEC-\d{3}\b"),
    "CLAIM": re.compile(r"\bCLAIM-\d{3}\b"),
    "RISK": re.compile(r"\bRISK-[TI]\d{3}\b"),
    "OQ": re.compile(r"\bOQ-\d{3}\b"),
    "HYP": re.compile(r"\bHYP-\d{3}\b"),
    "METRIC": re.compile(r"\bMETRIC-\d{3}\b"),
}
DEFINITION_PATHS = {
    "DEC": ("docs/decision_log.md",),
    "CLAIM": ("docs/governance/claims_register.md",),
    "RISK": ("docs/risk_register.md", "docs/risk_register_investment.md"),
    "OQ": ("docs/product/open_questions_register.md",),
    "HYP": ("docs/business/investment_hypotheses.md",),
    "METRIC": ("docs/metrics_contract.md",),
}
LINK_PATTERN = re.compile(r"\[[^]]+\]\(([^)]+)\)")


def root() -> Path:
    """Return the repository root from this script's location."""
    return Path(__file__).resolve().parents[1]


def markdown_files(project_root: Path) -> list[Path]:
    """Return all committed Markdown contract files."""
    return [
        project_root / "README.md",
        *sorted((project_root / "docs").rglob("*.md")),
    ]


def table_definition_ids(text: str, pattern: re.Pattern[str]) -> list[str]:
    """Extract IDs defined in the first cell of a Markdown table row."""
    definitions: list[str] = []
    for line in text.splitlines():
        if not line.lstrip().startswith("|"):
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if not cells:
            continue
        match = pattern.fullmatch(cells[0].strip("`"))
        if match:
            definitions.append(match.group(0))
    return definitions


def validate(project_root: Path | None = None) -> list[str]:
    """Return every structural documentation error."""
    resolved_root = (project_root or root()).resolve()
    errors: list[str] = []
    for relative, headings in REQUIRED_DOCS.items():
        path = resolved_root / relative
        if not path.is_file():
            errors.append(f"Missing required document: {relative}")
            continue
        text = path.read_text(encoding="utf-8")
        for heading in headings:
            if heading not in text:
                errors.append(f"Missing heading in {relative}: {heading}")

    all_text = "\n".join(
        path.read_text(encoding="utf-8")
        for path in markdown_files(resolved_root)
        if path.is_file()
    )
    for kind, pattern in ID_PATTERNS.items():
        definitions: list[str] = []
        for relative in DEFINITION_PATHS[kind]:
            definitions.extend(
                table_definition_ids(
                    (resolved_root / relative).read_text(encoding="utf-8"),
                    pattern,
                )
            )
        duplicates = [
            identifier
            for identifier, count in Counter(definitions).items()
            if count > 1
        ]
        if duplicates:
            errors.append(
                f"Duplicate {kind} definitions: {', '.join(sorted(duplicates))}"
            )
        defined = set(definitions)
        referenced = set(pattern.findall(all_text))
        missing = sorted(referenced - defined)
        if missing:
            errors.append(f"Unresolved {kind} references: {', '.join(missing)}")

    for path in markdown_files(resolved_root):
        if not path.is_file():
            continue
        text = path.read_text(encoding="utf-8")
        for target in LINK_PATTERN.findall(text):
            if target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            clean = target.split("#", 1)[0]
            if clean and not (path.parent / clean).resolve().exists():
                errors.append(
                    f"Broken link in {path.relative_to(resolved_root)}: {target}"
                )

    matrix = resolved_root / "docs/traceability/week_1_coverage_matrix.md"
    if matrix.is_file():
        text = matrix.read_text(encoding="utf-8")
        for prefix in (
            "REQ-W1-A",
            "REQ-W1-B",
            "REQ-W1-C",
            "REQ-W1-D",
            "REQ-W1-G",
        ):
            if prefix not in text:
                errors.append(f"Coverage matrix lacks workstream/gate prefix: {prefix}")
    return errors


def main() -> int:
    """Run documentation validation as a CLI."""
    errors = validate()
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print("Documentation contracts: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
