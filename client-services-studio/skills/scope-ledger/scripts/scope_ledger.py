#!/usr/bin/env python3
"""scope_ledger.py — the engagement record of truth, and the two gates in front of a price.

Not legal, tax, or accounting advice. This tool checks structure, not substance:
it can tell you a scope record is missing acceptance criteria; it cannot tell you
the criteria are good.

Gate 0 (qualify)  — refuse to proceed on a lead that fails the practice's
                    disqualifier rules.
Gate A (priceable)— refuse to price a scope that is not specified well enough to
                    be priced.
Change orders     — diff delivered work against agreed scope and name the drift.

Usage:
    python scope_ledger.py --gate0 lead.json --config practice.json
    python scope_ledger.py --gateA engagement.json
    python scope_ledger.py --drift engagement.json --delivered delivered.json
    python scope_ledger.py --self-check

Exit codes: 0 pass, 1 fail (gate blocked or drift found), 2 usage error.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

# --------------------------------------------------------------------------
# Gate 0 — qualify
# --------------------------------------------------------------------------

#: Checks applied to a lead record. Each is (key, predicate, message).
#: A lead must clear every one of these before discovery time is spent.
GATE0_CHECKS = (
    ("decision_maker",
     lambda lead, cfg: bool(lead.get("decision_maker")),
     "no named decision-maker"),
    ("budget_authority",
     lambda lead, cfg: lead.get("budget_authority") is True,
     "contact does not hold budget authority"),
    ("outcome_defined",
     lambda lead, cfg: lead.get("outcome_defined") is True,
     "desired outcome is not defined"),
    ("rate_floor",
     lambda lead, cfg: _clears_floor(lead, cfg),
     "indicative budget implies a rate below the practice floor"),
    ("concentration",
     lambda lead, cfg: _clears_concentration(lead, cfg),
     "would breach the client-concentration limit"),
)


def _clears_floor(lead, cfg):
    """True when the lead's implied day rate is at or above the walk-away rate.

    Unknown budget is not a failure — it is a question for discovery. Only a
    stated budget that implies a sub-floor rate blocks the gate.
    """
    budget = lead.get("indicative_budget")
    days = lead.get("indicative_days")
    floor = cfg.get("walk_away_day_rate")
    if budget in (None, 0) or not days or not floor:
        return True
    return (budget / days) >= floor


def _clears_concentration(lead, cfg):
    """True when taking this lead keeps the client below the concentration limit."""
    limit = cfg.get("concentration_limit_pct")
    current = lead.get("client_current_revenue_pct")
    added = lead.get("client_added_revenue_pct", 0)
    if limit is None or current is None:
        return True
    return (current + added) <= limit


def gate0(lead, config):
    """Return (passed, failures, warnings) for a lead record."""
    failures = []
    for key, predicate, message in GATE0_CHECKS:
        if not predicate(lead, config):
            failures.append({"check": key, "reason": message})

    # Named disqualifiers observed during first contact, from the practice config.
    observed = set(lead.get("disqualifiers_observed", []))
    declared = {d["id"]: d for d in config.get("disqualifiers", [])}
    warnings = []
    for signal in sorted(observed):
        rule = declared.get(signal)
        if rule is None:
            warnings.append({"check": signal, "reason": "signal not in practice config"})
        elif rule.get("tier") == "decline":
            failures.append({"check": signal, "reason": rule.get("reason", signal)})
        else:
            warnings.append({"check": signal,
                             "reason": f'{rule.get("tier", "probe")}: {rule.get("reason", signal)}'})

    return (not failures), failures, warnings


# --------------------------------------------------------------------------
# Gate A — priceable scope
# --------------------------------------------------------------------------

#: A scope record must carry all of these before a price may be quoted.
REQUIRED_SCOPE_KEYS = ("deliverables", "assumptions", "exclusions", "client_inputs")


def gateA(engagement):
    """Return (passed, failures) for an engagement's scope record.

    Refuses a price while the scope lacks deliverables with acceptance criteria,
    assumptions, exclusions, client inputs, or a named decision-maker.
    """
    failures = []
    scope = engagement.get("scope") or {}

    for key in REQUIRED_SCOPE_KEYS:
        value = scope.get(key)
        if not value:
            failures.append({"check": key, "reason": f"{key} is empty or absent"})

    for index, deliverable in enumerate(scope.get("deliverables") or []):
        label = deliverable.get("id") or deliverable.get("name") or f"#{index + 1}"
        if not deliverable.get("name"):
            failures.append({"check": f"deliverable[{label}]", "reason": "no name"})
        if not deliverable.get("format"):
            failures.append({"check": f"deliverable[{label}]", "reason": "no format"})
        if not deliverable.get("acceptance"):
            failures.append({"check": f"deliverable[{label}]",
                             "reason": "no acceptance criterion — cannot be judged complete"})

    for index, item in enumerate(scope.get("client_inputs") or []):
        label = item.get("input") or f"#{index + 1}"
        if not item.get("owner"):
            failures.append({"check": f"client_input[{label}]", "reason": "no named owner"})
        if not item.get("due"):
            failures.append({"check": f"client_input[{label}]", "reason": "no due date"})
        if not item.get("if_late"):
            failures.append({"check": f"client_input[{label}]",
                             "reason": "no stated consequence if late"})

    if not (engagement.get("lead") or {}).get("decision_maker"):
        failures.append({"check": "decision_maker", "reason": "no named decision-maker"})

    return (not failures), failures


# --------------------------------------------------------------------------
# Change-order drift
# --------------------------------------------------------------------------

def drift(engagement, delivered):
    """Compare delivered work against agreed scope.

    Returns a list of drift findings. Work delivered that is not an agreed
    deliverable, and is not on the exclusion list, is a change-order trigger.
    Work on the exclusion list is a harder finding: it was explicitly out.
    """
    scope = engagement.get("scope") or {}
    agreed = {d.get("id") for d in (scope.get("deliverables") or []) if d.get("id")}
    excluded = {e.lower() for e in (scope.get("exclusions") or [])}

    findings = []
    for item in delivered.get("items") or []:
        item_id = item.get("id")
        name = item.get("name", item_id or "unnamed")
        if item_id in agreed:
            continue
        if name.lower() in excluded:
            findings.append({
                "item": name,
                "severity": "high",
                "reason": "delivered work appears on the exclusion list",
                "action": "raise a change order before any further work",
            })
        else:
            findings.append({
                "item": name,
                "severity": "medium",
                "reason": "delivered work is not an agreed deliverable",
                "action": "raise a change order",
            })

    agreed_effort = sum(d.get("estimated_days", 0)
                        for d in (scope.get("deliverables") or []))
    actual_effort = sum(i.get("days", 0) for i in (delivered.get("items") or []))
    if agreed_effort and actual_effort > agreed_effort * 1.15:
        findings.append({
            "item": "effort",
            "severity": "medium",
            "reason": (f"effort {actual_effort} exceeds agreed {agreed_effort} "
                       f"by more than 15%"),
            "action": "review scope before continuing",
        })

    return findings


# --------------------------------------------------------------------------
# CLI plumbing
# --------------------------------------------------------------------------

def _load(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def _report(title, passed, failures, warnings=()):
    print(f"{title}: {'PASS' if passed else 'BLOCKED'}")
    for failure in failures:
        print(f"  FAIL  {failure['check']}: {failure['reason']}")
    for warning in warnings:
        print(f"  WARN  {warning['check']}: {warning['reason']}")
    return 0 if passed else 1


def _self_check():
    """Prove both gates and drift detection on planted fixtures."""
    config = {
        "walk_away_day_rate": 500,
        "concentration_limit_pct": 40,
        "disqualifiers": [
            {"id": "prior_vendors_all_blamed", "tier": "probe",
             "reason": "three prior suppliers described as incompetent"},
            {"id": "no_written_scope_wanted", "tier": "decline",
             "reason": "pressure to skip a written scope"},
        ],
    }

    good_lead = {"decision_maker": "A. Patel", "budget_authority": True,
                 "outcome_defined": True, "indicative_budget": 30000,
                 "indicative_days": 20}
    passed, failures, _ = gate0(good_lead, config)
    assert passed, f"good lead should pass Gate 0: {failures}"

    for mutation, expected in (
        ({"decision_maker": None}, "decision_maker"),
        ({"budget_authority": False}, "budget_authority"),
        ({"outcome_defined": False}, "outcome_defined"),
        ({"indicative_budget": 5000}, "rate_floor"),
    ):
        lead = dict(good_lead, **mutation)
        passed, failures, _ = gate0(lead, config)
        assert not passed, f"Gate 0 should block {mutation}"
        assert any(f["check"] == expected for f in failures), \
            f"expected {expected} in {failures}"

    lead = dict(good_lead, disqualifiers_observed=["no_written_scope_wanted"])
    passed, failures, _ = gate0(lead, config)
    assert not passed, "a decline-tier disqualifier must block Gate 0"

    lead = dict(good_lead, disqualifiers_observed=["prior_vendors_all_blamed"])
    passed, _, warnings = gate0(lead, config)
    assert passed and warnings, "a probe-tier disqualifier must warn, not block"

    lead = dict(good_lead, client_current_revenue_pct=35, client_added_revenue_pct=20)
    passed, failures, _ = gate0(lead, config)
    assert not passed and any(f["check"] == "concentration" for f in failures), \
        "concentration breach must block Gate 0"

    lead = dict(good_lead, indicative_budget=None, indicative_days=None)
    passed, _, _ = gate0(lead, config)
    assert passed, "unknown budget is a discovery question, not a Gate 0 failure"

    priceable = {
        "lead": {"decision_maker": "A. Patel"},
        "scope": {
            "deliverables": [{"id": "D1", "name": "Pipeline assessment",
                              "format": "written report",
                              "acceptance": "covers the seven named pipelines",
                              "estimated_days": 10}],
            "assumptions": ["read access granted in week 1"],
            "exclusions": ["implementation of the recommendations"],
            "client_inputs": [{"input": "read access", "owner": "A. Patel",
                               "due": "2026-10-01", "if_late": "clock continues"}],
        },
    }
    passed, failures = gateA(priceable)
    assert passed, f"complete scope should pass Gate A: {failures}"

    vague = json.loads(json.dumps(priceable))
    vague["scope"]["deliverables"][0].pop("acceptance")
    passed, failures = gateA(vague)
    assert not passed, "Gate A must block a deliverable with no acceptance criterion"

    for key in REQUIRED_SCOPE_KEYS:
        stripped = json.loads(json.dumps(priceable))
        stripped["scope"][key] = []
        passed, failures = gateA(stripped)
        assert not passed, f"Gate A must block when {key} is empty"

    no_consequence = json.loads(json.dumps(priceable))
    no_consequence["scope"]["client_inputs"][0].pop("if_late")
    passed, _ = gateA(no_consequence)
    assert not passed, "Gate A must block an input with no consequence for lateness"

    findings = drift(priceable, {"items": [{"id": "D1", "name": "Pipeline assessment",
                                            "days": 10}]})
    assert findings == [], f"on-scope delivery should not drift: {findings}"

    findings = drift(priceable, {"items": [
        {"id": "D1", "name": "Pipeline assessment", "days": 10},
        {"id": "X1", "name": "Implementation of the recommendations", "days": 6},
    ]})
    assert any(f["severity"] == "high" for f in findings), \
        "delivering an excluded item must be a high-severity finding"

    findings = drift(priceable, {"items": [{"id": "D1", "name": "Pipeline assessment",
                                            "days": 14}]})
    assert any(f["item"] == "effort" for f in findings), \
        "effort overrun beyond 15% must be flagged"

    print("scope_ledger.py self-check: PASS")
    return 0


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--gate0", metavar="LEAD_JSON")
    parser.add_argument("--config", metavar="PRACTICE_JSON")
    parser.add_argument("--gateA", metavar="ENGAGEMENT_JSON")
    parser.add_argument("--drift", metavar="ENGAGEMENT_JSON")
    parser.add_argument("--delivered", metavar="DELIVERED_JSON")
    parser.add_argument("--self-check", action="store_true")
    args = parser.parse_args(argv)

    if args.self_check:
        return _self_check()

    if args.gate0:
        if not args.config:
            parser.error("--gate0 requires --config")
        passed, failures, warnings = gate0(_load(args.gate0), _load(args.config))
        return _report("Gate 0 (qualify)", passed, failures, warnings)

    if args.gateA:
        passed, failures = gateA(_load(args.gateA))
        return _report("Gate A (priceable scope)", passed, failures)

    if args.drift:
        if not args.delivered:
            parser.error("--drift requires --delivered")
        findings = drift(_load(args.drift), _load(args.delivered))
        print(f"Scope drift: {len(findings)} finding(s)")
        for finding in findings:
            print(f"  {finding['severity'].upper():6} {finding['item']}: "
                  f"{finding['reason']} → {finding['action']}")
        return 1 if findings else 0

    parser.error("provide --gate0, --gateA, --drift, or --self-check")


if __name__ == "__main__":
    sys.exit(main())
