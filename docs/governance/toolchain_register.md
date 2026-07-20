# Toolchain register

| Component | Required version or reference | Role | Evidence source | Status |
|---|---|---|---|---|
| CPython | 3.11.15 evidence target; support `>=3.11,<3.12` | Runtime | `.python-version`, `pyproject.toml` | To verify on user workstation and CI |
| uv | 0.11.29 | Environment, lock, sync, execution | `pyproject.toml` and official uv documentation | Required |
| Git | Record observed version in evidence manifest | Version control | Local evidence | Pending user workstation evidence |
| PowerShell | Record observed version in evidence manifest | Canonical shell | Local evidence | Pending user workstation evidence |
| actions/checkout | commit `9c091bb21b7c1c1d1991bb908d89e4e9dddfe3e0` | CI checkout | Workflow | Pinned |
| astral-sh/setup-uv | commit `08807647e7069bb48b6ef5acd8ec9567f424441b` | CI uv and Python setup | Workflow | Pinned |
