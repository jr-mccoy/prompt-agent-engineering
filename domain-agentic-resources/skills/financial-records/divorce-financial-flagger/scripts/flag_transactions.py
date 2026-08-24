#!/usr/bin/env python3
"""
flag_transactions.py - Tag transactions across divorce/custody-relevant dimensions.

This tool ORGANIZES FACTS for review by your attorney. It does not give legal
advice, predict outcomes, or characterize anyone's intent. A flag means
"a reviewer may want to look at this row" - nothing more. Every flag is for your
attorney's judgment.

It reads a categorized transactions CSV and applies rule sets across four
dimensions (configurable in flag_rules.yaml):
    1. asset_property      - transfers, large purchases, asset movements, crypto
    2. income              - payroll, deposits, irregular inflows (income picture)
    3. child_custody       - childcare, school, pediatric/medical, kids' activities
    4. cash_undocumented   - ATM/cash withdrawals, checks to cash, round-dollar cash

It writes the flag codes back into the `flags` column and produces a review
queue (only the flagged rows, sorted by priority) for the attorney.

Pure standard library + PyYAML.

Usage:
    flag_transactions.py TRANSACTIONS_CSV [options]

Options:
    --rules PATH    Flag rules YAML (default: flag_rules.yaml)
    --out PATH      Output CSV (default: overwrite input with flags filled in)
    --queue PATH    Review-queue CSV (default: <stem>_review_queue.csv beside input)
    -v, --verbose

Examples:
    flag_transactions.py output/chase_jan_transactions.csv --rules config/flag_rules.yaml

Exit codes:
    0 success
    2 bad input / arguments
    3 missing dependency (PyYAML)
"""
from __future__ import annotations

import argparse
import csv
import re
import sys
from pathlib import Path

SCHEMA = [
    "source_file", "statement_period", "account_id", "date",
    "description_raw", "description_clean", "amount", "direction",
    "running_balance", "category", "subcategory", "flags",
    "confidence", "needs_review", "notes",
]

DIMENSION_PREFIX = {
    "asset_property": "ASSET",
    "income": "INCOME",
    "child_custody": "CHILD",
    "cash_undocumented": "CASH",
}
PRIORITY_RANK = {"HIGH": 3, "MEDIUM": 2, "LOW": 1, "INFO": 0}


def _load_yaml(path: Path):
    try:
        import yaml
    except Exception:
        print("[flag] ERROR: PyYAML is required. Install with: pip install pyyaml")
        sys.exit(3)
    if not path.exists():
        print(f"[flag] ERROR: flag rules not found: {path}")
        sys.exit(2)
    return yaml.safe_load(path.read_text(encoding="utf-8")) or {}


def _to_float(s):
    try:
        return float((s or "").strip())
    except (ValueError, AttributeError):
        return 0.0


def rule_matches(row: dict, rule: dict) -> bool:
    desc = (row.get("description_clean") or "").upper()
    cat = (row.get("category") or "").upper()
    amt = _to_float(row.get("amount"))
    direction = (row.get("direction") or "").lower()

    want_dir = (rule.get("direction") or "any").lower()
    if want_dir != "any" and want_dir != direction:
        return False
    if "regex" in rule:
        try:
            if not re.search(rule["regex"], desc, re.IGNORECASE):
                return False
        except re.error:
            return False
    if "not_regex" in rule:
        # Exclusion pattern: if it matches, this rule does NOT apply.
        # (e.g. keep a recognized paycheck out of "large NON-payroll deposit".)
        try:
            if re.search(rule["not_regex"], desc, re.IGNORECASE):
                return False
        except re.error:
            pass
    cats = rule.get("match_categories")
    if cats and cat not in [c.upper() for c in cats]:
        return False
    excl = rule.get("exclude_categories")
    if excl and cat in [c.upper() for c in excl]:
        return False
    if "min_amount" in rule and not (amt >= float(rule["min_amount"])):
        return False
    if "max_amount" in rule and not (amt <= float(rule["max_amount"])):
        return False
    if "min_abs_amount" in rule and not (abs(amt) >= float(rule["min_abs_amount"])):
        return False
    if rule.get("round_amount"):
        step = float(rule.get("round_step", 100))
        if abs(amt) < step or round(abs(amt)) % int(step) != 0:
            return False
    return True


def main() -> int:
    parser = argparse.ArgumentParser(description="Flag transactions for divorce/custody review.")
    parser.add_argument("transactions_csv")
    parser.add_argument("--rules", default="flag_rules.yaml")
    parser.add_argument("--out", default="")
    parser.add_argument("--queue", default="")
    parser.add_argument("-v", "--verbose", action="store_true")
    args = parser.parse_args()

    csv_path = Path(args.transactions_csv)
    if not csv_path.exists():
        print(f"[flag] ERROR: input not found: {csv_path}")
        return 2

    rules = _load_yaml(Path(args.rules))
    dimensions = rules.get("dimensions", {})

    with csv_path.open(encoding="utf-8") as fh:
        rows = list(csv.DictReader(fh))

    flagged = []
    total_flags = 0
    for r in rows:
        codes = []
        max_pri = -1
        for dim, dim_rules in dimensions.items():
            prefix = DIMENSION_PREFIX.get(dim, dim.upper())
            for rule in dim_rules or []:
                if rule_matches(r, rule):
                    pri = (rule.get("priority") or "INFO").upper()
                    codes.append(f"{prefix}:{rule['code']}|{pri}")
                    max_pri = max(max_pri, PRIORITY_RANK.get(pri, 0))
        if codes:
            r["flags"] = "; ".join(codes)
            total_flags += len(codes)
            if max_pri >= PRIORITY_RANK["HIGH"]:
                r["needs_review"] = "TRUE"
            flagged.append((max_pri, r))
            if args.verbose:
                print(f"[flag] {r['date']} {r['description_clean'][:32]:32} -> {r['flags']}")

    out_path = Path(args.out) if args.out else csv_path
    with out_path.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=SCHEMA)
        writer.writeheader()
        for r in rows:
            writer.writerow({k: r.get(k, "") for k in SCHEMA})

    queue_path = Path(args.queue) if args.queue else csv_path.with_name(
        csv_path.stem.replace("_transactions", "") + "_review_queue.csv")
    cols = ["priority", "source_file", "date", "description_clean", "amount", "category", "flags", "notes"]
    with queue_path.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.writer(fh)
        writer.writerow(cols)
        pri_name = {v: k for k, v in PRIORITY_RANK.items()}
        for max_pri, r in sorted(flagged, key=lambda x: -x[0]):
            writer.writerow([
                pri_name.get(max_pri, "INFO"), r.get("source_file", ""), r.get("date", ""),
                r.get("description_clean", ""), r.get("amount", ""), r.get("category", ""),
                r.get("flags", ""), r.get("notes", ""),
            ])

    print(f"[flag] OK: {len(flagged)}/{len(rows)} row(s) flagged ({total_flags} flag hits).")
    print(f"[flag] review queue -> {queue_path}")
    print("[flag] REMINDER: flags organize facts for YOUR ATTORNEY's review - not legal conclusions.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
