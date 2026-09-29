from __future__ import annotations

import json
from datetime import UTC, datetime
from pathlib import Path
from typing import Annotated

import typer

from synapse_core.audit import inspect_npy

app = typer.Typer(help="Synapse AI Week 1 dataset audit utilities.")


@app.command()
def inspect(path: Annotated[Path, typer.Argument(exists=True, readable=True)]) -> None:
    typer.echo(json.dumps(inspect_npy(path), indent=2, sort_keys=True))


@app.command()
def manifest(
    data_dir: Annotated[Path, typer.Argument(exists=True, file_okay=False, readable=True)],
    output: Annotated[Path, typer.Option("--output", "-o")] = Path(
        "data-manifests/dataset-manifest.json"
    ),
) -> None:
    entries = [inspect_npy(path) for path in sorted(data_dir.glob("*.npy"))]
    payload = {
        "dataset_id": "synapse-raman-v0-supplied-arrays",
        "generated_at": datetime.now(UTC).isoformat(),
        "source_path_policy": "filenames_only_no_absolute_paths",
        "files": entries,
    }
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    typer.echo(str(output))
