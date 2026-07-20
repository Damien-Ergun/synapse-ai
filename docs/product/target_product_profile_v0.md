# Target Product Profile v0

> Research-use hypothesis only. Not for diagnosis or treatment decisions.

## Prototype 0

| Field | Current controlled statement | Evidence status |
|---|---|---|
| User | Clinical laboratory professional or Raman researcher | Hypothesis |
| Setting | Hospital laboratory or microbiology research laboratory | Hypothesis |
| Input | Raman spectrum from a controlled biological sample | Product contract hypothesis |
| Output | Bacterial class, confidence, quality status, and alternatives | Future Prototype 0 behavior, not yet implemented |
| Clinical status | Research use only | Current policy |
| Current evidence | Week 1 software and governance foundation | Level 0 |

## Explicit non-scope

Prototype 0 does not establish blood-disease detection, sepsis detection, treatment recommendations, antibiotic-susceptibility prediction, hospital readiness, or regulatory approval. It does not establish that a bacterial-isolate classifier transfers to serum or plasma.

## Falsifiable future intended-use hypothesis

For adults undergoing investigation for a suspected serious bacterial infection in a hospital pathway, a controlled Raman measurement from a defined serum or plasma protocol may contain reproducible information that improves a predeclared classification or triage decision beyond predefined baseline information, within a turnaround time that changes a documented laboratory or clinical action.

The hypothesis is falsified for the selected use case if a controlled feasibility study cannot demonstrate reproducible signal above predefined technical and statistical thresholds, if performance does not add value beyond the comparator, if error or rejection rates are unacceptable, or if the workflow, cost, sample, instrument, reference standard, or regulatory burden makes the intended action infeasible.

## Intended decision variables still open

The exact population, serum versus plasma, collection protocol, target decision, operator, interpreter, reference standard, turnaround threshold, acceptable error rates, comparator, and action after uncertainty remain open and are tracked in `open_questions_register.md`.

## User-facing status concepts

Future outputs must distinguish accepted prediction, low classification confidence, out of distribution, quality failure, and software failure. Rejection is not a diagnosis.

## Evidence and review

The evidence ladder controls all claims. User, buyer, workflow, and operating-characteristic assumptions require interviews and later studies before adoption.
