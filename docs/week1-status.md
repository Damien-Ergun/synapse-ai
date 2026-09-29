# Week 1 closeout status

Updated after the audited Raman dataset manifest was committed on 2026-09-29.

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

## Additional Week 1 founder actions

These remain pending unless the founder supplies evidence:

- complete the 30-person interview candidate list across approximately ten Paris-region institutions;
- activate the warm introduction to the biology research assistant;
- approve/use the French outreach template;
- approve/use the English outreach template;
- schedule the first two interviews;
- document provisional Damien/Issam roles;
- schedule the equity and governance discussion before the end of Week 2;
- agree and document Issam's fixed weekly contribution.

## Follow-up items that do not invalidate the Week 1 technical foundation

- resolve the upstream clinical-2018 source discrepancy before isolate-level validation;
- establish explicit isolate/patient mapping if available;
- verify dataset licensing and commercial-use terms;
- verify/configure `main` branch protection with GitHub admin access.

## Merge readiness

The engineering and data-audit foundation is ready for review. Keep the Week 1 PR in draft until the remaining founder closeout actions, especially the two scheduled interviews required by the exit gate, are evidenced.
