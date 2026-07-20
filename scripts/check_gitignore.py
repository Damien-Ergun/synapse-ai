"""Validate every required ignore and negation rule independently."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

IGNORED = (
    ".venv/placeholder.txt",
    ".env",
    ".env.local",
    "data/raw/placeholder.npy",
    "data/interim/placeholder.npy",
    "data/processed/placeholder.npy",
    "models/placeholder.joblib",
    "reports/logs/placeholder.txt",
    "reports/generated/placeholder.json",
    "package/__pycache__/placeholder.pyc",
    ".pytest_cache/placeholder",
    ".ruff_cache/placeholder",
    "notebooks/.ipynb_checkpoints/placeholder.ipynb",
)
TRACKABLE = (
    ".env.example",
    "data/README.md",
    "models/README.md",
    "reports/README.md",
    "uv.lock",
    "configs/README.md",
)


def repository_root() -> Path:
    """Return the repository root from the script location."""
    return Path(__file__).resolve().parents[1]


def is_ignored(root: Path, path: str) -> tuple[bool, str]:
    """Check one path and return its exact Git explanation."""
    completed = subprocess.run(
        ["git", "check-ignore", "--no-index", "--verbose", "--", path],
        cwd=root,
        capture_output=True,
        text=True,
        check=False,
    )
    detail = (completed.stdout + completed.stderr).strip()
    if completed.returncode != 0:
        return False, detail
    first_line = detail.splitlines()[0] if detail else ""
    rule_and_path = first_line.split("\t", 1)[0]
    matched_pattern = rule_and_path.rsplit(":", 1)[-1]
    return not matched_pattern.startswith("!"), detail


def main() -> int:
    """Validate all ignore and negation expectations."""
    root = repository_root()
    failures: list[str] = []
    for path in IGNORED:
        ignored, detail = is_ignored(root, path)
        print(f"IGNORED {path}: {'PASS' if ignored else 'FAIL'} {detail}")
        if not ignored:
            failures.append(f"Expected ignored: {path}")
    for path in TRACKABLE:
        ignored, detail = is_ignored(root, path)
        print(f"TRACKABLE {path}: {'PASS' if not ignored else 'FAIL'} {detail}")
        if ignored:
            failures.append(f"Expected trackable: {path}")
    if failures:
        print("\n".join(failures), file=sys.stderr)
        return 1
    print("Git ignore policy: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
