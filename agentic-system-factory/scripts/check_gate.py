#!/usr/bin/env python3
"""check_gate.py — enforce the factory's hard gates on an emitted design bundle.

Part of agentic-system-factory. Stdlib-only; no network, no LLM.
Gates are enforced as CODE-NOT-TRUST: this script parses the machine-readable
HTML-comment markers defined in templates/BUNDLE_MANIFEST_TEMPLATE.md and
returns PASS/FAIL with the exact unmet conditions. The orchestrator checks the
exit code and refuses to advance on a non-zero exit.

Anti-gaming rules (regression-tested by --self-check):
  * Markers inside fenced code blocks (``` / ~~~) or inline code spans are
    IGNORED — the templates' worked examples can never satisfy a gate; only
    live markers the author emitted count (samples/templates-verbatim is the
    pinned negative fixture for this).
  * Two same-name markers with DIFFERENT values fail the gate closed — a
    stale example can't silently mask the real value.
  * The script verifies marker presence and shape, not truth. A marker with
    no real enforcement point / eval suite behind it is a false pass that the
    orchestrator critique and human review must catch (see the stage prompts'
    False-Positive Prevention blocks).

Gates:
  0  Justification    (ARCHITECTURE.md)      justified w/ honest written reason, or workflow-stop
  A  Security/OWASP-ASI (GATE_DESIGN.md)     SAFE-01/02 enforced + SAFE-04 (enforced | na: <reason>)
                                             + defense-in-depth + kill switch
  B  Evaluation       (EVAL_HARNESS.md)      capability AND safety markers both present
  C  Disclosure       (DISCLOSURE_MANIFEST + RUNBOOK + OBSERVABILITY)  6 dims + rollback + observability

Usage:
  python3 check_gate.py [--gate {0,A,B,C,all}] <bundle_dir>   (default: all)
  python3 check_gate.py --self-check

Exit code: 0 = all requested gates PASS, 1 = a gate FAILED, 2 = usage error.
"""
import argparse
import os
import re
import sys

# Sentinel returned when a file carries two same-name markers with different
# values (e.g. a stale example above the real one). It never equals a valid
# value, so every gate check fails closed with a self-explanatory repr.
CONFLICT = "<<conflicting duplicate markers>>"


def _read(path):
    try:
        with open(path, encoding="utf-8") as fh:
            return fh.read()
    except OSError:
        return None


def _strip_code(text):
    """Drop fenced code blocks and inline code spans before marker search.

    Marker examples quoted inside documentation snippets (the templates ship
    theirs fenced) must never satisfy a gate; only live markers count.
    """
    text = re.sub(r"(```|~~~).*?\1", "", text, flags=re.S)
    return re.sub(r"`[^`\n]*`", "", text)


def _marker(text, name):
    """Return the value of `<!-- NAME: value -->`.

    None if absent; CONFLICT if same-name markers disagree. Repeated markers
    with the SAME value are fine. Values may contain `>` (e.g. na-reasons).
    """
    if text is None:
        return None
    vals = [v.strip() for v in re.findall(
        r"<!--\s*" + re.escape(name) + r":\s*(.*?)\s*-->", _strip_code(text), re.S)]
    if not vals:
        return None
    return vals[0] if len(set(vals)) == 1 else CONFLICT


# ---- individual gates: return (passed: bool, unmet: list[str]) ----

def gate_0(bundle):
    text = _read(os.path.join(bundle, "ARCHITECTURE.md"))
    if text is None:
        return False, ["ARCHITECTURE.md missing"]
    val = _marker(text, "GATE-0")
    unmet = []
    if val not in ("JUSTIFIED", "WORKFLOW-STOP"):
        unmet.append(f"GATE-0 marker must be JUSTIFIED or WORKFLOW-STOP; got {val!r}")
        return False, unmet
    if val == "JUSTIFIED":
        m = re.search(r"<!--\s*JUSTIFICATION-START\s*-->(.*?)<!--\s*JUSTIFICATION-END\s*-->",
                      _strip_code(text), re.S)
        body = (m.group(1).strip() if m else "")
        if not body:
            unmet.append("JUSTIFICATION block is empty or missing "
                         "(it must sit outside any code fence)")
        elif "<…>" in body or "<...>" in body or len(body) < 25:
            unmet.append("JUSTIFICATION block is a placeholder / too short to be honest")
    return (not unmet), unmet


def gate_a(bundle):
    text = _read(os.path.join(bundle, "GATE_DESIGN.md"))
    if text is None:
        return False, ["GATE_DESIGN.md missing"]
    unmet = []
    # SAFE-01 / SAFE-02 are load-bearing: must be exactly "enforced".
    for safe in ("SAFE-01", "SAFE-02"):
        val = _marker(text, safe)
        if val != "enforced":
            unmet.append(f"{safe} must be 'enforced' (load-bearing); got {val!r}")
    # SAFE-04 may be enforced or na:<reason> (a bare/garbled 'na…' is rejected).
    s4 = _marker(text, "SAFE-04")
    if s4 != "enforced" and not (s4 and re.fullmatch(r"na:\s*\S.*", s4, re.S)):
        unmet.append(f"SAFE-04 must be 'enforced' or 'na: <reason>'; got {s4!r}")
    if _marker(text, "DEFENSE-IN-DEPTH") != "3-layers":
        unmet.append("DEFENSE-IN-DEPTH must be '3-layers'")
    if _marker(text, "KILL-SWITCH") != "present":
        unmet.append("KILL-SWITCH must be 'present'")
    return (not unmet), unmet


def gate_b(bundle):
    text = _read(os.path.join(bundle, "EVAL_HARNESS.md"))
    if text is None:
        return False, ["EVAL_HARNESS.md missing"]
    unmet = []
    if _marker(text, "GATE-B-CAPABILITY") != "present":
        unmet.append("GATE-B-CAPABILITY marker missing (ABC-valid capability suite)")
    if _marker(text, "GATE-B-SAFETY") != "present":
        unmet.append("GATE-B-SAFETY marker missing (real-tool safety eval) — capability != safety")
    return (not unmet), unmet


def gate_c(bundle):
    unmet = []
    disc = _read(os.path.join(bundle, "DISCLOSURE_MANIFEST.md"))
    if disc is None:
        unmet.append("DISCLOSURE_MANIFEST.md missing")
    else:
        for i in range(1, 7):
            if _marker(disc, f"DISCLOSURE-DIM-{i}") != "complete":
                unmet.append(f"DISCLOSURE-DIM-{i} not complete")
    runbook = _read(os.path.join(bundle, "RUNBOOK.md"))
    if runbook is None:
        unmet.append("RUNBOOK.md missing")
    elif _marker(runbook, "ROLLBACK") != "present":
        unmet.append("ROLLBACK marker missing in RUNBOOK.md")
    obs = os.path.join(bundle, "OBSERVABILITY.md")
    if not (os.path.isfile(obs) and os.path.getsize(obs) > 0):
        unmet.append("OBSERVABILITY.md missing or empty")
    return (not unmet), unmet


GATES = {"0": gate_0, "A": gate_a, "B": gate_b, "C": gate_c}


def run(bundle, which):
    keys = ["0", "A", "B", "C"] if which in ("all", None) else [which]
    all_ok = True
    for k in keys:
        passed, unmet = GATES[k](bundle)
        if passed:
            print(f"PASS  Gate {k}  {bundle}")
        else:
            all_ok = False
            print(f"FAIL  Gate {k}  {bundle}")
            for u in unmet:
                print(f"        - {u}")
    return all_ok


def self_check():
    here = os.path.dirname(os.path.abspath(__file__))
    samples = os.path.join(here, "..", "samples")
    # bundle -> {gate: expected_pass}
    expectations = {
        "bundle-pass": {"0": True, "A": True, "B": True, "C": True},
        "bundle-fail": {"0": True, "A": True, "B": False, "C": True},
        # Phase-5 validation fixtures (diverse topologies, all PASS):
        "single-agent-triage": {"0": True, "A": True, "B": True, "C": True},
        "sequential-invoice-pipeline": {"0": True, "A": True, "B": True, "C": True},
        "evaluator-optimizer-copy": {"0": True, "A": True, "B": True, "C": True},
        # Gate-0 WORKFLOW-STOP terminal (only Gate 0 applies — deliberately
        # not a full bundle; the pipeline correctly ends at Stage 0 here):
        "workflow-stop": {"0": True},
        # Anti-gaming negative: verbatim, unfilled template copies must fail
        # every gate — their markers are fenced examples, which are ignored:
        "templates-verbatim": {"0": False, "A": False, "B": False, "C": False},
    }
    ok = True
    print("check_gate --self-check (gates must bite exactly as designed):")
    for name, exp in expectations.items():
        bundle = os.path.join(samples, name)
        for k, expect in exp.items():
            passed, _ = GATES[k](bundle)
            verdict = "ok" if passed == expect else "UNEXPECTED"
            if passed != expect:
                ok = False
            print(f"   {name} Gate {k}: expected {'PASS' if expect else 'FAIL'}, "
                  f"got {'PASS' if passed else 'FAIL'} [{verdict}]")
    print("SELF-CHECK", "PASS" if ok else "FAIL")
    return ok


def main(argv=None):
    p = argparse.ArgumentParser(
        prog="check_gate.py",
        description="Enforce the factory's hard gates (0/A/B/C) on an emitted design bundle.",
        epilog="Exit codes: 0 = all requested gates PASS, 1 = a gate FAILED, 2 = usage error.")
    p.add_argument("bundle", nargs="?",
                   help="path to the emitted design-bundle directory")
    p.add_argument("--gate", default="all", choices=["0", "A", "B", "C", "all"],
                   help="which gate to check (default: all)")
    p.add_argument("--self-check", action="store_true",
                   help="run the regression suite against the tracked samples/ fixtures")
    a = p.parse_args(argv)
    if a.self_check:
        return 0 if self_check() else 1
    if not a.bundle:
        p.error("a bundle directory is required (or use --self-check)")
    if not os.path.isdir(a.bundle):
        p.error(f"{a.bundle} is not a directory")
    return 0 if run(a.bundle, a.gate) else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
