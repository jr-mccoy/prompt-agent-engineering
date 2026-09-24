---
title: "Political Law Compliance Review — Campaign Finance, Lobbying Registration, and Gift Rules"
category: legal/regulatory-compliance
description: "Attorney-facing review of an organization's political activity across campaign-finance, lobbying-registration and reporting, gift and travel rules, and pay-to-play restrictions at the federal, state, and local levels — activity inventory, per-regime trigger testing, reporting calendar, and policy gaps — distinct from enterprise-wide compliance program review and from policy-advocacy strategy or election-integrity communications."
techniques:
  - DS-32
  - DS-33
  - DT-05
  - QA-05
  - QA-12
difficulty: advanced
tags:
  - legal
  - political-law
  - campaign-finance
  - lobbying-disclosure
  - gift-rules
  - pay-to-play
  - company-political-donations
  - hiring-a-lobbyist
updated: "2026-09-24"
related_prompts:
  - domain-legal/regulatory-compliance/legal_compliance_program_gap_analysis.md
  - domain-legal/regulatory-compliance/legal_internal_investigation_plan.md
  - domain-policy/policy_stakeholder_coalition_map.md
---

# Political Law Compliance Review — Campaign Finance, Lobbying Registration, and Gift Rules

> **Scope guard — attorney-facing only.** This prompt is for political-law, government-affairs, or compliance counsel reviewing an organization's activities. It does not advise a candidate committee on campaign strategy, does not assess whether any particular message is persuasive, and does not advise an individual donor on their personal giving. A person without counsel should route to `domain-legal/personal-self-advocacy/cross-cutting/legalprep_professional_authority_router.md`.

> **No-fabrication rule.** Contribution limits, lobbying registration and reporting thresholds, gift-rule dollar exceptions, reporting deadlines, and pay-to-play de minimis amounts change by cycle, by rule amendment, and by jurisdiction. State none as settled — mark each `[VERIFY: current figure, jurisdiction, cycle]`. Do not invent statutes, advisory opinions, enforcement matters, or ethics-committee guidance; use `[CITE: …]` / `[NEED PIN: …]`.

## When to Use

- A company, trade association, or nonprofit wants a compliance review of its political contributions, PAC, lobbying, and interactions with officials before an election cycle or annual certification.
- The organization is starting government-affairs activity (hiring an outside lobbyist, bidding on public contracts, hosting officials) and needs to know what registrations and restrictions attach.
- A specific activity has been flagged (an executive reimbursed for a contribution, an official invited to a paid event) and counsel needs the regime analysis before investigating.

**Not this prompt if:**
- You are reviewing the whole compliance program across risk areas — use `domain-legal/regulatory-compliance/legal_compliance_program_gap_analysis.md` and feed its political-activity items here.
- A possible violation needs fact-finding (interviews, email review) — use `domain-legal/regulatory-compliance/legal_internal_investigation_plan.md`.
- The question is advocacy strategy (which coalitions, which officials) — use `domain-policy/policy_stakeholder_coalition_map.md`.

## Inputs

- **Jurisdictions (required):** Federal; each state and locality where the organization contributes, lobbies, contracts with government, or interacts with officials.
- **Organization profile:** Entity type (corporation, LLC, partnership, tax-exempt organization and its subsection, trade association); whether it is a government contractor or regulated entity (e.g., investment adviser, broker-dealer, municipal-securities dealer) subject to pay-to-play rules `[VERIFY]`; any foreign ownership or foreign nationals in decision-making roles.
- **Activity inventory:** Contributions (corporate, PAC, executives' personal where reimbursed or solicited), independent expenditures and issue ads, payments to political organizations or ballot committees, trade-association dues used for lobbying or political activity, in-kind support (facilities, staff time, mailing lists).
- **Lobbying facts:** Employees and outside firms who contact officials; subjects; time spent; expenses; which branches (legislative, executive, procurement).
- **Gifts and hospitality:** Meals, travel, event tickets, honoraria, and speaking fees provided to officials or staff.
- **Existing policies and filings:** Political-activity policy, pre-clearance process, recent registrations and reports.

## Method

1. **Jurisdiction lock.** List each jurisdiction and the regimes it has: campaign finance, lobbying registration/reporting, gift and ethics rules (by branch), pay-to-play, and any foreign-agent registration exposure `[VERIFY]`. Treat each as separate — federal compliance does not satisfy state or local rules.
2. **Contribution analysis, per item.** Source of funds (corporate treasury, PAC, individual); recipient type; permissibility (for example, corporate contributions to federal candidates are prohibited; state rules vary `[VERIFY]`); applicable limit `[VERIFY]`; aggregation with affiliates; reimbursement or "in the name of another" risk; foreign-national participation risk; employee solicitation rules for a connected PAC `[VERIFY: solicitable class]`.
3. **Independent expenditures and coordination.** For corporate or association spending on communications, test coordination with candidates or parties under the relevant jurisdiction's standards `[VERIFY]`, and disclaimer and reporting obligations `[VERIFY]`.
4. **Lobbying registration and reporting.** For each jurisdiction, test the registration trigger — definitions of lobbying contact, covered official, time threshold, and income/expense thresholds `[VERIFY]` — for in-house employees and for outside firms. Identify periodic report types and due dates `[VERIFY]`. Note where state definitions reach executive-branch, procurement, or grassroots lobbying that federal law does not.
5. **Gift, travel, and hospitality.** For each item, identify the recipient's branch and level and apply that body's gift rule, including exceptions (widely attended events, personal friendship, de minimis) `[VERIFY: current values and conditions]`. Rules for legislative staff, executive officials, and state officials differ.
6. **Pay-to-play.** If the organization or its executives seek government contracts or public-investor business, test contributions against applicable restrictions and look-back periods `[VERIFY]` and the consequence (e.g., bar on compensation or contract award).
7. **Tax-exempt overlay.** If a 501(c) organization is involved, flag campaign-intervention prohibitions and lobbying limits for tax counsel `[VERIFY]`; do not resolve tax status here.
8. **Findings, calendar, and policy gaps.** Classify each item as compliant, gap (fixable prospectively), or potential violation (route to investigation and disclosure analysis). Build a registration and reporting calendar. Recommend policy controls — pre-clearance, reimbursement ban, gift log, lobbying time-tracking.

## Output Format

```markdown
# Political Law Compliance Review — {Organization} — {Cycle / Period}
**Jurisdictions:** {…}  |  **Entity type:** {…}  |  **Privileged & Confidential — Attorney-Client Communication**

## 1. Regime Map by Jurisdiction
| Jurisdiction | Campaign finance | Lobbying | Gift/ethics (by branch) | Pay-to-play | Foreign-agent exposure |
## 2. Contribution Review
| # | Date | Source of funds | Recipient | Permissible? | Limit [VERIFY] | Aggregation / reimbursement / foreign-national issues | Finding |
## 3. Independent Expenditures and Coordination
## 4. Lobbying Registration and Reporting
| Jurisdiction | Person / firm | Trigger test [VERIFY] | Registered? | Reports due [VERIFY] | Finding |
## 5. Gifts, Travel, and Hospitality
| Item | Recipient (branch/level) | Rule applied | Exception claimed [VERIFY] | Finding |
## 6. Pay-to-Play Review
## 7. Tax-Exempt Flags (for tax counsel)
## 8. Findings Summary (compliant / gap / potential violation)
## 9. Registration and Reporting Calendar
## 10. Policy and Control Recommendations
## 11. Verification Items
```

## Verification

- [ ] Jurisdiction lock: every activity tested against each jurisdiction where it occurs; federal rules not assumed to govern state or local activity.
- [ ] Citation discipline: every limit, threshold, deadline, and exception value is supplied or `[VERIFY]`; no invented advisory opinions or enforcement matters.
- [ ] Scope discipline: compliance analysis only; no campaign strategy or tax-status determination.
- [ ] Each contribution checked for source of funds, recipient type, aggregation, reimbursement, and foreign-national participation.
- [ ] Lobbying trigger tested separately for in-house staff and outside firms, per jurisdiction.
- [ ] Each gift matched to the recipient's specific body's rule.
- [ ] Potential violations routed to investigation, not resolved by a prospective policy fix alone.

## False-Positive Prevention

| Failure mode | Correction |
|---|---|
| Treating federal compliance as sufficient | Test every state and local regime separately; definitions and thresholds differ |
| Quoting contribution limits or lobbying thresholds from memory | They are indexed or amended — `[VERIFY]` for the current cycle |
| Missing reimbursed "personal" contributions | Check expense reports and bonuses for reimbursement; this is a straw-donor issue |
| Applying one gift rule to all officials | Legislative, executive, and state bodies each have their own rules and exceptions |
| Overlooking pay-to-play for executives' personal giving | Where the organization seeks public business, executives' contributions can bar the business |
| Ignoring foreign-national involvement in decisions | Test who directs or decides on contributions and spending, not only whose money it is |

## Example

**Input (abridged):** Fictional Meridian Water Systems, a US corporation bidding on municipal water contracts in two states, with a minority foreign shareholder that has a board seat. Last year: the CEO gave to a mayoral candidate in a city where Meridian later bid; the company paid for a state legislator's travel to a plant tour; an in-house manager spends part of her time meeting state agency procurement staff; the board approved a $50,000 contribution to a ballot-measure committee.

**Output (excerpt):**

> **Pay-to-play — CEO contribution.** Test the city's and state's contractor-contribution restrictions and look-back periods `[VERIFY]`; if the contribution falls within a restricted window, the bid may be barred or require disclosure. Finding: **potential violation pending verification** — route to counsel review before the next bid.
>
> **Ballot-measure contribution — foreign-national participation.** State rules on corporate ballot-measure contributions vary `[VERIFY]`; separately, the foreign shareholder's board seat raises a question whether a foreign national participated in the decision `[VERIFY: federal and state foreign-national rules for ballot measures]`. Need: board minutes and recusal record `[NEED]`.
>
> **Lobbying — procurement contacts.** Several states treat procurement-related contacts with executive agencies as lobbying `[VERIFY: each state's definition and time/expense threshold]`; the manager may need to register.
>
> **Gift — legislator travel.** Apply the state legislature's travel rule and any fact-finding-trip exception `[VERIFY]`; confirm reporting by the legislator and by Meridian if the state requires lobbyist-employer reporting.
