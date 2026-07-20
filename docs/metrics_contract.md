# Metric contract v0.1

## Global rules

Class order comes from committed class metadata. Every result records split, data-manifest hash, configuration hash, software version, seed policy, sample count, class denominators, and confidence-interval method. Test and clinical splits cannot influence metric definitions, selection, threshold choice, or preprocessing.

| Metric ID | Name | Required convention |
|---|---|---|
| METRIC-001 | Accuracy | Correct predictions divided by evaluated samples; undefined for zero samples. |
| METRIC-002 | Balanced accuracy | Unweighted mean recall across supported classes; zero-support classes are reported. |
| METRIC-003 | Macro-F1 | Unweighted per-class F1; zero division returns zero and is flagged. |
| METRIC-004 | Weighted-F1 | Per-class F1 weighted by true support. |
| METRIC-005 | Top-3 accuracy | Use top `min(3,K)` ordered class probabilities. |
| METRIC-006 | Per-class precision | One-vs-rest TP divided by TP plus FP; denominator reported. |
| METRIC-007 | Per-class recall | TP divided by TP plus FN; denominator reported. |
| METRIC-008 | Per-class specificity | One-vs-rest TN divided by TN plus FP. |
| METRIC-009 | Confusion matrix | True-by-predicted counts in committed class order. |
| METRIC-010 | Multiclass Brier score | Mean squared error between one-hot outcomes and valid probability vectors. |
| METRIC-011 | Expected calibration error | Configuration-controlled bins, default 15 equal-width bins, with empty-bin handling recorded. |
| METRIC-012 | Rejection-versus-accuracy | Every accepted-sample metric is reported with coverage and rejection reason. |
| METRIC-013 | Inference time | Median and p90 with hardware, batch size, and warm-up recorded. |

## Reproducibility requirements

ECE bins, top-k, zero-division policy, timing protocol, hardware, confidence-interval resampling unit, and seeds are configuration-controlled. Validation may guide development. Test is reserved for Week 6 locked reporting and clinical splits for Week 7.
