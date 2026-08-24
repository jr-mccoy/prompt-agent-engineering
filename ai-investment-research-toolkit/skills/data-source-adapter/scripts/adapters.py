#!/usr/bin/env python3
"""Data-source adapters — the stubbable seam between the toolkit and any provider.

For informational and research purposes only. Not financial, investment, or tax advice.

Status (Phase 6):
  - IMPLEMENTED (stdlib only):
      * seam -> data/input/<seam>/ path resolution      (resolve_manual_path)
      * point-in-time check                              (validate_as_of)
      * manual-only read of trivial CSV / JSON files     (read_manual_record)
      * loading config/data_sources.yaml                (load_data_sources; PyYAML if
        present, else an embedded YAML-subset parser — manual-only stays dependency-free)
  - DEFERRED STUB (raises NotImplementedError with next steps) — needs a purchased provider:
      * live provider fetch                              (DataSourceAdapter._fetch_live)

The contract these implement is described in ../references/adapter_interface.md and the
manual-only layout in ../references/manual_only_mode.md. The two load-bearing rules:
  1. Never return a value dated after the requested as_of (look-ahead prevention).
  2. Never fabricate a missing value — report it as UNAVAILABLE so Stage 1 can queue it.
"""

from __future__ import annotations

import argparse
import csv
import json
import os
from dataclasses import dataclass, field
from datetime import date, datetime
from typing import Any, Dict, List

# The five DATA seams owned by this skill. The broker seams (PaperBrokerAdapter,
# LiveBrokerAdapter) belong to the deferred paper-trade-executor skill, not here.
DATA_SEAMS = (
    "MarketDataAdapter",
    "FundamentalsAdapter",
    "FilingsAdapter",
    "OnChainAdapter",
    "OptionsChainAdapter",
)

# Default manual-only input root, relative to the toolkit root.
DEFAULT_INPUT_ROOT = "data/input"

# Map each seam to its conventional manual_input subdirectory.
SEAM_DIR = {
    "MarketDataAdapter": "prices",
    "FundamentalsAdapter": "fundamentals",
    "FilingsAdapter": "filings",
    "OnChainAdapter": "onchain",
    "OptionsChainAdapter": "options",
}


@dataclass
class Record:
    """Normalized, provider-agnostic record handed to the stage prompts.

    `unavailable` lists requested fields with no real value; they are QUEUED, never guessed.
    """

    seam: str
    key: str
    as_of: str
    source: str = "manual_input"
    fields: Dict[str, Any] = field(default_factory=dict)
    unavailable: List[str] = field(default_factory=list)
    notes: str = ""

    def to_dict(self) -> Dict[str, Any]:
        return {
            "seam": self.seam,
            "key": self.key,
            "as_of": self.as_of,
            "source": self.source,
            "fields": self.fields,
            "unavailable": self.unavailable,
            "notes": self.notes,
        }


def _parse_date(value: str) -> date:
    """Parse a YYYY-MM-DD string into a date (raises ValueError on bad input)."""
    return datetime.strptime(value.strip(), "%Y-%m-%d").date()


def validate_as_of(record_date: str, as_of: str) -> bool:
    """Return True only if `record_date` is on or before `as_of` (point-in-time rule).

    A record dated after as_of is look-ahead leakage and must be rejected.
    """
    return _parse_date(record_date) <= _parse_date(as_of)


def resolve_manual_path(seam: str, key: str, as_of: str, root: str = DEFAULT_INPUT_ROOT) -> str:
    """Resolve the conventional manual-only file path for a seam/key/as_of.

    Convention (see references/manual_only_mode.md): data/input/<seam_dir>/<KEY>_<as_of>.<ext>
    Returns the path WITHOUT extension; read_manual_record tries .csv then .json.
    """
    if seam not in SEAM_DIR:
        raise ValueError(f"Unknown seam {seam!r}; expected one of {DATA_SEAMS}")
    return os.path.join(root, SEAM_DIR[seam], f"{key}_{as_of}")


def read_manual_record(seam: str, key: str, as_of: str, root: str = DEFAULT_INPUT_ROOT) -> Record:
    """Read a manual-only CSV or JSON file into a normalized Record (stdlib only).

    - Tries <path>.csv then <path>.json.
    - Rejects any row/record dated after as_of (validate_as_of).
    - Empty CSV cells / JSON nulls become `unavailable` entries (queued, NOT guessed).
    - If no file exists, returns a Record whose requested fields are all unavailable.
    Richer formats (e.g. raw filing text for FilingsAdapter) are a documented stub below.
    """
    base = resolve_manual_path(seam, key, as_of, root)
    csv_path, json_path = base + ".csv", base + ".json"

    if os.path.exists(csv_path):
        return _read_csv(seam, key, as_of, csv_path)
    if os.path.exists(json_path):
        return _read_json(seam, key, as_of, json_path)

    if seam == "FilingsAdapter":
        # Filing/news bodies are free text; structured extraction is intentionally a stub.
        raise NotImplementedError(
            "FilingsAdapter manual read of free-text filings is a documented stub. "
            "Provide a JSON metadata file (date + fields) at "
            f"{json_path}, or implement text extraction here."
        )

    return Record(
        seam=seam,
        key=key,
        as_of=as_of,
        source="manual_input",
        unavailable=["*"],
        notes=f"No manual file found at {csv_path} or {json_path}; all fields queued.",
    )


def _coerce(value: str) -> Any:
    """Best-effort numeric coercion for CSV strings; leaves non-numeric strings as-is."""
    if value is None:
        return None
    text = value.strip()
    if text == "":
        return None
    try:
        return int(text)
    except ValueError:
        pass
    try:
        return float(text)
    except ValueError:
        return text


def _read_csv(seam: str, key: str, as_of: str, path: str) -> Record:
    rec = Record(seam=seam, key=key, as_of=as_of, source=f"manual_input:{os.path.basename(path)}")
    with open(path, newline="", encoding="utf-8") as fh:
        rows = list(csv.DictReader(fh))
    if not rows:
        rec.unavailable.append("*")
        rec.notes = "Empty CSV; all fields queued."
        return rec
    # Use the latest row on/before as_of (point-in-time). Reject future-dated rows.
    valid = [r for r in rows if r.get("date") and validate_as_of(r["date"], as_of)]
    if not valid:
        rec.unavailable.append("*")
        rec.notes = "No CSV rows dated on/before as_of; all fields queued."
        return rec
    latest = max(valid, key=lambda r: _parse_date(r["date"]))
    for col, raw in latest.items():
        if col == "date":
            continue
        coerced = _coerce(raw)
        if coerced is None:
            rec.unavailable.append(col)
        else:
            rec.fields[col] = coerced
    rec.notes = f"From CSV row dated {latest['date']}."
    return rec


def _read_json(seam: str, key: str, as_of: str, path: str) -> Record:
    rec = Record(seam=seam, key=key, as_of=as_of, source=f"manual_input:{os.path.basename(path)}")
    with open(path, encoding="utf-8") as fh:
        obj = json.load(fh)
    record_date = obj.get("as_of")
    if record_date and not validate_as_of(record_date, as_of):
        rec.unavailable.append("*")
        rec.notes = f"JSON as_of {record_date} is after requested {as_of}; rejected (look-ahead)."
        return rec
    for k, v in obj.items():
        if k == "as_of":
            continue
        if v is None:
            rec.unavailable.append(k)
        else:
            rec.fields[k] = v
    return rec


class DataSourceAdapter:
    """Common contract for every data seam (see references/adapter_interface.md)."""

    def __init__(self, seam: str, implementation: str = "stub", root: str = DEFAULT_INPUT_ROOT):
        if seam not in DATA_SEAMS:
            raise ValueError(f"Unknown seam {seam!r}; expected one of {DATA_SEAMS}")
        self.seam = seam
        self.implementation = implementation
        self.root = root

    def fetch(self, key: str, as_of: str) -> Record:
        """Return a normalized Record for `key` as knowable on `as_of`.

        implementation == 'stub' -> manual-only read; otherwise -> live provider (stub).
        """
        if self.implementation == "stub":
            return read_manual_record(self.seam, key, as_of, self.root)
        return self._fetch_live(key, as_of)

    def _fetch_live(self, key: str, as_of: str) -> Record:
        """Live provider fetch — documented stub.

        To implement: read the provider id from self.implementation, load the API key from an
        environment variable or a git-ignored config/*.local.yaml (NEVER a tracked file), call
        the provider for `key` as of `as_of`, then normalize into a Record obeying the two rules
        (no post-as_of data; missing -> unavailable, never guessed).
        """
        raise NotImplementedError(
            f"Live fetch for seam {self.seam!r} via provider {self.implementation!r} is not "
            "implemented. Wire the provider here and supply its key via env/local config. "
            "Until then, set this seam to 'stub' in config/data_sources.yaml for manual-only mode."
        )


# --------------------------------------------------------------------------------------------
# Minimal YAML-subset loader (stdlib only; PyYAML used if present). Handles what
# config/data_sources.yaml needs: block maps, block scalars, flow seqs/maps, scalars.
# Keeps manual-only mode dependency-free.
# --------------------------------------------------------------------------------------------


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
        result: Dict[str, Any] = {}
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


def load_data_sources(path: str = "config/data_sources.yaml") -> Dict[str, Any]:
    """Load the seam->implementation map from config/data_sources.yaml.

    Uses PyYAML if installed, else the embedded stdlib YAML-subset parser, so this works in
    manual-only mode with no dependencies. Returns the mapping unchanged; the live provider
    branch (_fetch_live) remains intentionally unimplemented until a provider is wired in.
    """
    with open(path, encoding="utf-8") as fh:
        data = _load_yaml(fh.read())
    if not isinstance(data, dict):
        raise ValueError(f"{path} did not parse to a mapping")
    return data


def _self_check() -> int:
    """Prove the point-in-time + no-fabrication rules and YAML config load (no external files)."""
    import sys
    import tempfile

    failures: List[str] = []

    # 1. Look-ahead rule: a record dated after as_of is rejected.
    if validate_as_of("2026-06-19", "2026-06-18"):
        failures.append("validate_as_of allowed a future-dated record (look-ahead leak)")
    if not validate_as_of("2026-06-17", "2026-06-18"):
        failures.append("validate_as_of rejected a valid prior-dated record")

    with tempfile.TemporaryDirectory() as tmp:
        prices = os.path.join(tmp, "prices")
        os.makedirs(prices)
        # CSV with a usable row + a future-dated row (must be ignored) + a blank cell (queued).
        with open(os.path.join(prices, "EXMP_2026-06-18.csv"), "w", encoding="utf-8") as fh:
            fh.write("date,close_usd,volume\n2026-06-18,1.23,\n2026-06-20,9.99,1\n")
        rec = read_manual_record("MarketDataAdapter", "EXMP", "2026-06-18", root=tmp)
        if rec.fields.get("close_usd") != 1.23:
            failures.append(f"manual read should pick the on/before-as_of row, got {rec.fields}")
        if "volume" not in rec.unavailable:
            failures.append(f"blank cell must be queued as unavailable, got {rec.unavailable}")

        # 2. Missing file -> all fields queued, nothing fabricated.
        miss = read_manual_record("MarketDataAdapter", "NONE", "2026-06-18", root=tmp)
        if miss.unavailable != ["*"] or miss.fields:
            failures.append(f"missing file must queue '*' and fabricate nothing, got {miss.to_dict()}")

        # 3. YAML config load (embedded parser) round-trips the tracked data_sources.yaml shape.
        cfg = os.path.join(tmp, "data_sources.yaml")
        with open(cfg, "w", encoding="utf-8") as fh:
            fh.write(
                "MarketDataAdapter:\n  implementation: stub\n  manual_input: data/input/prices/\n"
                "LiveBrokerAdapter:\n  implementation: stub\n  enabled: false\n"
            )
        loaded = load_data_sources(cfg)
        if loaded.get("MarketDataAdapter", {}).get("implementation") != "stub":
            failures.append(f"load_data_sources misparsed implementation, got {loaded}")
        if loaded.get("LiveBrokerAdapter", {}).get("enabled") is not False:
            failures.append(f"load_data_sources must read LiveBrokerAdapter.enabled=false, got {loaded}")

    # 4. Live fetch stays a deferred stub (no provider purchased).
    try:
        DataSourceAdapter("MarketDataAdapter", implementation="someprovider").fetch("X", "2026-06-18")
        failures.append("live fetch must raise NotImplementedError until a provider is wired in")
    except NotImplementedError:
        pass

    if failures:
        print("SELF-CHECK FAILED:", file=sys.stderr)
        for f in failures:
            print(f"  - {f}", file=sys.stderr)
        return 1
    print("SELF-CHECK PASSED (look-ahead reject / queue unavailable / YAML load / live deferred)")
    return 0


def _main(argv: List[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Data-source adapter (Phase 6). Manual-only mode reads from data/input/.",
    )
    parser.add_argument("--self-check", action="store_true",
                        help="Run embedded point-in-time / no-fabrication / YAML fixtures and exit.")
    parser.add_argument("--seam", choices=list(DATA_SEAMS), help="Which data seam.")
    parser.add_argument("--key", help="Symbol / token / underlying to fetch.")
    parser.add_argument("--as-of", dest="as_of", help="Point-in-time date YYYY-MM-DD.")
    parser.add_argument(
        "--manual",
        dest="root",
        default=DEFAULT_INPUT_ROOT,
        help=f"Manual-only input root (default {DEFAULT_INPUT_ROOT}).",
    )
    args = parser.parse_args(argv)

    if args.self_check:
        return _self_check()
    for req in ("seam", "key", "as_of"):
        if getattr(args, req) is None:
            parser.error(f"--{req.replace('_', '-')} is required (or use --self-check)")

    # Validate the as_of format early with a clear message.
    try:
        _parse_date(args.as_of)
    except ValueError:
        parser.error("--as-of must be YYYY-MM-DD")

    adapter = DataSourceAdapter(args.seam, implementation="stub", root=args.root)
    record = adapter.fetch(args.key, args.as_of)
    print(json.dumps(record.to_dict(), indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(_main())
