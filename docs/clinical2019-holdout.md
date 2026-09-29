# Clinical 2019 holdout policy

Clinical 2019 is reserved for locked final evaluation.

`synapse_core.access.load_development_array` raises `HoldoutAccessError` for clinical2019. Tests prove ordinary development access fails.

Week 1 metadata auditing is permitted without model-development use. Detailed audit requires `SYNAPSE_HOLDOUT_METADATA_AUDIT=1`. The final-evaluation workflow is intentionally not implemented in Week 1.

No model selection, preprocessing tuning, threshold tuning, or exploratory predictive analysis may use clinical2019.
