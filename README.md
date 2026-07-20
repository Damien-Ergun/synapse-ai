# Raman Bacteria Prototype 0

> Research prototype. Not for diagnosis, treatment decisions, hospital use, or regulatory claims.

## Mission

Build a reproducible Raman machine-learning engine for biological spectrum classification on a public bacterial Raman benchmark while maintaining explicit scientific, product, business, governance, regulatory, and IP boundaries.

The repository currently contains the Week 1 foundation only. It does not contain a dataset, preprocessing pipeline, trained model, diagnostic output, or clinical evidence.

## Current evidence level

Level 0, foundation in review. Dataset acquisition remains blocked until authoritative reuse terms are documented in `docs/governance/dataset_rights.md` and DEC-021 is superseded.

## Environment

Windows PowerShell is the canonical local shell. CPython 3.11 is supported and uv 0.11.29 is required.

```powershell
uv lock --check
uv sync --locked
uv run --locked python scripts/run_checks.py
```

The canonical runner checks the lock, environment, Git-ignore policy, documentation, tests with branch coverage, Ruff, and Black.

## Repository map

- `configs/`: controlled configuration policy.
- `data/`: policy only; spectrum arrays remain local.
- `docs/`: programme, architecture, product, business, governance, and evidence records.
- `models/`: policy only; model binaries remain local.
- `notebooks/`: exploratory-work policy.
- `reports/`: policy only; logs and generated reports remain local.
- `scripts/`: validators and evidence capture tooling.
- `src/raman_bacteria_prototype/`: installable application foundation.
- `tests/`: positive and negative foundation tests.

## Evidence limitations

- No Raman spectrum array has been downloaded or inspected in Week 1.
- No performance metric has been computed.
- No diagnostic, sepsis, treatment, antibiotic-susceptibility, hospital-readiness, or regulatory-approval claim is permitted.
- Stakeholder outreach cannot be marked complete without private sending evidence.
- Public data availability does not itself establish all reuse, redistribution, derivative-output, or commercial rights.

## Controlled documents

See `docs/programme/12_week_roadmap.md`, `docs/weekly_plans/week_1_work_plan.md`, `docs/architecture.md`, `docs/metrics_contract.md`, `docs/product/target_product_profile_v0.md`, `docs/governance/claims_register.md`, `docs/data_governance.md`, and `docs/traceability/week_1_coverage_matrix.md`.

## Contribution boundary

Do not commit credentials, private contact details, contracts, raw, interim, or processed data, model binaries, logs, generated reports, or notebook checkpoints. No public `LICENSE` is included until ownership and licensing authority are resolved.
