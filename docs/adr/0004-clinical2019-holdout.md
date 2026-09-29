# ADR-0004: Clinical 2019 locked holdout

Status: Accepted, amended after independent Week 1 review

## Decision

Clinical2019 is inaccessible to ordinary development loaders.

Protection uses both canonical role detection and frozen SHA-256 content identities from the trusted registry. A renamed, copied, hardlinked, or symlinked file with the exact holdout bytes must remain blocked by the development loader.

Week 1 permits explicitly gated metadata auditing. Final evaluation will use a separate intentional workflow later.

## Consequences

No model selection, preprocessing tuning, threshold tuning, feature engineering, or exploratory predictive analysis may use clinical2019.

Changing the frozen holdout hashes requires an explicit provenance decision and review.
