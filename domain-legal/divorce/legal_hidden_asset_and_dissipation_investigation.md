---
title: "Hidden Asset and Dissipation Investigation Plan"
category: legal/divorce
description: "Build an investigation plan to find undisclosed assets and prove marital-waste/dissipation in divorce: a red-flag inventory, a lifestyle-vs-reported-income analysis, a document and discovery roadmap (subpoenas, tax-return cross-checks, business records), a tracing plan for transfers to third parties, a forensic-accountant scope, and a dissipation claim framework under the state's standard with burden and remedy."
techniques:
  - ST-01
  - ST-02
  - ST-03
  - RT-02
  - RT-05
  - CM-02
  - QA-01
  - QA-12
difficulty: advanced
tags:
  - legal
  - divorce
  - family-law
  - hidden-assets
  - dissipation
  - forensic-accounting
updated: "2026-06-01"
related_prompts:
  - domain-legal/divorce/legal_financial_affidavit_and_disclosure_builder.md
  - domain-legal/divorce/legal_divorce_discovery_plan_and_requests.md
  - domain-legal/divorce/legal_marital_property_characterization_analysis.md
  - domain-legal/divorce/legal_business_valuation_and_division_framework.md
  - domain-legal/discovery/legal_document_request_drafter.md
---

**Purpose:** Produce a structured plan to (a) detect assets a spouse may be hiding and (b) build a marital-waste/dissipation claim — identifying red flags, the lifestyle/income gap, the documents and discovery to compel, the tracing path, the forensic-accountant scope, and the legal standard and remedy. Output is an internal investigation and discovery plan, not an accusation or a fabricated finding.

**When to use:** Reported income or disclosure does not match the observed lifestyle; suspicious transfers, new accounts, or business cash; pre-separation spending on an affair/gambling/gifts; preparing dissipation claims or aggressive financial discovery.

---

## Your Input

- **Jurisdiction:** [State; the state's dissipation/marital-waste standard, lookback period, and burden `[CITE: …]`]
- **Property regime:** [Community / equitable distribution]
- **Reported finances:** [The other spouse's disclosed income, assets, and debts]
- **Lifestyle facts:** [Spending, travel, purchases, residences, tuition, club memberships inconsistent with reported income]
- **Red-flag facts:** [New/closed accounts, transfers to family/friends, cash-heavy business, crypto, deferred bonuses, "loans" to relatives, sudden debt]
- **Business involvement:** [Ownership, control of books, related-party dealings]
- **Suspected dissipation:** [Affair spending, gambling, gifts, intentional loss/sale of assets; dates and amounts if known]
- **Documents in hand:** [Tax returns, statements, deeds, applications]
- **Available tools:** [Subpoena power, forensic accountant budget, party deposition timing]

---

## Constraints

**Must:**
- State the state's **dissipation/marital-waste standard**, the **lookback/relevant period**, the **burden of proof**, and the **remedy** (charge-back/credit) `[CITE: …]`.
- Build a **red-flag inventory** tying each indicator to the specific record or discovery that would confirm or dispel it.
- Construct a **lifestyle-vs-reported-income analysis** (sources-and-uses / net-worth method) identifying the gap, while noting it is an analytical inference, not proof.
- Provide a **document and discovery roadmap**: tax-return line cross-checks, account subpoenas to third parties, business records, loan applications (sworn statements of net worth), and deposition topics.
- Provide a **tracing plan** for transfers to third parties (potential fraudulent-transfer/joinder issues).
- Scope the **forensic accountant's** engagement; mark quantitative conclusions as requiring the expert `[NEED FORENSIC ANALYSIS]`.
- Distinguish **dissipation** (waste for a non-marital purpose) from ordinary or pre-separation spending the state does not treat as waste.
- Use placeholders `[CITE: ...]`, `[NEED FORENSIC ANALYSIS]`, `[NEED: ...]` for unsupplied authority, computations, or facts.

**Must Not:**
- Assert assets are hidden or that dissipation occurred without the supporting evidence — frame as red flags requiring proof (QA-12).
- Recommend illegal or unethical means of obtaining information (unauthorized account access, pretexting, GPS/wiretap violations).
- Invent transfer amounts, account numbers, the state's standard, or the lookback period.
- Treat the lifestyle-gap inference as conclusive proof.
- Counsel any retaliatory dissipation by the client.
- Insert generic "consult counsel" disclaimers.

---

## Instructions

1. **Legal standard.** State dissipation standard, lookback, burden, and remedy `[CITE: …]`; note fraudulent-transfer and third-party joinder where relevant.
2. **Red-flag inventory.** List each indicator with the confirming record/discovery and a likelihood note.
3. **Lifestyle/income analysis.** Lay out the sources-and-uses or net-worth method and the apparent gap; mark as inference pending forensic work.
4. **Document roadmap.** Tax-return cross-checks (Schedules B/C/E, K-1s), bank/brokerage/crypto subpoenas, business GL, loan applications, prior sworn statements.
5. **Discovery roadmap.** RFPs, interrogatories, third-party subpoenas, and deposition topics targeting the red flags.
6. **Tracing plan.** Follow transfers to third parties; identify recipients who may need to be joined.
7. **Forensic scope.** Define the accountant's tasks and deliverables; mark conclusions `[NEED FORENSIC ANALYSIS]`.
8. **Dissipation claim framework.** Map proven transactions to the state's standard; quantify the charge-back/credit sought.

---

## Output Format

```markdown
# HIDDEN-ASSET & DISSIPATION INVESTIGATION PLAN — PRIVILEGED WORK PRODUCT
**State:** {…} — dissipation standard / lookback / burden / remedy [CITE: …]   **Regime:** {…}

## 1. Legal Standard
{Standard; lookback; burden; remedy; fraudulent transfer/joinder} [CITE: …]

## 2. Red-Flag Inventory
| Indicator | Confirming record / discovery | Likelihood | Status |
|---|---|---|---|
| {transfer to relative} | {bank subpoena} | {…} | {open} |

## 3. Lifestyle vs. Reported Income (inference)
- Method: {sources-and-uses / net-worth}; apparent gap: {$ / [NEED FORENSIC ANALYSIS]}

## 4. Document Roadmap
- [ ] {Tax returns + Schedules B/C/E, K-1} ; [ ] {Bank/brokerage/crypto subpoenas} ; [ ] {Business GL} ; [ ] {Loan applications / sworn net worth}

## 5. Discovery Roadmap
- RFPs: {…} ; Interrogatories: {…} ; Third-party subpoenas: {…} ; Deposition topics: {…}

## 6. Tracing Plan
- {Transfer → recipient → potential join/avoidance}

## 7. Forensic Accountant Scope
- Tasks: {…} ; deliverables: {…} — conclusions: [NEED FORENSIC ANALYSIS]

## 8. Dissipation Claim Framework
| Transaction | Date | Amount | Purpose (non-marital?) | Maps to standard | Credit sought |
|---|---|---|---|---|---|
| {…} | {…} | {$} | {…} | {yes/no} | {$} |
```

---

## Verification

- [ ] Dissipation standard, lookback, burden, and remedy stated for the state.
- [ ] Red flags tied to specific confirming records/discovery, not asserted as fact.
- [ ] Lifestyle/income analysis framed as inference pending forensic work.
- [ ] Document and discovery roadmaps target the specific red flags.
- [ ] Tracing plan identifies third-party recipients and joinder/avoidance issues.
- [ ] Forensic scope defined; quantitative conclusions flagged as expert work.
- [ ] Dissipation claim maps transactions to the state's standard with a quantified credit.
- [ ] No invented amounts, accounts, or standards; no illegal/unethical investigative methods.

---

## False-Positive Prevention

| Failure mode | Correction |
|---|---|
| Asserting assets are hidden as established fact | Frame as red flags requiring confirming evidence (QA-12) |
| Treating the lifestyle/income gap as proof | Present it as an inference; confirm with forensic analysis |
| Recommending unauthorized account access, pretexting, or tracking | Use lawful discovery and subpoenas only |
| Calling ordinary/pre-separation spending "dissipation" | Apply the state's waste standard (non-marital purpose, relevant period) |
| Inventing transfer amounts or account numbers | Tie every figure to a record; flag gaps |
| Skipping tax-return schedules that reveal hidden income | Cross-check Schedules B/C/E and K-1s for undisclosed sources |
| Ignoring third-party recipients of transfers | Plan tracing and consider joinder/fraudulent-transfer claims |
| Stating a forensic conclusion without an expert | Mark [NEED FORENSIC ANALYSIS] and scope the engagement |
| Inventing the state's lookback period | Use [CITE]/[NEED] placeholders |
| Counseling retaliatory dissipation by the client | Advise preservation; do not counsel waste |
