import hashlib
import shutil
from pathlib import Path

import numpy as np
import pytest
import synapse_core.access as access
from synapse_core.access import HoldoutAccessError, load_development_array
from synapse_core.registry import HOLDOUT_SHA256_BY_FILENAME


def test_frozen_holdout_hashes_match_audited_registry() -> None:
    assert HOLDOUT_SHA256_BY_FILENAME == {
        "X_2019clinical.npy": ("79235c885d66f4013647458154387863e717c78d27082ee457444321b90dab86"),
        "y_2019clinical.npy": ("705deee65ebf258582ff2dbe236a8145c8deb1ca5ebac9a53a9527fd174344dc"),
    }


def test_clinical2019_rejected_by_development_loader(tmp_path: Path) -> None:
    path = tmp_path / "X_2019clinical.npy"
    np.save(path, np.zeros((2, 3)))
    with pytest.raises(HoldoutAccessError, match="locked"):
        load_development_array(path)


@pytest.mark.parametrize("alias_name", ["X_reference.npy", "X_test.npy"])
def test_holdout_content_rejected_after_rename(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, alias_name: str
) -> None:
    source = tmp_path / "source.npy"
    np.save(source, np.arange(6, dtype=np.float64).reshape(2, 3))
    digest = hashlib.sha256(source.read_bytes()).hexdigest()
    monkeypatch.setattr(access, "PROTECTED_HOLDOUT_SHA256", frozenset({digest}))

    alias = tmp_path / alias_name
    shutil.copyfile(source, alias)

    with pytest.raises(HoldoutAccessError, match="locked"):
        load_development_array(alias)


def test_holdout_content_rejected_through_symlink(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    source = tmp_path / "source.npy"
    np.save(source, np.arange(6, dtype=np.float64).reshape(2, 3))
    digest = hashlib.sha256(source.read_bytes()).hexdigest()
    monkeypatch.setattr(access, "PROTECTED_HOLDOUT_SHA256", frozenset({digest}))

    alias = tmp_path / "X_reference.npy"
    try:
        alias.symlink_to(source)
    except OSError:
        pytest.skip("symlinks are not supported in this environment")

    with pytest.raises(HoldoutAccessError, match="locked"):
        load_development_array(alias)


def test_non_holdout_can_load(tmp_path: Path) -> None:
    path = tmp_path / "X_reference.npy"
    np.save(path, np.ones((2, 3)))
    assert load_development_array(path).shape == (2, 3)
