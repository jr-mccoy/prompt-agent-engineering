---
title: "Prenup / Postnup Enforceability Analysis"
category: legal/divorce
description: "Analyze the enforceability of a prenuptial or postnuptial agreement under the controlling state's framework (UPAA/UPMAA or state law): assess voluntariness/duress, adequacy of financial disclosure or waiver, unconscionability (at execution and/or at enforcement), independent counsel, timing, and any state-specific formalities — building either a challenge roadmap or an enforcement-defense memo with element-by-element strength and confidence levels."
techniques:
  - ST-01
  - ST-02
  - ST-03
  - RT-01
  - RT-02
  - RT-05
  - RP-01
  - CM-02
  - QA-01
  - QA-12
difficulty: advanced
tags:
  - legal
  - divorce
  - family-law
  - prenuptial
  - enforceability
  - unconscionability
updated: "2026-06-01"
related_prompts:
  - domain-legal/divorce/legal_prenuptial_postnuptial_agreement_drafter.md
  - domain-legal/divorce/legal_marital_property_characterization_analysis.md
  - domain-legal/divorce/legal_spousal_support_alimony_analysis.md
  - domain-legal/divorce/legal_marital_settlement_agreement_drafter.md
  - domain-legal/research/legal_research_memo_irac.md
---

**Purpose:** Evaluate whether a premarital or marital agreement is enforceable, attacking or defending each element the state requires, and produce a challenge roadmap (for the party seeking to set it aside) or a defense memo (for the party seeking to enforce). Output is an internal analysis with element-by-element strength and confidence, not advice to the client or a guaranteed result.

**When to use:** A spouse seeks to enforce or invalidate a prenup/postnup in a dissolution; assessing a challenge before raising it; preparing for a hearing on the agreement's validity.

---

## Your Input

- **Jurisdiction:** [State; UPAA/UPMAA or state law; the state's enforceability elements and burden `[CITE: …]`]
- **Posture:** [Challenging or defending the agreement]
- **Agreement type & dates:** [Prenup/postnup; execution date; wedding date; how far apart]
- **Disclosure facts:** [What financial disclosure was made or waived; schedules attached?]
- **Voluntariness facts:** [Negotiation history, pressure, timing relative to wedding, threats]
- **Counsel facts:** [Whether each party had independent counsel or waived it]
- **Substantive terms:** [The property/support terms; how one-sided; circumstances now]
- **Execution formalities:** [Notarization/acknowledgment, witnesses, writing]
- **Change in circumstances:** [Material changes since execution relevant to enforcement-time unconscionability]

---

## Constraints

**Must:**
- State the **governing framework** and the **specific enforceability elements** and **burden of proof** for the state `[CITE: …]` — these vary materially (UPAA shifts the burden to the challenger; some states require independent counsel or second-look unconscionability).
- Analyze **each element**: voluntariness/duress, **disclosure adequacy or valid waiver**, **unconscionability** (at execution and, where the state allows, at enforcement), independent counsel, timing, and formalities.
- Distinguish **procedural** defects (how it was signed) from **substantive** unconscionability (how unfair the terms are) and apply the state's interplay between them.
- Treat **spousal-support provisions** under any heightened standard the state applies (and note child support cannot be waived).
- Assign **element-by-element strength** and an overall **confidence** for enforceability/invalidity.
- Frame conclusions as **litigation positions**, not certainties (QA-12).
- Use placeholders `[CITE: ...]`, `[NEED ELEMENT: ...]`, `[NEED: ...]` for unsupplied authority or facts.

**Must Not:**
- Invent the state's elements, burden allocation, or case law.
- Treat the agreement as automatically valid or invalid.
- Conflate procedural and substantive unconscionability.
- Assume disclosure was adequate without examining the schedules/waiver.
- Present a definitive outcome where the standard is fact-intensive.
- Insert generic "consult counsel" disclaimers.

---

## Instructions

1. **Framework & burden.** State the governing law, the elements, and who bears the burden `[CITE: …]`.
2. **Voluntariness/duress.** Assess timing, pressure, and the negotiation record.
3. **Disclosure.** Examine the schedules or waiver; assess adequacy under the state's standard.
4. **Counsel & timing.** Assess independent counsel and the execution-to-wedding interval.
5. **Unconscionability.** Analyze procedural and substantive unconscionability at execution, and at enforcement where the state permits a second look.
6. **Support provisions.** Apply any heightened support standard; confirm child support is untouched.
7. **Formalities.** Confirm writing, signatures, notarization/acknowledgment as required.
8. **Strength & roadmap.** Score each element; state the overall position and the proof or discovery that would strengthen it.

---

## Output Format

```markdown
# PRENUP/POSTNUP ENFORCEABILITY ANALYSIS — PRIVILEGED WORK PRODUCT
**State / framework:** {…} [CITE: …]   **Posture:** {challenge/defend}   **Burden:** {who}

## 1. Framework & Burden
{Elements; burden allocation} [CITE: …]

## 2. Element-by-Element Analysis
| Element | Facts | State standard | Strength (for posture) | Confidence |
|---|---|---|---|---|
| Voluntariness / duress | {…} | {…} | {strong/weak} | {…} |
| Disclosure / waiver | {…} | {…} | {…} | {…} |
| Independent counsel | {…} | {…} | {…} | {…} |
| Timing | {…} | {…} | {…} | {…} |
| Procedural unconscionability | {…} | {…} | {…} | {…} |
| Substantive unconscionability (execution / enforcement) | {…} | {…} | {…} | {…} |
| Support provision | {…} | {heightened?} | {…} | {…} |
| Formalities | {…} | {…} | {…} | {…} |

## 3. Overall Position
- {Likely enforceable / likely set aside / fact-dependent}; key vulnerabilities: {…}

## 4. Roadmap
- Proof/discovery that would strengthen the position: {…}
```

---

## Verification

- [ ] Governing framework, elements, and burden stated for the state.
- [ ] Each element analyzed with the state's standard and the facts.
- [ ] Procedural vs. substantive unconscionability distinguished and their interplay applied.
- [ ] Enforcement-time (second-look) unconscionability addressed where the state allows it.
- [ ] Support provisions analyzed under any heightened standard; child support noted as non-waivable.
- [ ] Formalities checked.
- [ ] Element strength and overall confidence assigned; conclusions framed as positions.
- [ ] No invented elements, burden rules, or case law.

---

## False-Positive Prevention

| Failure mode | Correction |
|---|---|
| Declaring the agreement valid/invalid outright | Score each element; state a fact-dependent position with confidence |
| Ignoring who bears the burden | State the burden allocation (UPAA shifts it to the challenger) [CITE] |
| Conflating procedural and substantive unconscionability | Analyze each and apply the state's sliding-scale/interplay |
| Assuming disclosure was adequate | Examine the schedules or the validity of any waiver |
| Skipping enforcement-time unconscionability | Apply the state's second-look rule where it exists |
| Treating a support waiver like a property term | Apply any heightened support standard; note child support is non-waivable |
| Inventing the state's enforceability elements | Use [CITE]/[NEED ELEMENT] placeholders |
| Overlooking the execution-to-wedding timing | Assess timing as a voluntariness/duress factor |
| Ignoring formalities (notarization/writing) | Confirm statutory execution requirements |
| Stating certainty on a fact-intensive standard | Provide confidence levels and the proof that would move them |
