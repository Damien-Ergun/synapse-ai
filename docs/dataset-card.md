# Dataset card: supplied Raman arrays

Purpose: research-use-only microorganism candidate identification. Not clinically validated and not intended for patient management.

## Verified information
Actual shapes, dtypes, class counts, ranges, duplicate counts, and SHA-256 values must come from the generated manifest, never from roadmap estimates.

## Current audit status
**BLOCKED_LOCAL_AUDIT.** The worker sandbox rejected reads of the mounted NumPy inputs. No hashes or statistics are invented. Run `SYNAPSE_HOLDOUT_METADATA_AUDIT=1 uv run inspect-dataset manifest <data-dir>` where the arrays are accessible.

## Existing preprocessing
Unknown. The audit computes global/per-spectrum scale statistics, exact 0/1 frequencies, norms, sums, and duplicate counts. Values bounded near 0 and 1 would be consistent with prior scaling/normalization but would not establish a preprocessing method.

## Clinical 2018
The brief notes an apparent 10,000 spectra, arithmetically compatible with 25 x 400, while other descriptions may mention 30 isolates/12,000 spectra. No isolate interpretation is accepted without source evidence.

## Patient/isolate grouping
Verified grouping: **unknown**. Contiguous blocks must not be treated as biological replicates without provenance evidence.

## Clinical 2019
Locked final-evaluation holdout. Ordinary development loading is prohibited.

## Licensing
**UNVERIFIED.**

## Open questions
Original source/version; clinical-2018 isolate count and ordering; explicit isolate IDs; exact preprocessing history; reuse/redistribution/model-training/commercial-use/attribution terms.
