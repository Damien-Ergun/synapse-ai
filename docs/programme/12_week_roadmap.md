---
source_filename: 12-week-Roadmap.txt
source_sha256: c993737a6b4d299e9a264bb9a5e3cb0a9105f964854adc5b14e76e42dff7d1a3
adopted_on: 2026-07-20
status: ACTIVE
supersedes: NONE
---

# Raman Bacteria Prototype 0

## 12-Week Technical, Clinical and Investment-Readiness Roadmap

## 1. Programme mission

Over 12 weeks, I will build and validate:

> A reproducible Raman machine-learning engine for biological spectrum classification, demonstrated on a public bacterial Raman dataset, with calibrated uncertainty, input-quality controls, external-split evaluation, transparent reporting, and a documented route toward a serum or plasma validation study.

Prototype 0 is not a medical diagnostic product.

It is the first evidence package showing that I can:

1. Build a reliable Raman data pipeline.
2. Develop and evaluate biological-spectrum classifiers.
3. Detect uncertain or unsuitable inputs.
4. produce reproducible technical evidence.
5. Define a focused clinical use case.
6. Understand the regulatory and validation pathway.
7. Secure a credible route to clinical samples.
8. Present a fundable Prototype 1 plan.

## 2. What “10 out of 10” means

The programme targets the following final scorecard.

| Category                              | Week 12 target                                                                                   |
| ------------------------------------- | ------------------------------------------------------------------------------------------------ |
| Software engineering                  | Tested, modular, documented, automated and reproducible pipeline                                 |
| Raman and ML methodology              | Multiple preprocessing strategies, justified models, locked evaluation and robustness testing    |
| Reproducibility                       | One-command rebuild, fixed environments, manifests, hashes, seeds and experiment records         |
| Scientific credibility                | Confidence intervals, repeated runs, failure analysis, external splits and no test leakage       |
| Evidence for the future blood product | Explicit evidence ladder, acquisition protocol and serum/plasma pilot plan                       |
| Clinical translation                  | Narrow intended use, clinical workflow analysis, advisor feedback and sample-access route        |
| Business credibility                  | Defined user, buyer, value proposition, competitor analysis and economic assumptions             |
| Investment readiness                  | Prototype, proof-of-concept evidence, pitch, data room, use of funds and partner evidence        |
| Regulatory readiness                  | Intended-use statement, preliminary IVDR assessment, risk file and traceability documentation    |
| IP and defensibility                  | Data-rights review, code ownership review, preliminary patent landscape and defensibility thesis |

This is a 10 out of 10 **Prototype 0**, not a 10 out of 10 medical device.

A real diagnostic claim will require clinical samples, analytical validation, clinical performance studies, controlled acquisition protocols, regulatory work, quality management and independent evidence.

## 3. Four workstreams maintained every week

Every week must produce evidence across four parallel workstreams.

### Workstream A: Technical and scientific

- Raman data ingestion
- quality control
- preprocessing
- modelling
- uncertainty
- robustness
- reporting
- reproducibility

### Workstream B: Product and clinical translation

- intended use
- target population
- clinical workflow
- sample type
- reference standard
- pilot design
- clinical advisor and partner outreach

### Workstream C: Business and investment

- customer discovery
- buyer analysis
- competitive landscape
- economic value
- milestones
- use of funds
- pitch and data room

### Workstream D: Governance, regulation and IP

- claims control
- data provenance
- risk management
- preliminary IVDR pathway
- privacy and cybersecurity
- licensing
- intellectual property

Medical-device ML development should be considered over the total product life cycle rather than treated as an isolated model-training exercise. The current international GMLP principles were finalized through the IMDRF in January 2025.

---

# Week 1: foundation, scope and product thesis

## Objective

Create the project foundation and define exactly what I am building, what I am not building, and which future clinical decision the platform could eventually support.

## Technical and scientific tasks

1. Create the repository structure:

```text
configs/
data/
docs/
models/
notebooks/
reports/
scripts/
src/
tests/
```

2. Initialize:

```text
pyproject.toml
uv.lock
.python-version
.gitignore
README.md
```

3. Pin Python 3.11 and use `uv` for the environment.

4. Add initial automated checks:

```text
uv sync
environment validation
pytest
ruff
black
```

5. Define the package architecture:

```text
data loading
data validation
spectral quality control
preprocessing
features
modelling
calibration
evaluation
reporting
prediction
experiment tracking
```

6. Write the initial metric contract:

```text
accuracy
balanced accuracy
macro-F1
weighted-F1
top-3 accuracy
per-class precision
per-class recall
per-class specificity
confusion matrix
Brier score
expected calibration error
rejection-versus-accuracy curve
inference time
```

## Product and clinical tasks

1. Write `docs/product/target_product_profile_v0.md`.

2. Define the first product hypothesis:

```text
User:
Clinical laboratory professional or researcher

Setting:
Hospital laboratory or microbiology research laboratory

Input:
Raman spectrum from a controlled biological sample

Prototype 0 output:
Bacterial class, confidence, quality status and alternatives

Future product direction:
Serum or plasma pre-diagnostic support for a narrowly defined infectious-disease decision

Clinical status:
Research use only
```

3. Document the open questions:

- Which exact patient population?
- Which exact sample type?
- Which decision requires faster information?
- Who operates the instrument?
- Who interprets the result?
- What is the reference standard?
- What turnaround time creates value?
- What error rates are acceptable?
- What action follows an uncertain result?

4. Create the evidence ladder:

```text
Level 0:
Reliable software and Raman-processing pipeline

Level 1:
Public bacteria benchmark evidence

Level 2:
Acquisition and instrument robustness evidence

Level 3:
Retrospective serum or plasma feasibility study

Level 4:
Prospective silent clinical study

Level 5:
Regulated clinical product
```

## Business and investment tasks

1. Write a one-sentence company thesis.

> I am developing a Raman AI platform intended to extract clinically useful information from biological samples, beginning with a reproducible bacterial-spectrum classification engine and progressing toward serum or plasma validation.

2. Define the first stakeholder map:

- clinical microbiologist;
- laboratory director;
- infectious-disease clinician;
- emergency physician;
- Raman spectroscopy researcher;
- hospital innovation office;
- diagnostic-device manufacturer;
- regulator or regulatory consultant;
- medtech investor;
- non-dilutive funding organisation.

3. Create an interview script focused on problems rather than pitching.

4. Create `docs/business/investment_hypotheses.md` covering:

- problem;
- user;
- buyer;
- proposed value;
- workflow;
- alternatives;
- costs;
- adoption barriers;
- regulatory dependency;
- clinical-data dependency.

## Governance, regulation and IP tasks

1. Write the allowed claims.

2. Write the forbidden claims:

```text
No blood-disease detection claim.
No sepsis-detection claim.
No treatment recommendation.
No antibiotic-susceptibility prediction.
No hospital-readiness claim.
No regulatory-approval claim.
```

3. Create:

```text
docs/risk_register.md
docs/risk_register_investment.md
docs/decision_log.md
docs/data_governance.md
```

4. Review dependency licences, public-dataset terms and ownership of code created during academic work.

## Deliverables

- Clean repository
- Passing base checks
- README
- architecture document
- Target Product Profile v0
- evidence ladder
- claims register
- technical risk register
- investment risk register
- customer-discovery script
- initial stakeholder list

## Week 1 gate

Week 1 is complete when:

- the repository can be installed and tested from scratch;
- the prototype and non-prototype claims are explicit;
- the future use case is written as a testable hypothesis;
- the major technical, clinical and commercial risks are visible;
- at least five stakeholder interviews have been requested.

---

# Week 2: data ingestion, validation and problem discovery

## Objective

Build a trustworthy dataset layer and begin validating whether the proposed clinical problem is real and sufficiently important.

## Technical and scientific tasks

1. Obtain the public bacterial Raman dataset.

2. Validate the required files.

3. Load:

```text
train
validation
test
clinical2018
clinical2019
class metadata
wavenumbers
```

4. Implement explicit validation for:

- array dimensions;
- numeric dtypes;
- spectra-label alignment;
- finite values;
- wavenumber monotonicity;
- consistent spectral axes;
- duplicate spectra;
- duplicate spectra across splits;
- class consistency;
- empty and constant spectra;
- abnormal intensity ranges.

5. Implement spectral quality-control flags:

```text
flat spectrum
saturated spectrum
abnormal intensity
non-finite spectrum
axis mismatch
possible duplicate
```

6. Produce:

- split summary;
- class distribution;
- intensity summary;
- example raw spectra;
- mean spectra;
- validation report;
- raw dataset manifest.

7. Generate a validated interim dataset.

## Product and clinical tasks

1. Conduct at least three stakeholder interviews.

2. Interview at least:

- one clinical laboratory professional;
- one clinician;
- one Raman or spectroscopy specialist.

3. Record:

- current workflow;
- current turnaround time;
- current bottlenecks;
- failed or delayed decisions;
- acceptable sample preparation;
- required sensitivity;
- required specificity;
- consequence of errors;
- existing alternatives;
- willingness to test a research prototype.

4. Create `docs/product/clinical_workflow_v0.md`.

5. Define the ideal clinical label and reference standard for Prototype 1.

## Business and investment tasks

1. Start a competitor database covering:

- Raman infectious-disease companies;
- bacterial-identification systems;
- MALDI-TOF workflows;
- molecular diagnostics;
- rapid blood-culture systems;
- host-response diagnostics;
- AI spectroscopy platforms.

2. For each alternative, record:

```text
target use
sample type
time to result
capital cost
per-test cost
regulatory status
strengths
weaknesses
evidence level
```

3. Record the difference between:

- technical user;
- clinical beneficiary;
- budget holder;
- procurement decision-maker.

## Governance, regulation and IP tasks

1. Complete the dataset licence and provenance record.

2. Document which files may and may not be redistributed.

3. Add dataset versioning and file hashes.

4. Create a data-card template.

## Deliverables

- Validated data loader
- data-contract document
- quality-control module
- interim datasets
- raw manifest
- validation report
- dataset exploration notebook
- three completed interviews
- clinical workflow v0
- initial competitor database

## Week 2 gate

Week 2 is complete when:

- every raw input is traceable and validated;
- no split leakage or duplicate issue is left unexplained;
- the clinical problem hypothesis has received initial external feedback;
- the competitor database contains at least ten relevant alternatives;
- all data rights are documented.

---

# Week 3: preprocessing and clinical feasibility definition

## Objective

Build multiple controlled Raman preprocessing pipelines and convert the future clinical concept into a concrete pilot specification.

## Technical and scientific tasks

Implement and compare:

```text
P1: conservative fingerprint-region pipeline
P2: Georgiev-inspired pipeline
P3: MinMax-normalized sensitivity pipeline
P4: full-spectrum vector-normalized pipeline
```

Each pipeline must include declared choices for:

- cropping;
- despiking;
- smoothing;
- baseline correction;
- normalization;
- fitting policy;
- output validation.

For each pipeline:

1. Fit any global parameters on `train` only.
2. Apply the unchanged transformation to all other splits.
3. Preserve labels and sample ordering.
4. Validate shape and axis consistency.
5. reject NaNs and infinite values.
6. Save preprocessing metadata.
7. Save the configuration hash.
8. Save processed split manifests.
9. Plot raw-versus-processed examples.
10. Compare all pipelines on the same spectra.

The current repository already has the intended four-pipeline structure, train-only rules, processed-data integrity requirements and extensive Week 3 checks.

No model may be trained to choose the pipeline during Week 3.

Candidate preprocessing decisions must use:

- spectroscopy principles;
- train-set quality evidence;
- validation-set sanity evidence;
- stability;
- absence of artefacts;
- computational cost.

Test and clinical splits may only be inspected for transformation integrity, not performance selection.

## Product and clinical tasks

1. Write `docs/product/prototype1_data_specification.md`.

Include:

```text
sample type
collection tube
storage temperature
freeze-thaw policy
preparation protocol
substrate
instrument
laser wavelength
power
integration time
replicate count
calibration protocol
reference labels
clinical covariates
minimum metadata
exclusion criteria
```

2. Write two possible Prototype 1 routes.

### Route A: instrument access exists

Perform a non-diagnostic Raman acquisition feasibility experiment using commercially available control matrices or approved non-clinical samples.

The purpose is only to test:

- acquisition;
- signal quality;
- reproducibility;
- preprocessing compatibility;
- replicate variation.

No disease-classification conclusion may be made.

### Route B: no instrument access exists

Secure:

- a spectroscopy laboratory contact;
- an acquisition quotation;
- a draft access agreement;
- a documented experimental protocol.

3. Conduct at least three additional stakeholder interviews.

4. Refine the narrow intended-use hypothesis.

## Business and investment tasks

1. Write the first value-chain map.

2. Estimate:

- current diagnostic pathway cost;
- staff time;
- instrument time;
- delay cost;
- potential value of earlier information.

3. Separate quantified facts from assumptions.

4. Create a partner target list:

- hospitals;
- microbiology laboratories;
- spectroscopy facilities;
- university laboratories;
- instrument manufacturers;
- contract research organisations.

## Governance, regulation and IP tasks

1. Create a preliminary regulatory memo.

2. Record that a future system analysing blood, serum or plasma to provide diagnostic information would likely fall within the EU in-vitro diagnostic framework, subject to the exact intended purpose and configuration. The IVDR has applied in the EU since 26 May 2022.

3. Do not assign a definitive risk class without regulatory review.

4. Start the preliminary patent and publication landscape.

## Deliverables

- Four valid preprocessing pipelines
- processed datasets
- preprocessing comparison notebook
- generated diagnostics
- pipeline metadata and hashes
- Prototype 1 data specification
- acquisition feasibility route
- preliminary regulatory memo
- value-chain map
- six cumulative stakeholder interviews

## Week 3 gate

Week 3 is complete when:

- all preprocessing pipelines pass integrity checks;
- at least one primary candidate and two sensitivity pipelines are documented;
- no model or test evidence has influenced preprocessing selection;
- the future acquisition protocol is concrete enough for a laboratory to review;
- there is a named route to instrument or sample access.

---

# Week 4: baseline models and use-case validation

## Objective

Establish strong, interpretable baselines while testing whether the intended users value the proposed output.

## Technical and scientific tasks

Train reproducible baseline pipelines:

```text
StandardScaler + LogisticRegression
StandardScaler + PCA + LogisticRegression
StandardScaler + Linear SVM
StandardScaler + PCA + RBF SVM
PLS-based classifier
RandomForest baseline
```

For every experiment, record:

- preprocessing configuration;
- feature configuration;
- hyperparameters;
- random seed;
- training time;
- inference time;
- validation metrics;
- software version;
- data-manifest hash.

Use:

```text
train:
parameter fitting

validation:
pipeline and hyperparameter selection

test:
untouched

clinical splits:
untouched
```

Implement a common estimator interface and an experiment registry.

## Product and clinical tasks

1. Show prototype outputs, not performance claims, to three intended users.

2. Ask:

- Is the predicted class useful?
- Is top-k output useful?
- Is uncertainty useful?
- Which quality information is required?
- What would cause immediate rejection?
- Who should see the result?
- Where would it enter the workflow?

3. Update the Target Product Profile.

4. Define the desired output independently from what the current dataset happens to provide.

## Business and investment tasks

1. Complete competitor segmentation.

2. Define the initial wedge:

```text
research platform
laboratory decision-support tool
acquisition-quality platform
spectral-analysis software
future integrated diagnostic device
```

3. Decide which wedge is most credible for the first external conversation.

4. Draft a one-page problem statement without technical jargon.

## Governance, regulation and IP tasks

1. Create a model-development plan.

2. Create a model-card template.

3. Create a software requirements specification.

4. Begin a traceability matrix:

```text
requirement
risk
implementation
test
evidence
```

## Deliverables

- Reproducible baseline models
- experiment registry
- validation comparison table
- updated Target Product Profile
- nine cumulative interviews
- competitor segmentation
- model-development plan
- initial traceability matrix

## Week 4 gate

Week 4 is complete when:

- a command-line run can reproduce every baseline;
- no test or clinical split has been used for selection;
- baseline results include variability, not a single lucky run;
- intended users have reviewed the proposed output;
- the product wedge is explicit.

---

# Week 5: model benchmark, robustness and defensibility

## Objective

Select the most reliable modelling strategy and determine whether it learns stable Raman structure rather than fragile dataset artefacts.

## Technical and scientific tasks

Benchmark:

```text
regularized logistic regression
linear SVM
RBF SVM
PCA variants
PLS-based model
RandomForest
XGBoost
LightGBM
optional compact 1D CNN
```

Deep learning is optional and may only be selected if it provides repeatable, meaningful improvement without damaging calibration, interpretability or deployment simplicity.

Run:

- repeated seeds;
- bootstrap confidence intervals;
- hyperparameter stability analysis;
- training-time comparison;
- inference-time comparison;
- memory comparison.

Implement perturbation testing:

```text
wavenumber shift
intensity scaling
additive noise
baseline drift
peak broadening
reduced spectral resolution
spectral masking
spike contamination
```

Measure performance degradation against perturbation strength.

Investigate whether model predictions rely on:

- clinically or chemically plausible peaks;
- acquisition artefacts;
- baseline structure;
- split-specific signatures.

## Product and clinical tasks

1. Validate the required operating characteristics with users.

2. Define:

- minimum acceptable performance;
- maximum false-negative rate;
- maximum false-positive rate;
- required coverage;
- acceptable uncertain rate;
- turnaround requirement.

These remain hypotheses until clinical studies.

3. Identify one potential clinical or spectroscopy advisor.

## Business and investment tasks

1. Conduct at least three further interviews.

2. Produce:

```text
market map
buyer map
procurement map
adoption barriers
economic assumptions
```

3. Build a preliminary bottom-up market model based on:

- number of possible sites;
- tests per site;
- instrument model;
- licence model;
- service model;
- realistic adoption sequence.

Do not rely only on a top-down market percentage.

## Governance, regulation and IP tasks

1. Complete a preliminary patent landscape.

2. Document possible defensibility sources:

- proprietary clinical dataset;
- acquisition protocol;
- spectral harmonisation;
- quality-control system;
- uncertainty and eligibility engine;
- workflow integration;
- clinical evidence;
- hardware-software combination.

3. Separate true proprietary elements from open-source or standard methods.

## Deliverables

- Full benchmark table
- robustness report
- perturbation curves
- model-selection recommendation
- advisor target
- 12 cumulative interviews
- bottom-up market model
- preliminary IP and defensibility memo

## Week 5 gate

Select the model family only if:

- results are stable across seeds;
- improvement is meaningful rather than marginal;
- calibration can be supported;
- inference is operationally feasible;
- robustness is acceptable;
- no uncontrolled leakage has been discovered;
- the selection can be justified in plain language.

---

# Week 6: model lock and internal test evaluation

## Objective

Freeze the analytical pipeline and perform the single final internal test evaluation.

## Technical and scientific tasks

Before opening the test result, lock:

```text
preprocessing pipeline
model family
hyperparameters
random seed policy
calibration plan
evaluation metrics
confidence-interval method
failure criteria
```

Create a signed or hashed model-lock record.

Train the final internal model on:

```text
train + validation
```

Evaluate once on:

```text
test
```

Report:

- all predefined metrics;
- bootstrap 95% confidence intervals;
- per-class denominators;
- confusion matrix;
- top-k errors;
- inference time;
- calibration before calibration work;
- robustness results;
- representative errors.

Do not tune after reviewing the test results.

Any later change creates a new development version and invalidates the original locked-test status.

## Product and clinical tasks

1. Write `docs/clinical/prototype1_pilot_protocol_v0.md`.

Include:

- objective;
- study population;
- inclusion criteria;
- exclusion criteria;
- sample type;
- collection timing;
- reference standard;
- acquisition protocol;
- primary endpoint;
- secondary endpoints;
- subgroup analyses;
- missing-data handling;
- analysis lock;
- limitations;
- no-impact-on-care statement.

2. Draft sample-size scenarios rather than inventing one definitive number.

3. Request review from a clinician and spectroscopy expert.

## Business and investment tasks

1. Define Prototype 1 milestones and budget categories:

```text
ethics and legal
sample access
instrument time
consumables
data management
personnel
regulatory advice
software development
statistics
contingency
```

2. Define what an investment would de-risk.

3. Prepare a use-of-funds table for:

```text
€100k
€250k
€500k
€1m
```

## Governance, regulation and IP tasks

1. Freeze the Version 0.1 software bill of materials.

2. Create:

- model card;
- test report;
- known-limitations register;
- software version record;
- change-control procedure.

## Deliverables

- Locked internal model
- final test report
- confidence intervals
- model-lock record
- pilot protocol v0
- sample-size scenarios
- use-of-funds scenarios
- model card
- change-control procedure

## Week 6 gate

Week 6 passes only if:

- the evaluation was predeclared;
- the test split was not used for tuning;
- all negative results are reported;
- the model version is reproducible;
- the pilot protocol is reviewable by an external expert.

---

# Week 7: clinical-isolate generalisation and failure analysis

## Objective

Determine how the locked pipeline behaves under the most clinically relevant shift available in the public dataset.

## Technical and scientific tasks

Evaluate the locked model separately on:

```text
clinical2018
clinical2019
```

Do not merge them into a single headline score.

Compare:

```text
validation
internal test
clinical2018
clinical2019
```

Analyse:

- absolute performance drop;
- relative performance drop;
- class-specific failure;
- confidence on errors;
- calibration drift;
- spectral-distribution shift;
- quality-control rejection;
- perturbation sensitivity;
- likely acquisition or cohort differences.

Perform embedding and distance analysis to identify domain shift.

Create a structured failure taxonomy:

```text
low signal quality
class ambiguity
domain shift
preprocessing instability
model overconfidence
rare class
possible label issue
unknown cause
```

## Product and clinical tasks

1. Present the failure modes to advisors.

2. Ask which failures would be tolerable and which would be unacceptable in the future use case.

3. Update the pilot protocol to collect the metadata required to explain these failures.

4. Begin formal discussions with potential sample-access partners.

## Business and investment tasks

1. Create the first non-confidential partner brief.

2. Contact:

- hospital research groups;
- microbiology laboratories;
- Raman facilities;
- instrument companies;
- innovation offices.

3. Ask for:

- scientific feedback;
- instrument access;
- sample-access feasibility;
- protocol review;
- research collaboration;
- a non-binding letter of interest.

## Governance, regulation and IP tasks

1. Create a preliminary hazard analysis.

Examples:

```text
poor-quality input receives prediction
out-of-domain input receives prediction
incorrect high-confidence result
incorrect metadata mapping
model or preprocessing version mismatch
untraceable acquisition conditions
silent software failure
```

2. Define a mitigation and verification test for every hazard.

## Deliverables

- Clinical-split report
- domain-shift analysis
- failure taxonomy
- updated pilot protocol
- partner brief
- outreach log
- hazard analysis
- mitigation traceability

## Week 7 gate

Week 7 is complete when:

- external-split degradation is quantified honestly;
- failures are categorised;
- no clinical conclusion exceeds the dataset evidence;
- at least three potential partners have received the research brief;
- every major safety failure has a proposed mitigation.

---

# Week 8: calibration, rejection, OOD and safety logic

## Objective

Transform the classifier into a system that can abstain, reject poor inputs and communicate uncertainty.

## Technical and scientific tasks

Compare calibration methods:

```text
Platt scaling
isotonic regression
temperature scaling where applicable
```

Calibration parameters must be fitted without using test or clinical splits.

Evaluate:

- Brier score;
- log loss;
- expected calibration error;
- reliability curves;
- calibration by class;
- calibration under domain shift.

Implement selective prediction.

Choose the threshold on validation evidence according to a predefined constraint, such as:

```text
maximize coverage
subject to accepted-sample error below a declared limit
```

Report:

```text
threshold
coverage
accepted accuracy
accepted macro-F1
rejection rate
error rate among accepted predictions
```

Implement an input-eligibility layer:

```text
spectral quality checks
axis checks
intensity checks
preprocessing checks
distance-to-training-domain checks
OOD score
classifier confidence
```

Compare OOD approaches:

- PCA distance;
- Mahalanobis distance;
- nearest-neighbour distance;
- ensemble disagreement;
- conformal prediction where appropriate.

The final report must distinguish:

```text
Low classification confidence:
Several known classes are plausible.

Out of distribution:
The sample does not sufficiently resemble the validated training domain.

Quality rejection:
The Raman acquisition does not meet input requirements.
```

## Product and clinical tasks

1. Define the human action for each status:

```text
accepted
uncertain
out of distribution
quality failure
software failure
```

2. Review the wording with intended users.

3. Ensure the system never presents rejection as a diagnosis.

## Business and investment tasks

1. Quantify the commercial tradeoff between:

- high coverage;
- high accepted accuracy;
- repeat acquisitions;
- confirmatory testing;
- workflow delay.

2. Explain why rejection can create safety value rather than appear as model failure.

## Governance, regulation and IP tasks

1. Create the first safety case.

2. Map:

```text
hazard
control
software requirement
test
result
residual risk
```

3. Update the preliminary regulatory memo.

## Deliverables

- Calibrated model
- threshold-selection report
- rejection curves
- OOD module
- input-eligibility module
- human-action matrix
- safety case
- updated model card

## Week 8 gate

Week 8 is complete when:

- thresholds are selected without test leakage;
- the system can refuse unsuitable inputs;
- uncertainty types are distinguishable;
- every user-facing status has a clear action;
- high-confidence errors are specifically analysed.

---

# Week 9: reporting, transparency and pilot package

## Objective

Convert model output and technical evidence into transparent materials for researchers, clinicians and investors.

## Technical and scientific tasks

Build a structured report generator containing:

```text
sample ID
acquisition metadata
input quality
eligibility status
predicted class
calibrated probability
top alternatives
uncertainty status
OOD status
model version
preprocessing version
limitations
research-use-only notice
```

Do not place antibiotic metadata in the main clinical-style result.

If retained, display it only in a separate dataset-metadata section with an explicit statement that it is not an antimicrobial susceptibility prediction.

Generate both:

- human-readable HTML or PDF;
- machine-readable JSON.

Create:

- dataset card;
- model card;
- performance summary;
- known-failure document;
- reproducibility guide.

## Product and clinical tasks

1. Finalise the pilot package:

```text
Target Product Profile
pilot protocol
data specification
acquisition specification
metadata dictionary
analysis plan
sample-size scenarios
research-only output example
partner responsibilities
```

2. Obtain written feedback from at least one relevant external expert.

## Business and investment tasks

1. Write the first clinical-partner one-pager.

2. Write the first investor one-pager.

3. Separate the two narratives.

### Clinical narrative

- silent research study;
- no impact on care;
- explicit scientific question;
- required samples and metadata;
- joint validation;
- possible publication.

### Investor narrative

- problem;
- technology thesis;
- Prototype 0 evidence;
- remaining risks;
- Prototype 1 milestone;
- capital required;
- value created by the next dataset.

## Governance, regulation and IP tasks

1. Complete a preliminary cybersecurity and privacy architecture.

2. Document:

- data minimisation;
- de-identification;
- access control;
- storage;
- audit logs;
- retention;
- deletion;
- incident response.

## Deliverables

- Report generator
- sample reports
- JSON schema
- complete transparency documentation
- partner one-pager
- investor one-pager
- pilot package
- privacy and cybersecurity architecture

## Week 9 gate

Week 9 is complete when:

- a result can be audited back to its data, model and preprocessing versions;
- limitations are visible in the output;
- the clinical package can be sent without investor language;
- the investor package can be read without opening the codebase.

---

# Week 10: interactive demonstrator and external usability

## Objective

Build a polished but honest live demonstrator and test whether external users understand it correctly.

## Technical and scientific tasks

Build a Streamlit application with:

### Page 1: sample analysis

- raw spectrum;
- processed spectrum;
- quality status;
- prediction;
- top alternatives;
- calibrated confidence;
- OOD status;
- report export.

### Page 2: model evidence

- internal test results;
- clinical2018 results;
- clinical2019 results;
- confidence intervals;
- class-level results;
- confusion matrices.

### Page 3: uncertainty

- calibration curves;
- threshold controls;
- coverage-versus-performance;
- rejection reasons;
- examples of uncertain inputs.

### Page 4: robustness

- perturbation experiments;
- shift analysis;
- known limitations;
- failure examples.

### Page 5: development roadmap

- what Prototype 0 proves;
- what it does not prove;
- Prototype 1 study;
- evidence ladder.

Package the application so it runs from a documented command.

## Product and clinical tasks

1. Conduct at least five usability sessions.

2. Include:

- clinician or laboratory professional;
- spectroscopy researcher;
- technical ML reviewer;
- non-technical healthcare stakeholder;
- potential investor or entrepreneur.

3. Ask users to explain the result back to me.

4. Record misunderstandings.

5. Revise terminology that causes overinterpretation.

## Business and investment tasks

1. Produce a three-minute demo script.

2. Create answers for difficult questions:

- Why bacteria?
- Why does this transfer to blood?
- What is proprietary?
- What is the regulatory pathway?
- What evidence is missing?
- What happens if the serum signal is insufficient?
- Why will a hospital adopt this?
- Why cannot an instrument manufacturer build it?
- What does the next investment purchase?
- What is the first revenue route?

3. Draft a credible pivot strategy.

Possible pivots include:

- Raman quality-control platform;
- research-use spectral analytics;
- bacterial isolate classification;
- instrument harmonisation;
- laboratory workflow software;
- clinical research platform.

## Governance, regulation and IP tasks

1. Red-team the application for misleading outputs.

2. Verify that all screens state:

```text
Research prototype
Not for diagnosis
Not for treatment decisions
```

3. Test logging, errors and invalid inputs.

## Deliverables

- Working application
- demo script
- usability report
- revised terminology
- recorded demonstration
- difficult-question document
- pivot map
- error-handling tests

## Week 10 gate

Week 10 is complete when:

- the application runs from a clean environment;
- external users understand the output correctly;
- the demo exposes weaknesses rather than hiding them;
- invalid and OOD inputs cannot silently produce normal-looking predictions;
- the three-minute presentation is repeatable.

---

# Week 11: investment case, data room and external proof

## Objective

Assemble the technical, clinical and commercial evidence into a due-diligence-ready package.

Accelerators such as MedTech Innovator prefer applicants with a prototype and at least some proof-of-concept evidence. Their review environment includes investors, providers, payers, regulators and corporate decision-makers.

European deep-tech funding also evaluates more than the technology. The 2026 EIC Accelerator process requires applicants to address innovation, potential market and team, while the full proposal can include an implementation plan, financial information, letters of intent and FTO analysis.

## Technical and scientific tasks

Write the technical report:

```text
1. Executive summary
2. Intended scope
3. Dataset
4. Data validation
5. Preprocessing
6. Model development
7. Selection protocol
8. Locked evaluation
9. Clinical-split evaluation
10. Calibration
11. OOD and rejection
12. Robustness
13. Failure analysis
14. Reproducibility
15. Limitations
16. Prototype 1 plan
```

Have an external technical reviewer inspect:

- methodology;
- leakage risk;
- metrics;
- claims;
- reproducibility;
- statistics.

Record and resolve comments.

## Product and clinical tasks

1. Obtain one or more of:

- advisor agreement;
- written protocol feedback;
- instrument-access confirmation;
- meeting memorandum;
- non-binding letter of interest;
- preliminary collaboration proposal.

2. Finalise the clinical evidence plan.

3. Explicitly state the question Prototype 1 must answer:

> Does Raman spectroscopy applied to the specified serum or plasma protocol contain reproducible information that improves the intended clinical classification or triage task beyond predefined baseline information?

## Business and investment tasks

Create the investment data room:

```text
01_company/
02_pitch/
03_product/
04_technology/
05_scientific_evidence/
06_clinical_strategy/
07_regulatory/
08_market/
09_competition/
10_ip_and_licensing/
11_financials/
12_partnerships/
13_risks/
14_team/
```

Prepare:

- ten-slide pitch deck;
- three-minute video pitch;
- investor one-pager;
- market model;
- competitor matrix;
- business model;
- 24-month milestones;
- use-of-funds plan;
- hiring plan;
- funding-source map;
- risk-adjusted development plan.

Do not present the EIC Accelerator as an immediate Week 12 funding target unless the company and technology meet its maturity requirements. Its 2026 programme is aimed at innovations around TRL 6 to 8.

Nearer-term targets may include:

- university proof-of-concept funds;
- regional innovation grants;
- Bpifrance programmes;
- research collaborations;
- incubators;
- angel investors;
- medtech accelerators;
- hospital innovation funding;
- instrument-company partnerships.

## Governance, regulation and IP tasks

Complete:

- preliminary FTO report;
- licence register;
- code-ownership record;
- data-rights record;
- regulatory memo;
- risk-management file;
- software traceability;
- cybersecurity summary;
- claims register.

## Deliverables

- Technical report
- external-review record
- complete data room
- pitch deck
- video pitch
- financial model
- partner evidence
- preliminary FTO
- 24-month development plan

## Week 11 gate

Week 11 is complete when:

- every pitch claim links to evidence;
- every major uncertainty is visible;
- the next experiment and its cost are explicit;
- a technical reviewer has challenged the work;
- at least one external stakeholder has provided written evidence of interest or substantive review.

---

# Week 12: independent verification, pitch readiness and Prototype 1 decision

## Objective

Prove that the package works independently, present it under scrutiny, and make an evidence-based decision about the next phase.

## Technical and scientific tasks

1. Rebuild the project from a clean checkout.

2. Run the complete pipeline from raw data to final reports.

3. Verify:

```text
environment lock
data manifests
preprocessing hashes
model hashes
test results
clinical-split results
figures
reports
application
```

4. Run all tests and static checks.

5. Conduct a final leakage audit.

6. Conduct a final claims audit.

7. Conduct a final robustness and failure review.

8. Archive a release:

```text
v0.1.0 Prototype 0
```

9. Produce a release manifest.

## Product and clinical tasks

Hold a Prototype 1 review with at least two external viewpoints.

Evaluate:

- clinical importance;
- protocol feasibility;
- sample access;
- instrument access;
- reference-label quality;
- study cost;
- ethics requirements;
- expected decision value.

Decide:

```text
GO:
Proceed with serum or plasma feasibility study.

CONDITIONAL GO:
Resolve specified access, protocol or regulatory issue first.

PIVOT:
Use the Raman engine for a more defensible initial application.

STOP:
Evidence does not justify further expenditure.
```

## Business and investment tasks

1. Conduct at least three mock investment meetings.

2. Use reviewers with different perspectives:

- technical;
- clinical;
- commercial.

3. Record every objection.

4. Update the deck and data room only when evidence supports the change.

5. Create the first 50-target outreach list:

```text
clinical partners
scientific advisors
instrument partners
incubators
grant programmes
angels
medtech funds
strategic companies
```

6. Create a structured outreach tracker.

7. Define the exact funding request:

```text
amount
runway
milestones
value inflection point
risks removed
deliverables
next financing event
```

## Governance, regulation and IP tasks

1. Freeze all Prototype 0 documentation.

2. Ensure all research-use notices are present.

3. Document open regulatory questions for professional advice.

4. Create a controlled change list for Prototype 1.

## Final deliverables

By the end of Week 12, I must possess:

### Technology

- validated Raman data layer;
- four preprocessing pipelines;
- model benchmark;
- locked final model;
- calibrated probabilities;
- OOD and rejection system;
- robustness analysis;
- report generator;
- working application;
- one-command reproducibility.

### Scientific evidence

- internal test report;
- clinical-isolate split report;
- confidence intervals;
- repeated-seed results;
- calibration report;
- robustness report;
- failure analysis;
- model card;
- data card;
- technical report.

### Clinical translation

- Target Product Profile;
- intended-use hypothesis;
- clinical workflow;
- Prototype 1 data specification;
- acquisition protocol;
- pilot protocol;
- sample-size scenarios;
- advisor feedback;
- partner outreach evidence;
- path to samples and instrument access.

### Business and investment

- customer-discovery report;
- competitor map;
- market model;
- value-chain analysis;
- business-model hypotheses;
- use-of-funds scenarios;
- 24-month roadmap;
- investor one-pager;
- pitch deck;
- pitch video;
- data room;
- outreach target list.

### Governance and defensibility

- claims register;
- technical risk register;
- investment risk register;
- preliminary regulatory memo;
- hazard analysis;
- traceability matrix;
- privacy and cybersecurity plan;
- licensing register;
- IP landscape;
- preliminary FTO;
- software bill of materials;
- change-control procedure.

## Final Week 12 success statement

At the end of the programme, I should be able to make the following claim:

> I have built a reproducible Raman machine-learning platform on a public biological spectroscopy benchmark. The platform validates spectral inputs, applies controlled preprocessing, trains and locks classification models, evaluates them on internal and clinical-isolate splits, quantifies uncertainty, rejects unsuitable inputs, tests robustness to acquisition perturbations and produces traceable reports. In parallel, I have defined a focused future clinical use case, documented the regulatory and validation assumptions, tested the product hypothesis with relevant stakeholders, prepared a serum or plasma pilot protocol, and established a credible route toward samples, instrument access and Prototype 1 funding.

## Final decision rule

I must not raise money merely to “improve the AI.”

The next funding request must finance a defined evidence milestone:

> Acquisition and analysis of the first controlled serum or plasma dataset needed to determine whether the future clinical product is scientifically feasible.

That is the transition from an interesting technical project to an investable medtech programme.
