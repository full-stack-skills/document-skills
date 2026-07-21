#!/usr/bin/env python3
"""Execute artifact regression cases without a shell or live external services."""

from __future__ import annotations

import argparse
import subprocess
import sys
import tempfile
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CASES = ROOT / "evals" / "artifact-cases.yaml"


def substitute(value: str, temp_dir: str) -> str:
    return value.replace("{python}", sys.executable).replace("{temp}", temp_dir)


def run_case(case: dict, temp_dir: str) -> list[str]:
    errors = []
    command = [substitute(str(item), temp_dir) for item in case["command"]]
    result = subprocess.run(command, cwd=ROOT, text=True, capture_output=True, check=False)
    assertions = case.get("assertions", {})
    expected_code = assertions.get("exit_code", 0)
    if result.returncode != expected_code:
        errors.append(f"exit_code expected {expected_code}, got {result.returncode}")
    for expected in assertions.get("stdout_contains", []):
        if expected not in result.stdout:
            errors.append(f"stdout missing {expected!r}")
    for expected in assertions.get("stderr_contains", []):
        if expected not in result.stderr:
            errors.append(f"stderr missing {expected!r}")
    for raw_path in assertions.get("paths_absent", []):
        path = Path(substitute(raw_path, temp_dir))
        if path.exists():
            errors.append(f"path should not exist: {path}")
    if errors:
        errors.append(f"stdout={result.stdout[-1000:]!r}")
        errors.append(f"stderr={result.stderr[-1000:]!r}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--cases", type=Path, default=DEFAULT_CASES)
    args = parser.parse_args()
    data = yaml.safe_load(args.cases.read_text(encoding="utf-8"))
    cases = data.get("cases", [])
    failures = 0
    with tempfile.TemporaryDirectory(prefix="document-skills-evals-") as temp_dir:
        for case in cases:
            errors = run_case(case, temp_dir)
            if errors:
                failures += 1
                print(f"FAIL     {case['id']}")
                for error in errors:
                    print(f"         {error}")
            else:
                print(f"PASS     {case['id']}")
    print(f"SUMMARY  cases={len(cases)} failures={failures}")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
