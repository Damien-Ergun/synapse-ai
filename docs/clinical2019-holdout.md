# Clinical 2019 holdout policy

Clinical 2019 is reserved for locked final evaluation.

Protection uses frozen SHA-256 identities, not only filenames. The trusted registry records both clinical2019 hashes, and `load_development_array` hashes the opened bytes before NumPy loads them. Files with those identities are rejected even if copied, renamed, hardlinked, or exposed through a symlink alias.

Automated tests cover:
- canonical clinical2019 filenames;
- copied holdout-equivalent bytes renamed as accepted development files;
- symlink aliases where supported.

Week 1 metadata auditing remains separately gated by `SYNAPSE_HOLDOUT_METADATA_AUDIT=1`. The final-evaluation workflow is intentionally not implemented in Week 1.

No model selection, preprocessing tuning, threshold tuning, feature engineering, or exploratory predictive analysis may use clinical2019.
