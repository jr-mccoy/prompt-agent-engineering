#!/usr/bin/env python3
"""screen_rank.py — Stage 4 screener that enforces Gate A at ranking time, in code.

For informational and research purposes only. Not financial, investment, or tax advice.
Nothing here places real-money trades.

STATUS: implemented (Phase 7, stdlib only). ``validate_pattern.py`` enforces Gate A for ONE
record; this script enforces it where it actually bites — when patterns are combined into a
ranked watchlist. It takes a map of candidate -> fired pattern ids, runs each fired pattern
through ``validate_pattern`` (the same Gate A checker), and:

  * counts a pattern toward a candidate's score ONLY if it is ``status: validated`` AND clears
    Gate A (PASS), weighted by its recorded ``confidence`` (low=1, medium=2, high=3);
  * shows every ``hypothesis`` / ``retired`` / ineligible firing as an UNSCORED "paper-only
    signal" that can never move the rank — the single most important rule of Stage 4.

It hardens Gate A *in code, not by trust*: a hypothesis pattern is structurally incapable of
contributing to a score here. It never fabricates a firing — the firings come from the caller
(the Stage 4 prompt's pattern-matching against dossiers); a firing whose pattern record is
missing is reported, not assumed favorable.

Interface (stable; relied on by the Stage 4 prompt + tests)
-----------------------------------------------------------
    screen_rank(firings: dict, patterns_dir: str, min_sample_size: int = 30) -> dict
        firings = {"SYMBOL": {"PATTERN-0001": "evidence note", ...}, ...}
        -> {"ranked": [...], "min_sample_size": int}

CLI
---
    python skills/pattern-knowledge-base/scripts/screen_rank.py \
        --firings firings.json --patterns-dir knowledge-base/patterns [--out data/output/watchlist.csv]
    python skills/pattern-knowledge-base/scripts/screen_rank.py --self-check
"""

from __future__ import annotations

import argparse
import csv
import json
import os
import sys

# validate_pattern.py is a sibling module; make it importable both as a CLI (run by path) and
# when this file is loaded by path from tests.
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from validate_pattern import (  # noqa: E402  (intentional: after sys.path shim)
    _read_frontmatter,
    validate_pattern,
)

CONFIDENCE_WEIGHT = {"low": 1, "medium": 2, "high": 3}


def _pattern_path(patterns_dir, pattern_id):
    """Resolve <patterns_dir>/<id>.md (the conventional record filename)."""
    return os.path.join(patterns_dir, f"{pattern_id}.md")


def screen_rank(firings, patterns_dir, min_sample_size: int = 30) -> dict:
    """Score + rank candidates on VALIDATED patterns only (Gate A). Never mutates records."""
    ranked = []
    for symbol in sorted(firings):
        fired = firings[symbol] or {}
        scored, paper_only, cannot_score = [], [], []
        score = 0
        for pattern_id in sorted(fired):
            evidence = fired[pattern_id]
            path = _pattern_path(patterns_dir, pattern_id)
            if not os.path.exists(path):
                cannot_score.append({"pattern": pattern_id,
                                     "reason": f"record not found at {path}"})
                continue
            result = validate_pattern(path, min_sample_size)
            try:
                conf = (_read_frontmatter(path).get("confidence") or "low")
            except (OSError, ValueError):
                conf = "low"
            if result["status"] == "PASS" and result["record_status"] == "validated":
                weight = CONFIDENCE_WEIGHT.get(conf, 1)
                score += weight
                scored.append({"pattern": pattern_id, "confidence": conf,
                               "weight": weight, "evidence": evidence})
            else:
                paper_only.append({
                    "pattern": pattern_id,
                    "record_status": result["record_status"],
                    "reason": "Gate A: not validated"
                              if result["record_status"] != "validated"
                              else "Gate A: validated record fails OOS bar",
                })
        ranked.append({
            "symbol": symbol,
            "score": score,
            "scored_patterns": scored,
            "paper_only_signals": paper_only,
            "cannot_score": cannot_score,
        })
    # Rank by score desc, then symbol for determinism.
    ranked.sort(key=lambda r: (-r["score"], r["symbol"]))
    for i, row in enumerate(ranked, 1):
        row["rank"] = i
    return {"ranked": ranked, "min_sample_size": min_sample_size}


def write_watchlist(result, out_path) -> None:
    """Write the ranked watchlist to CSV (the Stage 4 artifact)."""
    os.makedirs(os.path.dirname(out_path) or ".", exist_ok=True)
    columns = ["rank", "symbol", "score", "validated_patterns_fired",
               "evidence_trail", "paper_only_signals"]
    with open(out_path, "w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=columns)
        writer.writeheader()
        for row in result["ranked"]:
            writer.writerow({
                "rank": row["rank"],
                "symbol": row["symbol"],
                "score": row["score"],
                "validated_patterns_fired": "; ".join(
                    f"{p['pattern']}({p['confidence']})" for p in row["scored_patterns"]),
                "evidence_trail": " | ".join(
                    f"{p['pattern']}: {p['evidence']}" for p in row["scored_patterns"]),
                "paper_only_signals": "; ".join(
                    f"{p['pattern']}[{p['record_status']}]" for p in row["paper_only_signals"]),
            })


def _self_check() -> int:
    """Prove Gate A at rank time: a hypothesis pattern can never contribute to a score."""
    import tempfile

    validated = """---
id: PV
title: "validated fixture"
status: validated
asset_classes: [equity]
hypothesis: "h"
registered_on: "2025-09-01"
feature_definition: "precise"
sample_frame: "frame"
base_rate: "0.34"
in_sample_result: { n: 210, lift_vs_base_rate: 0.19 }
out_of_sample_result: { n: 42, lift_vs_base_rate: 0.11 }
multiple_comparisons_note: "3"
decay_estimate: "24m"
capacity_note: "ok"
confidence: medium
last_reviewed: "2026-06-18"
linked_predictions: []
---
notes
"""
    hypothesis = validated.replace("id: PV", "id: PH").replace(
        "status: validated", "status: hypothesis").replace(
        "out_of_sample_result: { n: 42, lift_vs_base_rate: 0.11 }",
        "out_of_sample_result: { n: 0, lift_vs_base_rate: null }")

    failures = []
    with tempfile.TemporaryDirectory() as tmp:
        with open(os.path.join(tmp, "PV.md"), "w", encoding="utf-8") as fh:
            fh.write(validated)
        with open(os.path.join(tmp, "PH.md"), "w", encoding="utf-8") as fh:
            fh.write(hypothesis)
        firings = {
            "SCOR": {"PV": "margins §1", "PH": "insider §2"},  # fires one validated + one hypothesis
            "SIG": {"PH": "insider §2"},                        # fires ONLY a hypothesis
        }
        result = screen_rank(firings, tmp, 30)
        by_sym = {r["symbol"]: r for r in result["ranked"]}

        scor = by_sym["SCOR"]
        if scor["score"] != 2:  # medium-confidence validated => weight 2; hypothesis adds nothing
            failures.append(f"SCOR should score 2 on the validated pattern only, got {scor['score']}")
        if [p["pattern"] for p in scor["scored_patterns"]] != ["PV"]:
            failures.append(f"only PV should score for SCOR, got {scor['scored_patterns']}")
        if [p["pattern"] for p in scor["paper_only_signals"]] != ["PH"]:
            failures.append(f"PH must be an unscored paper-only signal, got {scor['paper_only_signals']}")

        sig = by_sym["SIG"]
        if sig["score"] != 0:
            failures.append(f"SIG fires only a hypothesis — score must be 0, got {sig['score']}")

        if scor["rank"] >= sig["rank"]:
            failures.append("a hypothesis-only candidate must not outrank a validated-scored one")

        # missing record is reported, not assumed favorable
        miss = screen_rank({"X": {"PNONE": "n/a"}}, tmp, 30)["ranked"][0]
        if miss["score"] != 0 or not miss["cannot_score"]:
            failures.append(f"missing pattern record must be reported, not scored, got {miss}")

    if failures:
        print("SELF-CHECK FAILED:", file=sys.stderr)
        for f in failures:
            print(f"  - {f}", file=sys.stderr)
        return 1
    print("SELF-CHECK PASSED (validated-only scoring / hypothesis unscored / missing reported)")
    return 0


def _main(argv=None) -> int:
    parser = argparse.ArgumentParser(
        description="Stage 4 screener — Gate A enforced at ranking time (Phase 7).",
    )
    parser.add_argument("--self-check", action="store_true",
                        help="Run embedded Gate-A-at-rank fixtures and exit.")
    parser.add_argument("--firings", help="JSON file: {symbol: {pattern_id: evidence_note}}.")
    parser.add_argument("--patterns-dir", dest="patterns_dir",
                        default="knowledge-base/patterns",
                        help="Directory of PATTERN-*.md records (default knowledge-base/patterns).")
    parser.add_argument("--min-sample-size", dest="min_sample_size", type=int, default=30,
                        help="Gate A out-of-sample minimum (default 30).")
    parser.add_argument("--out", help="Optional watchlist.csv path; prints JSON if omitted.")
    args = parser.parse_args(argv)

    if args.self_check:
        return _self_check()
    if not args.firings:
        parser.error("--firings <file.json> is required (or use --self-check)")

    with open(args.firings, encoding="utf-8") as fh:
        firings = json.load(fh)
    result = screen_rank(firings, args.patterns_dir, args.min_sample_size)

    if args.out:
        write_watchlist(result, args.out)
        result["watchlist_csv"] = args.out
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(_main())
