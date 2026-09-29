from pathlib import Path

import numpy as np
from hypothesis import given
from hypothesis import strategies as st
from synapse_core.audit import (
    axis_summary,
    duplicate_summary,
    inspect_npy,
    label_summary,
    sha256_file,
)


def test_inspect_detects_nan_inf_and_shape(tmp_path: Path) -> None:
    path = tmp_path / "X_reference.npy"
    np.save(path, np.array([[0.0, np.nan], [np.inf, -np.inf]]))
    report = inspect_npy(path)
    assert report["shape"] == [2, 2]
    assert report["nan_count"] == 1
    assert report["posinf_count"] == 1
    assert report["neginf_count"] == 1
    assert len(report["sha256"]) == 64
    assert report["sha256"] == sha256_file(path)


def test_duplicate_detection() -> None:
    report = duplicate_summary(np.array([[1.0, 2.0], [1.0, 2.0], [3.0, 4.0]]))
    assert report["exact_duplicate_count"] == 1
    assert report["unique_spectra"] == 2


def test_label_distribution() -> None:
    report = label_summary(np.array([0, 0, 1, 2]))
    assert report["class_counts"] == {"0": 2, "1": 1, "2": 1}


def test_axis_monotonicity() -> None:
    report = axis_summary(np.array([100.0, 101.5, 103.0]))
    assert report["strictly_monotonic"] is True


@given(st.lists(st.integers(min_value=-10, max_value=10), min_size=1, max_size=100))
def test_duplicate_count_bounds(values: list[int]) -> None:
    report = duplicate_summary(np.asarray(values, dtype=np.int64).reshape(-1, 1))
    assert 0 <= report["exact_duplicate_count"] <= len(values) - 1
