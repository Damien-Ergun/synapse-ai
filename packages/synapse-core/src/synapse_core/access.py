from __future__ import annotations

from enum import StrEnum
from pathlib import Path

import numpy as np
from numpy.typing import NDArray


class DatasetRole(StrEnum):
    REFERENCE = "reference"
    FINETUNE = "finetune"
    TEST = "test"
    CLINICAL_2018 = "clinical2018"
    CLINICAL_2019 = "clinical2019"
    AXIS = "axis"


class HoldoutAccessError(PermissionError):
    pass


def infer_role(path: Path) -> DatasetRole:
    name = path.name.lower()
    if "2019clinical" in name:
        return DatasetRole.CLINICAL_2019
    if "2018clinical" in name:
        return DatasetRole.CLINICAL_2018
    if "finetune" in name:
        return DatasetRole.FINETUNE
    if "reference" in name:
        return DatasetRole.REFERENCE
    if "test" in name:
        return DatasetRole.TEST
    if "wavenumber" in name:
        return DatasetRole.AXIS
    raise ValueError(f"Cannot infer dataset role from {path.name!r}")


def assert_development_access(path: Path) -> None:
    if infer_role(path) is DatasetRole.CLINICAL_2019:
        raise HoldoutAccessError(
            "clinical2019 is locked for final evaluation and cannot be loaded by development workflows"
        )


def load_development_array(path: Path) -> NDArray[np.generic]:
    assert_development_access(path)
    return np.load(path, allow_pickle=False)
