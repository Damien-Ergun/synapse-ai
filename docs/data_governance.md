# Data governance

## 1. Scope

This policy covers public research datasets, generated artifacts, stakeholder discovery records, and future clinical metadata. Week 1 contains no spectrum array or patient data.

## 2. Data zones

| Zone | Location | Commit status | Rule |
|---|---|---|---|
| Controlled metadata and policies | `docs/`, `configs/` | Committed | No sensitive content |
| Raw data | `data/raw/` | Local only | Immutable after verified acquisition |
| Interim data | `data/interim/` | Local only | Reproducible from raw data and config |
| Processed data | `data/processed/` | Local only | Reproducible and manifest-linked |
| Models | `models/` | Local only | Hash, config, seed, and training manifest required later |
| Logs and generated reports | `reports/logs/`, `reports/generated/` | Local only | Sanitised manifest hashes may be committed |
| Sensitive data | No default location | Prohibited | Requires separate approval and controls |

## 3. Dataset split permissions

| Split | First array inspection | Permitted use | Forbidden use before assigned week |
|---|---:|---|---|
| `train` | Week 2 after rights authorization | Integrity checks; later transformation and model fitting | Any access before rights gate |
| `validation` | Week 2 for integrity only | Development sanity; later selection | Final claims or test-like reporting |
| `test` | Week 2 for file integrity only | Structural validation without performance inspection; final evaluation in Week 6 | Selection, tuning, metric inspection |
| `clinical2018` | Week 2 for file integrity only | Structural validation; locked evaluation in Week 7 | Selection, tuning, performance inspection |
| `clinical2019` | Week 2 for file integrity only | Structural validation; locked evaluation in Week 7 | Selection, tuning, performance inspection |

## 4. Provenance and reproducibility

Every acquired file requires source URI, source filename, retrieval timestamp, byte size, SHA-256, dataset version, split role, rights record ID, and manifest identifier. Every generated artifact requires source-manifest hash, config hash, software version, seed where stochastic, and creation timestamp.

## 5. Leakage prevention

Transformations with learned parameters fit on `train` only unless a later locked protocol states otherwise. Labels and ordered sample IDs are checked before and after transformation. Test and clinical metrics cannot influence development. Any accidental reserved-split performance access is an incident, invalidates affected selection evidence, and creates a risk and decision-log entry.

## 6. Retention and deletion

Public research arrays remain local only while needed for the controlled programme and are deleted if rights are revoked or source integrity cannot be established. Private stakeholder identity mappings are retained for no more than 12 months after the last follow-up unless a documented relationship requires longer retention. Deletion is recorded by evidence ID.

## 7. Security and privacy

No credentials, contact details, contracts, patient identifiers, or confidential institutional data are committed. Local private records use access-controlled storage outside Git. Security incidents are recorded and escalated through the risk register.
