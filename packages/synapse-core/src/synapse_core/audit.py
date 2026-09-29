from __future__ import annotations

import hashlib
import os
from collections import Counter
from pathlib import Path
from typing import Any

import numpy as np
from numpy.typing import NDArray

from synapse_core.access import DatasetRole, infer_role


def sha256_file(path: Path, chunk_size: int = 1024 * 1024) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(chunk_size), b""):
            digest.update(chunk)
    return digest.hexdigest()


def duplicate_summary(matrix: NDArray[np.generic]) -> dict[str, int | float]:
    if matrix.ndim != 2:
        raise ValueError("duplicate_summary requires a 2D matrix")
    counts = Counter(
        hashlib.sha256(np.ascontiguousarray(row).tobytes()).digest() for row in matrix
    )
    unique = len(counts)
    duplicates = matrix.shape[0] - unique
    return {
        "unique_spectra": unique,
        "exact_duplicate_count": duplicates,
        "duplicate_fraction": duplicates / matrix.shape[0] if matrix.shape[0] else 0.0,
        "duplicate_clusters": sum(count > 1 for count in counts.values()),
        "largest_duplicate_cluster": max(counts.values(), default=0),
    }


def label_summary(labels: NDArray[np.generic]) -> dict[str, Any]:
    values, counts = np.unique(labels, return_counts=True)
    total = len(labels)
    return {
        "observations": total,
        "unique_classes": len(values),
        "class_values": [value.item() for value in values],
        "class_counts": {
            str(value.item()): int(count)
            for value, count in zip(values, counts, strict=True)
        },
        "class_proportions": {
            str(value.item()): float(count / total)
            for value, count in zip(values, counts, strict=True)
        },
    }


def axis_summary(axis: NDArray[np.generic]) -> dict[str, Any]:
    numeric = np.asarray(axis, dtype=np.float64)
    spacing = np.diff(numeric)
    return {
        "length": len(numeric),
        "minimum": float(numeric.min()),
        "maximum": float(numeric.max()),
        "ascending": bool(np.all(spacing >= 0)),
        "descending": bool(np.all(spacing <= 0)),
        "strictly_monotonic": bool(np.all(spacing > 0) or np.all(spacing < 0)),
        "repeated_axis_values": int(len(numeric) - len(np.unique(numeric))),
        "spacing": {
            "minimum": float(spacing.min()),
            "maximum": float(spacing.max()),
            "mean": float(spacing.mean()),
            "median": float(np.median(spacing)),
            "std": float(spacing.std()),
        },
    }


def _distribution(values: NDArray[np.float64]) -> dict[str, float]:
    quantiles = np.quantile(values, [0, 0.05, 0.25, 0.5, 0.75, 0.95, 1])
    keys = ("min", "p05", "p25", "median", "p75", "p95", "max")
    return dict(zip(keys, map(float, quantiles), strict=True))


def spectrum_summary(matrix: NDArray[np.generic]) -> dict[str, Any]:
    x = np.asarray(matrix, dtype=np.float64)
    return {
        "global_min": float(x.min()),
        "global_max": float(x.max()),
        "global_mean": float(x.mean()),
        "global_median": float(np.median(x)),
        "global_std": float(x.std()),
        "exact_zero_count": int(np.count_nonzero(x == 0)),
        "exact_one_count": int(np.count_nonzero(x == 1)),
        "per_spectrum_min": _distribution(x.min(axis=1)),
        "per_spectrum_max": _distribution(x.max(axis=1)),
        "per_spectrum_mean": _distribution(x.mean(axis=1)),
        "per_spectrum_std": _distribution(x.std(axis=1)),
        "per_spectrum_sum": _distribution(x.sum(axis=1)),
        "per_spectrum_l2": _distribution(np.linalg.norm(x, axis=1)),
        **duplicate_summary(x),
    }


def inspect_npy(path: Path) -> dict[str, Any]:
    role = infer_role(path)
    array = np.load(path, mmap_mode="r", allow_pickle=False)
    floating = np.asarray(array, dtype=np.float64)
    result: dict[str, Any] = {
        "filename": path.name,
        "role": role.value,
        "sha256": sha256_file(path),
        "shape": list(array.shape),
        "ndim": array.ndim,
        "dtype": str(array.dtype),
        "estimated_memory_bytes": int(array.nbytes),
        "nan_count": int(np.isnan(floating).sum()),
        "posinf_count": int(np.isposinf(floating).sum()),
        "neginf_count": int(np.isneginf(floating).sum()),
        "finite_fraction": float(np.isfinite(floating).mean()),
    }
    holdout_locked = (
        role is DatasetRole.CLINICAL_2019
        and os.environ.get("SYNAPSE_HOLDOUT_METADATA_AUDIT") != "1"
    )
    if holdout_locked:
        result["holdout_detail_status"] = "LOCKED_METADATA_ONLY"
        return result
    if path.name.startswith("y_"):
        result["labels"] = label_summary(array)
    elif role is DatasetRole.AXIS:
        result["axis"] = axis_summary(array)
    elif array.ndim == 2:
        result["spectra"] = spectrum_summary(array)
    return result
