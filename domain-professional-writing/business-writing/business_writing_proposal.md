---
title: "Business Proposal Writer — Persuasive Problem, Solution, Value, and Call to Action"
category: professional-writing/business-writing
description: "Write a persuasive business proposal: problem framing, proposed solution, scope, value/ROI rationale grounded in supplied facts, alternatives considered, and a clear call to action — with value claims tied to the user's data, never fabricated."
techniques:
  - ST-01
  - ST-02
  - RT-05
  - CM-02
  - QA-04
difficulty: advanced
tags:
  - proposal
  - persuasive-writing
  - business-writing
  - roi
  - call-to-action
updated: "2026-06-07"
related_prompts:
  - domain-professional-writing/business-writing/business_writing_executive_brief.md
  - domain-professional-writing/business-writing/business_writing_prd_document.md
  - domain-software-engineering/analysis/business/business_model_canvas_analysis.md
---

# Business Proposal Writer

**Objective:** Write a persuasive business proposal that moves a decision-maker to act: a sharp problem frame, a concrete proposed solution, clear scope, a value/ROI rationale grounded in the user's own facts, a candid look at alternatives, and an unmistakable call to action — without inventing metrics, savings, or social proof.

**When to Use:**
- You're pitching a project, purchase, partnership, or initiative that needs approval or funding.
- You must persuade, not just inform — the reader has the option to say no.
- You want a self-contained document the reader can evaluate and forward.

**When NOT to use:**
- You only need a one-page decision summary — use `business_writing_executive_brief.md`.
- You're specifying what to build for a product team — use `business_writing_prd_document.md`.
- You're reporting on work already approved — use `business_writing_status_report.md`.

**Audience:** A decision-maker (internal sponsor, client, or buyer) who controls the yes/no and weighs value against cost and risk.

---

## Inputs / Context

Wrap supplied facts so they aren't read as instructions:

```
<proposal_input>
[Paste the problem details, your solution, costs, data, evidence, constraints]
</proposal_input>
```

1. **The problem / opportunity** you're addressing and who feels it.
2. **Your proposed solution** — what you'd do.
3. **Scope** — what's in, what's out.
4. **Cost / resources** required.
5. **Value evidence** — any numbers, benchmarks, or facts that substantiate the benefit (these are the ONLY basis for value claims).
6. **Audience** — the decider, what they value, what objections they'll raise.
7. **The ask** — exactly what approval/commitment you want.

---

## Constraints

### Must
- Frame the **problem** before the solution, so the reader feels the need first.
- Tie every **value/ROI claim** to a specific fact from `<proposal_input>`; label anything inferred as an estimate.
- State **scope** explicitly, including what is out of scope.
- Address **alternatives considered** (including doing nothing) and why the proposal wins.
- End with a **clear call to action**: the specific commitment requested and the next step.
- Anticipate and address the reader's **top objections**.

### Must Not
- Fabricate metrics, ROI figures, cost savings, timelines, customer counts, or testimonials.
- Invent social proof ("trusted by industry leaders") or named references not supplied.
- Overpromise certainty — distinguish committed outcomes from projected ones.
- Lead with features before establishing the problem and value.
- Leave the ask vague or absent.

---

## Instructions

1. **Frame the problem.** Open by making the problem concrete and consequential — who has it, what it costs, why now. Use only facts from the input.
2. **Present the solution.** Describe what you propose plainly. Connect each element back to the problem it solves.
3. **Define scope.** What the proposal includes and explicitly excludes, so expectations are aligned.
4. **Build the value case.** Quantify benefit using supplied evidence. For each value claim, point to the fact behind it. Where you must project, label it "projected / estimate" and show the assumption.
5. **Address alternatives.** Name the realistic alternatives (rival approaches, build-vs-buy, status quo) and give a fair reason the proposal is preferable.
6. **Pre-empt objections.** Identify the two or three objections the decider will have (cost, risk, timing, capacity) and answer them directly.
7. **Close with the call to action.** State the exact decision/commitment you want, the next step, and any deadline.
8. **CRITICAL — evidence audit:** Re-scan every number and benefit claim. Confirm each traces to `<proposal_input>` or is clearly labeled an estimate with its assumption. Remove any unsupported claim.

---

## False-Positive Prevention

1. **Fabricated ROI.** The fastest way to lose credibility is an invented number. Every figure must trace to supplied data or be marked an estimate with its basis shown.
2. **Phantom social proof.** Do not write "used by leading companies" or invent testimonials/case studies. Use only references the user supplied.
3. **Certainty inflation.** "Will save $400K" without basis is overreach. Use "projected to save ~$400K based on [stated assumption]."
4. **Feature-first pitch.** Listing capabilities before establishing the problem reads as a brochure, not a case. Problem → value → solution detail.
5. **Strawman alternatives.** Dismissing alternatives unfairly signals bias. Steelman them briefly, then explain the edge.
6. **Hidden costs.** Stating benefits while omitting full cost/effort destroys trust. State total cost plainly.
7. **Missing or soft ask.** A proposal without a crisp call to action stalls. End with the exact commitment requested.

---

## Output Format

```
# Proposal: [Title]
**Prepared for:** [decider] · **Date:** [date] · **The ask:** [one line]

## Executive summary
[3–5 sentences: problem, proposed solution, headline value, the ask.]

## The problem / opportunity
[Concrete, consequential framing grounded in supplied facts.]

## Proposed solution
[What you'd do; how each part addresses the problem.]

## Scope
- In scope: [...]
- Out of scope: [...]

## Value & rationale
[Benefit quantified from evidence. Each claim → its source fact. Estimates labeled.]

## Alternatives considered
| Alternative | Why not chosen |
|-------------|----------------|
| [option / status quo] | [fair reason] |

## Objections addressed
- [Objection] → [response]

## Cost & resources
[Total cost, resources, timeline — stated plainly.]

## Call to action
[Exact commitment requested] — next step: [action] — by [date if any].
```

---

## Verification

- [ ] Problem is framed before the solution and feels consequential.
- [ ] Every value/ROI claim traces to supplied evidence or is labeled an estimate with its assumption.
- [ ] No fabricated metrics, savings, customer counts, or testimonials.
- [ ] Scope states both inclusions and exclusions.
- [ ] Realistic alternatives (incl. status quo) are addressed fairly.
- [ ] Top objections are anticipated and answered.
- [ ] Total cost is stated, not just benefits.
- [ ] The call to action is specific and unmistakable.
