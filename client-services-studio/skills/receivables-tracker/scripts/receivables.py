#!/usr/bin/env python3
"""receivables.py — invoice schedule, AR aging, cause triage, and the escalation rung.

Not legal, tax, or accounting advice. Escalation rungs 6 and 7 involve formal
notice and legal process; take advice before either. Interest entitlement,
suspension rights and limitation periods are jurisdiction-specific.

    schedule   — build an invoice schedule from a SOW's payment milestones,
                 projecting cash dates from the CLIENT'S PAYMENT RUN rather than
                 from contractual terms.
    age        — bucket overdue invoices and compute exposure against runway.
    rung       — given a cause and a contact history, name the next escalation
                 rung. Never repeats a rung; refuses to escalate a dispute.

Usage:
    python receivables.py --schedule engagement.json
    python receivables.py --age ledger.json
    python receivables.py --rung invoice.json
    python receivables.py --self-check

Exit codes: 0 clean, 1 action required, 2 usage error.
"""

from __future__ import annotations

import argparse
import json
import sys
from datetime import date, timedelta
from pathlib import Path

#: Aging buckets, in days overdue.
BUCKETS = ((1, 30), (31, 60), (61, 90), (91, None))

#: The escalation ladder. One rung at a time; never repeated.
LADDER = (
    (1, "AP confirmation", 3,
     "Direct contact with accounts payable. Confirm receipt, approval, PO validity, "
     "and which payment run it is in.", "none"),
    (2, "Written follow-up with evidence", 14,
     "Email to AP, sponsor copied, re-attaching the invoice and its evidence pack. "
     "Ask one direct question: is anything preventing payment?", "negligible"),
    (3, "Sponsor escalation", 30,
     "Direct to the sponsor who wanted the work. Frame as help unblocking an "
     "internal process. Name the specific help required.", "low"),
    (4, "Notice of suspension", 45,
     "Written notice that work pauses on a stated date unless payment is received. "
     "Only issue if the contractual right exists and you will execute it.", "material"),
    (5, "Suspension, executed", 52,
     "Stop. Confirm in writing, neutrally, with what is required to resume.", "high"),
    (6, "Formal notice before action", 60,
     "Formal letter stating the debt, contractual basis, interest claimed, final "
     "deadline and intended next step. Take legal advice first.", "relationship ends"),
    (7, "Handoff", 75,
     "Demand letter, collections agency, or a recorded commercial write-off.",
     "relationship ended"),
)

#: The four causes an overdue invoice can have. Each has a different remedy.
CAUSES = {
    "administrative": "Fix the document or the route. Usually one call to AP.",
    "dispute": "Resolve the substance. Collect the undisputed portion separately.",
    "distress": "Move fast, rank early, get a written payment plan.",
    "refusal": "Legal path. Stop work; preserve evidence.",
}


def schedule(engagement):
    """Project cash dates from the client's payment run, not contractual terms.

    Net-30 is a ceiling on the client's obligation, not a prediction. The date
    that matters is the first payment run after the approval window closes.
    """
    commercial = engagement.get("commercial") or {}
    machinery = engagement.get("payment_machinery") or {}
    terms_days = machinery.get("terms_days", 30)
    approval_days = machinery.get("approval_window_days", 0)
    run_day = machinery.get("payment_run_day_of_month")
    cutoff_days = machinery.get("cutoff_days_before_run", 0)

    rows = []
    for payment in commercial.get("payment_schedule") or []:
        issue = _parse(payment.get("issue_date"))
        if issue is None:
            rows.append({"label": payment.get("label"), "amount": payment.get("amount"),
                         "trigger": payment.get("trigger"),
                         "issue_date": None, "expected_receipt": None,
                         "note": "no issue date — trigger not yet dated"})
            continue
        due = issue + timedelta(days=terms_days + approval_days)
        expected = _next_run(due, run_day, cutoff_days) if run_day else due
        rows.append({
            "label": payment.get("label"),
            "amount": payment.get("amount"),
            "trigger": payment.get("trigger"),
            "issue_date": issue.isoformat(),
            "contractual_due": due.isoformat(),
            "expected_receipt": expected.isoformat(),
            "slip_days": (expected - due).days,
        })

    total = sum(r["amount"] for r in rows if r.get("amount"))
    final = rows[-1]["amount"] if rows and rows[-1].get("amount") else 0
    deposit = rows[0]["amount"] if rows and rows[0].get("amount") else 0

    warnings = []
    if total and final / total > 0.25:
        warnings.append(
            f"final payment is {final / total:.0%} of total — above 25%, and it falls "
            f"due when your leverage is lowest")
    if total and deposit == 0:
        warnings.append("no deposit — all delivery risk is carried before any cash arrives")
    if not machinery.get("po_number") and machinery.get("po_required"):
        warnings.append("PO required but no PO number recorded — invoices reject silently at intake")

    return {"rows": rows, "total": total, "warnings": warnings}


def _parse(value):
    return date.fromisoformat(value) if value else None


def _next_run(due, run_day, cutoff_days):
    """First payment run on or after `due`, respecting the submission cut-off."""
    candidate = _run_in_month(due.year, due.month, run_day)
    if candidate - timedelta(days=cutoff_days) < due:
        year = due.year + (due.month // 12)
        month = due.month % 12 + 1
        candidate = _run_in_month(year, month, run_day)
    return candidate


def _run_in_month(year, month, run_day):
    if month == 12:
        last = date(year + 1, 1, 1) - timedelta(days=1)
    else:
        last = date(year, month + 1, 1) - timedelta(days=1)
    return date(year, month, min(run_day, last.day))


def age(ledger):
    """Bucket overdue invoices and express exposure against the practice's runway."""
    as_of = _parse(ledger.get("as_of")) or date.today()
    buckets = {f"{lo}-{hi or '+'}": {"count": 0, "amount": 0.0} for lo, hi in BUCKETS}
    rows = []

    for invoice in ledger.get("invoices") or []:
        due = _parse(invoice.get("due_date"))
        if due is None:
            continue
        overdue = (as_of - due).days
        if overdue < 1:
            continue
        key = next(f"{lo}-{hi or '+'}" for lo, hi in BUCKETS
                   if overdue >= lo and (hi is None or overdue <= hi))
        amount = invoice.get("amount", 0)
        buckets[key]["count"] += 1
        buckets[key]["amount"] += amount
        cause = invoice.get("cause")
        rows.append({
            "invoice": invoice.get("id"),
            "client": invoice.get("client"),
            "amount": amount,
            "days_overdue": overdue,
            "bucket": key,
            "cause": cause,
            "remedy": CAUSES.get(cause, "undiagnosed — call AP before escalating"),
        })

    total = sum(b["amount"] for b in buckets.values())
    monthly_cost = ledger.get("monthly_cost")
    by_client = {}
    for row in rows:
        by_client[row["client"]] = by_client.get(row["client"], 0) + row["amount"]

    return {
        "as_of": as_of.isoformat(),
        "buckets": buckets,
        "rows": sorted(rows, key=lambda r: -r["days_overdue"]),
        "total_overdue": round(total, 2),
        "largest_single": max((r["amount"] for r in rows), default=0),
        "largest_client_exposure": max(by_client.items(), key=lambda kv: kv[1],
                                       default=(None, 0)),
        "months_of_cost_covered": round(total / monthly_cost, 2) if monthly_cost else None,
        "undiagnosed": [r["invoice"] for r in rows if not r["cause"]],
    }


def rung(invoice):
    """Name the next escalation rung, or refuse.

    Rules enforced here: a dispute is never escalated; a rung fires only when its
    trigger is met; a rung is never repeated; suspension is not proposed where
    there is no contractual right or no ongoing work.
    """
    cause = invoice.get("cause")
    if cause == "dispute":
        return {"action": "refuse",
                "reason": "cause is dispute — resolve the substance before escalating; "
                          "escalation hardens the position and stalls the undisputed portion"}
    if not cause:
        return {"action": "diagnose",
                "reason": "cause not established — run aging triage first; roughly half "
                          "of overdue services invoices are administrative"}

    history = invoice.get("contact_history") or []
    highest = max((entry.get("rung", 0) for entry in history), default=0)
    days_overdue = invoice.get("days_overdue", 0)

    compress = 0.5 if cause == "distress" else 1.0

    for number, name, trigger_days, action, cost in LADDER:
        if number <= highest:
            continue
        # Eligibility is checked before the trigger: a rung that is unavailable
        # is skipped outright rather than waited on.
        if number in (4, 5) and not invoice.get("suspension_right"):
            continue
        if number in (4, 5) and not invoice.get("work_ongoing"):
            continue
        effective_trigger = trigger_days * compress
        if days_overdue < effective_trigger:
            return {"action": "wait",
                    "next_rung": number,
                    "next_rung_name": name,
                    "fires_in_days": round(effective_trigger - days_overdue),
                    "reason": f"rung {number} trigger is {effective_trigger:.0f} days overdue"}
        return {"action": "escalate", "rung": number, "name": name,
                "detail": action, "relationship_cost": cost,
                "compressed_for_distress": cause == "distress"}

    return {"action": "escalate", "rung": 7, "name": "Handoff",
            "detail": LADDER[-1][3], "relationship_cost": "relationship ended"}


def _load(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def _self_check():
    engagement = {
        "commercial": {"payment_schedule": [
            {"label": "Deposit", "amount": 12000, "trigger": "signature",
             "issue_date": "2026-10-01"},
            {"label": "Milestone 1", "amount": 12000, "trigger": "acceptance of D1",
             "issue_date": "2026-11-01"},
            {"label": "Final", "amount": 6000, "trigger": "acceptance of D2",
             "issue_date": "2026-12-01"},
        ]},
        "payment_machinery": {"terms_days": 30, "approval_window_days": 5,
                              "payment_run_day_of_month": 25,
                              "cutoff_days_before_run": 10,
                              "po_required": True, "po_number": "PO-4471"},
    }
    result = schedule(engagement)
    assert result["total"] == 30000
    assert all(row["expected_receipt"] for row in result["rows"])
    # The payment run must push cash later than the contractual due date.
    assert any(row["slip_days"] > 0 for row in result["rows"]), result["rows"]
    assert result["warnings"] == [], result["warnings"]

    heavy_final = json.loads(json.dumps(engagement))
    heavy_final["commercial"]["payment_schedule"] = [
        {"label": "Final", "amount": 30000, "trigger": "completion",
         "issue_date": "2026-12-01"}]
    warnings = schedule(heavy_final)["warnings"]
    assert any("final payment" in w for w in warnings), warnings

    no_po = json.loads(json.dumps(engagement))
    no_po["payment_machinery"]["po_number"] = None
    assert any("PO required" in w for w in schedule(no_po)["warnings"])

    ledger = {
        "as_of": "2026-12-01",
        "monthly_cost": 9000,
        "invoices": [
            {"id": "INV-1", "client": "Northwind", "amount": 12000,
             "due_date": "2026-10-15", "cause": "administrative"},
            {"id": "INV-2", "client": "Northwind", "amount": 6000,
             "due_date": "2026-11-20", "cause": "distress"},
            {"id": "INV-3", "client": "Acme", "amount": 3000,
             "due_date": "2026-12-10"},
            {"id": "INV-4", "client": "Acme", "amount": 2000,
             "due_date": "2026-11-25"},
        ],
    }
    aged = age(ledger)
    assert aged["total_overdue"] == 20000.0, aged["total_overdue"]
    # INV-3 is not yet due and must be excluded.
    assert all(row["invoice"] != "INV-3" for row in aged["rows"])
    assert aged["buckets"]["31-60"]["count"] == 1, aged["buckets"]
    assert aged["largest_client_exposure"][0] == "Northwind"
    assert aged["months_of_cost_covered"] == round(20000 / 9000, 2)
    assert aged["undiagnosed"] == ["INV-4"], aged["undiagnosed"]

    assert rung({"cause": "dispute"})["action"] == "refuse"
    assert rung({"cause": None})["action"] == "diagnose"

    fresh = rung({"cause": "administrative", "days_overdue": 5, "contact_history": []})
    assert fresh["action"] == "escalate" and fresh["rung"] == 1, fresh

    waiting = rung({"cause": "administrative", "days_overdue": 1, "contact_history": []})
    assert waiting["action"] == "wait" and waiting["next_rung"] == 1, waiting

    # A rung already fired is never repeated.
    second = rung({"cause": "administrative", "days_overdue": 20,
                   "contact_history": [{"rung": 1}]})
    assert second["rung"] == 2, second

    # Suspension is skipped without a contractual right: rungs 4 and 5 are not
    # offered at all, so the ladder waits for rung 6 rather than proposing a
    # notice that could not be executed.
    no_right = rung({"cause": "administrative", "days_overdue": 50,
                     "contact_history": [{"rung": 1}, {"rung": 2}, {"rung": 3}],
                     "suspension_right": False, "work_ongoing": True})
    assert no_right["action"] == "wait" and no_right["next_rung"] == 6, no_right

    no_right_later = rung({"cause": "administrative", "days_overdue": 65,
                           "contact_history": [{"rung": 1}, {"rung": 2}, {"rung": 3}],
                           "suspension_right": False, "work_ongoing": True})
    assert no_right_later["rung"] == 6, no_right_later

    # Nor is suspension offered where the work has already finished.
    finished = rung({"cause": "administrative", "days_overdue": 65,
                     "contact_history": [{"rung": 1}, {"rung": 2}, {"rung": 3}],
                     "suspension_right": True, "work_ongoing": False})
    assert finished["rung"] == 6, finished

    with_right = rung({"cause": "administrative", "days_overdue": 50,
                       "contact_history": [{"rung": 1}, {"rung": 2}, {"rung": 3}],
                       "suspension_right": True, "work_ongoing": True})
    assert with_right["rung"] == 4, with_right

    # Distress compresses the triggers.
    distress = rung({"cause": "distress", "days_overdue": 16,
                     "contact_history": [{"rung": 1}, {"rung": 2}]})
    assert distress["action"] == "escalate" and distress["rung"] == 3, distress
    steady = rung({"cause": "administrative", "days_overdue": 16,
                   "contact_history": [{"rung": 1}, {"rung": 2}]})
    assert steady["action"] == "wait", steady

    print("receivables.py self-check: PASS")
    return 0


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--schedule", metavar="ENGAGEMENT_JSON")
    parser.add_argument("--age", metavar="LEDGER_JSON")
    parser.add_argument("--rung", metavar="INVOICE_JSON")
    parser.add_argument("--self-check", action="store_true")
    args = parser.parse_args(argv)

    if args.self_check:
        return _self_check()

    if args.schedule:
        result = schedule(_load(args.schedule))
        print(json.dumps(result, indent=2))
        return 1 if result["warnings"] else 0

    if args.age:
        result = age(_load(args.age))
        print(json.dumps(result, indent=2))
        return 1 if result["total_overdue"] else 0

    if args.rung:
        print(json.dumps(rung(_load(args.rung)), indent=2))
        return 0

    parser.error("provide --schedule, --age, --rung, or --self-check")


if __name__ == "__main__":
    sys.exit(main())
