#!/usr/bin/env python3
"""assemble.py — render a proposal/SOW from the scope record, and Gate B.

Not legal advice. Gate B is a structural red-flag scan over a contract summary
you have already extracted; it does not read contracts, does not interpret them,
and does not replace review by a lawyer before signature.

    render  — deterministic proposal + SOW correspondence table from an
              engagement record, so the document that is accepted is the
              document that governs delivery.
    Gate B  — refuse to mark an engagement closeable while unresolved red-flag
              clauses remain.

Usage:
    python assemble.py --render engagement.json
    python assemble.py --gateB engagement.json
    python assemble.py --self-check

Exit codes: 0 pass, 1 fail (gate blocked), 2 usage error.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

#: Clause conditions that block signature until resolved or consciously accepted.
#: Each is (id, predicate over the contract summary, severity, why it matters).
RED_FLAGS = (
    ("unlimited_liability",
     lambda c: c.get("liability_cap") in (None, 0) or c.get("liability_cap") == "unlimited",
     "critical",
     "no limitation of liability, or an unlimited cap"),
    ("uncapped_ip_indemnity",
     lambda c: c.get("ip_indemnity_capped") is False,
     "critical",
     "IP indemnity is uncapped"),
    ("unbounded_ip_assignment",
     lambda c: c.get("ip_assignment_scope") == "all_work_product",
     "high",
     "assignment extends beyond engagement deliverables to all work product"),
    ("payment_terms_long",
     lambda c: (c.get("payment_terms_days") or 0) > 60,
     "high",
     "payment terms beyond 60 days"),
    ("no_termination_compensation",
     lambda c: c.get("termination_for_convenience") is True
     and not c.get("termination_compensation"),
     "high",
     "client may terminate for convenience with no compensation"),
    ("unilateral_scope_change",
     lambda c: c.get("unilateral_scope_change") is True,
     "critical",
     "client may vary scope unilaterally"),
    ("no_suspension_right",
     lambda c: c.get("suspension_right") is False,
     "medium",
     "no right to suspend work for non-payment"),
    ("unilateral_set_off",
     lambda c: c.get("set_off") == "unilateral",
     "high",
     "client may set off sums it alone determines are owed"),
    ("unpriced_transition_assistance",
     lambda c: c.get("transition_assistance") == "unpriced",
     "medium",
     "transition assistance obligation with no rate and no cap"),
    ("no_undisputed_portion_clause",
     lambda c: c.get("undisputed_portion_payable") is False,
     "medium",
     "a small dispute can hold an entire invoice"),
)

BLOCKING_SEVERITIES = {"critical", "high"}

#: Proposal section -> the SOW section it must become. The correspondence is the
#: point: nothing is agreed in the proposal that the contract will not carry.
SOW_CORRESPONDENCE = (
    ("What you get", "Deliverables schedule"),
    ("How it will be judged complete", "Acceptance criteria"),
    ("What we need from you", "Client obligations"),
    ("What this assumes", "Assumptions"),
    ("What is not included", "Exclusions"),
    ("Timeline", "Milestone schedule"),
    ("Investment", "Fee and payment schedule"),
    ("If things change", "Change-order procedure"),
)


def gateB(engagement):
    """Return (passed, findings) over the engagement's contract summary.

    Findings at critical or high severity block unless explicitly accepted with
    a recorded rationale. Medium findings warn.
    """
    contract = engagement.get("contract") or {}
    accepted = {a["flag"]: a for a in contract.get("accepted_risks", [])}

    findings = []
    for flag_id, predicate, severity, why in RED_FLAGS:
        if not predicate(contract):
            continue
        acceptance = accepted.get(flag_id)
        findings.append({
            "flag": flag_id,
            "severity": severity,
            "reason": why,
            "accepted": bool(acceptance and acceptance.get("rationale")),
            "rationale": (acceptance or {}).get("rationale"),
        })

    if not contract.get("counsel_reviewed"):
        findings.append({
            "flag": "counsel_review",
            "severity": "high",
            "reason": "no record of review by a lawyer before signature",
            "accepted": False,
            "rationale": None,
        })

    blocking = [f for f in findings
                if f["severity"] in BLOCKING_SEVERITIES and not f["accepted"]]
    return (not blocking), findings


def render(engagement):
    """Render the proposal and the SOW correspondence table as Markdown."""
    scope = engagement.get("scope") or {}
    commercial = engagement.get("commercial") or {}
    client = engagement.get("client", "[client]")
    name = engagement.get("name", "[engagement]")

    lines = [f"# {name}", f"### Prepared for {client}", ""]

    problem = engagement.get("problem_statement")
    lines += ["## The problem as we understand it", problem or "_[from the discovery record]_", ""]

    lines += ["## What you get", "", "| # | Deliverable | Format | Judged complete when |",
              "|---|---|---|---|"]
    for index, deliverable in enumerate(scope.get("deliverables") or [], 1):
        lines.append(
            f'| {index} | {deliverable.get("name", "")} | {deliverable.get("format", "")} '
            f'| {deliverable.get("acceptance", "")} |')
    lines.append("")

    lines += ["## What we need from you", "",
              "| Input | Owner | By when | If late |", "|---|---|---|---|"]
    for item in scope.get("client_inputs") or []:
        lines.append(f'| {item.get("input", "")} | {item.get("owner", "")} '
                     f'| {item.get("due", "")} | {item.get("if_late", "")} |')
    lines.append("")

    lines += ["## What this assumes", ""]
    lines += [f"- {a}" for a in scope.get("assumptions") or []] or ["- _none stated_"]
    lines.append("")

    lines += ["## What is not included", ""]
    lines += [f"- {e}" for e in scope.get("exclusions") or []] or ["- _none stated_"]
    lines.append("")

    lines += ["## Investment", "",
              f'**Structure:** {commercial.get("structure", "[structure]")}  ',
              f'**Fee:** {commercial.get("fee", "[fee]")}', ""]
    schedule = commercial.get("payment_schedule") or []
    if schedule:
        lines += ["| Payment | Amount | Trigger |", "|---|---|---|"]
        for payment in schedule:
            lines.append(f'| {payment.get("label", "")} | {payment.get("amount", "")} '
                         f'| {payment.get("trigger", "")} |')
        lines.append("")

    lines += ["## If things change", "",
              engagement.get("change_procedure")
              or "_Work outside the deliverables above is a change order, quoted and "
                 "agreed in writing before it starts._", ""]

    lines += ["---", "", "## Proposal → SOW correspondence", "",
              "| Proposal section | Becomes, in the SOW |", "|---|---|"]
    for proposal_section, sow_section in SOW_CORRESPONDENCE:
        lines.append(f"| {proposal_section} | {sow_section} |")
    lines += ["",
              "_Not legal advice. Have a lawyer review the SOW before signature._"]

    return "\n".join(lines)


def _load(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def _self_check():
    clean_contract = {
        "liability_cap": 250000,
        "ip_indemnity_capped": True,
        "ip_assignment_scope": "deliverables",
        "payment_terms_days": 30,
        "termination_for_convenience": True,
        "termination_compensation": "work performed plus committed costs",
        "unilateral_scope_change": False,
        "suspension_right": True,
        "set_off": "admitted_only",
        "transition_assistance": "at standard rates, capped at 10 days",
        "undisputed_portion_payable": True,
        "counsel_reviewed": True,
    }
    engagement = {
        "name": "Pipeline assessment",
        "client": "Northwind",
        "problem_statement": "Deploy failures are rising and nobody can say why.",
        "scope": {
            "deliverables": [{"id": "D1", "name": "Pipeline assessment",
                              "format": "written report",
                              "acceptance": "covers the seven named pipelines"}],
            "assumptions": ["read access granted in week 1"],
            "exclusions": ["implementation of the recommendations"],
            "client_inputs": [{"input": "read access", "owner": "A. Patel",
                               "due": "2026-10-01", "if_late": "clock continues"}],
        },
        "commercial": {"structure": "fixed", "fee": 30000,
                       "payment_schedule": [{"label": "Deposit", "amount": 12000,
                                             "trigger": "signature"}]},
        "contract": clean_contract,
    }

    passed, findings = gateB(engagement)
    assert passed, f"a clean contract should pass Gate B: {findings}"

    for mutation, expected in (
        ({"liability_cap": None}, "unlimited_liability"),
        ({"ip_indemnity_capped": False}, "uncapped_ip_indemnity"),
        ({"ip_assignment_scope": "all_work_product"}, "unbounded_ip_assignment"),
        ({"payment_terms_days": 90}, "payment_terms_long"),
        ({"termination_compensation": None}, "no_termination_compensation"),
        ({"unilateral_scope_change": True}, "unilateral_scope_change"),
        ({"set_off": "unilateral"}, "unilateral_set_off"),
        ({"counsel_reviewed": False}, "counsel_review"),
    ):
        broken = json.loads(json.dumps(engagement))
        broken["contract"].update(mutation)
        passed, findings = gateB(broken)
        assert not passed, f"Gate B should block {expected}"
        assert any(f["flag"] == expected for f in findings), \
            f"expected {expected} in {[f['flag'] for f in findings]}"

    # Medium-severity findings warn but do not block.
    medium = json.loads(json.dumps(engagement))
    medium["contract"]["suspension_right"] = False
    passed, findings = gateB(medium)
    assert passed, "a medium finding alone must not block"
    assert any(f["flag"] == "no_suspension_right" for f in findings)

    # A blocking flag can be accepted, but only with a recorded rationale.
    accepted = json.loads(json.dumps(engagement))
    accepted["contract"]["payment_terms_days"] = 90
    accepted["contract"]["accepted_risks"] = [
        {"flag": "payment_terms_long", "rationale": "offset by a 40% deposit"}]
    passed, _ = gateB(accepted)
    assert passed, "an accepted flag with a rationale should unblock"

    bare = json.loads(json.dumps(engagement))
    bare["contract"]["payment_terms_days"] = 90
    bare["contract"]["accepted_risks"] = [{"flag": "payment_terms_long"}]
    passed, _ = gateB(bare)
    assert not passed, "acceptance without a rationale must not unblock"

    markdown = render(engagement)
    for expected in ("Pipeline assessment", "Northwind", "What is not included",
                     "implementation of the recommendations",
                     "Proposal → SOW correspondence", "Acceptance criteria",
                     "Not legal advice"):
        assert expected in markdown, f"render() omitted {expected!r}"
    assert render(engagement) == markdown, "render() must be deterministic"

    print("assemble.py self-check: PASS")
    return 0


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--render", metavar="ENGAGEMENT_JSON")
    parser.add_argument("--gateB", metavar="ENGAGEMENT_JSON")
    parser.add_argument("--self-check", action="store_true")
    args = parser.parse_args(argv)

    if args.self_check:
        return _self_check()

    if args.render:
        print(render(_load(args.render)))
        return 0

    if args.gateB:
        passed, findings = gateB(_load(args.gateB))
        print(f"Gate B (signature risk cleared): {'PASS' if passed else 'BLOCKED'}")
        for finding in findings:
            status = "ACCEPTED" if finding["accepted"] else finding["severity"].upper()
            print(f"  {status:9} {finding['flag']}: {finding['reason']}")
            if finding["rationale"]:
                print(f"            rationale: {finding['rationale']}")
        return 0 if passed else 1

    parser.error("provide --render, --gateB, or --self-check")


if __name__ == "__main__":
    sys.exit(main())
