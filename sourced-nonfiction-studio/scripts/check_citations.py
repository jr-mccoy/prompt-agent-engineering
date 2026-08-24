#!/usr/bin/env python3
"""
check_citations.py — mechanical Gate-A floor for the Sourced Nonfiction Studio.

This is the CHEAP, LEXICAL pre-check. It verifies citation SHAPE and catches
orphan claims — it does NOT verify that a source actually supports a claim
(that is the orchestrator/claim-verifier's semantic job). Passing this script
is necessary but not sufficient for Gate A.

What it checks in a fact->source matrix (markdown table):
  1. Every KEEP / SOFTEN row carries at least one [S#] source token (no orphans).
  2. No KEEP / SOFTEN row is anchored on an UNVERIFIED / empty source.
  3. Every [S#] token used resolves to a reference with a real locator
     (http(s):// , doi: , 10.xxxx/ DOI, or ISBN) somewhere in the file.

Exit codes: 0 = PASS, 1 = FAIL (issues found), 2 = usage/parse error.

Usage:
  python3 check_citations.py path/to/matrix.md
  python3 check_citations.py --self-check      # run built-in fixtures
Stdlib only; no dependencies.
"""

import re
import sys

TOKEN_RE = re.compile(r"\[S\d+\]")
LOCATOR_RE = re.compile(
    r"(https?://\S+|doi:\s*\S+|\b10\.\d{4,9}/\S+|\bISBN[:\s]*[\d\-Xx]{10,17})",
    re.IGNORECASE,
)
ANCHOR_DISPOSITIONS = {"KEEP", "SOFTEN"}
UNVERIFIED_RE = re.compile(r"UNVERIFIED", re.IGNORECASE)


def _split_row(line):
    # Split a markdown table row into cell strings.
    cells = [c.strip() for c in line.strip().strip("|").split("|")]
    return cells


def _is_separator(cells):
    return all(re.fullmatch(r":?-{2,}:?", c or "-") for c in cells) if cells else False


def find_matrix_rows(text):
    """Return (header_cells, [data_row_cells]) for the first table whose header
    contains a 'Disposition' column and a 'Source' column. Empty if none."""
    lines = text.splitlines()
    for i, line in enumerate(lines):
        if "|" not in line:
            continue
        header = _split_row(line)
        low = [h.lower() for h in header]
        if any("disposition" in h for h in low) and any("source" in h for h in low):
            # next non-empty line should be a separator
            if i + 1 < len(lines) and _is_separator(_split_row(lines[i + 1])):
                rows = []
                for l in lines[i + 2:]:
                    if "|" not in l or not l.strip():
                        break
                    rows.append(_split_row(l))
                return header, rows
    return None, []


def check_text(text):
    """Return (ok: bool, issues: list[str])."""
    issues = []
    header, rows = find_matrix_rows(text)
    if header is None:
        return False, ["No fact->source matrix found (need a table with "
                       "'Disposition' and 'Source' columns)."]

    low = [h.lower() for h in header]
    disp_idx = next(i for i, h in enumerate(low) if "disposition" in h)
    src_idx = next(i for i, h in enumerate(low) if "source" in h)

    all_tokens_used = set()
    keep_rows = 0
    for n, cells in enumerate(rows, 1):
        if len(cells) <= max(disp_idx, src_idx):
            continue  # ragged/short row, skip
        disposition = cells[disp_idx].upper()
        src_cell = cells[src_idx]
        # normalize disposition (may contain extra words)
        disp = next((d for d in ("KEEP", "SOFTEN", "REFRAME", "QUOTE", "CUT")
                     if d in disposition), disposition)
        if disp in ANCHOR_DISPOSITIONS:
            keep_rows += 1
            tokens = TOKEN_RE.findall(src_cell)
            if not tokens:
                issues.append(f"Row {n}: {disp} claim has NO [S#] source token "
                              f"(orphan): {cells[:2]}")
            elif UNVERIFIED_RE.search(src_cell):
                issues.append(f"Row {n}: {disp} claim anchored on UNVERIFIED source: "
                              f"{src_cell}")
            all_tokens_used.update(tokens)

    # Every used token must resolve to a locator somewhere in the doc.
    for tok in sorted(all_tokens_used):
        # find lines mentioning the token that also carry a locator
        resolved = any(
            tok in line and LOCATOR_RE.search(line)
            for line in text.splitlines()
        )
        if not resolved:
            issues.append(f"Source {tok} has no resolvable locator "
                          f"(URL/DOI/ISBN) anywhere in the file.")

    if keep_rows == 0:
        issues.append("No KEEP/SOFTEN (fact) rows found — nothing anchored. "
                      "If the piece is all judgment this may be fine; verify intent.")

    return (len([i for i in issues if not i.startswith("No KEEP/SOFTEN")]) == 0
            and not any("orphan" in i or "UNVERIFIED" in i or "no resolvable" in i
                        for i in issues)), issues


def run_self_check():
    passing = """
## Fact->Source Matrix
| # | Claim | Type | Disposition | Verdict | Source | Reference | Certainty |
|---|-------|------|-------------|---------|--------|-----------|-----------|
| 1 | Avg job search ~5 months | verifiable-fact | KEEP | SUPPORTED | [S1] | BLS, 2024, https://bls.gov/data | established |
| 2 | Referrals fill many roles | verifiable-fact | SOFTEN | PARTIAL | [S2] | Jones 2021, doi:10.1000/abc | some evidence |
| 3 | Prompt thank-yous help | experiential-opinion | REFRAME | UNVERIFIED | — | — | author judgment |
"""
    failing = """
## Fact->Source Matrix
| # | Claim | Type | Disposition | Verdict | Source | Reference | Certainty |
|---|-------|------|-------------|---------|--------|-----------|-----------|
| 1 | Never take a counteroffer | verifiable-fact | KEEP | UNVERIFIED | — | — | high |
| 2 | X causes Y | verifiable-fact | KEEP | SUPPORTED | [S5] | (no locator provided) | established |
"""
    ok1, issues1 = check_text(passing)
    ok2, issues2 = check_text(failing)
    print("[self-check] PASSING fixture ->", "PASS" if ok1 else "FAIL (unexpected)")
    for i in issues1:
        print("   -", i)
    print("[self-check] FAILING fixture ->", "FAIL (expected)" if not ok2 else "PASS (unexpected!)")
    for i in issues2:
        print("   -", i)
    # self-check succeeds only if passing->ok and failing->not ok
    if ok1 and not ok2:
        print("[self-check] OK: gate behaves correctly.")
        return 0
    print("[self-check] BROKEN: gate did not behave as expected.")
    return 1


def main(argv):
    if len(argv) == 2 and argv[1] == "--self-check":
        return run_self_check()
    if len(argv) != 2:
        print(__doc__)
        return 2
    try:
        with open(argv[1], "r", encoding="utf-8") as f:
            text = f.read()
    except OSError as e:
        print(f"error: cannot read {argv[1]}: {e}")
        return 2
    ok, issues = check_text(text)
    if ok:
        print(f"GATE A (citation shape): PASS — {argv[1]}")
        for i in issues:  # non-fatal notes may still print
            print("  note:", i)
        return 0
    print(f"GATE A (citation shape): FAIL — {argv[1]}")
    for i in issues:
        print("  -", i)
    return 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
