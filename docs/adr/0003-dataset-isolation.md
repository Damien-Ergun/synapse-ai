# ADR-0003: Raw dataset isolation

Status: Accepted

Raw NumPy arrays are immutable external inputs, excluded from Git, identified by SHA-256 manifests, and accessed through controlled loaders.
