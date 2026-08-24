#!/usr/bin/env python3
"""test_gates.py — prove the gates + kill switch in code (stdlib unittest only).

For informational and research purposes only. Not financial, investment, or tax advice.
Nothing here places real-money trades.

Run from the toolkit root:

    python -m unittest discover -s tests -v
    # or
    python tests/test_gates.py

These tests load the four skill scripts directly from their paths and assert the
paper-only invariant and each gate:
  Gate A — a hypothesis pattern is blocked; a validated one (OOS n>=min, lift>0) passes.
  Gate B — unsized / no-stop / over-cap orders are REJECTED; a compliant one FILLS.
  Gate C — LiveBrokerAdapter.place_order raises (real money unreachable).
  Kill switch — halt:true HALTS an order with no fill.
  No fabrication — missing data is queued UNAVAILABLE, never guessed; the scorer
  ignores unresolved predictions.
"""

import importlib.util
import os
import sys
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SAMPLES = os.path.join(ROOT, "samples")


def _load(rel_path, name):
    spec = importlib.util.spec_from_file_location(name, os.path.join(ROOT, rel_path))
    mod = importlib.util.module_from_spec(spec)
    # Register before exec so dataclasses can resolve annotations via sys.modules.
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


validate_pattern = _load(
    "skills/pattern-knowledge-base/scripts/validate_pattern.py", "vp")
brokers = _load("skills/paper-trade-executor/scripts/brokers.py", "brk")
score_brier = _load("skills/prediction-journal/scripts/score_brier.py", "sb")
adapters = _load("skills/data-source-adapter/scripts/adapters.py", "ad")
build_snapshot = _load(
    "skills/data-source-adapter/scripts/build_snapshot.py", "bs")
screen_rank = _load(
    "skills/pattern-knowledge-base/scripts/screen_rank.py", "sr")


def _order(**kw):
    base = dict(
        order_id="ORD-TEST", timestamp="2026-06-18T00:00:00+00:00", symbol="EXMP",
        asset_class="equity", side="buy", quantity=100, price=5.0, stop=4.25,
        sizing_ref="orders.md#sizing", premortem_ref="orders.md#premortem",
    )
    base.update(kw)
    return brokers.Order(**base)


def _fresh():
    return brokers.Portfolio(capital_base=50000.0, cash=50000.0)


class GateA(unittest.TestCase):
    def test_hypothesis_pattern_blocked(self):
        r = validate_pattern.validate_pattern(
            os.path.join(SAMPLES, "patterns/PATTERN-0007.md"), 30)
        self.assertEqual(r["status"], "FAIL")
        self.assertFalse(r["eligible_for_validated"])
        self.assertEqual(r["record_status"], "hypothesis")

    def test_validated_pattern_passes(self):
        r = validate_pattern.validate_pattern(
            os.path.join(SAMPLES, "patterns/PATTERN-0001.md"), 30)
        self.assertEqual(r["status"], "PASS")
        self.assertTrue(r["eligible_for_validated"])

    def test_self_check(self):
        self.assertEqual(validate_pattern._self_check(), 0)


class GateB(unittest.TestCase):
    def setUp(self):
        self.broker = brokers.PaperBrokerAdapter(
            mandate=dict(brokers.DEFAULT_MANDATE), limits=brokers.DEFAULT_RISK_LIMITS)

    def test_compliant_fills(self):
        pf = _fresh()
        fill = self.broker.place_order(_order(), pf)
        self.assertEqual(fill.status, "FILLED")
        self.assertEqual(pf.cash, 49500.0)

    def test_unsized_rejected(self):
        fill = self.broker.place_order(_order(sizing_ref=""), _fresh())
        self.assertEqual(fill.status, "REJECTED")
        self.assertTrue(any("unsized" in r for r in fill.reasons))

    def test_no_stop_rejected(self):
        fill = self.broker.place_order(_order(stop=None), _fresh())
        self.assertEqual(fill.status, "REJECTED")

    def test_over_cap_rejected(self):
        fill = self.broker.place_order(_order(quantity=500), _fresh())
        self.assertEqual(fill.status, "REJECTED")
        self.assertTrue(any("per-position cap" in r for r in fill.reasons))

    def test_rejected_order_does_not_mutate_portfolio(self):
        pf = _fresh()
        self.broker.place_order(_order(quantity=500), pf)
        self.assertEqual(pf.cash, 50000.0)
        self.assertEqual(pf.positions, {})


class GateC(unittest.TestCase):
    def test_live_adapter_unreachable(self):
        live = brokers.LiveBrokerAdapter(mandate=dict(brokers.DEFAULT_MANDATE))
        with self.assertRaises(NotImplementedError):
            live.place_order(_order(), _fresh())

    def test_gate_c_status_not_ready(self):
        live = brokers.LiveBrokerAdapter(mandate=dict(brokers.DEFAULT_MANDATE))
        ready, unmet = live.gate_c_status(resolved_predictions=3, brier=0.2915)
        self.assertFalse(ready)
        self.assertEqual(len(unmet), 3)


class KillSwitch(unittest.TestCase):
    def test_halt_halts_order(self):
        broker = brokers.PaperBrokerAdapter(
            mandate={**brokers.DEFAULT_MANDATE, "halt": True},
            limits=brokers.DEFAULT_RISK_LIMITS)
        pf = _fresh()
        fill = broker.place_order(_order(), pf)
        self.assertEqual(fill.status, "HALTED")
        self.assertEqual(pf.positions, {})


class NoFabrication(unittest.TestCase):
    def test_calibration_ignores_unresolved(self):
        rep = score_brier.calibration_report(os.path.join(SAMPLES, "journal"))
        self.assertEqual(rep["n"], 3)  # PRED-0045 is open and excluded
        self.assertAlmostEqual(rep["brier"], 0.2915, places=4)
        self.assertFalse(rep["gate_c"]["unlock_ready"])
        self.assertEqual(rep["schema_errors"], [])

    def test_missing_data_queued_not_guessed(self):
        rec = adapters.read_manual_record(
            "MarketDataAdapter", "EXMP", "2026-06-18",
            root=os.path.join(SAMPLES, "input"))
        self.assertEqual(rec.fields.get("close_usd"), 5.0)
        self.assertIn("pe_ratio", rec.unavailable)

    def test_config_load_round_trips(self):
        limits, mandate = brokers.load_config(
            os.path.join(ROOT, "config/risk_limits.yaml"),
            os.path.join(ROOT, "config/mandate.yaml"))
        self.assertEqual(limits["max_position_pct"], 0.02)
        self.assertEqual(limits["per_asset_class"]["crypto"]["max_position_pct"], 0.01)
        self.assertIs(limits["require_stop_loss"], True)
        self.assertEqual(mandate["capital"]["simulated_usd"], 50000)
        self.assertEqual(mandate["gate_c"]["max_brier_score"], 0.18)


class Stage1Snapshot(unittest.TestCase):
    """build_snapshot writes an immutable, look-ahead-safe universe from manual data."""

    def test_self_check(self):
        self.assertEqual(build_snapshot._self_check(), 0)

    def test_snapshot_from_samples_and_immutability(self):
        import csv as _csv
        import tempfile
        with tempfile.TemporaryDirectory() as tmp:
            summary = build_snapshot.build_snapshot(
                "2026-06-18",
                os.path.join(SAMPLES, "input"),
                tmp,
                os.path.join(ROOT, "config/asset_classes.yaml"),
            )
            self.assertEqual(summary["included"], 1)
            with open(summary["universe_csv"], encoding="utf-8") as fh:
                rows = {r["symbol"]: r for r in _csv.DictReader(fh)}
            self.assertIn("EXMP", rows)
            self.assertEqual(float(rows["EXMP"]["close_usd"]), 5.0)
            # pe_ratio was null in the fixture -> queued UNAVAILABLE, never guessed.
            self.assertIn("pe_ratio", rows["EXMP"]["unavailable"])
            # Immutability: a second build on the same as_of must refuse.
            with self.assertRaises(FileExistsError):
                build_snapshot.build_snapshot(
                    "2026-06-18", os.path.join(SAMPLES, "input"), tmp,
                    os.path.join(ROOT, "config/asset_classes.yaml"))


class Stage4Screen(unittest.TestCase):
    """screen_rank enforces Gate A at ranking time: only validated patterns score."""

    def test_self_check(self):
        self.assertEqual(screen_rank._self_check(), 0)

    def test_only_validated_scores_on_samples(self):
        firings = {"EXMP": {"PATTERN-0001": "margins", "PATTERN-0007": "insiders"}}
        result = screen_rank.screen_rank(
            firings, os.path.join(SAMPLES, "patterns"), 30)
        row = result["ranked"][0]
        # Validated PATTERN-0001 (medium confidence -> weight 2) scores; hypothesis 0007 does not.
        self.assertEqual(row["score"], 2)
        self.assertEqual([p["pattern"] for p in row["scored_patterns"]], ["PATTERN-0001"])
        self.assertEqual([p["pattern"] for p in row["paper_only_signals"]], ["PATTERN-0007"])

    def test_hypothesis_only_candidate_scores_zero(self):
        firings = {"ZZZ": {"PATTERN-0007": "insiders"}}
        row = screen_rank.screen_rank(
            firings, os.path.join(SAMPLES, "patterns"), 30)["ranked"][0]
        self.assertEqual(row["score"], 0)


class ExposureReport(unittest.TestCase):
    """brokers.exposure_report is read-only and computes exposure vs the Gate B caps."""

    def test_report_math_within_caps(self):
        pf = _fresh()
        broker = brokers.PaperBrokerAdapter(
            mandate=dict(brokers.DEFAULT_MANDATE), limits=brokers.DEFAULT_RISK_LIMITS)
        broker.place_order(_order(), pf)  # $500 of $50k = 1% deployed
        rep = brokers.exposure_report(pf, brokers.DEFAULT_RISK_LIMITS)
        self.assertAlmostEqual(rep["deployed"]["fraction"], 0.01, places=6)
        self.assertTrue(rep["deployed"]["within"])
        self.assertTrue(rep["by_position"]["EXMP"]["within"])
        # read-only: the ledger is unchanged by reporting
        self.assertEqual(pf.cash, 49500.0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
