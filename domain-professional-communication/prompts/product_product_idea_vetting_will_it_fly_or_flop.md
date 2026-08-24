---
title: "Product Idea Vetting — Will It Fly or Flop? Fast Structured Gut-Check"
category: professional-communication/product-management
description: "Fast solo vetting of a raw product idea against demand, feasibility, risk, and timing dimensions. Outputs a FLY / FLOP / RESHAPE verdict with explicit reasoning and the single biggest kill-risk. A structured gut-check, not a full validation study."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - DS-06
  - QA-04
difficulty: beginner
tags:
  - idea-validation
  - product-strategy
  - go-no-go
  - risk-assessment
  - early-stage
updated: "2026-06-07"
related_prompts:
  - domain-idea-to-product/stage-1-ideation/ideation_concept_legs_test.md
  - domain-professional-communication/prompts/product_competitor_feature_teardown.md
  - domain-professional-communication/prompts/product_create_prd.md
---

# Product Idea Vetting — Will It Fly or Flop?

**Objective:** Give a raw product idea a fast, structured gut-check across four make-or-break dimensions (demand, feasibility, risk, timing) and return a single clear verdict — FLY, FLOP, or RESHAPE — with the reasoning made explicit and the one biggest kill-risk named.

**When to Use:**
- You have a raw idea and want a fast, honest read before investing more time.
- You need to decide whether an idea is worth a deeper validation effort at all.
- You want to surface the single thing most likely to kill the idea, early.
- You are choosing between several ideas and need a comparable scoring lens.

**When NOT to use:**
- You have already decided to build and need an architecture or build plan — use `product_planning_coding_roadmap.md`.
- You need a rigorous, multi-perspective concept stress-test with kill/reshape branching — use `domain-idea-to-product/stage-1-ideation/ideation_concept_legs_test.md` (this prompt is the faster, lighter cousin).
- You need real market sizing or customer-discovery data — this is a reasoning gut-check, not a research study.

---

## Inputs / Context

Provide what you can; the prompt will flag gaps rather than invent answers.

1. **The idea** — one or two sentences. What is it, who is it for?
2. **The problem it solves** — what pain or job-to-be-done does it address?
3. **Target user** — who specifically would use/buy it?
4. **Why now** — what changed (tech, behavior, regulation, cost) that makes this timely?
5. **Your unfair advantage (if any)** — skills, access, audience, data you have that others don't.
6. **Known constraints** — budget, time, team size, technical limits.
7. **Closest existing alternatives** — what people use today instead (including "nothing / a spreadsheet").

If a field is blank, treat it as a known unknown — do not fabricate a value.

---

## Constraints

### Must
- Score each of the four dimensions (Demand, Feasibility, Risk, Timing) on a 1–5 scale with a one-line justification.
- Identify the **single biggest kill-risk** — the one thing most likely to make this fail — and state it plainly.
- Return exactly one verdict: **FLY**, **FLOP**, or **RESHAPE**.
- Distinguish stated facts (from the user's inputs) from inferences (your reasoning) — label inferences as such.
- For RESHAPE, name the specific pivot that would move it toward FLY.
- Attach a confidence level (High / Medium / Low) to the overall verdict, driven by how much real input was provided.
- Name the cheapest next test that would most reduce uncertainty on the biggest kill-risk.

### Must Not
- Invent market data, user counts, competitor numbers, or revenue figures.
- Default to encouragement — a FLOP verdict must be given plainly when warranted.
- Hide behind "it depends" without committing to a verdict.
- Treat a missing input as a positive or negative signal — treat it as an unknown and lower confidence.
- Recommend building before the biggest kill-risk has a cheap test attached.

---

## Instructions

1. **Restate the idea in one sentence.** If you cannot, the idea is too vague to vet — say so and ask for sharpening before scoring.

2. **Separate facts from gaps.** List what the user actually told you vs. what is missing. Missing inputs lower verdict confidence; they are not assumed good or bad.

3. **Score the four dimensions (RT-02 — multi-dimensional):**
   - **Demand (1–5):** Is the pain real, frequent, and acute enough that someone would change behavior or pay? Pull from the stated problem and alternatives.
   - **Feasibility (1–5):** Can this be built and delivered within the stated constraints? Consider technical, operational, and distribution feasibility.
   - **Risk (1–5, where 5 = low risk):** What could go wrong — regulatory, dependency, adoption, defensibility? Higher score = fewer/smaller risks.
   - **Timing (1–5):** Is "why now" credible? Too early (no infrastructure/behavior), too late (market saturated), or in the window?
   - One-line justification per score. Mark any score driven mostly by inference (not user input) with *(inferred)*.

4. **Name the single biggest kill-risk.** Across all four dimensions, what one factor, if it goes the wrong way, sinks the idea? State it in one sentence. This is the headline.

5. **Reach a verdict (DS-06 — prioritized judgment):**
   - **FLY:** Demand and Timing are strong (≥4), no single kill-risk is fatal, feasibility is within reach. Worth a deeper validation effort.
   - **FLOP:** A dimension scores 1–2 in a way that cannot be cheaply fixed, OR the biggest kill-risk is structural and unaddressable. Say so plainly.
   - **RESHAPE:** The core has a strong leg (usually Demand) but one dimension is weak in a fixable way. Name the specific pivot.

6. **Attach confidence (QA-04).** High only if most inputs were provided and the kill-risk is well understood. Low if scoring leaned heavily on inference.

7. **Name the cheapest next test.** What single, low-cost action (a few customer conversations, a landing-page smoke test, a technical spike, a regulatory check) would most reduce uncertainty on the biggest kill-risk?

---

## False-Positive Prevention

1. **Optimism bias.** Do not let an exciting idea inflate Demand. Demand is about *observed behavior or willingness to pay*, not how cool the idea sounds. If the only evidence is the founder's enthusiasm, score Demand as *(inferred)* and cap confidence at Medium.
2. **Fabricated market signals.** Never state "the market is $X billion" or "competitors have N users" unless the user supplied it. Say "market size unknown — verify."
3. **Feasibility hand-waving.** "It's just an app" is not feasibility analysis. If the hardest technical or operational piece is unclear, lower the Feasibility score and flag the unknown.
4. **Confusing novelty with timing.** Being first is not the same as being timely. Ask whether the enabling conditions (infrastructure, user behavior, cost curves) actually exist yet.
5. **Verdict-dodging.** "It could work if everything goes right" is not a verdict. Commit to FLY/FLOP/RESHAPE based on the most likely path, then state what would change it.
6. **Mistaking a feature for a product.** If the idea is a feature a dominant incumbent would add for free, that belongs in the kill-risk, not buried.
7. **Treating absent inputs as neutral-positive.** Missing data lowers confidence; it never raises a score.
8. **Over-reshaping.** Don't reshape every idea to avoid saying FLOP. Some ideas should be killed; reshape only when a genuinely strong leg exists.

---

## Output Format

```
# Idea Vetting: [idea in one sentence]

## What I was told vs. what's missing
- Provided: [...]
- Missing (lowers confidence): [...]

## Dimension Scores
| Dimension          | Score (1–5) | Justification                          |
|--------------------|-------------|----------------------------------------|
| Demand             | [n]         | [...] [(inferred) if applicable]       |
| Feasibility        | [n]         | [...]                                   |
| Risk (5=low risk)  | [n]         | [...]                                   |
| Timing             | [n]         | [...]                                   |

## Biggest Kill-Risk
[One sentence: the single thing most likely to make this fail.]

## Verdict: FLY | FLOP | RESHAPE
[2–4 sentences of reasoning. If RESHAPE, state the specific pivot. If FLOP, say plainly why and whether any salvageable core remains.]

**Confidence:** High | Medium | Low — [why, tied to input completeness]

## Cheapest Next Test
[The one low-cost action that most reduces uncertainty on the kill-risk.]
```

---

## Verification

- [ ] Idea restated in one clear sentence (or flagged as too vague).
- [ ] Facts separated from gaps; missing inputs listed.
- [ ] All four dimensions scored 1–5 with one-line justifications.
- [ ] Inference-driven scores marked *(inferred)*.
- [ ] Single biggest kill-risk named in one sentence.
- [ ] Exactly one verdict given: FLY, FLOP, or RESHAPE.
- [ ] RESHAPE verdicts include a specific pivot.
- [ ] Confidence level attached and tied to input completeness.
- [ ] Cheapest next test targets the kill-risk.
- [ ] No fabricated market, competitor, or revenue figures.
