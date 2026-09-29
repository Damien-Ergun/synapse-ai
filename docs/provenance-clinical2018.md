# Clinical 2018 provenance issue

## Week 1 status

The discrepancy is **verified and documented**. Resolving the upstream source history remains a follow-up requirement before isolate-level validation, but the Week 1 requirement to expose the discrepancy is satisfied.

## What we know

The committed dataset manifest verifies:

- `X_2018clinical.npy` shape: 10,000 x 1,000
- `X_2018clinical.npy` SHA-256: `9e23eecf4fb43c32313c1111d144720764bb93ac7887fe9bcfd5223ec151db29`
- `y_2018clinical.npy` shape: 10,000
- `y_2018clinical.npy` SHA-256: `968f1eb87996ff36a2388f7df03e8fff4b177bc0a32e131cc4b9603ca4cc4ae6`
- five class labels: 0, 2, 3, 5, and 6
- 2,000 spectra per class label
- no NaN or infinite values
- no exact duplicate spectra within the clinical-2018 matrix

The 10,000-spectrum count is therefore a measured fact for the delivered file.

The arithmetic `25 x 400 = 10,000` is compatible with the size of the array, but it is not evidence that the file contains 25 isolates or that each contiguous block of 400 spectra corresponds to one isolate.

## What we do not know

No verified isolate IDs, patient IDs, acquisition-order metadata, or split-construction metadata are present in the supplied arrays.

Repository evidence still does not establish why other descriptions may refer to 30 isolates or 12,000 spectra.

## Possible explanations

Possible explanations include:

- the delivered file is a subset of a larger source release;
- isolates were excluded upstream;
- another description refers to a different release or split;
- filtering occurred before delivery;
- one of the descriptive counts is incorrect.

These remain hypotheses.

## Evidence required for resolution

- original publication and/or source repository;
- exact source dataset version;
- split-generation or export code;
- acquisition metadata;
- explicit isolate or patient mapping.

## Impact on validation

Until isolate identity is established, the clinical spectra cannot support claims of isolate-level or patient-level independence.

Any reconstructed grouping must be clearly marked as reconstructed or hypothetical.

## Follow-up

Tracked in GitHub Issue #3. This issue should be resolved before later roadmap work makes isolate-level validation claims.
