#!/usr/bin/env python3
"""test_gates.py — prove the four gates in code, against the sample fixtures.

Not legal, tax, or accounting advice. These tests verify that the gates block and
pass where they should; they say nothing about the quality of any scope, contract
or price.

Run from the toolkit root:

    python -m unittest discover -s tests -v

The tests load each skill script directly from its path, so they exercise the same
code the pipeline runs -- there is no separate test-only implementation.
"""

from __future__ import annotations

import importlib.util
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SAMPLES = ROOT / "samples"
CONFIG = ROOT / "config" / "practice.json"


def _load_module(name, relative):
    path = ROOT / relative
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


scope_ledger = _load_module("scope_ledger", "skills/scope-ledger/scripts/scope_ledger.py")
economics = _load_module("economics", "skills/engagement-economics/scripts/economics.py")
assemble = _load_module("assemble", "skills/proposal-assembler/scripts/assemble.py")
receivables = _load_module("receivables", "skills/receivables-tracker/scripts/receivables.py")


def sample(name):
    return json.loads((SAMPLES / name).read_text(encoding="utf-8"))


def practice():
    return json.loads(CONFIG.read_text(encoding="utf-8"))


class SelfChecks(unittest.TestCase):
    """Every skill script must prove itself."""

    def test_all_self_checks_pass(self):
        for module in (scope_ledger, economics, assemble, receivables):
            with self.subTest(module=module.__name__):
                self.assertEqual(module._self_check(), 0)


class Gate0Qualify(unittest.TestCase):

    def test_good_lead_passes(self):
        passed, failures, _ = scope_ledger.gate0(sample("lead_pass.json"), practice())
        self.assertTrue(passed, failures)

    def test_bad_lead_is_blocked(self):
        passed, failures, _ = scope_ledger.gate0(sample("lead_blocked.json"), practice())
        self.assertFalse(passed)
        checks = {f["check"] for f in failures}
        for expected in ("decision_maker", "budget_authority", "outcome_defined",
                         "rate_floor", "no_written_scope_wanted"):
            self.assertIn(expected, checks)

    def test_probe_tier_warns_without_blocking(self):
        lead = dict(sample("lead_pass.json"),
                    disqualifiers_observed=["prior_vendors_all_blamed"])
        passed, failures, warnings = scope_ledger.gate0(lead, practice())
        self.assertTrue(passed, failures)
        self.assertTrue(warnings)

    def test_unknown_budget_is_a_discovery_question_not_a_failure(self):
        lead = dict(sample("lead_pass.json"), indicative_budget=None,
                    indicative_days=None)
        passed, failures, _ = scope_ledger.gate0(lead, practice())
        self.assertTrue(passed, failures)

    def test_concentration_breach_blocks(self):
        lead = dict(sample("lead_pass.json"),
                    client_current_revenue_pct=35, client_added_revenue_pct=20)
        passed, failures, _ = scope_ledger.gate0(lead, practice())
        self.assertFalse(passed)
        self.assertIn("concentration", {f["check"] for f in failures})


class GateAPriceableScope(unittest.TestCase):

    def test_complete_scope_passes(self):
        passed, failures = scope_ledger.gateA(sample("engagement_priceable.json"))
        self.assertTrue(passed, failures)

    def test_vague_scope_is_blocked(self):
        passed, failures = scope_ledger.gateA(sample("engagement_vague.json"))
        self.assertFalse(passed)
        reasons = " ".join(f["reason"] for f in failures)
        self.assertIn("acceptance criterion", reasons)
        self.assertIn("exclusions", {f["check"] for f in failures})

    def test_every_required_section_is_enforced(self):
        for key in scope_ledger.REQUIRED_SCOPE_KEYS:
            with self.subTest(key=key):
                engagement = sample("engagement_priceable.json")
                engagement["scope"][key] = []
                passed, _ = scope_ledger.gateA(engagement)
                self.assertFalse(passed)

    def test_client_input_without_consequence_blocks(self):
        engagement = sample("engagement_priceable.json")
        engagement["scope"]["client_inputs"][0].pop("if_late")
        passed, failures = scope_ledger.gateA(engagement)
        self.assertFalse(passed)
        self.assertIn("consequence", " ".join(f["reason"] for f in failures))


class ScopeDrift(unittest.TestCase):

    def test_on_scope_delivery_does_not_drift(self):
        engagement = sample("engagement_priceable.json")
        delivered = {"items": [{"id": "D1", "name": "Pipeline assessment", "days": 12},
                               {"id": "D2", "name": "Prioritised remediation sequence",
                                "days": 4}]}
        self.assertEqual(scope_ledger.drift(engagement, delivered), [])

    def test_excluded_work_is_high_severity(self):
        findings = scope_ledger.drift(sample("engagement_priceable.json"),
                                      sample("delivered_drifted.json"))
        self.assertTrue(any(f["severity"] == "high" for f in findings), findings)
        self.assertTrue(any(f["item"] == "effort" for f in findings), findings)


class GateBSignatureRisk(unittest.TestCase):

    def test_clean_contract_passes(self):
        passed, findings = assemble.gateB(sample("engagement_priceable.json"))
        self.assertTrue(passed, findings)

    def test_bad_contract_is_blocked(self):
        passed, findings = assemble.gateB(sample("engagement_contract_blocked.json"))
        self.assertFalse(passed)
        flags = {f["flag"] for f in findings}
        for expected in ("unlimited_liability", "uncapped_ip_indemnity",
                         "unbounded_ip_assignment", "payment_terms_long",
                         "no_termination_compensation", "unilateral_scope_change",
                         "unilateral_set_off", "counsel_review"):
            self.assertIn(expected, flags)

    def test_acceptance_requires_a_recorded_rationale(self):
        engagement = sample("engagement_priceable.json")
        engagement["contract"]["payment_terms_days"] = 90

        engagement["contract"]["accepted_risks"] = [{"flag": "payment_terms_long"}]
        passed, _ = assemble.gateB(engagement)
        self.assertFalse(passed, "acceptance without a rationale must not unblock")

        engagement["contract"]["accepted_risks"] = [
            {"flag": "payment_terms_long", "rationale": "offset by a 40% deposit"}]
        passed, _ = assemble.gateB(engagement)
        self.assertTrue(passed)

    def test_missing_counsel_review_is_a_finding(self):
        engagement = sample("engagement_priceable.json")
        engagement["contract"]["counsel_reviewed"] = False
        passed, findings = assemble.gateB(engagement)
        self.assertFalse(passed)
        self.assertIn("counsel_review", {f["flag"] for f in findings})


class GateCCloseOut(unittest.TestCase):

    def test_complete_closeout_passes(self):
        passed, failures = economics.gateC(sample("closeout_complete.json"))
        self.assertTrue(passed, failures)

    def test_open_closeout_is_blocked(self):
        passed, failures = economics.gateC(sample("closeout_open.json"))
        self.assertFalse(passed)
        checks = {f["check"] for f in failures}
        for expected in ("final_invoice", "unbilled_effort", "case_study_consent",
                         "client_verdict"):
            self.assertIn(expected, checks)


class Economics(unittest.TestCase):

    def test_margin_is_a_divisor_not_a_multiplier(self):
        result = economics.rate_floor(practice())
        expected = result["walk_away_day_rate"] / (1 - practice()["target_margin"])
        self.assertAlmostEqual(result["floor_day_rate"], expected, places=1)

    def test_lower_utilization_raises_the_floor(self):
        sensitivity = economics.rate_floor(practice())["sensitivity"]
        self.assertGreater(sensitivity["0.5"], sensitivity["0.8"])

    def test_realised_rate_uses_collected_revenue_and_total_effort(self):
        closeout = sample("closeout_complete.json")
        result = economics.postcalc(closeout, practice())
        # 30000 invoiced - 1000 written off - 0 outstanding - 4000 costs = 25000
        self.assertEqual(result["collected_revenue"], 29000.0)
        self.assertEqual(result["net_revenue"], 25000.0)
        # 18 billed + 4 unbilled
        self.assertEqual(result["total_effort_days"], 22.0)
        self.assertIn("against_floor", result)

    def test_ignoring_unbilled_effort_flatters_the_rate(self):
        closeout = sample("closeout_complete.json")
        honest = economics.postcalc(closeout)["realised_day_rate"]
        closeout["effort"]["unbilled_days"] = 0
        flattered = economics.postcalc(closeout)["realised_day_rate"]
        self.assertGreater(flattered, honest)

    def test_outstanding_amounts_are_not_revenue(self):
        closeout = sample("closeout_complete.json")
        closeout["revenue"]["outstanding"] = 10000
        self.assertEqual(economics.postcalc(closeout)["collected_revenue"], 19000.0)

    def test_fixed_price_eligibility_needs_five_points(self):
        self.assertTrue(
            economics.estimate_series([1.1, 1.2, 1.0])["fixed_price_eligible"]
            .startswith("no"))

    def test_high_variance_blocks_fixed_price(self):
        wild = economics.estimate_series([1.0, 2.2, 0.6, 1.8, 0.7])
        self.assertTrue(wild["fixed_price_eligible"].startswith("no"), wild)


class ConfigConsistency(unittest.TestCase):
    """Stage 0 requires the stored walk-away rate to match the computed one.

    They are stored separately so Gate 0 can run without recomputing the floor,
    which means they can drift. This test is the thing that notices.
    """

    def test_stored_walk_away_matches_computed(self):
        config = practice()
        computed = economics.rate_floor(config)["walk_away_day_rate"]
        self.assertAlmostEqual(config["walk_away_day_rate"], computed, places=1)

    def test_practice_config_has_a_decline_tier_disqualifier(self):
        tiers = {d["tier"] for d in practice()["disqualifiers"]}
        self.assertIn("decline", tiers)


class Receivables(unittest.TestCase):

    def test_payment_run_pushes_cash_later_than_contractual_terms(self):
        result = receivables.schedule(sample("engagement_priceable.json"))
        self.assertTrue(any(row["slip_days"] > 0 for row in result["rows"]),
                        result["rows"])

    def test_not_yet_due_invoices_are_excluded_from_aging(self):
        aged = receivables.age(sample("ledger_overdue.json"))
        self.assertNotIn("INV-3", [row["invoice"] for row in aged["rows"]])

    def test_exposure_is_expressed_against_runway(self):
        aged = receivables.age(sample("ledger_overdue.json"))
        self.assertEqual(aged["total_overdue"], 20000.0)
        self.assertIsNotNone(aged["months_of_cost_covered"])
        self.assertEqual(aged["undiagnosed"], ["INV-4"])

    def test_a_dispute_is_never_escalated(self):
        decision = receivables.rung(sample("invoice_disputed.json"))
        self.assertEqual(decision["action"], "refuse")

    def test_an_undiagnosed_invoice_goes_back_to_triage(self):
        decision = receivables.rung({"cause": None, "days_overdue": 40})
        self.assertEqual(decision["action"], "diagnose")

    def test_a_rung_is_never_repeated(self):
        decision = receivables.rung({"cause": "administrative", "days_overdue": 20,
                                     "contact_history": [{"rung": 1}]})
        self.assertEqual(decision["rung"], 2)

    def test_suspension_is_not_proposed_without_the_right(self):
        history = [{"rung": 1}, {"rung": 2}, {"rung": 3}]
        decision = receivables.rung({"cause": "administrative", "days_overdue": 65,
                                     "contact_history": history,
                                     "suspension_right": False, "work_ongoing": True})
        self.assertEqual(decision["rung"], 6)

    def test_distress_compresses_the_triggers(self):
        history = [{"rung": 1}, {"rung": 2}]
        distressed = receivables.rung({"cause": "distress", "days_overdue": 16,
                                       "contact_history": history})
        steady = receivables.rung({"cause": "administrative", "days_overdue": 16,
                                   "contact_history": history})
        self.assertEqual(distressed["action"], "escalate")
        self.assertEqual(steady["action"], "wait")


class Rendering(unittest.TestCase):

    def test_render_is_deterministic_and_carries_the_sow_mapping(self):
        engagement = sample("engagement_priceable.json")
        first = assemble.render(engagement)
        self.assertEqual(first, assemble.render(engagement))
        self.assertIn("Proposal → SOW correspondence", first)
        self.assertIn("Acceptance criteria", first)
        self.assertIn("Not legal advice", first)

    def test_exclusions_appear_in_the_proposal_body(self):
        rendered = assemble.render(sample("engagement_priceable.json"))
        self.assertIn("What is not included", rendered)
        self.assertIn("implementation of the recommendations", rendered)


if __name__ == "__main__":
    unittest.main(verbosity=2)
