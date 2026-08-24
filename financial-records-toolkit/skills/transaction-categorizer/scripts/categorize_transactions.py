#!/usr/bin/env python3
"""
categorize_transactions.py - Assign a spending category to each transaction.

Uses the Plaid personal-finance taxonomy (16 primary categories / detailed
subcategories) via a layered, deterministic matcher, then routes anything it
cannot recognize into a research queue so a human or the transaction-research
agent can identify the merchant and teach the rules file.

Matching layers (first hit wins, highest confidence first):
    1. MCC code     - if an MCC is present in the description, look it up
    2. Merchant whitelist - exact / substring match on a known payee
    3. Regex rules  - bank-descriptor patterns (e.g. "CHEVRON|SHELL|EXXON")
    4. Fuzzy match  - close match to a known merchant (rapidfuzz if available,
                      else difflib); accepted only above a similarity threshold
    -> otherwise category = UNKNOWN, needs_review = TRUE, added to the queue.

The rules live in a YAML file (see assets/category_rules.example.yaml) so the
system learns over time: research a merchant once, append it to the rules with
--merge, and every future statement categorizes it automatically.

Pure standard library + PyYAML. rapidfuzz is used if installed (better fuzzy
matching) but is optional.

Usage:
    categorize_transactions.py TRANSACTIONS_CSV [options]
    categorize_transactions.py --merge RESEARCHED.yaml --rules RULES.yaml

Options:
    --rules PATH    Category rules YAML (default: category_rules.yaml beside script's assets)
    --out PATH      Output CSV (default: overwrite input with categories filled in)
    --queue PATH    Where to write the unknown-merchant research queue
                    (default: <stem>_research_queue.csv beside the input)
    --threshold F   Fuzzy similarity threshold 0-1 (default: 0.86)
    --merge FILE    Append researched merchants (YAML list) into the rules file and exit
    -v, --verbose

Examples:
    categorize_transactions.py output/chase_jan_transactions.csv --rules config/category_rules.yaml
    categorize_transactions.py --merge research/found.yaml --rules config/category_rules.yaml

Exit codes:
    0 success
    2 bad input / arguments
    3 missing dependency (PyYAML)
"""
from __future__ import annotations

import argparse
import csv
import difflib
import re
import sys
from pathlib import Path

SCHEMA = [
    "source_file", "statement_period", "account_id", "date",
    "description_raw", "description_clean", "amount", "direction",
    "running_balance", "category", "subcategory", "flags",
    "confidence", "needs_review", "notes",
]


def _load_yaml(path: Path):
    try:
        import yaml
    except Exception:
        print("[categorize] ERROR: PyYAML is required. Install with: pip install pyyaml")
        sys.exit(3)
    if not path.exists():
        return {}
    return yaml.safe_load(path.read_text(encoding="utf-8")) or {}


def _dump_yaml(obj, path: Path):
    import yaml
    path.write_text(yaml.safe_dump(obj, sort_keys=False, allow_unicode=True), encoding="utf-8")


def _fuzzy_ratio(a: str, b: str) -> float:
    try:
        from rapidfuzz import fuzz
        return fuzz.token_set_ratio(a, b) / 100.0
    except Exception:
        return difflib.SequenceMatcher(None, a, b).ratio()


def categorize_one(desc: str, rules: dict, threshold: float):
    """Return (category, subcategory, confidence, method) for a description."""
    d = (desc or "").upper()

    # Layer 1: MCC code embedded in the descriptor.
    mcc_map = rules.get("mcc_mappings", {}) or {}
    mcc_hit = re.search(r"\bMCC[:\s]?(\d{4})\b", d)
    if mcc_hit and mcc_hit.group(1) in mcc_map:
        e = mcc_map[mcc_hit.group(1)]
        return e.get("category", "UNKNOWN"), e.get("subcategory", ""), 0.97, "mcc"

    # Layer 2: merchant whitelist (exact, then substring).
    wl = rules.get("merchant_whitelist", {}) or {}
    for name, e in wl.items():
        if name.upper() == d:
            return e.get("category", "UNKNOWN"), e.get("subcategory", ""), 1.0, "whitelist-exact"
    for name, e in wl.items():
        if name.upper() in d:
            return e.get("category", "UNKNOWN"), e.get("subcategory", ""), 0.95, "whitelist-substr"

    # Layer 3: regex descriptor patterns.
    for rule in rules.get("regex_patterns", []) or []:
        try:
            if re.search(rule["pattern"], d, re.IGNORECASE):
                return rule.get("category", "UNKNOWN"), rule.get("subcategory", ""), 0.93, "regex"
        except re.error:
            continue

    # Layer 4: fuzzy match against known merchant names.
    best_name, best_score = None, 0.0
    for name in wl:
        score = _fuzzy_ratio(d, name.upper())
        if score > best_score:
            best_name, best_score = name, score
    if best_name and best_score >= threshold:
        e = wl[best_name]
        return e.get("category", "UNKNOWN"), e.get("subcategory", ""), round(0.75 + 0.2 * best_score, 2), "fuzzy"

    return "UNKNOWN", "", 0.0, "none"


def do_merge(researched_path: Path, rules_path: Path) -> int:
    """Append researched merchant entries into the rules file's whitelist."""
    researched = _load_yaml(researched_path)
    if not isinstance(researched, list):
        print("[categorize] ERROR: --merge file must be a YAML list of {match, category, subcategory, note}.")
        return 2
    rules = _load_yaml(rules_path)
    wl = rules.setdefault("merchant_whitelist", {})
    added = 0
    for item in researched:
        key = (item.get("match") or "").strip()
        if not key:
            continue
        wl[key] = {
            "category": item.get("category", "UNKNOWN"),
            "subcategory": item.get("subcategory", ""),
            "note": item.get("note", "researched"),
        }
        added += 1
    _dump_yaml(rules, rules_path)
    print(f"[categorize] merged {added} researched merchant(s) into {rules_path}")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Categorize transactions (Plaid taxonomy).")
    parser.add_argument("transactions_csv", nargs="?", default="")
    parser.add_argument("--rules", default="category_rules.yaml")
    parser.add_argument("--out", default="")
    parser.add_argument("--queue", default="")
    parser.add_argument("--threshold", type=float, default=0.86)
    parser.add_argument("--merge", default="")
    parser.add_argument("-v", "--verbose", action="store_true")
    args = parser.parse_args()

    rules_path = Path(args.rules)

    if args.merge:
        return do_merge(Path(args.merge), rules_path)

    if not args.transactions_csv:
        print("[categorize] ERROR: provide a transactions CSV (or use --merge).")
        return 2
    csv_path = Path(args.transactions_csv)
    if not csv_path.exists():
        print(f"[categorize] ERROR: input not found: {csv_path}")
        return 2

    rules = _load_yaml(rules_path)
    if not rules:
        print(f"[categorize] WARNING: rules file empty/missing at {rules_path}; everything will be UNKNOWN.")

    with csv_path.open(encoding="utf-8") as fh:
        rows = list(csv.DictReader(fh))

    unknown_counts: dict[str, int] = {}
    n_known = 0
    for r in rows:
        cat, sub, conf, method = categorize_one(r.get("description_clean", ""), rules, args.threshold)
        r["category"] = cat
        r["subcategory"] = sub
        # Preserve a lower extraction confidence if it was already set below this.
        try:
            prior = float(r.get("confidence") or 1.0)
        except ValueError:
            prior = 1.0
        r["confidence"] = f"{min(prior, conf) if cat != 'UNKNOWN' else conf:.2f}"
        if cat == "UNKNOWN":
            r["needs_review"] = "TRUE"
            key = r.get("description_clean", "").strip()
            unknown_counts[key] = unknown_counts.get(key, 0) + 1
        else:
            n_known += 1
            if conf < 0.75:
                r["needs_review"] = "TRUE"
        if args.verbose:
            print(f"[categorize] {r['date']} {r['description_clean'][:32]:32} -> {cat}/{sub} ({method}, {conf})")

    out_path = Path(args.out) if args.out else csv_path
    with out_path.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=SCHEMA)
        writer.writeheader()
        for r in rows:
            writer.writerow({k: r.get(k, "") for k in SCHEMA})

    queue_path = Path(args.queue) if args.queue else csv_path.with_name(
        csv_path.stem.replace("_transactions", "") + "_research_queue.csv")
    if unknown_counts:
        with queue_path.open("w", newline="", encoding="utf-8") as fh:
            writer = csv.writer(fh)
            writer.writerow(["description_clean", "occurrences", "proposed_category", "proposed_subcategory", "source"])
            for desc, n in sorted(unknown_counts.items(), key=lambda kv: -kv[1]):
                writer.writerow([desc, n, "", "", ""])
        print(f"[categorize] {len(unknown_counts)} unknown merchant(s) -> research queue: {queue_path}")

    print(f"[categorize] OK: {n_known}/{len(rows)} categorized; {len(unknown_counts)} unique unknown(s).")
    if unknown_counts:
        print("[categorize] NEXT: research the queue, save findings as YAML, then run with --merge and re-run.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
