"""Console entry points for repository validation."""

from __future__ import annotations

import json
import sys
from collections.abc import Sequence
from pathlib import Path

from .checks import run_checks
from .environment import print_environment_report, run_environment_checks


def check_environment_main(argv: Sequence[str] | None = None) -> int:
    """Run environment validation and return its documented exit code."""
    args = list(argv if argv is not None else sys.argv[1:])

    if args:
        print("Usage: raman-check-environment", file=sys.stderr)
        return 2

    code, payload = run_environment_checks()
    print_environment_report(payload)
    return code


def run_checks_main(argv: Sequence[str] | None = None) -> int:
    """Run the canonical aggregate validator."""
    args = list(argv if argv is not None else sys.argv[1:])
    output_path: Path | None = None
    if args:
        if len(args) != 2 or args[0] != "--output":
            print("Usage: raman-checks [--output PATH]", file=sys.stderr)
            return 2
        output_path = Path(args[1])
    code, payload = run_checks(output_path=output_path)
    print(json.dumps({"overall_status": payload["overall_status"]}, sort_keys=True))
    return code
