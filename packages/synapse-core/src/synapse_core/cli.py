from __future__ import annotations

import json
import os
from datetime import UTC, datetime
from pathlib import Path
from typing import Annotated, Any

import typer

from synapse_core.audit import cross_split_duplicate_summary, inspect_npy, json_safe
from synapse_core.registry import (
    EXPECTED_DATASET_FILENAMES,
    EXPECTED_DATASET_ORDER,
    SPECTRAL_MATRIX_FILENAMES,
    XY_PAIRS,
)

app = typer.Typer(help="Synapse AI Week 1 dataset audit utilities.")


def validate_dataset_inventory(data_dir: Path) -> list[Path]:
    discovered = {path.name for path in data_dir.glob("*.npy")}
    missing = EXPECTED_DATASET_FILENAMES - discovered
    unexpected = discovered - EXPECTED_DATASET_FILENAMES
    if missing or unexpected:
        details: list[str] = []
        if missing:
            details.append(f"missing required files: {', '.join(sorted(missing))}")
        if unexpected:
            details.append(f"unexpected NPY files: {', '.join(sorted(unexpected))}")
        raise ValueError("; ".join(details))
    return [data_dir / name for name in EXPECTED_DATASET_ORDER]


def _validate_compatibility(entries: list[dict[str, Any]]) -> None:
    by_name = {str(entry["filename"]): entry for entry in entries}
    axis_length = int(by_name["wavenumbers.npy"]["shape"][0])
    for x_name, y_name in XY_PAIRS:
        x_shape = by_name[x_name]["shape"]
        y_shape = by_name[y_name]["shape"]
        if int(x_shape[0]) != int(y_shape[0]):
            raise ValueError(f"observation-count mismatch between {x_name} and {y_name}")
        if int(x_shape[1]) != axis_length:
            raise ValueError(f"feature-count mismatch between {x_name} and wavenumbers.npy")


def build_manifest_payload(data_dir: Path) -> dict[str, Any]:
    if os.environ.get("SYNAPSE_HOLDOUT_METADATA_AUDIT") != "1":
        raise ValueError(
            "authoritative manifest generation requires SYNAPSE_HOLDOUT_METADATA_AUDIT=1"
        )
    paths = validate_dataset_inventory(data_dir)
    entries = [inspect_npy(path) for path in paths]
    _validate_compatibility(entries)
    spectral_paths = [data_dir / name for name in SPECTRAL_MATRIX_FILENAMES]
    return {
        "dataset_id": "synapse-raman-v0-supplied-arrays",
        "generated_at": datetime.now(UTC).isoformat(),
        "source_path_policy": "filenames_only_no_absolute_paths",
        "files": entries,
        "cross_split_exact_duplicates": cross_split_duplicate_summary(spectral_paths),
    }


def write_manifest(data_dir: Path, output: Path) -> None:
    payload = json_safe(build_manifest_payload(data_dir))
    serialized = json.dumps(payload, indent=2, sort_keys=True, allow_nan=False) + "\n"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(serialized, encoding="utf-8")


@app.command()
def inspect(path: Annotated[Path, typer.Argument(exists=True, readable=True)]) -> None:
    payload = json_safe(inspect_npy(path))
    typer.echo(json.dumps(payload, indent=2, sort_keys=True, allow_nan=False))


@app.command()
def manifest(
    data_dir: Annotated[Path, typer.Argument(exists=True, file_okay=False, readable=True)],
    output: Annotated[Path, typer.Option("--output", "-o")] = Path(
        "data-manifests/dataset-manifest.json"
    ),
) -> None:
    try:
        write_manifest(data_dir, output)
    except ValueError as exc:
        raise typer.BadParameter(str(exc)) from exc
    typer.echo(str(output))
