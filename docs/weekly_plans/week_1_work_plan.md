# Week 1 Work Plan, controlled execution baseline

Source roadmap SHA-256: `c993737a6b4d299e9a264bb9a5e3cb0a9105f964854adc5b14e76e42dff7d1a3`

## Objective

Implement the complete Week 1 foundation across technical, product, business, and governance workstreams on a review branch without touching `main`.

## Task sequence

1. `W1-A01`: inspect local and remote Git state and preserve unpushed work.
2. `W1-A02`: initialize the packaged Python 3.11 application with pinned uv, locked dependencies, policies, and controlled documents.
3. `W1-A03`: define architecture boundaries and Week 2 data contracts.
4. `W1-D01`: establish decision-log format before foundational choices.
5. `W1-D02`: define claims, split discipline, privacy, and generated-artifact boundaries.
6. `W1-A04`: implement the seven-step locked aggregate validator.
7. `W1-A05`: implement positive and negative tests with at least 90 percent branch coverage.
8. `W1-A06`: add pinned Windows and Ubuntu CI.
9. `W1-A07`: adopt metric contract v0.1.
10. `W1-B01` and `W1-B02`: create TPP v0, open questions, and evidence ladder.
11. `W1-C01` to `W1-C03`: create company thesis, stakeholder map, outreach materials, and investment hypotheses.
12. `W1-D03` and `W1-D04`: create risk, rights, licensing, ownership, and evidence controls.
13. `W1-D05`: verify an implementation commit, then add a separate evidence report commit.

## Validation contract

The canonical command is `uv run --locked python scripts/run_checks.py`. It runs `uv lock --check`, environment validation, per-path Git-ignore validation, documentation validation, Pytest with branch coverage enforcement, Ruff, and Black. The same command runs locally, from a clean checkout, and in both CI operating systems.

## Completion boundary

Five stakeholder requests cannot be checked off without private sending evidence. Dataset arrays cannot be downloaded until DEC-021 is superseded. No spectrum array, preprocessing pipeline, model, test result, clinical-split result, or diagnostic claim belongs to Week 1.
