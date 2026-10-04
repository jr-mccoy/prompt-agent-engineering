#!/usr/bin/env python3
"""
Validate and summarise playtest telemetry logs written as JSON Lines.

Each line is one event object. Required envelope fields:
    schema_version, build_id, session_id, participant_code, t_ms, event

Checks per file:
    - every line parses as JSON and has the envelope fields
    - one session_id, one build_id and one participant_code per file
    - t_ms (milliseconds on the session clock) never decreases
    - session_start is the first event; session_end is present (warns if missing,
      which usually means a crash or force-quit)
    - event names are in the allowed list, if --events is given
    - no field name looks like personal data (name, email, phone, ip)

Writes a per-session summary to stdout and, with --csv, a section summary CSV
(deaths, time spent and quits per section) for the synthesis step.

Usage:
    validate_playtest_log.py <log.jsonl> [<log.jsonl> ...] [--events events.txt] [--csv out.csv]

Examples:
    validate_playtest_log.py sessions/*.jsonl
    validate_playtest_log.py sessions/*.jsonl --events allowed_events.txt --csv summary.csv

Exit codes:
    0  all files valid (warnings allowed)
    1  one or more files have errors
    2  usage error (no files, unreadable allowed-events file)

Standard library only.
"""

from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

ENVELOPE = ("schema_version", "build_id", "session_id", "participant_code", "t_ms", "event")
PII_TOKENS = {"name", "email", "phone", "ip", "address", "dob", "birthdate", "birthday"}
# Leading characters a spreadsheet may evaluate as a formula (CSV/formula injection).
FORMULA_PREFIXES = ("=", "+", "-", "@", "\t", "\r")


def spreadsheet_safe(value):
    """Neutralise a string cell that a spreadsheet would evaluate as a formula.

    Log fields such as participant_code or section come from the build, so a
    value like ``=HYPERLINK(...)`` must not execute when a researcher opens the
    summary CSV. Numbers are left untouched.
    """
    if isinstance(value, str) and value.startswith(FORMULA_PREFIXES):
        return "'" + value
    return value


def validate_file(path: Path, allowed: set[str] | None) -> tuple[list[str], list[str], dict]:
    """Validate one session log. Returns (errors, warnings, summary)."""
    errors: list[str] = []
    warnings: list[str] = []
    events: list[dict] = []

    try:
        lines = path.read_text(encoding="utf-8").splitlines()
    except OSError as exc:
        return [f"cannot read file: {exc}"], [], {}

    for lineno, raw in enumerate(lines, start=1):
        if not raw.strip():
            continue
        try:
            obj = json.loads(raw)
        except json.JSONDecodeError as exc:
            # A truncated final line is expected after a crash; anything else is an error.
            if lineno == len(lines):
                warnings.append(f"line {lineno}: truncated final line ignored ({exc.msg})")
            else:
                errors.append(f"line {lineno}: invalid JSON ({exc.msg})")
            continue
        if not isinstance(obj, dict):
            errors.append(f"line {lineno}: not a JSON object")
            continue
        missing = [k for k in ENVELOPE if k not in obj]
        if missing:
            errors.append(f"line {lineno}: missing envelope fields {missing}")
            continue
        for key in obj.get("payload", {}) if isinstance(obj.get("payload"), dict) else {}:
            if PII_TOKENS & set(re.split(r"[_\-\s.]+", key.lower())):
                warnings.append(f"line {lineno}: payload field '{key}' may be personal data")
        if allowed is not None and obj["event"] not in allowed:
            errors.append(f"line {lineno}: unknown event '{obj['event']}'")
        obj["_line"] = lineno
        events.append(obj)

    if not events:
        errors.append("no valid events")
        return errors, warnings, {}

    for field in ("session_id", "build_id", "participant_code", "schema_version"):
        values = {e[field] for e in events}
        if len(values) > 1:
            errors.append(f"multiple {field} values in one file: {sorted(map(str, values))}")

    prev = None
    for e in events:
        if not isinstance(e["t_ms"], (int, float)):
            errors.append(f"line {e['_line']}: t_ms is not a number")
            continue
        if prev is not None and e["t_ms"] < prev:
            errors.append(f"line {e['_line']}: t_ms went backwards ({prev} -> {e['t_ms']})")
        prev = e["t_ms"]

    if events[0]["event"] != "session_start":
        errors.append("first event is not session_start")
    if not any(e["event"] == "session_end" for e in events):
        warnings.append("no session_end (crash or force-quit?)")

    summary = summarise(events)
    return errors, warnings, summary


def summarise(events: list[dict]) -> dict:
    """Per-section time, deaths and quits, plus event counts and bookmarks."""
    counts: dict[str, int] = defaultdict(int)
    sections: dict[str, dict[str, float]] = defaultdict(lambda: {"time_ms": 0.0, "deaths": 0, "quits": 0})
    bookmarks = []
    current, entered_at = None, None

    for e in events:
        counts[e["event"]] += 1
        payload = e.get("payload") if isinstance(e.get("payload"), dict) else {}
        section = e.get("section") or payload.get("section")
        if e["event"] == "section_enter" and section:
            if current is not None and entered_at is not None:
                sections[current]["time_ms"] += e["t_ms"] - entered_at
            current, entered_at = section, e["t_ms"]
        elif e["event"] in ("section_exit", "session_end", "quit") and current is not None:
            sections[current]["time_ms"] += e["t_ms"] - entered_at
            if e["event"] == "quit":
                sections[current]["quits"] += 1
            if e["event"] == "section_exit":
                current, entered_at = None, None
            else:
                entered_at = e["t_ms"]
        if e["event"] == "death":
            sections[section or current or "unknown"]["deaths"] += 1
        if e["event"] == "observer_bookmark":
            bookmarks.append((e["t_ms"], payload.get("tag", "")))

    first = events[0]
    return {
        "session_id": first["session_id"],
        "participant_code": first["participant_code"],
        "build_id": first["build_id"],
        "duration_min": round((events[-1]["t_ms"] - first["t_ms"]) / 60000, 1),
        "counts": dict(counts),
        "sections": {k: dict(v) for k, v in sections.items()},
        "bookmarks": bookmarks,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate playtest JSONL telemetry logs")
    parser.add_argument("logs", nargs="+", help="Session log files (.jsonl)")
    parser.add_argument("--events", help="File with one allowed event name per line")
    parser.add_argument("--csv", help="Write per-section summary CSV to this path")
    args = parser.parse_args()

    allowed = None
    if args.events:
        try:
            allowed = {ln.strip() for ln in Path(args.events).read_text(encoding="utf-8").splitlines() if ln.strip()}
        except OSError as exc:
            print(f"error: cannot read --events file: {exc}", file=sys.stderr)
            return 2

    any_errors = False
    rows = []
    for name in args.logs:
        path = Path(name)
        errors, warnings, summary = validate_file(path, allowed)
        status = "FAIL" if errors else "OK"
        print(f"[{status}] {path}")
        for msg in errors:
            print(f"    error:   {msg}")
        for msg in warnings:
            print(f"    warning: {msg}")
        if summary:
            print(f"    participant={summary['participant_code']} build={summary['build_id']} "
                  f"duration={summary['duration_min']} min events={sum(summary['counts'].values())} "
                  f"bookmarks={len(summary['bookmarks'])}")
            for section, s in summary["sections"].items():
                rows.append([summary["participant_code"], summary["session_id"], summary["build_id"],
                             section, round(s["time_ms"] / 1000, 1), s["deaths"], s["quits"]])
        any_errors = any_errors or bool(errors)

    if args.csv:
        with open(args.csv, "w", newline="", encoding="utf-8") as fh:
            writer = csv.writer(fh)
            writer.writerow(["participant_code", "session_id", "build_id", "section", "time_s", "deaths", "quits"])
            writer.writerows([spreadsheet_safe(cell) for cell in row] for row in rows)
        print(f"wrote {args.csv} ({len(rows)} rows)")

    return 1 if any_errors else 0


if __name__ == "__main__":
    sys.exit(main())
