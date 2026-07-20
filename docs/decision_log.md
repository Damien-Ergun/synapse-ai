# Decision log

## Status vocabulary

`PROPOSED`, `ACTIVE`, `SUPERSEDED`, `REJECTED`, and `CLOSED` are the only statuses.

## Decisions

| Decision ID | Status | Decision | Consequence |
|---|---|---|---|
| DEC-001 | ACTIVE | Distribution `raman-bacteria-prototype`, import `raman_bacteria_prototype`. | Packaging and imports use these names. |
| DEC-002 | ACTIVE | Use a packaged application with a `src` layout. | No library-template `py.typed` marker is expected. |
| DEC-003 | ACTIVE | Support Python `>=3.11,<3.12`, evidence target 3.11.15. | CI and local evidence record the patch. |
| DEC-004 | ACTIVE | Require uv 0.11.29. | Validation uses `uv lock --check`, `uv sync --locked`, and locked runs. |
| DEC-005 | ACTIVE | Use `uv_build>=0.11.29,<0.12`. | Build metadata is centralized. |
| DEC-006 | ACTIVE | Keep data, models, logs, generated reports, secrets, contracts, and private crosswalks outside Git. | Only policies and sanitised manifests are committed. |
| DEC-007 | ACTIVE | Use `scripts/run_checks.py`; no Makefile in Week 1. | One PowerShell-compatible command is canonical. |
| DEC-008 | ACTIVE | Enforce split roles in `docs/data_governance.md`. | Reserved splits cannot influence development. |
| DEC-009 | ACTIVE | All Week 1 outputs are research-use-only. | Diagnostic language is prohibited. |
| DEC-010 | ACTIVE | Do not add a public `LICENSE` until ownership authority is confirmed. | Public visibility is not an open-source licence grant. |
| DEC-011 | ACTIVE | Run CI on Windows and Ubuntu with PowerShell. | Primary environment and portability are checked. |
| DEC-012 | ACTIVE | Verify an implementation commit, then create a separate evidence commit. | Completion reporting is non-circular. |
| DEC-013 | ACTIVE | Use the module tree and dependency directions in `docs/architecture.md`. | Week 2 does not invent package boundaries. |
| DEC-014 | ACTIVE | Use canonical UTF-8 JSON and SHA-256 for future configuration identity. | Hashes are cross-platform and versioned. |
| DEC-015 | ACTIVE | Commit anonymous stakeholder metadata only. | Contact details and message evidence remain private. |
| DEC-016 | ACTIVE | Use the 5x5 inherent and residual risk policy. | Blocker rules are explicit. |
| DEC-017 | ACTIVE | Use the exact seven-step aggregate validator. | Lock, environment, ignore, docs, tests, Ruff, and Black share one gate. |
| DEC-018 | ACTIVE | Automate document paths, headings, IDs, references, and relative links. | Manual judgment remains separately recorded. |
| DEC-019 | ACTIVE | Adopt metric contract v0.1 before model development. | Evaluation definitions are predeclared. |
| DEC-020 | ACTIVE | Do not download or inspect spectrum arrays in Week 1. | Rights review remains separate from data access. |
| DEC-021 | ACTIVE | Dataset acquisition is blocked until authoritative dataset terms or written permission are retained. | Week 2 array access cannot start yet. |
| DEC-022 | ACTIVE | A public review branch may contain original sanitised Week 1 material only, with no licence grant or private evidence. | Main remains untouched pending review. |
