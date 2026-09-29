from __future__ import annotations

import hashlib
from enum import StrEnum
from pathlib import Path
from typing import BinaryIO, cast

import numpy as np
from numpy.typing import NDArray

from synapse_core.registry import PROTECTED_HOLDOUT_SHA256


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


def _sha256_handle(handle: BinaryIO, chunk_size: int = 1024 * 1024) -> str:
    digest = hashlib.sha256()
    for chunk in iter(lambda: handle.read(chunk_size), b""):
        digest.update(chunk)
    return digest.hexdigest()


def _raise_if_holdout(role: DatasetRole, sha256: str | None = None) -> None:
    if role is DatasetRole.CLINICAL_2019 or sha256 in PROTECTED_HOLDOUT_SHA256:
        raise HoldoutAccessError(
            "clinical2019 is locked for final evaluation and cannot be loaded "
            "by development workflows"
        )


def assert_development_access(path: Path) -> None:
    role = infer_role(path)
    _raise_if_holdout(role)
    with path.open("rb") as handle:
        _raise_if_holdout(role, _sha256_handle(handle))


def load_development_array(path: Path) -> NDArray[np.generic]:
    role = infer_role(path)
    _raise_if_holdout(role)
    with path.open("rb") as handle:
        digest = _sha256_handle(handle)
        _raise_if_holdout(role, digest)
        handle.seek(0)
        loaded = cast(NDArray[np.generic], np.load(handle, allow_pickle=False))
    return loaded
