#!/usr/bin/env python3
"""claim_guard.py — refuse to ship an audit report that overclaims.

Part of ai-governance-audit-kit. Stdlib-only; no network, no LLM.

Gate B — CLAIM-SAFE. This is the ADR-0040 enforcement point, and it is the gate
that protects the person selling the engagement. ADR-0040 is Accepted and
implemented, and its consequence is stated flatly: *"Nothing in this repository
currently supports any public performance claim, and the tooling says so."* An
audit report is the single most likely place for that to be quietly forgotten,
because a client is paying for a conclusion.

**What the gate blocks, and why each rule is the one ADR-0040 actually states.**

1. ``forbidden_sentence`` — the claims the ADR forbids by name.
2. ``unlicensed_direction`` — the ADR's own rule: *"There is no code path that
   writes 'improved' without a number requiring it."* A directional word in the
   same sentence as a quantity, with no interval licensing that quantity, is
   blocked. A directional word with **no** number is not blocked: "this gate
   reduces the chance of an unbacked claim" carries nothing to mislead with,
   and a gate that blocks ordinary prose gets switched off, which protects
   nobody.
3. ``roi_or_money_claim`` — a payback or ROI figure is a performance claim
   wearing a finance costume.
4. ``undisclosed_tier`` — ``pae_registry/governance.py`` refuses to assert a
   quality tier because *"inferring one from document structure would be
   fabricating a rubric score"*. A report may say a score was observed or
   self-reported; it may not say an artifact *is* Tier N.
5. ``fixture_figure_unstamped`` — every fixture-derived figure carries
   ``SYNTHETIC TEST FIXTURE — NOT INDEPENDENT BENCHMARK EVIDENCE``, so sample
   output cannot be mistaken for a result by a reader who was not there.
6. ``missing_limitations`` — limitations are **generated, not remembered**. A
   report with quantities and no limitations section does not pass.

**Fenced examples never trip the gate.** Prose detectors run on text with
fenced blocks and inline code spans removed, the same anti-gaming rule as
``agentic-system-factory/scripts/check_gate.py`` — otherwise this kit's own
reference page, which quotes every forbidden sentence, could not exist.

Usage:
  python3 claim_guard.py <report.md> [--config PATH] [--json]
  python3 claim_guard.py --self-check

Exit code: 0 = Gate B PASS, 1 = Gate B BLOCKED, 2 = usage error.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
KIT_ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
DEFAULT_CONFIG = os.path.join(KIT_ROOT, "config", "audit.json")

SYNTHETIC_STAMP = "SYNTHETIC TEST FIXTURE — NOT INDEPENDENT BENCHMARK EVIDENCE"

#: Forbidden by name in ADR-0040. Matched on normalized text so casing and
#: whitespace cannot smuggle one through.
FORBIDDEN = (
    "pae makes ai 20% smarter",
    "pae has 90% accuracy",
    "proven to improve every model",
)

_DIRECTIONAL = re.compile(
    r"\b(?:improve[sd]?|improvement|better|best|worse|faster|slower|cheaper|"
    r"reduce[sd]?|reduction|increase[sd]?|decrease[sd]?|boost(?:s|ed)?|"
    r"outperform(?:s|ed)?|beats?|gain(?:s|ed)?|uplift|smarter|more accurate|"
    r"less accurate|speed-?up)\b",
    re.I,
)
_QUANTITY = re.compile(r"(?<![\w.])\d+(?:[.,]\d+)?\s*(?:%|percent|pp|x\b|×)|(?<![\w.])\d{2,}")
_INTERVAL = re.compile(r"95%\s*CI|confidence interval|\bCI\s*[:\[]|±", re.I)
_MONEY = re.compile(
    r"\bROI\b|\breturn on investment\b|\bpayback\b|\bpays for itself\b"
    r"|\bsaves?\s*[$£€]|\b[$£€]\s?\d",
    re.I,
)
_TIER = re.compile(r"\bis\s+(?:a\s+)?tier\s*\d\b|\btier\s*\d\s+(?:prompt|skill|artifact)\b", re.I)
_DISCLOSED = re.compile(r"self-reported|observed|not asserted|candidate|disclosed", re.I)
_SENTENCE = re.compile(r"[^.!?\n]*[.!?]|[^.!?\n]+")
_LIMITATIONS = re.compile(r"^#{1,6}\s*Limitations\b", re.M | re.I)
_BULLET = re.compile(r"^\s*[-*]\s+\S", re.M)


def _read(path):
    try:
        with open(path, encoding="utf-8") as fh:
            return fh.read()
    except OSError:
        return None


def _strip_code(text):
    """Drop fenced blocks and inline code spans.

    A quoted counter-example must never block a report, and a forbidden
    sentence shown inside a fence as "do not write this" is documentation.
    """
    text = re.sub(r"(```|~~~).*?\1", "", text, flags=re.S)
    return re.sub(r"`[^`\n]*`", "", text)


def _normalize(text):
    return re.sub(r"\s+", " ", text).strip().lower()


def _sentences(prose):
    for match in _SENTENCE.finditer(prose):
        sentence = match.group(0).strip()
        if sentence:
            yield match.start(), sentence


def _line_of(text, offset):
    return text[:offset].count("\n") + 1


# ---------------------------------------------------------------- detectors


def scan(path, cfg):
    """Return the findings list for one report. Every entry names a location."""
    raw = _read(path)
    rel = os.path.relpath(path, KIT_ROOT)
    if raw is None:
        return [{
            "rule": "report_readable",
            "path": rel,
            "line": 0,
            "detail": "report could not be read",
        }]

    claim_cfg = cfg.get("claim_safety") or {}
    prose = _strip_code(raw)
    findings = []

    normalized = _normalize(prose)
    for phrase in FORBIDDEN:
        if phrase in normalized:
            findings.append({
                "rule": "forbidden_sentence",
                "path": rel,
                "line": 0,
                "detail": f"ADR-0040 forbids this claim by name: {phrase!r}",
            })

    for offset, sentence in _sentences(prose):
        line = _line_of(prose, offset)
        directional = _DIRECTIONAL.search(sentence)
        quantity = _QUANTITY.search(sentence)
        if directional and quantity and not _INTERVAL.search(sentence):
            findings.append({
                "rule": "unlicensed_direction",
                "path": rel,
                "line": line,
                "detail": (
                    f"{directional.group(0)!r} sits beside the quantity "
                    f"{quantity.group(0)!r} with no interval licensing it: "
                    f"{sentence.strip()[:160]}"
                ),
            })
        money = _MONEY.search(sentence)
        if money:
            findings.append({
                "rule": "roi_or_money_claim",
                "path": rel,
                "line": line,
                "detail": (
                    f"{money.group(0)!r} is a performance claim in financial "
                    f"clothing: {sentence.strip()[:160]}"
                ),
            })
        tier = _TIER.search(sentence)
        if tier and not _DISCLOSED.search(sentence):
            findings.append({
                "rule": "undisclosed_tier",
                "path": rel,
                "line": line,
                "detail": (
                    f"{tier.group(0)!r} asserts a quality tier as a fact: "
                    f"{sentence.strip()[:160]}"
                ),
            })

    markers = claim_cfg.get("fixture_path_markers") or []
    cites_fixture = any(marker in raw for marker in markers)
    has_quantity = bool(_QUANTITY.search(prose))
    if cites_fixture and has_quantity and SYNTHETIC_STAMP not in raw:
        findings.append({
            "rule": "fixture_figure_unstamped",
            "path": rel,
            "line": 0,
            "detail": (
                "the report quotes figures against a fixture corpus without the "
                f"stamp {SYNTHETIC_STAMP!r}; sample output must not be readable "
                "as a result"
            ),
        })

    minimum = int(claim_cfg.get("min_limitations", 3))
    heading = _LIMITATIONS.search(prose)
    if not heading:
        if has_quantity:
            findings.append({
                "rule": "missing_limitations",
                "path": rel,
                "line": 0,
                "detail": (
                    "the report carries quantities and no Limitations section; "
                    "ADR-0040 requires limitations to be generated, not remembered"
                ),
            })
    else:
        tail = prose[heading.end():]
        next_heading = re.search(r"^#{1,6}\s+\S", tail, re.M)
        section = tail[: next_heading.start()] if next_heading else tail
        bullets = len(_BULLET.findall(section))
        if bullets < minimum:
            findings.append({
                "rule": "missing_limitations",
                "path": rel,
                "line": _line_of(prose, heading.start()),
                "detail": (
                    f"Limitations section lists {bullets} item(s); the engagement "
                    f"config requires at least {minimum}"
                ),
            })

    findings.sort(key=lambda f: (f["line"], f["rule"]))
    return findings


def gate_b(path, cfg):
    """Return ``(passed, findings)``. Any finding blocks: there is no advisory tier."""
    findings = scan(path, cfg)
    return (not findings), findings


# ---------------------------------------------------------------- cli


def run_one(path, cfg, as_json=False):
    passed, findings = gate_b(path, cfg)
    if as_json:
        print(json.dumps({
            "report": os.path.relpath(path, KIT_ROOT),
            "gate_b": {"passed": passed, "findings": findings},
        }, indent=2, sort_keys=True))
        return passed
    print(f"{'PASS' if passed else 'BLOCK'}  Gate B (claim-safe) — "
          f"{os.path.relpath(path, KIT_ROOT)}")
    for finding in findings:
        where = f":{finding['line']}" if finding["line"] else ""
        print(f"        - [{finding['rule']}]{where} {finding['detail']}")
    return passed


def self_check():
    print("claim_guard --self-check:")
    with open(DEFAULT_CONFIG, encoding="utf-8") as fh:
        cfg = json.load(fh)
    reports = os.path.join(KIT_ROOT, "samples", "reports")
    expectations = (
        ("report_clean.md", True),
        ("report_unlicensed_claim.md", False),
        ("report_tier_asserted.md", False),
        ("report_missing_stamp.md", False),
        ("report_no_limitations.md", False),
        ("report_roi_claim.md", False),
        ("report_forbidden_sentence.md", False),
        # Anti-gaming: the same forbidden sentences, but fenced as the
        # counter-examples they are. Documentation must remain writable.
        ("report_fenced_counterexamples.md", True),
    )
    ok = True
    for name, expect in expectations:
        result = run_one(os.path.join(reports, name), cfg)
        if result != expect:
            ok = False
        print(f"   -> {name}: expected {'PASS' if expect else 'BLOCK'}, "
              f"got {'PASS' if result else 'BLOCK'} "
              f"[{'ok' if result == expect else 'UNEXPECTED'}]")
    print("SELF-CHECK", "PASS" if ok else "FAIL")
    return ok


def main(argv=None):
    parser = argparse.ArgumentParser(
        prog="claim_guard.py",
        description="Refuse to ship an audit report that overclaims (ADR-0040).",
        epilog="Exit codes: 0 = Gate B PASS, 1 = Gate B BLOCKED, 2 = usage error.")
    parser.add_argument("report", nargs="?", help="the report markdown file to check")
    parser.add_argument("--config", help=f"audit config (default: {DEFAULT_CONFIG})")
    parser.add_argument("--json", action="store_true", help="emit the result as JSON")
    parser.add_argument("--self-check", action="store_true",
                        help="run the regression suite against the tracked samples/ fixtures")
    args = parser.parse_args(argv)

    if args.self_check:
        return 0 if self_check() else 1
    if not args.report:
        parser.error("a report file is required (or use --self-check)")
    if not os.path.isfile(args.report):
        parser.error(f"{args.report} is not a file")
    with open(args.config or DEFAULT_CONFIG, encoding="utf-8") as fh:
        cfg = json.load(fh)
    return 0 if run_one(args.report, cfg, as_json=args.json) else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
