# Week 1 closeout status

Updated after the independent Week 1 review identified a holdout-isolation blocker and manifest/documentation gaps.

## Current release-gate state

**PENDING INDEPENDENT RE-REVIEW**

The independent reviewer returned **FAIL** because the original clinical2019 safeguard trusted filenames. The implementation has now been remediated to enforce frozen SHA-256 identities before loading.

## Remediated reviewer findings

| Finding | Status | Evidence |
| --- | --- | --- |
| W1-B01 holdout alias bypass | REMEDIATED, RE-REVIEW REQUIRED | Frozen clinical2019 SHA-256 registry, content-hash enforcement, rename/symlink tests |
| W1-H01 incomplete manifest generation | REMEDIATED, RE-REVIEW REQUIRED | Exact 11-file inventory validation and missing-file tests |
| W1-H02 biological label equivalence wording | REMEDIATED | Dataset card now says same numeric label codes; biological mapping is UNVERIFIED |
| Cross-split duplicate reproducibility | REMEDIATED | Reusable pairwise audit plus synthetic detection test and committed zero-overlap result |
| W1-H03 authoritative manifest reproducibility | REMEDIATED, RE-REVIEW REQUIRED | Generator restored to committed schema/order; explicit timestamp-normalized verifier and regression tests added |

## Other robustness improvements

- strict JSON serialization converts non-finite summary values to `null`;
- malformed spectral dimensionality is rejected;
- Docker runtime uses `uv run --no-sync`;
- `*.egg-info/` is ignored and tracked generated metadata cleanup has begun;
- PR #1 is draft again.

## Technical gates

The original data identity, hashes, shapes, integrity checks, Raman axis, preprocessing assessment, clinical-2018 uncertainty, environment, CI, and Docker results remain documented. The revised branch must pass CI and then undergo the independent reviewer gate again before Week 2.

## Founder/business deliverables

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

## Release rule

Do not begin Week 2 until:

1. the revised technical branch passes CI;
2. the independent Week 1 reviewer approves the remediated safeguards;
3. the required Week 1 founder closeout, including two scheduled interviews, is evidenced.
