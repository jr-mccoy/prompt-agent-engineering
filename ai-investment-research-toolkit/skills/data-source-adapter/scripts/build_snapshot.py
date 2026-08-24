#!/usr/bin/env python3
"""build_snapshot.py — write an immutable, look-ahead-safe Stage 1 universe snapshot.

For informational and research purposes only. Not financial, investment, or tax advice.
Nothing here places real-money trades.

STATUS: implemented (Phase 7, stdlib only). This is the executable writer behind Stage 1:
it derives the candidate universe from the manual-only inputs, pulls each candidate's
point-in-time record through ``adapters.read_manual_record`` (which already rejects any
value dated after ``as_of``), applies the active-class universe filters from
``config/asset_classes.yaml`` where the data is available, and writes a deterministic
``data/snapshots/<as_of>/universe.csv`` plus per-candidate raw JSON.

It hardens two Stage 1 invariants *in code*, not by trust:
  1. **Immutability** — it refuses to overwrite an existing snapshot folder (each ``as_of``
     is written once). Re-running on a written date is a hard error, not a silent clobber.
  2. **No fabrication / no look-ahead** — every value comes from ``read_manual_record`` with
     its ``as_of`` contract; unavailable fields are recorded as ``UNAVAILABLE`` and queued,
     never guessed, and a candidate with no point-in-time price is skipped (not back-filled).

It does NOT pull live data (that is the deferred provider branch in ``adapters.py``), assign
a pattern status, or score anything — Stages 3/4 do that.

Interface (stable; relied on by the Stage 1 prompt + tests)
-----------------------------------------------------------
    build_snapshot(as_of, manual_root, out_root, asset_classes_path=None,
                   seams=("MarketDataAdapter", "FundamentalsAdapter")) -> dict

CLI
---
    python skills/data-source-adapter/scripts/build_snapshot.py \
        --as-of 2026-06-18 --manual samples/input --out /tmp/snap
    python skills/data-source-adapter/scripts/build_snapshot.py --self-check
    # exit code 0 = snapshot written, 2 = refused (immutability) / usage error
"""

from __future__ import annotations

import argparse
import csv
import glob
import json
import os
import sys

# adapters.py is a sibling module; make it importable both as a CLI (run by path) and when
# this file is loaded by path from tests (which does not put the script dir on sys.path).
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from adapters import (  # noqa: E402  (intentional: after sys.path shim)
    SEAM_DIR,
    Record,
    read_manual_record,
)

try:  # load_data_sources / config loader is optional; only asset_classes.yaml is needed here
    from adapters import _load_yaml  # noqa: E402
except ImportError:  # pragma: no cover
    _load_yaml = None  # type: ignore

# The seam whose presence defines whether a candidate has any point-in-time data at all.
PRICE_SEAM = "MarketDataAdapter"


def _read_asset_classes(path):
    """Return the active-class -> universe_filters map from config/asset_classes.yaml.

    Returns {} if the file is absent or the parser is unavailable; callers then skip filtering
    (every priced candidate is included) rather than guessing a filter.
    """
    if not path or not os.path.exists(path) or _load_yaml is None:
        return {}
    with open(path, encoding="utf-8") as fh:
        data = _load_yaml(fh.read())
    if not isinstance(data, dict):
        return {}
    active = {}
    for cls, body in data.items():
        if isinstance(body, dict) and body.get("active") is True:
            active[cls] = (body.get("universe_filters") or {})
    return active


def _discover_symbols(manual_root, as_of):
    """List symbols that have a manual price file for `as_of` (the manual-only universe).

    Convention (adapters.SEAM_DIR): <manual_root>/prices/<SYMBOL>_<as_of>.{json,csv}.
    """
    price_dir = os.path.join(manual_root, SEAM_DIR[PRICE_SEAM])
    symbols = set()
    for ext in ("json", "csv"):
        for p in glob.glob(os.path.join(price_dir, f"*_{as_of}.{ext}")):
            base = os.path.basename(p)
            symbols.add(base[: -(len(as_of) + len(ext) + 2)])  # strip _<as_of>.<ext>
    return sorted(symbols)


def _filters_verdict(filters, fields):
    """Evaluate the universe filters we CAN against a candidate's available fields.

    Returns (passes_all_evaluable, notes). A filter whose input field is absent/UNAVAILABLE is
    not evaluated (recorded as a note) — it neither passes nor fails (no guessing).
    """
    notes = []
    ok = True
    checks = {
        "max_market_cap_usd": ("market_cap_usd", lambda v, lim: v <= lim),
        "min_market_cap_usd": ("market_cap_usd", lambda v, lim: v >= lim),
    }
    # liquidity floor: avg daily $ volume ~= close * volume when both present
    for fname, (field, test) in checks.items():
        if fname not in filters:
            continue
        val = fields.get(field)
        if not isinstance(val, (int, float)):
            notes.append(f"{fname}: {field} UNAVAILABLE (not evaluated)")
            continue
        if not test(val, filters[fname]):
            ok = False
            notes.append(f"{fname}: failed ({field}={val} vs {filters[fname]})")
    if "min_avg_daily_dollar_volume" in filters:
        close, vol = fields.get("close_usd"), fields.get("volume")
        if isinstance(close, (int, float)) and isinstance(vol, (int, float)):
            addv = close * vol
            if addv < filters["min_avg_daily_dollar_volume"]:
                ok = False
                notes.append(f"min_avg_daily_dollar_volume: failed ({addv:.0f})")
        else:
            notes.append("min_avg_daily_dollar_volume: inputs UNAVAILABLE (not evaluated)")
    return ok, notes


def build_snapshot(as_of, manual_root, out_root,
                   asset_classes_path="config/asset_classes.yaml",
                   seams=("MarketDataAdapter", "FundamentalsAdapter")):
    """Build one immutable, look-ahead-safe universe snapshot. Returns a summary dict.

    Raises FileExistsError if the snapshot folder already exists (immutability).
    """
    snap_dir = os.path.join(out_root, as_of)
    if os.path.exists(snap_dir):
        raise FileExistsError(
            f"snapshot {snap_dir} already exists — snapshots are immutable per as_of; "
            "never overwrite a written snapshot (delete it deliberately if you must rebuild)."
        )

    active = _read_asset_classes(asset_classes_path)
    symbols = _discover_symbols(manual_root, as_of)

    included, skipped = [], []
    raw_records = {}
    field_names = set()

    for sym in symbols:
        price = read_manual_record(PRICE_SEAM, sym, as_of, manual_root)
        # No usable point-in-time price (missing or future-dated -> '*' unavailable) => skip,
        # never fabricate. This is the look-ahead guard surfacing as a skip, not a leak.
        if "*" in price.unavailable or not price.fields:
            skipped.append({"symbol": sym, "reason": price.notes or "no point-in-time price"})
            continue

        merged = dict(price.fields)
        unavailable = list(price.unavailable)
        asset_class = str(merged.pop("asset_class", "equity"))

        # Pull any additional seams (fundamentals, etc.) point-in-time; queue what is missing.
        for seam in seams:
            if seam == PRICE_SEAM:
                continue
            try:
                extra = read_manual_record(seam, sym, as_of, manual_root)
            except NotImplementedError:
                continue
            for k, v in extra.fields.items():
                merged.setdefault(k, v)
            unavailable.extend(u for u in extra.unavailable if u != "*")

        filters = active.get(asset_class, {})
        passes, notes = _filters_verdict(filters, merged)
        if filters and not passes:
            skipped.append({"symbol": sym, "reason": "; ".join(notes) or "filter failed"})
            continue

        row = {"symbol": sym, "asset_class": asset_class, "as_of": as_of}
        row.update({k: merged[k] for k in merged})
        row["unavailable"] = ";".join(sorted(set(unavailable))) if unavailable else ""
        row["source"] = price.source
        row["filter_notes"] = "; ".join(notes)
        included.append(row)
        field_names.update(merged.keys())
        raw_records[sym] = Record(
            seam=PRICE_SEAM, key=sym, as_of=as_of, source=price.source,
            fields=merged, unavailable=sorted(set(unavailable)),
        ).to_dict()

    # Write the immutable snapshot.
    os.makedirs(snap_dir)
    columns = ["symbol", "asset_class", "as_of"] + sorted(field_names) + [
        "unavailable", "source", "filter_notes"]
    universe_csv = os.path.join(snap_dir, "universe.csv")
    with open(universe_csv, "w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=columns)
        writer.writeheader()
        for row in sorted(included, key=lambda r: r["symbol"]):
            writer.writerow({c: row.get(c, "") for c in columns})

    raw_dir = os.path.join(snap_dir, "raw")
    os.makedirs(raw_dir)
    for sym, rec in raw_records.items():
        with open(os.path.join(raw_dir, f"{sym}.json"), "w", encoding="utf-8") as fh:
            json.dump(rec, fh, indent=2, sort_keys=True)

    summary = {
        "as_of": as_of,
        "snapshot_dir": snap_dir,
        "universe_csv": universe_csv,
        "active_classes": sorted(active.keys()),
        "candidates_priced": len(symbols),
        "included": len(included),
        "skipped": skipped,
        "queued_unavailable": sum(1 for r in included if r["unavailable"]),
    }
    with open(os.path.join(snap_dir, "snapshot_meta.json"), "w", encoding="utf-8") as fh:
        json.dump(summary, fh, indent=2, sort_keys=True)
    return summary


def _self_check() -> int:
    """Prove immutability + look-ahead-safety + no-fabrication without external files."""
    import tempfile

    failures = []
    with tempfile.TemporaryDirectory() as tmp:
        manual = os.path.join(tmp, "input")
        prices = os.path.join(manual, "prices")
        os.makedirs(prices)
        # AAA: clean priced candidate inside the equity band.
        with open(os.path.join(prices, "AAA_2026-06-18.json"), "w", encoding="utf-8") as fh:
            json.dump({"as_of": "2026-06-18", "close_usd": 5.0, "volume": 600000,
                       "market_cap_usd": 250000000, "pe_ratio": None}, fh)
        # BBB: only a FUTURE-dated record -> read_manual_record rejects it -> must be SKIPPED.
        with open(os.path.join(prices, "BBB_2026-06-18.json"), "w", encoding="utf-8") as fh:
            json.dump({"as_of": "2026-06-30", "close_usd": 99.0,
                       "market_cap_usd": 100000000}, fh)
        # CCC: priced but market_cap is null -> included, market_cap queued UNAVAILABLE.
        with open(os.path.join(prices, "CCC_2026-06-18.json"), "w", encoding="utf-8") as fh:
            json.dump({"as_of": "2026-06-18", "close_usd": 3.0, "volume": 500000,
                       "market_cap_usd": None}, fh)
        # DDD: over the equity max market cap -> filtered out.
        with open(os.path.join(prices, "DDD_2026-06-18.json"), "w", encoding="utf-8") as fh:
            json.dump({"as_of": "2026-06-18", "close_usd": 50.0, "volume": 900000,
                       "market_cap_usd": 900000000}, fh)
        ac = os.path.join(tmp, "asset_classes.yaml")
        with open(ac, "w", encoding="utf-8") as fh:
            fh.write("equity:\n  active: true\n  universe_filters:\n"
                     "    max_market_cap_usd: 300000000\n    min_market_cap_usd: 10000000\n"
                     "    min_avg_daily_dollar_volume: 100000\n")
        out = os.path.join(tmp, "snapshots")

        summary = build_snapshot("2026-06-18", manual, out, ac)
        with open(summary["universe_csv"], encoding="utf-8") as fh:
            rows = {r["symbol"]: r for r in csv.DictReader(fh)}

        if "AAA" not in rows or float(rows["AAA"]["close_usd"]) != 5.0:
            failures.append(f"AAA should be included with its price, got {list(rows)}")
        if "BBB" in rows:
            failures.append("BBB had only a future-dated record — must be skipped (look-ahead)")
        if "CCC" not in rows or "market_cap_usd" not in (rows.get("CCC", {}).get("unavailable", "")):
            failures.append(f"CCC should be included with market_cap queued UNAVAILABLE, got {rows.get('CCC')}")
        if "DDD" in rows:
            failures.append("DDD exceeds the equity max market cap — must be filtered out")

        # Immutability: a second build on the same as_of must refuse.
        try:
            build_snapshot("2026-06-18", manual, out, ac)
            failures.append("second build on a written snapshot must refuse (immutability)")
        except FileExistsError:
            pass

    if failures:
        print("SELF-CHECK FAILED:", file=sys.stderr)
        for f in failures:
            print(f"  - {f}", file=sys.stderr)
        return 1
    print("SELF-CHECK PASSED (priced include / look-ahead skip / UNAVAILABLE queue / filter / immutable)")
    return 0


def _main(argv=None) -> int:
    parser = argparse.ArgumentParser(
        description="Build an immutable, look-ahead-safe Stage 1 universe snapshot (Phase 7).",
    )
    parser.add_argument("--self-check", action="store_true",
                        help="Run embedded immutability / look-ahead / no-fabrication fixtures and exit.")
    parser.add_argument("--as-of", dest="as_of", help="Snapshot date YYYY-MM-DD.")
    parser.add_argument("--manual", dest="manual_root", default="data/input",
                        help="Manual-only input root (default data/input).")
    parser.add_argument("--out", dest="out_root", default="data/snapshots",
                        help="Snapshot output root (default data/snapshots).")
    parser.add_argument("--asset-classes", dest="asset_classes_path",
                        default="config/asset_classes.yaml",
                        help="Path to asset_classes.yaml (default config/asset_classes.yaml).")
    args = parser.parse_args(argv)

    if args.self_check:
        return _self_check()
    if not args.as_of:
        parser.error("--as-of is required (or use --self-check)")

    try:
        summary = build_snapshot(args.as_of, args.manual_root, args.out_root,
                                 args.asset_classes_path)
    except FileExistsError as exc:
        print(f"REFUSED: {exc}", file=sys.stderr)
        return 2
    print(json.dumps(summary, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(_main())
