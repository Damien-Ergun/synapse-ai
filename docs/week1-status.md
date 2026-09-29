# Week 1 closeout status

Updated after the audited Raman dataset manifest and outreach templates were committed on 2026-09-29.

## Technical exit gates

| Requirement | Status | Evidence |
| --- | --- | --- |
| `uv sync` works | PASS | Locked dependency installation passes in GitHub Actions |
| CI passes | PASS | Quality and Docker Compose smoke jobs pass |
| All supplied dataset files checksummed | PASS | `data-manifests/dataset-manifest.json` |
| Shapes and labels documented | PASS | Dataset manifest and dataset card |
| `clinical2019` protected | PASS | Controlled loader, automated test, immutable hashes recorded |
| Isolate grouping issue documented | PASS | Grouping explicitly remains unknown |
| Clinical-2018 discrepancy documented | PASS | Delivered 10,000-spectrum file verified and discrepancy recorded |
| Preprocessing uncertainty documented | PASS | Strong evidence of prior scaling, exact method remains unknown |
| First two interviews scheduled | PENDING HUMAN ACTION | Calendar/email evidence required |

## Week 1 founder/business deliverables

| Deliverable | Status |
| --- | --- |
| 30 interview candidates across ~10 Paris-region institutions | PENDING |
| Warm introduction to biology research assistant | PENDING HUMAN ACTION |
| French outreach template | PASS |
| English outreach template | PASS |
| First two interviews scheduled | PENDING HUMAN ACTION |
| Damien and Issam provisional roles agreed | PENDING HUMAN ACTION |
| Equity/governance discussion scheduled before end of Week 2 | PENDING HUMAN ACTION |
| Issam fixed weekly contribution agreed | PENDING HUMAN ACTION |

## Follow-up items that do not invalidate the Week 1 technical foundation

- resolve the upstream clinical-2018 source discrepancy before isolate-level validation;
- establish explicit isolate/patient mapping if available;
- verify dataset licensing and commercial-use terms;
- verify/configure `main` branch protection with GitHub admin access.

## Merge readiness

The engineering and data-audit foundation is ready for review.

Keep PR #1 in draft until the founder/business closeout is evidenced, especially the explicit exit gate requiring the first two interviews to be scheduled.
