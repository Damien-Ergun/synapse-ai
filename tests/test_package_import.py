from __future__ import annotations

import pytest

import raman_bacteria_prototype
from raman_bacteria_prototype import (
    calibration,
    core,
    data,
    data_validation,
    evaluation,
    features,
    modelling,
    prediction,
    preprocessing,
    reporting,
    spectral_qc,
    tracking,
)


@pytest.mark.unit
def test_package_and_namespaces_import() -> None:
    assert all(
        module.__name__.startswith("raman_bacteria_prototype")
        for module in (
            core,
            data,
            data_validation,
            spectral_qc,
            preprocessing,
            features,
            modelling,
            calibration,
            evaluation,
            reporting,
            prediction,
            tracking,
        )
    )


@pytest.mark.unit
def test_version_comes_from_distribution_metadata(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setattr(raman_bacteria_prototype, "version", lambda _: "0.1.0")
    assert raman_bacteria_prototype.get_version() == "0.1.0"


@pytest.mark.unit
def test_version_has_uninstalled_fallback(monkeypatch: pytest.MonkeyPatch) -> None:
    def missing(_: str) -> str:
        raise raman_bacteria_prototype.PackageNotFoundError

    monkeypatch.setattr(raman_bacteria_prototype, "version", missing)
    assert raman_bacteria_prototype.get_version() == "0+uninstalled"
