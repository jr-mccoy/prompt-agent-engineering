#!/usr/bin/env python3
"""egress_check.py — secret-leak / exfiltration scan for anything the loop writes.

For informational and research purposes only. Not financial, investment, or tax
advice. Nothing here places real-money trades.

STATUS: implemented (hardening pass). Closes the egress gap in SECURITY.md §4d/§6:
agents hold ``Write`` to ``data/output/**`` and ``knowledge-base/**``, so a
prompt-injection could smuggle a held secret (an API key, a raw ``data/input``
dump) into a dossier, alert, order, or ``PRED-*`` note. This is the redaction /
egress pass to run on those files BEFORE writing or committing them — the
write-side counterpart to never putting secrets in prompts.

It is intentionally conservative (favours catching a real key over silence) but
keyed to *assignment context* so it does not fire on every long hash. ``scan``
reports findings; ``redact`` returns the text with matches masked.

Detected: cloud keys (AWS AKIA…), provider tokens (GitHub ghp_…, Slack xox…),
PEM private-key blocks, and ``key|secret|token|password|bearer = <long value>``
assignments. The check is a guard, not a guarantee — it complements, never
replaces, keeping secrets in env vars / git-ignored ``config/*.local.yaml``.

Interface
---------
    scan(path: str) -> dict   # {"clean": bool, "findings": [...], "files_scanned": int}
    redact(text: str) -> str  # same text with secret-shaped substrings masked

CLI
---
    python egress_check.py --scan data/output/        # scan a file or directory
    python egress_check.py --self-check
    # exit 0 = clean, 1 = findings, 2 = usage/parse error
"""

from __future__ import annotations

import argparse
import glob
import os
import re
import sys

# Extensions worth scanning when handed a directory (the loop's text output sinks).
_SCAN_EXTS = (".md", ".json", ".csv", ".txt", ".yaml", ".yml")

# (name, compiled pattern). Ordered; first match per span wins for redaction.
_PATTERNS = [
    ("aws_access_key", re.compile(r"\bAKIA[0-9A-Z]{16}\b")),
    ("github_token", re.compile(r"\bgh[posru]_[A-Za-z0-9]{36,}\b")),
    ("slack_token", re.compile(r"\bxox[baprs]-[A-Za-z0-9-]{10,}\b")),
    ("private_key_block", re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----")),
    ("openai_key", re.compile(r"\bsk-[A-Za-z0-9]{20,}\b")),
    # key/secret/token/password/bearer = <16+ char value> (quoted or bare)
    ("secret_assignment", re.compile(
        r"(?i)\b(?:api[_-]?key|secret(?:[_-]?key)?|access[_-]?token|auth[_-]?token|"
        r"token|password|passwd|bearer)\b\s*[:=]\s*['\"]?([A-Za-z0-9/+=_\-]{16,})['\"]?")),
]

# Values that look secret-shaped but are obviously placeholders -> never flag.
_ALLOW = re.compile(r"(?i)\b(example|placeholder|your[_-]?key|redacted|xx+|todo|"
                    r"none|null|changeme|<[^>]+>)\b")


def _iter_findings(text: str):
    for name, pat in _PATTERNS:
        for m in pat.finditer(text):
            span = m.group(0)
            if _ALLOW.search(span):
                continue
            # For secret_assignment, the captured value is group(1); ignore placeholders.
            if name == "secret_assignment":
                val = m.group(1)
                if _ALLOW.search(val) or val.isdigit():
                    continue
            yield name, m.start(), span


def redact(text: str) -> str:
    """Return text with each secret-shaped substring replaced by a masked marker."""
    spans = sorted(
        ((start, start + len(span)) for _n, start, span in _iter_findings(text)),
        reverse=True,
    )
    out = text
    for start, end in spans:
        out = out[:start] + "[REDACTED-SECRET]" + out[end:]
    return out


def _scan_text(text: str, label: str) -> list:
    findings = []
    line_starts = [0]
    for i, ch in enumerate(text):
        if ch == "\n":
            line_starts.append(i + 1)
    for name, pos, span in _iter_findings(text):
        line_no = sum(1 for s in line_starts if s <= pos)
        preview = (span[:8] + "…") if len(span) > 9 else span
        findings.append({"file": label, "line": line_no, "kind": name, "preview": preview})
    return findings


def scan(path: str) -> dict:
    """Scan a file or directory for secret-shaped strings. Never mutates anything."""
    targets = []
    if os.path.isdir(path):
        for ext in _SCAN_EXTS:
            targets.extend(glob.glob(os.path.join(path, "**", "*" + ext), recursive=True))
    elif os.path.isfile(path):
        targets = [path]
    else:
        return {"clean": False, "findings": [], "files_scanned": 0,
                "error": f"no such file or directory: {path}"}

    findings = []
    for t in sorted(set(targets)):
        try:
            with open(t, encoding="utf-8", errors="replace") as fh:
                findings.extend(_scan_text(fh.read(), os.path.relpath(t, path) if os.path.isdir(path) else t))
        except OSError as exc:
            findings.append({"file": t, "line": 0, "kind": "unreadable", "preview": str(exc)})
    return {"clean": len(findings) == 0, "findings": findings, "files_scanned": len(set(targets))}


def _self_check() -> int:
    import tempfile
    failures = []

    planted = (
        "# dossier\nThesis looks great.\n"
        "aws_key = AKIAIOSFODNN7EXAMPLE\n"            # placeholder-ish but AKIA pattern
        "api_key: 8f4b21c9d7e6a5039b2c1f8e4d6a7b09\n"  # secret assignment
        "token = ghp_ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789\n"
    )
    clean = "# alert\nEXMP earnings on 2026-07-01. Stop at -15%. No secrets here.\n"
    placeholders = 'api_key: "your-key-here"\npassword = changeme\nhash: <REDACTED>\n'

    with tempfile.TemporaryDirectory() as tmp:
        p = os.path.join(tmp, "dossier.md")
        with open(p, "w", encoding="utf-8") as fh:
            fh.write(planted)
        rep = scan(p)
        kinds = {f["kind"] for f in rep["findings"]}
        if rep["clean"]:
            failures.append("planted secrets must be flagged, got clean")
        if "secret_assignment" not in kinds or "github_token" not in kinds:
            failures.append(f"expected secret_assignment + github_token, got {kinds}")

        # redact masks them.
        masked = redact(planted)
        if "ghp_ABCDEFGH" in masked or "8f4b21c9d7e6a5039b2c1f8e4d6a7b09" in masked:
            failures.append("redact must mask the planted secrets")

        c = os.path.join(tmp, "alert.md")
        with open(c, "w", encoding="utf-8") as fh:
            fh.write(clean)
        if not scan(c)["clean"]:
            failures.append(f"clean file must scan clean, got {scan(c)['findings']}")

        ph = os.path.join(tmp, "ph.md")
        with open(ph, "w", encoding="utf-8") as fh:
            fh.write(placeholders)
        if not scan(ph)["clean"]:
            failures.append(f"obvious placeholders must not flag, got {scan(ph)['findings']}")

        # directory scan reaches nested files.
        os.makedirs(os.path.join(tmp, "orders"), exist_ok=True)
        with open(os.path.join(tmp, "orders", "o.md"), "w", encoding="utf-8") as fh:
            fh.write(planted)
        if scan(tmp)["clean"]:
            failures.append("directory scan must find the nested planted secret")

    if failures:
        print("SELF-CHECK FAILED:", file=sys.stderr)
        for f in failures:
            print(f"  - {f}", file=sys.stderr)
        return 1
    print("SELF-CHECK PASSED (planted flagged / redacted / clean clean / placeholders ignored / nested found)")
    return 0


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(
        description="Secret-leak / exfiltration scan for the loop's output files.")
    parser.add_argument("--scan", metavar="PATH", help="File or directory to scan.")
    parser.add_argument("--self-check", action="store_true",
                        help="Run embedded egress fixtures and exit.")
    args = parser.parse_args(argv)

    if args.self_check:
        return _self_check()
    if not args.scan:
        parser.error("provide --scan PATH or --self-check")

    rep = scan(args.scan)
    if rep.get("error"):
        print(f"ERROR: {rep['error']}", file=sys.stderr)
        return 2
    print(f"Scanned {rep['files_scanned']} file(s).")
    for f in rep["findings"]:
        print(f"  - {f['file']}:{f['line']}  {f['kind']}  ({f['preview']})")
    print(f"EGRESS: {'CLEAN' if rep['clean'] else 'SECRET-SHAPED CONTENT FOUND — redact before writing/committing'}")
    return 0 if rep["clean"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
