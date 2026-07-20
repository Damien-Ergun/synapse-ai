# Architecture

## 1. Scope and component status

Only environment validation, repository validation, documentation validation, and aggregate checks are **IMPLEMENTED** in Week 1. Scientific pipeline namespaces are **SCAFFOLDED** or **DEFERRED**. No placeholder function may fabricate data or predictions.

| Component | Package | Owner | Week 1 status | Responsibility |
|---|---|---|---|---|
| Core contracts | `core` | Technical lead | SCAFFOLDED | Shared immutable contracts and exceptions |
| Data loading | `data` | Data lead | SCAFFOLDED | Dataset discovery and loading after rights authorization |
| Data validation | `data_validation` | Data-quality lead | SCAFFOLDED | Dataset integrity checks and validation reports |
| Spectral QC | `spectral_qc` | Spectroscopy lead | SCAFFOLDED | Sample-level quality flags |
| Preprocessing | `preprocessing` | Spectroscopy lead | DEFERRED | Controlled fitted transformations |
| Features | `features` | ML lead | DEFERRED | Feature construction |
| Modelling | `modelling` | ML lead | DEFERRED | Estimator interfaces and training |
| Calibration | `calibration` | ML lead | DEFERRED | Probability calibration |
| Evaluation | `evaluation` | Scientific lead | DEFERRED | Metrics and locked evaluation |
| Reporting | `reporting` | Product lead | DEFERRED | Immutable result presentation |
| Prediction | `prediction` | ML lead | DEFERRED | Approved-component orchestration |
| Tracking | `tracking` | Reproducibility lead | DEFERRED | Config, manifest, seed, software, and artifact records |
| Environment checks | `environment` | Engineering lead | IMPLEMENTED | Pure, testable repository and toolchain checks |
| Aggregate checks | `checks` | Engineering lead | IMPLEMENTED | Deterministic mandatory validation sequence |

## 2. Allowed dependency directions

`core` imports no feature package. `data` may depend on `core`. `data_validation` and `spectral_qc` may depend on `core` and `data` contracts. `preprocessing` may depend on validated data contracts but not modelling or evaluation. `features` may depend on preprocessing outputs. `modelling` may depend on features and core interfaces. `calibration` and `evaluation` may consume model outputs. `reporting` consumes immutable results and cannot alter predictions. `prediction` orchestrates approved fitted components. `tracking` records metadata and hashes without making scientific decisions.

## 3. Prohibited dependencies

- No model import in data ingestion.
- No evaluation import in preprocessing.
- No test or clinical performance access in development selection.
- No production-only logic in notebooks.
- No hidden scientific settings sourced from environment variables.

## 4. Repository root and path policy

Runtime utilities resolve the root from an explicit path or by walking from the installed source or script location until both `pyproject.toml` and `docs/weekly_plans/week_1_work_plan.md` are found. Current working directory is never treated as authoritative. Stored paths are repository-relative and use POSIX separators in manifests.

## 5. Configuration contract

Human-authored controlled configs live under `configs/`, use UTF-8 TOML, contain `schema_version`, and pass schema validation before use. Scientific settings must be visible in committed configuration or a recorded experiment configuration.

## 6. Canonical hashing

Validated configuration is converted to canonical JSON with sorted keys, compact separators, UTF-8 encoding, and rejection of NaN or Infinity. SHA-256 is computed over those bytes. Records include `canonicalization_version = "1"`. Artifact names use:

```text
{artifact_type}__{dataset_id}__{split}__{config_hash_12}__{run_id}.{ext}
```

## 7. Random-seed policy

Every stochastic run has an explicit integer seed in configuration, logs, and experiment records. Pipeline code may not rely on unseeded global Python or NumPy state.

## 8. Logging and errors

Use the standard `logging` library with module loggers and stable fields for run ID, task ID, artifact ID, and split. Never log patient information, contact details, credentials, or spectrum payloads. User-facing errors are separated from debug traces.

Future exception hierarchy: `RamanPrototypeError`, `ConfigurationError`, `DataContractError`, `DataIntegrityError`, `AxisMismatchError`, and `ArtifactVerificationError`.

Validation severities are `INFO`, `WARNING`, `ERROR`, and `FATAL`.

## 9. Week 2 contract definitions

### `SplitName`

Closed values: `train`, `validation`, `test`, `clinical2018`, and `clinical2019`.

### `DatasetDescriptor`

Required fields: `dataset_id`, `title`, `version`, `source_uri`, `publication_doi`, `retrieved_at_utc`, `rights_record_id`, `expected_splits`, `class_metadata_source`, and `axis_source`.

### `FileManifestEntry`

Required fields: `relative_path`, `byte_size`, `sha256`, `split`, `role`, `media_type`, `created_at_utc`, and `source_file_name`.

### `SpectrumBatch`

Required fields: `spectra`, `labels`, `sample_ids`, `wavenumbers`, `split`, immutable metadata mapping, and source-manifest hash. Shapes are `(n_samples, n_wavenumbers)`, `(n_samples,)`, `(n_samples,)`, and `(n_wavenumbers,)` respectively.

### `ValidationIssue`

Required fields: `issue_id`, `check_id`, `severity`, `message`, `split`, optional `sample_id`, optional `feature_index`, and evidence fields.

### `ValidationReport`

Required fields: report ID, dataset ID, manifest ID, checks run, issues, counts by severity, pass/fail decision, software version, configuration hash, start timestamp, and finish timestamp.

### `QualityFlag`

Required fields: stable code, severity, sample ID, measured value, threshold identifier, message, and source check ID.

## 10. Preservation invariants

Contract objects are immutable when implemented. Every transformation preserves ordered `sample_ids` unless a filtering artifact records removed IDs and reasons. Labels cannot change during preprocessing. The spectral axis is one-dimensional, finite, strictly monotonic, records orientation and unit `cm^-1`, and is never reversed implicitly. Metadata propagates through every artifact with source-manifest and configuration hashes.
