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

Raw Raman arrays are immutable inputs and remain outside Git. Generate the machine-readable inventory with:

```bash
SYNAPSE_HOLDOUT_METADATA_AUDIT=1 uv run inspect-dataset manifest /path/to/data -o data-manifests/dataset-manifest.json
```

Clinical 2019 is a locked final-evaluation holdout. Ordinary development loading is rejected by code. See `docs/clinical2019-holdout.md`.

Layout: `packages/synapse-core`, `packages/synapse-api`, `packages/synapse-ui`, `configs`, `data-manifests`, `tests`, `docs`, `artifacts`, `reports`, `notebooks`.

Week 1 deliberately contains no predictive model training.
