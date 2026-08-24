---
title: "Divorce Intake and Case Assessment"
category: legal/divorce
description: "Conduct a structured divorce/dissolution intake and produce a case-assessment memo: residency and subject-matter jurisdiction, grounds, asset and debt snapshot, children and custody posture, urgent issues (domestic violence, asset dissipation, immediate support need), client objectives, conflict screen, and a recommended process path (litigation, mediation, or collaborative) — all sized to the controlling state's dissolution statute."
techniques:
  - ST-01
  - ST-02
  - ST-03
  - RT-02
  - CM-02
  - DS-02
  - QA-01
  - QA-12
difficulty: intermediate
tags:
  - legal
  - divorce
  - family-law
  - intake
  - case-assessment
  - jurisdiction
updated: "2026-06-01"
related_prompts:
  - domain-legal/divorce/legal_divorce_petition_complaint_drafter.md
  - domain-legal/divorce/legal_divorce_settlement_and_mediation_prep.md
  - domain-legal/divorce/legal_financial_affidavit_and_disclosure_builder.md
  - domain-legal/divorce/legal_domestic_violence_protective_order_petition.md
  - domain-legal/custody/legal_uccjea_jurisdiction_analysis.md
  - domain-legal/client-intake-communications/legal_new_matter_intake_summary.md
---

**Purpose:** Turn a first divorce consultation into a structured assessment that (a) confirms the court has jurisdiction and the petitioner meets residency requirements, (b) inventories the marital estate and the children's posture, (c) flags issues requiring immediate action, and (d) recommends a process path. Output is an internal attorney work-product memo, not advice to the client and not a pleading.

**When to use:** Initial divorce/dissolution/legal-separation consultation; lateral transfer of a family-law matter requiring fresh assessment; deciding whether to take the case and at what scope.

---

## Your Input

- **Jurisdiction:** [State whose dissolution law governs; county/court; attorney's bar admission for that state]
- **Property regime:** [Community-property state / equitable-distribution state — if unknown, state so]
- **Marriage facts:** [Date and place of marriage; date of separation (if recognized); current living arrangement]
- **Residency facts:** [How long each spouse has lived in the state/county; military or relocation issues; prior filings elsewhere]
- **Grounds sought:** [No-fault (irretrievable breakdown / irreconcilable differences) / fault grounds if pleaded; waiting/separation period if required]
- **Parties:** [Names, ages, employment, income sources; represented status of other spouse if known]
- **Children:** [Names, ages, current schedule, school district, any existing custody order, special needs]
- **Asset/debt snapshot:** [Real property, retirement, business interests, accounts, vehicles, debts; which are likely separate vs. marital]
- **Urgent issues:** [Domestic violence / safety; threatened or actual asset dissipation; immediate support need; imminent relocation; bankruptcy; immigration status tied to marriage]
- **Client objectives:** [Stated priorities — children, house, support, speed, privacy, cost control]
- **Conflict-check inputs:** [Other spouse's name, related entities, prior representation]

---

## Constraints

**Must:**
- Confirm the **state and court** and identify the **residency/durational requirement** for filing in that jurisdiction; flag if the petitioner does not yet meet it.
- Identify the **property regime** (community vs. equitable distribution) because it changes the entire financial analysis; if not supplied, mark `[NEED REGIME]`.
- Run a **conflict-of-interest screen** and note that the firm cannot jointly represent both spouses (MRPC 1.7).
- Separate **issues requiring immediate action** (DV protective order, status-quo/standing orders, account freezes, preservation letters) from issues that can wait.
- Distinguish **marital/community property** from **separate property** at a preliminary level, expressly noting characterization is provisional pending disclosure and tracing.
- For any matter with children, confirm **UCCJEA home-state** posture and any existing custody order before assuming the forum can decide custody.
- State **confidence levels** (High/Medium/Low) on jurisdictional and characterization conclusions given that intake facts are unverified.
- Use placeholders `[CITE: ...]`, `[NEED FACTOR LIST: ...]`, `[NEED GUIDELINE: ...]`, `[NEED: ...]` for any statute, residency period, or fact not supplied.

**Must Not:**
- Invent the state's residency period, grounds language, waiting periods, statutory best-interests factors, or support guideline figures.
- Assume community property or equitable distribution without confirming the state's regime.
- Provide a definitive valuation or division — this is a preliminary snapshot, not a property settlement.
- Counsel concealment, dissipation, or removal of children; flag the duty to preserve assets and the risk of status-quo violations instead.
- Treat a safety/DV disclosure as a routine item — escalate it.
- Insert generic "consult a licensed attorney" disclaimers — this is the attorney's own assessment.

---

## Instructions

1. **Jurisdiction & residency.** Identify the state and court; state the residency/durational requirement `[CITE: …]`; assess whether petitioner qualifies and when. Note venue. Flag competing jurisdictions or prior filings.
2. **Grounds & timing.** Identify available grounds (no-fault and any fault grounds); note any mandatory separation period, waiting period, or cooling-off period `[NEED: …]`.
3. **Conflict screen.** Document the conflict check result; note joint-representation prohibition; note any prior contact with the other spouse.
4. **Marital estate snapshot.** Build a preliminary asset/debt table; provisionally tag each item marital/community vs. separate; mark items needing tracing or valuation.
5. **Children & custody posture.** Summarize children, current arrangement, existing orders; run a preliminary UCCJEA home-state check; flag if custody jurisdiction is contested or sits elsewhere.
6. **Support posture.** Identify likely spousal-support and child-support exposure/entitlement at a high level; note guideline vs. discretionary `[NEED GUIDELINE: …]`; do not compute final numbers.
7. **Urgent-issue triage.** List immediate actions with deadlines: DV protective order, automatic temporary/standing orders, account/asset preservation, insurance continuation, document preservation letter.
8. **Objectives & realistic outcomes.** Map the client's stated objectives to likely ranges under the governing law; identify objectives that are unrealistic or in tension.
9. **Process-path recommendation.** Recommend litigation, mediation, or collaborative process with reasons tied to conflict level, DV presence, complexity, and cost tolerance.
10. **Next steps & scope.** List the next 30-day action items and a proposed engagement scope.

---

## Output Format

```markdown
# DIVORCE CASE ASSESSMENT — PRIVILEGED & CONFIDENTIAL ATTORNEY WORK PRODUCT

**Client:** {name}   **Matter:** {short title}   **Date:** {date}
**Jurisdiction:** {state / county / court}   **Property regime:** {community / equitable / [NEED REGIME]}

## 1. Jurisdiction & Residency
- Residency requirement: {period} [CITE: …]
- Petitioner qualifies: {Yes / Not until [date] / Contested}  — Confidence: {High/Med/Low}
- Venue: {county}   Competing/prior filings: {…}

## 2. Grounds & Timing
- Grounds: {no-fault / fault} ; mandatory separation/waiting period: {…} [NEED: …]

## 3. Conflict Check
- Result: {clear / conflict noted} ; joint representation barred (MRPC 1.7)

## 4. Marital Estate Snapshot (provisional)
| Asset / Debt | Approx. value | Title | Provisional characterization | Needs |
|---|---|---|---|---|
| {item} | {$} | {whose} | Marital / Separate / Mixed | tracing / valuation |

## 5. Children & Custody Posture
- Children: {names/ages} ; current schedule: {…} ; existing order: {…}
- UCCJEA home state: {state} — Confidence: {…}

## 6. Support Posture (preliminary)
- Spousal support: {exposure/entitlement, type} ; Child support: {guideline model} [NEED GUIDELINE: …]

## 7. Urgent-Issue Triage
| Issue | Action | Deadline | Status |
|---|---|---|---|
| {DV / dissipation / standing orders / insurance / preservation} | {…} | {…} | {…} |

## 8. Objectives vs. Realistic Outcomes
- {Objective} → {likely range / tension}

## 9. Recommended Process Path
- {Litigation / Mediation / Collaborative} — because {reasons}

## 10. Next 30 Days & Proposed Scope
- [ ] {action}
- Proposed engagement scope: {…}
```

---

## Verification

- [ ] State, court, and residency requirement identified; petitioner's qualification assessed with a date if not yet met.
- [ ] Property regime (community vs. equitable) stated or flagged `[NEED REGIME]`.
- [ ] Conflict check documented; joint-representation prohibition noted.
- [ ] Asset/debt items provisionally characterized with tracing/valuation flags.
- [ ] UCCJEA home-state posture checked where children are involved.
- [ ] Urgent issues (DV, dissipation, standing orders) triaged with deadlines, not buried.
- [ ] No invented residency periods, grounds language, factor lists, or guideline numbers.
- [ ] Confidence levels stated on jurisdictional and characterization conclusions.

---

## False-Positive Prevention

| Failure mode | Correction |
|---|---|
| Assuming community property in an equitable-distribution state (or vice versa) | Confirm the regime first; the entire financial analysis turns on it |
| Treating the petitioner as qualified to file without checking the durational requirement | State the residency period [CITE] and the date qualification is met |
| Burying a DV or dissipation disclosure among routine intake items | Escalate to urgent-issue triage with an immediate action and deadline |
| Assuming the forum can decide custody | Run a UCCJEA home-state check; an existing out-of-state order may control |
| Producing definitive valuations from intake estimates | Mark values provisional; flag items needing appraisal/tracing |
| Inventing the state's best-interests factors or support guideline figures | Use [NEED FACTOR LIST] / [NEED GUIDELINE] placeholders |
| Recommending mediation/collaborative where DV is present without caveat | Note that DV may contraindicate joint process and require safety planning |
| Counseling the client to move money or children to "protect" them | Flag preservation duties and status-quo/standing-order risk instead |
| Promising the client their stated objectives are achievable | Map objectives to realistic ranges under the governing law |
| Omitting the joint-representation conflict | State that the firm cannot represent both spouses (MRPC 1.7) |
