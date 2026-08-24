#!/usr/bin/env python3
"""score_brier.py — Brier scorer + calibration report.

For informational and research purposes only. Not financial, investment, or tax
advice. Nothing here places real-money trades.

STATUS: implemented (Phase 6). Computes the single-prediction Brier component, the
running Brier over a journal directory, a calibration bucket table, and Gate C
progress (see ../references/brier_method.md and ../references/journal_schema.md).

Gate C (from ARCHITECTURE §5) needs >=100 resolved predictions AND a running Brier
<= 0.18 AND a manual switch. This script reports the first two; it NEVER enables
anything and NEVER edits a probability or invents a resolution — only resolved
records (non-null resolution) are scored, over ALL of them, never a favorable subset.

Dependencies: standard library only. If PyYAML is installed it is used to parse
PRED-*.md frontmatter; otherwise a small embedded YAML-subset parser is used (so
manual-only mode stays dependency-free).

Interface (stable; relied on by AGENTS.md and the Stage 7 prompt)
-----------------------------------------------------------------
    score(probability: float, outcome: int) -> float
        outcome 1 (hit) or 0 (miss); returns (probability - outcome) ** 2.

    calibration_report(journal_dir: str) -> dict
        -> {"n": int, "brier": float|None, "buckets": [...],
            "gate_c": {...}, "schema_errors": [...]}

CLI
---
    python score_brier.py --prob 0.62 --outcome 1
    python score_brier.py --calibration-report path/to/knowledge-base/journal/
    python score_brier.py --self-check
"""

from __future__ import annotations

import argparse
import glob
import os
import sys

# Default Gate C thresholds (mirror config/mandate.yaml gate_c). The CLI/report can
# be passed explicit values; these are only the fallback so a quick run needs no YAML.
DEFAULT_MIN_RESOLVED = 100
DEFAULT_MAX_BRIER = 0.18

# Calibration buckets: [low, high) except the last which is closed at 1.0.
_BUCKETS = ((0.0, 0.2), (0.2, 0.4), (0.4, 0.6), (0.6, 0.8), (0.8, 1.0))


def _integrity_verify(journal_dir: str) -> dict:
    """Run the sibling journal_integrity.verify (tamper-evidence + resolution honesty).

    Loaded by path so it works regardless of cwd / sys.path. If the module is missing,
    fail SAFE: report not-clean so Gate C can never be claimed on an unverifiable journal.
    """
    import importlib.util
    here = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(here, "journal_integrity.py")
    try:
        spec = importlib.util.spec_from_file_location("journal_integrity", path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)  # type: ignore[union-attr]
        return mod.verify(journal_dir)
    except (OSError, ImportError, AttributeError) as exc:
        return {"clean": False,
                "issues": [f"integrity check unavailable ({exc}) — Gate C cannot be claimed"],
                "counts": {}}


def score(probability: float, outcome: int) -> float:
    """Brier component for one binary prediction: (probability - outcome) ** 2."""
    if not 0.0 <= probability <= 1.0:
        raise ValueError("probability must be in [0, 1]")
    if outcome not in (0, 1):
        raise ValueError("outcome must be 1 (hit) or 0 (miss)")
    return (probability - outcome) ** 2


# ----------------------------------------------------------------------------
# Minimal YAML-subset loader (stdlib only; PyYAML used if present).
# ----------------------------------------------------------------------------


def _load_yaml(text: str):
    try:
        import yaml  # type: ignore
    except ImportError:
        return _mini_yaml_load(text)
    return yaml.safe_load(text)


def _strip_comment(s: str) -> str:
    out, in_s, in_d, i = [], False, False, 0
    while i < len(s):
        c = s[i]
        if c == "'" and not in_d:
            in_s = not in_s
        elif c == '"' and not in_s:
            in_d = not in_d
        elif c == "#" and not in_s and not in_d and (i == 0 or s[i - 1] in " \t"):
            break
        out.append(c)
        i += 1
    return "".join(out).rstrip()


def _split_kv(s: str):
    idx = s.find(":")
    if idx < 0:
        return s.strip(), False, ""
    return s[:idx].strip().strip("\"'"), True, s[idx + 1:]


def _split_flow(inner: str):
    parts, depth, in_s, in_d, cur = [], 0, False, False, ""
    for c in inner:
        if c == '"' and not in_s:
            in_d = not in_d
            cur += c
        elif c == "'" and not in_d:
            in_s = not in_s
            cur += c
        elif not in_s and not in_d:
            if c in "[{":
                depth += 1
                cur += c
            elif c in "]}":
                depth -= 1
                cur += c
            elif c == "," and depth == 0:
                parts.append(cur)
                cur = ""
            else:
                cur += c
        else:
            cur += c
    if cur.strip() != "":
        parts.append(cur)
    return parts


def _parse_scalar(val: str):
    val = val.strip()
    if val == "":
        return None
    if val[0] == "[":
        inner = val[1:-1].strip()
        return [] if inner == "" else [_parse_scalar(p.strip()) for p in _split_flow(inner)]
    if val[0] == "{":
        inner = val[1:-1].strip()
        if inner == "":
            return {}
        out = {}
        for p in _split_flow(inner):
            k, has, v = _split_kv(p.strip())
            if has:
                out[k] = _parse_scalar(v.strip())
        return out
    if (val[0] == '"' and val[-1] == '"') or (val[0] == "'" and val[-1] == "'"):
        return val[1:-1]
    low = val.lower()
    if low in ("null", "~"):
        return None
    if low in ("true", "yes"):
        return True
    if low in ("false", "no"):
        return False
    try:
        return int(val)
    except ValueError:
        pass
    try:
        return float(val)
    except ValueError:
        return val


def _mini_yaml_load(text: str):
    lines = text.split("\n")
    index = [0]

    def parse_map(min_indent: int):
        result = {}
        while index[0] < len(lines):
            raw = lines[index[0]]
            if raw.strip() == "" or raw.lstrip().startswith("#"):
                index[0] += 1
                continue
            indent = len(raw) - len(raw.lstrip(" "))
            if indent < min_indent:
                break
            key, has, val = _split_kv(_strip_comment(raw).strip())
            index[0] += 1
            if not has:
                continue
            val = val.strip()
            if val in (">", "|", ">-", "|-"):
                block = []
                while index[0] < len(lines):
                    bl = lines[index[0]]
                    if bl.strip() == "":
                        block.append("")
                        index[0] += 1
                        continue
                    if (len(bl) - len(bl.lstrip(" "))) <= indent:
                        break
                    block.append(bl.strip())
                    index[0] += 1
                result[key] = " ".join(b for b in block if b != "")
            elif val == "":
                result[key] = parse_map(indent + 1)
            else:
                result[key] = _parse_scalar(val)
        return result

    return parse_map(0)


def _read_frontmatter(path: str) -> dict:
    with open(path, encoding="utf-8") as fh:
        text = fh.read()
    if not text.lstrip().startswith("---"):
        raise ValueError("no YAML frontmatter")
    body = text.lstrip()[3:]
    end = body.find("\n---")
    if end < 0:
        raise ValueError("unterminated frontmatter")
    data = _load_yaml(body[:end])
    if not isinstance(data, dict):
        raise ValueError("frontmatter is not a mapping")
    return data


# ----------------------------------------------------------------------------
# Calibration report
# ----------------------------------------------------------------------------


def _record_errors(rec: dict, path: str) -> list:
    errs = []
    p = rec.get("probability")
    if not isinstance(p, (int, float)) or not 0.0 <= p <= 1.0:
        errs.append(f"{os.path.basename(path)}: probability {p!r} not in [0,1]")
    res = rec.get("resolution")
    if res not in (None,) and isinstance(res, dict):
        outcome = res.get("outcome")
        if outcome not in ("hit", "miss"):
            errs.append(f"{os.path.basename(path)}: resolution.outcome {outcome!r} not hit/miss")
    return errs


def calibration_report(
    journal_dir: str,
    min_resolved: int = DEFAULT_MIN_RESOLVED,
    max_brier: float = DEFAULT_MAX_BRIER,
) -> dict:
    """Running Brier + calibration buckets + Gate C progress over a journal dir.

    Only records with a non-null ``resolution`` are scored, over ALL of them.
    """
    paths = sorted(glob.glob(os.path.join(journal_dir, "PRED-*.md")))
    schema_errors, resolved = [], []
    for path in paths:
        if os.path.basename(path).upper().startswith("PRED-TEMPLATE"):
            continue
        try:
            rec = _read_frontmatter(path)
        except (OSError, ValueError) as exc:
            schema_errors.append(f"{os.path.basename(path)}: {exc}")
            continue
        schema_errors.extend(_record_errors(rec, path))
        res = rec.get("resolution")
        if not isinstance(res, dict) or res.get("outcome") not in ("hit", "miss"):
            continue  # unresolved or invalid resolution -> not scored
        p = rec.get("probability")
        if not isinstance(p, (int, float)) or not 0.0 <= p <= 1.0:
            continue
        outcome = 1 if res.get("outcome") == "hit" else 0
        resolved.append((rec.get("id", os.path.basename(path)), float(p), outcome))

    n = len(resolved)
    brier = (sum(score(p, o) for _, p, o in resolved) / n) if n else None

    buckets = []
    for lo, hi in _BUCKETS:
        members = [
            (p, o) for _, p, o in resolved
            if (lo <= p < hi) or (hi == 1.0 and p == 1.0)
        ]
        if members:
            mean_p = sum(p for p, _ in members) / len(members)
            hit_rate = sum(o for _, o in members) / len(members)
            gap = hit_rate - mean_p
        else:
            mean_p = hit_rate = gap = None
        buckets.append({
            "range": [lo, hi], "n": len(members),
            "mean_stated_p": mean_p, "realized_hit_rate": hit_rate, "gap": gap,
        })

    # Tamper-evidence + resolution-honesty (F12/F13, SECURITY §4e). A tampered or
    # unverifiable journal can NEVER report unlock_ready, even at count + Brier.
    integrity = _integrity_verify(journal_dir)

    gate_c = {
        "resolved": n,
        "min_resolved": min_resolved,
        "meets_count": n >= min_resolved,
        "brier": brier,
        "max_brier": max_brier,
        "meets_brier": (brier is not None and brier <= max_brier),
        "integrity_clean": bool(integrity.get("clean")),
    }
    gate_c["unlock_ready"] = (
        gate_c["meets_count"] and gate_c["meets_brier"] and gate_c["integrity_clean"]
    )

    return {
        "n": n, "brier": brier, "buckets": buckets,
        "gate_c": gate_c, "schema_errors": schema_errors, "integrity": integrity,
    }


def _print_report(report: dict) -> None:
    n, brier = report["n"], report["brier"]
    print(f"Resolved predictions: {n}")
    print(f"Running Brier: {('%.4f' % brier) if brier is not None else 'n/a (no resolved predictions)'}")
    print("\nCalibration (stated p vs realized hit rate):")
    print("  bucket        n   mean_p   hit_rate   gap")
    for b in report["buckets"]:
        lo, hi = b["range"]
        if b["n"]:
            print(f"  {lo:.1f}-{hi:.1f}   {b['n']:>3}   {b['mean_stated_p']:.3f}    "
                  f"{b['realized_hit_rate']:.3f}    {b['gap']:+.3f}")
        else:
            print(f"  {lo:.1f}-{hi:.1f}     0      -        -        -")
    g = report["gate_c"]
    print(f"\nGate C progress: {g['resolved']}/{g['min_resolved']} resolved "
          f"(count {'OK' if g['meets_count'] else 'not met'}); "
          f"Brier {('%.4f' % g['brier']) if g['brier'] is not None else 'n/a'} vs "
          f"<= {g['max_brier']} ({'OK' if g['meets_brier'] else 'not met'}); "
          f"integrity {'CLEAN' if g.get('integrity_clean') else 'NOT CLEAN'}. "
          f"Unlock-ready: {g['unlock_ready']} (still requires manual live_enabled — Gate C).")
    integ = report.get("integrity", {})
    if integ.get("issues"):
        print("\nJournal integrity issues (tamper-evidence / resolution honesty):")
        for i in integ["issues"]:
            print(f"  - {i}")
    if report["schema_errors"]:
        print("\nSchema warnings:")
        for e in report["schema_errors"]:
            print(f"  - {e}")


# ----------------------------------------------------------------------------
# Self-check — reproduces the brier_method.md worked example + a calibration run.
# ----------------------------------------------------------------------------

_PRED = """---
id: {id}
date_opened: "2026-03-01"
asset: "{asset}"
direction: long
probability: {p}
thesis_ref: "data/output/dossiers/{asset}.md"
patterns_fired: []
horizon: "90 days"
tripwires: ["stop at -15%"]
resolution: {resolution}
brier_component: null
notes: ""
---
## Notes
fixture
"""


def _self_check() -> int:
    import tempfile
    failures = []

    # 1. Single-component scores from the reference doc.
    cases = [(0.62, 1, 0.1444), (0.30, 0, 0.0900), (0.80, 0, 0.6400), (0.5, 1, 0.25)]
    for p, o, expect in cases:
        got = round(score(p, o), 4)
        if got != expect:
            failures.append(f"score({p},{o}) = {got}, expected {expect}")

    # 2. Running Brier over the doc's three resolved predictions = 0.2915.
    with tempfile.TemporaryDirectory() as tmp:
        rows = [
            ("PRED-0042", "EXMP", 0.62, '{ outcome: hit, realized_return: 0.22 }'),
            ("PRED-0043", "FOOB", 0.30, '{ outcome: miss, realized_return: -0.05 }'),
            ("PRED-0044", "BAZQ", 0.80, '{ outcome: miss, realized_return: -0.11 }'),
            ("PRED-0045", "OPEN", 0.55, "null"),  # unresolved -> must be ignored
        ]
        for pid, asset, p, res in rows:
            with open(os.path.join(tmp, f"{pid}.md"), "w", encoding="utf-8") as fh:
                fh.write(_PRED.format(id=pid, asset=asset, p=p, resolution=res))
        rep = calibration_report(tmp, min_resolved=100, max_brier=0.18)
        if rep["n"] != 3:
            failures.append(f"expected 3 resolved (1 unresolved ignored), got {rep['n']}")
        if rep["brier"] is None or round(rep["brier"], 4) != 0.2915:
            failures.append(f"running Brier should be 0.2915, got {rep['brier']}")
        if rep["gate_c"]["meets_count"] or rep["gate_c"]["meets_brier"]:
            failures.append("3 predictions @0.2915 must NOT meet Gate C count or Brier")
        if rep["gate_c"]["unlock_ready"]:
            failures.append("Gate C unlock_ready must be False")
        # Integrity wiring: unstamped fixtures are unverifiable -> not integrity_clean.
        if "integrity" not in rep or rep["gate_c"].get("integrity_clean") is not False:
            failures.append(f"unstamped fixtures must report integrity_clean False, got {rep['gate_c'].get('integrity_clean')}")
        if rep["schema_errors"]:
            failures.append(f"unexpected schema errors: {rep['schema_errors']}")

    if failures:
        print("SELF-CHECK FAILED:", file=sys.stderr)
        for f in failures:
            print(f"  - {f}", file=sys.stderr)
        return 1
    print("SELF-CHECK PASSED (4 component cases + running Brier 0.2915 + Gate C lock)")
    return 0


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description="Brier scorer / calibration report.")
    parser.add_argument("--prob", type=float, help="Stated probability (0-1)")
    parser.add_argument("--outcome", type=int, choices=(0, 1), help="1 = hit, 0 = miss")
    parser.add_argument("--calibration-report", metavar="JOURNAL_DIR",
                        help="Directory of PRED-*.md records to summarize")
    parser.add_argument("--min-resolved", type=int, default=DEFAULT_MIN_RESOLVED,
                        help="Gate C resolved-prediction threshold (default 100)")
    parser.add_argument("--max-brier", type=float, default=DEFAULT_MAX_BRIER,
                        help="Gate C Brier threshold (default 0.18)")
    parser.add_argument("--self-check", action="store_true",
                        help="Run embedded Brier / calibration fixtures and exit")
    args = parser.parse_args(argv)

    if args.self_check:
        return _self_check()

    if args.calibration_report is not None:
        report = calibration_report(args.calibration_report, args.min_resolved, args.max_brier)
        _print_report(report)
        return 0

    if args.prob is not None and args.outcome is not None:
        print(f"{score(args.prob, args.outcome):.4f}")
        return 0

    parser.error("provide --prob and --outcome, or --calibration-report, or --self-check")
    return 2  # unreachable


if __name__ == "__main__":
    raise SystemExit(main())
