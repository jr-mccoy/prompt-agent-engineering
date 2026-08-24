#!/usr/bin/env python3
"""validate_pattern.py — Gate A checker for pattern records.

For informational and research purposes only. Not financial, investment, or tax
advice. Nothing here places real-money trades.

STATUS: implemented (Phase 6). Enforces Gate A in code and validates a
``knowledge-base/patterns/PATTERN-<id>.md`` record against the §6 schema
(see ../references/pattern_schema.md and ../references/validation_discipline.md).

Gate A (from ARCHITECTURE §5): a pattern may hold ``status: validated`` only when

  PASS  status == "validated" AND
        out_of_sample_result.n >= min_sample_size AND
        out_of_sample_result.lift_vs_base_rate > 0 AND
        registered_on is present (pre-registration) AND
        base_rate is present AND
        the record is schema-valid.
  FAIL  otherwise — the unmet conditions are returned, never hidden.

The checker NEVER mutates the record; promotion stays a human/agent decision
informed by this report. ``eligible_for_validated`` reports whether a *hypothesis*
record already clears the out-of-sample bar (i.e. could be promoted), without
asserting that it has been.

Dependencies: standard library only. If PyYAML is installed it is used to parse
the frontmatter; otherwise a small embedded YAML-subset parser handles the
record frontmatter (so manual-only mode stays dependency-free).

Interface (stable; relied on by AGENTS.md and the Stage 3 prompt)
-----------------------------------------------------------------
    validate_pattern(path: str, min_sample_size: int = 30) -> dict
        -> {"status": "PASS"|"FAIL", "reasons": [...],
            "record_status": str|None, "eligible_for_validated": bool}

CLI
---
    python validate_pattern.py PATTERN-0001.md [--min-sample-size N]
    python validate_pattern.py --self-check
    # exit code 0 = PASS, 1 = FAIL, 2 = usage/parse error
"""

from __future__ import annotations

import argparse
import os
import sys

# Fields required by the §6 / pattern_schema.md record schema.
REQUIRED_FIELDS = (
    "id", "title", "status", "asset_classes", "hypothesis", "registered_on",
    "feature_definition", "sample_frame", "base_rate", "in_sample_result",
    "out_of_sample_result", "multiple_comparisons_note", "decay_estimate",
    "capacity_note", "confidence", "last_reviewed", "linked_predictions",
)
VALID_STATUSES = ("hypothesis", "validated", "retired")
VALID_CONFIDENCE = ("low", "medium", "high")


# ----------------------------------------------------------------------------
# Minimal YAML-subset loader (stdlib only; PyYAML used if present).
# Handles exactly what pattern/journal frontmatter and config/*.yaml need:
# block maps, block scalars (>, |), flow seqs [..], flow maps {..}, and scalars.
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
        raise ValueError("no YAML frontmatter (file does not start with '---')")
    body = text.lstrip()[3:]
    end = body.find("\n---")
    if end < 0:
        raise ValueError("unterminated YAML frontmatter (missing closing '---')")
    data = _load_yaml(body[:end])
    if not isinstance(data, dict):
        raise ValueError("frontmatter did not parse to a mapping")
    return data


# ----------------------------------------------------------------------------
# Schema + Gate A logic
# ----------------------------------------------------------------------------


def _schema_errors(rec: dict) -> list:
    errors = []
    for f in REQUIRED_FIELDS:
        if f not in rec:
            errors.append(f"missing required field '{f}'")
    status = rec.get("status")
    if status is not None and status not in VALID_STATUSES:
        errors.append(f"status '{status}' not in {VALID_STATUSES}")
    conf = rec.get("confidence")
    if conf is not None and conf not in VALID_CONFIDENCE:
        errors.append(f"confidence '{conf}' not in {VALID_CONFIDENCE}")
    for f in ("in_sample_result", "out_of_sample_result"):
        v = rec.get(f)
        if v is not None and not isinstance(v, dict):
            errors.append(f"'{f}' must be a map with keys n, lift_vs_base_rate")
        elif isinstance(v, dict):
            for k in ("n", "lift_vs_base_rate"):
                if k not in v:
                    errors.append(f"'{f}' missing key '{k}'")
    for f in ("asset_classes", "linked_predictions"):
        v = rec.get(f)
        if v is not None and not isinstance(v, list):
            errors.append(f"'{f}' must be a list")
    return errors


def _gate_a_unmet(rec: dict, min_sample_size: int) -> list:
    """Return the list of out-of-sample / pre-registration conditions NOT met."""
    unmet = []
    if not rec.get("registered_on"):
        unmet.append("registered_on is empty (no pre-registration)")
    if rec.get("base_rate") in (None, ""):
        unmet.append("base_rate is empty (lift has no anchor)")
    oos = rec.get("out_of_sample_result")
    if not isinstance(oos, dict):
        unmet.append("out_of_sample_result is missing / not a map")
        return unmet
    n = oos.get("n")
    lift = oos.get("lift_vs_base_rate")
    if not isinstance(n, (int, float)) or n < min_sample_size:
        unmet.append(
            f"out_of_sample_result.n ({n!r}) < min_sample_size ({min_sample_size})"
        )
    if not isinstance(lift, (int, float)) or lift <= 0:
        unmet.append(f"out_of_sample_result.lift_vs_base_rate ({lift!r}) not > 0")
    return unmet


# Multiple-comparisons count above which a single-hypothesis OOS bar is suspect
# (leakage_and_skepticism_audit.md §E). Advisory only — never changes PASS/FAIL.
_MANY_COMPARISONS = 20

# Point-in-time / survivorship language we expect a defensible sample_frame to carry
# (leakage_and_skepticism_audit.md §A2 / §D). Absence is a warning, not a failure.
_PIT_MARKERS = (
    "point-in-time", "point in time", "as-of", "as of", "snapshot",
    "delisted", "delist", "survivor", "including names", "point in-time",
)


def _max_int_in(text: str):
    """Largest standalone integer mentioned in a free-text field (None if none)."""
    num, cur = None, ""
    for ch in str(text) + " ":
        if ch.isdigit():
            cur += ch
        else:
            if cur:
                num = int(cur) if num is None else max(num, int(cur))
            cur = ""
    return num


def _advisory_warnings(rec: dict) -> list:
    """Non-blocking leakage/skepticism warnings (audit §A/§D/§E).

    These DO NOT change PASS/FAIL — a PASS still means 'eligible', not 'audited
    clean' (see leakage_and_skepticism_audit.md). They surface the substance checks
    the gate cannot verify, so the operator runs the human audit before promoting.
    """
    warnings = []
    mcn = rec.get("multiple_comparisons_note")
    count = _max_int_in(mcn) if mcn not in (None, "") else None
    if count is not None and count >= _MANY_COMPARISONS:
        warnings.append(
            f"multiple_comparisons_note mentions {count} comparisons — a pattern mined from "
            f"many needs a HIGHER out-of-sample bar than a single pre-registered hypothesis "
            f"(audit §E). Confirm the bar was raised."
        )
    sf = rec.get("sample_frame")
    if isinstance(sf, str) and sf.strip() and not any(m in sf.lower() for m in _PIT_MARKERS):
        warnings.append(
            "sample_frame has no point-in-time / survivorship language (e.g. 'point-in-time', "
            "'as-of', 'including delisted') — verify it is not survivorship-pruned and not a "
            "single live pull (audit §A2/§D)."
        )
    return warnings


def validate_pattern(path: str, min_sample_size: int = 30) -> dict:
    """Gate A check for a pattern record. Returns a report dict; never mutates."""
    try:
        rec = _read_frontmatter(path)
    except (OSError, ValueError) as exc:
        return {
            "status": "FAIL",
            "reasons": [f"could not read record: {exc}"],
            "record_status": None,
            "eligible_for_validated": False,
            "warnings": [],
        }

    reasons = []
    reasons.extend(_schema_errors(rec))

    record_status = rec.get("status")
    unmet = _gate_a_unmet(rec, min_sample_size)
    eligible = len(unmet) == 0

    if record_status != "validated":
        reasons.append(
            f"status is {record_status!r}, not 'validated' "
            "(only 'validated' patterns may drive screening / sizing — Gate A)"
        )
    # A 'validated' record must actually meet the out-of-sample bar.
    reasons.extend(unmet)

    passed = (record_status == "validated") and eligible and (_schema_errors(rec) == [])
    return {
        "status": "PASS" if passed else "FAIL",
        "reasons": [] if passed else reasons,
        "record_status": record_status,
        "eligible_for_validated": eligible,
        "warnings": _advisory_warnings(rec),
    }


# ----------------------------------------------------------------------------
# INDEX / record reconciliation (FAILURE_MODES.md F18 — memory drift).
# A retired/overfit pattern still listed 'validated' in INDEX.md would keep
# scoring in Stage 4. This asserts the index agrees with the records on disk.
# ----------------------------------------------------------------------------


def _index_statuses(index_path: str) -> dict:
    """Parse the INDEX.md markdown table -> {PATTERN-id: status}. Skips the header/legend."""
    import re
    out = {}
    with open(index_path, encoding="utf-8") as fh:
        for line in fh:
            if not line.lstrip().startswith("|"):
                continue
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if not cells:
                continue
            m = re.search(r"PATTERN-\d+", cells[0])
            if not m:
                continue  # header row, separator, or the empty placeholder
            status = cells[2].lower() if len(cells) > 2 else ""
            out[m.group(0)] = status
    return out


def reconcile_index(patterns_dir: str, index_path: str) -> dict:
    """Compare INDEX.md statuses against the PATTERN-*.md records on disk.

    Returns {"status": PASS|FAIL, "mismatches": [...], "missing_from_index": [...],
    "missing_on_disk": [...]}. Run before any Stage 4 screen so a stale index cannot
    let a retired pattern keep scoring.
    """
    import glob as _glob
    index = _index_statuses(index_path)
    disk = {}
    for path in sorted(_glob.glob(os.path.join(patterns_dir, "PATTERN-*.md"))):
        if os.path.basename(path).upper().startswith("PATTERN-TEMPLATE"):
            continue
        try:
            rec = _read_frontmatter(path)
        except (OSError, ValueError):
            continue
        rid = rec.get("id") or os.path.basename(path)
        disk[rid] = str(rec.get("status", "")).lower()

    mismatches, missing_from_index, missing_on_disk = [], [], []
    for rid, dstatus in disk.items():
        if rid not in index:
            missing_from_index.append(rid)
        elif index[rid] != dstatus:
            mismatches.append(f"{rid}: INDEX says '{index[rid]}' but record is '{dstatus}'")
    for rid in index:
        if rid not in disk:
            missing_on_disk.append(rid)

    ok = not (mismatches or missing_from_index or missing_on_disk)
    return {
        "status": "PASS" if ok else "FAIL",
        "mismatches": mismatches,
        "missing_from_index": missing_from_index,
        "missing_on_disk": missing_on_disk,
    }


# ----------------------------------------------------------------------------
# Self-check — proves Gate A in code without external files.
# ----------------------------------------------------------------------------

_FIXTURE_BASE = """---
id: PATTERN-0001
title: "fixture"
status: {status}
asset_classes: [equity-microcap]
hypothesis: "signal predicts outcome"
registered_on: {registered_on}
feature_definition: "precise"
sample_frame: "universe + dates"
base_rate: {base_rate}
in_sample_result: {{ n: 120, lift_vs_base_rate: 0.18 }}
out_of_sample_result: {{ n: {oos_n}, lift_vs_base_rate: {oos_lift} }}
multiple_comparisons_note: "screened 4"
decay_estimate: "12 months"
capacity_note: "survives costs"
confidence: medium
last_reviewed: "2026-06-18"
linked_predictions: []
---

## Notes
fixture
"""


def _write_fixture(tmpdir, name, **kw):
    import os
    defaults = dict(status="validated", registered_on='"2026-01-01"',
                    base_rate='"0.30"', oos_n=40, oos_lift=0.12)
    defaults.update(kw)
    path = os.path.join(tmpdir, name)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(_FIXTURE_BASE.format(**defaults))
    return path


def _self_check() -> int:
    import tempfile
    failures = []
    with tempfile.TemporaryDirectory() as tmp:
        # 1. Properly validated record with OOS n>=30, lift>0 -> PASS.
        ok = validate_pattern(_write_fixture(tmp, "p_ok.md"), 30)
        if ok["status"] != "PASS":
            failures.append(f"validated/OOS-ok should PASS, got {ok}")

        # 2. Hypothesis with no OOS -> FAIL, not eligible (Gate A blocks scoring).
        hyp = validate_pattern(
            _write_fixture(tmp, "p_hyp.md", status="hypothesis", oos_n=0, oos_lift="null"), 30
        )
        if hyp["status"] != "FAIL" or hyp["eligible_for_validated"]:
            failures.append(f"hypothesis/no-OOS should FAIL & be ineligible, got {hyp}")

        # 3. status 'validated' but OOS sample too small -> FAIL (overfit guard).
        small = validate_pattern(
            _write_fixture(tmp, "p_small.md", status="validated", oos_n=12, oos_lift=0.2), 30
        )
        if small["status"] != "FAIL":
            failures.append(f"validated/small-OOS should FAIL, got {small}")

        # 4. Hypothesis that already clears the OOS bar -> eligible_for_validated True.
        ready = validate_pattern(
            _write_fixture(tmp, "p_ready.md", status="hypothesis", oos_n=55, oos_lift=0.15), 30
        )
        if ready["status"] != "FAIL" or not ready["eligible_for_validated"]:
            failures.append(f"hypothesis/strong-OOS should be FAIL but eligible, got {ready}")

        # 5. validated but negative OOS lift -> FAIL.
        neg = validate_pattern(
            _write_fixture(tmp, "p_neg.md", status="validated", oos_n=80, oos_lift=-0.05), 30
        )
        if neg["status"] != "FAIL":
            failures.append(f"validated/negative-lift should FAIL, got {neg}")

        # 6. Advisory warnings (audit §E/§A) are non-blocking: a PASS still PASSes
        # but surfaces the high-comparisons + no-point-in-time-language warnings.
        warn_path = _write_fixture(
            tmp, "p_warn.md", status="validated", oos_n=60, oos_lift=0.2)
        # Rewrite the two free-text fields to trip both advisories.
        with open(warn_path, encoding="utf-8") as fh:
            t = fh.read()
        t = t.replace('multiple_comparisons_note: "screened 4"',
                      'multiple_comparisons_note: "screened 250 features"')
        t = t.replace('sample_frame: "universe + dates"',
                      'sample_frame: "currently listed names only"')
        with open(warn_path, "w", encoding="utf-8") as fh:
            fh.write(t)
        warn = validate_pattern(warn_path, 30)
        if warn["status"] != "PASS":
            failures.append(f"warnings must not change PASS/FAIL, got {warn['status']}")
        if len(warn.get("warnings", [])) != 2:
            failures.append(f"expected 2 advisory warnings, got {warn.get('warnings')}")

        # 7. INDEX/record reconciliation (F18): a status mismatch is caught.
        os.makedirs(os.path.join(tmp, "pat"), exist_ok=True)
        _write_fixture(tmp, "pat/PATTERN-0001.md", status="validated")
        idx = os.path.join(tmp, "INDEX.md")
        with open(idx, "w", encoding="utf-8") as fh:
            fh.write("| id | title | status | confidence |\n|---|---|---|---|\n"
                     "| PATTERN-0001 | t | retired | medium |\n")
        rec = reconcile_index(os.path.join(tmp, "pat"), idx)
        if rec["status"] != "FAIL" or not rec["mismatches"]:
            failures.append(f"reconcile must flag validated-on-disk vs retired-in-index, got {rec}")

    if failures:
        print("SELF-CHECK FAILED:", file=sys.stderr)
        for f in failures:
            print(f"  - {f}", file=sys.stderr)
        return 1
    print("SELF-CHECK PASSED (5/5 Gate A cases + advisory warnings + index reconcile)")
    return 0


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description="Gate A checker for a pattern record.")
    parser.add_argument("path", nargs="?", help="Path to a PATTERN-<id>.md record")
    parser.add_argument("--min-sample-size", type=int, default=30,
                        help="Minimum out-of-sample n required for 'validated' (default 30)")
    parser.add_argument("--reconcile", metavar="PATTERNS_DIR",
                        help="Reconcile INDEX.md statuses against PATTERN-*.md records (F18). "
                             "Use with --index.")
    parser.add_argument("--index", metavar="INDEX.md",
                        help="Path to the pattern INDEX.md (for --reconcile).")
    parser.add_argument("--self-check", action="store_true",
                        help="Run embedded Gate A fixtures and exit")
    args = parser.parse_args(argv)

    if args.self_check:
        return _self_check()

    if args.reconcile:
        if not args.index:
            parser.error("--reconcile requires --index INDEX.md")
        rep = reconcile_index(args.reconcile, args.index)
        print(f"RECONCILE: {rep['status']}")
        for m in rep["mismatches"]:
            print(f"  - mismatch: {m}")
        for r in rep["missing_from_index"]:
            print(f"  - on disk but not in INDEX: {r}")
        for r in rep["missing_on_disk"]:
            print(f"  - in INDEX but no record on disk: {r}")
        return 0 if rep["status"] == "PASS" else 1

    if not args.path:
        parser.error("provide a PATTERN-<id>.md path, --reconcile, or --self-check")

    result = validate_pattern(args.path, args.min_sample_size)
    print(f"RESULT: {result['status']}")
    print(f"  record_status: {result['record_status']}")
    print(f"  eligible_for_validated: {result['eligible_for_validated']}")
    for reason in result.get("reasons", []):
        print(f"  - {reason}")
    for warning in result.get("warnings", []):
        print(f"  ! advisory: {warning}")
    return 0 if result["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
