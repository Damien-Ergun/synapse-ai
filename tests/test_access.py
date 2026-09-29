from pathlib import Path

import numpy as np
import pytest
from synapse_core.access import HoldoutAccessError, load_development_array


def test_clinical2019_rejected_by_development_loader(tmp_path: Path) -> None:
    path = tmp_path / "X_2019clinical.npy"
    np.save(path, np.zeros((2, 3)))
    with pytest.raises(HoldoutAccessError, match="locked"):
        load_development_array(path)


def test_non_holdout_can_load(tmp_path: Path) -> None:
    path = tmp_path / "X_reference.npy"
    np.save(path, np.ones((2, 3)))
    assert load_development_array(path).shape == (2, 3)
