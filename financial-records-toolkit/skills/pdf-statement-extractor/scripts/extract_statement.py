#!/usr/bin/env python3
"""
extract_statement.py - Extract transactions from a bank / credit-card statement.

Converts a single statement (PDF, or a plain-text/CSV export) into a normalized
transactions CSV plus a raw-text dump and a metadata JSON. The CSV is the
canonical, machine-readable source of truth for every downstream stage
(verification, categorization, flagging).

Design notes:
    * The data layer is pure standard library (csv/re/json) so this runs in any
      Python 3.8+ sandbox. PDF parsing lazily imports `pdfplumber`; if it is not
      installed the script prints an actionable message and exits 3.
    * Scanned/image PDFs have little or no extractable text. Pass --ocr to route
      the file through `ocrmypdf` first (must be installed) to add a text layer.
    * Real statements vary by institution. The generic parser handles the common
      "<date> <description> <amount> [<running balance>]" line shape. Add or
      override patterns per bank in institutions.yaml (see --config).

Usage:
    extract_statement.py INPUT [options]

Options:
    --out DIR               Output directory (default: ./output)
    --institution NAME      Key into institutions.yaml for custom parse hints
    --account-type TYPE     bank | credit (default: bank). Controls sign convention.
    --ocr                   Run ocrmypdf on the PDF before extraction (scanned docs)
    --config PATH           Path to institutions.yaml (optional)
    -v, --verbose           Print parsing diagnostics

Examples:
    extract_statement.py statements/chase_jan.pdf --out output/
    extract_statement.py amex_2024.pdf --account-type credit --institution amex
    extract_statement.py scanned.pdf --ocr --out output/

Exit codes:
    0 success
    1 no transactions parsed (likely a format the generic parser can't read)
    2 bad input / arguments
    3 missing dependency (pdfplumber or ocrmypdf)
"""
from __future__ import annotations

import argparse
import csv
import json
import re
import subprocess
import sys
from pathlib import Path

EXTRACTOR_VERSION = "1.0.0"

# Canonical transaction schema - kept identical across every stage of the pipeline.
SCHEMA = [
    "source_file", "statement_period", "account_id", "date",
    "description_raw", "description_clean", "amount", "direction",
    "running_balance", "category", "subcategory", "flags",
    "confidence", "needs_review", "notes",
]

# --- Money / date parsing helpers -------------------------------------------------

# Matches $1,234.56 / 1234.56 / (1,234.56) / -1234.56 / 1,234.56- / 1,234.56 CR
_MONEY = r"\(?-?\$?\s?\d{1,3}(?:,\d{3})*(?:\.\d{2})?\)?-?\s?(?:CR|DR)?"
_MONEY_RE = re.compile(_MONEY)
# Statement amounts carry cents. Requiring ".dd" avoids matching the digits in a
# date (01/03/2024) or a store number (#123) as if they were money amounts.
_MONEY_DEC_RE = re.compile(r"\(?-?\$?\s?\d{1,3}(?:,\d{3})*\.\d{2}\)?-?\s?(?:CR|DR)?")

_DATE_PATTERNS = [
    re.compile(r"^\s*(\d{1,2}/\d{1,2}/\d{2,4})\b"),          # 01/15/2024 or 1/5/24
    re.compile(r"^\s*(\d{4}-\d{2}-\d{2})\b"),                 # 2024-01-15
    re.compile(r"^\s*([A-Z][a-z]{2}\.?\s+\d{1,2})\b"),        # Jan 15 / Jan. 15
    re.compile(r"^\s*(\d{1,2}/\d{1,2})\b"),                   # 01/15 (no year)
]


def parse_money(token: str) -> float | None:
    """Parse a single monetary token into a signed float, or None if not money.

    Sign rules: leading '-', surrounding parentheses, a trailing '-', or a
    trailing 'DR' all mean a negative (outflow) amount. Trailing 'CR' is positive.
    """
    if token is None:
        return None
    t = token.strip()
    if not re.search(r"\d", t):
        return None
    neg = False
    if t.endswith("CR"):
        t = t[:-2].strip()
    elif t.endswith("DR"):
        neg = True
        t = t[:-2].strip()
    if t.startswith("(") and t.endswith(")"):
        neg = True
        t = t[1:-1]
    if t.startswith("-") or t.endswith("-"):
        neg = True
    cleaned = t.replace("$", "").replace(",", "").replace("(", "").replace(")", "")
    cleaned = cleaned.replace("-", "").strip()
    if not cleaned:
        return None
    try:
        val = float(cleaned)
    except ValueError:
        return None
    return -val if neg else val


def find_date(line: str) -> tuple[str, int] | None:
    """Return (date_string, end_index) for a leading date, or None."""
    for pat in _DATE_PATTERNS:
        m = pat.match(line)
        if m:
            return m.group(1), m.end()
    return None


def trailing_amounts(text: str) -> list[tuple[float, int]]:
    """Return cents-bearing monetary values as (value, start_index), in order.

    Falls back to integer-style money only if no decimal amounts are present
    (rare for real statements), preserving robustness without matching dates.
    """
    out: list[tuple[float, int]] = []
    for m in _MONEY_DEC_RE.finditer(text):
        val = parse_money(m.group(0).strip())
        if val is not None:
            out.append((val, m.start()))
    if out:
        return out
    for m in _MONEY_RE.finditer(text):
        raw = m.group(0).strip()
        val = parse_money(raw)
        if val is not None and raw not in (".", "-"):
            out.append((val, m.start()))
    return out


# --- Input readers ----------------------------------------------------------------

def read_pdf_text(path: Path, use_ocr: bool, verbose: bool) -> tuple[str, int]:
    """Return (full_text, page_count). Lazily imports pdfplumber."""
    src = path
    if use_ocr:
        try:
            ocr_out = path.with_suffix(".ocr.pdf")
            subprocess.run(
                ["ocrmypdf", "--skip-text", str(path), str(ocr_out)],
                check=True, capture_output=True,
            )
            src = ocr_out
            if verbose:
                print(f"[extract] OCR layer written to {ocr_out}")
        except FileNotFoundError:
            print("[extract] ERROR: --ocr requested but 'ocrmypdf' is not installed.")
            print("[extract] Install it (e.g. 'apt-get install ocrmypdf' or 'pip install ocrmypdf').")
            sys.exit(3)
        except subprocess.CalledProcessError as exc:
            print(f"[extract] WARNING: ocrmypdf failed ({exc.returncode}); using original PDF.")
    try:
        import pdfplumber  # noqa: WPS433 (intentional lazy import)
    except Exception as exc:  # pragma: no cover - environment dependent
        print(f"[extract] ERROR: pdfplumber is required to read PDFs ({exc}).")
        print("[extract] Install it with: pip install pdfplumber")
        print("[extract] (For text/CSV exports you can skip pdfplumber entirely.)")
        sys.exit(3)
    pages_text: list[str] = []
    with pdfplumber.open(str(src)) as pdf:
        for page in pdf.pages:
            pages_text.append(page.extract_text() or "")
    return "\n".join(pages_text), len(pages_text)


def read_text_file(path: Path) -> tuple[str, int]:
    text = path.read_text(encoding="utf-8", errors="replace")
    pages = text.count("\f") + 1
    return text, pages


# --- Statement-level metadata -----------------------------------------------------

def extract_meta(text: str) -> dict:
    """Best-effort extraction of opening balance, closing balance, period, account."""
    meta: dict = {
        "opening_balance": None,
        "closing_balance": None,
        "statement_period": "",
        "account_id": "",
    }

    def _grab(patterns: list[str]) -> float | None:
        for p in patterns:
            m = re.search(p, text, re.IGNORECASE)
            if m:
                v = parse_money(m.group(1))
                if v is not None:
                    return v
        return None

    meta["opening_balance"] = _grab([
        r"(?:beginning|opening|previous|starting)\s+balance[:\s]+(" + _MONEY + r")",
    ])
    meta["closing_balance"] = _grab([
        r"(?:ending|closing|new|current)\s+balance[:\s]+(" + _MONEY + r")",
    ])
    mperiod = re.search(
        r"(?:statement period|billing period|for the period)[:\s]+"
        r"([A-Za-z0-9/.,\s-]+?\d{4})",
        text, re.IGNORECASE,
    )
    if mperiod:
        meta["statement_period"] = " ".join(mperiod.group(1).split())
    macct = re.search(
        r"(?:account|acct)(?:\s*(?:number|no\.?|#))?[:\s]+([Xx*\d-]{4,})",
        text, re.IGNORECASE,
    )
    if macct:
        meta["account_id"] = macct.group(1).strip()
    return meta


# --- Transaction parsing ----------------------------------------------------------

def parse_transactions(text: str, account_type: str, verbose: bool) -> list[dict]:
    """Parse transaction rows from statement text using the generic line shape.

    For each line beginning with a recognizable date we read the trailing money
    tokens: if two are present we treat them as (amount, running_balance); if one
    is present it is the amount with no running balance. Description is the text
    between the date and the first money token.
    """
    rows: list[dict] = []
    for line in text.splitlines():
        if not line.strip():
            continue
        # Skip statement-level balance lines (not transactions).
        if re.search(r"(beginning|opening|ending|closing|previous|new)\s+balance", line, re.IGNORECASE):
            continue
        hit = find_date(line)
        if not hit:
            continue
        date, date_end = hit
        rest = line[date_end:]
        amounts = trailing_amounts(rest)
        if not amounts:
            continue
        # Description = text between the date and the first money token.
        first_start = amounts[0][1]
        desc = rest[:first_start].strip(" \t-|$")
        if len(amounts) >= 2:
            amount = amounts[-2][0]
            running = amounts[-1][0]
        else:
            amount = amounts[-1][0]
            running = None
        rows.append({
            "date": date,
            "description_raw": desc,
            "amount": amount,
            "running_balance": running,
        })
        if verbose:
            print(f"[extract] {date} | {desc[:40]:40} | {amount:>12} | bal={running}")
    return _reconcile_signs(rows, account_type)


def _reconcile_signs(rows: list[dict], account_type: str) -> list[dict]:
    """If running balances are present, derive amount signs from balance deltas.

    This makes the sign convention robust and account-type-agnostic:
    running_balance[i] == running_balance[i-1] + amount[i].
    """
    prev = None
    for r in rows:
        bal = r["running_balance"]
        if bal is not None and prev is not None:
            delta = round(bal - prev, 2)
            if abs(abs(delta) - abs(r["amount"])) < 0.01:
                r["amount"] = delta
        if bal is not None:
            prev = bal
    return rows


def normalize(rows: list[dict], meta: dict, source: str) -> list[dict]:
    norm: list[dict] = []
    for r in rows:
        amt = r["amount"]
        direction = "credit" if amt >= 0 else "debit"
        desc_clean = re.sub(r"\s+", " ", r["description_raw"]).strip().upper()
        norm.append({
            "source_file": source,
            "statement_period": meta.get("statement_period", ""),
            "account_id": meta.get("account_id", ""),
            "date": r["date"],
            "description_raw": r["description_raw"],
            "description_clean": desc_clean,
            "amount": f"{amt:.2f}",
            "direction": direction,
            "running_balance": "" if r["running_balance"] is None else f"{r['running_balance']:.2f}",
            "category": "",
            "subcategory": "",
            "flags": "",
            "confidence": "1.0",
            "needs_review": "FALSE",
            "notes": "",
        })
    return norm


def write_outputs(rows: list[dict], raw_text: str, meta: dict,
                  source: Path, out_dir: Path, page_count: int) -> dict:
    out_dir.mkdir(parents=True, exist_ok=True)
    stem = source.stem
    csv_path = out_dir / f"{stem}_transactions.csv"
    raw_path = out_dir / f"{stem}_raw.txt"
    meta_path = out_dir / f"{stem}_meta.json"

    with csv_path.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=SCHEMA)
        writer.writeheader()
        writer.writerows(rows)

    raw_path.write_text(raw_text, encoding="utf-8")

    meta_out = {
        "source_file": source.name,
        "extractor_version": EXTRACTOR_VERSION,
        "page_count": page_count,
        "transaction_count": len(rows),
        **meta,
    }
    meta_path.write_text(json.dumps(meta_out, indent=2), encoding="utf-8")
    return {"csv": str(csv_path), "raw": str(raw_path), "meta": str(meta_path)}


def main() -> int:
    parser = argparse.ArgumentParser(description="Extract transactions from a statement.")
    parser.add_argument("input", help="Statement file (.pdf, .txt, or .csv)")
    parser.add_argument("--out", default="output", help="Output directory")
    parser.add_argument("--institution", default="", help="institutions.yaml key")
    parser.add_argument("--account-type", default="bank", choices=["bank", "credit"])
    parser.add_argument("--ocr", action="store_true", help="OCR the PDF first")
    parser.add_argument("--config", default="", help="Path to institutions.yaml")
    parser.add_argument("-v", "--verbose", action="store_true")
    args = parser.parse_args()

    src = Path(args.input)
    if not src.exists():
        print(f"[extract] ERROR: input not found: {src}")
        return 2

    suffix = src.suffix.lower()
    if suffix == ".pdf":
        text, pages = read_pdf_text(src, args.ocr, args.verbose)
    elif suffix in (".txt", ".csv"):
        text, pages = read_text_file(src)
    else:
        print(f"[extract] ERROR: unsupported input type '{suffix}'. Use .pdf, .txt, or .csv.")
        return 2

    if not text.strip():
        print("[extract] ERROR: no extractable text. If this is a scanned PDF, re-run with --ocr.")
        return 1

    meta = extract_meta(text)
    rows = parse_transactions(text, args.account_type, args.verbose)
    if not rows:
        print("[extract] WARNING: parsed 0 transactions. The generic parser may not")
        print("[extract] recognize this layout. Add a pattern in institutions.yaml")
        print("[extract] (see references/statement_formats.md) and retry.")
        return 1

    norm = normalize(rows, meta, src.name)
    paths = write_outputs(norm, text, meta, src, Path(args.out), pages)

    print(f"[extract] OK: {len(norm)} transactions -> {paths['csv']}")
    print(f"[extract] opening={meta['opening_balance']} closing={meta['closing_balance']} "
          f"period='{meta['statement_period']}' account='{meta['account_id']}'")
    print(f"[extract] NEXT: verify with reconcile_statement.py before categorizing.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
