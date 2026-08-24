---
title: "Narrative Lifecycle Tracker — Seeding, Amplification, Mainstreaming, Laundering"
category: psy-ops/influence-operations
description: "Track a narrative through its stages — origination, seeding into receptive communities, amplification, crossover to mainstream attention, and laundering into citable legitimacy — recording what changed at each transition and which actors were load-bearing. Distinguishes a pushed narrative from one that simply resonated, and identifies the stage where intervention would still have mattered."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - DS-01
  - QA-01
difficulty: advanced
tags:
  - psy-ops
  - narrative
  - diffusion
  - media-analysis
  - influence-operations
updated: "2026-07-28"
reasoning:
  styles: [analytic, systems, evidential]
  stakes: high
  horizon: months
  uncertainty: ambiguity
  evidence_quality: variable
  domain_complexity: cross_domain
  collaboration: solo_or_team
  output_format: lifecycle_map_with_transitions
  user_role: [analyst, journalist, communications, researcher]
  mode: [assess, document, synthesize]
related_prompts:
  - domain-psy-ops/influence-operations/psyops_information_laundering_chain_map.md
  - domain-psy-ops/technique-analysis/psyops_framing_and_narrative_analysis.md
  - domain-psy-ops/counter-messaging/psyops_prebunking_inoculation_design.md
---

# Narrative Lifecycle Tracker

**Objective:** Map how a narrative moved from wherever it started to wherever it is now, staged: **origination**, **seeding** into receptive communities, **amplification**, **crossover** into mainstream attention, and **laundering** into a form that can be cited as established. The value is in the transitions rather than the stages — most narratives die between seeding and amplification, so the ones that cross a boundary reveal what carried them, and which actors were genuinely load-bearing rather than merely present.

The tracker distinguishes two shapes that look alike in a final snapshot: a narrative that was **pushed** through the stages by concentrated effort, and one that **resonated** and moved itself because it articulated something an audience already felt. Both end up mainstream. Only the first has a coordinator, and only the first can be disrupted by addressing the coordinator. Confusing them produces counter-strategy aimed at the wrong thing — usually at a handful of visible amplifiers who were downstream passengers.

**When to use:**
- A narrative has reached mainstream attention and you need to reconstruct how.
- You are deciding where to intervene and need to know which stage is still open.
- You are writing up a case study of how a claim became conventional wisdom.
- You need to distinguish a manufactured narrative from a genuine shift in public sentiment.

**When NOT to use:**
- You are tracing a single artifact's chain of custody — use `../technique-analysis/psyops_provenance_and_transmission_trace.md`.
- You are specifically mapping outlet-to-outlet legitimacy laundering — use `psyops_information_laundering_chain_map.md`.
- You want to analyze how the narrative is constructed rather than how it travelled — use `../technique-analysis/psyops_framing_and_narrative_analysis.md`.

**Audience:** Analysts, journalists, communications and policy staff, and researchers reconstructing how a claim took hold.

---

## Inputs / Context

1. **The narrative.** Stated as a proposition, in its current mainstream form.
2. **Its earliest known form.** How it was phrased when you first find it — usually materially different, and the difference is the finding.
3. **The timeline.** Dates for the appearances you can evidence, with gaps marked as gaps.
4. **Communities and outlets involved.** Where it appeared at each stage, and their audiences.
5. **The receptive substrate.** What the audience already believed or feared that made this land. Narratives do not propagate in a vacuum.
6. **Countervailing efforts.** Any correction, debunk, or competing narrative, and what happened to it.

---

## Constraints

### Must
- Track the **mutation of the proposition** across stages. Narratives sharpen, lose hedges, and acquire specificity as they travel; record the exact wording at each stage.
- Identify **transition events** — the specific post, article, broadcast, or endorsement that carried it across a boundary.
- Distinguish **load-bearing actors** (removal would have stopped it) from **passengers** (high volume, no causal role).
- Assess **push versus resonance** explicitly, with evidence for whichever you conclude.
- Characterize the **receptive substrate**: what pre-existing belief or grievance the narrative attached to.
- Identify the **latest stage at which intervention was still viable**, and what it would have had to be.
- Mark **gaps in the timeline** as gaps rather than smoothing them into a continuous story.

### Must Not
- Construct a clean linear chain from fragmentary evidence. Real diffusion is messy, parallel, and often has several independent origins.
- Assume the loudest amplifier is the cause. Visibility and causal weight are frequently inverse.
- Treat resonance as proof of authenticity, or push as proof of falsity. A pushed narrative can be true; a resonant one can be false.
- Fabricate dates, outlets, engagement figures, or intermediate hops to complete the chain.
- Name private individuals as narrative originators. Early posting is not authorship, and this finding directs harassment.
- Ignore the substrate and describe the audience as passively injected. Narratives that take hold usually articulate a real grievance, however badly.

---

## Instructions

### Step 1 — State the narrative in both forms
Current mainstream phrasing, and earliest phrasing found. Put them side by side; the drift between them is the first finding.

### Step 2 — Establish the receptive substrate
What did the audience already believe, fear, or resent that this attached to? A narrative with no substrate does not propagate regardless of push.

### Step 3 — Map the stages with evidence
For each of origination, seeding, amplification, crossover, and laundering: where, when, in what form, and with what evidence. Mark stages you cannot evidence as unevidenced rather than inferring them.

### Step 4 — Identify the transition events
Pinpoint what specifically carried it across each boundary: a particular broadcast, an endorsement by someone with a different audience, a mainstream outlet's first coverage — including coverage that was debunking it.

### Step 5 — Separate load-bearing actors from passengers
For each significant actor, ask the counterfactual: if this actor had not participated, does the narrative still cross the next boundary? Most high-volume accounts fail this test.

### Step 6 — Assess push versus resonance
Evidence of push: concentrated early effort, coordination indicators, spend, effort disproportionate to organic interest. Evidence of resonance: broad independent uptake, rapid mutation into local variants, spread through unconnected communities. Both can be present; say which dominates and how you know.

### Step 7 — Track the countervailing efforts
What corrections appeared, when, and what happened to them? Note where a debunk amplified the narrative by introducing it to a new audience.

### Step 8 — Adversarial check and intervention window
Argue that this narrative spread entirely organically because it resonated, and that the actors you flagged were incidental. Then state the last viable intervention point and what it would have required.

---

## False-Positive Prevention

1. **Retrospective linearity.** Building a clean chain from scattered evidence because the story reads better. Diffusion is parallel and multi-origin; mark the gaps.
2. **Loudest-equals-cause.** Assigning causal weight to the highest-volume amplifier. Run the counterfactual on every actor before calling them load-bearing.
3. **Push assumed from success.** Treating any narrative that reaches the mainstream as pushed. Most successful narratives resonate; concentrated effort is a separate, evidenced claim.
4. **Substrate blindness.** Describing an audience as injected with a narrative rather than as having a grievance the narrative articulated. This produces counter-strategy that insults the audience and fails.
5. **Origin naming.** Identifying a private individual as the originator on the basis of an early post. It is usually wrong and it directs harassment at someone who was themselves a recipient.
6. **Debunk-blindness.** Missing that corrective coverage was itself a transition event, carrying the narrative to audiences who had not encountered it.
7. **Truth-status conflation.** Letting the narrative's falsity imply it was pushed, or its resonance imply it is true. Independent axes.
8. **Fabricated intermediate hops.** Inventing a plausible bridging step to connect two evidenced points. An unevidenced gap stays a gap.

---

## Output Format

```
# Narrative lifecycle — [narrative]

## The proposition, then and now
- Earliest form found: "[verbatim]" — [date, where]
- Current mainstream form: "[verbatim]" — [date, where]
- **Drift:** [what sharpened, what hedges were dropped, what specificity was acquired]

## Receptive substrate
[What the audience already believed, feared, or resented that this attached to]

## Stage map
| Stage | When | Where | Form at this stage | Evidence | Confidence |
|---|---|---|---|---|---|
| Origination | [date or "not established"] | | | | |
| Seeding | | | | | |
| Amplification | | | | | |
| Crossover | | | | | |
| Laundering | | | | | |

**Timeline gaps:** [unevidenced periods, marked as gaps]

## Transition events
| Boundary crossed | What carried it | Evidence |
|---|---|---|

## Actors: load-bearing vs passengers
| Actor | Volume | Counterfactual: does it still cross without them? | Verdict |
|---|---|---|---|
| [ref] | high | yes | passenger |

## Push vs resonance
[Which dominates, with the evidence for it — and the evidence for the other]

## Countervailing efforts
[Corrections, when, effect — including any that amplified]

## Intervention window
[Latest stage where intervention was still viable, and what it would have had to be]

## Adversarial check
[The case that this was purely organic resonance and my flagged actors were incidental]

## Unknowns
[All [VERIFY] and unevidenced stages]
```

---

## Verification

- [ ] The proposition is quoted in both its earliest and current forms, with the drift between them named.
- [ ] The receptive substrate is characterized; the audience is not described as passively injected.
- [ ] Unevidenced stages and timeline gaps are marked as gaps, not smoothed over.
- [ ] Every actor called load-bearing passed an explicit counterfactual test.
- [ ] Push versus resonance is assessed with evidence for both readings, not assumed from the narrative's success.
- [ ] Corrective efforts are tracked, including any that amplified the narrative.
- [ ] No private individual is named as originator; early posting is not treated as authorship.
- [ ] The narrative's truth status is kept independent of whether it was pushed.
- [ ] No dates, outlets, metrics, or intermediate hops were invented to complete the chain.
- [ ] A specific intervention window is identified with what it would have required.
