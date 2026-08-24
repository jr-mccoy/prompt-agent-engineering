#!/usr/bin/env python3
"""test_hardening.py — prove the hardening guards added after the failure-mode pass.

For informational and research purposes only. Not financial, investment, or tax advice.
Nothing here places real-money trades.

Mirrors tests/test_gates.py. Covers the code guards that close the top code-uncovered
residuals in FAILURE_MODES.md:
  F12/F13 — journal tamper-evidence + resolution honesty (journal_integrity.py), folded
            into Gate C so a tampered/unverifiable journal can never report unlock_ready.
  F18     — INDEX/record reconciliation (validate_pattern.reconcile_index).
  Leakage audit §A/§E — non-blocking advisory warnings on a pattern record.

    python -m unittest discover -s tests -v
"""

import importlib.util
import os
import sys
import tempfile
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SAMPLES = os.path.join(ROOT, "samples")


def _load(rel_path, name):
    spec = importlib.util.spec_from_file_location(name, os.path.join(ROOT, rel_path))
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


ji = _load("skills/prediction-journal/scripts/journal_integrity.py", "ji_h")
score_brier = _load("skills/prediction-journal/scripts/score_brier.py", "sb_h")
validate_pattern = _load("skills/pattern-knowledge-base/scripts/validate_pattern.py", "vp_h")


_PRED = """---
id: {id}
date_opened: "2026-03-01"
asset: "EXMP"
direction: long
probability: {p}
thesis_ref: "data/output/dossiers/EXMP.md"
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


def _write_pred(tmp, name, **kw):
    d = dict(id="PRED-0100", p="0.60", resolution="null")
    d.update(kw)
    path = os.path.join(tmp, name)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(_PRED.format(**d))
    return path


_PATTERN = """---
id: {id}
title: "fixture"
status: {status}
asset_classes: [equity]
hypothesis: "signal predicts outcome"
registered_on: "2026-01-01"
feature_definition: "precise"
sample_frame: {sample_frame}
base_rate: "0.30"
in_sample_result: {{ n: 120, lift_vs_base_rate: 0.18 }}
out_of_sample_result: {{ n: 60, lift_vs_base_rate: 0.12 }}
multiple_comparisons_note: {mcn}
decay_estimate: "12 months"
capacity_note: "survives costs"
confidence: medium
last_reviewed: "2026-06-19"
linked_predictions: []
---
## Notes
fixture
"""


class JournalIntegrity(unittest.TestCase):
    def test_self_check(self):
        self.assertEqual(ji._self_check(), 0)

    def test_sample_journal_is_clean(self):
        rep = ji.verify(os.path.join(SAMPLES, "journal"))
        self.assertTrue(rep["clean"], rep["issues"])
        self.assertEqual(rep["counts"]["resolved"], 3)
        self.assertEqual(rep["counts"]["tampered"], 0)

    def test_edited_probability_is_tamper(self):
        with tempfile.TemporaryDirectory() as tmp:
            p = _write_pred(tmp, "PRED-0100.md", id="PRED-0100", p="0.60")
            ji.stamp(p)
            with open(p, encoding="utf-8") as fh:
                txt = fh.read().replace("probability: 0.60", "probability: 0.95")
            with open(p, "w", encoding="utf-8") as fh:
                fh.write(txt)
            rep = ji.verify(tmp)
            self.assertFalse(rep["clean"])
            self.assertEqual(rep["counts"]["tampered"], 1)


class GateCIntegrity(unittest.TestCase):
    def test_score_brier_self_check(self):
        self.assertEqual(score_brier._self_check(), 0)

    def test_clean_sample_journal_integrity_clean_but_count_unmet(self):
        rep = score_brier.calibration_report(os.path.join(SAMPLES, "journal"))
        self.assertIn("integrity", rep)
        self.assertTrue(rep["gate_c"]["integrity_clean"])
        self.assertFalse(rep["gate_c"]["meets_count"])      # 3 < 100
        self.assertFalse(rep["gate_c"]["unlock_ready"])     # count alone blocks

    def test_unverifiable_journal_blocks_integrity(self):
        with tempfile.TemporaryDirectory() as tmp:
            # Resolved record with no lock_hash -> unverifiable -> integrity not clean.
            _write_pred(tmp, "PRED-0101.md", id="PRED-0101", p="0.6",
                        resolution='{ outcome: hit, realized_return: 0.2, resolved_on: "2026-06-10" }')
            rep = score_brier.calibration_report(tmp)
            self.assertEqual(rep["n"], 1)
            self.assertFalse(rep["gate_c"]["integrity_clean"])
            self.assertFalse(rep["gate_c"]["unlock_ready"])


class PatternReconcileAndWarnings(unittest.TestCase):
    def test_reconcile_detects_status_drift(self):
        with tempfile.TemporaryDirectory() as tmp:
            pdir = os.path.join(tmp, "patterns")
            os.makedirs(pdir)
            with open(os.path.join(pdir, "PATTERN-0001.md"), "w", encoding="utf-8") as fh:
                fh.write(_PATTERN.format(id="PATTERN-0001", status="validated",
                                         sample_frame='"point-in-time universe"',
                                         mcn='"screened 3"'))
            idx = os.path.join(tmp, "INDEX.md")
            with open(idx, "w", encoding="utf-8") as fh:
                fh.write("| id | title | status | confidence |\n|---|---|---|---|\n"
                         "| PATTERN-0001 | t | retired | medium |\n")
            rep = validate_pattern.reconcile_index(pdir, idx)
            self.assertEqual(rep["status"], "FAIL")
            self.assertTrue(rep["mismatches"])

    def test_reconcile_clean_when_aligned(self):
        with tempfile.TemporaryDirectory() as tmp:
            pdir = os.path.join(tmp, "patterns")
            os.makedirs(pdir)
            with open(os.path.join(pdir, "PATTERN-0002.md"), "w", encoding="utf-8") as fh:
                fh.write(_PATTERN.format(id="PATTERN-0002", status="validated",
                                         sample_frame='"point-in-time universe"',
                                         mcn='"screened 3"'))
            idx = os.path.join(tmp, "INDEX.md")
            with open(idx, "w", encoding="utf-8") as fh:
                fh.write("| id | title | status | confidence |\n|---|---|---|---|\n"
                         "| PATTERN-0002 | t | validated | medium |\n")
            self.assertEqual(validate_pattern.reconcile_index(pdir, idx)["status"], "PASS")

    def test_advisory_warnings_do_not_change_pass(self):
        with tempfile.TemporaryDirectory() as tmp:
            # validated + clears OOS, but mined from many features and no point-in-time language.
            p = os.path.join(tmp, "PATTERN-0003.md")
            with open(p, "w", encoding="utf-8") as fh:
                fh.write(_PATTERN.format(id="PATTERN-0003", status="validated",
                                         sample_frame='"currently listed names only"',
                                         mcn='"screened 250 features"'))
            r = validate_pattern.validate_pattern(p, 30)
            self.assertEqual(r["status"], "PASS")          # advisories never block
            self.assertEqual(len(r["warnings"]), 2)        # both advisories fire


if __name__ == "__main__":
    unittest.main(verbosity=2)
