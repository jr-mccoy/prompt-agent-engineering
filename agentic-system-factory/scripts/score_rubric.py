#!/usr/bin/env python3
"""score_rubric.py — score a design bundle against the 100-point quality rubric.

Part of agentic-system-factory. Stdlib-only; no network, no LLM.
Mirrors authoring/system-patterns/SYSTEM_QUALITY_RUBRIC.md. Parses the
`<!-- RUBRIC ... -->` block in RUBRIC_SCORE.md (see
templates/BUNDLE_MANIFEST_TEMPLATE.md) and enforces the LOAD-BEARING rules:

  * total >= 75 for "production-ready"
  * cat3_security >= 14   (load-bearing minimum)
  * Gate B must pass       (capability AND safety markers present)
Failing any load-bearing rule caps the tier at "Needs work" regardless of total.

Honesty caveat (by design): the per-category scores are SELF-REPORTED by the
curator. This script enforces the caps, the load-bearing minimums, and the
Gate-B cross-check — the truthfulness of the numbers is the orchestrator
critique's and the human reviewer's job. Rubric blocks inside code fences are
ignored (the template's fenced example can never score a bundle).

Usage:
  python3 score_rubric.py <bundle_dir>
  python3 score_rubric.py --self-check

Exit code: 0 = PASS (production-ready or better), 1 = FAIL, 2 = usage error.
"""
import argparse
import os
import re
import sys

CATS = {
    "cat1_justification": 15,
    "cat2_topology": 15,
    "cat3_security": 20,
    "cat4_eval": 20,
    "cat5_durability": 10,
    "cat6_documentation": 10,
    "cat7_crosslink": 10,
}
TOTAL_MAX = sum(CATS.values())  # 100
PASS_THRESHOLD = 75
SECURITY_MIN = 14  # load-bearing minimum on cat3_security


def _read(path):
    try:
        with open(path, encoding="utf-8") as fh:
            return fh.read()
    except OSError:
        return None


def _strip_code(text):
    """Drop fenced code blocks and inline code spans (documentation examples
    must never be parsed as the live rubric block or live gate markers)."""
    text = re.sub(r"(```|~~~).*?\1", "", text, flags=re.S)
    return re.sub(r"`[^`\n]*`", "", text)


def parse_rubric(text):
    """Return (scores dict, errors list)."""
    errors = []
    if text is None:
        return {}, ["RUBRIC_SCORE.md missing"]
    # Take the first RUBRIC comment that actually contains catN_* lines, so an
    # innocuous prose comment mentioning "RUBRIC" can't shadow the real block.
    block = None
    for m in re.finditer(r"<!--\s*RUBRIC\b(.*?)-->", _strip_code(text), re.S):
        if re.search(r"cat\d+_\w+\s*:", m.group(1)):
            block = m.group(1)
            break
    if block is None:
        return {}, ["no <!-- RUBRIC ... --> score block in RUBRIC_SCORE.md "
                    "(it must contain catN_* lines and sit outside any code fence)"]
    scores = {}
    for cat, cap in CATS.items():
        mm = re.search(rf"{cat}\s*:\s*(\d+)", block)
        if not mm:
            errors.append(f"missing {cat}")
            continue
        v = int(mm.group(1))
        if v > cap:
            errors.append(f"{cat}={v} exceeds max {cap}")
        scores[cat] = v
    return scores, errors


def gate_b_passes(bundle):
    """Inline Gate-B check (capability AND safety markers) so scoring is self-contained."""
    text = _read(os.path.join(bundle, "EVAL_HARNESS.md"))
    if text is None:
        return False
    text = _strip_code(text)
    cap = re.search(r"<!--\s*GATE-B-CAPABILITY:\s*present\s*-->", text)
    safe = re.search(r"<!--\s*GATE-B-SAFETY:\s*present\s*-->", text)
    return bool(cap and safe)


def tier(total, security_ok, gate_b_ok):
    if not (security_ok and gate_b_ok):
        return "Needs work (load-bearing gate failed)"
    if total >= 90:
        return "Exemplary"
    if total >= PASS_THRESHOLD:
        return "Production-ready"
    return "Needs work"


def run_one(bundle):
    scores, errors = parse_rubric(_read(os.path.join(bundle, "RUBRIC_SCORE.md")))
    if errors:
        print(f"FAIL  {bundle}: rubric block invalid")
        for e in errors:
            print(f"        - {e}")
        return False
    total = sum(scores.values())
    security_ok = scores["cat3_security"] >= SECURITY_MIN
    gate_b_ok = gate_b_passes(bundle)
    t = tier(total, security_ok, gate_b_ok)
    passed = (total >= PASS_THRESHOLD) and security_ok and gate_b_ok
    print(f"{'PASS' if passed else 'FAIL'}  {bundle}: {total}/{TOTAL_MAX} — {t}")
    if not security_ok:
        print(f"        - cat3_security {scores['cat3_security']} < load-bearing minimum {SECURITY_MIN}")
    if not gate_b_ok:
        print("        - Gate B fails (capability and/or safety marker missing) — caps tier")
    if total < PASS_THRESHOLD:
        print(f"        - total {total} < {PASS_THRESHOLD}")
    return passed


def self_check():
    here = os.path.dirname(os.path.abspath(__file__))
    samples = os.path.join(here, "..", "samples")
    expectations = [
        ("bundle-pass", True), ("bundle-fail", False),
        # Phase-5 validation fixtures (all production-ready or better):
        ("single-agent-triage", True), ("sequential-invoice-pipeline", True),
        ("evaluator-optimizer-copy", True),
        # Anti-gaming negative: a verbatim template copy has only a fenced
        # example rubric block, which must not parse:
        ("templates-verbatim", False),
    ]
    ok = True
    print("score_rubric --self-check:")
    for name, expect in expectations:
        result = run_one(os.path.join(samples, name))
        verdict = "ok" if result == expect else "UNEXPECTED"
        if result != expect:
            ok = False
        print(f"   -> {name}: expected {'PASS' if expect else 'FAIL'}, "
              f"got {'PASS' if result else 'FAIL'} [{verdict}]")
    print("SELF-CHECK", "PASS" if ok else "FAIL")
    return ok


def main(argv=None):
    p = argparse.ArgumentParser(
        prog="score_rubric.py",
        description="Score a design bundle against the 100-point quality rubric.",
        epilog="Exit codes: 0 = PASS (production-ready or better), 1 = FAIL, 2 = usage error.")
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
