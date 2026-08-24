---
title: "Client Status Update Memo"
category: legal/client-intake-communications
description: "Draft a client-facing matter status update memo: matter identification, reporting period, decisions made within counsel's authority, decisions awaiting client input, progress against budget, upcoming milestones, opposing-party movement, risk-posture changes, and recommended next actions with cost estimates — with attorney-client privilege caption and distribution-list discipline to avoid waiver."
techniques:
  - ST-01
  - ST-02
  - ST-03
  - CM-02
  - DS-02
  - QA-01
difficulty: beginner
tags:
  - legal
  - client-communication
  - status-update
  - matter-management
  - budget
  - privilege
updated: "2026-05-11"
related_prompts:
  - domain-legal/client-intake-communications/legal_new_matter_intake_summary.md
  - domain-legal/client-intake-communications/legal_engagement_letter_drafter.md
  - domain-legal/in-house-legalops/legal_matter_summary_for_executive.md
  - domain-legal/litigation/legal_complaint_drafter.md
---

**Purpose:** Produce a periodic client-facing status update that gives the client a complete picture of where the matter stands, what decisions are pending, how spend is tracking against budget, and what comes next — without waiving privilege through over-broad distribution or unguarded language. Output is a client deliverable.

**When to use:** Monthly or quarterly client reporting cadence; ad-hoc updates after material events (ruling, opposing-party motion, settlement overture, regulatory development); pre-billing-cycle briefing; in-house legal-ops dashboards rolled up to the business decision-maker.

---

## Your Input

- **Jurisdiction:** [State / federal forum; controlling law — relevant for risk posture and budget assumptions]
- **Practice area:** [Litigation / transactional / regulatory / IP / employment / etc.]
- **Posture:** [Pre-suit / pleading stage / discovery / dispositive motions / trial prep / appeal / closing / regulatory response]
- **Matter identification:** [Matter name; internal matter ID / docket number; responsible attorney]
- **Reporting period:** [Start and end dates]
- **Client decision-maker:** [Name, title, role for this matter]
- **Distribution list:** [Who is to receive this memo — note any non-client recipients raise privilege-waiver questions]
- **Activity in reporting period:** [Filings, hearings, depositions, document productions, communications, negotiations, decisions made by counsel]
- **Decisions within counsel's authority taken during period:** [E.g., scheduling stipulations, routine objections, witness sequencing]
- **Decisions awaiting client input:** [E.g., settlement range authority, willingness to depose specific witness, scope of waiver, deal-term tradeoffs]
- **Budget status:** [Fees and expenses incurred to date; budget for matter or phase; variance and explanation]
- **Upcoming milestones:** [Next 30/60/90 day deadlines, hearings, deliverables]
- **Opposing-party / counterparty movement:** [Position changes, new filings, settlement overtures, regulatory action]
- **Risk-posture changes:** [Material developments shifting likelihood, exposure, or strategy]
- **Recommended next actions:** [Counsel's recommendation with cost estimate for each]

---

## Constraints

**Must:**
- Caption the memo as **Attorney-Client Privileged & Work Product**.
- Identify the **client decision-maker** and confirm the distribution list is limited to (a) the client, (b) those whose presence does not destroy privilege (e.g., agents necessary to the representation, joint clients, common-interest parties under a written agreement). Flag any non-client recipient before sending.
- State **reporting period** and **matter ID**.
- Distinguish clearly between **decisions counsel has taken within authority** (informational) and **decisions awaiting client input** (action items).
- For each pending decision, state the question, the options, counsel's recommendation, the deadline for decision, and the consequence of inaction.
- Report **budget posture**: amount incurred this period; cumulative incurred; budget for the matter / current phase; variance; explanation if variance > {threshold, e.g., 10%}; revised forecast if material.
- Report **upcoming milestones** with dates and what is required of the client.
- Report **opposing-party / counterparty movement** factually, without unguarded characterizations.
- Report **risk-posture changes** with reasons — what changed and why it matters for outcome / exposure / cost.
- For **recommended next actions**, include cost estimate ranges.
- Use placeholders `[CITE: ...]`, `[NEED: ...]` where data is incomplete.

**Must Not:**
- CC anyone outside the client / privileged circle without confirming privilege impact — copying a non-client (e.g., the client's PR firm, business partner, or relative) can waive privilege.
- Use language that would be harmful if produced in discovery (e.g., loose admissions of weakness; characterizations of witnesses as "lying"; speculative legal conclusions). Be candid about risk but disciplined in phrasing.
- Conflate counsel's recommendation with the client's decision — separate them.
- State outcome predictions as guarantees; use calibrated language (likely / possible / unlikely with reasons).
- Invent docket numbers, hearing dates, dollar amounts, party names, or rulings.
- Insert generic "consult counsel" disclaimers — counsel IS reporting.

---

## Instructions

1. **Header.** Privilege caption; date; matter name and ID; reporting period; from (responsible attorney); to (client decision-maker); cc (with privilege-impact note).
2. **Executive summary.** Two to four sentences: posture, headline development this period, immediate decisions needed.
3. **Activity during reporting period.** Bulleted: filings, hearings, depositions, productions, negotiations, regulatory steps. Each with date.
4. **Decisions taken by counsel within authority.** Informational list with brief rationale.
5. **Decisions awaiting client input.** Numbered. Each has: (a) the question; (b) the options; (c) counsel's recommendation and reason; (d) deadline for client decision; (e) consequence of inaction.
6. **Budget posture.** Table or short ledger:
   - Fees this period; expenses this period
   - Cumulative fees + expenses
   - Budget (matter or current phase)
   - Variance and explanation
   - Forecast for next reporting period or to next milestone
7. **Upcoming milestones (next 30/60/90 days).** Date; event; client action required (if any).
8. **Opposing-party / counterparty movement.** Position changes, filings, settlement overtures — factual.
9. **Risk-posture changes.** What shifted, why, and the implication for outcome / exposure / cost / timing.
10. **Recommended next actions.** Numbered, each with cost estimate range and decision needed (if any).
11. **Closing.** Availability for live discussion; preferred channel; deadline for time-sensitive items.

---

## Output Format

```markdown
ATTORNEY-CLIENT PRIVILEGED & ATTORNEY WORK PRODUCT — DO NOT FORWARD WITHOUT COUNSEL APPROVAL

MEMORANDUM

TO:       {Client Decision-Maker, Title}
CC:       {Limit to privileged recipients; flag any non-client recipient}
FROM:     {Responsible Attorney, Firm}
DATE:     {Date}
RE:       Status Update — {Matter Name} (Matter ID {…})
PERIOD:   {Start Date} – {End Date}

EXECUTIVE SUMMARY
{2–4 sentences: posture; headline development; decisions needed this cycle.}

1. ACTIVITY DURING REPORTING PERIOD
   - {YYYY-MM-DD}: {filing / hearing / deposition / negotiation / etc.}
   - {YYYY-MM-DD}: {…}
   - {YYYY-MM-DD}: {…}

2. DECISIONS TAKEN BY COUNSEL WITHIN AUTHORITY
   - {Decision, brief rationale}
   - {Decision, brief rationale}

3. DECISIONS AWAITING CLIENT INPUT
   3.1 Question: {…}
       Options: (a) {…}; (b) {…}; (c) {…}
       Recommendation: {option and reason}
       Deadline: {date}
       Consequence of inaction: {…}
   3.2 Question: {…}
       Options: {…}
       Recommendation: {…}
       Deadline: {…}
       Consequence of inaction: {…}

4. BUDGET POSTURE
   | Item | This Period | Cumulative | Budget | Variance |
   |---|---|---|---|---|
   | Fees | ${…} | ${…} | ${…} | {±%} |
   | Expenses | ${…} | ${…} | ${…} | {±%} |
   | Total | ${…} | ${…} | ${…} | {±%} |
   Explanation of variance: {…}
   Forecast to next milestone / next period: ${…}

5. UPCOMING MILESTONES
   - {YYYY-MM-DD}: {event} — Client action required: {…}
   - {YYYY-MM-DD}: {event} — Client action required: {…}
   - {YYYY-MM-DD}: {event} — Client action required: {…}

6. OPPOSING-PARTY / COUNTERPARTY MOVEMENT
   - {Position change, filing, settlement overture, regulatory action — factually described}

7. RISK-POSTURE CHANGES
   - What changed: {…}
   - Why it matters: {outcome / exposure / cost / timing}
   - Net assessment: likelihood of {result} is now {likely / possible / unlikely} because {…}

8. RECOMMENDED NEXT ACTIONS
   8.1 {Action} — Estimated cost: ${range} — Decision needed: {y/n; if yes, see 3.x}
   8.2 {Action} — Estimated cost: ${range} — Decision needed: {…}
   8.3 {Action} — Estimated cost: ${range} — Decision needed: {…}

9. AVAILABILITY
   Available to discuss live at {…}. Time-sensitive items above have deadlines by {date}.

— {Attorney Name}, {Firm}
```

---

## Verification

- [ ] Privilege caption present and distribution list reviewed for non-client recipients.
- [ ] Matter ID and reporting period identified.
- [ ] Executive summary states posture, headline development, and decisions needed.
- [ ] Decisions taken by counsel are separated from decisions awaiting client input.
- [ ] Each pending decision states question, options, recommendation, deadline, and consequence of inaction.
- [ ] Budget table shows this-period, cumulative, budget, variance, and explanation if variance exceeds threshold.
- [ ] Upcoming milestones list dates and client actions required.
- [ ] Risk-posture section explains what changed and why it matters with calibrated language.
- [ ] Recommended actions include cost-estimate ranges.
- [ ] No language usable as a discovery admission against client.
- [ ] No invented docket numbers, dates, dollar amounts, or rulings.

---

## False-Positive Prevention

| Failure mode | Correction |
|---|---|
| CC'ing non-client recipients (PR firm, family, business partner) without privilege analysis | Limit distribution; non-client CC may waive privilege; document any common-interest agreement |
| Conflating counsel's recommendation with client's decision | Separate "decisions taken within authority" from "decisions awaiting client input" |
| Loose characterizations of witnesses / opposing parties ("lying," "incompetent") in a discoverable document | Use factual, disciplined phrasing — the document may be produced |
| Outcome predictions stated as certainty | Use calibrated terms (likely / possible / unlikely) with the basis |
| Budget reported only as a total without variance explanation | Show variance and explain when over threshold; revise forecast |
| Generic "next steps" without cost estimate | Include a range and the decision (if any) it requires |
| Missing privilege / work-product caption | Caption every status memo; train staff not to strip it on forwarding |
| Decisions presented without deadline or consequence of inaction | Each decision item needs both — clients defer when consequences are not stated |
| Treating routine scheduling decisions as needing client approval | Counsel makes within-authority calls; over-escalation wastes client time and trust |
| Using the memo to argue with opposing party / posture for litigation | This is a client report, not a position paper |
| Forwarding the memo to insurers / indemnitors without coverage-counsel coordination | Insurer communications may have separate privilege analysis; coordinate before sending |
| Omitting a "decisions awaiting client input" section because nothing is pending | State "None this period" explicitly; absence with no statement reads as oversight |
