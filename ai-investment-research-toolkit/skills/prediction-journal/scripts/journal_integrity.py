#!/usr/bin/env python3
"""journal_integrity.py — tamper-evidence + resolution-honesty for the prediction journal.

For informational and research purposes only. Not financial, investment, or tax
advice. Nothing here places real-money trades.

STATUS: implemented (hardening pass). Closes the highest-severity code-uncovered
failures in FAILURE_MODES.md (F12 journal/calibration tampering, F13 invented
resolution) and SECURITY.md §4e (forged calibration to fake the Gate C track
record). ``score_brier.py`` computes Brier honestly over whatever is present but
cannot, by itself, detect a ``probability`` edited after the outcome is known or a
resolution invented with no provenance. This module makes those tamper-evident.

The mechanism (no external deps, no network, git-independent):

  * **Lock hash.** At the moment a prediction is OPENED, ``stamp`` writes a
    ``lock_hash`` over the immutable fields (id, date_opened, asset, direction,
    probability, horizon). Editing any of those later — most importantly
    ``probability`` after the outcome is known — makes the stored hash no longer
    match, which ``verify`` reports as TAMPER.
  * **Resolution honesty.** ``verify`` requires every *resolved* record to carry a
    numeric ``realized_return`` and a ``resolved_on`` date that is at or after the
    prediction's horizon end (no resolving before the horizon elapses, no
    outcome with no provenance).
  * **Integrity-clean gate.** ``verify`` returns ``clean`` = no tampered records,
    no dishonest resolutions, and every *resolved* record verifiable (carries a
    matching lock_hash). ``score_brier.py`` folds this into Gate C so a tampered
    or unverifiable journal can never report ``unlock_ready``.

A lock_hash is intentionally NOT a cryptographic anti-forgery proof (anyone with
write access to the file can recompute it). It is a tamper-EVIDENCE mechanism: it
makes the common, quiet failure — quietly editing a stated probability after the
fact, or back-dating a resolution — loud and machine-detectable, the same role
git history plays but enforceable in code before Gate C.

Interface (stable; relied on by score_brier.py + the Stage 7 prompt)
--------------------------------------------------------------------
    compute_lock_hash(rec: dict) -> str        # "sha256:<16 hex>"
    stamp(path: str, *, force: bool=False) -> dict
        -> {"id":..., "lock_hash":..., "action": "stamped"|"already"|"skipped", ...}
    verify(journal_dir: str) -> dict
        -> {"clean": bool, "issues": [...], "counts": {...}}

CLI
---
    python journal_integrity.py --stamp PRED-0042.md      # lock at open
    python journal_integrity.py --verify path/to/journal/ # audit a journal dir
    python journal_integrity.py --self-check
    # exit 0 = clean/ok, 1 = issues found, 2 = usage/parse error
"""

from __future__ import annotations

import argparse
import datetime as _dt
import glob
import hashlib
import os
import sys

# Fields hashed at open. Editing any of these after stamping breaks the lock_hash.
LOCKED_FIELDS = ("id", "date_opened", "asset", "direction", "probability", "horizon")


# ----------------------------------------------------------------------------
# Minimal YAML-subset loader (stdlib only; PyYAML used if present) — same subset
# the sibling skill scripts use, so manual-only mode stays dependency-free.
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


def _read_frontmatter(path: str):
    """Return (record_dict, raw_text). Raises ValueError on malformed frontmatter."""
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
    return data, text


# ----------------------------------------------------------------------------
# Lock hash
# ----------------------------------------------------------------------------


def _canonical(value) -> str:
    """Stable string form for a locked field (floats normalized so 0.6 == 0.60)."""
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, float):
        return repr(round(value, 10))
    if value is None:
        return ""
    return str(value).strip()


def compute_lock_hash(rec: dict) -> str:
    """Deterministic hash over the immutable open-time fields. Format 'sha256:<16 hex>'."""
    payload = "|".join(f"{f}={_canonical(rec.get(f))}" for f in LOCKED_FIELDS)
    digest = hashlib.sha256(payload.encode("utf-8")).hexdigest()[:16]
    return f"sha256:{digest}"


# ----------------------------------------------------------------------------
# Stamp (lock at open)
# ----------------------------------------------------------------------------


def stamp(path: str, *, force: bool = False) -> dict:
    """Write a ``lock_hash`` into a PRED record's frontmatter at open.

    Refuses to stamp a record whose ``resolution`` is already set unless ``force``
    (you lock at OPEN, before the outcome is known — stamping post-resolution would
    defeat the purpose). ``force`` exists only for backfilling exemplar fixtures.
    """
    rec, text = _read_frontmatter(path)
    rid = rec.get("id", os.path.basename(path))
    if rec.get("lock_hash"):
        existing = compute_lock_hash(rec)
        match = (str(rec.get("lock_hash")).strip() == existing)
        return {"id": rid, "lock_hash": rec.get("lock_hash"), "action": "already",
                "matches": match}
    resolved = isinstance(rec.get("resolution"), dict)
    if resolved and not force:
        return {"id": rid, "lock_hash": None, "action": "skipped",
                "reason": "resolution already set — lock at OPEN only (use force= to backfill)"}

    lock = compute_lock_hash(rec)
    # Insert a `lock_hash:` line just before the closing '---' of the frontmatter.
    lead = text[: len(text) - len(text.lstrip())]  # preserve any leading whitespace
    body = text.lstrip()
    inner = body[3:]
    end = inner.find("\n---")
    fm, rest = inner[:end], inner[end:]
    newline = "\n" if not fm.endswith("\n") else ""
    fm = fm + newline + f'lock_hash: "{lock}"\n'
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(lead + "---" + fm + rest)
    return {"id": rid, "lock_hash": lock, "action": "stamped"}


# ----------------------------------------------------------------------------
# Verify (tamper-evidence + resolution honesty)
# ----------------------------------------------------------------------------

_HORIZON_UNITS = {"day": 1, "days": 1, "week": 7, "weeks": 7,
                  "month": 30, "months": 30, "year": 365, "years": 365}


def _parse_date(value):
    try:
        return _dt.date.fromisoformat(str(value).strip())
    except (ValueError, TypeError):
        return None


def _horizon_days(horizon) -> "int | None":
    if not horizon:
        return None
    toks = str(horizon).strip().split()
    num = None
    for t in toks:
        try:
            num = int(float(t))
            break
        except ValueError:
            continue
    if num is None:
        return None
    unit_mult = 30  # default to ~month if unit is unrecognized but a number was given
    for t in toks:
        if t.lower().rstrip("s") + "s" in _HORIZON_UNITS or t.lower() in _HORIZON_UNITS:
            unit_mult = _HORIZON_UNITS.get(t.lower(), _HORIZON_UNITS.get(t.lower().rstrip("s") + "s", 30))
            break
    return num * unit_mult


def verify(journal_dir: str) -> dict:
    """Audit a journal directory for tampering + resolution honesty.

    Returns {"clean": bool, "issues": [...], "counts": {...}}. ``clean`` is the
    boolean Gate C consumes: True only if no record is tampered, no resolution is
    dishonest, and every *resolved* record is verifiable (carries a matching
    lock_hash). Unresolved records without a lock_hash are reported as a warning
    but do not block (they are not yet Gate C evidence).
    """
    paths = sorted(glob.glob(os.path.join(journal_dir, "PRED-*.md")))
    issues = []
    counts = {"records": 0, "resolved": 0, "tampered": 0, "dishonest": 0,
              "unverifiable_resolved": 0, "unstamped_open": 0}

    for path in paths:
        base = os.path.basename(path)
        if base.upper().startswith("PRED-TEMPLATE"):
            continue
        counts["records"] += 1
        try:
            rec, _ = _read_frontmatter(path)
        except (OSError, ValueError) as exc:
            issues.append(f"BLOCK {base}: unreadable record ({exc})")
            counts["tampered"] += 1
            continue

        stored = rec.get("lock_hash")
        has_lock = bool(stored)
        if has_lock and str(stored).strip() != compute_lock_hash(rec):
            issues.append(
                f"BLOCK {base}: lock_hash mismatch — a locked field "
                f"(id/date_opened/asset/direction/probability/horizon) was edited after open"
            )
            counts["tampered"] += 1

        res = rec.get("resolution")
        is_resolved = isinstance(res, dict) and res.get("outcome") in ("hit", "miss")
        if is_resolved:
            counts["resolved"] += 1
            if not has_lock:
                issues.append(f"BLOCK {base}: resolved but has no lock_hash (unverifiable track record)")
                counts["unverifiable_resolved"] += 1
            rr = res.get("realized_return")
            if not isinstance(rr, (int, float)):
                issues.append(f"BLOCK {base}: resolution has no numeric realized_return (no outcome provenance)")
                counts["dishonest"] += 1
            opened = _parse_date(rec.get("date_opened"))
            resolved_on = _parse_date(res.get("resolved_on"))
            if resolved_on is None:
                issues.append(f"BLOCK {base}: resolution has no valid resolved_on date")
                counts["dishonest"] += 1
            elif opened is not None:
                hd = _horizon_days(rec.get("horizon"))
                if resolved_on < opened:
                    issues.append(f"BLOCK {base}: resolved_on {resolved_on} precedes date_opened {opened}")
                    counts["dishonest"] += 1
                elif hd is not None and resolved_on < opened + _dt.timedelta(days=hd):
                    issues.append(
                        f"WARN {base}: resolved_on {resolved_on} is before the horizon end "
                        f"({opened + _dt.timedelta(days=hd)}) — early resolution"
                    )
        else:
            if not has_lock:
                counts["unstamped_open"] += 1
                issues.append(f"WARN {base}: open prediction not yet stamped with a lock_hash")

    clean = (counts["tampered"] == 0 and counts["dishonest"] == 0
             and counts["unverifiable_resolved"] == 0)
    return {"clean": clean, "issues": issues, "counts": counts}


# ----------------------------------------------------------------------------
# Self-check — proves stamping + every tamper/honesty case without external files.
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


def _write(tmp, name, **kw):
    defaults = dict(id="PRED-0001", asset="EXMP", p="0.62", resolution="null")
    defaults.update(kw)
    path = os.path.join(tmp, name)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(_PRED.format(**defaults))
    return path


def _self_check() -> int:
    import tempfile
    failures = []
    good_res = '{ outcome: hit, realized_return: 0.22, resolved_on: "2026-06-15" }'
    with tempfile.TemporaryDirectory() as tmp:
        # 1. Stamp an open record, then editing probability is detected as TAMPER.
        p = _write(tmp, "PRED-0001.md", id="PRED-0001", p="0.62")
        st = stamp(p)
        if st["action"] != "stamped" or not st["lock_hash"]:
            failures.append(f"stamp should lock an open record, got {st}")
        # Re-stamp is idempotent and matches.
        again = stamp(p)
        if again["action"] != "already" or not again.get("matches"):
            failures.append(f"re-stamp should report already+matches, got {again}")
        # Tamper: rewrite probability 0.62 -> 0.95 keeping the old lock_hash.
        with open(p, encoding="utf-8") as fh:
            tampered = fh.read().replace("probability: 0.62", "probability: 0.95")
        with open(p, "w", encoding="utf-8") as fh:
            fh.write(tampered)
        rep = verify(tmp)
        if rep["clean"] or rep["counts"]["tampered"] != 1:
            failures.append(f"edited probability must be flagged TAMPER, got {rep}")

    with tempfile.TemporaryDirectory() as tmp:
        # 2. A clean, stamped, properly-resolved journal verifies clean.
        p = _write(tmp, "PRED-0002.md", id="PRED-0002", p="0.62")
        stamp(p)
        with open(p, encoding="utf-8") as fh:
            txt = fh.read().replace("resolution: null", f"resolution: {good_res}")
        with open(p, "w", encoding="utf-8") as fh:
            fh.write(txt)
        rep = verify(tmp)
        if not rep["clean"] or rep["counts"]["resolved"] != 1:
            failures.append(f"clean stamped+resolved journal should verify clean, got {rep}")

    with tempfile.TemporaryDirectory() as tmp:
        # 3. Resolved with no lock_hash -> unverifiable -> NOT clean.
        p = _write(tmp, "PRED-0003.md", id="PRED-0003", p="0.7", resolution=good_res)
        rep = verify(tmp)
        if rep["clean"] or rep["counts"]["unverifiable_resolved"] != 1:
            failures.append(f"resolved w/o lock_hash must block, got {rep}")
        # stamp refuses a resolved record unless force.
        st = stamp(p)
        if st["action"] != "skipped":
            failures.append(f"stamp must refuse a resolved record without force, got {st}")

    with tempfile.TemporaryDirectory() as tmp:
        # 4. Invented resolution (no realized_return / no resolved_on) -> dishonest -> NOT clean.
        p = _write(tmp, "PRED-0004.md", id="PRED-0004", p="0.7")
        stamp(p)
        with open(p, encoding="utf-8") as fh:
            txt = fh.read().replace("resolution: null", "resolution: { outcome: hit }")
        with open(p, "w", encoding="utf-8") as fh:
            fh.write(txt)
        rep = verify(tmp)
        if rep["clean"] or rep["counts"]["dishonest"] < 1:
            failures.append(f"resolution with no provenance must block, got {rep}")

    if failures:
        print("SELF-CHECK FAILED:", file=sys.stderr)
        for f in failures:
            print(f"  - {f}", file=sys.stderr)
        return 1
    print("SELF-CHECK PASSED (stamp + tamper / clean / unverifiable / dishonest)")
    return 0


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(
        description="Tamper-evidence + resolution-honesty for the prediction journal.")
    parser.add_argument("--stamp", metavar="PRED.md",
                        help="Write a lock_hash into an OPEN prediction record.")
    parser.add_argument("--force", action="store_true",
                        help="Allow --stamp on an already-resolved record (fixture backfill only).")
    parser.add_argument("--verify", metavar="JOURNAL_DIR",
                        help="Audit a journal directory for tampering + resolution honesty.")
    parser.add_argument("--self-check", action="store_true",
                        help="Run embedded integrity fixtures and exit.")
    args = parser.parse_args(argv)

    if args.self_check:
        return _self_check()
    if args.stamp:
        try:
            res = stamp(args.stamp, force=args.force)
        except (OSError, ValueError) as exc:
            print(f"ERROR: {exc}", file=sys.stderr)
            return 2
        print(f"{res['action'].upper()}: {res.get('id')} lock_hash={res.get('lock_hash')}")
        if res.get("reason"):
            print(f"  - {res['reason']}")
        return 0
    if args.verify:
        rep = verify(args.verify)
        c = rep["counts"]
        print(f"Records: {c['records']}  resolved: {c['resolved']}  "
              f"tampered: {c['tampered']}  dishonest: {c['dishonest']}  "
              f"unverifiable_resolved: {c['unverifiable_resolved']}  unstamped_open: {c['unstamped_open']}")
        for i in rep["issues"]:
            print(f"  - {i}")
        print(f"INTEGRITY: {'CLEAN' if rep['clean'] else 'ISSUES FOUND'}")
        return 0 if rep["clean"] else 1
    parser.error("provide --stamp, --verify, or --self-check")
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
