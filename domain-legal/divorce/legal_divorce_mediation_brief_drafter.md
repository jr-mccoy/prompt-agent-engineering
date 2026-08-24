---
title: "Divorce Mediation Brief Drafter"
category: legal/divorce
description: "Draft a mediation statement/brief for a divorce mediation: case posture, undisputed vs. disputed facts, issue-by-issue positions with supporting-authority placeholders, settlement history, what the client needs to resolve, and a proposed path — in two versions where useful (confidential for the mediator's eyes only, and an exchanged version), with tone calibrated to persuade a neutral facilitator rather than a judge."
techniques:
  - ST-01
  - ST-02
  - ST-03
  - RT-02
  - CM-02
  - DS-02
  - QA-01
difficulty: intermediate
tags:
  - legal
  - divorce
  - family-law
  - mediation
  - mediation-brief
  - settlement
  - drafting
updated: "2026-06-10"
related_prompts:
  - domain-legal/divorce/legal_divorce_settlement_and_mediation_prep.md
  - domain-legal/divorce/legal_post_mediation_term_sheet_and_mou_drafter.md
  - domain-legal/divorce/legal_property_division_and_equalization_proposal.md
  - domain-legal/divorce/legal_spousal_support_alimony_analysis.md
  - domain-legal/custody/legal_custody_mediation_brief_drafter.md
---

**Purpose:** Draft the written mediation statement counsel submits before a divorce mediation — orienting the mediator to the case posture, the financial landscape, what is genuinely disputed, the client's positions and the reasoning behind them, and what a workable resolution requires. A mediation brief persuades a **neutral facilitator**, not a judge: it should make the client's positions look reasonable, identify movement, and equip the mediator to push the other side — without the adversarial heat of a trial brief. Where strategy or sensitive facts shouldn't reach the other side, produce a confidential (mediator-only) version alongside an exchanged version. For custody-issue briefs, use `legal_custody_mediation_brief_drafter.md`.

**When to use:** Mediator requests pre-session statements; counsel wants to frame the issues before the session; a prior session stalled and a refocused written statement would reset the table.

---

## Your Input

- **Jurisdiction:** [State; community-property vs. equitable-distribution regime; mediation-confidentiality rule and whether briefs are confidential by default `[CITE: …]`]
- **Mediator's instructions:** [Page limit, format, exchanged vs. confidential, deadline, what the mediator asked to see]
- **Case posture:** [Filing date, stage (pre-filing / discovery / trial set), pending motions, temporary orders in place]
- **Parties & marriage facts:** [Names, ages, marriage length, employment/income, children (ages only; custody issues routed separately)]
- **Issues for this mediation:** [Property division, equalization, spousal support, child support, fees — list each in play]
- **Undisputed facts:** [What both sides agree on — estate composition, values stipulated, incomes]
- **Disputed facts:** [Valuations, characterization (separate vs. marital), income/earning capacity, dissipation claims]
- **Client positions per issue with reasons:** [Position + supporting facts and authority `[CITE: …]`]
- **Settlement history:** [Offers and counteroffers to date, with dates; what moved and what stalled]
- **Confidential-only material:** [Bottom lines, client constraints (health, job change, cash-flow cliff), strategy, sensitive facts — mediator's eyes only]
- **What the client needs to resolve:** [The interests a deal must satisfy]

---

## Constraints

**Must:**
- Follow the **mediator's instructions** (length, format, exchange status, deadline) — they override defaults; if not supplied, mark `[NEED: mediator instructions]` and use a concise default.
- Calibrate tone for a **neutral**: confident and factual, not inflammatory; characterize the other side's positions fairly enough that the mediator trusts the brief as a map.
- Separate **undisputed from disputed** facts explicitly — the undisputed list shrinks the fight and builds credibility.
- Present each issue with **position → supporting facts → supporting authority** `[CITE: …]`, and where the position depends on a valuation or guideline, mark `[NEED VALUATION: …]` / `[NEED GUIDELINE: …]` rather than inventing figures.
- Maintain a hard wall between the **exchanged version** and the **confidential version**: bottom lines, client constraints, and strategy go only in the confidential version, clearly labeled "CONFIDENTIAL — FOR MEDIATOR ONLY."
- Include **settlement history** accurately (dates, offers) so the mediator sees the bid-ask and the movement pattern.
- State **what resolution requires** — the interests a deal must satisfy — so the mediator has material to work with, not just positions.
- Respect **mediation confidentiality** and note the brief's status under the governing rule `[CITE: …]`.
- Flag any **DV/safety or power-imbalance** concern relevant to session format (caucus, shuttle) in the confidential version.

**Must Not:**
- Write a trial brief: no extended argument, no attacks on opposing counsel, no credibility assaults that poison the room.
- Put bottom lines, walk-away numbers, or client vulnerabilities in the exchanged version.
- Invent valuations, guideline figures, statutory factors, or case citations.
- Misstate the settlement history or the other side's offers.
- Overstate disputed facts as undisputed — the mediator will discover it and the brief loses its credibility.
- Promise or predict what the court would do as certainty — frame litigated outcomes as ranges.
- Insert generic "consult counsel" disclaimers.

---

## Instructions

1. **Frame & format.** Apply the mediator's instructions; confirm the brief's confidentiality status under the governing rule `[CITE: …]`; decide whether one exchanged brief suffices or a confidential supplement is needed.
2. **Case snapshot.** One paragraph: parties, marriage length, procedural posture, temporary orders, what brought the case to mediation.
3. **Undisputed-facts ledger.** List stipulated values, agreed estate items, agreed incomes — everything off the table.
4. **Disputed-issues map.** For each disputed issue: the question (characterization, valuation, support amount/duration), each side's number or position, and the delta.
5. **Issue-by-issue positions.** For each issue in play: client's position, the facts supporting it, the authority `[CITE: …]`, and the range a court would likely reach (stated as a range, with confidence).
6. **Settlement history.** Chronology of offers/counteroffers with dates; characterize movement neutrally.
7. **What resolution requires.** State the client's interests a deal must satisfy (liquidity, housing transition, retirement security, finality, cost control) — the mediator's working material.
8. **Proposed path.** Suggest a session structure: issue order, what can be resolved first, what may need caucus, any process requests (shuttle, separate sessions) — safety-related requests go in the confidential version.
9. **Confidential supplement (if used).** Bottom lines per issue, client constraints and timing pressures, candid assessment of weaknesses, strategy notes, safety concerns — labeled and segregated.
10. **Credibility pass.** Re-read as the mediator: anything inflammatory, overstated, or unsupported weakens the brief — cut or support it.

---

## Output Format

```markdown
# MEDIATION STATEMENT — {EXCHANGED / CONFIDENTIAL — FOR MEDIATOR ONLY}
**Matter:** {caption}   **Mediation date:** {date}   **Mediator:** {name}
**Submitted by:** {counsel} for {party}   **Status under {rule}:** {confidential / exchanged} [CITE: …]

## 1. Case Snapshot
{Parties, marriage length, posture, temporary orders, why mediation now.}

## 2. Undisputed Facts
- {Stipulated value / agreed item / agreed income}

## 3. Disputed Issues at a Glance
| Issue | {Client} position | {Other party} position | Delta |
|---|---|---|---|

## 4. Positions & Support (by issue)
### {Issue — e.g., Characterization of {asset}}
- Position: {…}
- Supporting facts: {…}
- Authority: [CITE: …]   Likely litigated range: {…} — Confidence: {H/M/L}

## 5. Settlement History
| Date | Offer (by) | Terms | Response |
|---|---|---|---|

## 6. What Resolution Requires
- {Interest a deal must satisfy}

## 7. Proposed Session Path
- {Issue order; caucus suggestions; process requests}

---
*(Confidential version only)*
## C-1. Bottom Lines
| Issue | Walk-away | Note |
|---|---|---|
## C-2. Constraints, Weaknesses & Strategy
- {Timing pressures, candid weaknesses, negotiation read}
## C-3. Safety / Process Concerns
- {DV / power imbalance; requested format: caucus / shuttle}
```

---

## Verification

- [ ] Mediator's instructions (length, format, exchange status, deadline) followed or flagged `[NEED: …]`.
- [ ] Tone calibrated for a neutral — no trial-brief heat, no attacks.
- [ ] Undisputed facts separated from disputed; nothing disputed listed as agreed.
- [ ] Every position backed by facts and authority placeholders; no invented valuations, guidelines, or citations.
- [ ] Bottom lines and client constraints appear only in the confidential version, clearly labeled.
- [ ] Settlement history accurate with dates; movement characterized neutrally.
- [ ] Client interests ("what resolution requires") stated, not just positions.
- [ ] Litigated outcomes framed as ranges with confidence, never as certainties.
- [ ] Brief's confidentiality status under the governing rule stated `[CITE: …]`.
- [ ] Any DV/safety process request routed to the confidential version.

---

## False-Positive Prevention

| Failure mode | Correction |
|---|---|
| Writing a trial brief for a mediator | Persuade a neutral: factual confidence, fair characterization, settlement orientation |
| Leaking the bottom line in the exchanged version | Hard wall: walk-aways and constraints go in the confidential supplement only |
| Listing disputed valuations as "undisputed" to look strong | The mediator will find out; credibility is the brief's main asset |
| Inflammatory characterization of the other spouse | Cut it; heat in the brief makes the mediator's job harder and signals unreasonableness |
| Inventing a guideline number or case citation to round out an argument | [NEED GUIDELINE] / [CITE] placeholders — never fabricate |
| Predicting the court's ruling as certain | Ranges with confidence levels |
| Omitting settlement history because it shows the client moved | Include it accurately; the mediator will hear the other side's version anyway |
| Ignoring the mediator's page limit or format request | The mediator's instructions override the template |
| Presenting positions with no underlying interests | Add "what resolution requires" — interests are what the mediator trades on |
| Burying a DV/safety process need in the exchanged brief (or omitting it) | Confidential version, explicit format request (caucus/shuttle) |
| One brief for both audiences when strategy must be shared with the mediator | Produce exchanged + confidential versions with a clean wall |
