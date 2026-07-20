# Dependency licence register

## Status

`COMPLETE FOR UV.LOCK SHA-256 65594067016c5eb1442d586573468e80e79bdff3dd9270db2a0f445175dc5939`

This register covers every third-party package represented in the current lock, the declared build backend, the target runtime, the pinned environment manager, and the two pinned GitHub Actions. The project itself is excluded from the third-party count. Reconciliation must be repeated whenever `pyproject.toml`, `uv.lock`, the CI workflow, or the target interpreter changes.

Package metadata was used to identify licence expressions, then checked against the named upstream project or licence file. This is a technical diligence record, not legal advice.

## Locked Python packages

| Component | Locked version | Relationship | Scope and marker | Purpose | Licence | Authoritative project or licence source | Compatibility conclusion | Required action |
|---|---:|---|---|---|---|---|---|---|
| black | 26.5.1 | Direct | Development | Formatting | MIT | `https://github.com/psf/black` | Permissive development dependency | Recheck on lock change |
| click | 8.4.2 | Transitive through Black | Development | Black CLI dependency | BSD-3-Clause | `https://github.com/pallets/click` | Permissive | Recheck on lock change |
| colorama | 0.4.6 | Transitive through Click and Pytest | Development, Windows only | Terminal colour compatibility | BSD-3-Clause | `https://github.com/tartley/colorama` | Permissive | Recheck on lock change |
| coverage | 7.15.2 | Transitive through pytest-cov | Development | Coverage engine | Apache-2.0 | `https://github.com/nedbat/coveragepy` | Permissive; notice obligations apply to redistribution | Retain applicable notices if redistributed |
| iniconfig | 2.3.0 | Transitive through Pytest | Development | Configuration parsing | MIT | `https://github.com/pytest-dev/iniconfig` | Permissive | Recheck on lock change |
| mypy-extensions | 1.1.0 | Transitive through Black | Development | Typing helpers | MIT | `https://github.com/python/mypy_extensions` | Permissive | Recheck on lock change |
| packaging | 26.2 | Transitive through Black and Pytest | Development | Version and requirement parsing | Apache-2.0 OR BSD-2-Clause | `https://github.com/pypa/packaging` | Permissive dual option | Retain applicable notices if redistributed |
| pathspec | 1.1.1 | Transitive through Black | Development | Path matching | MPL-2.0 | `https://github.com/cpburnz/python-pathspec` | File-level copyleft does not affect unchanged use as a development dependency | Review before modifying or redistributing this component |
| platformdirs | 4.10.1 | Transitive through Black | Development | Platform directory discovery | MIT | `https://github.com/tox-dev/platformdirs` | Permissive | Recheck on lock change |
| pluggy | 1.6.0 | Transitive through Pytest and pytest-cov | Development | Plugin system | MIT | `https://github.com/pytest-dev/pluggy` | Permissive | Recheck on lock change |
| Pygments | 2.20.0 | Transitive through Pytest | Development | Terminal syntax highlighting | BSD-2-Clause | `https://github.com/pygments/pygments` | Permissive | Recheck on lock change |
| pytest | 9.1.1 | Direct | Development | Test runner | MIT | `https://github.com/pytest-dev/pytest` | Permissive development dependency | Recheck on lock change |
| pytest-cov | 7.1.0 | Direct | Development | Coverage integration | MIT | `https://github.com/pytest-dev/pytest-cov` | Permissive development dependency | Recheck on lock change |
| pytokens | 0.4.1 | Transitive through Black | Development | Python tokenisation | MIT | `https://github.com/tusharsadhwani/pytokens` | Permissive | Recheck on lock change |
| ruff | 0.15.22 | Direct | Development | Linting | MIT | `https://github.com/astral-sh/ruff` | Permissive development dependency | Recheck on lock change |
| tomli | 2.4.1 | Transitive through coverage | Development, Python 3.11 marker | TOML parsing support | MIT | `https://github.com/hukkin/tomli` | Permissive | Recheck on lock change |

## Runtime, build, and automation components

| Component | Controlled version or reference | Relationship | Scope | Licence | Authoritative source | Compatibility conclusion | Required action |
|---|---|---|---|---|---|---|---|
| CPython | 3.11.15 evidence target; project range `>=3.11,<3.12` | Runtime | Runtime | Python Software Foundation License | `https://docs.python.org/3/license.html` | Permissive runtime licence with notice terms | Record exact local and CI patch in evidence |
| uv | 0.11.29 | Direct toolchain | Environment, locking, execution | Apache-2.0 OR MIT | `https://github.com/astral-sh/uv` | Permissive dual licence | Recheck on toolchain change |
| uv-build | `>=0.11.29,<0.12` | Direct build backend, resolved by build isolation rather than the project lock | Build | Apache-2.0 OR MIT | `https://github.com/astral-sh/uv` | Permissive dual licence | Record the exact build-isolation version in release evidence |
| actions/checkout | `9c091bb21b7c1c1d1991bb908d89e4e9dddfe3e0` | Direct CI action | CI | MIT | `https://github.com/actions/checkout` | Permissive | Review pin and licence on workflow update |
| astral-sh/setup-uv | `08807647e7069bb48b6ef5acd8ec9567f424441b` | Direct CI action | CI | MIT | `https://github.com/astral-sh/setup-uv` | Permissive | Review pin and licence on workflow update |

## Reconciliation evidence

| Evidence | Path | SHA-256 | Status |
|---|---|---|---|
| Controlled lock | `uv.lock` | `65594067016c5eb1442d586573468e80e79bdff3dd9270db2a0f445175dc5939` | Committed |
| Locked package tree | `reports/generated/week_1/locked_packages.txt` | `3b1f0442b98db54dc428c572550553fe9822c3b50aae94b76df242993c52e224` | Local and ignored |
| CycloneDX 1.5 provisional SBOM | `reports/generated/week_1/dependency_sbom.cdx.json` | `26f4f81f617aeeeb6362320711ec168571e9a7d4ce548cdc204f46a2acb5322f` | Local and ignored |

## Reconciliation result

- Current lock contains 16 third-party Python packages plus the project package.
- Every locked third-party Python package has one register row.
- There are no runtime Python package dependencies in Week 1.
- The development dependency set is compatible with research-only project use based on the recorded permissive licences and the stated MPL-2.0 treatment for Pathspec.
- This review does not authorize dataset use, public relicensing of project code, or commercial distribution.
