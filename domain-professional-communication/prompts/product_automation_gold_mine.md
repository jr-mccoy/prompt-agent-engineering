---
title: "Automation Gold Mine — Rank a Workflow's Highest-ROI Automation Candidates"
category: professional-communication/product-management
description: "Analyze a described workflow to find the highest-ROI automation candidates, scored on frequency × effort-saved × rule-clarity (low rule-clarity = poor automation fit). Outputs a ranked shortlist and a recommended first automation."
techniques:
  - ST-01
  - ST-02
  - DT-02
  - DS-06
  - QA-04
difficulty: intermediate
tags:
  - automation
  - workflow-analysis
  - prioritization
  - roi
  - process-improvement
updated: "2026-06-07"
related_prompts:
  - domain-professional-communication/prompts/product_zombie_meeting_detector.md
  - domain-productivity/automation/automation_data_sync.md
  - domain-business-strategy/browser-automation/browserauto_weekly_audit.md
---

# Automation Gold Mine

**Objective:** Take a described workflow and identify which steps are the highest-ROI automation candidates by scoring each on frequency × effort-saved × rule-clarity, then return a ranked shortlist and a single recommended first automation to build.

**When to Use:**
- You have a repetitive workflow and want to know what to automate first.
- You suspect you're wasting time on manual steps but aren't sure which ones pay back.
- You want a defensible ranking, not a gut feeling, before investing in tooling.
- You're scoping an internal automation or RPA initiative and need to triage candidates.

**When NOT to use:**
- The workflow is a one-off — automation rarely pays back for non-recurring work.
- You specifically want to audit recurring *meetings* for async/kill decisions — use `product_zombie_meeting_detector.md`.
- You already know what to automate and need the implementation — use a domain-specific automation prompt under `domain-productivity/automation/`.

---

## Inputs / Context

1. **The workflow** — paste or describe it step by step. The more granular the steps, the better the scoring.
   - If pasting a process doc or task list, wrap it in `<workflow>...</workflow>` so it isn't mistaken for instructions.
2. **Frequency context** — how often the whole workflow runs (per day/week/month) and, if it varies, which steps repeat more than others.
3. **Who does it** — role(s) and rough hourly cost if known (used to weight effort-saved; if unknown, weight by time alone).
4. **Tools in play** — current apps/systems, and any that expose APIs or integrations.
5. **Constraints** — compliance, approval gates, data-sensitivity, or steps that legally require a human.

---

## Constraints

### Must
- Break the workflow into discrete steps before scoring (do not score the workflow as a single blob).
- Score each step on three factors, 1–5 each:
  - **Frequency** — how often this specific step runs.
  - **Effort-saved** — time/toil removed if automated (weight by hourly cost when provided).
  - **Rule-clarity** — how deterministic the decision logic is. **Low rule-clarity = poor automation fit** and must drag the score down, not up.
- Compute a composite score and rank candidates by it.
- Flag any step that requires human judgment, legal sign-off, or handles sensitive data as **human-in-the-loop**, even if otherwise automatable.
- Recommend exactly one **first automation** with rationale (usually the best ROI that is also low-risk to pilot).
- State assumptions explicitly and attach confidence to the ranking.

### Must Not
- Recommend automating steps with low rule-clarity just because they are frequent — fuzzy judgment is where automation fails.
- Invent time savings or frequencies the user did not provide; mark estimates as assumptions.
- Ignore compliance/approval constraints in pursuit of ROI.
- Collapse distinct steps so coarsely that the ranking becomes meaningless.
- Recommend a high-risk, high-blast-radius step as the *first* automation.

---

## Instructions

1. **Decompose the workflow (DT-02).** List each discrete step. If the user gave a coarse description, propose a finer breakdown and note it as your interpretation.

2. **Score each step on three factors (1–5):**
   - **Frequency:** 1 = rare, 5 = many times a day. Use the user's frequency context; mark inferred values.
   - **Effort-saved:** 1 = trivial, 5 = large time/toil sink. Weight by hourly cost when provided.
   - **Rule-clarity:** 1 = requires nuanced human judgment / ambiguous inputs; 5 = fully deterministic, "if X then Y." This factor is the automation-fit gate — a step can be frequent and effortful but a terrible automation target if rule-clarity is 1–2.

3. **Compute the composite.** Use Frequency × Effort-saved × Rule-clarity (range 1–125). Because rule-clarity is a multiplier, low-clarity steps are automatically penalized — that is intended.

4. **Apply the human-in-the-loop filter.** Mark any step that needs human judgment, approval, or touches sensitive/regulated data. These can still be partially automated (e.g., automate prep, keep the decision human) — note that hybrid option.

5. **Rank and shortlist (DS-06).** Order steps by composite score. Present the top candidates as the shortlist; briefly note why low-ranked steps were excluded (usually low rule-clarity).

6. **Recommend the first automation.** Choose the candidate with the best balance of high ROI and low pilot risk. State why it's first, what it would replace, and the rough payback signal (frequency × time saved).

7. **State assumptions and confidence (QA-04).** Call out every estimated frequency or time saving, and rate ranking confidence based on how much real data was supplied.

---

## False-Positive Prevention

1. **Frequency × effort tunnel-vision.** A step that runs constantly and is tedious looks like an obvious win — but if it requires human judgment (rule-clarity 1–2), automating it produces brittle, error-prone results. Always let rule-clarity gate the recommendation.
2. **Fabricated savings.** Do not assert "this saves 5 hours a week" unless the user gave the numbers. Label all time/frequency estimates as assumptions and lower confidence accordingly.
3. **Ignoring the human-required steps.** Approval gates, compliance checks, and sensitive-data handling can be legally or ethically human-required. Flag them even when the math says automate.
4. **Picking the riskiest step first.** The highest-ROI step may also be the one whose failure has the largest blast radius. The *first* automation should be high-value AND safe to pilot.
5. **Over-coarse decomposition.** Scoring "process the order" as one step hides that 80% of the toil is in one sub-step. Decompose until the scoring is actionable.
6. **Treating clarity and frequency as interchangeable.** They are not. A clear-but-rare step and a frequent-but-fuzzy step are both poor candidates, for opposite reasons. The composite must reflect both.
7. **Assuming integrations exist.** Don't assume two tools talk to each other. If automation depends on an API/integration the user didn't confirm, flag it as a feasibility unknown.

---

## Output Format

```
# Automation Gold Mine: [workflow name]

## Workflow steps (as analyzed)
[Numbered list; note any decomposition you introduced.]

## Scoring
| # | Step | Frequency | Effort-saved | Rule-clarity | Composite | HITL? |
|---|------|-----------|--------------|--------------|-----------|-------|
| 1 | [...] | [1–5]    | [1–5]        | [1–5]        | [1–125]   | yes/no |
| 2 | [...] | ...      | ...          | ...          | ...       | ...   |

## Ranked shortlist (top candidates)
1. [Step] — composite [n] — [one-line why]
2. [Step] — composite [n] — [one-line why]
3. [Step] — composite [n] — [one-line why]

Excluded and why: [low rule-clarity / human-required / rare ...]

## Recommended first automation
**[Step]** — [why this one first: high ROI + low pilot risk]
- Replaces: [the manual work]
- Payback signal: [frequency × time saved, with assumptions labeled]
- Feasibility note: [integration/API dependency if any]

## Assumptions & confidence
- Assumptions: [labeled estimates]
- Ranking confidence: High | Medium | Low — [why]
```

---

## Verification

- [ ] Workflow broken into discrete, actionable steps.
- [ ] Each step scored on Frequency, Effort-saved, and Rule-clarity (1–5).
- [ ] Rule-clarity acts as a penalty multiplier (low clarity drags the composite down).
- [ ] Composite computed and steps ranked by it.
- [ ] Human-in-the-loop / compliance / sensitive-data steps flagged.
- [ ] Exactly one first automation recommended, balancing ROI and pilot risk.
- [ ] All frequency/time estimates labeled as assumptions.
- [ ] Ranking confidence stated and tied to data completeness.
- [ ] No fabricated savings or assumed integrations.
