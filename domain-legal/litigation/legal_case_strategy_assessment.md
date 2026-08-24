---
title: "Case Strategy Assessment"
category: legal/litigation
description: "Produce an internal case-strategy memo: claims/defenses status, factual and legal strengths and weaknesses, damages exposure, leverage, settlement posture, and a phased work plan with decision points."
techniques:
  - ST-01
  - ST-02
  - ST-03
  - CM-02
  - DS-02
  - QA-01
difficulty: advanced
tags:
  - legal
  - litigation
  - strategy
  - case-assessment
  - settlement
updated: "2026-05-08"
related_prompts:
  - domain-legal/research/legal_issue_spotter_from_facts.md
  - domain-legal/litigation/legal_settlement_value_range_analysis.md
  - domain-legal/litigation/legal_complaint_drafter.md
---

**Purpose:** Build a candid internal strategy memo a partner could read in 10 minutes and walk into a client meeting with. Output covers where the case is, where it can go, what each side has and lacks, and what to do next.

**When to use:** New matter intake, post-discovery checkpoint, pre-MSJ assessment, mediation prep, client decision points (settle / try / appeal).

---

## Your Input

- **Matter:** [Caption, court, posture]
- **Client and role:** [Plaintiff / defendant / counter-claimant; what the client wants]
- **Procedural status:** [Pre-suit / pleading / discovery phase / pre-trial / trial / appeal]
- **Claims and defenses:** [List with controlling law]
- **Key documents:** [Contracts, communications, business records — text or summary]
- **Witnesses:** [Names, role, what each can credibly say]
- **Discovery completed and remaining:** [What's done, what's outstanding]
- **Damages model:** [Theory, computation, caps]
- **Insurance / indemnification status:** [Coverage, reservation of rights, defense control]
- **Prior settlement discussions:** [Demands, offers, mediator involvement]
- **External pressures:** [Press exposure, regulatory parallel, parallel matters]
- **Budget / runway:** [What's been spent, what's authorized]

---

## Constraints

**Must:**
- Be candid. The audience is internal counsel and the client; they need to make decisions, not feel reassured.
- Separate **factual** strengths/weaknesses from **legal** strengths/weaknesses. They are different and they trade off differently.
- Quantify where possible: damages range, fee burn rate, probability bands by element or outcome.
- Identify each side's **leverage** — not just merits — including reputational risk, regulatory exposure, witness availability, document gaps, dispositive-motion posture.
- Identify the **single most dispositional issue** that will most likely decide the case, and how to develop it.
- Identify **decision points** with what triggers each (after MTD ruling, after deposition X, after expert report Y, after summary-judgment ruling).
- Build a **phased work plan** with cost estimates and dependencies.
- End with a **client-decision frame**: settle now / continue to next decision point / try.

**Must Not:**
- Generate happy talk. Soft assessments make for surprised clients.
- Conflate certainty in liability with certainty on damages. They are separately uncertain.
- Use a single point estimate where a range is appropriate.
- Recommend "more discovery" without identifying the specific evidence needed and what decision it will inform.
- Treat sunk costs as a reason to continue.
- Present settlement value as just a number without a band, a discount, and the reasoning.

---

## Instructions

1. **One-paragraph executive summary** with the operative recommendation and the operative reason.
2. **Posture and Calendar.** Where the case is, what's pending, what the next dispositive event is.
3. **Claims / Defenses Status Table.** For each claim or affirmative defense:
   - Element status (met / disputed / unknown / likely-not).
   - Factual strength (Strong / Moderate / Weak / Adverse), with the operative fact.
   - Legal strength under the controlling law, with the operative authority gap or hook.
4. **Factual Strengths and Weaknesses.** Per side, cited to documents and witnesses.
5. **Legal Strengths and Weaknesses.** Per side, cited to authority gaps or favorable rules.
6. **Damages Exposure.** Best / likely / worst case bands with assumptions and a sensitivity table for the two or three drivers that move the number most.
7. **Leverage Map.** What each side has (and has not) outside the merits.
8. **Most Dispositional Issue.** Identify it; describe the evidence needed to win it; estimate cost and time.
9. **Decision Points.** Triggers, options at each, and information that should drive the call.
10. **Phased Work Plan.** Discovery, motions, experts, settlement, trial — with sequence, cost estimate, and dependencies.
11. **Client-Decision Frame.** Settle now / continue to next decision point / try; with a one-sentence rationale.

---

## Output Format

```markdown
# CASE STRATEGY ASSESSMENT — {MATTER}
**Privileged & Confidential — Attorney Work Product**

## Executive Summary
{One paragraph. Operative recommendation. Operative reason.}

## Posture and Calendar
- Court / posture: {...}
- Pending: {...}
- Next dispositive event: {... — date, what's at stake}

## Claims / Defenses Status

| Claim or Defense | Elements (status) | Factual strength | Legal strength | Notes |
|------------------|-------------------|------------------|-----------------|-------|

## Factual Strengths and Weaknesses
- **Our strengths:** {bullet list with document/witness ties}
- **Our weaknesses:** {...}
- **Their strengths:** {...}
- **Their weaknesses:** {...}

## Legal Strengths and Weaknesses
- **Favorable authority and rules:** {... with `[CITE: ...]` placeholders where needed}
- **Unfavorable authority and rules:** {...}
- **Open doctrinal questions:** {...}

## Damages Exposure

| Scenario | Components | Range | Drivers |
|----------|-----------|-------|---------|
| Best | ... | $X–$Y | ... |
| Likely | ... | $X–$Y | ... |
| Worst | ... | $X–$Y | ... |

**Sensitivity table:** {drivers and their effect on the number}

## Leverage Map
- Our non-merits leverage: {...}
- Their non-merits leverage: {...}
- Asymmetries: {...}

## Most Dispositional Issue
- The issue: {...}
- Why it controls: {...}
- Evidence needed to win it: {...}
- Cost / time estimate: {...}

## Decision Points

| Decision point | Trigger | Options | Information needed |
|----------------|---------|---------|---------------------|

## Phased Work Plan

| Phase | Activities | Sequence / dependencies | Cost estimate |
|-------|-----------|--------------------------|----------------|

## Client-Decision Frame

**Recommendation:** {Settle now at {range} / Continue to next decision point at {trigger} / Try the case}

**Why:** {one sentence}

**What we need from the client:** {decisions, fact development, settlement authority}

## Open Items / Information Gaps
- {...}
```

---

## Verification

- [ ] Recommendation appears in the executive summary, not buried.
- [ ] Damages presented as a range with drivers, not a point estimate.
- [ ] Each claim/defense row identifies factual and legal strength separately.
- [ ] Most dispositional issue identified with the evidence path to win it.
- [ ] Decision points carry triggers and the information needed to make the call.
- [ ] Phased work plan ties cost estimates to specific activities.
- [ ] Leverage map covers non-merits factors.
- [ ] No happy talk; weaknesses are stated plainly.
- [ ] No invented facts, witness statements, or authority.

---

## False-Positive Prevention

| Failure mode | Correction |
|---|---|
| Soft "case is strong" assessments without specifics | Tie strength claims to elements and evidence |
| Single-point damages estimate | Use a range; identify drivers and sensitivity |
| Recommending more discovery without a decision purpose | Tie every discovery item to a decision it will inform |
| Treating sunk legal spend as a reason to continue | Sunk costs are sunk; the question is forward expected value |
| Equating high merits with high settlement value | Settlement value is merits × probability − costs ± leverage; not just merits |
| Burying weaknesses in a "considerations" section | Weaknesses go in the SWOT and the recommendation |
| Ignoring insurance / indemnification dynamics | Coverage, reservation of rights, and defense control change leverage and decision rights |
| Failing to frame the client decision | Always end with a clear settle / continue / try recommendation |
