#!/usr/bin/env python3
"""economics.py — rate floor, engagement margin post-calculation, and Gate C.

Not tax, accounting, or financial advice. Employment-burden rates, deductibility
and entity treatment are jurisdiction-specific; these are arithmetic, not counsel.

    rate floor   — derive walk-away / floor / standard day rates from the cost of
                   delivery and a utilization assumption.
    post-calc    — realised effective rate for a completed engagement, using
                   COLLECTED revenue and TOTAL effort (billed plus unbilled).
    Gate C       — refuse close-out until the engagement is actually closed.

Usage:
    python economics.py --floor practice.json
    python economics.py --postcalc closeout.json --config practice.json
    python economics.py --gateC closeout.json
    python economics.py --self-check

Exit codes: 0 pass, 1 fail (gate blocked), 2 usage error.
"""

from __future__ import annotations

import argparse
import json
import statistics
import sys
from pathlib import Path


# --------------------------------------------------------------------------
# Rate floor
# --------------------------------------------------------------------------

def rate_floor(practice):
    """Compute walk-away, floor and standard day rates from the cost base.

    Margin is applied as a divisor -- cost is (1 - margin) of price. Multiplying
    cost by (1 + margin) is the common error and understates the rate.
    """
    costs = practice["costs"]
    total_cost = (
        costs["fixed_business"]
        + costs["target_income"]
        + costs["target_income"] * costs["employment_burden_rate"]
        + costs.get("pension_and_healthcare", 0)
    )

    capacity = practice["capacity"]
    present_days = capacity["working_days"] - capacity["absence_days"]
    billable_days = present_days * capacity["billable_fraction"]
    if billable_days <= 0:
        raise ValueError("billable days must be positive")

    breakeven = total_cost / billable_days

    risk = practice.get("risk", {})
    bad_debt = risk.get("bad_debt_rate", 0.0)
    overrun = risk.get("typical_overrun", 0.0)
    if not 0 <= bad_debt < 1:
        raise ValueError("bad_debt_rate must be in [0, 1)")
    walk_away = breakeven / ((1 - bad_debt) * (1 + overrun))

    margin = practice.get("target_margin", 0.0)
    if not 0 <= margin < 1:
        raise ValueError("target_margin must be in [0, 1)")
    floor = walk_away / (1 - margin)

    premium = practice.get("positioning_premium", 0.0)
    standard = floor * (1 + premium)

    hours = capacity.get("billable_hours_per_day", 8)

    return {
        "total_cost": round(total_cost, 2),
        "present_days": round(present_days, 2),
        "billable_days": round(billable_days, 2),
        "breakeven_day_rate": round(breakeven, 2),
        "walk_away_day_rate": round(walk_away, 2),
        "floor_day_rate": round(floor, 2),
        "standard_day_rate": round(standard, 2),
        "floor_hourly_rate": round(floor / hours, 2),
        "sensitivity": {
            str(u): round(
                (total_cost / (present_days * u))
                / ((1 - bad_debt) * (1 + overrun))
                / (1 - margin), 2)
            for u in (0.50, 0.60, 0.70, 0.80)
        },
    }


# --------------------------------------------------------------------------
# Engagement post-calculation
# --------------------------------------------------------------------------

def postcalc(closeout, practice=None):
    """Realised economics for a completed engagement.

    Revenue is COLLECTED, not invoiced: write-offs and outstanding amounts are
    excluded rather than assumed. Effort is TOTAL, billed plus unbilled --
    excluding unbilled effort reports the rate you wished you had earned.
    """
    revenue = closeout["revenue"]
    collected = (
        revenue["invoiced"]
        - revenue.get("write_offs", 0)
        - revenue.get("outstanding", 0)
    )
    direct_costs = sum(closeout.get("direct_costs", {}).values())
    net_revenue = collected - direct_costs

    effort = closeout["effort"]
    total_effort = effort["billed_days"] + effort.get("unbilled_days", 0)
    if total_effort <= 0:
        raise ValueError("total effort must be positive")

    realised_rate = net_revenue / total_effort

    estimated = effort.get("estimated_days")
    ratio = (total_effort / estimated) if estimated else None

    result = {
        "collected_revenue": round(collected, 2),
        "direct_costs": round(direct_costs, 2),
        "net_revenue": round(net_revenue, 2),
        "total_effort_days": round(total_effort, 2),
        "realised_day_rate": round(realised_rate, 2),
        "estimate_ratio": round(ratio, 3) if ratio else None,
    }

    if practice:
        thresholds = rate_floor(practice)
        result["against_floor"] = _place(realised_rate, thresholds)
        result["thresholds"] = {
            "walk_away": thresholds["walk_away_day_rate"],
            "floor": thresholds["floor_day_rate"],
            "standard": thresholds["standard_day_rate"],
        }

    return result


def _place(rate, thresholds):
    if rate >= thresholds["standard_day_rate"]:
        return "at or above standard"
    if rate >= thresholds["floor_day_rate"]:
        return "above floor"
    if rate >= thresholds["walk_away_day_rate"]:
        return "between walk-away and floor"
    return "below walk-away"


def estimate_series(ratios):
    """Summarise an estimate-error series and rule on fixed-price eligibility.

    Fewer than five data points is itself a 'do not fix a price' verdict: the
    coefficient of variation is not yet meaningful.
    """
    ratios = [r for r in ratios if r]
    if len(ratios) < 5:
        return {"n": len(ratios), "cv": None,
                "fixed_price_eligible": "no — fewer than five data points"}
    mean = statistics.fmean(ratios)
    cv = statistics.pstdev(ratios) / mean if mean else None
    if cv is None:
        verdict = "no — cannot compute"
    elif cv < 0.25:
        verdict = "yes"
    elif cv <= 0.40:
        verdict = "with a tight input contract"
    else:
        verdict = "no — variance too high"
    return {
        "n": len(ratios),
        "median": round(statistics.median(ratios), 3),
        "min": round(min(ratios), 3),
        "max": round(max(ratios), 3),
        "cv": round(cv, 3) if cv is not None else None,
        "fixed_price_eligible": verdict,
    }


# --------------------------------------------------------------------------
# Gate C — close-out complete
# --------------------------------------------------------------------------

def gateC(closeout):
    """Refuse close-out until the engagement is genuinely closed."""
    failures = []
    revenue = closeout.get("revenue") or {}

    if revenue.get("outstanding", 0) > 0 and not revenue.get("outstanding_written_off"):
        failures.append({
            "check": "final_invoice",
            "reason": (f'{revenue["outstanding"]} still outstanding and not written '
                       f"off — the engagement is not closed"),
        })

    effort = closeout.get("effort") or {}
    if "unbilled_days" not in effort:
        failures.append({"check": "unbilled_effort",
                         "reason": "unbilled effort not recorded — margin cannot be computed"})
    if not effort.get("estimated_days"):
        failures.append({"check": "estimate",
                         "reason": "original estimate not recorded — estimate error cannot be updated"})

    if not closeout.get("case_study_consent"):
        failures.append({"check": "case_study_consent",
                         "reason": "case-study consent not recorded (grant, decline, or not-asked)"})

    if not closeout.get("client_verdict"):
        failures.append({"check": "client_verdict",
                         "reason": "no repeat/decline verdict — disqualifier list cannot be updated"})

    return (not failures), failures


# --------------------------------------------------------------------------
# CLI plumbing
# --------------------------------------------------------------------------

def _load(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def _self_check():
    practice = {
        "costs": {
            "fixed_business": 12000,
            "target_income": 80000,
            "employment_burden_rate": 0.15,
            "pension_and_healthcare": 8000,
        },
        "capacity": {
            "working_days": 250,
            "absence_days": 30,
            "billable_fraction": 0.60,
            "billable_hours_per_day": 8,
        },
        "risk": {"bad_debt_rate": 0.02, "typical_overrun": 0.10},
        "target_margin": 0.20,
        "positioning_premium": 0.15,
    }

    floor = rate_floor(practice)
    assert floor["billable_days"] == 132.0, floor["billable_days"]
    # 12000 + 80000 + 12000 + 8000 = 112000
    assert floor["total_cost"] == 112000.0, floor["total_cost"]
    assert abs(floor["breakeven_day_rate"] - 848.48) < 0.5, floor["breakeven_day_rate"]
    assert floor["walk_away_day_rate"] < floor["floor_day_rate"] < floor["standard_day_rate"]

    # Margin as a divisor, not a multiplier.
    assert abs(floor["floor_day_rate"] - floor["walk_away_day_rate"] / 0.80) < 0.01

    # Lower utilization must raise the floor.
    assert floor["sensitivity"]["0.5"] > floor["sensitivity"]["0.8"], floor["sensitivity"]

    try:
        rate_floor(dict(practice, target_margin=1.0))
    except ValueError:
        pass
    else:
        raise AssertionError("a margin of 1.0 must be rejected")

    closeout = {
        "revenue": {"invoiced": 30000, "write_offs": 1000, "outstanding": 0},
        "direct_costs": {"subcontractor": 4000},
        "effort": {"estimated_days": 20, "billed_days": 22, "unbilled_days": 4},
        "case_study_consent": "declined",
        "client_verdict": "repeat",
    }
    result = postcalc(closeout, practice)
    assert result["collected_revenue"] == 29000.0
    assert result["net_revenue"] == 25000.0
    assert result["total_effort_days"] == 26.0
    assert abs(result["realised_day_rate"] - 961.54) < 0.5, result["realised_day_rate"]
    assert result["estimate_ratio"] == 1.3
    assert "against_floor" in result

    # Unbilled effort must lower the realised rate.
    billed_only = json.loads(json.dumps(closeout))
    billed_only["effort"]["unbilled_days"] = 0
    assert postcalc(billed_only)["realised_day_rate"] > result["realised_day_rate"], \
        "ignoring unbilled effort must flatter the rate"

    # Outstanding amounts must not count as revenue.
    unpaid = json.loads(json.dumps(closeout))
    unpaid["revenue"]["outstanding"] = 10000
    assert postcalc(unpaid)["collected_revenue"] == 19000.0

    passed, failures = gateC(closeout)
    assert passed, f"a complete close-out should pass Gate C: {failures}"

    for mutation, expected in (
        ({"revenue": dict(closeout["revenue"], outstanding=5000)}, "final_invoice"),
        ({"case_study_consent": None}, "case_study_consent"),
        ({"client_verdict": None}, "client_verdict"),
    ):
        broken = dict(json.loads(json.dumps(closeout)), **mutation)
        passed, failures = gateC(broken)
        assert not passed and any(f["check"] == expected for f in failures), \
            f"Gate C should block {expected}: {failures}"

    no_unbilled = json.loads(json.dumps(closeout))
    no_unbilled["effort"].pop("unbilled_days")
    passed, failures = gateC(no_unbilled)
    assert not passed and any(f["check"] == "unbilled_effort" for f in failures)

    assert estimate_series([1.1, 1.2])["fixed_price_eligible"].startswith("no")
    tight = estimate_series([1.0, 1.05, 1.1, 0.95, 1.02])
    assert tight["fixed_price_eligible"] == "yes", tight
    wild = estimate_series([1.0, 2.2, 0.6, 1.8, 0.7])
    assert wild["fixed_price_eligible"].startswith("no"), wild

    print("economics.py self-check: PASS")
    return 0


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--floor", metavar="PRACTICE_JSON")
    parser.add_argument("--postcalc", metavar="CLOSEOUT_JSON")
    parser.add_argument("--gateC", metavar="CLOSEOUT_JSON")
    parser.add_argument("--config", metavar="PRACTICE_JSON")
    parser.add_argument("--self-check", action="store_true")
    args = parser.parse_args(argv)

    if args.self_check:
        return _self_check()

    if args.floor:
        print(json.dumps(rate_floor(_load(args.floor)), indent=2))
        return 0

    if args.postcalc:
        practice = _load(args.config) if args.config else None
        print(json.dumps(postcalc(_load(args.postcalc), practice), indent=2))
        return 0

    if args.gateC:
        passed, failures = gateC(_load(args.gateC))
        print(f"Gate C (close-out complete): {'PASS' if passed else 'BLOCKED'}")
        for failure in failures:
            print(f"  FAIL  {failure['check']}: {failure['reason']}")
        return 0 if passed else 1

    parser.error("provide --floor, --postcalc, --gateC, or --self-check")


if __name__ == "__main__":
    sys.exit(main())
