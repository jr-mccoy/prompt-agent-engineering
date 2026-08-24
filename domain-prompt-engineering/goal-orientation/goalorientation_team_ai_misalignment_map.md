---
title: "Map a Team's Current AI Use Against Misalignment Risk"
category: prompt-engineering/goal-orientation
description: "Produce a team-level map of how AI is currently being used — by whom, for what, with what stakes and verification — and identify the specific workflows where the gap between stated goals and how the model is actually being asked to behave is large enough to create real risk."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - DS-01
  - CM-02
  - QA-01
difficulty: advanced
tags:
  - goal-orientation
  - team
  - misalignment-risk
  - ai-audit
  - workflow-review
updated: "2026-04-20"
related_prompts:
  - domain-prompt-engineering/goal-orientation/goalorientation_right_problem_diagnostic.md
  - domain-prompt-engineering/goal-orientation/goalorientation_constraint_architecture_workshop.md
  - domain-business-strategy/ai-strategy/aistrategy_context_accumulation_map.md
  - domain-engineering-workflows/ai-patterns/ai_pattern_intent_and_verification_first.md
---

# Map a Team's Current AI Use Against Misalignment Risk

**Objective:** Produce a structured map of a team's live AI usage — which workflows, who runs them, what the stated goal is, what the model is actually being asked to optimize for, what the verification looks like, and who acts on the output — and identify the specific workflows where the gap between stated goal and operational behavior is large enough to create real misalignment risk. The output is a prioritized list of workflows to either tighten, hand off to a human, or sunset.

**When to use:** A team has been using AI informally for months or longer, it's become load-bearing in daily work, and nobody has stepped back to audit where the stated purpose of each workflow has diverged from what's actually happening. Especially useful ahead of scaling AI use, before a compliance review, or after a first AI-caused incident.

**Audience:** Team leads, engineering managers, ops leaders, or a chief of staff running a top-down review of AI in the team's workflow. Not for individuals — individual misalignment is handled by `goalorientation_right_problem_diagnostic.md` per task.

---

## Inputs Required

1. **Inventory of current AI workflows** in the team — anything where a team member consistently reaches for an AI tool to do a piece of work. Should include the obvious (Claude Code, ChatGPT for drafting) and the less obvious (anyone using AI inside a spreadsheet, for customer replies, for research, for meeting notes).
2. **For each workflow**: one sentence on what it does, who uses it, roughly how often.
3. **The team's stated use-of-AI principles** (if any — it's fine if none exist, but name it explicitly).
4. **Any AI-related incidents** or near-misses in the past quarter.
5. **The scope of the audit.** Which team, which function, which time horizon.

Refuse to run the audit on a hypothetical team. This is an evidence-based review; without a real inventory it produces a generic checklist. If the user doesn't have the inventory, have them collect it first (ask each team member for five minutes on what AI tools they've used this week and for what).

---

## Instructions

### Step 1 — Normalize the inventory into a single table

Put every workflow in one table with these columns:
- **Workflow.** One line.
- **Owner.** Individual or role who runs it most.
- **Stated goal.** What the workflow is supposed to produce.
- **What the model is actually asked to optimize for.** Often different from the stated goal. E.g., stated goal "customer reply" but the prompt optimizes for "reply that sounds friendly" rather than "reply that resolves the customer's issue."
- **Who acts on output.** Model itself downstream? A human on the team? A customer? Each implies a different risk profile.
- **Verification.** What check happens before the output leaves the team. "Human skim," "regex validation," "none," "peer review" — be specific.
- **Frequency.** How often it runs.
- **Stakes if wrong.** Rough: low / medium / high, with a one-line reason.

Collecting this table honestly is the audit. Users often discover half the findings during data entry.

### Step 2 — Classify each workflow against a fixed taxonomy

For each workflow, assign a primary type:

- **Aligned.** Stated goal and what the model optimizes for match closely. Verification exists. Low or known-contained stakes. → Safe to keep.
- **Intent drift.** What the model is asked to optimize for doesn't match the stated goal. The workflow mostly works but sometimes produces output that is wrong *in the direction of the gap*. → Needs prompt redesign.
- **Verification gap.** The goal and model-optimization align, but no one checks the output before downstream action. → Needs a verification step or an escalation trigger.
- **Scope creep.** The workflow has quietly grown past what it was originally designed for. Now handles adjacent cases it was never calibrated for. → Needs scope re-definition.
- **Shadow workflow.** One person runs it; if they leave, it breaks or gets redone from scratch. → Needs documentation and/or a shared prompt.
- **Wrong-tool.** AI is doing work that would be better served by a deterministic script, a form, or a human. AI was used because it was easy, not because it was right. → Needs replacement.
- **Compounding bad output.** The workflow's output feeds another AI workflow; errors compound silently. → Needs chain review (this is the highest-risk class).

A workflow can be multiple types; name the primary and any secondary.

### Step 3 — Rank by misalignment risk

For each workflow, score on three dimensions (low / medium / high):
- **Gap magnitude.** How far apart are the stated goal and the model's effective optimization?
- **Downstream exposure.** How visible are errors? Who sees bad output?
- **Verification strength.** How likely is a bad output to be caught before it matters?

Compute risk as a qualitative rollup — workflows with large gaps, high downstream exposure, and weak verification go to the top of the list. Workflows with any two of those at "high" are the priority class.

### Step 4 — For each priority workflow, name the specific intervention

For the top 3–5 workflows, state the concrete next step:
- **Tighten.** Rewrite the prompt/system prompt using `goalorientation_constraint_architecture_workshop.md` and `escapemedian_instruction_sharpener.md`.
- **Verify.** Insert a human review step, add an escalation trigger, or add an automated check before downstream action.
- **Hand off.** Move the workflow fully back to a human.
- **Sunset.** The workflow isn't saving what it costs to monitor. Kill it.
- **Re-scope.** Trim the workflow back to what it was calibrated for; the adjacent cases become a separate workflow or stay manual.

Each intervention should state who owns it and a rough time cost.

### Step 5 — Surface patterns across the team

After classifying all workflows, look for patterns:
- Does one person account for most of the risk? (Coaching / documentation opportunity.)
- Does one workflow type dominate the team? (Systemic opportunity to improve that pattern once rather than N times.)
- Are incidents clustering around workflows of a specific type? (Pattern is diagnostic.)
- Are high-risk workflows concentrated in recently-adopted tools, or old ones?

State the 1–3 team-level patterns worth acting on.

### Step 6 — Set a re-audit cadence

AI workflows drift. State how often this audit should re-run, and what events (new tool, new incident, org change) should trigger a re-run even if the cadence hasn't hit.

---

## Constraints

### Must
- Require a real inventory before running.
- Put every workflow through the same table and taxonomy; no selective coverage.
- Distinguish "stated goal" from "what the model is asked to optimize for." They are different axes.
- Rank by misalignment risk using all three dimensions.
- Pair every priority workflow with a specific intervention and an owner.
- Name 1–3 team-level patterns.
- Set a re-audit cadence.

### Must Not
- Run this on teams that haven't collected an inventory. Generic output is worse than no output here.
- Treat frequency as a proxy for risk. A rare high-stakes workflow can out-rank a daily low-stakes one.
- Recommend "more training" as a primary intervention. Training doesn't fix misaligned workflows; redesign does.
- Publish specific findings outside the team without the team's consent — AI-audit reports are politically sensitive.
- Skip the shadow-workflow check. Single-owner workflows are a common failure mode.

---

## False-Positive Prevention

1. **"Misalignment" is an easy label to over-apply.** A workflow where the stated goal and model optimization differ *in a way that doesn't matter for outcomes* is not misaligned — it's fine. Require evidence of actual outcome drift before labeling a workflow as needing intervention.
2. **Audits performed on the team by the team can be captured.** If everyone rates their own workflow as "aligned, high verification," there's a cultural incentive problem. Consider a cross-review.
3. **A workflow that's never produced a bad output may be (a) genuinely aligned or (b) the incident hasn't happened yet.** Don't confuse absence of incidents with absence of risk. Use gap + exposure + verification as the rank, not incident history alone.
4. **Stakes should be reviewed separately from the team member's perception of stakes.** Team members under-report downstream exposure when they don't see the downstream effects.
5. **"Sunset" recommendations are politically hard.** If the workflow is saving someone's time, even a risky workflow won't sunset without an explicit alternative. Propose the alternative alongside the sunset.
6. **Compounding-bad-output workflows are the highest-priority class** and the hardest to see. Actively look for chains where one AI's output feeds another's input. These concentrate risk invisibly.
7. **A generic "use AI more carefully" recommendation is the audit failing.** If the output of this prompt reads like a blog post, the inventory was thin. Push back and re-collect.
8. **Incidents are lagging indicators.** Use them to calibrate, not to define the priority list. A team with no incidents and a gap-full inventory is at tomorrow's incident.

---

## Output Format

```markdown
## Audit scope
- Team: [...]
- Function / time horizon: [...]
- Inventory method: [how the workflows were collected]
- Inventory completeness: [confident / likely gaps]

## Workflow inventory

| Workflow | Owner | Stated goal | What model optimizes for | Who acts on output | Verification | Frequency | Stakes | Type(s) |
|----------|-------|-------------|--------------------------|-------------------|--------------|-----------|--------|---------|
| [...] | [...] | [...] | [...] | [...] | [...] | [...] | [L/M/H: why] | [aligned / intent drift / ...] |

## Misalignment risk ranking

| Rank | Workflow | Gap | Exposure | Verification | Rollup risk | Primary type |
|------|----------|-----|----------|--------------|-------------|---------------|
| 1 | [...] | H | H | L | H | compounding bad output |
| ... | | | | | | |

## Priority interventions

| Workflow | Intervention | Owner | Time estimate | Success signal |
|----------|--------------|-------|----------------|-----------------|
| [...] | [Tighten / verify / hand off / sunset / re-scope] | [...] | [...] | [how we'll know it worked] |

## Team-level patterns (1–3)
1. [Pattern]: [evidence across multiple workflows]. [Team-level action.]
2. [...]

## Re-audit cadence
- Schedule: [...]
- Trigger events forcing an early re-audit: [...]

## Risks this audit does not cover
- [What's out of scope, what the user should not assume was reviewed.]
```

---

## Verification

- [ ] Real inventory supplied; no hypothetical workflows.
- [ ] Every workflow has a row in the table.
- [ ] Stated goal and model optimization are distinguished.
- [ ] Risk is computed from gap + exposure + verification, not frequency.
- [ ] Priority workflows have a specific intervention, owner, and success signal.
- [ ] 1–3 team-level patterns are named with evidence.
- [ ] A re-audit cadence with trigger events is set.
- [ ] Risks the audit did not cover are disclosed.
