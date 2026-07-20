# Technical, scientific, clinical, and governance risk register

Scores follow `docs/governance/risk_scoring_policy.md`.

| Risk ID | Risk | Residual score | Status | Treatment or gate | Owner |
|---|---|---:|---|---|---|
| RISK-T001 | Dataset reuse rights unclear | 25 | BLOCKING | Do not download arrays; obtain authoritative terms or written permission under DEC-021. | Damien Ergun |
| RISK-T002 | Public code ownership authority incomplete | 10 | BLOCKING_FOR_LICENSING | Publish original sanitised review material only; no licence grant under DEC-022. | Damien Ergun |
| RISK-T003 | Reserved split leakage | 5 | CONTROLLED | Enforce split roles and audit accesses under DEC-008. | Scientific lead |
| RISK-T004 | Duplicate spectra across splits | 12 | BLOCKING_WEEK2_GATE | Implement duplicate checks before the Week 2 gate. | Data lead |
| RISK-T005 | Acquisition artefacts dominate signal | 12 | OPEN | Add spectral QC and robustness evidence. | Spectroscopy lead |
| RISK-T006 | Preprocessing instability | 8 | CONTROLLED | Use controlled train-only pipelines in Week 3. | Spectroscopy lead |
| RISK-T007 | Domain shift to clinical isolates | 20 | OPEN_NOT_CURRENT_BLOCKER | Evaluate locked model separately in Week 7. | Scientific lead |
| RISK-T008 | Non-reproducible environment | 4 | CONTROLLED | Pinned uv, lock checks, tests, and CI. | Engineering lead |
| RISK-T009 | Incorrect labels or metadata mapping | 10 | BLOCKING_WEEK2_GATE | Validate manifests, axes, labels, and sample order. | Data lead |
| RISK-T010 | Unsupported medical claims | 5 | CONTROLLED | Claims register and documentation checks. | Programme lead |
| RISK-T011 | Instrument access unavailable | 16 | OPEN_NOT_WEEK1_BLOCKER | Maintain access and quotation routes for Week 3. | Product lead |
| RISK-T012 | Clinical sample access unavailable | 20 | OPEN_NOT_WEEK1_BLOCKER | Maintain partner and protocol route. | Product lead |
| RISK-T013 | Stakeholder privacy breach | 5 | CONTROLLED | Anonymous IDs and private crosswalk. | Programme lead |
| RISK-T014 | Credential or secret committed | 5 | CONTROLLED | Ignore rules and staged review. | Engineering lead |
| RISK-T015 | Third-party licence obligations missed | 8 | CONTROLLED | Reconcile every locked dependency. | Programme lead |
| RISK-T016 | Publication or patent disclosure conflict | 10 | BLOCKING_FOR_DISCLOSURE | Complete ownership and disclosure review. | Damien Ergun |
