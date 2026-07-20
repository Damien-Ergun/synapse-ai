# Risk scoring policy

## Likelihood scale

1 Rare, 2 Unlikely, 3 Possible, 4 Likely, 5 Almost certain.

## Impact scale

1 Negligible, 2 Minor, 3 Moderate, 4 Major, 5 Severe.

## Calculation and bands

`score = likelihood x impact`.

- 1 to 4: Low
- 5 to 9: Moderate
- 10 to 14: High
- 15 to 25: Critical

Registers record inherent and residual scores. A treatment may reduce likelihood or impact only when a control and verification method are named.

## Blocker rules

- Every Critical residual risk is blocking.
- A High residual risk is blocking when it concerns scientific leakage, data rights, code ownership/publication authority, privacy, security, or a mandatory weekly gate.
- A High non-blocking risk requires an owner, treatment, due date, and explicit decision.
- Moderate and Low risks are monitored at least weekly while active.
- A risk closes only with evidence and a decision or recorded acceptance.
