#!/usr/bin/env python3
"""validate_bundle.py — are all required design-bundle artifacts present and non-empty?

Part of agentic-system-factory. Stdlib-only; no network, no LLM.
The bundle is the framework-agnostic terminal artifact the factory emits
(Stage 6). This script checks structure only; gate markers are checked by
check_gate.py and rubric scoring by score_rubric.py.

Usage:
  python3 validate_bundle.py <bundle_dir>
  python3 validate_bundle.py --self-check     # runs against the tracked fixtures in ../samples/

Exit code: 0 = PASS, 1 = FAIL (missing/empty artifacts), 2 = usage error.
"""
import argparse
import os
import sys

# Required single files at the bundle root.
REQUIRED_FILES = [
    "BUNDLE_MANIFEST.md",
    "ARCHITECTURE.md",
    "GATE_DESIGN.md",
    "EVAL_HARNESS.md",
    "DISCLOSURE_MANIFEST.md",
    "OBSERVABILITY.md",
    "RUNBOOK.md",
    "RUBRIC_SCORE.md",
]
# Required directories that must contain >= 1 non-empty .md file.
REQUIRED_DIRS = ["agents", "tools"]


def _nonempty(path):
    try:
        return os.path.getsize(path) > 0
    except OSError:
        return False


def validate(bundle):
    missing = []
    for f in REQUIRED_FILES:
        p = os.path.join(bundle, f)
        if not os.path.isfile(p):
            missing.append(f"{f} (missing)")
        elif not _nonempty(p):
            missing.append(f"{f} (empty)")
    for d in REQUIRED_DIRS:
        dp = os.path.join(bundle, d)
        if not os.path.isdir(dp):
            missing.append(f"{d}/ (missing dir)")
            continue
        mds = [m for m in os.listdir(dp) if m.endswith(".md") and _nonempty(os.path.join(dp, m))]
        if not mds:
            missing.append(f"{d}/ (no non-empty .md spec)")
    return missing


def run_one(bundle):
    if not os.path.isdir(bundle):
        print(f"FAIL  {bundle}: not a directory")
        return False
    missing = validate(bundle)
    if missing:
        print(f"FAIL  {bundle}")
        for m in missing:
            print(f"        - {m}")
        return False
    print(f"PASS  {bundle}: all required artifacts present and non-empty")
    return True


def self_check():
    here = os.path.dirname(os.path.abspath(__file__))
    samples = os.path.join(here, "..", "samples")
    # (bundle, expected_pass) — bundle-fail is structurally complete on
    # purpose (it fails Gate B, not this structural check); the last two are
    # deliberately partial fixtures for check_gate/score_rubric negatives.
    expectations = [
        ("bundle-pass", True), ("bundle-fail", True),
        # Phase-5 validation fixtures (all structurally complete):
        ("single-agent-triage", True), ("sequential-invoice-pipeline", True),
        ("evaluator-optimizer-copy", True),
        # Intentionally-partial fixtures (not full bundles):
        ("workflow-stop", False), ("templates-verbatim", False),
    ]
    ok = True
    print("validate_bundle --self-check (every fixture must validate exactly as expected):")
    for name, expect in expectations:
        result = run_one(os.path.join(samples, name))
        verdict = "ok" if result == expect else "UNEXPECTED"
        if result != expect:
            ok = False
        print(f"   -> {name}: expected {'PASS' if expect else 'FAIL'}, got {'PASS' if result else 'FAIL'} [{verdict}]")
    print("SELF-CHECK", "PASS" if ok else "FAIL")
    return ok


def main(argv=None):
    p = argparse.ArgumentParser(
        prog="validate_bundle.py",
        description="Check that all required design-bundle artifacts are present and non-empty.",
        epilog="Exit codes: 0 = PASS, 1 = FAIL (missing/empty artifacts), 2 = usage error.")
    p.add_argument("bundle", nargs="?",
                   help="path to the emitted design-bundle directory")
    p.add_argument("--self-check", action="store_true",
                   help="run the regression suite against the tracked samples/ fixtures")
    a = p.parse_args(argv)
    if a.self_check:
        return 0 if self_check() else 1
    if not a.bundle:
        p.error("a bundle directory is required (or use --self-check)")
    if not os.path.isdir(a.bundle):
        p.error(f"{a.bundle} is not a directory")
    return 0 if run_one(a.bundle) else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
