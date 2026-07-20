# Week 1 Work Plan

Document status: **CONTROLLED DRAFT FOR EXECUTION**  
Target week: **1**  
Previous week: **0, not applicable**  
Next week: **2**  
Repository: `https://github.com/Damien-Ergun/synapse-ai`  
Default branch: `main`  
Canonical local environment: Windows PowerShell, CPython 3.11.15, `uv` 0.11.29  
Roadmap source: `12-week-Roadmap.txt`  
Roadmap SHA-256: `c993737a6b4d299e9a264bb9a5e3cb0a9105f964854adc5b14e76e42dff7d1a3`  
Roadmap adoption date: 20 July 2026  
Review source SHA-256: `5ed2764f5916c56ecb81e462a672a88f80492ba53ffb4e5542b03fad95217c72`  
Supersession rule: this plan is superseded only by a later committed plan that identifies this document, states the reason for change, and records the approving decision ID.

## 1. Executive verdict

Week 1 remains a genuine greenfield foundation week.

The GitHub repository was re-inspected on 20 July 2026. It exists, is public, and declares `main` as the default branch, but GitHub reports repository size `0` and no commit can be listed. There is therefore no GitHub branch ref, latest commit SHA, source tree, checklist, report, configuration, automation, test, notebook, model, or committed artifact to preserve in the inspected remote revision.

That observation is time-bounded. It must be rechecked from the local machine immediately before initialization and immediately before the first push. An empty remote does not prove that the local directory is empty, and it does not guarantee that the remote will remain empty.

The Week 1 execution strategy is:

1. Preserve any local or newly created remote work before initialization.
2. Create the decision and traceability system before making foundational choices.
3. Initialize a deterministic **packaged application**, not a distributable library.
4. Pin CPython 3.11.15 and `uv` 0.11.29.
5. Use `uv lock --check`, `uv sync --locked`, and `uv run --locked` for validation.
6. Add one canonical aggregate validator, negative tests for that validator, structural documentation checks, and GitHub Actions CI.
7. Commit the controlled roadmap and this complete Week 1 work plan.
8. Produce product, clinical, business, governance, regulatory, rights, and IP evidence alongside the technical foundation.
9. Verify one exact implementation commit from a clean clone.
10. Commit the completion report and evidence manifest separately, avoiding commit self-reference.

A known governance risk is already visible. The intended Ho et al. bacterial Raman dataset is identifiable and publicly downloadable, but the official data location does not state a dataset-specific licence. The source repository has an MIT licence for software, while the array files are distributed through an external Dropbox location. Until an authoritative dataset licence or written permission is retained, dataset acquisition is blocked. Week 1 code and documentation may proceed, but Week 2 may not download or inspect the spectrum arrays.

## 2. Week 1 objective

Create the project foundation and define exactly:

1. What Prototype 0 is building.
2. What Prototype 0 does not establish.
3. Which future clinical decision is being investigated as a hypothesis.
4. How software, configuration, data, evidence, and decisions will be structured.
5. Which metrics will govern later model evaluation.
6. Which claims are allowed and forbidden.
7. Which technical, scientific, clinical, business, privacy, regulatory, ownership, licensing, and IP risks block progress.
8. How every Week 1 result will be tested, recorded, committed, and independently rechecked.

The target outcome is a repository that can be installed and validated from a clean checkout, with a green local gate, a green CI gate, explicit evidence boundaries, five verifiable stakeholder interview requests, and no unresolved blocker preventing the lawful start of Week 2.

## 3. Roadmap requirements

### 3.1 Controlled roadmap version

The active roadmap is the uploaded `12-week-Roadmap.txt`, SHA-256 `c993737a6b4d299e9a264bb9a5e3cb0a9105f964854adc5b14e76e42dff7d1a3`.

Week 1 must commit a controlled copy to:

```text
docs/programme/12_week_roadmap.md
```

The committed copy must include a control header containing:

| Field | Required value |
|---|---|
| `source_filename` | `12-week-Roadmap.txt` |
| `source_sha256` | `c993737a6b4d299e9a264bb9a5e3cb0a9105f964854adc5b14e76e42dff7d1a3` |
| `adopted_on` | `2026-07-20` |
| `status` | `ACTIVE` |
| `supersedes` | `NONE` |
| `supersession_rule` | Later controlled roadmap must identify the prior hash and approval decision |

The final revised plan must be committed unchanged, apart from repository-local metadata fields that are explicitly marked as fillable, to:

```text
docs/weekly_plans/week_1_work_plan.md
```

### 3.2 Week 1 objective from the roadmap

Create the project foundation and define exactly what is being built, what is not being built, and which future clinical decision the platform could eventually support.

### 3.3 Workstream A: Technical and scientific

Required Week 1 work:

- Create `configs/`, `data/`, `docs/`, `models/`, `notebooks/`, `reports/`, `scripts/`, `src/`, and `tests/`.
- Create `pyproject.toml`, `uv.lock`, `.python-version`, `.gitignore`, and `README.md`.
- Use Python 3.11 and `uv`.
- Add environment validation, Pytest, Ruff, and Black.
- Define package architecture for data loading, data validation, spectral quality control, preprocessing, features, modelling, calibration, evaluation, reporting, prediction, and experiment tracking.
- Define the initial metric contract.
- Demonstrate local, clean-clone, and repository-hosted validation.

### 3.4 Workstream B: Product and clinical translation

Required Week 1 work:

- Create `docs/product/target_product_profile_v0.md`.
- Define user, setting, controlled Raman input, Prototype 0 output, future direction, and research-only status.
- Record all open clinical and workflow questions.
- Define one testable future intended-use hypothesis.
- Create the six-level evidence ladder.
- Define what evidence is required before any clinical, diagnostic, treatment, hospital-readiness, or regulatory claim.

### 3.5 Workstream C: Business and investment

Required Week 1 work:

- Write the one-sentence company thesis.
- Build the initial stakeholder map.
- Create a problem-first interview script.
- Create `docs/business/investment_hypotheses.md` covering problem, user, buyer, value, workflow, alternatives, costs, barriers, regulatory dependency, and clinical-data dependency.
- Send at least five interview requests.
- Preserve privacy-safe evidence that each request was sent.

### 3.6 Workstream D: Governance, regulation and IP

Required Week 1 work:

- Define allowed and forbidden claims.
- Create the technical risk register.
- Create the investment risk register.
- Create the decision log before architectural decisions are made.
- Create the data-governance policy.
- Review all direct and transitive dependency licences.
- Identify the intended dataset and determine its access and reuse conditions.
- Review code ownership, publication obligations, employer or institutional rights, and patent-disclosure risk.
- Establish privacy-safe stakeholder evidence handling.

### 3.7 Week 1 deliverables

- Clean repository.
- Passing local base checks.
- Passing GitHub Actions CI.
- README.
- Architecture document and Week 2 core contracts.
- Initial metric contract.
- Target Product Profile v0.
- Evidence ladder.
- Claims register.
- Technical risk register.
- Investment risk register.
- Customer-discovery script.
- Outreach templates.
- Interview-record template.
- Initial stakeholder map.
- Five sent interview requests with evidence IDs.
- Controlled roadmap.
- Controlled Week 1 work plan.
- Dependency licence register.
- Dataset-rights record.
- Code-ownership record.
- Decision log.
- Evidence manifest.
- Week 1 completion report.

### 3.8 Week 1 gate

Week 1 is complete only when:

1. The repository installs and tests from a clean checkout of the exact verified implementation SHA.
2. Local validation returns exit code `0`.
3. CI returns success for the exact verified implementation SHA.
4. Prototype and non-prototype claims are explicit.
5. The future use case is testable and falsifiable.
6. Major technical, scientific, clinical, commercial, privacy, licensing, ownership, regulatory, and IP risks are visible.
7. At least five stakeholder interviews have been requested and mapped to evidence questions.
8. The authoritative dataset-rights record permits the exact Week 2 acquisition action.
9. No active blocking risk remains.

### 3.9 Week 0 gate

`PREVIOUS_WEEK = 0`. No Week 0 objective, deliverable, or gate exists. Its status is `NOT_APPLICABLE`.

### 3.10 Week 2 objective and boundary

Week 2 will build the trustworthy dataset layer and begin external problem validation.

Week 1 must prepare:

- controlled package and path contracts;
- data storage and split rules;
- dataset identity and lawful-use evidence;
- validation issue and manifest schemas;
- automated checks;
- outreach and interview records.

Week 1 must not:

- download or inspect spectrum arrays;
- derive split contents;
- implement the data loader;
- implement spectral quality-control algorithms;
- preprocess spectra;
- train models;
- inspect test or clinical performance.

## 4. Repository snapshot

### 4.1 Time-bounded remote inspection

| Field | Inspected value | Evidence label | Completion status |
|---|---|---|---|
| Repository | `Damien-Ergun/synapse-ai` | `VERIFIED_IN_REPOSITORY` | Exists |
| Visibility | Public | `VERIFIED_IN_REPOSITORY` | Existing setting |
| Configured default branch | `main` | `VERIFIED_IN_REPOSITORY` | Configured only |
| Actual `main` ref | No ref returned because repository has no commits | `VERIFIED_IN_REPOSITORY` | Missing ref |
| Latest commit SHA | None | `VERIFIED_IN_REPOSITORY` | `MISSING` |
| Latest commit date | None | `VERIFIED_IN_REPOSITORY` | `MISSING` |
| Repository size | `0` | `VERIFIED_IN_REPOSITORY` | Empty remote |
| Inspection date | `2026-07-20` | `VERIFIED_IN_REPOSITORY` | Recorded |

### 4.2 Requested paths

Every committed path requested in the original work-plan prompt is currently `MISSING` in the inspected remote revision because no commit exists.

| Path or category | Evidence label | Completion status |
|---|---|---|
| `README.md` | `MISSING` | Not committed |
| `pyproject.toml` | `MISSING` | Not committed |
| `uv.lock` | `MISSING` | Not committed |
| `.python-version` | `MISSING` | Not committed |
| `.gitignore` | `MISSING` | Not committed |
| `.github/workflows/ci.yml` | `MISSING` | Not committed |
| `Makefile` | `MISSING` | Intentionally not required in Week 1 |
| `configs/`, `docs/`, `scripts/`, `src/`, `tests/`, `notebooks/` | `MISSING` | Not committed |
| `data/`, `models/`, `reports/` policy files | `MISSING` | Not committed |
| Previous-week checklist | `NOT_APPLICABLE` | No Week 0 |
| Existing Week 1 checklist | `MISSING` | Not committed |
| Previous weekly reports | `NOT_APPLICABLE` | No prior week |
| Existing implementation | `MISSING` | No remote implementation |
| Local working tree | `LOCAL_ONLY_NOT_INSPECTABLE` | Must be audited before initialization |

### 4.3 Snapshot validity rule

The empty-repository diagnosis is evidence about the remote on 20 July 2026 only. Before initialization and again before push, run:

```powershell
git ls-remote --heads origin
git fetch --prune origin
```

If any remote branch appears, the greenfield instructions cease to apply. Fetch and inspect the remote state before creating or pushing files.

## 5. Evidence and inspection limits

### 5.1 Permitted evidence labels

Only the following labels may be used in plans, checklists, reports, risk records, and evidence manifests:

| Label | Exact use |
|---|---|
| `VERIFIED_IN_REPOSITORY` | Directly inspected in the current repository revision |
| `VERIFIED_FROM_USER_OUTPUT` | Demonstrated by user-provided terminal output, logs, screenshots, tables, or figures |
| `DECLARED_BUT_NOT_VERIFIED` | An actual document, checklist, report, or user statement claims completion but the underlying evidence was not inspected |
| `LOCAL_ONLY_NOT_INSPECTABLE` | May exist locally but cannot be inspected through the repository |
| `MISSING` | A required committed artifact or required evidence does not exist after reasonable search |
| `INCOMPLETE` | An inspected artifact exists but does not satisfy its stated contract |
| `CONFLICTING_EVIDENCE` | Inspected sources disagree |
| `NOT_APPLICABLE` | The requirement does not apply |

Evidence label and completion status must be separate fields. Use only the approved evidence labels in the evidence-label column.

### 5.2 Required inaccessible evidence

| Required item | Exact path or evidence requested | Why needed | What must be checked | Evidence label now | Blocking scope | Simplest provision method |
|---|---|---|---|---|---|---|
| Local Git state | Output of `git status --short --branch`, `git remote -v`, guarded `git log`, `git ls-remote --heads origin` | Prevent overwrite and stale remote assumptions | Branch, detached HEAD, history, local files, remote refs | `LOCAL_ONLY_NOT_INSPECTABLE` | Blocks initialization | Save as `EVID-W1-A01-PREFLIGHT` |
| Local file inventory | UTF-8 recursive file listing excluding `.git`, `.venv`, caches | Determine create versus modify actions | Existing source, docs, generated output, private files | `LOCAL_ONLY_NOT_INSPECTABLE` | Blocks initialization | Save inventory log |
| Git identity | `git config user.name` and `git config user.email` | First commit must be attributable | Non-empty values, no unintended work identity | `LOCAL_ONLY_NOT_INSPECTABLE` | Blocks first commit | Save preflight output |
| Local validation | Logged canonical aggregate command | Proves technical gate | SHA, command, OS, Python, uv, exit codes, output | `MISSING` | Blocks implementation verification | Generate `EVID-W1-A05-LOCAL` |
| Clean-clone validation | Logged validation of exact implementation SHA | Proves scratch reproducibility | Detached checkout of exact SHA, locked sync, checks | `MISSING` | Blocks Week 1 gate | Generate `EVID-W1-D05-CLEAN-CLONE` |
| CI result | GitHub Actions run for exact implementation SHA | Repository-hosted automation | Both OS jobs green, exact SHA | `MISSING` | Blocks Week 1 gate | Record run URL and status in manifest |
| Five outreach requests | Public sanitised tracker plus private evidence crosswalk | Proves business gate | Five unique requests, dates, roles, questions, evidence IDs | `LOCAL_ONLY_NOT_INSPECTABLE` | Blocks Workstream C gate | Retain private evidence outside Git |
| Dataset reuse permission | Dataset-specific licence or written rights-holder confirmation | Determines whether Week 2 can download arrays | Research use, redistribution, derivatives, commercial use, attribution | `INCOMPLETE` | Blocks Week 2 acquisition | Retain authoritative terms or written permission |
| Code ownership | Relevant contract clauses or written institutional guidance | Determines whether code may be publicly committed and licensed | Employer, university, internship, funding, publication, patent rights | `LOCAL_ONLY_NOT_INSPECTABLE` | May block public push | Record a sanitised conclusion and retain private evidence |
| Dependency licences | Locked package list plus authoritative licence checks | Governance and future distribution | Direct, transitive, runtime, dev, Python, uv, actions | `MISSING` | Blocks governance completion | Generate provisional SBOM and licence register |

### 5.3 Dataset identity already established

The intended public benchmark is:

- Title: **Rapid identification of pathogenic bacteria using Raman spectroscopy and deep learning**.
- Authors: Chi-Sing Ho, Neal Jean, Catherine A. Hogan, Lena Blackmon, Stefanie S. Jeffrey, Mark Holodniy, Niaz Banaei, Amr A. E. Saleh, Stefano Ermon, and Jennifer Dionne.
- Publication: *Nature Communications*, volume 10, article 4927, 2019.
- DOI: `10.1038/s41467-019-12898-9`.
- Official article data-availability statement: all data needed to replicate the results are available through `https://github.com/csho33/bacteria-ID`.
- Official source repository: `csho33/bacteria-ID`.
- Repository data link: external Dropbox folder referenced by the official README.
- Named arrays visible in the official README include `X_finetune.npy`, `y_finetune.npy`, `X_test.npy`, `y_test.npy`, `X_2018clinical.npy`, `y_2018clinical.npy`, `X_2019clinical.npy`, and `y_2019clinical.npy`.
- Official source repository software licence: MIT.
- Dataset-specific licence: not found in the article data-availability statement, repository README, or external data landing page inspected for this plan.

Current rights status: `INCOMPLETE`.

The MIT software licence must not be assumed to license externally hosted arrays. The article's Creative Commons licence must not be assumed to determine the dataset licence. Week 1 may inspect the publication, README, file names, repository metadata, and rights documentation. It may not download or open the arrays until `DATA-RIGHTS-001` is resolved.

## 6. Week 0 continuity audit

| Previous-week requirement | Evidence found | Evidence label | Completion status | Blocks Week 1? | Required action |
|---|---|---|---|---|---|
| Week 0 objective | No Week 0 in roadmap | `NOT_APPLICABLE` | Not applicable | No | None |
| Week 0 technical gate | No Week 0 gate | `NOT_APPLICABLE` | Not applicable | No | None |
| Week 0 product gate | No Week 0 gate | `NOT_APPLICABLE` | Not applicable | No | None |
| Week 0 business gate | No Week 0 gate | `NOT_APPLICABLE` | Not applicable | No | None |
| Week 0 governance gate | No Week 0 gate | `NOT_APPLICABLE` | Not applicable | No | None |
| Existing local project work | Not inspectable remotely | `LOCAL_ONLY_NOT_INSPECTABLE` | Unknown until preflight | Yes, initialization only | Complete W1-A01 |

There is no previous-week work to carry forward. The only continuity requirement is preservation and classification of any local work.

## 7. Entry gate for Week 1

No file-creation task may start until all entry conditions below pass.

### 7.1 Repository-location and local-state checks

Run from the intended repository directory:

```powershell
$ErrorActionPreference = "Stop"

Get-Location
Test-Path ".git"
Get-ChildItem -Force

if (Test-Path ".git") {
    git status --short --branch
    git remote -v

    $hasHead = git rev-parse --verify HEAD 2>$null
    if ($LASTEXITCODE -eq 0) {
        git log -5 --oneline --decorate
    }
    else {
        Write-Output "LOCAL_HEAD_STATUS=UNBORN"
    }
}

Get-ChildItem -Recurse -File -Force |
    Where-Object {
        $_.FullName -notmatch '\\.git\\' -and
        $_.FullName -notmatch '\\.venv\\' -and
        $_.FullName -notmatch '\\__pycache__\\'
    } |
    Sort-Object FullName |
    Select-Object -ExpandProperty FullName
```

### 7.2 Remote-state checks

If `.git` exists and `origin` is configured:

```powershell
git ls-remote --heads origin
git fetch --prune origin
```

Decision rule:

- No remote heads: proceed with greenfield flow.
- `origin/main` exists: switch to or create a local tracking branch, inspect it, and rebuild this plan against that revision before proceeding.
- Another remote branch exists: inspect it and decide through a recorded decision whether it is relevant.
- Push rejected because remote changed: do not force push. Fetch, inspect, reconcile, rerun validation, and create a new verified implementation SHA.

### 7.3 Git-state normalization

If no Git repository exists:

```powershell
git init -b main
```

If Git exists and HEAD is detached:

```powershell
$mainExists = git show-ref --verify --quiet refs/heads/main
if ($LASTEXITCODE -eq 0) {
    git switch main
}
else {
    git switch -c main
}
```

If a local branch exists under another name and `main` does not exist:

```powershell
git branch -M main
```

If `origin` is absent:

```powershell
git remote add origin https://github.com/Damien-Ergun/synapse-ai.git
```

If `origin` is incorrect:

```powershell
git remote set-url origin https://github.com/Damien-Ergun/synapse-ai.git
```

### 7.4 Git identity checks

```powershell
git config user.name
git config user.email
```

Both must return intended non-empty values. Do not silently reuse an employer identity if the project is personal.

### 7.5 Privacy and ownership preconditions

Before public push:

- no secret, credential, `.env`, private contract, private contact crosswalk, patient information, or confidential institutional material may be staged;
- `OWNERSHIP-001` must conclude that public publication of original Week 1 code and documentation is permitted;
- `DISCLOSURE-001` must record whether public disclosure creates a patent or publication risk;
- unresolved ownership that creates a credible third-party claim blocks the public push;
- unresolved dataset rights do not block code foundation work, but block Week 2 data acquisition.

## 8. Gaps, conflicts and blockers

| ID | Gap or conflict | Affected evidence or path | Practical consequence | Resolution | Week 1 owner | Blocking rule |
|---|---|---|---|---|---|---|
| GAP-001 | Remote is empty but local work may exist | Entire local tree | Initialization may overwrite work | Complete W1-A01 inventory and backup | W1-A01 | Blocks initialization |
| GAP-002 | Remote snapshot may become stale | Git refs | First push may conflict | Recheck remote before initialization and push | W1-A01, W1-D05 | Blocks push until reconciled |
| GAP-003 | Repository name and import name differ | `pyproject.toml`, package | Import and metadata ambiguity | Distribution `raman-bacteria-prototype`, import `raman_bacteria_prototype` | W1-D01 | Must be recorded before init |
| GAP-004 | Project template previously undecided | Project structure | Agent could create wrong generated files | Select packaged application, not library | W1-D01, W1-A02 | Blocks init until decision exists |
| GAP-005 | Validation previously used `--frozen` incorrectly | All validation | Lock drift could pass unnoticed | Use `uv lock --check`, `uv sync --locked`, `uv run --locked` | W1-A04 | Blocks technical gate |
| GAP-006 | Completion report could self-reference | Completion sequence | Impossible clean state in one commit | Separate implementation verification and evidence commit | W1-D05 | Blocks finalization |
| GAP-007 | No controlled roadmap or work plan in repo | `docs/programme/`, `docs/weekly_plans/` | Later review loses requirements | Commit both controlled documents | W1-D01 | Blocks traceability gate |
| GAP-008 | No repository-hosted CI | `.github/workflows/ci.yml` | Local output is sole automation evidence | Add pinned Windows and Ubuntu CI | W1-A06 | Blocks Week 1 gate |
| GAP-009 | Dataset-specific licence not found | `docs/governance/dataset_rights.md` | Lawful reuse scope is unclear | Obtain authoritative licence or written permission | W1-D04 | Blocks Week 2 acquisition |
| GAP-010 | Code ownership and disclosure risk not yet known | `docs/governance/licensing_and_ownership_review.md` | Public push may create contractual or IP risk | Review relevant clauses and record conclusion | W1-D04 | May block public push |
| GAP-011 | Generic `validation` namespace is ambiguous | Architecture | Week 2 could mix data and model validation | Use `data_validation` for dataset integrity | W1-A03 | Must resolve before scaffold |
| GAP-012 | Manual document review alone is insufficient | All Markdown deliverables | Missing headings and broken IDs may go unnoticed | Add structural documentation validator | W1-A05 | Blocks aggregate gate |
| GAP-013 | Ignored-path test previously proved only one match | `.gitignore` | Sensitive path may remain trackable | Check every ignored and every negated path separately | W1-A05 | Blocks Git hygiene |
| GAP-014 | Dependency tree is not a licence register | Governance | Transitive obligations could be omitted | Generate SBOM, inspect every component, verify authoritative licences | W1-D04 | Blocks governance completion |
| GAP-015 | Outreach handling was under-specified | Business and privacy docs | Confirmation bias or privacy leakage | Add templates, consent, retention, anonymisation, and statuses | W1-C02 | Blocks outreach gate |
| GAP-016 | Risk scoring and blocker logic were vague | Risk registers | Readiness could be asserted without controlled risk decisions | Use exact 5x5 scoring and explicit blocker rules | W1-D03 | Blocks readiness verdict |


## 9. Step-by-step work plan

The tasks are ordered by dependency. A task may not be marked complete merely because its files exist. Its validation and acceptance criteria must also pass.

### Phase 0: Preserve state and establish controlled requirements

### W1-A01: Audit the local and remote Git state

**Purpose**

Prevent loss of unpushed work, detect remote changes since the inspection snapshot, and establish a safe basis for initialization.

**Roadmap requirement, risk, or gate satisfied**

- Clean repository foundation.
- GAP-001 and GAP-002.
- Git hygiene and reproducibility prerequisites.

**Preconditions**

- Access to the intended local project directory.
- Git installed.
- Network access to GitHub.

**Current state**

| Statement | Evidence label | Completion status |
|---|---|---|
| GitHub repository existed and was empty at the inspection time | `VERIFIED_IN_REPOSITORY` | Snapshot only |
| Current remote refs at execution time | `LOCAL_ONLY_NOT_INSPECTABLE` | Not yet checked |
| Existing local files and Git history | `LOCAL_ONLY_NOT_INSPECTABLE` | Not yet checked |

**Exact files**

Create:

- none before the audit.

Modify:

- local Git configuration only if the remote, branch, or author identity is wrong.

Inspect only:

- local working tree;
- `.git/` metadata;
- current branches;
- remote refs;
- Git author identity.

Generated locally:

- `reports/logs/week_1/EVID-W1-GIT-001-preflight.txt`, after the logging helper exists;
- a backup outside the repository if local work exists.

**Implementation steps**

1. Confirm the intended directory:

   ```powershell
   Get-Location
   Get-ChildItem -Force
   ```

2. Detect whether Git exists:

   ```powershell
   $isGitRepo = Test-Path ".git"
   $isGitRepo
   ```

3. If `.git` exists, inspect safely:

   ```powershell
   git status --short --branch
   git remote -v
   git branch --show-current
   git rev-parse --is-inside-work-tree
   git symbolic-ref -q HEAD

   $hasHead = $true
   git rev-parse --verify HEAD 2>$null
   if ($LASTEXITCODE -ne 0) {
       $hasHead = $false
   }

   if ($hasHead) {
       git log -5 --oneline --decorate
   } else {
       Write-Output "No local commit exists."
   }
   ```

4. Inventory local files without treating generated environments as source:

   ```powershell
   Get-ChildItem -Recurse -File -Force |
       Where-Object {
           $_.FullName -notmatch '\\.git\\' -and
           $_.FullName -notmatch '\\.venv\\'
       } |
       Select-Object -ExpandProperty FullName
   ```

5. Inspect the current remote independently of local branch state:

   ```powershell
   git ls-remote --heads https://github.com/Damien-Ergun/synapse-ai.git
   ```

6. If no local Git repository exists and the directory is safe to initialize:

   ```powershell
   git init -b main
   git remote add origin https://github.com/Damien-Ergun/synapse-ai.git
   ```

7. If Git exists but the branch is detached, stop and create or switch to an explicit branch only after identifying the commit that must be preserved.
8. If the current branch is an unborn branch with a different name:

   ```powershell
   git branch -M main
   ```

9. If `origin` is absent, add it. If it is wrong, record the original value before replacing it:

   ```powershell
   git remote add origin https://github.com/Damien-Ergun/synapse-ai.git
   # Or, when origin exists but is wrong:
   git remote set-url origin https://github.com/Damien-Ergun/synapse-ai.git
   ```

10. Fetch remote state without merging:

    ```powershell
    git fetch --prune origin
    git ls-remote --heads origin
    ```

11. If `origin/main` now exists, do not initialize or push blindly. Compare local and remote history, preserve both, and rebase or merge only after inspecting the remote files.
12. Check author identity:

    ```powershell
    git config user.name
    git config user.email
    ```

13. If either value is absent or inappropriate, set a repository-local identity.
14. Create an external backup before modifying any pre-existing local source or documentation.
15. Prohibit `git push --force`, `git push --force-with-lease`, history rewriting, and destructive cleanup during Week 1.

**Validation**

```powershell
git status --short --branch
git remote get-url origin
git branch --show-current
git config user.name
git config user.email
git ls-remote --heads origin
```

**Expected result**

- The directory, local state, remote state, branch, author identity, and existing files are known.
- Any local work is preserved.
- `origin` is correct.
- No remote change is ignored.

**Acceptance criteria**

- No unidentified local file is overwritten.
- No detached HEAD remains.
- The working branch is `main`, unless a preserved remote branch requires a documented reconciliation branch.
- Git author name and email are non-empty and intentional.
- Current remote refs have been checked during execution.
- No force-push plan exists.

**Dependencies and downstream use**

All other tasks depend on W1-A01.

---

### W1-D01: Establish controlled requirements, the decision log, and traceability

**Purpose**

Place the roadmap, the final Week 1 plan, and the decision mechanism inside the repository before foundational implementation decisions are made.

**Roadmap requirement, risk, or gate satisfied**

- Decision log.
- Stable roadmap traceability.
- GAP-003, GAP-004, GAP-006, and GAP-007.

**Preconditions**

- W1-A01 complete.
- The local tree has been reconciled.

**Current state**

| Artifact | Evidence label | Completion status |
|---|---|---|
| Roadmap in chat and uploaded file | `VERIFIED_FROM_USER_OUTPUT` | Available but not controlled in Git |
| Reviewer requirements | `VERIFIED_FROM_USER_OUTPUT` | Available but not controlled in Git |
| Repository decision log | `MISSING` | Not created |
| Repository Week 1 work plan | `MISSING` | Not created |

**Exact files**

Create:

- `docs/programme/12_week_roadmap.md`
- `docs/programme/README.md`
- `docs/weekly_plans/week_1_work_plan.md`
- `docs/weekly_plans/README.md`
- `docs/decision_log.md`
- `docs/traceability/week_1_coverage_matrix.md`
- `docs/traceability/README.md`

Modify:

- `README.md`, after W1-A02 creates it.

Inspect only:

- `/mnt/data/12-week-Roadmap.txt` or the exact user-provided roadmap source;
- the final revised plan used for implementation.

Generated locally:

- source file hashes used to establish control.

**Implementation steps**

1. Copy the full current roadmap into `docs/programme/12_week_roadmap.md` without changing substantive requirements.
2. Add a controlled-document header containing:
   - source filename;
   - SHA-256 `c993737a6b4d299e9a264bb9a5e3cb0a9105f964854adc5b14e76e42dff7d1a3`;
   - adoption date;
   - document status `ACTIVE`;
   - supersession rule;
   - change owner.
3. Copy the complete final revised Week 1 guide into `docs/weekly_plans/week_1_work_plan.md`.
4. Give the weekly plan a controlled-document header containing:
   - target week;
   - roadmap identifier and hash;
   - plan status `APPROVED_FOR_EXECUTION`;
   - creation date;
   - supersession rule.
5. Create the decision log before project initialization. Use this required schema for every entry:

   | Decision ID | Date | Status | Decision | Rationale | Alternatives considered | Consequences | Evidence | Owner | Review trigger |
   |---|---|---|---|---|---|---|---|---|---|

6. Create at least these initial decisions:
   - `DEC-001`: distribution name `raman-bacteria-prototype` and import name `raman_bacteria_prototype`;
   - `DEC-002`: packaged application template with `src` layout, not a library template;
   - `DEC-003`: Python support range `>=3.11,<3.12`, evidence interpreter `3.11.15`;
   - `DEC-004`: `uv` is the canonical environment and execution tool, required version `0.11.29`;
   - `DEC-005`: `uv_build` is the build backend;
   - `DEC-006`: generated data, model binaries, logs, private evidence, and secrets remain local;
   - `DEC-007`: no Makefile in Week 1; `scripts/run_checks.py` is canonical;
   - `DEC-008`: test and clinical splits are reserved as defined in `docs/data_governance.md`;
   - `DEC-009`: repository remains research-use-only;
   - `DEC-010`: no public `LICENSE` until ownership and licensing authority are resolved;
   - `DEC-011`: CI matrix uses Windows and Ubuntu to cover the primary development environment and basic portability;
   - `DEC-012`: finalization uses a verified implementation commit followed by a separate evidence commit.
7. Create `docs/traceability/week_1_coverage_matrix.md` with this schema:

   | Requirement ID | Roadmap wording | Workstream | Task ID | Deliverable path | Validation ID | Evidence ID | Status |
   |---|---|---|---|---|---|---|---|

8. Seed the matrix with every Week 1 roadmap task, deliverable, and gate condition.
9. Require all references to `DEC-*`, `RISK-*`, `CLAIM-*`, `REQ-*`, `VAL-*`, and `EVID-*` to resolve to an existing record.

**Validation**

- Recalculate the controlled roadmap SHA from the unmodified source content before the header is applied.
- Compare the controlled roadmap body with the source.
- Run the documentation validator created in W1-A05.

**Expected result**

- Requirements and decisions remain inspectable without access to this chat.
- Foundational choices exist before their implementation.
- Every Week 1 requirement has a traceability row.

**Acceptance criteria**

- The full roadmap and full Week 1 plan are committed controlled documents.
- The roadmap source hash is correct.
- `docs/decision_log.md` exists before W1-A02.
- `DEC-001` through `DEC-012` are present with all required fields.
- No traceability row lacks a task, deliverable, and validation reference.
- All referenced IDs are unique and resolvable.

**Dependencies and downstream use**

W1-A02 and every later decision-producing task depend on W1-D01.

### Phase 1: Deterministic project foundation

### W1-A02: Initialize the packaged application and repository structure

**Purpose**

Create a deterministic Python 3.11 packaged application, lock its environment, and establish exact committed and local artifact boundaries.

**Roadmap requirement, risk, or gate satisfied**

- Repository structure.
- `pyproject.toml`, `uv.lock`, `.python-version`, `.gitignore`, and `README.md`.
- Python 3.11 and `uv`.
- Clean-install foundation.

**Preconditions**

- W1-A01 complete.
- W1-D01 complete.
- `DEC-001` through `DEC-007` accepted.

**Current state**

All required repository files remain `MISSING` in the inspected GitHub revision. Local equivalents, if any, must be classified during W1-A01.

**Exact files**

Create:

- `.python-version`
- `.gitignore`
- `.env.example`
- `pyproject.toml`
- `uv.lock`
- `README.md`
- `configs/README.md`
- `data/README.md`
- `models/README.md`
- `notebooks/README.md`
- `reports/README.md`
- `docs/clinical/README.md`
- `src/raman_bacteria_prototype/__init__.py`
- `src/raman_bacteria_prototype/cli.py`

Modify:

- `docs/decision_log.md` only if execution reveals a necessary deviation.

Inspect only:

- existing local project metadata, if present.

Generated locally:

- `.venv/`
- Python, pytest, Ruff, Black, and coverage caches.

**Implementation steps**

1. Select one of the following idempotent paths.

   **Case A: empty directory, no `.git`, no `pyproject.toml`**

   - Complete W1-A01.
   - Initialize Git manually.
   - Run:

     ```powershell
     uv init --app --package --bare --build-backend uv_build `
         --name raman-bacteria-prototype `
         --python 3.11 `
         --vcs none .
     ```

   **Case B: existing Git repository, no `pyproject.toml`**

   - Preserve current files.
   - Run the same `uv init` command with `--vcs none` and `--bare`.

   **Case C: existing `pyproject.toml`**

   - Do not run `uv init`.
   - Compare the existing project against the exact contract below.
   - Modify only the fields required to satisfy the contract.

   **Case D: partial files such as `README.md` or `.python-version` exist**

   - Back them up or merge their relevant content.
   - Use `--bare` so `uv` does not create conflicting template files.

   **Case E: remote commits now exist**

   - Fetch and inspect them first.
   - Do not initialize an unrelated history.
   - Rebase the work plan onto the current repository architecture or report `CONFLICTING_EVIDENCE`.

2. Write `.python-version` as:

   ```text
   3.11.15
   ```

3. Build `pyproject.toml` according to the exact W1-A04 contract.
4. Add development dependencies through `uv`, not by editing `uv.lock`:

   ```powershell
   uv add --dev `
       "pytest==9.1.1" `
       "pytest-cov==7.1.0" `
       "ruff==0.15.22" `
       "black==26.5.1"
   ```

5. Intentionally create or refresh the lock only during setup:

   ```powershell
   uv lock
   uv sync --locked
   ```

6. Create required directories:

   ```powershell
   New-Item -ItemType Directory -Force `
       ".github/workflows", `
       "configs", `
       "data", `
       "docs/business", `
       "docs/clinical", `
       "docs/governance", `
       "docs/product", `
       "docs/programme", `
       "docs/traceability", `
       "docs/weekly_checklist", `
       "docs/weekly_plans", `
       "docs/weekly_reports", `
       "models", `
       "notebooks", `
       "reports", `
       "scripts", `
       "src/raman_bacteria_prototype", `
       "tests" | Out-Null
   ```

7. Define `.gitignore` with these required ignored patterns:

   ```gitignore
   .venv/
   .env
   .env.*
   !.env.example
   __pycache__/
   *.py[cod]
   .pytest_cache/
   .ruff_cache/
   .coverage
   coverage.xml
   htmlcov/
   .ipynb_checkpoints/

   data/raw/**
   data/interim/**
   data/processed/**
   !data/README.md

   models/**
   !models/README.md

   reports/logs/**
   reports/generated/**
   !reports/README.md
   ```

8. Do not ignore `uv.lock`, controlled documents, configs, source, tests, or CI.
9. Put only non-secret variable names and comments in `.env.example`.
10. Document in the directory README files:
    - allowed contents;
    - committed versus local status;
    - naming rules;
    - who creates the artifacts;
    - how they are reproduced.
11. Expose package version through `importlib.metadata.version("raman-bacteria-prototype")`. Do not maintain an independent hard-coded `__version__`.
12. In `README.md`, include:
    - programme mission;
    - current Level 0 status;
    - research-use-only notice;
    - explicit non-diagnostic scope;
    - installation commands;
    - canonical validation command;
    - repository map;
    - links to controlled roadmap, plan, TPP, claims, metrics, and governance;
    - current evidence limitations.

**Validation**

```powershell
uv --version
uv python list
uv lock --check
uv sync --locked
uv run --locked python --version
uv run --locked python -c "import importlib.metadata as m; import raman_bacteria_prototype; print(m.version('raman-bacteria-prototype'))"
```

**Expected result**

- `uv lock --check` exits `0` without modifying files.
- `uv sync --locked` exits `0`.
- Python is `3.11.15` for the evidence run.
- The package imports and reports the project metadata version.

**Acceptance criteria**

- Initialization followed the correct existing-state branch.
- `uv init` used `--vcs none` when Git already existed.
- The project is a packaged application with a `src` layout.
- No `py.typed` marker is expected because the library template was not selected.
- `.python-version`, `pyproject.toml`, and `uv.lock` are mutually consistent.
- No final validation command modifies project metadata or the lock.
- Ignored and committed boundaries match the declared policy.

**Dependencies and downstream use**

All source, test, CI, and documentation automation tasks depend on W1-A02.

---

### W1-A03: Define architecture and the Week 2 contracts

**Purpose**

Create enough architectural specificity that Week 2 can implement data ingestion and validation without inventing package boundaries, schemas, hashing, or preservation rules.

**Roadmap requirement, risk, or gate satisfied**

- Package architecture.
- Architecture document.
- Week 2 readiness.
- GAP-011.

**Preconditions**

- W1-D01 and W1-A02 complete.

**Current state**

Architecture is `MISSING` in GitHub. No implementation architecture exists to preserve.

**Exact files**

Create:

- `docs/architecture.md`
- `src/raman_bacteria_prototype/core/__init__.py`
- `src/raman_bacteria_prototype/data/__init__.py`
- `src/raman_bacteria_prototype/data_validation/__init__.py`
- `src/raman_bacteria_prototype/spectral_qc/__init__.py`
- `src/raman_bacteria_prototype/preprocessing/__init__.py`
- `src/raman_bacteria_prototype/features/__init__.py`
- `src/raman_bacteria_prototype/modelling/__init__.py`
- `src/raman_bacteria_prototype/calibration/__init__.py`
- `src/raman_bacteria_prototype/evaluation/__init__.py`
- `src/raman_bacteria_prototype/reporting/__init__.py`
- `src/raman_bacteria_prototype/prediction/__init__.py`
- `src/raman_bacteria_prototype/tracking/__init__.py`

Modify:

- `docs/decision_log.md`
- `README.md`

Inspect only:

- `pyproject.toml`
- directory policy files.

Generated locally:

- none.

**Implementation steps**

1. Define the exact module tree above.
2. Give every module one owner and one responsibility.
3. Define allowed dependency direction:
   - `core` may not import project feature modules;
   - `data` may depend on `core`;
   - `data_validation` and `spectral_qc` may depend on `core` and `data` contracts;
   - `preprocessing` may depend on validated data contracts but not modelling or evaluation;
   - `features` may depend on preprocessing outputs;
   - `modelling` may depend on features and core interfaces;
   - `calibration` and `evaluation` may consume model outputs;
   - `reporting` may consume immutable result objects but may not change predictions;
   - `prediction` orchestrates approved fitted components;
   - `tracking` records metadata and hashes without owning scientific decisions.
4. Define prohibited dependencies, especially:
   - no model import in data ingestion;
   - no evaluation import in preprocessing;
   - no test or clinical result access in development selection;
   - no notebook-only production logic.
5. Define repository-root discovery as walking from `Path(__file__).resolve()` or a supplied explicit root, not relying on the current working directory.
6. Define configuration ownership:
   - human-authored committed configs under `configs/`;
   - UTF-8 TOML for project-controlled pipeline configuration;
   - a required `schema_version` field;
   - no hidden environment-variable scientific settings.
7. Define canonical hashing:
   - normalize validated configuration into canonical JSON;
   - sort keys;
   - use UTF-8;
   - reject NaN and Infinity;
   - use compact separators;
   - compute SHA-256;
   - record the canonicalization version.
8. Define random-seed policy:
   - each stochastic run has an explicit integer seed;
   - the seed appears in config, logs, and experiment records;
   - no unseeded global NumPy or Python random state in pipeline code.
9. Define logging policy:
   - standard `logging` library;
   - module logger names;
   - no patient or secret values;
   - structured stable fields for run ID, task ID, artifact ID, and split;
   - user-visible errors separated from debug traces.
10. Define exception hierarchy names for future implementation:
    - `RamanPrototypeError`;
    - `ConfigurationError`;
    - `DataContractError`;
    - `DataIntegrityError`;
    - `AxisMismatchError`;
    - `ArtifactVerificationError`.
11. Define validation severity values:
    - `INFO`;
    - `WARNING`;
    - `ERROR`;
    - `FATAL`.
12. Define documentation-only Week 2 contract names and minimum fields:

    **`SplitName`**

    - closed values: `train`, `validation`, `test`, `clinical2018`, `clinical2019`.

    **`DatasetDescriptor`**

    - `dataset_id`;
    - `title`;
    - `version`;
    - `source_uri`;
    - `publication_doi`;
    - `retrieved_at_utc`;
    - `rights_record_id`;
    - `expected_splits`;
    - `class_metadata_source`;
    - `axis_source`.

    **`FileManifestEntry`**

    - `relative_path`;
    - `byte_size`;
    - `sha256`;
    - `split`;
    - `role`;
    - `media_type`;
    - `created_at_utc`;
    - `source_file_name`.

    **`SpectrumBatch`**

    - `spectra` as a two-dimensional numeric array with shape `(n_samples, n_wavenumbers)`;
    - `labels` with shape `(n_samples,)`;
    - `sample_ids` with shape `(n_samples,)`;
    - `wavenumbers` with shape `(n_wavenumbers,)`;
    - `split`;
    - immutable metadata mapping;
    - source manifest hash.

    **`ValidationIssue`**

    - `issue_id`;
    - `check_id`;
    - `severity`;
    - `message`;
    - `split`;
    - optional `sample_id`;
    - optional `feature_index`;
    - evidence fields.

    **`ValidationReport`**

    - report ID;
    - dataset and manifest IDs;
    - checks run;
    - issues;
    - counts by severity;
    - pass/fail decision;
    - software version;
    - configuration hash;
    - start and finish timestamps.

    **`QualityFlag`**

    - stable code;
    - severity;
    - sample ID;
    - measured value;
    - threshold identifier;
    - message;
    - source check ID.

13. Define immutability: contract objects are frozen dataclasses or immutable validated models when implemented.
14. Define sample-order preservation: every transformation returns the same ordered `sample_ids` unless an explicit filtering artifact records removed IDs and reasons.
15. Define label preservation: no transformation may alter labels; equality must be asserted before and after preprocessing.
16. Define axis representation: one-dimensional finite strictly monotonic numeric array, unit recorded as `cm^-1`, orientation recorded, no implicit reversal.
17. Define artifact naming:

    ```text
    {artifact_type}__{dataset_id}__{split}__{config_hash_12}__{run_id}.{ext}
    ```

18. Mark every component as `IMPLEMENTED`, `SCAFFOLDED`, or `DEFERRED`. In Week 1, only environment and validation infrastructure may be `IMPLEMENTED`; scientific pipeline modules remain `SCAFFOLDED` or `DEFERRED`.
19. Add `DEC-013` for the exact architecture and `DEC-014` for canonical hashing.

**Validation**

```powershell
uv run --locked python -c "from raman_bacteria_prototype import core, data, data_validation, spectral_qc, preprocessing, features, modelling, calibration, evaluation, reporting, prediction, tracking; print('architecture imports: PASS')"
```

Run the documentation validator and architecture consistency tests.

**Expected result**

- All namespaces import.
- Week 2 contract names and semantics are fixed in documentation.
- No fake loader or scientific function exists.

**Acceptance criteria**

- All eleven roadmap domains have exact package locations.
- `data_validation` is unambiguous.
- Every allowed and prohibited dependency is documented.
- All six Week 2 contract types have required fields and invariants.
- Root discovery, config, hashing, seed, logging, exception, metadata, order, label, axis, and artifact policies are explicit.
- Status labels accurately distinguish implementation from scaffolding.

**Dependencies and downstream use**

Week 2 implementation depends directly on W1-A03.

---

### W1-D02: Define claims control, data governance, and split discipline

**Purpose**

Prevent unsupported medical claims, data leakage, uncontrolled storage, privacy breaches, and misuse of reserved splits.

**Roadmap requirement, risk, or gate satisfied**

- Allowed and forbidden claims.
- Data governance.
- Explicit prototype and non-prototype scope.
- Scientific validity.

**Preconditions**

- W1-D01, W1-A02, and W1-A03 complete.

**Current state**

The required committed documents are `MISSING`.

**Exact files**

Create:

- `docs/governance/claims_register.md`
- `docs/data_governance.md`
- `docs/governance/privacy_and_stakeholder_data.md`

Modify:

- `README.md`
- `docs/decision_log.md`
- later TPP and outreach documents.

Inspect only:

- `.gitignore`
- architecture contracts.

Generated locally:

- private stakeholder crosswalk, outside Git.

**Implementation steps**

1. Use this claims-register schema:

   | Claim ID | Exact wording | Status | Audience | Current evidence level | Evidence required | Prohibited contexts | Owner | Review trigger |
   |---|---|---|---|---|---|---|---|---|

2. Create explicit allowed claims limited to actual Week 1 evidence.
3. Create explicit forbidden claims for:
   - blood-disease detection;
   - sepsis detection;
   - treatment recommendation;
   - antibiotic-susceptibility prediction;
   - hospital readiness;
   - regulatory approval.
4. Give every claim a stable `CLAIM-*` ID.
5. Define data zones:
   - committed metadata and policies;
   - local immutable raw data;
   - local interim data;
   - local processed data;
   - local model artifacts;
   - local generated reports and logs;
   - prohibited sensitive data unless separately approved.
6. Define split permissions:

   | Split | Week first opened for array inspection | Permitted use | Forbidden use before assigned week |
   |---|---:|---|---|
   | `train` | Week 2 | Fit data checks, transformations, and later models | None before rights and integrity gate |
   | `validation` | Week 2 for integrity only | Development sanity and later selection | No test-like final claims |
   | `test` | Week 2 for file integrity only, no performance inspection | One locked internal evaluation in Week 6 | No tuning, selection, threshold setting, or preprocessing choice |
   | `clinical2018` | Week 2 for transformation integrity only | Locked evaluation in Week 7 | No development selection |
   | `clinical2019` | Week 2 for transformation integrity only | Locked evaluation in Week 7 | No development selection |

7. Clarify that Week 1 may inspect publications, metadata, repository documentation, and rights terms, but may not download or inspect spectrum arrays.
8. Define data provenance fields, manifest fields, hashes, versioning, timestamps, and retention.
9. Define stakeholder-data rules:
   - no patient information;
   - no confidential case details;
   - no identifiable patient or employee information;
   - no recording by default;
   - consent required for note-taking;
   - private contact crosswalk retained separately;
   - public records use anonymous evidence IDs;
   - retention review after 12 months;
   - deletion upon withdrawal or when no longer required.
10. Add `DEC-015` for split discipline and `DEC-016` for stakeholder-data handling.

**Validation**

- Claims validator checks unique claim IDs and required forbidden concepts.
- Documentation validator checks required headings and links.
- Manual scientific and privacy review records reviewer, date, outcome, and open issues.

**Expected result**

- Every permitted claim is evidence-bounded.
- Every split has an exact allowed role.
- Stakeholder information has a safe collection and retention policy.

**Acceptance criteria**

- All six forbidden claim categories are explicit.
- No document presents Prototype 0 as a diagnostic product.
- No future serum or plasma result is described as demonstrated.
- Test and clinical splits cannot influence development choices.
- Week 1 spectrum-array access is explicitly prohibited.
- Stakeholder privacy rules prohibit patient and confidential institutional data.

**Dependencies and downstream use**

W1-B01, W1-B02, W1-C02, and all later scientific work depend on W1-D02.

### Phase 2: Exact tool contracts, validators, and CI

### W1-A04: Define `pyproject.toml` and the canonical aggregate validator

**Purpose**

Make local and CI validation deterministic, locked, coverage-enforcing, and impossible to report as passing after a failed mandatory check.

**Roadmap requirement, risk, or gate satisfied**

- Environment validation.
- Pytest, Ruff, and Black.
- Reproducibility.
- GAP-005.

**Preconditions**

- W1-A02 and W1-A03 complete.

**Current state**

The final tool contract and runner are `MISSING`.

**Exact files**

Create:

- `src/raman_bacteria_prototype/environment.py`
- `src/raman_bacteria_prototype/checks.py`
- `scripts/check_environment.py`
- `scripts/check_gitignore.py`
- `scripts/check_documentation.py`
- `scripts/run_checks.py`

Modify:

- `pyproject.toml`
- `src/raman_bacteria_prototype/cli.py`
- `README.md`
- `docs/decision_log.md`

Inspect only:

- `uv.lock`
- architecture and governance documents.

Generated locally:

- `.coverage`;
- pytest and lint caches;
- `reports/logs/week_1/check-results.json`, ignored.

**Implementation steps**

1. Require this substantive `pyproject.toml` contract:

   ```toml
   [project]
   name = "raman-bacteria-prototype"
   version = "0.1.0"
   description = "Research-use Raman spectrum classification prototype foundation"
   readme = "README.md"
   requires-python = ">=3.11,<3.12"
   dependencies = []

   [project.scripts]
   raman-check-environment = "raman_bacteria_prototype.cli:check_environment_main"
   raman-checks = "raman_bacteria_prototype.cli:run_checks_main"

   [build-system]
   requires = ["uv_build>=0.11.29,<0.12"]
   build-backend = "uv_build"

   [dependency-groups]
   dev = [
       "black==26.5.1",
       "pytest==9.1.1",
       "pytest-cov==7.1.0",
       "ruff==0.15.22",
   ]

   [tool.uv]
   required-version = "==0.11.29"

   [tool.pytest.ini_options]
   minversion = "9.1"
   testpaths = ["tests"]
   addopts = ["-ra", "--strict-config", "--strict-markers"]

   [tool.coverage.run]
   branch = true
   source = ["raman_bacteria_prototype"]
   omit = ["src/raman_bacteria_prototype/*/__init__.py"]

   [tool.coverage.report]
   fail_under = 90
   show_missing = true
   skip_covered = false

   [tool.ruff]
   target-version = "py311"
   line-length = 88
   extend-exclude = ["data", "models", "reports", ".venv"]

   [tool.ruff.lint]
   select = ["E4", "E7", "E9", "F", "I", "UP", "B", "C4", "SIM", "RUF"]

   [tool.black]
   line-length = 88
   target-version = ["py311"]
   extend-exclude = "/(data|models|reports|\\.venv)/"
   ```

2. Keep package version metadata in `pyproject.toml` only. `__init__.py` may expose a helper that calls `importlib.metadata.version`, but must not duplicate the version literal.
3. Implement environment checks as testable pure functions where possible. Required checks:
   - Python major and minor;
   - exact evidence interpreter version recorded but not hard-coded as the only supported patch;
   - required `uv` version;
   - repository root;
   - `pyproject.toml` and valid TOML;
   - `uv.lock` existence;
   - required committed paths;
   - package import;
   - controlled roadmap and plan existence.
4. Implement `scripts/run_checks.py` with this exact mandatory command sequence:

   ```text
   1. uv lock --check
   2. <current interpreter> scripts/check_environment.py
   3. <current interpreter> scripts/check_gitignore.py
   4. <current interpreter> scripts/check_documentation.py
   5. <current interpreter> -m pytest -q --cov=raman_bacteria_prototype --cov-branch --cov-report=term-missing --cov-report=xml:coverage.xml --cov-fail-under=90
   6. <current interpreter> -m ruff check .
   7. <current interpreter> -m black --check .
   ```

5. Resolve the executable `uv` through `shutil.which("uv")`. Resolve Python through `sys.executable`.
6. Resolve the repository root from the script path and validated markers, not the caller’s working directory.
7. Run all mandatory checks even if an earlier one fails, so the user receives a complete result set.
8. Stream child stdout and stderr to the terminal while recording them in the stable summary.
9. Record for each check:
   - check ID;
   - command array;
   - start and finish UTC timestamps;
   - duration;
   - exit code;
   - status;
   - stdout and stderr log references.
10. Use these exit semantics:
    - `0`: every mandatory check passed;
    - `1`: one or more mandatory checks failed normally;
    - `2`: unexpected runner exception or invalid runner configuration;
    - `127`: missing required executable, recorded for the affected child and resulting in overall failure.
11. Never print overall PASS if any mandatory check has nonzero exit status.
12. Write stable machine-readable JSON to an optional supplied path or `reports/logs/week_1/check-results.json`.
13. Make `raman-checks` and `uv run --locked python scripts/run_checks.py` invoke the same underlying `run_checks` function.
14. Add `DEC-017` for the exact tool and runner contract.

**Validation**

```powershell
uv lock --check
uv sync --locked
uv run --locked python scripts/run_checks.py
```

Before and after validation:

```powershell
git diff -- pyproject.toml uv.lock
```

**Expected result**

- All checks run in the declared order.
- The final command exits `0` only if every check passes.
- `pyproject.toml` and `uv.lock` remain unchanged.
- Coverage is enforced by the canonical command.

**Acceptance criteria**

- `uv lock --check`, `uv sync --locked`, and `uv run --locked` are used for final validation.
- No final validation uses `--frozen` as a freshness proof.
- The aggregate runner contains the exact coverage threshold.
- Missing tools, child failures, and unexpected exceptions have deterministic statuses.
- Root discovery works outside the repository working directory.
- A stable JSON result is produced.

**Dependencies and downstream use**

W1-A05, W1-A06, and W1-D05 depend on W1-A04.

---

### W1-A05: Implement negative tests, documentation checks, and per-path ignore checks

**Purpose**

Verify not only the happy path, but also every failure mode claimed by the environment and aggregate-validation design.

**Roadmap requirement, risk, or gate satisfied**

- Test coverage.
- Documentation integrity.
- Git privacy and artifact boundaries.
- GAP-012 and GAP-013.

**Preconditions**

- W1-A04 complete.

**Current state**

The required tests and structural validators are `MISSING`.

**Exact files**

Create:

- `tests/conftest.py`
- `tests/test_package_import.py`
- `tests/test_environment.py`
- `tests/test_check_runner.py`
- `tests/test_cli.py`
- `tests/test_repository_structure.py`
- `tests/test_documentation_contracts.py`
- `tests/test_gitignore_policy.py`

Modify:

- `scripts/check_gitignore.py`
- `scripts/check_documentation.py`
- `pyproject.toml` only if test configuration needs a controlled correction.

Inspect only:

- all committed Markdown documents;
- `.gitignore`;
- project metadata.

Generated locally:

- temporary test repositories under pytest `tmp_path`;
- coverage artifacts.

**Implementation steps**

1. In `tests/conftest.py`, provide fixtures for:
   - a minimal valid temporary repository;
   - a repository missing one required path;
   - malformed `pyproject.toml`;
   - injected Python version information;
   - fake subprocess results;
   - isolated environment variables;
   - temporary Git repositories.
2. Keep unit tests separate from subprocess integration tests through explicit markers, for example `unit` and `integration`.
3. Test package and all namespace imports.
4. Test environment-validation success.
5. Test missing `pyproject.toml`.
6. Test missing `uv.lock`.
7. Test each mandatory committed directory missing.
8. Test malformed TOML metadata.
9. Test unsupported Python logic through an injected version tuple rather than altering the running interpreter.
10. Test invocation from an unexpected working directory.
11. Test repository-root resolution through script location.
12. Test CLI success exit code `0`.
13. Test CLI validation failure exit code `1`.
14. Test unexpected runner exception exit code `2`.
15. Test missing tool child result `127` and overall failure.
16. Test child failure propagation.
17. Test exact command ordering.
18. Test that a failed child can never produce overall PASS.
19. Test stable JSON summary keys and deterministic repeated execution after normalizing timestamps and duration.
20. Implement `scripts/check_gitignore.py` so each expected path is checked separately. It must assert ignored status for:

    ```text
    .venv/placeholder.txt
    .env
    .env.local
    data/raw/placeholder.npy
    data/interim/placeholder.npy
    data/processed/placeholder.npy
    models/placeholder.joblib
    reports/logs/placeholder.txt
    reports/generated/placeholder.json
    package/__pycache__/placeholder.pyc
    .pytest_cache/placeholder
    .ruff_cache/placeholder
    notebooks/.ipynb_checkpoints/placeholder.ipynb
    ```

21. The same validator must assert trackable status for:

    ```text
    .env.example
    data/README.md
    models/README.md
    reports/README.md
    uv.lock
    configs/README.md
    ```

22. Use `git check-ignore --no-index --verbose -- <single-path>` separately for every path. An ignored test path passes only when its individual command returns `0`. A trackable test path passes only when its individual command returns nonzero.
23. Implement documentation structural checks for:
   - required document existence;
   - controlled-document headers;
   - required headings;
   - required table columns;
   - unique IDs;
   - resolvable decision, risk, claim, task, validation, and evidence references;
   - internal Markdown links;
   - complete roadmap coverage rows;
   - task-to-deliverable-to-validation mapping;
   - forbidden claim phrases outside explicitly labelled prohibition or governance contexts.
24. Define an allowlist of paths where forbidden wording is expected, such as the claims register and review discussion. Do not rely on naive global substring blocking.
25. Test architecture component status consistency.
26. Require no private data or dataset arrays for any Week 1 test.

**Validation**

```powershell
uv run --locked python -m pytest -q `
    --cov=raman_bacteria_prototype `
    --cov-branch `
    --cov-report=term-missing `
    --cov-report=xml:coverage.xml `
    --cov-fail-under=90
uv run --locked python scripts/check_gitignore.py
uv run --locked python scripts/check_documentation.py
```

**Expected result**

- Zero failed tests.
- Branch coverage at least 90% for current executable package code.
- Every ignore and negation assertion passes individually.
- Documentation references and schemas pass structural checks.

**Acceptance criteria**

- Every required positive and negative behavior listed above has a named test.
- Failure-path assertions include exact exit codes.
- Coverage enforcement is part of the canonical runner.
- Per-path ignore validation proves every path independently.
- Documentation quality still receives manual review, but structural omissions are automated.

**Dependencies and downstream use**

W1-A06 and the final gate depend on W1-A05.

---

### W1-A06: Add pinned GitHub Actions CI for Windows and Ubuntu

**Purpose**

Provide repository-hosted automation in addition to local evidence, with the primary Windows environment and a portability check on Ubuntu.

**Roadmap requirement, risk, or gate satisfied**

- Automated checks.
- Clean repository reproducibility.
- GAP-008.

**Preconditions**

- W1-A04 and W1-A05 complete.

**Current state**

No CI workflow exists: `MISSING`.

**Exact files**

Create:

- `.github/workflows/ci.yml`

Modify:

- `README.md`
- `docs/decision_log.md`

Inspect only:

- GitHub Actions status after push.

Generated locally:

- none.

**Implementation steps**

1. Create one workflow named `CI`.
2. Trigger on:
   - `push` to `main`;
   - `pull_request` targeting `main`;
   - changes to source, tests, scripts, project metadata, workflow files, configs, or committed documentation.
3. Use a matrix:

   ```yaml
   strategy:
     fail-fast: false
     matrix:
       os: [windows-latest, ubuntu-latest]
   ```

4. Use PowerShell explicitly on both systems:

   ```yaml
   defaults:
     run:
       shell: pwsh
   ```

5. Pin checkout by immutable commit:

   ```yaml
   uses: actions/checkout@9c091bb21b7c1c1d1991bb908d89e4e9dddfe3e0 # v7.0.0
   ```

6. Pin `setup-uv` by immutable commit and pin `uv` itself:

   ```yaml
   uses: astral-sh/setup-uv@08807647e7069bb48b6ef5acd8ec9567f424441b # v8.1.0
   with:
     version: "0.11.29"
     python-version: "3.11.15"
     enable-cache: true
     cache-dependency-glob: "uv.lock"
   ```

7. Run:

   ```powershell
   uv lock --check
   uv sync --locked
   uv run --locked python scripts/run_checks.py
   ```

8. Do not use secrets or dataset access.
9. Grant minimum permissions:

   ```yaml
   permissions:
     contents: read
   ```

10. Add concurrency cancellation for superseded runs on the same ref.
11. Add `DEC-011` evidence describing why both Windows and Ubuntu are used.
12. Document that local and CI evidence are both required for the final gate.

**Validation**

- Validate YAML syntax locally with the documentation or workflow structural checker.
- Push the implementation commit.
- Inspect the GitHub Actions status for the exact implementation SHA.

**Expected result**

- Both matrix jobs pass for the verified implementation commit.
- The workflow uses locked sync and the canonical runner.
- No action or tool version uses an unpinned `latest` reference.

**Acceptance criteria**

- Windows and Ubuntu jobs both conclude `success`.
- The recorded commit SHA exactly matches the implementation SHA later placed in the completion report.
- CI performs no data download.
- Local success is not used as a substitute for CI, and CI is not used as a substitute for clean-clone local validation.

**Dependencies and downstream use**

W1-D05 finalization depends on successful CI for the implementation SHA.

---

### W1-A07: Create the initial metric contract

**Purpose**

Fix the semantics, averaging, edge cases, timing protocol, and split restrictions of every metric before model development.

**Roadmap requirement, risk, or gate satisfied**

- Initial metric contract.
- Scientific reproducibility.
- Leakage prevention.

**Preconditions**

- W1-A03 and W1-D02 complete.

**Current state**

The metric contract is `MISSING`.

**Exact files**

Create:

- `docs/metrics_contract.md`

Modify:

- `docs/architecture.md`
- `docs/decision_log.md`
- `docs/traceability/week_1_coverage_matrix.md`

Inspect only:

- `docs/data_governance.md`

Generated locally:

- none.

**Implementation steps**

1. Give every metric a stable `METRIC-*` ID.
2. Require these fields for each metric:
   - name;
   - purpose;
   - mathematical definition;
   - input types and shapes;
   - class ordering;
   - averaging convention;
   - undefined denominator policy;
   - probability requirement;
   - allowed selection split;
   - output schema;
   - confidence-interval expectation;
   - reporting precision;
   - known limitations.
3. Cover:
   - accuracy;
   - balanced accuracy;
   - macro-F1;
   - weighted-F1;
   - top-3 accuracy;
   - per-class precision;
   - per-class recall;
   - per-class specificity;
   - confusion matrix;
   - multiclass Brier score;
   - expected calibration error;
   - rejection-versus-accuracy curve;
   - inference time.
4. Define top-k as `min(3, K)` if fewer than three classes exist.
5. Define specificity one-versus-rest and require denominators.
6. Define confusion-matrix order from committed class metadata.
7. Require ECE binning strategy and bin count to be configuration-controlled and frozen before final evaluation.
8. Require selective metrics to report coverage and accepted-sample denominators.
9. Require inference timing to record hardware, OS, Python, batch size, warm-up, repetition count, and summary statistic.
10. Require later confidence intervals to identify the resampling unit and seed.
11. Add `DEC-018` approving metric-contract version `0.1`.

**Validation**

Run documentation structural checks and perform a manual scientific review with reviewer, date, and outcome recorded.

**Expected result**

Every roadmap metric has one unambiguous definition and one permitted selection policy.

**Acceptance criteria**

- All thirteen metric categories are present.
- Multiclass and undefined cases are explicit.
- Calibration and rejection metrics are distinguished.
- No test or clinical split may select a metric definition or threshold.
- The contract version is linked from the decision log.

**Dependencies and downstream use**

Weeks 4, 5, 6, 7, and 8 depend on W1-A07.

### Phase 3: Product and clinical translation

### W1-B01: Create Target Product Profile v0 and a falsifiable use-case hypothesis

**Purpose**

Define what Prototype 0 is, what it is not, and one future clinical hypothesis specific enough to test while remaining explicitly provisional.

**Roadmap requirement, risk, or gate satisfied**

- `docs/product/target_product_profile_v0.md`.
- Testable future use case.
- Explicit prototype and non-prototype claims.

**Preconditions**

- W1-D02 complete.

**Current state**

The TPP is `MISSING`.

**Exact files**

Create:

- `docs/product/target_product_profile_v0.md`
- `docs/product/open_questions_register.md`

Modify:

- `README.md`
- `docs/governance/claims_register.md`
- `docs/decision_log.md`
- `docs/traceability/week_1_coverage_matrix.md`

Inspect only:

- evidence ladder after W1-B02.

Generated locally:

- none.

**Implementation steps**

1. Put the research-use-only notice before the product description.
2. Use this required TPP structure:
   - document control;
   - current Prototype 0 scope;
   - intended user;
   - setting;
   - controlled input;
   - Prototype 0 output;
   - current evidence level;
   - explicit exclusions;
   - future product hypothesis;
   - target population hypothesis;
   - sample type hypothesis;
   - intended operator;
   - intended decision;
   - current comparator;
   - reference standard hypothesis;
   - turnaround-value hypothesis;
   - acceptable error hypotheses;
   - action after accepted, uncertain, rejected, or failed output;
   - falsification conditions;
   - dependencies and open questions;
   - linked claims and risks.
3. Keep Prototype 0 output limited to bacterial class, confidence, quality status, and alternatives on controlled public benchmark spectra.
4. Define one provisional future serum or plasma use-case hypothesis. Where external evidence is insufficient, label the field `HYPOTHESIS` rather than inventing a fact.
5. Make the hypothesis falsifiable through predefined scientific and workflow conditions.
6. Give every open question an `OQ-*` ID and these fields:
   - question;
   - current assumption;
   - required evidence;
   - owner;
   - target week;
   - linked claim;
   - linked risk;
   - status.
7. Address all nine roadmap questions.
8. Add `DEC-019` recording the selected provisional hypothesis and its non-clinical status.

**Validation**

- Structural documentation check.
- Claims cross-check.
- Manual product and clinical review using an explicit review checklist.

**Expected result**

A reader can distinguish current software evidence from the future clinical hypothesis and identify what would falsify it.

**Acceptance criteria**

- Every required TPP section exists.
- No unknown field is silently presented as known.
- One future hypothesis is testable and falsifiable.
- No diagnostic, treatment, hospital-readiness, or regulatory claim appears.
- All roadmap open questions have IDs, owners, evidence plans, and target weeks.

**Dependencies and downstream use**

Week 2 interviews and clinical workflow work depend on W1-B01.

---

### W1-B02: Create the evidence ladder and claim-to-evidence boundaries

**Purpose**

Define what may be claimed at each development level and prevent public bacteria benchmark results from being misrepresented as serum, plasma, clinical, or regulated evidence.

**Roadmap requirement, risk, or gate satisfied**

- Evidence ladder.
- Claims control.
- Product and clinical foundation.

**Preconditions**

- W1-B01 and W1-D02 complete.

**Current state**

The evidence ladder is `MISSING`.

**Exact files**

Create:

- `docs/product/evidence_ladder.md`

Modify:

- `docs/product/target_product_profile_v0.md`
- `docs/governance/claims_register.md`
- `README.md`
- `docs/traceability/week_1_coverage_matrix.md`

**Implementation steps**

1. Define Levels 0 through 5 exactly as the roadmap requires.
2. For each level, include:
   - objective;
   - required data or study;
   - minimum technical evidence;
   - minimum external review;
   - permitted claims;
   - prohibited claims;
   - exit gate;
   - dependencies;
   - linked risks.
3. Mark current status as `Level 0: IN_PROGRESS`.
4. State explicitly that:
   - public bacterial spectra do not demonstrate serum or plasma feasibility;
   - acquisition robustness does not demonstrate clinical performance;
   - retrospective feasibility does not establish prospective clinical utility;
   - regulatory product claims require the corresponding regulated evidence.
5. Link every allowed claim to a minimum evidence level.

**Validation**

Run documentation checks and a claims-boundary manual review.

**Expected result**

Every future statement can be evaluated against a minimum evidence level.

**Acceptance criteria**

- Six levels exist with objective exit gates.
- No clinical or regulatory claim is allowed at Level 0 or Level 1.
- Current project status is accurate.
- TPP, claims register, and evidence ladder cross-links resolve.

**Dependencies and downstream use**

All later product, investor, and regulatory communications depend on W1-B02.

### Phase 4: Business and investment foundation

### W1-C01: Define the company thesis and stakeholder map

**Purpose**

Distinguish the problem owner, user, beneficiary, operator, buyer, procurement authority, regulator, partner, and funder before outreach.

**Roadmap requirement, risk, or gate satisfied**

- One-sentence company thesis.
- Initial stakeholder list.

**Preconditions**

- W1-B01 and W1-B02 complete.

**Current state**

The required business documents are `MISSING`.

**Exact files**

Create:

- `docs/business/company_thesis.md`
- `docs/business/stakeholder_map.md`

Modify:

- `README.md`
- `docs/traceability/week_1_coverage_matrix.md`

**Implementation steps**

1. Use the roadmap company thesis as the controlled initial wording.
2. Separate the sentence into:
   - current evidence;
   - future hypothesis;
   - intended value;
   - assumptions.
3. Use this stakeholder table schema:

   | Stakeholder ID | Category | Role in workflow | Problem exposure | Decision authority | Buying influence | Evidence question | Priority | Outreach route | Linked hypothesis |
   |---|---|---|---|---|---|---|---|---|---|

4. Include at least the ten roadmap stakeholder categories.
5. Assign an evidence question to every category.
6. Do not include personal email addresses, names without consent, or private contact data in the public repository.

**Validation**

Run documentation checks and compare categories with the roadmap.

**Expected result**

The stakeholder map explains why each stakeholder matters and what the project needs to learn.

**Acceptance criteria**

- All ten categories are present.
- User, buyer, beneficiary, operator, and procurement authority are not conflated.
- Every stakeholder row maps to an evidence question and hypothesis.
- The thesis contains no unsupported claim.

**Dependencies and downstream use**

W1-C02 depends on W1-C01.

---

### W1-C02: Create privacy-safe outreach and request five interviews

**Purpose**

Begin external problem discovery with reproducible, non-leading outreach and auditable evidence while protecting personal and institutional information.

**Roadmap requirement, risk, or gate satisfied**

- Customer-discovery script.
- At least five interview requests.
- Initial external validation route.
- GAP-015.

**Preconditions**

- W1-D02, W1-B01, and W1-C01 complete.

**Current state**

The script, templates, tracker, and sending evidence are `MISSING` or `LOCAL_ONLY_NOT_INSPECTABLE`.

**Exact files**

Create:

- `docs/business/customer_discovery_interview_script.md`
- `docs/business/outreach_templates.md`
- `docs/business/stakeholder_outreach_log.md`
- `docs/business/interview_record_template.md`

Modify:

- `docs/governance/privacy_and_stakeholder_data.md`
- `docs/traceability/week_1_coverage_matrix.md`

Inspect only:

- stakeholder map;
- TPP;
- claims register.

Generated locally:

- `private/stakeholder_crosswalk.csv`, outside Git or in an explicitly ignored private location;
- sent email or message evidence;
- future interview notes.

**Implementation steps**

1. Define the request:
   - a 30-minute research conversation;
   - focused on current workflow and problems;
   - no patient cases or confidential institutional data requested;
   - no product performance claim;
   - no sales request.
2. Create differentiated outreach templates for:
   - clinical laboratory professional;
   - clinician;
   - Raman or spectroscopy specialist;
   - hospital innovation or instrument partner;
   - regulatory, funding, or investment stakeholder.
3. Put the research-only scope and interview purpose in every template.
4. Create a problem-first interview script covering:
   - current workflow;
   - delays and bottlenecks;
   - consequences;
   - sample and instrument constraints;
   - reference standards;
   - acceptable uncertainty and failure handling;
   - existing alternatives;
   - procurement and adoption barriers.
5. Define consent:
   - obtain consent to take notes;
   - do not record audio or video by default;
   - obtain separate explicit consent before any recording;
   - permit withdrawal of notes.
6. Use this public tracker vocabulary:
   - `IDENTIFIED`;
   - `READY_TO_CONTACT`;
   - `REQUEST_SENT`;
   - `FOLLOW_UP_1_SENT`;
   - `FOLLOW_UP_2_SENT`;
   - `ACCEPTED`;
   - `DECLINED`;
   - `NO_RESPONSE`;
   - `INTERVIEW_COMPLETED`.
7. Use this public tracker schema:

   | Outreach ID | Stakeholder category | Organisation type | Date UTC | Channel | Status | Hypothesis ID | Evidence question | Evidence ID | Next action date |
   |---|---|---|---|---|---|---|---|---|---|

8. Use anonymous IDs and keep the identity crosswalk private.
9. Follow up once after 7 days and once after 14 days, then mark `NO_RESPONSE` unless invited to continue.
10. Create an interview record template with:
    - interview ID;
    - role category;
    - organisation type;
    - date;
    - consent status;
    - current workflow;
    - bottlenecks;
    - consequences;
    - evidence quotes or paraphrases;
    - assumptions supported;
    - assumptions contradicted;
    - follow-up questions;
    - TPP impact;
    - risk-register impact;
    - next action.
11. Explicitly prohibit identifiable patient data and confidential institutional information.
12. Select at least five unique contacts across at least three stakeholder categories.
13. Map every request to one stakeholder hypothesis and evidence question.
14. Send all five requests and retain private evidence.

**Validation**

- Public tracker contains at least five unique `REQUEST_SENT` rows.
- Each row has a unique evidence ID.
- Private evidence matches each evidence ID.
- Documentation and privacy checks pass.

**Expected result**

At least five verifiable requests exist, with no private information committed.

**Acceptance criteria**

- Five unique requests have actually been sent.
- At least three stakeholder categories are represented.
- Each request maps to a hypothesis and evidence question.
- Outreach language is problem-focused and claim-safe.
- Consent, retention, deletion, anonymisation, and follow-up rules are explicit.
- No patient, private contact, or confidential institutional data is committed.

**Dependencies and downstream use**

Week 2 completed interviews depend on W1-C02.

---

### W1-C03: Create the investment-hypothesis register

**Purpose**

Convert the commercial narrative into testable assumptions rather than unsupported claims.

**Roadmap requirement, risk, or gate satisfied**

- `docs/business/investment_hypotheses.md`.
- Visibility of commercial risk.

**Preconditions**

- W1-B01 and W1-C01 complete.

**Current state**

The register is `MISSING`.

**Exact files**

Create:

- `docs/business/investment_hypotheses.md`

Modify:

- later investment risk register;
- `docs/traceability/week_1_coverage_matrix.md`.

**Implementation steps**

1. Cover the ten roadmap categories: problem, user, buyer, proposed value, workflow, alternatives, costs, adoption barriers, regulatory dependency, and clinical-data dependency.
2. Use this schema:

   | Hypothesis ID | Category | Statement | Evidence status | Supporting evidence | Contradicting evidence | Test | Falsification condition | Owner | Target week | Linked risk |
   |---|---|---|---|---|---|---|---|---|---|---|

3. Separate facts from assumptions.
4. Do not invent market size, clinical performance, cost saving, turnaround benefit, or willingness to pay.
5. Link every high-uncertainty commercial hypothesis to a risk.

**Validation**

Run structural checks and manual commercial review.

**Expected result**

Every business statement is supported, identified as an assumption, or scheduled for evidence collection.

**Acceptance criteria**

- All ten categories are represented.
- Every hypothesis has a falsification condition, owner, target week, and linked risk where material.
- Unsupported numbers are absent.

**Dependencies and downstream use**

Week 2 competitor work and later market modelling depend on W1-C03.

### Phase 5: Governance, rights, risks, and evidence control

### W1-D03: Create scored technical and investment risk registers

**Purpose**

Make technical, scientific, clinical, privacy, cybersecurity, regulatory, ownership, and commercial blockers explicit and governed by a consistent decision rule.

**Roadmap requirement, risk, or gate satisfied**

- Technical risk register.
- Investment risk register.
- Major technical, clinical, and commercial risks visible.
- GAP-016.

**Preconditions**

- W1-D02, W1-B01, and W1-C03 complete.

**Current state**

Both registers are `MISSING`.

**Exact files**

Create:

- `docs/risk_register.md`
- `docs/risk_register_investment.md`
- `docs/governance/risk_scoring_policy.md`

Modify:

- TPP;
- investment hypotheses;
- decision log;
- traceability matrix.

**Implementation steps**

1. Define likelihood:
   - 1 Rare;
   - 2 Unlikely;
   - 3 Possible;
   - 4 Likely;
   - 5 Almost certain.
2. Define impact:
   - 1 Negligible;
   - 2 Minor;
   - 3 Moderate;
   - 4 Major;
   - 5 Critical.
3. Compute priority score as `likelihood * impact`.
4. Define bands:
   - 1 to 4 Low;
   - 5 to 9 Medium;
   - 10 to 14 High;
   - 15 to 25 Critical.
5. Record inherent likelihood, inherent impact, inherent score, controls, residual likelihood, residual impact, and residual score.
6. Use this register schema:

   | Risk ID | Category | Cause | Event | Consequence | Inherent L | Inherent I | Inherent score | Controls | Residual L | Residual I | Residual score | Treatment | Owner | Indicator | Review date | Status | Blocking decision |
   |---|---|---|---|---|---:|---:|---:|---|---:|---:|---:|---|---|---|---|---|---|

7. Define blocker logic:
   - any active residual Critical risk blocks the relevant gate;
   - any active High risk requires a named owner, dated mitigation, and explicit accept, reduce, avoid, or transfer decision;
   - a dataset-rights risk blocks acquisition when rights are unclear;
   - a credible code-ownership risk blocks public publication;
   - privacy and security risks block any handling of prohibited data;
   - non-blocking controlled risks must have residual rationale and review date.
8. Include technical risks for data access, provenance, leakage, duplicates, acquisition artefacts, preprocessing instability, domain shift, reproducibility, labels, sample order, claims, sample access, instrument access, privacy, cybersecurity, dataset licensing, code ownership, data ownership, publication obligations, and open-source contamination.
9. Include investment risks for clinical need, buyer, procurement, economics, adoption, regulation, clinical evidence, IP, partnerships, financing, and team capacity.
10. Add explicit risk IDs for:
    - `RISK-DATA-RIGHTS-001`;
    - `RISK-CODE-OWNERSHIP-001`;
    - `RISK-PRIVACY-001`;
    - `RISK-CYBER-001`;
    - `RISK-CLAIMS-001`;
    - `RISK-LEAKAGE-001`;
    - `RISK-PUBLICATION-001`;
    - `RISK-OSS-LICENCE-001`.
11. Add `DEC-020` approving the risk policy.

**Validation**

- Structural validator checks score arithmetic, required fields, unique IDs, and review dates.
- Manual risk review records decisions for every High or Critical residual risk.

**Expected result**

Every major risk has a controlled status and an objective blocker interpretation.

**Acceptance criteria**

- Required categories are represented.
- Score arithmetic is correct.
- Every active High or Critical risk has an owner, treatment, indicator, review date, and blocking decision.
- Readiness references specific risk IDs rather than a vague statement.

**Dependencies and downstream use**

W1-D04 and W1-D05 depend on W1-D03.

---

### W1-D04: Complete dataset-rights, dependency-licence, ownership, and disclosure reviews

**Purpose**

Determine what may be downloaded, redistributed, published, licensed, or used commercially before Week 2 data acquisition or the first public push.

**Roadmap requirement, risk, or gate satisfied**

- Dependency licences.
- Public-dataset terms.
- Academic-work code ownership.
- Governance and IP workstream.
- GAP-009, GAP-010, and GAP-014.

**Preconditions**

- W1-A02, W1-D02, and W1-D03 complete.

**Current state**

| Item | Evidence label | Completion status |
|---|---|---|
| Intended dataset publication and source repository | `VERIFIED_FROM_USER_OUTPUT` and independently researched | Identified |
| Separate dataset licence for hosted arrays | `INCOMPLETE` | Blocking Week 2 acquisition |
| Locked dependency inventory | `MISSING` | Not generated |
| Code ownership conclusion | `LOCAL_ONLY_NOT_INSPECTABLE` | Not reviewed |

**Exact files**

Create:

- `docs/governance/dataset_rights.md`
- `docs/governance/licensing_and_ownership_review.md`
- `docs/governance/dependency_licence_register.md`
- `docs/governance/toolchain_register.md`

Modify:

- `docs/risk_register.md`
- `docs/risk_register_investment.md`
- `docs/decision_log.md`
- `docs/traceability/week_1_coverage_matrix.md`

Inspect only:

- `pyproject.toml`;
- `uv.lock`;
- Python licence;
- `uv` licence;
- every locked package licence;
- GitHub Actions licences and pinned references;
- relevant academic, employment, internship, funding, and institutional agreements;
- official dataset publication, source repository, data availability statement, and hosting record.

Generated locally:

- `reports/generated/week_1/dependency_sbom.cdx.json`;
- `reports/generated/week_1/locked_packages.txt`;
- private contract notes.

**Implementation steps**

1. Identify the intended dataset as:
   - title: *Rapid identification of pathogenic bacteria using Raman spectroscopy and deep learning*;
   - authors: Ho et al.;
   - publication: *Nature Communications*, volume 10, article 4927, 2019;
   - DOI: `10.1038/s41467-019-12898-9`;
   - official code and data-reference repository: `csho33/bacteria-ID`;
   - array hosting referenced by that repository: external Dropbox link;
   - named split files include fine-tuning, test, clinical 2018, and clinical 2019 arrays.
2. Record the authoritative publication data-availability statement and source-repository location.
3. Record that the code repository has an MIT software licence, but that this does not automatically establish rights for externally hosted data arrays.
4. Search for a dataset-specific licence or terms from the authors, publisher, repository, or hosting record.
5. If no authoritative dataset licence or written permission is found:
   - mark the rights record `INCOMPLETE`;
   - keep `RISK-DATA-RIGHTS-001` active and blocking;
   - prohibit Week 2 array download;
   - request written clarification from the corresponding author or rights holder;
   - record the exact question covering research use, redistribution, derived artifacts, publication, and commercial research.
6. Clarify that Week 1 rights research may inspect publication and metadata only, not spectrum arrays.
7. Generate the locked component set without changing the lock:

   ```powershell
   uv lock --check
   uv export --locked --all-groups --format cyclonedx1.5 `
       --output-file reports/generated/week_1/dependency_sbom.cdx.json
   uv tree --locked > reports/generated/week_1/locked_packages.txt
   ```

8. If the installed `uv` version does not support the declared CycloneDX export format, record `CONFLICTING_EVIDENCE`, do not invent an SBOM, and generate a deterministic package inventory from `uv.lock` using a documented local parser. The formal Week 6 SBOM remains deferred.
9. Cover every component:
   - direct runtime dependencies;
   - direct development dependencies;
   - transitive dependencies;
   - Python runtime;
   - `uv`;
   - build backend;
   - GitHub Actions.
10. Use this licence-register schema:

    | Component | Version or commit | Direct/transitive/tool | Runtime/dev/CI | Purpose | Declared licence | Authoritative source | Compatibility conclusion | Ambiguity | Required action |
    |---|---|---|---|---|---|---|---|---|---|

11. Do not treat an unverified package metadata classifier as final evidence. Verify each licence against an authoritative package distribution, project repository, or licence file.
12. Review code ownership and disclosure:
    - author;
    - employment and academic relationships;
    - funding;
    - project scope;
    - ownership clauses;
    - invention disclosure;
    - publication restrictions;
    - patent implications;
    - open-source authority.
13. Apply these rules:
    - credible third-party ownership claim blocks public push;
    - uncertainty that permits private research but not publication must be recorded as such;
    - an accepted controlled risk must have evidence, scope, owner, and review date;
    - do not commit private contracts;
    - do not add `LICENSE` until authority and strategy are confirmed.
14. Add `DEC-021` for dataset acquisition authorization status and `DEC-022` for public code publication authorization.

**Validation**

```powershell
uv lock --check
uv tree --locked
```

Manual checks:

- every locked package has a licence row;
- every licence row has an authoritative source;
- dataset-rights record contains a clear permitted or blocked action;
- ownership decision contains an evidence basis and scope.

**Expected result**

- All third-party components are traceable.
- Public push authority is explicit.
- Week 2 data acquisition is either explicitly permitted or blocked with an escalation route.

**Acceptance criteria**

- Every direct and transitive locked dependency is represented.
- Python, `uv`, build backend, and CI actions are represented.
- Dataset title, publication, DOI, repository, host, version information, and rights status are recorded.
- An absent dataset licence is not treated as permission.
- Public push occurs only if `DEC-022` permits it.
- `LICENSE` remains absent unless a later controlled decision authorizes it.

**Dependencies and downstream use**

Week 2 acquisition depends on `DEC-021`. Public finalization depends on `DEC-022`.

---

### W1-D05: Capture auditable evidence and complete the non-circular Git finalization

**Purpose**

Prove the Week 1 gate on an exact implementation commit, retain local evidence without exposing private data, and commit a completion report without impossible self-reference.

**Roadmap requirement, risk, or gate satisfied**

- Repository installs and tests from scratch.
- Passing base checks.
- Week 1 gate.
- Clean Git history and Week 2 continuity.
- GAP-006.

**Preconditions**

- W1-A01 through W1-D04 complete.
- Five outreach requests sent.
- Dataset and ownership blocker decisions recorded.

**Current state**

The evidence manifest, completion report, implementation commit, CI result, and clean-clone result are `MISSING`.

**Exact files**

Create:

- `scripts/invoke_logged_command.ps1`
- `docs/weekly_checklist/week_1_completion_checklist.md`
- `docs/weekly_reports/week_1_evidence_manifest.md`
- `docs/weekly_reports/week_1_completion_report.md`

Modify:

- `docs/traceability/week_1_coverage_matrix.md`
- `docs/decision_log.md`
- risk registers.

Inspect only:

- staged diff;
- GitHub Actions for the exact implementation SHA;
- clean clone at the exact implementation SHA.

Generated locally:

- `reports/logs/week_1/EVID-W1-ENV-001.txt`
- `reports/logs/week_1/EVID-W1-CHECKS-001.txt`
- `reports/logs/week_1/EVID-W1-CLONE-001.txt`
- `reports/logs/week_1/EVID-W1-CI-001.txt` or exported CI metadata;
- `reports/logs/week_1/EVID-W1-OUTREACH-001-private.*`;
- temporary clean clone.

**Implementation steps**

1. Implement `scripts/invoke_logged_command.ps1` with parameters for evidence ID, command, arguments, output path, repository root, and verified SHA.
2. The script must record in UTF-8:
   - evidence ID;
   - exact command and argument array;
   - start and finish UTC timestamps;
   - OS and PowerShell version;
   - repository-relative working directory;
   - Git SHA;
   - Python version;
   - `uv` version;
   - stdout;
   - stderr;
   - child exit code.
3. Preserve the child exit code when using `Tee-Object`. Use a controlled process invocation or capture `$LASTEXITCODE` immediately after the child process and exit with that code after writing metadata.
4. Compute SHA-256 for each retained log:

   ```powershell
   Get-FileHash -Algorithm SHA256 <log-path>
   ```

5. In the committed evidence manifest, record:

   | Evidence ID | Purpose | Verified implementation SHA | Command or source | Start UTC | Finish UTC | Exit code or status | Local log relative path | SHA-256 | Privacy class |
   |---|---|---|---|---|---|---|---|---|---|

6. Do not commit machine-specific absolute paths, private names, email addresses, or message bodies.
7. Use the following non-circular sequence.

   **Stage 1: implementation commits**

   a. Recheck remote:

   ```powershell
   git fetch --prune origin
   git ls-remote --heads origin
   ```

   b. Stage explicit reviewed path groups, never `git add .`:

   ```powershell
   git add .python-version .gitignore .env.example pyproject.toml uv.lock README.md
   git add .github configs data docs models notebooks reports scripts src tests
   ```

   c. Review staged names and content:

   ```powershell
   git diff --cached --name-status
   git diff --cached --check
   git diff --cached
   ```

   d. Search staged content for secrets, personal contacts, private paths, and prohibited data.

   e. Use logical commits, for example:

   ```text
   chore: establish controlled programme baseline
   build: initialize packaged Python project
   feat: add architecture and validation contracts
   test: add aggregate checks and CI
   docs: add product business and governance foundation
   ```

   f. Record the exact final implementation commit:

   ```powershell
   $implementationSha = git rev-parse HEAD
   $implementationSha
   ```

   g. Recheck the remote immediately before push. If the remote changed, stop, fetch, inspect, and reconcile without force push.

   h. Push the implementation history:

   ```powershell
   git push -u origin main
   ```

   **Stage 2: verify exact implementation SHA**

   i. Create a clean temporary clone and detach at the exact SHA:

   ```powershell
   $verifyRoot = Join-Path $env:TEMP "synapse-ai-week1-verify"
   if (Test-Path $verifyRoot) {
       Remove-Item -Recurse -Force $verifyRoot
   }

   git clone https://github.com/Damien-Ergun/synapse-ai.git $verifyRoot
   Push-Location $verifyRoot
   git checkout --detach $implementationSha
   uv lock --check
   uv sync --locked
   uv run --locked python scripts/run_checks.py
   $cloneExit = $LASTEXITCODE
   Pop-Location
   if ($cloneExit -ne 0) { exit $cloneExit }
   ```

   j. Verify both GitHub Actions matrix jobs for the exact implementation SHA.

   **Stage 3: evidence and report commit**

   k. Create `docs/weekly_reports/week_1_completion_report.md` recording:
   - `verified_implementation_commit_sha`;
   - roadmap identifier and hash;
   - exact local, clean-clone, and CI commands;
   - observed exit codes;
   - evidence IDs and log hashes;
   - Python and `uv` versions;
   - outreach evidence IDs;
   - claim, split, risk, rights, and ownership decisions;
   - unresolved non-blocking risks;
   - Week 2 readiness verdict.

   l. The report must not claim to contain its own commit SHA.

   m. Stage only the evidence manifest, completion report, completed checklist, and any necessary status updates:

   ```powershell
   git add docs/weekly_checklist/week_1_completion_checklist.md
   git add docs/weekly_reports/week_1_evidence_manifest.md
   git add docs/weekly_reports/week_1_completion_report.md
   git add docs/traceability/week_1_coverage_matrix.md
   git add docs/decision_log.md docs/risk_register.md docs/risk_register_investment.md
   ```

   n. Review the staged diff and commit:

   ```powershell
   git diff --cached --name-status
   git diff --cached --check
   git diff --cached
   git commit -m "docs: record Week 1 verification evidence"
   git push origin main
   ```

   o. Record the evidence/report commit SHA externally for the post-push reviewer:

   ```powershell
   git rev-parse HEAD
   git show -s --format="%H%n%cI%n%s" HEAD
   ```

   p. Do not amend the completion report to contain this same SHA. Supply it to the reviewer from Git output.

8. If push is rejected because the remote changed, do not force push. Fetch, inspect, rebase or merge intentionally, rerun verification on the resulting new implementation SHA, and update the report evidence accordingly.
9. Final Git check:

   ```powershell
   git status --short --branch
   ```

**Validation**

- All commands in Section 13.
- Local check evidence.
- Clean-clone evidence at exact implementation SHA.
- Windows and Ubuntu CI success at exact implementation SHA.
- Clean final working tree after evidence commit.

**Expected result**

- The report refers to an immutable verified implementation SHA.
- Local logs have hashes and evidence IDs.
- CI and clean-clone evidence match the same implementation SHA.
- The final repository contains a later report commit without self-reference.

**Acceptance criteria**

- The implementation and report commits are separate.
- No report claims its own SHA.
- Both CI jobs pass for the exact implementation SHA.
- Clean-clone validation exits `0` at the exact implementation SHA.
- Evidence logs are local, hashed, and represented by a sanitised committed manifest.
- The final working tree is clean and tracks `origin/main`.
- No force push or broad unreviewed staging occurred.

**Dependencies and downstream use**

W1-D05 is the final Week 1 gate and provides the input for the post-push reviewer.

## 10. Exact file-change ledger

The ledger is normative. Any path created during execution that is not listed here must be added through a recorded decision before commit.

| Path | Action | Workstream | Purpose | Expected contents | Generated or committed | Validation |
|---|---|---|---|---|---|---|
| `.github/workflows/ci.yml` | CREATE | A | Repository-hosted checks | Pinned Windows and Ubuntu CI using locked `uv` validation | Committed | CI success for implementation SHA |
| `.python-version` | CREATE | A | Evidence interpreter pin | `3.11.15` | Committed | `uv run --locked python --version` |
| `.gitignore` | CREATE | A/D | Protect local and private artifacts | Exact ignore and negation rules from W1-A02 | Committed | Per-path validator |
| `.env.example` | CREATE | A/D | Safe environment template | Variable names and comments only, no values or secrets | Committed | Trackability and secret review |
| `LICENSE` | NO_CHANGE | D | Avoid unauthorized licensing | Absent until a controlled ownership and licensing decision authorizes it | Not created | `DEC-010`, `DEC-022` |
| `README.md` | CREATE | A/B/C/D | Repository entry point | Mission, scope, setup, checks, status, links, limitations | Committed | Documentation validator and manual review |
| `pyproject.toml` | CREATE | A | Exact project and tool contract | Project, build, dependencies, scripts, Pytest, coverage, Ruff, Black, `uv` version | Committed | `uv lock --check`, metadata tests |
| `uv.lock` | CREATE | A/D | Locked environment | `uv`-generated lock | Committed | `uv lock --check` |
| `configs/README.md` | CREATE | A | Configuration policy | TOML, schema version, hashing, commit policy | Committed | Structure check |
| `data/README.md` | CREATE | A/D | Data-zone policy | Raw/interim/processed boundaries and Week 2 rights gate | Committed | Structure and ignore checks |
| `models/README.md` | CREATE | A/D | Model-artifact policy | Local binaries, future model manifests | Committed | Structure and ignore checks |
| `notebooks/README.md` | CREATE | A | Notebook policy | Exploratory role, no production-only logic, output policy | Committed | Structure check |
| `reports/README.md` | CREATE | A/D | Report and evidence policy | Local logs/generated reports versus committed summaries | Committed | Structure and ignore checks |
| `docs/programme/README.md` | CREATE | D | Controlled roadmap policy | Status and supersession rules | Committed | Documentation validator |
| `docs/programme/12_week_roadmap.md` | CREATE | A/B/C/D | Controlled source requirements | Full roadmap plus control header | Committed | Source hash and body comparison |
| `docs/weekly_plans/README.md` | CREATE | D | Weekly-plan policy | Approval and supersession rules | Committed | Documentation validator |
| `docs/weekly_plans/week_1_work_plan.md` | CREATE | A/B/C/D | Complete execution baseline | Full revised guide | Committed | Coverage and structure checks |
| `docs/traceability/README.md` | CREATE | D | Traceability policy | ID and matrix rules | Committed | Documentation validator |
| `docs/traceability/week_1_coverage_matrix.md` | CREATE | A/B/C/D | Requirement traceability | Roadmap to task, deliverable, validation, evidence | Committed | Coverage validator |
| `docs/decision_log.md` | CREATE | D/A | Foundational decisions | `DEC-*` records with required schema | Committed | ID and reference checks |
| `docs/architecture.md` | CREATE | A | Package and contract architecture | Tree, dependencies, contracts, hashing, seeds, logging, status | Committed | Architecture tests and review |
| `docs/metrics_contract.md` | CREATE | A | Scientific metric policy | `METRIC-*` definitions and split rules | Committed | Structural and scientific review |
| `docs/data_governance.md` | CREATE | D/A | Data and split governance | Data zones, provenance, split permissions, retention | Committed | Split and document checks |
| `docs/clinical/README.md` | CREATE | B/D | Clinical-document boundary | Research-only status and deferred protocol work | Committed | Structure check |
| `docs/product/target_product_profile_v0.md` | CREATE | B | Product hypothesis | TPP structure and falsifiable future hypothesis | Committed | TPP and claims review |
| `docs/product/open_questions_register.md` | CREATE | B | Product unknowns | `OQ-*` records, owners, evidence, target weeks | Committed | Required-field check |
| `docs/product/evidence_ladder.md` | CREATE | B/D | Evidence boundaries | Levels 0 to 5, claims and gates | Committed | Claims cross-check |
| `docs/business/company_thesis.md` | CREATE | C | Company thesis | Controlled current and future wording | Committed | Claims review |
| `docs/business/stakeholder_map.md` | CREATE | C/B | Stakeholder structure | `Stakeholder ID` rows and evidence questions | Committed | Category audit |
| `docs/business/customer_discovery_interview_script.md` | CREATE | C/B | Interview execution | Problem-first questions and consent opening | Committed | Manual bias and claims review |
| `docs/business/outreach_templates.md` | CREATE | C/B | Reusable outreach | Five role-specific templates | Committed | Claims and privacy review |
| `docs/business/stakeholder_outreach_log.md` | CREATE | C | Public outreach evidence | Anonymous IDs, status, evidence IDs | Committed | Five `REQUEST_SENT` rows |
| `docs/business/interview_record_template.md` | CREATE | C/B/D | Future interview records | Consent, workflow, evidence, TPP and risk impacts | Committed | Template-field check |
| `docs/business/investment_hypotheses.md` | CREATE | C | Commercial assumptions | `Hypothesis ID` rows and falsification tests | Committed | Category and risk-link check |
| `docs/governance/claims_register.md` | CREATE | D | Claims control | `CLAIM-*` allowed and forbidden wording | Committed | Claims validator |
| `docs/governance/privacy_and_stakeholder_data.md` | CREATE | D/B/C | Privacy policy | Consent, anonymisation, retention, deletion, prohibited data | Committed | Privacy review |
| `docs/governance/risk_scoring_policy.md` | CREATE | D | Risk method | 5x5 scales, bands, blocker rules | Committed | Arithmetic and rule tests |
| `docs/risk_register.md` | CREATE | D/A/B | Technical and clinical risks | Scored `RISK-*` rows and controls | Committed | Risk validator |
| `docs/risk_register_investment.md` | CREATE | D/C | Commercial and financing risks | Scored investment rows | Committed | Risk validator |
| `docs/governance/dataset_rights.md` | CREATE | D/A | Dataset authorization | Exact dataset identity, sources, terms, status, escalation | Committed | Rights review and decision |
| `docs/governance/licensing_and_ownership_review.md` | CREATE | D | Code and disclosure authority | Ownership relationships, evidence, conclusions | Committed | `DEC-022` and manual review |
| `docs/governance/dependency_licence_register.md` | CREATE | D/A | Third-party obligations | Direct, transitive, runtime, dev, build, CI components | Committed | Inventory-to-lock reconciliation |
| `docs/governance/toolchain_register.md` | CREATE | D/A | Tool evidence | Python, `uv`, Git, PowerShell, CI actions and versions | Committed | Completion report cross-check |
| `docs/weekly_checklist/week_1_completion_checklist.md` | CREATE | A/B/C/D | Action and gate checklist | Final checklist from this plan | Committed | Checklist coverage validator |
| `docs/weekly_reports/week_1_evidence_manifest.md` | CREATE | A/B/C/D | Sanitised evidence index | IDs, SHAs, hashes, statuses, privacy class | Committed in evidence commit | Evidence-hash reconciliation |
| `docs/weekly_reports/week_1_completion_report.md` | CREATE | A/B/C/D | Final Week 1 verdict | Verified implementation SHA, observed results, risks, readiness | Committed in evidence commit | Report schema and evidence checks |
| `scripts/check_environment.py` | CREATE | A | Environment CLI | Thin CLI using package functions | Committed | CLI tests |
| `scripts/check_gitignore.py` | CREATE | A/D | Per-path policy check | Independent ignored and trackable assertions | Committed | Unit and integration tests |
| `scripts/check_documentation.py` | CREATE | A/D | Structural documentation check | Paths, headings, schemas, IDs, references, links, coverage | Committed | Negative tests |
| `scripts/run_checks.py` | CREATE | A | Canonical aggregate validation | Exact seven-check sequence and stable JSON | Committed | Runner tests and CI |
| `scripts/invoke_logged_command.ps1` | CREATE | A/D | Evidence capture | UTF-8 log wrapper preserving child exit code | Committed | Controlled failure and success tests |
| `src/raman_bacteria_prototype/__init__.py` | CREATE | A | Package import and metadata | Metadata-derived version helper only | Committed | Import/version test |
| `src/raman_bacteria_prototype/cli.py` | CREATE | A | Entry points | Environment and aggregate CLI functions | Committed | CLI tests |
| `src/raman_bacteria_prototype/environment.py` | CREATE | A | Testable environment logic | Pure checks, root resolution, structured results | Committed | Environment tests |
| `src/raman_bacteria_prototype/checks.py` | CREATE | A | Aggregate runner logic | Commands, statuses, streaming, JSON summary | Committed | Runner tests |
| `src/raman_bacteria_prototype/core/__init__.py` | CREATE | A | Core namespace | Responsibility and status docstring | Committed | Namespace import test |
| `src/raman_bacteria_prototype/data/__init__.py` | CREATE | A | Data-loading namespace | Responsibility and scaffold status | Committed | Namespace import test |
| `src/raman_bacteria_prototype/data_validation/__init__.py` | CREATE | A | Dataset-integrity namespace | Responsibility and scaffold status | Committed | Namespace import test |
| `src/raman_bacteria_prototype/spectral_qc/__init__.py` | CREATE | A | Spectral-QC namespace | Responsibility and scaffold status | Committed | Namespace import test |
| `src/raman_bacteria_prototype/preprocessing/__init__.py` | CREATE | A | Preprocessing namespace | Deferred status | Committed | Namespace import test |
| `src/raman_bacteria_prototype/features/__init__.py` | CREATE | A | Feature namespace | Deferred status | Committed | Namespace import test |
| `src/raman_bacteria_prototype/modelling/__init__.py` | CREATE | A | Modelling namespace | Deferred status | Committed | Namespace import test |
| `src/raman_bacteria_prototype/calibration/__init__.py` | CREATE | A | Calibration namespace | Deferred status | Committed | Namespace import test |
| `src/raman_bacteria_prototype/evaluation/__init__.py` | CREATE | A | Evaluation namespace | Deferred status | Committed | Namespace import test |
| `src/raman_bacteria_prototype/reporting/__init__.py` | CREATE | A | Reporting namespace | Deferred status | Committed | Namespace import test |
| `src/raman_bacteria_prototype/prediction/__init__.py` | CREATE | A | Prediction namespace | Deferred status | Committed | Namespace import test |
| `src/raman_bacteria_prototype/tracking/__init__.py` | CREATE | A | Tracking namespace | Deferred status | Committed | Namespace import test |
| `tests/conftest.py` | CREATE | A | Shared test fixtures | Temporary repositories, subprocess fakes, version injection | Committed | Pytest collection |
| `tests/test_package_import.py` | CREATE | A | Package contract | Package, namespace, version tests | Committed | Pytest |
| `tests/test_environment.py` | CREATE | A | Environment behavior | Success and all specified negative cases | Committed | Pytest |
| `tests/test_check_runner.py` | CREATE | A | Aggregate behavior | Order, failures, missing tools, JSON, determinism | Committed | Pytest |
| `tests/test_cli.py` | CREATE | A | CLI behavior | Exit codes and unexpected working directory | Committed | Pytest |
| `tests/test_repository_structure.py` | CREATE | A/D | Repository contract | Required committed paths and project metadata | Committed | Pytest |
| `tests/test_documentation_contracts.py` | CREATE | A/D | Document structure | Headings, tables, IDs, links, coverage, claims context | Committed | Pytest |
| `tests/test_gitignore_policy.py` | CREATE | A/D | Artifact privacy | Every ignore and negation path independently | Committed | Pytest |
| `.venv/` | GENERATE_LOCALLY | A | Local environment | `uv`-managed environment | Ignored local | Per-path ignore check |
| `reports/logs/week_1/` | GENERATE_LOCALLY | A/B/C/D | Validation and private evidence | UTF-8 logs and local-only records | Ignored local | Evidence manifest hashes |
| `reports/generated/week_1/dependency_sbom.cdx.json` | GENERATE_LOCALLY | D/A | Provisional dependency inventory | CycloneDX or documented equivalent | Ignored local | Component reconciliation |
| `reports/generated/week_1/locked_packages.txt` | GENERATE_LOCALLY | D/A | Dependency tree evidence | Locked package tree | Ignored local | Licence-register reconciliation |
| `private/stakeholder_crosswalk.csv` | GENERATE_LOCALLY | C/D | Private identity mapping | Outreach ID to private contact | Outside Git or ignored local | Privacy audit |
| `data/raw/` | NO_CHANGE | A/D | Week 2 data location | No array downloaded in Week 1 | Local later | Deferred and rights-blocked |
| `data/interim/` | NO_CHANGE | A/D | Week 2 generated data | No output in Week 1 | Local later | Deferred |
| `data/processed/` | NO_CHANGE | A/D | Week 3 generated data | No output in Week 1 | Local later | Deferred |
| `Makefile` | NO_CHANGE | A | Avoid parallel automation | Not created in Week 1 | Not applicable | `DEC-007` |

## 11. Expected deliverables

| Deliverable | Roadmap source | Workstream | Repository or local path | Produced by task | Validation evidence |
|---|---|---|---|---|---|
| Clean controlled repository | Week 1 deliverables | A/D | Repository root | W1-A01, W1-A02, W1-D05 | Clean status, remote checks, reviewed commits |
| Passing locked base checks | Week 1 deliverables | A | `scripts/run_checks.py` | W1-A04, W1-A05 | `EVID-W1-CHECKS-001`, exit `0` |
| Passing CI | Automated-check interpretation | A | `.github/workflows/ci.yml` | W1-A06 | Windows and Ubuntu success for implementation SHA |
| README | Week 1 deliverables | A/B/C/D | `README.md` | W1-A02 | Documentation and claims checks |
| Controlled roadmap | Traceability correction | A/B/C/D | `docs/programme/12_week_roadmap.md` | W1-D01 | Hash and body comparison |
| Controlled Week 1 plan | Traceability correction | A/B/C/D | `docs/weekly_plans/week_1_work_plan.md` | W1-D01 | Coverage validator |
| Architecture document | Week 1 deliverables | A | `docs/architecture.md` | W1-A03 | Architecture tests and review |
| Week 2 contract definitions | Stable Week 2 foundation | A | `docs/architecture.md` | W1-A03 | Required field and invariant checks |
| Metric contract | Week 1 technical task | A | `docs/metrics_contract.md` | W1-A07 | Structural and scientific review |
| TPP v0 | Week 1 deliverables | B | `docs/product/target_product_profile_v0.md` | W1-B01 | Claims and completeness review |
| Product open questions | Week 1 product task | B | `docs/product/open_questions_register.md` | W1-B01 | `OQ-*` completeness |
| Evidence ladder | Week 1 deliverables | B/D | `docs/product/evidence_ladder.md` | W1-B02 | Level and claim mapping |
| Company thesis | Week 1 business task | C | `docs/business/company_thesis.md` | W1-C01 | Claims review |
| Stakeholder map | Week 1 deliverables | C/B | `docs/business/stakeholder_map.md` | W1-C01 | Ten-category audit |
| Interview script | Week 1 deliverables | C/B | `docs/business/customer_discovery_interview_script.md` | W1-C02 | Problem-first review |
| Outreach templates | Executability correction | C/B | `docs/business/outreach_templates.md` | W1-C02 | Claims and privacy review |
| Five interview requests | Week 1 gate | C | Public tracker and local private proof | W1-C02 | Five evidence IDs |
| Investment hypotheses | Week 1 business task | C | `docs/business/investment_hypotheses.md` | W1-C03 | Ten-category and falsification audit |
| Claims register | Week 1 deliverables | D | `docs/governance/claims_register.md` | W1-D02 | Claim validator |
| Data governance | Week 1 governance task | D/A | `docs/data_governance.md` | W1-D02 | Split and storage checks |
| Stakeholder privacy policy | Reviewer correction | D/B/C | `docs/governance/privacy_and_stakeholder_data.md` | W1-D02 | Privacy review |
| Technical risk register | Week 1 deliverables | D/A/B | `docs/risk_register.md` | W1-D03 | Score and blocker validation |
| Investment risk register | Week 1 deliverables | D/C | `docs/risk_register_investment.md` | W1-D03 | Score and blocker validation |
| Risk policy | Reviewer correction | D | `docs/governance/risk_scoring_policy.md` | W1-D03 | Arithmetic and threshold check |
| Dataset-rights record | Week 1 governance task | D/A | `docs/governance/dataset_rights.md` | W1-D04 | Authorization decision `DEC-021` |
| Dependency licence register | Week 1 governance task | D/A | `docs/governance/dependency_licence_register.md` | W1-D04 | Full lock reconciliation |
| Ownership and disclosure review | Week 1 governance task | D | `docs/governance/licensing_and_ownership_review.md` | W1-D04 | Public-push decision `DEC-022` |
| Decision log | Week 1 deliverables | D/A | `docs/decision_log.md` | W1-D01 onward | Unique and resolvable decisions |
| Evidence manifest | Reviewer correction | A/B/C/D | `docs/weekly_reports/week_1_evidence_manifest.md` | W1-D05 | Local log hashes and IDs |
| Completion report | Week 1 continuity | A/B/C/D | `docs/weekly_reports/week_1_completion_report.md` | W1-D05 | Exact implementation SHA and observed results |
| Final checklist | Requested execution artifact | A/B/C/D | `docs/weekly_checklist/week_1_completion_checklist.md` | W1-D05 | Checklist coverage validator |

## 12. Definition of done

Week 1 is complete only when every condition below is supported by inspectable evidence.

### 12.1 Functional completion

- The project is an installable packaged application under `src/raman_bacteria_prototype/`.
- `uv lock --check` and `uv sync --locked` return exit code `0`.
- The package and all declared namespaces import.
- The environment, ignore, documentation, test, Ruff, and Black checks are all part of one canonical aggregate runner.
- The canonical runner returns exit code `0` locally and in a clean clone of the verified implementation SHA.

### 12.2 Scientific validity

- Week 2 dataset contracts are documented before implementation.
- The metric contract defines every roadmap metric and selection restriction.
- Train, validation, test, clinical2018, and clinical2019 roles are explicit.
- No test or clinical performance evidence has been inspected.
- No spectrum array has been downloaded or inspected in Week 1.
- No preprocessing or model implementation has been used to make a scientific choice.

### 12.3 Test coverage

- All required test modules exist.
- Positive and negative environment, CLI, runner, documentation, and `.gitignore` behaviors are tested.
- Current executable package branch coverage is at least 90%.
- The canonical runner and CI enforce the same threshold.
- Zero tests fail.

### 12.4 Reproducibility

- The evidence interpreter is Python 3.11.15.
- The required `uv` version is 0.11.29.
- `pyproject.toml` and `uv.lock` remain unchanged during final validation.
- The exact implementation SHA is recorded.
- Clean-clone validation checks out that exact SHA.
- Windows and Ubuntu CI pass for that exact SHA.

### 12.5 Required generated evidence

- Local environment and aggregate-check logs exist in UTF-8.
- Clean-clone logs exist for the exact implementation SHA.
- CI status is recorded for both matrix jobs.
- Every local log has a SHA-256 in the committed evidence manifest.
- Five outreach requests have anonymous evidence IDs and matching private proof.
- No private evidence content is committed.

### 12.6 Documentation

- All paths in the deliverables table exist.
- Required headings and table schemas pass structural validation.
- Internal Markdown links resolve.
- All IDs are unique and referenced IDs exist.
- Manual scientific, product, business, privacy, risk, rights, and ownership reviews record reviewer, date, outcome, and open issues.

### 12.7 Required decisions

- `DEC-001` through `DEC-022` exist or are superseded by explicit recorded decisions.
- `DEC-021` either authorizes Week 2 dataset acquisition based on authoritative rights evidence or explicitly blocks it.
- `DEC-022` authorizes public publication of Week 1 code and documentation before the first public push.
- Every active High or Critical risk has a treatment and blocking decision.

### 12.8 Completion of all four workstreams

- Workstream A has an installable, tested, locked, documented, and CI-validated foundation.
- Workstream B has a TPP, open-question register, and evidence ladder.
- Workstream C has a thesis, stakeholder map, interview script, outreach templates, investment hypotheses, and five sent requests.
- Workstream D has claims, governance, privacy, scored risks, dataset rights, dependency licences, ownership, and traceability.

### 12.9 Git hygiene

- Current remote refs were checked immediately before push.
- No force push occurred.
- Explicit path groups were staged and reviewed.
- No secret, private contact, contract, data array, model binary, generated report, log, cache, or environment was committed.
- Implementation verification and evidence reporting are separate commits.
- The completion report does not claim its own commit SHA.
- Final `git status --short --branch` is clean and tracks `origin/main`.

### 12.10 Week 1 gate

- The repository installs and tests from a clean checkout at the exact implementation SHA.
- Prototype and non-prototype claims are explicit.
- The future use case is written as a testable and falsifiable hypothesis.
- Major technical, clinical, commercial, privacy, rights, and ownership risks are visible.
- At least five stakeholder interviews have been requested with evidence IDs.

### 12.11 Week 2 readiness

- Week 2 architecture and contract names are fixed.
- No Week 1 implementation blocker remains.
- Dataset acquisition proceeds only if `DEC-021` permits it.
- If dataset rights remain `INCOMPLETE`, Week 2 technical acquisition is blocked while non-data interview and competitor work may continue.
- All other Week 2 prerequisites are committed and verified.

## 13. Validation matrix

### 13.1 Ordered validation sequence

| Validation ID | Order | Command or manual check | Purpose | Expected successful result | Expected artifacts | Failure interpretation | Corrective action |
|---|---:|---|---|---|---|---|---|
| `VAL-W1-001` | 1 | `git status --short --branch` | Inspect local state | Valid branch state displayed | Terminal output | Wrong directory, detached state, or unresolved files | Complete W1-A01 reconciliation |
| `VAL-W1-002` | 2 | `git fetch --prune origin; git ls-remote --heads origin` | Refresh remote state | Current refs known | Terminal output | Remote changed or inaccessible | Inspect and reconcile, never force push |
| `VAL-W1-003` | 3 | `git config user.name; git config user.email` | Verify authorship | Intended non-empty values | Terminal output | Missing or inappropriate identity | Set repository-local identity |
| `VAL-W1-004` | 4 | `uv --version` | Verify required tool | `uv 0.11.29` | Evidence log | Wrong tool version | Install or select required version |
| `VAL-W1-005` | 5 | `uv run --locked python --version` | Verify evidence interpreter | `Python 3.11.15` | Evidence log | Wrong patch or Python family | Install/select 3.11.15 and resync |
| `VAL-W1-006` | 6 | `uv lock --check` | Prove lock freshness | Exit `0`, no file changes | Terminal and log | Lock differs from project metadata | Intentionally run `uv lock`, review and commit lock change |
| `VAL-W1-007` | 7 | `uv sync --locked` | Reproduce environment | Exit `0` | `.venv/` | Missing or incompatible lock/dependency | Correct project or lock intentionally |
| `VAL-W1-008` | 8 | `uv run --locked python scripts/check_environment.py` | Validate package and repository foundation | All required checks pass, exit `0` | Structured output | Missing path, invalid TOML, version, root, or import | Fix reported condition |
| `VAL-W1-009` | 9 | `uv run --locked python scripts/check_gitignore.py` | Verify every ignore and negation | Every individual assertion passes | Structured output | Generated/private path may be trackable or policy file ignored | Correct `.gitignore` and rerun |
| `VAL-W1-010` | 10 | `uv run --locked python scripts/check_documentation.py` | Validate document structure and traceability | Required documents, headings, tables, links, IDs, and coverage pass | Structured output | Missing requirement, broken link, duplicate or unresolved ID | Correct documents and mappings |
| `VAL-W1-011` | 11 | `uv run --locked python -m pytest -q --cov=raman_bacteria_prototype --cov-branch --cov-report=term-missing --cov-report=xml:coverage.xml --cov-fail-under=90` | Execute tests and enforce coverage | Zero failures, coverage at least 90%, exit `0` | `coverage.xml`, local caches | Defect, missing negative test, or low coverage | Fix code/tests without lowering gate |
| `VAL-W1-012` | 12 | `uv run --locked python -m ruff check .` | Lint and import checks | No violations, exit `0` | Output log | Static defect | Correct source or justified config |
| `VAL-W1-013` | 13 | `uv run --locked python -m black --check .` | Format check | No file requires formatting, exit `0` | Output log | Formatting drift | Run Black, inspect diff, rerun |
| `VAL-W1-014` | 14 | `uv run --locked python scripts/run_checks.py` | Canonical aggregate gate | Seven checks recorded, overall PASS, exit `0` | JSON result and log | Any mandatory check failed or runner defect | Correct first causal defect and rerun all |
| `VAL-W1-015` | 15 | `git diff -- pyproject.toml uv.lock` before and after validation | Prove validation is non-mutating | No diff created by validation | Git output | Command changed metadata or lock | Replace non-locked command and restore reviewed state |
| `VAL-W1-016` | 16 | Manual claims and split review | Scientific and communications control | Reviewer records PASS or controlled actions | Review record | Overclaiming or leakage ambiguity | Correct documents before commit |
| `VAL-W1-017` | 17 | Manual TPP and evidence-ladder review | Product completeness | All required fields and claim boundaries accepted | Review record | Vague or unsupported use case | Revise TPP and claims |
| `VAL-W1-018` | 18 | Manual stakeholder and outreach review | Business and privacy gate | Five requests, three categories, safe evidence | Tracker and private proof | Requests unsent or privacy issue | Send or correct records |
| `VAL-W1-019` | 19 | Manual risk review | Blocker control | All High/Critical risks have decisions | Risk review record | Uncontrolled blocker | Treat or explicitly block gate |
| `VAL-W1-020` | 20 | Manual dataset-rights review | Week 2 acquisition authorization | `DEC-021` is explicit | Rights record | Rights unclear | Keep acquisition blocked and escalate |
| `VAL-W1-021` | 21 | Manual ownership/disclosure review | Public-push authority | `DEC-022` permits publication | Ownership record | Credible third-party claim or disclosure risk | Stop public push, seek advice |
| `VAL-W1-022` | 22 | `git diff --cached --name-status; git diff --cached --check; git diff --cached` | Review explicit staging | Only intended reviewed files staged | Staged diff | Private/generated or unintended files staged | Unstage and correct policy |
| `VAL-W1-023` | 23 | Secret and privacy scan of staged content | Prevent disclosure | No credential, private identity, contract, or data array | Review record | Sensitive content present | Remove, rotate if needed, and review history |
| `VAL-W1-024` | 24 | Push implementation commits | Establish exact candidate SHA | Push succeeds without force | Remote implementation SHA | Remote changed or auth failed | Fetch, inspect, reconcile, revalidate |
| `VAL-W1-025` | 25 | Clean-clone sequence at exact implementation SHA | Prove fresh reproducibility | Locked sync and aggregate runner exit `0` | `EVID-W1-CLONE-001` | Missing committed file, path assumption, or non-reproducibility | Fix, create new implementation SHA, repeat |
| `VAL-W1-026` | 26 | GitHub Actions status for exact implementation SHA | Repository-hosted validation | Windows and Ubuntu jobs both `success` | CI run IDs/status | Platform issue or project defect | Inspect logs, fix, produce new SHA, repeat |
| `VAL-W1-027` | 27 | Hash all retained evidence logs | Evidence integrity | SHA-256 recorded for every local log | Evidence manifest | Missing, mutable, or mismatched log | Regenerate or correct manifest |
| `VAL-W1-028` | 28 | Commit and push evidence report | Preserve observed verdict | Separate evidence commit succeeds | Report commit | Circular or incomplete evidence | Correct report without self-reference |
| `VAL-W1-029` | 29 | `git status --short --branch` | Final hygiene | Clean tree tracking `origin/main` | Terminal output | Uncommitted or untracked item | Classify, commit, ignore, or remove safely |
| `VAL-W1-030` | 30 | Post-push reviewer input | Enable independent review | Final report commit SHA and verified implementation SHA supplied | Reviewer input | Wrong or ambiguous revision | Re-read Git output and provide exact SHAs |

### 13.2 Command properties

| Validation ID | Requires local dataset? | Modifies generated outputs? | Safe to rerun? | Success exit code | Files expected to appear or change | Evidence retained |
|---|---:|---:|---:|---:|---|---|
| `VAL-W1-004` | No | No | Yes | `0` | None | Tool version log |
| `VAL-W1-005` | No | May create `.venv` if not synced | Yes | `0` | `.venv/` only | Python version log |
| `VAL-W1-006` | No | No | Yes | `0` | None | Lock-check output |
| `VAL-W1-007` | No | Yes, `.venv/` | Yes | `0` | `.venv/` | Sync output |
| `VAL-W1-008` | No | No | Yes | `0` | None | Environment log |
| `VAL-W1-009` | No | May create temporary placeholder paths in a temp area | Yes | `0` | No committed change | Ignore-check output |
| `VAL-W1-010` | No | No | Yes | `0` | None | Documentation-check output |
| `VAL-W1-011` | No | Yes, coverage and caches | Yes | `0` | `coverage.xml`, ignored caches | Test and coverage log |
| `VAL-W1-012` | No | Cache only | Yes | `0` | `.ruff_cache/` | Ruff log |
| `VAL-W1-013` | No | No in check mode | Yes | `0` | None | Black log |
| `VAL-W1-014` | No | Logs, coverage, caches | Yes | `0` | Stable JSON result, ignored caches | Aggregate log and JSON hash |
| `VAL-W1-025` | No | Temporary clone and `.venv` | Yes after removing prior temp clone | `0` | Temporary clone | Clean-clone log and hash |
| `VAL-W1-026` | No | CI cache only | New run per SHA | Job `success` | GitHub Actions records | Run IDs and status summary |

### 13.3 Canonical aggregate command

The canonical Week 1 local technical gate is:

```powershell
uv lock --check
uv sync --locked
uv run --locked python scripts/run_checks.py
```

The first two commands prove the environment can be resolved from a current lock. The third runs the complete non-mutating validation suite. A Makefile is not created.

## 14. Expected validation outputs

These are expected formats, not claims that the commands have already passed.

### 14.1 Environment validator

```text
CHECK ENV-PYTHON ........ PASS
CHECK ENV-UV ............ PASS
CHECK ENV-ROOT .......... PASS
CHECK ENV-PYPROJECT ..... PASS
CHECK ENV-LOCK .......... PASS
CHECK ENV-STRUCTURE ..... PASS
CHECK ENV-PACKAGE ....... PASS
OVERALL ENVIRONMENT ..... PASS
```

### 14.2 Ignore validator

```text
IGNORED .venv/placeholder.txt ................ PASS
IGNORED .env .................................. PASS
IGNORED data/raw/placeholder.npy .............. PASS
TRACKABLE .env.example ........................ PASS
TRACKABLE data/README.md ...................... PASS
TRACKABLE models/README.md .................... PASS
TRACKABLE reports/README.md ................... PASS
OVERALL GITIGNORE ............................. PASS
```

Every path must have its own result. A single successful `git check-ignore` invocation is insufficient.

### 14.3 Documentation validator

```text
DOCUMENTS REQUIRED PATHS ...................... PASS
DOCUMENTS REQUIRED HEADINGS ................... PASS
DOCUMENTS REQUIRED TABLE SCHEMAS .............. PASS
DOCUMENTS UNIQUE IDS .......................... PASS
DOCUMENTS REFERENCES .......................... PASS
DOCUMENTS INTERNAL LINKS ...................... PASS
DOCUMENTS ROADMAP COVERAGE .................... PASS
DOCUMENTS CLAIM CONTEXT ....................... PASS
OVERALL DOCUMENTATION ......................... PASS
```

### 14.4 Pytest and coverage

Expected properties:

```text
0 failed
0 errors
branch coverage >= 90%
coverage.xml created
exit code 0
```

The exact test count must be reported from observed output and must not be predetermined.

### 14.5 Aggregate runner

```text
CHECK-01 uv lock --check ...................... PASS [0]
CHECK-02 environment .......................... PASS [0]
CHECK-03 gitignore ............................ PASS [0]
CHECK-04 documentation ........................ PASS [0]
CHECK-05 pytest and coverage .................. PASS [0]
CHECK-06 ruff ................................. PASS [0]
CHECK-07 black ................................ PASS [0]
OVERALL ....................................... PASS [0]
RESULT JSON ................................... <repository-relative local path>
```

### 14.6 CI

Expected matrix result for the verified implementation SHA:

| Job | Expected conclusion |
|---|---|
| `windows-latest` | `success` |
| `ubuntu-latest` | `success` |

### 14.7 Completion report

The report must include these exact fields:

```text
verified_implementation_commit_sha:
roadmap_sha256:
python_version:
uv_version:
local_check_exit_code:
clean_clone_exit_code:
ci_windows_status:
ci_ubuntu_status:
dataset_acquisition_decision:
public_push_decision:
outreach_evidence_ids:
active_blocking_risk_ids:
week_2_readiness_verdict:
```

It must not include a field claiming the SHA of the commit that contains the report itself.

## 15. Common mistakes and failure modes

| Mistake | Why it is harmful | How to detect it | Prevention |
|---|---|---|---|
| Treating the inspection-time empty repository as permanently empty | Remote work may appear before execution | `git ls-remote --heads origin` differs from snapshot | Recheck remote before initialization and push |
| Running initialization before preserving local files | Can destroy or duplicate unpushed work | Local inventory contains files not accounted for | Complete W1-A01 and external backup |
| Running `uv init` without `--vcs none` inside an existing Git repository | Creates conflicting VCS behavior | Unexpected Git initialization or files | Use exact case-based initialization flow |
| Using the library template unintentionally | Adds library-specific structure and changes packaging semantics | `py.typed` or template files appear unexpectedly | Use packaged application decision `DEC-002` |
| Running `uv sync --frozen` as a freshness gate | It skips lock freshness validation | Stale lock still installs | Use `uv lock --check` and `uv sync --locked` |
| Running plain `uv run` during final validation | May update the lock automatically | `git diff` shows lock changes | Use `uv run --locked` and non-mutation check |
| Duplicating project version in `__init__.py` | Version can drift | Metadata and code literals disagree | Read version from `importlib.metadata` |
| Creating a runner that stops after the first failure | Hides other defects | Summary has missing mandatory checks | Run all checks and combine statuses |
| Allowing failed children to produce PASS | Creates false evidence | Negative runner test | Explicit nonzero overall status |
| Omitting coverage from the aggregate runner | Canonical command may pass below threshold | Standalone test differs from aggregate behavior | Put exact coverage command in runner |
| Testing only happy paths | Failure claims remain unverified | Required negative test absent | Implement W1-A05 test matrix |
| Relying on one multi-path `git check-ignore` exit code | Proves only one or more paths matched | Non-matching path omitted | Test each path independently |
| Ignoring policy README files through broad directory rules | Removes committed governance markers | `data/README.md` is ignored | Required negation tests |
| Scanning forbidden phrases without context | Flags the claims register itself | False failures in governance documents | Use path and section allowlist |
| Using unpinned GitHub Actions or tool versions | CI can change without a code change | Workflow uses tags such as `latest` | Pin action commits and `uv` version |
| Letting CI replace local clean-clone evidence | Platform-specific local defects may remain | No local exact-SHA log | Require both evidence types |
| Writing the report before verifying the pushed implementation SHA | Produces circular or inaccurate evidence | Report precedes clean-clone and CI | Use the three-stage finalization sequence |
| Trying to place the report commit SHA inside the same report commit | Creates impossible self-reference | Editing report changes SHA | Record only verified implementation SHA; supply report SHA externally |
| Using `git add .` | Can stage private or generated files | Staged list contains unexpected paths | Stage explicit reviewed path groups |
| Force-pushing after remote change | Can destroy remote history | Reflog or push command | Prohibit force pushes and reconcile normally |
| Treating the code repository MIT licence as a dataset licence | Software licence may not cover hosted arrays | No dataset-specific terms | Keep rights status `INCOMPLETE` until authoritative evidence |
| Downloading arrays to inspect their metadata in Week 1 | Violates the Week 1 scope and rights gate | Data files or download logs exist | Inspect publication and rights metadata only |
| Reviewing only direct dependency licences | Omits transitive obligations | Lock contains unregistered packages | Reconcile every locked component |
| Treating `uv tree` as a licence inventory | Dependency structure does not prove licence | Register lacks authoritative licence sources | Verify each component separately |
| Committing employment or academic contracts | Exposes confidential information | Staged diff contains contract text | Record only conclusions and evidence references |
| Leaving ownership uncertainty undefined | Public push may violate third-party rights | `DEC-022` absent or vague | Apply explicit public-push blocker rule |
| Sending product-pitch interviews | Produces confirmation bias | Script asks whether recipient likes the solution | Ask about current workflow before product explanation |
| Recording interviews without consent | Creates privacy and trust risks | Consent field absent | No recording by default, note-taking consent required |
| Committing contact details or message bodies | Public privacy breach | Staged privacy scan | Anonymous IDs and private crosswalk |
| Using vague risks without scoring or treatment | Gate decisions become subjective | Missing residual score or treatment | Enforce exact risk schema |
| Building data loaders, preprocessing, or models in Week 1 | Premature later-week scope and leakage risk | Scientific implementation appears outside environment utilities | Scaffold namespaces only |
| Claiming tests or CI pass without observed output | Confuses planned and verified evidence | Evidence manifest lacks log or run ID | Require observed exit codes and hashes |

## 16. Explicitly deferred work

| Deferred item | Owning week | Why premature now | Required prior evidence or gate | Early scaffolding allowed |
|---|---:|---|---|---|
| Download public Raman spectrum arrays | Week 2 | Dataset rights are not yet established and Week 1 is foundation work | `DEC-021` must authorize acquisition | Publication and licence metadata review only |
| Implement data loader | Week 2 | File contracts and rights gate must be fixed first | W1-A03 contracts and Week 2 entry gate | `data` namespace only |
| Implement array, dtype, label, axis, duplicate, and range checks | Week 2 | Requires actual authorized files | Validated download and manifest | `data_validation` namespace and documented contracts |
| Implement spectral quality-control flags | Week 2 | Thresholds require inspected spectra and documented evidence | Week 2 data validation | `spectral_qc` namespace only |
| Generate interim dataset, split summaries, spectra plots, or exploration notebook | Week 2 | No array may be opened in Week 1 | Data rights and validation | Notebook policy only |
| Implement P1 to P4 preprocessing | Week 3 | Requires validated input and train-only fit policy | Week 2 gate | Preprocessing namespace only |
| Train or compare any model | Week 4 | Preprocessing candidates must be controlled first | Week 3 gate | Modelling namespace and metric contract only |
| Use model performance to choose preprocessing | Never in Week 3 | Violates the roadmap selection discipline | Later model-development protocol | None |
| Inspect test performance | Week 6 | Test is reserved for locked internal evaluation | Model lock and predeclared analysis | File-integrity checks only in Week 2 |
| Inspect clinical2018 or clinical2019 performance | Week 7 | Clinical splits are reserved for domain-shift evaluation | Week 6 model lock | Transformation-integrity checks only before Week 7 |
| Fit calibration, rejection, or OOD thresholds | Week 8 | Requires a selected and locked model workflow | Earlier modelling and validation outputs | Metric definitions only |
| Build report generator | Week 9 | Prediction, uncertainty, and status contracts are not stable | Week 8 gate | Reporting namespace only |
| Build Streamlit demonstrator | Week 10 | Outputs and safety logic are not ready | Week 9 report contract | No UI scaffolding needed |
| Make definitive IVDR classification | Later governance review | Depends on exact intended purpose and professional advice | Narrow intended use and regulatory consultation | Record open question and no definitive class |
| Add repository `LICENSE` | After ownership and licensing decision | User may not yet have authority to grant rights | Controlled decision based on ownership review | Licence strategy discussion only |
| Formal Version 0.1 software bill of materials | Week 6 | Roadmap assigns software-version freeze later | Locked model and software version | Provisional Week 1 dependency inventory allowed |
| Patent landscape and publication landscape | Week 3 onward | Roadmap assigns preliminary landscape later | Product hypothesis and disclosure policy | Record publication-risk question only |
| Diagnostic, treatment, hospital, regulatory, or blood-product claims | Only after corresponding evidence level | Current evidence cannot support them | Evidence ladder exit gates | Explicit prohibited-claim documentation |

## 17. Coverage audit

### 17.1 Roadmap technical and scientific task coverage

| Roadmap task | Task ID | Deliverable | Validation ID |
|---|---|---|---|
| Create repository structure | W1-A02 | Root and policy directories | `VAL-W1-008`, `VAL-W1-010` |
| Initialize `pyproject.toml` | W1-A02, W1-A04 | `pyproject.toml` | `VAL-W1-006`, `VAL-W1-008` |
| Initialize `uv.lock` | W1-A02 | `uv.lock` | `VAL-W1-006`, `VAL-W1-007` |
| Initialize `.python-version` | W1-A02 | `.python-version` | `VAL-W1-005` |
| Initialize `.gitignore` | W1-A02 | `.gitignore` | `VAL-W1-009` |
| Initialize README | W1-A02 | `README.md` | `VAL-W1-010` |
| Pin Python 3.11 | W1-A02 | `.python-version`, `pyproject.toml` | `VAL-W1-005` |
| Use `uv` | W1-A02, W1-A04 | project/tool contract | `VAL-W1-004`, `VAL-W1-006`, `VAL-W1-007` |
| Add environment validation | W1-A04 | environment module and script | `VAL-W1-008` |
| Add Pytest | W1-A04, W1-A05 | tests and config | `VAL-W1-011` |
| Add Ruff | W1-A04 | Ruff config | `VAL-W1-012` |
| Add Black | W1-A04 | Black config | `VAL-W1-013` |
| Define package architecture | W1-A03 | `docs/architecture.md`, namespaces | `VAL-W1-008`, `VAL-W1-010`, `VAL-W1-011` |
| Write metric contract | W1-A07 | `docs/metrics_contract.md` | `VAL-W1-010`, `VAL-W1-016` |

### 17.2 Product and clinical task coverage

| Roadmap task | Task ID | Deliverable | Validation ID |
|---|---|---|---|
| Write TPP v0 | W1-B01 | `docs/product/target_product_profile_v0.md` | `VAL-W1-017` |
| Define first product hypothesis | W1-B01 | TPP hypothesis section | `VAL-W1-017` |
| Document nine open questions | W1-B01 | `docs/product/open_questions_register.md` | `VAL-W1-010`, `VAL-W1-017` |
| Create evidence ladder | W1-B02 | `docs/product/evidence_ladder.md` | `VAL-W1-010`, `VAL-W1-017` |

### 17.3 Business and investment task coverage

| Roadmap task | Task ID | Deliverable | Validation ID |
|---|---|---|---|
| Write company thesis | W1-C01 | `docs/business/company_thesis.md` | `VAL-W1-010`, `VAL-W1-016` |
| Define stakeholder map | W1-C01 | `docs/business/stakeholder_map.md` | `VAL-W1-018` |
| Create problem-focused interview script | W1-C02 | interview script | `VAL-W1-018` |
| Create investment hypotheses | W1-C03 | investment register | `VAL-W1-010`, `VAL-W1-019` |
| Request five interviews | W1-C02 | public tracker and private proof | `VAL-W1-018` |

### 17.4 Governance, regulation, and IP task coverage

| Roadmap task | Task ID | Deliverable | Validation ID |
|---|---|---|---|
| Write allowed claims | W1-D02 | claims register | `VAL-W1-016` |
| Write forbidden claims | W1-D02 | claims register | `VAL-W1-010`, `VAL-W1-016` |
| Create technical risk register | W1-D03 | `docs/risk_register.md` | `VAL-W1-019` |
| Create investment risk register | W1-D03 | `docs/risk_register_investment.md` | `VAL-W1-019` |
| Create decision log | W1-D01 | `docs/decision_log.md` | `VAL-W1-010` |
| Create data governance | W1-D02 | `docs/data_governance.md` | `VAL-W1-010`, `VAL-W1-016` |
| Review dependency licences | W1-D04 | dependency register | `VAL-W1-019`, manual reconciliation |
| Review public-dataset terms | W1-D04 | dataset-rights record | `VAL-W1-020` |
| Review academic-work code ownership | W1-D04 | ownership review | `VAL-W1-021` |

### 17.5 Deliverable coverage

| Roadmap deliverable | Task ID | Repository or evidence path | Pass condition |
|---|---|---|---|
| Clean repository | W1-A01, W1-A02, W1-D05 | repository root | Exact-SHA verification and clean final status |
| Passing base checks | W1-A04, W1-A05, W1-A06 | local logs and CI | Local, clean clone, Windows CI, Ubuntu CI all pass |
| README | W1-A02 | `README.md` | Structural and manual review pass |
| Architecture document | W1-A03 | `docs/architecture.md` | Exact contracts and tests pass |
| TPP v0 | W1-B01 | TPP path | Product and claims review pass |
| Evidence ladder | W1-B02 | evidence-ladder path | Level and claim mapping complete |
| Claims register | W1-D02 | claims path | Allowed and forbidden controls pass |
| Technical risk register | W1-D03 | technical register | All mandatory risks scored and controlled |
| Investment risk register | W1-D03 | investment register | All mandatory risks scored and controlled |
| Customer-discovery script | W1-C02 | interview script | Problem-first and privacy-safe |
| Initial stakeholder list | W1-C01 | stakeholder map | All ten roadmap categories present |

### 17.6 Gate coverage

| Week 1 gate condition | Task IDs | Evidence required |
|---|---|---|
| Repository installs and tests from scratch | W1-A02, W1-A04, W1-A05, W1-A06, W1-D05 | Exact implementation SHA, clean-clone exit `0`, both CI jobs success |
| Prototype and non-prototype claims explicit | W1-D02, W1-B01, W1-B02 | Claims review and document checks |
| Future use case is testable | W1-B01 | Falsifiable TPP hypothesis and review record |
| Major technical, clinical, and commercial risks visible | W1-D03, W1-D04 | Scored registers and blocker decisions |
| At least five stakeholder interviews requested | W1-C02 | Five anonymous evidence IDs with private proof |

### 17.7 Four-workstream audit

| Workstream | Required Week 1 evidence | Task IDs | Coverage verdict before execution |
|---|---|---|---|
| A: Technical and scientific | Packaged project, architecture, metrics, checks, tests, CI, reproducibility | W1-A01 to W1-A07 | `MISSING` until implemented |
| B: Product and clinical translation | TPP, open questions, evidence ladder | W1-B01, W1-B02 | `MISSING` until implemented |
| C: Business and investment | Thesis, stakeholders, script, templates, five requests, hypotheses | W1-C01 to W1-C03 | `MISSING` until implemented |
| D: Governance, regulation and IP | Controlled requirements, claims, data governance, privacy, risks, rights, licences, ownership, evidence | W1-D01 to W1-D05 | `MISSING` or `INCOMPLETE` until implemented |

## Weekly checklist

### Scope and entry gate

- [ ] Run `git status --short --branch` and record `EVID-W1-GIT-001`.
- [ ] Run `git fetch --prune origin` and `git ls-remote --heads origin`; record the execution-time remote state.
- [ ] Confirm or correct `origin` to `https://github.com/Damien-Ergun/synapse-ai.git`.
- [ ] Confirm the working branch is not detached and is named `main`, or record an approved reconciliation decision.
- [ ] Run `git config user.name` and `git config user.email`; confirm both values are intentional.
- [ ] Inventory every local file outside `.git/` and `.venv/` and preserve any unpushed work.
- [ ] Confirm no force-push operation will be used during Week 1.
- [ ] Confirm no secret, patient data, private contact crosswalk, contract, or confidential institutional material is inside the intended commit set.
- [ ] Record `DEC-022` permitting public publication before the first public push.

### Controlled requirements and decisions

- [ ] Create `docs/programme/12_week_roadmap.md` with source filename, SHA-256 `c993737a6b4d299e9a264bb9a5e3cb0a9105f964854adc5b14e76e42dff7d1a3`, adoption date, status, and supersession rule.
- [ ] Create `docs/weekly_plans/week_1_work_plan.md` containing the complete approved Week 1 guide.
- [ ] Create `docs/decision_log.md` before project initialization.
- [ ] Add complete `DEC-001` through `DEC-012` records before dependent implementation begins.
- [ ] Create `docs/traceability/week_1_coverage_matrix.md` and map every roadmap task, deliverable, and gate condition.
- [ ] Confirm every `DEC-*`, `RISK-*`, `CLAIM-*`, `OQ-*`, `METRIC-*`, `VAL-*`, and `EVID-*` reference resolves.

### Workstream A: Technical and scientific

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

### Workstream B: Product and clinical translation

- [ ] Create `docs/product/target_product_profile_v0.md` with every required section from W1-B01.
- [ ] Put the research-use-only notice before the product description.
- [ ] State the exact current Prototype 0 user, setting, controlled input, output, evidence level, and exclusions.
- [ ] Define one provisional future use-case hypothesis with population, sample type, operator, decision, comparator, reference standard, turnaround hypothesis, actions, and falsification conditions.
- [ ] Label every unsupported product field `HYPOTHESIS`.
- [ ] Create `docs/product/open_questions_register.md` with all nine roadmap questions and complete `OQ-*` records.
- [ ] Create `docs/product/evidence_ladder.md` with Levels 0 through 5, permitted claims, prohibited claims, evidence, reviewers, and exit gates.
- [ ] Mark current status `Level 0: IN_PROGRESS`.
- [ ] Add `DEC-019`.

### Workstream C: Business and investment

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

### Workstream D: Governance, regulation and IP

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

### Tests and validation

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

### Generated evidence

- [ ] Create `scripts/invoke_logged_command.ps1` and test success, failure, UTF-8, stdout, stderr, and child-exit preservation.
- [ ] Create `reports/logs/week_1/EVID-W1-ENV-001.txt` with command, timestamps, OS, repository-relative working directory, Git SHA, Python, `uv`, stdout, stderr, and exit code.
- [ ] Create `reports/logs/week_1/EVID-W1-CHECKS-001.txt` for the canonical aggregate command.
- [ ] After implementation push, create `reports/logs/week_1/EVID-W1-CLONE-001.txt` for the exact implementation SHA.
- [ ] Record both CI job statuses and run identifiers as `EVID-W1-CI-001`.
- [ ] Retain private sent-message evidence for the five outreach evidence IDs outside Git.
- [ ] Calculate SHA-256 for every retained local evidence log.
- [ ] Create `docs/weekly_reports/week_1_evidence_manifest.md` without private content or absolute machine paths.

### Documentation and decisions

- [ ] Run the documentation validator and resolve every missing heading, table column, duplicate ID, unresolved reference, broken link, coverage gap, and forbidden-claim context error.
- [ ] Confirm the TPP, claims register, evidence ladder, data governance, architecture, metrics, hypotheses, risks, rights, and decisions cross-link correctly.
- [ ] Record reviewer, review date, outcome, and open actions for each manual review.
- [ ] Update `docs/traceability/week_1_coverage_matrix.md` with final validation and evidence IDs.
- [ ] Create `docs/weekly_checklist/week_1_completion_checklist.md` from this checklist.

### Reproducibility and CI

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

### Completion report and Git hygiene

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
