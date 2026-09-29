"""Trusted identities and expected inventory for the supplied Week 1 dataset."""

EXPECTED_DATASET_ORDER: tuple[str, ...] = (
    "X_reference.npy",
    "y_reference.npy",
    "X_finetune.npy",
    "y_finetune.npy",
    "X_test.npy",
    "y_test.npy",
    "X_2018clinical.npy",
    "y_2018clinical.npy",
    "X_2019clinical.npy",
    "y_2019clinical.npy",
    "wavenumbers.npy",
)

EXPECTED_DATASET_FILENAMES: frozenset[str] = frozenset(EXPECTED_DATASET_ORDER)

SPECTRAL_MATRIX_FILENAMES: tuple[str, ...] = (
    "X_reference.npy",
    "X_finetune.npy",
    "X_test.npy",
    "X_2018clinical.npy",
    "X_2019clinical.npy",
)

XY_PAIRS: tuple[tuple[str, str], ...] = (
    ("X_reference.npy", "y_reference.npy"),
    ("X_finetune.npy", "y_finetune.npy"),
    ("X_test.npy", "y_test.npy"),
    ("X_2018clinical.npy", "y_2018clinical.npy"),
    ("X_2019clinical.npy", "y_2019clinical.npy"),
)

HOLDOUT_SHA256_BY_FILENAME: dict[str, str] = {
    "X_2019clinical.npy": "79235c885d66f4013647458154387863e717c78d27082ee457444321b90dab86",
    "y_2019clinical.npy": "705deee65ebf258582ff2dbe236a8145c8deb1ca5ebac9a53a9527fd174344dc",
}

PROTECTED_HOLDOUT_SHA256: frozenset[str] = frozenset(HOLDOUT_SHA256_BY_FILENAME.values())
