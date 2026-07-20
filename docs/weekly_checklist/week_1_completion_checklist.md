# Week 1 completion checklist

## Scope and entry gate

- [ ] Run `git status --short --branch` and record `EVID-W1-GIT-001`.
- [ ] Run `git fetch --prune origin` and `git ls-remote --heads origin`; record the execution-time remote state.
- [ ] Confirm or correct `origin` to `https://github.com/Damien-Ergun/synapse-ai.git`.
- [ ] Confirm the working branch is not detached and is named `main`, or record an approved reconciliation decision.
- [ ] Run `git config user.name` and `git config user.email`; confirm both values are intentional.
- [ ] Inventory every local file outside `.git/` and `.venv/` and preserve any unpushed work.
- [ ] Confirm no force-push operation will be used during Week 1.
- [ ] Confirm no secret, patient data, private contact crosswalk, contract, or confidential institutional material is inside the intended commit set.
- [ ] Record `DEC-022` permitting public publication before the first public push.

## Controlled requirements and decisions

- [ ] Create `docs/programme/12_week_roadmap.md` with source filename, SHA-256 `c993737a6b4d299e9a264bb9a5e3cb0a9105f964854adc5b14e76e42dff7d1a3`, adoption date, status, and supersession rule.
- [ ] Create `docs/weekly_plans/week_1_work_plan.md` containing the complete approved Week 1 guide.
- [ ] Create `docs/decision_log.md` before project initialization.
- [ ] Add complete `DEC-001` through `DEC-012` records before dependent implementation begins.
- [ ] Create `docs/traceability/week_1_coverage_matrix.md` and map every roadmap task, deliverable, and gate condition.
- [ ] Confirm every `DEC-*`, `RISK-*`, `CLAIM-*`, `OQ-*`, `METRIC-*`, `VAL-*`, and `EVID-*` reference resolves.

## Workstream A: Technical and scientific

- [ ] Apply the correct W1-A02 initialization case based on the existing local repository state.
- [ ] When initialization is required, run `uv init --app --package --bare --build-backend uv_build --name raman-bacteria-prototype --python 3.11 --vcs none .`.
- [ ] Create `.python-version` containing `3.11.15`.
- [ ] Create `pyproject.toml` with the exact project, build, dependency, Pytest, coverage, Ruff, Black, entry-point, and `[tool.uv]` contract from W1-A04.
- [ ] Add exact dev dependencies using `uv add --dev "pytest==9.1.1" "pytest-cov==7.1.0" "ruff==0.15.22" "black==26.5.1"`.
- [ ] Run `uv lock` intentionally during setup and review the resulting `uv.lock`.
- [ ] Create `.gitignore` with every required ignored pattern and negation.
- [ ] Create `.env.example` without values or secrets.
- [ ] Create `configs/README.md`, `data/README.md`, `models/README.md`, `notebooks/README.md`, and `reports/README.md`.
- [ ] Create `README.md` with mission, scope, research-only notice, setup, checks, structure, controlled-document links, and limitations.
- [ ] Create `src/raman_bacteria_prototype/__init__.py` with metadata-derived version exposure and no duplicated version literal.
- [ ] Create `src/raman_bacteria_prototype/cli.py`.
- [ ] Create all architecture namespaces listed in W1-A03.
- [ ] Create `docs/architecture.md` with exact package tree, allowed and prohibited dependencies, root policy, config format, canonical SHA-256 hashing, seeds, logging, exceptions, severity levels, metadata, preservation rules, artifact naming, and component status.
- [ ] Define `SplitName`, `DatasetDescriptor`, `FileManifestEntry`, `SpectrumBatch`, `ValidationIssue`, `ValidationReport`, and `QualityFlag` in `docs/architecture.md` with all required fields and invariants.
- [ ] Add `DEC-013` and `DEC-014`.
- [ ] Create `src/raman_bacteria_prototype/environment.py` and `src/raman_bacteria_prototype/checks.py`.
- [ ] Create `scripts/check_environment.py`, `scripts/check_gitignore.py`, `scripts/check_documentation.py`, and `scripts/run_checks.py`.
- [ ] Implement the exact seven-check aggregate sequence and exit-code contract from W1-A04.
- [ ] Ensure `scripts/run_checks.py` runs all mandatory checks, streams output, records every child exit code, and cannot print PASS after a failure.
- [ ] Ensure root discovery does not depend on the caller’s current working directory.
- [ ] Create `tests/conftest.py` and all seven required test modules.
- [ ] Add named tests for every positive and negative behavior listed in W1-A05.
- [ ] Verify every ignored and every trackable path individually with `git check-ignore --no-index --verbose -- <single-path>`.
- [ ] Create `.github/workflows/ci.yml` with pinned checkout commit `9c091bb21b7c1c1d1991bb908d89e4e9dddfe3e0` and pinned setup-uv commit `08807647e7069bb48b6ef5acd8ec9567f424441b`.
- [ ] Configure CI for `windows-latest` and `ubuntu-latest`, PowerShell, Python `3.11.15`, `uv` `0.11.29`, minimum permissions, locked sync, and the canonical runner.
- [ ] Create `docs/metrics_contract.md` with all thirteen roadmap metric categories and complete `METRIC-*` schemas.
- [ ] Add `DEC-017` and `DEC-018`.

## Workstream B: Product and clinical translation

- [ ] Create `docs/product/target_product_profile_v0.md` with every required section from W1-B01.
- [ ] Put the research-use-only notice before the product description.
- [ ] State the exact current Prototype 0 user, setting, controlled input, output, evidence level, and exclusions.
- [ ] Define one provisional future use-case hypothesis with population, sample type, operator, decision, comparator, reference standard, turnaround hypothesis, actions, and falsification conditions.
- [ ] Label every unsupported product field `HYPOTHESIS`.
- [ ] Create `docs/product/open_questions_register.md` with all nine roadmap questions and complete `OQ-*` records.
- [ ] Create `docs/product/evidence_ladder.md` with Levels 0 through 5, permitted claims, prohibited claims, evidence, reviewers, and exit gates.
- [ ] Mark current status `Level 0: IN_PROGRESS`.
- [ ] Add `DEC-019`.

## Workstream C: Business and investment

- [ ] Create `docs/business/company_thesis.md` and separate current evidence from future hypothesis.
- [ ] Create `docs/business/stakeholder_map.md` with all ten roadmap stakeholder categories and evidence questions.
- [ ] Create `docs/business/customer_discovery_interview_script.md` with a problem-first 30-minute interview structure.
- [ ] Create `docs/business/outreach_templates.md` with five differentiated, claim-safe templates.
- [ ] Create `docs/business/interview_record_template.md` with consent, workflow, evidence, TPP impact, risk impact, and next-action fields.
- [ ] Create `docs/business/stakeholder_outreach_log.md` using anonymous outreach IDs and the exact status vocabulary.
- [ ] Send at least five interview requests across at least three stakeholder categories.
- [ ] Map every sent request to a stakeholder hypothesis and evidence question.
- [ ] Assign one private evidence ID to each sent request and keep the identity crosswalk outside Git.
- [ ] Create `docs/business/investment_hypotheses.md` covering all ten roadmap categories with falsification conditions, owners, target weeks, and risk links.

## Workstream D: Governance, regulation and IP

- [ ] Create `docs/governance/claims_register.md` with unique `CLAIM-*` IDs and all six forbidden claim categories.
- [ ] Create `docs/data_governance.md` with exact data zones, provenance fields, retention, and split permissions.
- [ ] Explicitly prohibit Week 1 spectrum-array download or inspection.
- [ ] Create `docs/governance/privacy_and_stakeholder_data.md` with consent, no-recording default, anonymisation, retention, deletion, and prohibited-data rules.
- [ ] Add `DEC-015` and `DEC-016`.
- [ ] Create `docs/governance/risk_scoring_policy.md` with the exact 5x5 scales, score bands, and blocker rules.
- [ ] Create `docs/risk_register.md` and include every mandatory technical, clinical, privacy, cybersecurity, rights, ownership, publication, and open-source risk.
- [ ] Create `docs/risk_register_investment.md` and include every mandatory commercial and financing risk.
- [ ] Give every High or Critical residual risk an owner, treatment, indicator, review date, and blocking decision.
- [ ] Add `DEC-020`.
- [ ] Create `docs/governance/dataset_rights.md` and record the Ho et al. publication, DOI `10.1038/s41467-019-12898-9`, `csho33/bacteria-ID`, referenced host, split filenames, and current rights status.
- [ ] Search for authoritative dataset-specific terms without downloading spectrum arrays.
- [ ] If no authoritative licence or written permission is found, keep `RISK-DATA-RIGHTS-001` active, classify the record `INCOMPLETE`, set `DEC-021` to block Week 2 array acquisition, and record the escalation request.
- [ ] Generate `reports/generated/week_1/dependency_sbom.cdx.json` with `uv export --locked --all-groups --format cyclonedx1.5` when supported, or record and use the documented deterministic fallback.
- [ ] Generate `reports/generated/week_1/locked_packages.txt` with `uv tree --locked`.
- [ ] Create `docs/governance/dependency_licence_register.md` covering every direct and transitive dependency, Python, `uv`, build backend, and CI action.
- [ ] Verify each declared licence against an authoritative source.
- [ ] Create `docs/governance/toolchain_register.md`.
- [ ] Create `docs/governance/licensing_and_ownership_review.md` without committing private contracts.
- [ ] Record whether code may be privately developed, publicly published, licensed, commercially used, externally contributed, or disclosed for patent purposes.
- [ ] Set `DEC-022` only after the ownership and disclosure review supports the public action.
- [ ] Keep `LICENSE` absent unless a separate controlled decision authorizes it.

## Tests and validation

- [ ] Run `uv --version` and record `0.11.29` in `EVID-W1-ENV-001`.
- [ ] Run `uv run --locked python --version` and record `3.11.15` in `EVID-W1-ENV-001`.
- [ ] Run `uv lock --check`; retain exit code `0`.
- [ ] Run `uv sync --locked`; retain exit code `0`.
- [ ] Run `uv run --locked python scripts/check_environment.py`; retain exit code `0`.
- [ ] Run `uv run --locked python scripts/check_gitignore.py`; confirm every path has an individual PASS result.
- [ ] Run `uv run --locked python scripts/check_documentation.py`; retain exit code `0`.
- [ ] Run `uv run --locked python -m pytest -q --cov=raman_bacteria_prototype --cov-branch --cov-report=term-missing --cov-report=xml:coverage.xml --cov-fail-under=90`.
- [ ] Confirm zero test failures and branch coverage at least 90%.
- [ ] Run `uv run --locked python -m ruff check .`; retain exit code `0`.
- [ ] Run `uv run --locked python -m black --check .`; retain exit code `0`.
- [ ] Run `uv run --locked python scripts/run_checks.py`; confirm seven mandatory checks and overall exit code `0`.
- [ ] Confirm `git diff -- pyproject.toml uv.lock` is empty after validation.
- [ ] Complete and record manual claims, split, TPP, evidence-ladder, stakeholder, privacy, risk, rights, licence, and ownership reviews.

## Generated evidence

- [ ] Create `scripts/invoke_logged_command.ps1` and test success, failure, UTF-8, stdout, stderr, and child-exit preservation.
- [ ] Create `reports/logs/week_1/EVID-W1-ENV-001.txt` with command, timestamps, OS, repository-relative working directory, Git SHA, Python, `uv`, stdout, stderr, and exit code.
- [ ] Create `reports/logs/week_1/EVID-W1-CHECKS-001.txt` for the canonical aggregate command.
- [ ] After implementation push, create `reports/logs/week_1/EVID-W1-CLONE-001.txt` for the exact implementation SHA.
- [ ] Record both CI job statuses and run identifiers as `EVID-W1-CI-001`.
- [ ] Retain private sent-message evidence for the five outreach evidence IDs outside Git.
- [ ] Calculate SHA-256 for every retained local evidence log.
- [ ] Create `docs/weekly_reports/week_1_evidence_manifest.md` without private content or absolute machine paths.

## Documentation and decisions

- [ ] Run the documentation validator and resolve every missing heading, table column, duplicate ID, unresolved reference, broken link, coverage gap, and forbidden-claim context error.
- [ ] Confirm the TPP, claims register, evidence ladder, data governance, architecture, metrics, hypotheses, risks, rights, and decisions cross-link correctly.
- [ ] Record reviewer, review date, outcome, and open actions for each manual review.
- [ ] Update `docs/traceability/week_1_coverage_matrix.md` with final validation and evidence IDs.
- [ ] Create `docs/weekly_checklist/week_1_completion_checklist.md` from this checklist.

## Reproducibility and CI

- [ ] Recheck `git fetch --prune origin` and `git ls-remote --heads origin` immediately before the first push.
- [ ] Stage explicit reviewed path groups; do not run `git add .`.
- [ ] Run `git diff --cached --name-status`, `git diff --cached --check`, and `git diff --cached` before every commit.
- [ ] Perform a staged secret, privacy, contract, and data-array review.
- [ ] Create logical implementation commits and record the final implementation SHA with `git rev-parse HEAD`.
- [ ] Push implementation commits without force.
- [ ] Clone the repository into `$env:TEMP\synapse-ai-week1-verify` and check out the exact implementation SHA in detached mode.
- [ ] In the clean clone, run `uv lock --check`, `uv sync --locked`, and `uv run --locked python scripts/run_checks.py`; retain exit code `0`.
- [ ] Confirm the Windows GitHub Actions job concludes `success` for the exact implementation SHA.
- [ ] Confirm the Ubuntu GitHub Actions job concludes `success` for the exact implementation SHA.

## Completion report and Git hygiene

- [ ] Create `docs/weekly_reports/week_1_completion_report.md` only after local, clean-clone, and CI verification of the exact implementation SHA.
- [ ] Include `verified_implementation_commit_sha`, roadmap hash, tool versions, observed exit codes, evidence IDs, log hashes, rights decision, ownership decision, risk decisions, outreach evidence IDs, and Week 2 verdict.
- [ ] Do not state that the completion report contains its own commit SHA.
- [ ] Stage only the completion checklist, evidence manifest, completion report, traceability updates, and necessary status updates for the evidence commit.
- [ ] Review the staged evidence diff.
- [ ] Commit with `docs: record Week 1 verification evidence` and push without force.
- [ ] Run `git rev-parse HEAD` and supply that final report-commit SHA externally to the post-push reviewer.
- [ ] Run `git status --short --branch` and confirm a clean tree tracking `origin/main`.

## Ready for Week 2

- [ ] `docs/weekly_reports/week_1_completion_report.md` records one exact `verified_implementation_commit_sha` and does not claim its own commit SHA.
- [ ] `EVID-W1-CHECKS-001` records `uv lock --check`, `uv sync --locked`, and the canonical aggregate validator with exit code `0` for the verified implementation SHA.
- [ ] `EVID-W1-CLONE-001` records clean-clone validation of the exact verified implementation SHA with exit code `0`.
- [ ] Windows and Ubuntu GitHub Actions jobs both conclude `success` for the exact verified implementation SHA.
- [ ] `docs/weekly_reports/week_1_evidence_manifest.md` contains matching SHA-256 values for every required local evidence log.
- [ ] Every committed Week 1 artifact in the exact file-change ledger exists and passes structural validation.
- [ ] Every Week 1 roadmap task, deliverable, and gate condition has a task ID, deliverable path, validation ID, and evidence ID in `docs/traceability/week_1_coverage_matrix.md`.
- [ ] `docs/governance/claims_register.md` and the recorded claims review prove that Prototype 0 and prohibited claims are explicit.
- [ ] `docs/product/target_product_profile_v0.md` contains one reviewed, testable, falsifiable future use-case hypothesis.
- [ ] `docs/risk_register.md` and `docs/risk_register_investment.md` contain no active residual Critical risk and every active residual High risk has an explicit controlled decision.
- [ ] Five unique stakeholder requests across at least three categories have anonymous evidence IDs and matching private proof.
- [ ] No spectrum array, reserved-split performance, patient information, confidential institutional data, model, or preprocessing result was accessed or produced in Week 1.
- [ ] `DEC-022` proves that public publication of the Week 1 code and documentation was authorized before push.
- [ ] `DEC-021` explicitly permits or blocks Week 2 dataset acquisition; no acquisition proceeds while `RISK-DATA-RIGHTS-001` remains blocking.
- [ ] The final report commit is pushed, the final SHA is supplied externally to the post-push reviewer, and `git status --short --branch` is clean and tracking `origin/main`.
