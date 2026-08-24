---
title: "Attribution Confidence — How Sure Can You Honestly Be About Who Did This"
category: psy-ops/influence-operations
description: "Grade attribution claims about who is behind an influence operation, separating the three distinct questions of infrastructure, sponsorship, and direction, and applying explicit confidence language with stated basis. Treats 'unattributed' as the correct default and the most common honest outcome, and handles the fact that false-flag and imitation activity make the obvious attribution the one most worth doubting."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - DS-01
  - QA-01
difficulty: advanced
tags:
  - psy-ops
  - attribution
  - confidence
  - intelligence-analysis
  - influence-operations
updated: "2026-07-28"
reasoning:
  styles: [analytic, adversarial, evidential, abductive]
  stakes: high
  horizon: months
  uncertainty: deep_uncertainty
  evidence_quality: weak
  domain_complexity: cross_domain
  collaboration: solo_or_team
  output_format: graded_attribution_judgment
  user_role: [analyst, researcher, journalist, policy]
  mode: [assess, audit, document]
related_prompts:
  - domain-psy-ops/influence-operations/psyops_influence_operation_analysis.md
  - domain-psy-ops/influence-operations/psyops_coordinated_inauthentic_behavior_indicators.md
  - domain-reasoning-craft/epistemic/epistemic_evidence_quality_score.md
---

# Attribution Confidence Assessment

**Objective:** Grade how confidently an influence operation can be attributed, holding apart three questions that are routinely merged into one: **who built and ran the infrastructure**, **who paid for it**, and **who directed it**. Evidence about one says surprisingly little about the others. Contractors run operations for clients they never meet; states fund proxies they do not task; enthusiastic volunteers replicate a sponsor's messaging with no contact of any kind.

Attribution is the hardest claim in this field and the one most often wrong, and its errors are consequential — they drive diplomatic incidents, sanctions, platform policy, and public accusation against organizations and countries. This prompt therefore treats **unattributed as the correct default**. Most operations are never confidently attributed by open-source analysis, and reporting "unattributed" is the honest and common outcome rather than an analytic failure. It also builds in the specific hazard that the most obvious attribution deserves the most scrutiny: imitation is cheap, false-flag construction is a known technique, and analysts who expect a particular actor find that actor's signatures.

**When to use:**
- You have established that an operation exists and must state who is behind it.
- Someone has attributed an operation and you need to assess whether the evidence supports it.
- You are writing up findings that will be read as an accusation against an organization or state.
- You are deciding whether attribution is publishable at all.

**When NOT to use:**
- You have not yet established that an operation exists — do that first with `psyops_influence_operation_analysis.md`.
- You want to assess coordination rather than sponsorship — use `psyops_coordinated_inauthentic_behavior_indicators.md`.
- You want to grade general evidence quality without the attribution frame — use `domain-reasoning-craft/epistemic/epistemic_evidence_quality_score.md`.

**Audience:** Analysts, researchers, journalists, and policy staff who must state or evaluate an attribution.

---

## Inputs / Context

1. **The established activity.** What you have already assessed as coordinated or inauthentic, at what confidence. Attribution cannot exceed this.
2. **The proposed attribution.** Who is being named, and by whom — you, a prior report, a platform disclosure, or a government statement.
3. **The evidence by type.** Technical/infrastructure, linguistic, behavioral, temporal, financial, and testimonial — kept separate because they have very different strengths.
4. **Prior reporting.** Existing attributions of the same actor, and whether they were independently verified or are being repeated.
5. **Your expectations.** Which actor you expected before looking. This is an input because expectation drives attribution error more than any evidentiary weakness.
6. **The consequence.** What the attribution will be used for, which sets the required threshold.

---

## Constraints

### Must
- Assess **infrastructure, sponsorship, and direction as three separate findings**, each with its own confidence.
- Use explicit confidence language — **low / moderate / high** — with the basis stated for each, and define what each band means in this assessment.
- Treat **unattributed** as a valid, complete, and common outcome.
- Run the **false-flag and imitation pass**: what would the evidence look like if a third party were imitating the named actor, and can you distinguish?
- Weight evidence by **fabricability**: how cheaply could each indicator be faked or planted by someone wanting this attribution made?
- Distinguish **capability, motive, and evidence**. Capability and motive narrow a field; only evidence attributes.
- State the **consequence-calibrated threshold**: what confidence is required given how the attribution will be used.
- Note explicitly where you are **relying on prior attributions** rather than independent evidence, and whether those were themselves independently established.

### Must Not
- Attribute on capability and motive. Many actors have both for almost any operation; this is the most common attribution error and it reliably produces the geopolitically expected answer.
- Treat language, time zone, or working-hours evidence as strong. All are cheap to fake and frequently reflect a contractor's location rather than a client's.
- Merge the three questions. "Russian-linked," "Iranian-backed," and "state-directed" are different claims with different evidence, and collapsing them is how overreach happens.
- Fabricate infrastructure overlaps, technical indicators, financial links, or prior report findings.
- Name individuals. Attribution at the individual level requires legal-standard evidence that open-source analysis does not produce.
- Launder confidence by repetition — citing three reports that all trace to one original as three sources.
- Present attribution as settled when the underlying activity assessment was itself low confidence.

---

## Instructions

### Step 1 — Record your prior expectation
Which actor did you expect before examining evidence? Name it. Expectation is the dominant source of attribution error and it cannot be corrected for unless it is written down.

### Step 2 — Cap against the underlying assessment
State the confidence of your finding that an operation exists at all. Attribution confidence cannot exceed it, and frequently should be well below.

### Step 3 — Sort evidence by type and fabricability
Tabulate each indicator: type, what it supports, and how cheaply a third party could fake or plant it. Language artifacts, time zones, and stylistic tells are cheap. Sustained infrastructure and financial links are expensive.

### Step 4 — Assess infrastructure separately
Who built and operated the technical and organizational apparatus? This is often the best-evidenced of the three, and it frequently identifies a contractor rather than a principal.

### Step 5 — Assess sponsorship separately
Who paid? Financial evidence is the strongest attribution evidence available and the least often obtainable. Absence here is normal; record it as absence.

### Step 6 — Assess direction separately
Who set objectives? This is the weakest-evidenced of the three and the one most often asserted. Alignment of messaging with a state's interests is not evidence of tasking.

### Step 7 — Run the false-flag and imitation pass
Construct the scenario where a third party deliberately produced this evidence to implicate the named actor. Ask what would look different. If nothing would, say so and cap confidence at low.

### Step 8 — Adversarial check and graded judgment
Argue for the null: this is unattributable from available evidence. Then state each of the three findings with confidence and basis, apply the consequence-calibrated threshold, and say whether attribution is publishable.

---

## False-Positive Prevention

1. **Capability-and-motive attribution.** The dominant failure. It reliably yields the expected geopolitical answer and is not evidence.
2. **Expectation-driven pattern matching.** Finding an actor's signature because you were looking for it. Recording the prior expectation is the only real defense.
3. **Cheap indicators weighted heavily.** Language, keyboard layout, time zone, and working hours are trivially faked and often reflect subcontractors.
4. **Confidence laundering by repetition.** Three reports tracing to one original are one source. Check whether prior attributions were independently established.
5. **The three questions merged.** Evidence of infrastructure presented as evidence of direction. State which question each indicator addresses.
6. **False-flag blindness.** Never asking what deliberate misdirection would look like. Where you cannot distinguish it, confidence is capped at low.
7. **Attribution exceeding the base finding.** Confidently naming a sponsor for activity you only weakly established as coordinated.
8. **Consequence blindness.** Applying a research-note threshold to an attribution that will be read as a public accusation against a state or organization.

---

## Output Format

```
# Attribution assessment — [operation]

## Prior expectation (recorded first)
[Which actor I expected before looking, and why]

## Cap: underlying activity assessment
[Confidence that coordinated/inauthentic activity exists at all] — attribution cannot exceed this.

## Confidence band definitions (for this assessment)
- Low: [what it means here]
- Moderate: [what it means here]
- High: [what it means here]

## Evidence by type and fabricability
| Indicator | Type | Supports which question | Fabricability | Weight |
|---|---|---|---|---|
| [item] | linguistic | infrastructure | cheap | low |
| [item] | financial | sponsorship | expensive | high |

## The three findings
| Question | Finding | Confidence | Basis |
|---|---|---|---|
| Who built/ran the infrastructure | [actor or "unattributed"] | low/mod/high | [...] |
| Who funded it | [actor or "unattributed"] | low/mod/high | [...] |
| Who directed it | [actor or "unattributed"] | low/mod/high | [...] |

## False-flag / imitation pass
[What the evidence would look like if a third party were imitating the named actor;
whether I can distinguish; if not, confidence capped at low]

## Reliance on prior reporting
[Which findings rest on others' attributions; whether those were independently established
or trace to a single original]

## Consequence-calibrated threshold
[How this will be used → required confidence → met or not met]

## Judgment
[Attributable at X confidence to Y for question Z / **Unattributed** — the default and a valid result]

## Publishable?
[Yes / yes with hedges as written / no — because ...]

## Adversarial check
[The case that this is unattributable from what I have]
```

---

## Verification

- [ ] Prior expectation is recorded before the evidence assessment.
- [ ] Infrastructure, sponsorship, and direction are assessed as three separate findings with separate confidences.
- [ ] Attribution confidence does not exceed the confidence that the operation exists.
- [ ] Every indicator is rated for fabricability, and cheap indicators are weighted low.
- [ ] Capability and motive are used only to narrow the field, never to attribute.
- [ ] The false-flag/imitation pass was run, and confidence is capped at low where it cannot be distinguished.
- [ ] Reliance on prior reporting is disclosed, and repeated citations tracing to one original are counted once.
- [ ] "Unattributed" was available and was not avoided for being unsatisfying.
- [ ] No individual is named; no technical, financial, or prior-report finding was invented.
- [ ] The consequence-calibrated threshold is stated and the publishability call follows from it.
