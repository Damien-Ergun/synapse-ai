# Synapse AI

Research-use-only Raman microorganism candidate-identification prototype. Not clinically validated and not intended for patient management.

## Week 1 foundation

Requirements: Python 3.11, uv, and Docker Compose for service smoke tests.

```bash
uv sync --all-groups --locked
uv run ruff check .
uv run ruff format --check .
uv run pyright
uv run pytest
uv run inspect-dataset --help
docker compose up --build
```

Raw Raman arrays are immutable inputs and remain outside Git. Generate the authoritative machine-readable inventory with the explicit holdout metadata-audit gate:

```bash
SYNAPSE_HOLDOUT_METADATA_AUDIT=1 uv run inspect-dataset manifest /path/to/data -o data-manifests/dataset-manifest.json
```

The authoritative manifest has a stable schema and canonical file order. Cross-split exact-duplicate results are intentionally stored separately in `data-manifests/cross-split-duplicates.json`.

Verify that the committed authoritative manifest is reproducible from the current generator, ignoring only the nondeterministic `generated_at` value:

```bash
SYNAPSE_HOLDOUT_METADATA_AUDIT=1 uv run inspect-dataset verify-manifest /path/to/data --committed-manifest data-manifests/dataset-manifest.json
```

The manifest workflow refuses incomplete or unexpected NPY inventories and validates X/y observation counts plus spectral feature count against the Raman axis.

Clinical 2019 is a locked final-evaluation holdout. Ordinary development loading rejects canonical clinical2019 paths and any aliased file whose SHA-256 matches a frozen holdout identity. See `docs/clinical2019-holdout.md`.

Layout: `packages/synapse-core`, `packages/synapse-api`, `packages/synapse-ui`, `configs`, `data-manifests`, `tests`, `docs`, `artifacts`, `reports`, `notebooks`.

Week 1 deliberately contains no predictive model training.
