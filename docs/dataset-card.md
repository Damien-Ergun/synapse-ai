# Dataset card: supplied Raman arrays

## Purpose

Foundation dataset for a research-use-only microorganism candidate-identification prototype. It is not clinically validated and is not intended for patient management.

## Audit status

**COMPLETED on 2026-09-29.** The generated machine-readable inventory is committed at `data-manifests/dataset-manifest.json`. Raw NumPy arrays remain outside Git.

All supplied arrays are `float64`, have finite fraction 1.0, and report zero NaN, positive infinity, and negative infinity values.

## Verified inventory

| File | Shape | SHA-256 |
| --- | --- | --- |
| `wavenumbers.npy` | 1000 | `22e11b897a4a7ddbf1dfe3a8067ff68906655cde569a667f7978636760d104f7` |
| `X_reference.npy` | 60000 x 1000 | `80040a919a6346b410745322b5593227823c77fb9ea4ae9b4bf7f4aef2a07e45` |
| `y_reference.npy` | 60000 | `f7458e2a5256ae828c6c00d93cd5e6b9f7d04a455860c77382408b04943ac85f` |
| `X_finetune.npy` | 3000 x 1000 | `361acaf2fa8fe868c90c33d3321a6045c1ea6be915c5dafae8a3d41a9bb900ad` |
| `y_finetune.npy` | 3000 | `aece34e11169d5cd9d13124b666d3e4d69f38f582817bcf66218abf6a9d55edb` |
| `X_test.npy` | 3000 x 1000 | `ec43c85b44bf71ed6fabfcb4ddfde3d751d85e5a96be1fed9bb2b9ab1cd1f6e4` |
| `y_test.npy` | 3000 | `aece34e11169d5cd9d13124b666d3e4d69f38f582817bcf66218abf6a9d55edb` |
| `X_2018clinical.npy` | 10000 x 1000 | `9e23eecf4fb43c32313c1111d144720764bb93ac7887fe9bcfd5223ec151db29` |
| `y_2018clinical.npy` | 10000 | `968f1eb87996ff36a2388f7df03e8fff4b177bc0a32e131cc4b9603ca4cc4ae6` |
| `X_2019clinical.npy` | 2500 x 1000 | `79235c885d66f4013647458154387863e717c78d27082ee457444321b90dab86` |
| `y_2019clinical.npy` | 2500 | `705deee65ebf258582ff2dbe236a8145c8deb1ca5ebac9a53a9527fd174344dc` |

The byte-identical hashes for `y_finetune.npy` and `y_test.npy` are a verified observation. Both contain 3,000 labels with exactly 100 observations in each of the 30 classes. Their X matrices have different hashes, so the identical label arrays do not by themselves establish spectral leakage.

## Splits and labels

Reference has 60,000 observations across 30 numeric label codes, with 2,000 observations per code.

Fine-tuning and reference test each have 3,000 observations using the same numeric label-code set `0..29`, with 100 observations per code.

Clinical 2018 has 10,000 observations across five numeric label codes: 0, 2, 3, 5, and 6, with 2,000 observations per code.

Clinical 2019 has 2,500 observations using the same numeric label-code set `0, 2, 3, 5, 6`, with 500 observations per code.

**Biological label mapping status: UNVERIFIED.** Equality of numeric codes across splits does not by itself establish that those codes have identical biological meaning. The numeric labels are also not verified patient or isolate identifiers.

## Raman axis

The Raman axis contains 1,000 unique values from 1792.4 down to 381.98. It is strictly monotonic descending, has no repeated axis values, and has median spacing approximately -1.4.

## Duplicate spectra

No exact duplicate spectra were detected within any supplied spectral matrix:

- reference: 60,000 unique of 60,000
- fine-tuning: 3,000 unique of 3,000
- test: 3,000 unique of 3,000
- clinical 2018: 10,000 unique of 10,000
- clinical 2019: 2,500 unique of 2,500

No exact within-split duplicates were found. A reusable exact cross-split audit is also committed at `data-manifests/cross-split-duplicates.json`; all ten current matrix pairs report zero exact overlaps. Exact non-duplication still does not prove biological independence.

## Existing preprocessing assessment

The supplied spectral matrices show strong evidence of prior amplitude scaling or normalization.

Verified observations:

- every spectral matrix has global minimum exactly 0.0 and global maximum exactly 1.0;
- the median per-spectrum maximum is exactly 1.0 in every split;
- at least 95% of spectra in every split reach a maximum of exactly 1.0;
- the median per-spectrum minimum is 0.0 in every split;
- many spectra contain exact zero and exact one values.

This pattern is **strongly consistent with prior min-max-like scaling or normalization**.

The arrays alone do not establish the exact preprocessing pipeline. In particular, they do not prove whether scaling was performed per spectrum, whether it occurred before cropping to the retained Raman range, or whether baseline correction, clipping, smoothing, or other transformations were also applied.

No new preprocessing was applied during Week 1.

## Clinical 2018 discrepancy

The supplied array is now verified as exactly 10,000 x 1,000 with five balanced class labels. This confirms the delivered-data side of the previously documented 10,000 versus 12,000 discrepancy.

The arithmetic `25 x 400 = 10,000` remains only a possible grouping interpretation. No isolate identity or 400-spectrum acquisition grouping has been verified.

See `docs/provenance-clinical2018.md`.

## Patient/isolate grouping

Verified grouping: **unknown**.

No patient or isolate identifiers are present in the audited arrays. Class balance, contiguous ordering, or convenient divisibility must not be treated as evidence of biological grouping.

## Clinical 2019 holdout

Clinical 2019 is the locked final-evaluation holdout. Its two SHA-256 identities are recorded in `data-manifests/clinical2019-holdout.json`. Ordinary development loading remains prohibited by code and covered by tests.

## Licensing

Status: **UNVERIFIED**.

No redistribution or commercial-use claim is made. The raw arrays are intentionally not committed to Git.

See `docs/licensing-provenance.md`.

## Open questions

1. Original dataset publication/repository and exact version.
2. Why the delivered clinical-2018 data contain 10,000 spectra while other descriptions may refer to 12,000 or 30 isolates.
3. Explicit patient/isolate identifiers and acquisition ordering.
4. Exact upstream preprocessing history.
5. Research-use, commercial-use, redistribution, derivative-model, and attribution terms.
