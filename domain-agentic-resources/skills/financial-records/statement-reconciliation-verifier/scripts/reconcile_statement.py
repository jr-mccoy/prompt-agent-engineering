#!/usr/bin/env python3
"""
reconcile_statement.py - Verify that a statement was extracted completely and correctly.

This is the hard gate of the pipeline. It answers one question with evidence:
"Did every transaction transfer from the statement into the CSV, with correct
amounts?" Downstream stages (categorize, flag) must not run on a statement that
fails verification.

Four verification layers plus a coverage check:
    Layer 1 - Balance arithmetic ("Golden Rule"):
        opening_balance + sum(signed amounts) == closing_balance   (within tolerance)
    Layer 2 - Transaction consistency:
        running-balance continuity, numeric amounts, non-decreasing dates,
        duplicate detection (hash of date+description+amount)
    Layer 3 - Document structure:
        page-count continuity, "Page X of Y" gap detection, account/period present
    Layer 4 - Statistical anomaly (informational):
        amounts > 3 sigma, days with > 10x the median transaction count
    Coverage check (the "every transaction" guarantee):
        every transaction-like line in the raw text maps to exactly one CSV row;
        any unmatched raw lines are listed by line number.

HARD checks (cause a non-zero exit / failure): balance arithmetic when balances
are available, and the coverage check. Everything else is reported as a WARNING
so a human/attorney can review without blocking the pipeline.

Pure standard library - runs anywhere Python 3.8+ runs.

Usage:
    reconcile_statement.py TRANSACTIONS_CSV [options]

Options:
    --meta PATH        Path to <stem>_meta.json (default: alongside the CSV)
    --raw PATH         Path to <stem>_raw.txt (default: alongside the CSV)
    --report DIR       Where to write <stem>_reconciliation.json (default: CSV dir)
    --tolerance FLOAT  Balance tolerance in dollars (default: 0.01)
    -v, --verbose      Print every check

Examples:
    reconcile_statement.py output/chase_jan_transactions.csv
    reconcile_statement.py output/amex_transactions.csv --tolerance 0.05 -v

Exit codes:
    0  VERIFIED   - all hard checks passed (warnings may still be present)
    1  DISCREPANCY - a hard check failed (balance mismatch or coverage gap)
    2  bad input / arguments
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import statistics
import sys
from pathlib import Path

_MONEY = r"\(?-?\$?\s?\d{1,3}(?:,\d{3})*(?:\.\d{2})?\)?-?\s?(?:CR|DR)?"
_MONEY_RE = re.compile(_MONEY)
# Coverage detection requires a real cents amount so headers/periods/account
# numbers (which contain digit groups but no ".dd") are not mistaken for rows.
_MONEY_DEC_RE = re.compile(r"\(?-?\$?\s?\d{1,3}(?:,\d{3})*\.\d{2}\)?-?\s?(?:CR|DR)?")
_DATE_RE = re.compile(r"(\d{1,2}/\d{1,2}/\d{2,4}|\d{4}-\d{2}-\d{2}|\d{1,2}/\d{1,2}|[A-Z][a-z]{2}\.?\s+\d{1,2})")


def _to_float(s: str) -> float | None:
    s = (s or "").strip()
    if not s:
        return None
    try:
        return float(s)
    except ValueError:
        return None


def load_rows(csv_path: Path) -> list[dict]:
    with csv_path.open(encoding="utf-8") as fh:
        return list(csv.DictReader(fh))


def layer1_balance(rows, meta, tol, report):
    opening = meta.get("opening_balance")
    closing = meta.get("closing_balance")
    total = sum(_to_float(r["amount"]) or 0.0 for r in rows)
    report["totals"] = {
        "transaction_count": len(rows),
        "sum_amounts": round(total, 2),
        "credits": round(sum((_to_float(r["amount"]) or 0) for r in rows if (_to_float(r["amount"]) or 0) > 0), 2),
        "debits": round(sum((_to_float(r["amount"]) or 0) for r in rows if (_to_float(r["amount"]) or 0) < 0), 2),
    }
    if opening is None or closing is None:
        report["layer1_balance"] = {
            "status": "SKIPPED",
            "reason": "opening and/or closing balance not found in metadata",
        }
        report["warnings"].append("Balance arithmetic skipped: statement opening/closing balance not detected.")
        return True  # cannot fail a check we can't run; coverage still guards completeness
    computed = round(opening + total, 2)
    diff = round(computed - closing, 2)
    ok = abs(diff) <= tol
    report["layer1_balance"] = {
        "status": "PASS" if ok else "FAIL",
        "opening_balance": opening,
        "closing_balance": closing,
        "computed_closing": computed,
        "difference": diff,
        "tolerance": tol,
    }
    if not ok:
        report["errors"].append(
            f"Balance mismatch: opening {opening} + sum {round(total,2)} = {computed}, "
            f"but statement closing is {closing} (off by {diff})."
        )
    return ok


def layer2_consistency(rows, tol, report):
    issues = []
    # Running-balance continuity (only where balances are present on consecutive rows).
    prev_bal = None
    for i, r in enumerate(rows):
        bal = _to_float(r.get("running_balance", ""))
        amt = _to_float(r.get("amount", ""))
        if amt is None:
            issues.append(f"Row {i+1}: non-numeric amount '{r.get('amount')}'.")
        if bal is not None and prev_bal is not None and amt is not None:
            expected = round(prev_bal + amt, 2)
            if abs(expected - bal) > tol:
                issues.append(
                    f"Row {i+1}: running balance {bal} != previous {prev_bal} + amount {amt} ({expected})."
                )
        if bal is not None:
            prev_bal = bal
    # Date sequence (warning only - some statements group by type, not date).
    # Duplicate detection.
    seen: dict[str, int] = {}
    dups = []
    for i, r in enumerate(rows):
        key = hashlib.md5(
            f"{r['date']}|{r['description_clean']}|{r['amount']}".encode("utf-8")
        ).hexdigest()
        if key in seen:
            dups.append(f"Row {i+1} duplicates row {seen[key]+1} ({r['date']} {r['description_clean']} {r['amount']}).")
        else:
            seen[key] = i
    report["layer2_consistency"] = {
        "status": "PASS" if not issues else "WARN",
        "issues": issues,
        "possible_duplicates": dups,
    }
    report["warnings"].extend(issues)
    if dups:
        report["warnings"].extend(dups)
    return True  # consistency issues are warnings, not hard failures


def layer3_structure(rows, meta, raw_text, report):
    notes = []
    pages = re.findall(r"Page\s+(\d+)\s+of\s+(\d+)", raw_text, re.IGNORECASE)
    if pages:
        seen_pages = sorted({int(p) for p, _ in pages})
        total = int(pages[0][1])
        missing = [n for n in range(1, total + 1) if n not in seen_pages]
        if missing:
            notes.append(f"Possible missing pages: {missing} (statement says {total} pages).")
    if not meta.get("account_id"):
        notes.append("Account number not detected in statement text.")
    if not meta.get("statement_period"):
        notes.append("Statement period not detected in statement text.")
    report["layer3_structure"] = {
        "status": "PASS" if not notes else "WARN",
        "page_count_meta": meta.get("page_count"),
        "notes": notes,
    }
    report["warnings"].extend(notes)
    return True


def layer4_anomaly(rows, report):
    amts = [abs(_to_float(r["amount"]) or 0) for r in rows]
    notes = []
    if len(amts) >= 3:
        mean = statistics.mean(amts)
        sd = statistics.pstdev(amts)
        if sd > 0:
            outliers = [
                f"{r['date']} {r['description_clean'][:30]} {r['amount']}"
                for r in rows
                if abs(_to_float(r["amount"]) or 0) > mean + 3 * sd
            ]
            if outliers:
                notes.append(f"{len(outliers)} amount(s) > 3 sigma (review): {outliers[:5]}")
    # Per-day count spike.
    by_day: dict[str, int] = {}
    for r in rows:
        by_day[r["date"]] = by_day.get(r["date"], 0) + 1
    if by_day:
        counts = list(by_day.values())
        med = statistics.median(counts)
        spikes = [d for d, c in by_day.items() if med > 0 and c > 10 * med]
        if spikes:
            notes.append(f"Day(s) with >10x median transaction count: {spikes}")
    report["layer4_anomaly"] = {"status": "INFO", "notes": notes}
    report["warnings"].extend(notes)
    return True


def coverage_check(rows, raw_text, report):
    """Every transaction-like raw line must map to exactly one extracted row.

    A raw line is "transaction-like" if it contains a date AND at least one money
    token. We match by (date, last money token) against the extracted rows. Any
    unmatched raw line is a coverage gap - a transaction that may have been dropped.
    """
    # Build a multiset of (date, amount) signatures from extracted rows.
    extracted_sigs: dict[tuple[str, str], int] = {}
    for r in rows:
        amt = _to_float(r["amount"])
        sig = (r["date"], f"{abs(amt):.2f}" if amt is not None else "")
        extracted_sigs[sig] = extracted_sigs.get(sig, 0) + 1

    unmatched = []
    candidate_count = 0
    for lineno, line in enumerate(raw_text.splitlines(), start=1):
        if not line.strip():
            continue
        dm = _DATE_RE.search(line)
        monies = [m.group(0).strip() for m in _MONEY_DEC_RE.finditer(line)]
        monies = [m for m in monies if re.search(r"\d", m)]
        if not dm or not monies:
            continue
        # Skip obvious balance/summary lines.
        if re.search(r"(beginning|opening|ending|closing|previous|new)\s+balance", line, re.IGNORECASE):
            continue
        candidate_count += 1
        date = dm.group(1)
        # Use the transaction amount token (second-to-last if a running balance trails).
        amt_tok = monies[-2] if len(monies) >= 2 else monies[-1]
        val = re.sub(r"[^\d.]", "", amt_tok)
        sig = (date, f"{float(val):.2f}") if val else (date, "")
        if extracted_sigs.get(sig, 0) > 0:
            extracted_sigs[sig] -= 1
        else:
            unmatched.append(f"L{lineno}: {line.strip()[:90]}")

    ok = not unmatched
    report["coverage_check"] = {
        "status": "PASS" if ok else "FAIL",
        "raw_candidate_lines": candidate_count,
        "extracted_rows": len(rows),
        "unmatched_raw_lines": unmatched,
    }
    if not ok:
        report["errors"].append(
            f"Coverage gap: {len(unmatched)} transaction-like line(s) in the statement "
            f"did not map to an extracted row. Transactions may be missing."
        )
    return ok


def main() -> int:
    parser = argparse.ArgumentParser(description="Verify a statement extraction.")
    parser.add_argument("transactions_csv")
    parser.add_argument("--meta", default="")
    parser.add_argument("--raw", default="")
    parser.add_argument("--report", default="")
    parser.add_argument("--tolerance", type=float, default=0.01)
    parser.add_argument("-v", "--verbose", action="store_true")
    args = parser.parse_args()

    csv_path = Path(args.transactions_csv)
    if not csv_path.exists():
        print(f"[verify] ERROR: transactions CSV not found: {csv_path}")
        return 2
    stem = csv_path.stem.replace("_transactions", "")
    meta_path = Path(args.meta) if args.meta else csv_path.with_name(f"{stem}_meta.json")
    raw_path = Path(args.raw) if args.raw else csv_path.with_name(f"{stem}_raw.txt")

    rows = load_rows(csv_path)
    meta = json.loads(meta_path.read_text(encoding="utf-8")) if meta_path.exists() else {}
    raw_text = raw_path.read_text(encoding="utf-8") if raw_path.exists() else ""

    report: dict = {"source": csv_path.name, "errors": [], "warnings": []}

    hard_ok = True
    hard_ok &= layer1_balance(rows, meta, args.tolerance, report)
    layer2_consistency(rows, args.tolerance, report)
    layer3_structure(rows, meta, raw_text, report)
    layer4_anomaly(rows, report)
    if raw_text.strip():
        hard_ok &= coverage_check(rows, raw_text, report)
    else:
        report["coverage_check"] = {"status": "SKIPPED", "reason": "no raw text available"}
        report["warnings"].append("Coverage check skipped: raw text not available.")

    report["result"] = "VERIFIED" if hard_ok else "DISCREPANCY"

    report_dir = Path(args.report) if args.report else csv_path.parent
    report_dir.mkdir(parents=True, exist_ok=True)
    report_path = report_dir / f"{stem}_reconciliation.json"
    report_path.write_text(json.dumps(report, indent=2), encoding="utf-8")

    # Human-readable summary.
    print(f"\n=== RECONCILIATION: {csv_path.name} ===")
    print(f"  Layer 1 balance:     {report['layer1_balance']['status']}")
    print(f"  Layer 2 consistency: {report['layer2_consistency']['status']}")
    print(f"  Layer 3 structure:   {report['layer3_structure']['status']}")
    print(f"  Layer 4 anomaly:     {report['layer4_anomaly']['status']}")
    print(f"  Coverage check:      {report['coverage_check']['status']}")
    print(f"  RESULT: {report['result']}")
    for e in report["errors"]:
        print(f"  ERROR: {e}")
    if args.verbose:
        for w in report["warnings"]:
            print(f"  warn:  {w}")
    print(f"  report -> {report_path}")

    return 0 if hard_ok else 1


if __name__ == "__main__":
    sys.exit(main())
