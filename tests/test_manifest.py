import json
from pathlib import Path

import numpy as np
import pytest
from synapse_core.cli import (
    build_manifest_payload,
    normalize_manifest_for_comparison,
    validate_dataset_inventory,
    verify_manifest_reproducibility,
    write_manifest,
)
from synapse_core.registry import EXPECTED_DATASET_ORDER


def _write_complete_dataset(data_dir: Path) -> None:
    data_dir.mkdir(parents=True, exist_ok=True)
    np.save(data_dir / "wavenumbers.npy", np.array([3.0, 2.0, 1.0]))
    for index, name in enumerate(
        [
            "X_reference.npy",
            "X_finetune.npy",
            "X_test.npy",
            "X_2018clinical.npy",
            "X_2019clinical.npy",
        ]
    ):
        offset = float(index * 10)
        np.save(
            data_dir / name,
            np.array(
                [
                    [offset + 1.0, offset + 2.0, offset + 3.0],
                    [offset + 4.0, offset + 5.0, offset + 6.0],
                ]
            ),
        )
    for name in [
        "y_reference.npy",
        "y_finetune.npy",
        "y_test.npy",
        "y_2018clinical.npy",
        "y_2019clinical.npy",
    ]:
        np.save(data_dir / name, np.array([0.0, 1.0]))


def test_empty_inventory_fails(tmp_path: Path) -> None:
    data_dir = tmp_path / "empty"
    data_dir.mkdir()
    with pytest.raises(ValueError, match="missing required files"):
        validate_dataset_inventory(data_dir)


@pytest.mark.parametrize(
    "missing_name",
    ["X_reference.npy", "y_test.npy", "wavenumbers.npy"],
)
def test_missing_required_file_prevents_manifest_write(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, missing_name: str
) -> None:
    data_dir = tmp_path / "data"
    _write_complete_dataset(data_dir)
    (data_dir / missing_name).unlink()
    output = tmp_path / "manifest.json"
    monkeypatch.setenv("SYNAPSE_HOLDOUT_METADATA_AUDIT", "1")

    with pytest.raises(ValueError, match="missing required files"):
        write_manifest(data_dir, output)

    assert not output.exists()


def test_complete_inventory_writes_manifest(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    data_dir = tmp_path / "data"
    _write_complete_dataset(data_dir)
    output = tmp_path / "manifest.json"
    monkeypatch.setenv("SYNAPSE_HOLDOUT_METADATA_AUDIT", "1")

    write_manifest(data_dir, output)

    assert output.exists()
    text = output.read_text(encoding="utf-8")
    assert '"dataset_id": "synapse-raman-v0-supplied-arrays"' in text
    assert '"cross_split_exact_duplicates"' not in text
    for name in EXPECTED_DATASET_ORDER:
        assert name in text


def test_manifest_generator_uses_canonical_schema_and_order(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    data_dir = tmp_path / "data"
    _write_complete_dataset(data_dir)
    monkeypatch.setenv("SYNAPSE_HOLDOUT_METADATA_AUDIT", "1")

    payload = build_manifest_payload(data_dir)

    assert list(payload) == [
        "dataset_id",
        "generated_at",
        "source_path_policy",
        "files",
    ]
    assert [entry["filename"] for entry in payload["files"]] == list(
        EXPECTED_DATASET_ORDER
    )


def test_manifest_reproducibility_ignores_only_generated_at(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    data_dir = tmp_path / "data"
    _write_complete_dataset(data_dir)
    monkeypatch.setenv("SYNAPSE_HOLDOUT_METADATA_AUDIT", "1")

    committed = build_manifest_payload(data_dir)
    committed["generated_at"] = "2000-01-01T00:00:00+00:00"
    committed_path = tmp_path / "committed.json"
    committed_path.write_text(
        json.dumps(committed, sort_keys=True),
        encoding="utf-8",
    )

    verify_manifest_reproducibility(data_dir, committed_path)

    committed["source_path_policy"] = "materially-different"
    committed_path.write_text(
        json.dumps(committed, sort_keys=True),
        encoding="utf-8",
    )
    with pytest.raises(ValueError, match="differs materially"):
        verify_manifest_reproducibility(data_dir, committed_path)


def test_committed_manifest_contract_matches_generator_contract() -> None:
    committed_path = Path("data-manifests/dataset-manifest.json")
    committed = json.loads(committed_path.read_text(encoding="utf-8"))

    assert list(committed) == [
        "dataset_id",
        "files",
        "generated_at",
        "source_path_policy",
    ]
    assert [entry["filename"] for entry in committed["files"]] == list(
        EXPECTED_DATASET_ORDER
    )
    assert "cross_split_exact_duplicates" not in committed
    assert "generated_at" not in normalize_manifest_for_comparison(committed)
