---
title: "Regulatory Risk Radar"
category: decision-making
description: "Scan an industry, jurisdiction, or product surface for regulatory risks relevant to a specific product or decision. Output: a risk inventory tagged by jurisdiction and regime, probability x impact scoring, monitoring signals per risk, hedging actions, and a decision-shaped 'what to do this quarter' summary. Optimized to feed a decision, not produce a compliance audit."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - RT-03
  - DS-02
  - DS-06
  - CM-02
  - QA-01
  - QA-02
difficulty: advanced
tags:
  - decision-making
  - regulatory-risk
  - compliance
  - jurisdiction-scan
  - hedging
  - risk-radar
updated: "2026-04-26"
related_prompts:
  - domain-decision-making/decisioning_chained_alignment_evaluator.md
  - domain-decision-making/decisioning_competitive_intelligence_scanner.md
  - domain-decision-making/decisioning_crisis_severity_triage.md
  - domain-business-strategy/analysis/pestel_analysis.md
---

# Regulatory Risk Radar

**Objective:** Produce a regulatory risk radar for a specified product, business, or decision: an inventory of regulatory risks relevant in the next 6–24 months, scored on probability and impact, tagged by jurisdiction and regime, with monitoring signals per risk, hedging actions, and a one-page decision-shaped "what to do this quarter." This is a decision-feeding artifact, not a compliance program.

**When to Use:**
- A new product, geography, customer segment, or business model is being considered, and the user wants a 30-minute read on the regulatory surface before committing.
- An existing product faces a shifting regulatory landscape (AI rules, data localization, antitrust posture, sector-specific licensing) and the user must decide what to do this quarter.
- Quarterly or semi-annual radar refresh as part of a planning cycle.

**When NOT to use:**
- The user needs a formal compliance audit. Refer to qualified counsel and a compliance audit framework.
- The user needs jurisdiction-specific legal advice. This prompt is legal-input shaped scanning, not legal advice.
- The user wants a full PESTEL analysis covering political, economic, social, tech, environmental, legal. Use `pestel_analysis.md`.
- The user is responding to an active regulatory action (subpoena, investigation). Use a crisis triage prompt and engage counsel.

**Audience:** Founders, general counsel, compliance leads, product leads operating in regulated or shifting-regulated spaces, board members preparing for risk discussions.

---

## Inputs / Context

1. **Product or decision in scope.** What is being scanned. Specific. ("Launch our Series A AI-assisted underwriting tool in EU and UK markets in H2.")
2. **Jurisdictions in scope.** Country, state, region. List explicitly. If the product is sold globally, scope by where revenue or users are concentrated, plus any jurisdictions with extraterritorial reach (EU GDPR, US export controls, China DSL).
3. **Sector / regime.** Healthcare, financial services, AI/ML, advertising, communications, employment, consumer goods, energy, etc. A product can be in multiple regimes simultaneously.
4. **Time horizon.** 6, 12, 18, 24 months.
5. **Existing legal/compliance posture.** What's already in place. Counsel on retainer or in-house, certifications held (SOC 2, ISO, HIPAA, PCI), licenses obtained.
6. **Forcing function.** Why now: pre-launch decision, board ask, investor diligence, media risk, observed competitor action.
7. **Risk appetite.** How much regulatory risk the user is willing to absorb in pursuit of the opportunity. Conservative / moderate / aggressive, with a one-line definition.

If jurisdictions and sector regimes are missing, **stop**. The radar is shaped by both.

---

## Constraints

### Must
- Tag every risk with jurisdiction(s) and regime(s).
- Score every risk on probability (low / medium / high) and impact (low / medium / high), with a one-line basis for each score. Probability is the chance the risk crystallizes inside the time horizon; impact is the cost if it does.
- Distinguish **enacted** risks (already law, the question is enforcement), **proposed** risks (in legislative/regulatory pipeline), and **emerging** risks (not yet proposed but signal-detectable).
- Provide 1–3 monitoring signals per risk. Each signal must be observable (a specific regulator's docket, a named bill, a known agency, a public consultation, a court case).
- Provide 1–3 hedging actions per risk. Distinguish **avoid** (don't enter the surface), **mitigate** (do less of), **prepare** (stay but build optionality), and **accept** (proceed knowingly, with a budget for the impact).
- Output a "what to do this quarter" decision summary tied back to the in-scope decision.
- Flag every risk where the probability x impact warrants escalation to qualified counsel before the user takes action.
- Include a "what we cannot see" section listing the risks the user should expect exist but the scan cannot resolve without legal expertise.

### Must Not
- Provide legal advice. The output is risk *scanning* and *signal monitoring*; specific legal advice requires counsel.
- Treat enacted, proposed, and emerging risks as equivalent. They are not.
- Score every risk as "high impact" — that produces an unactionable list. Force differentiation.
- Recommend "wait and see" as a hedging action. That's the absence of a hedge, not a hedge.
- Conflate jurisdictions. A risk in California is not necessarily a risk in Texas; a risk in EU is not the same regime as UK post-Brexit.
- Output more than 12 risks. Past 12, the radar loses focus and the user cannot act.

---

## Instructions

### Step 1 — Restate scope, jurisdictions, regimes
One paragraph: what the user is doing, in which jurisdictions, under which regimes, on what time horizon, with what risk appetite.

### Step 2 — Generate candidate risks
For each (jurisdiction x regime) pair, generate candidate risks. Categories to walk:
- **Data and privacy.** Localization, transfer, consent, profiling.
- **Sector-specific licensing.** Operating without a license, license expiration, scope drift past license.
- **Consumer protection.** Disclosure, advertising, dark patterns, refund rules.
- **AI/algorithmic.** Model transparency, bias, automated decision-making, training-data provenance.
- **Antitrust / competition.** Pricing coordination, exclusionary contracts, M&A review.
- **Employment / labor.** Worker classification, mandatory benefits, AI-in-hiring rules.
- **Tax / cross-border.** Sales tax, VAT, digital services tax, transfer pricing.
- **Export / sanctions.** Restricted parties, dual-use tech, embargoed jurisdictions.
- **Environment / sustainability.** Disclosure, supply-chain due diligence, packaging.
- **Industry-specific.** Healthcare (HIPAA, EMA), finance (KYC/AML, PSD2), telecom, energy.

Discard categories that don't apply. Keep the rest.

### Step 3 — Tag enacted vs proposed vs emerging
For each candidate risk:
- **Enacted:** law in force in the jurisdiction. Risk is enforcement-shaped.
- **Proposed:** in legislative or regulatory pipeline; cite the bill, docket, or consultation.
- **Emerging:** not yet proposed but signal-detectable in agency speeches, regulator priorities, journalist coverage, case law, peer-jurisdiction adoption.

### Step 4 — Score probability and impact
For each risk:
- **Probability:** chance the risk crystallizes inside the time horizon. For enacted risks, probability is enforcement likelihood. For proposed risks, probability is enactment likelihood. For emerging risks, probability is movement-to-proposed likelihood.
- **Impact:** cost if it crystallizes — fines, license loss, market exit, brand damage, mandatory product change, operational rebuild.

Assign low / medium / high on each axis, with a one-line basis. The risks worth carrying past Step 5 are typically (M, H), (H, M), and (H, H).

### Step 5 — Monitoring signals
For each risk that survived prioritization, name 1–3 observable signals:
- Specific regulator + specific docket or rulemaking ID.
- Named bill + sponsor + committee status.
- Court case + court + docket number.
- Industry guidance, advisory letter, agency speech.
- Peer-jurisdiction adoption (a leading indicator for follower jurisdictions).

For each signal: where to watch, what change is meaningful, check cadence, owner.

### Step 6 — Hedging actions
For each prioritized risk, output 1–3 hedging actions tagged with the hedging type:
- **Avoid:** don't enter the surface (skip a jurisdiction, skip a use case).
- **Mitigate:** reduce exposure (limit data retention, segment a feature, gate a market).
- **Prepare:** maintain optionality (build the toggle, hold the certification, retain counsel).
- **Accept:** proceed with eyes open and budget for the impact.

For each action: cost (time, headcount, dollars), reversibility, lead time before it must be in place.

### Step 7 — Adversarial pass
Three questions:
- "Which risk is the user most likely to under-rate because they have not personally encountered it?"
- "Which jurisdiction is the user most likely to under-attend because it is not their primary market?"
- "What is the second-order regulatory consequence of the action the user is leaning toward?"

Surface 2–3 sentences each. These often reorder the radar.

### Step 8 — What to do this quarter
Tie the radar back to the in-scope decision. Output a one-page summary:
- Decision in scope.
- Top 3 risks that move the decision.
- Recommended hedge per top risk (avoid / mitigate / prepare / accept).
- Trigger condition that would force escalation to counsel.
- Open questions for legal review.

### Step 9 — What we cannot see
List the risks that almost certainly exist but the scan cannot resolve without legal expertise. Be specific about what kind of expert (jurisdictional, sector, doctrinal). This is the bridge to counsel.

---

## False-Positive Prevention

1. **Treating proposed as enacted.** A bill in committee may never pass. A draft consultation may not become a final rule. Probability scoring forces this distinction.
2. **Generic "AI regulation" handwave.** AI risk in EU (AI Act) is not AI risk in California (SB-1047 history) is not AI risk in NY (NYC AEDT). Tag jurisdictions specifically.
3. **Compliance theater.** Holding a SOC 2 does not address GDPR; ISO 27001 does not satisfy HIPAA. Don't accept a held certification as coverage for a risk it doesn't address.
4. **Over-broad impact rating.** If everything is high impact, nothing is. Force a low / medium / high distribution.
5. **Wait-and-see disguised as a hedge.** "Continue monitoring" is not a hedge. A real hedge has a cost, a lead time, and a state change.
6. **Single-jurisdiction blindness.** Products with users in multiple jurisdictions inherit the strictest jurisdiction's rules in many regimes (data, consumer protection). Tag this carefully.
7. **Extraterritorial-reach blindness.** GDPR, US sanctions, China DSL apply outside their issuing jurisdictions. A user-set in jurisdiction A can still trigger jurisdiction B's regime.
8. **Stale legal posture.** "Our counsel reviewed this last year" is often a false comfort in a fast-moving regime. Flag review staleness when relevant.
9. **Over-stepping into legal advice.** This prompt does *not* produce legal advice. Hedging actions are operational moves; legal advice is what the user gets from counsel after the radar identifies the surface.
10. **Adversarial-pass omission.** The under-rated risk is almost always the most expensive one. Skipping the adversarial pass is the most common failure mode.

---

## Output Format

```
# Regulatory risk radar — [scope] — [horizon] — [date]

**Decision in scope:** [one sentence]
**Jurisdictions:** [list]
**Regimes:** [list]
**Risk appetite:** [conservative / moderate / aggressive — with one-line definition]

## Risk inventory

| # | Risk | Jurisdiction(s) | Regime | Status | Probability | Impact | Basis (one line) |
|---|------|------------------|--------|--------|-------------|--------|-------------------|
| 1 | [...] | [...]            | [...]  | enacted/proposed/emerging | L/M/H | L/M/H | [...] |

## Prioritized risks (probability x impact)

[Risks scored (M,H), (H,M), or (H,H) carry forward.]

## Monitoring signals

| Risk # | Signal | Where to watch | Meaningful change | Cadence | Owner |
|--------|--------|-----------------|--------------------|---------|-------|
|        |        |                 |                    |         |       |

## Hedging actions

| Risk # | Hedge type | Action | Cost | Reversibility | Lead time |
|--------|------------|--------|------|----------------|-----------|
|        | avoid/mitigate/prepare/accept | [...] | [...] | high/med/low | [...] |

## Adversarial pass
- **Most under-rated risk:** [...]
- **Most under-attended jurisdiction:** [...]
- **Second-order consequence of leaning decision:** [...]

## What to do this quarter

- **Decision in scope:** [...]
- **Top 3 risks that move the decision:** [...]
- **Recommended hedge per top risk:** [...]
- **Trigger condition for counsel escalation:** [...]
- **Open questions for legal review:** [...]

## What we cannot see (bridge to counsel)

| Open question | Type of expert needed |
|----------------|------------------------|
| [...]          | jurisdictional / sector / doctrinal |
```

---

## Verification

- [ ] Every risk is tagged with jurisdiction(s) and regime.
- [ ] Every risk is tagged enacted / proposed / emerging.
- [ ] Probability and impact are scored with a one-line basis each, and the distribution is differentiated (not all high).
- [ ] Monitoring signals are observable (named docket, bill, agency, court case).
- [ ] Hedging actions are tagged avoid / mitigate / prepare / accept and have cost, reversibility, and lead time.
- [ ] The adversarial pass produced three responses.
- [ ] "What to do this quarter" ties back to the in-scope decision and includes a trigger for counsel escalation.
- [ ] "What we cannot see" lists open questions for legal review with the type of expert required.
- [ ] No "wait and see" disguised as a hedge.
- [ ] No more than 12 prioritized risks; if more were generated, the cut is justified.
