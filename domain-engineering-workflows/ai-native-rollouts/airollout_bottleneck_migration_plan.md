---
title: "Plan Migration of the Organizational Bottleneck From Humans to AI"
category: engineering-workflows/ai-native-rollouts
description: "Identify where the organizational bottleneck currently sits, evaluate whether AI migration is appropriate, and plan the migration with guardrails, fallback, and a named owner — instead of quietly handing a load-bearing function to an AI system and hoping."
techniques:
  - ST-01
  - ST-02
  - CM-02
  - DS-01
  - RT-07
  - RT-11
  - QA-01
difficulty: advanced
tags:
  - ai-native-rollouts
  - bottleneck
  - theory-of-constraints
  - migration
  - organizational-design
updated: "2026-04-21"
related_prompts:
  - domain-engineering-workflows/ai-native-rollouts/airollout_tiered_adoption_rollout.md
  - domain-engineering-workflows/ai-native-rollouts/airollout_delegate_like_parallel_coworker.md
  - domain-business-strategy/ai-strategy/aistrategy_context_accumulation_map.md
  - domain-business-strategy/ai-strategy/aistrategy_capability_compounding_evaluation.md
  - domain-personal-development/career-transformation/career_role_structural_vulnerability.md
---

# Plan Migration of the Organizational Bottleneck From Humans to AI

**Purpose:** Organizations have a current bottleneck — the function through which throughput is constrained. When AI is deployed, the natural instinct is to automate the bottleneck. This is sometimes right, often disastrous. This prompt produces a structured plan: confirm where the bottleneck actually is, decide whether AI migration is safe, sequence the migration, install guardrails and fallback, and identify where the bottleneck will move next — because it always does.

**When to use:**
- An engineering org, product org, or functional team is considering using AI to expand throughput at a constrained function (code review, support triage, legal review, content moderation, quality gates, etc.).
- Leadership has proposed "let's use AI for X" and the team wants a rigorous plan before executing.
- An existing AI deployment has migrated part of a bottleneck and the team wants to evaluate what happened and what to do next.
- A CoS / staff engineer / PM is preparing a brief on AI leverage for leadership.

**Don't use when:** The goal is to automate individual tasks, not to relieve a throughput constraint. Task automation is not bottleneck migration; treat them separately.

**Audience:** Senior IC, EM, PM, or leadership owning the function in question. Output is a decision document + migration plan.

---

## Inputs Required

1. **The proposed target function.** What the AI would take over. Be specific (e.g., "initial pass of incoming support tickets," "first-round code review," "contract redlines under $X threshold," "quarterly summary of OKR progress").
2. **Current throughput and constraint evidence.** How much of the work backs up here; how long the queue sits; what downstream work is blocked while this is blocked. Data, not vibes.
3. **What the function currently does.** Not the title of the job — the actual decisions being made, the inputs consumed, the outputs produced, and the judgment applied.
4. **Failure cost of the function.** If the function makes a wrong decision, what's the blast radius? Recoverable / expensive / regulatory / reputational / irreversible.
5. **Who owns accountability today.** Role, not name, usually. Who gets paged when the function fails?
6. **Proposed AI system.** Off-the-shelf / tuned model / agent / RAG / human-in-loop shape. Or "open — we're evaluating."
7. **Leadership context.** What problem is leadership trying to solve by doing this? Cost, speed, capacity, strategic positioning? (This shapes whether the plan succeeds by leadership's definition.)

---

## Instructions

### Step 1 — Verify the bottleneck

Is the proposed target function actually the bottleneck? Check:

- **Queue evidence.** Work visibly piles up at this function (input 2). If nothing piles up, this isn't the bottleneck.
- **Downstream starvation.** Other teams wait on this function's output. If not, the bottleneck is elsewhere.
- **Slack elsewhere.** Other functions have slack and could absorb more. If the whole system is saturated, the "bottleneck" is whole-system capacity, not this function.

If any check fails, state so. Do NOT plan a migration against a non-bottleneck — you'll move work faster into a different bottleneck and exhaust it.

### Step 2 — Characterize the function's judgment

Break the function's work into three categories:

- **Routine-rule:** The work applies rules that can be written down. Volume and speed constrained only by throughput.
- **Judgment-under-ambiguity:** The work requires interpreting context, weighing competing considerations, or knowing when to break the rule.
- **Exception / novel:** Rare edge cases the function's owner escalates or handles manually.

Estimate the share of each. If judgment-under-ambiguity is > 50%, the function is not a clean AI-migration target — migration is possible but requires much stronger guardrails and higher human-in-loop ratio.

### Step 3 — Evaluate failure cost

From input 4, map to a failure-cost band:

| Band | Examples | AI migration posture |
|------|----------|---------------------|
| **Recoverable** | Queued work, minor customer inconvenience | AI can be load-bearing with a drift audit. |
| **Expensive** | Customer churn, financial exposure at scale | AI augments; humans retain decision authority on each case. |
| **Regulatory / reputational** | Compliance breach, public incident | AI assists; humans decide and sign. |
| **Irreversible** | Physical safety, medical harm, legal binding | No direct AI migration. AI informs; humans decide and verify. |

Name the band explicitly. Do NOT proceed to step 4 without it.

### Step 4 — Sequence the migration

Migration is done in stages, never in one cut. Propose three stages (some functions won't reach stage 3):

- **Stage 1 — AI proposes, human decides.** AI runs on every case; produces a recommendation. Human decides every case. This builds a labeled dataset of human decisions against AI recommendations.
- **Stage 2 — AI decides on high-confidence cases, human decides the rest.** AI auto-handles cases above a confidence threshold with strong agreement rate with past human decisions. Ambiguous cases escalate.
- **Stage 3 — AI decides, human audits a sample.** AI auto-handles the bulk; human samples N% for audit and reviews drift.

For each stage, specify: entry criteria (what passes before entering), observable metrics during the stage, exit criteria (what must hold to advance), and rollback conditions.

Failure-cost band constrains how far the migration can go: Expensive functions cap at Stage 2; Regulatory cap at Stage 1 with decision authority clearly in a human role; Irreversible functions do not migrate in this framework.

### Step 5 — Install guardrails

For each stage that will be live, name:

- **Confidence signal.** How AI expresses certainty (calibrated to actual accuracy, not a raw model logprob).
- **Escalation trigger.** Specific conditions that force human review even in later stages (novel input shape, out-of-distribution, repeated pattern the AI hasn't seen).
- **Drift detection.** How the team knows AI output quality is changing (sample agreement with ground-truth reviewers, customer escalation rate, downstream-defect rate).
- **Kill switch.** A specific person and a specific trigger that reverts to an earlier stage or pauses. The kill switch must be exercisable within hours, not weeks.

### Step 6 — Define fallback capacity

AI migration does not reduce the need for humans; it changes their shape. Specify:

- **Residual human capacity required.** To audit, to handle exceptions, to make decisions at the failure-cost band where AI isn't authorized. State headcount / hours.
- **Skills required by residual humans.** Different from the skills that did the work pre-migration. Reviewing AI output is not the same as doing the work.
- **Pipeline.** Where do the residual humans come from — retained staff, reskilled, hired? If the plan requires a skill that doesn't exist yet, call it out.

This step is where "we'll replace 90% of the team" plans typically collapse.

### Step 7 — Predict where the bottleneck moves next

The bottleneck is the thing constraining throughput. Removing the current one creates a new one. Identify:

- Which downstream or upstream function will become the new constraint once AI migration increases throughput at the target.
- Whether the org is prepared for the shift (staffing, tooling, process).

If the new bottleneck is in a function that can't scale with AI, the net throughput gain may be small. Call that out.

### Step 8 — Address the three common cascade failures

Walk through how the plan handles each:

- **Silent quality decay.** AI output is "mostly fine" and degrades slowly; humans stop auditing; quality drifts below threshold unnoticed. Caught by: drift detection + mandatory sample audit.
- **Bottleneck displacement.** AI moves the bottleneck to an unprepared function; net throughput stalls. Caught by: step 7 + pre-migration capacity check on the new bottleneck.
- **Role erosion by stealth.** Remaining humans are nominally in charge but reviewing so much AI output they become rubber-stampers. Caught by: residual-capacity design (step 6) + explicit decision-authority placement.

If any failure isn't caught, revise the plan.

### Step 9 — Owner and cadence

Name a specific owner (role) for the migration, a scheduled review cadence, and a stop condition that forces re-evaluation independent of normal reviews (e.g., "one regulatory event," "drift metric crosses threshold X").

### Step 10 — Verify and output

Run the verification checklist.

---

## Constraints

### Must
- Verify the bottleneck exists before planning migration.
- Map failure cost to a band that constrains stage depth.
- Stage the migration; never do a one-cut handover.
- Install drift detection, escalation triggers, and a kill switch per live stage.
- Size residual human capacity explicitly.
- Predict where the bottleneck moves next.

### Must Not
- Assume the bottleneck is where leadership says it is. Verify with evidence.
- Plan to Stage 3 for Expensive or Regulatory functions.
- Plan migration for Irreversible-band functions in this framework.
- Replace residual human capacity with confidence the AI won't need oversight.
- Confuse a task-automation plan with a bottleneck-migration plan.
- Let the plan proceed without a named kill-switch owner.

---

## False-Positive Prevention (MUST follow)

❌ **DON'T:**
- Treat "we have a backlog" as evidence of a bottleneck if nothing downstream waits on that function. Backlogs can exist without constraining throughput.
- Accept leadership's input 7 as the problem definition. It's the context; the plan must still ground in operational evidence.
- Claim AI can handle "judgment-under-ambiguity" at scale without a labeled dataset of human decisions. Without data, Stage 1 is mandatory.
- Fold drift detection into the same AI system doing the work. The auditor should be independent.
- Let the plan silently demote human accountability. State authority explicitly.

✅ **DO:**
- Collect pre-migration baseline metrics for 2–4 weeks minimum so "drift" has a baseline.
- Require the kill switch be a single named role with trigger clarity.
- Pair this plan with `aistrategy_capability_compounding_evaluation.md` if leadership is assuming the capability will compound.
- Treat any plan that claims Stage 3 in < 6 months as suspect; ask for the evidence.
- Include a pre-mortem: if this migration goes wrong in 12 months, which of the 3 cascade failures (step 8) is the likely cause?

---

## Dual-Failure Prevention (QA-20)

❌ **HARMFUL failure:** Plan migrates an expensive-band function too fast; AI makes a correlated error across many cases; team discovers at a downstream incident.

❌ **UNHELPFUL failure:** Plan is so hedged it never progresses past Stage 1; the migration generates audit overhead without capacity gain; leadership loses patience, plan ends.

✅ **Quality check:** A senior peer reading the plan believes both (a) if Stage 1 succeeds, Stage 2 will be tried responsibly, and (b) if something goes wrong, the kill switch will fire before material damage.

---

## Output Format

```markdown
# AI Bottleneck Migration Plan — [Function]

## Bottleneck Verification
- Queue evidence: [data]
- Downstream starvation: [data]
- Slack elsewhere: [yes/no + detail]
- Verdict: [is / is not the bottleneck; proceed / don't proceed]

## Function Judgment Breakdown
| Category | Share | Notes |
|----------|-------|-------|
| Routine-rule | % | |
| Judgment-under-ambiguity | % | |
| Exception / novel | % | |

## Failure-Cost Band
- Band: [Recoverable / Expensive / Regulatory / Irreversible]
- Stage ceiling: [Stage 3 / Stage 2 / Stage 1 / not eligible]

## Migration Stages
### Stage 1 — AI proposes, human decides
- Entry criteria:
- Metrics during:
- Exit criteria (advance to Stage 2):
- Rollback conditions:

### Stage 2 — AI decides high-confidence, human decides rest
- [Same fields; skip if band restricts]

### Stage 3 — AI decides, human audits
- [Same fields; skip if band restricts]

## Guardrails (per live stage)
- Confidence signal:
- Escalation triggers:
- Drift detection (independent auditor):
- Kill switch: [owner role + trigger condition]

## Residual Human Capacity
- Headcount / hours:
- Required skills (review of AI output is different from doing the work):
- Pipeline:

## Bottleneck Next
- Predicted new constraint: [function]
- Readiness: [yes / no / action required]

## Cascade Failure Coverage
- Silent quality decay → caught by: [mechanism]
- Bottleneck displacement → caught by: [mechanism]
- Role erosion by stealth → caught by: [mechanism]

## Owner and Cadence
- Plan owner (role):
- Review cadence:
- Independent stop condition:

## Pre-Mortem
- If this goes wrong at 12 months, the likeliest cause is: [cascade failure + why]
```

---

## Verification

- [ ] Bottleneck existence is evidence-checked, not assumed.
- [ ] Function's judgment share is characterized.
- [ ] Failure-cost band is explicit and constrains the stage ceiling.
- [ ] Stages have entry, metrics, exit, rollback defined.
- [ ] Guardrails per live stage include kill switch with named owner.
- [ ] Residual human capacity is sized.
- [ ] Next bottleneck is predicted with readiness check.
- [ ] Three cascade failures are each covered.
- [ ] Independent stop condition named.

---

## Techniques Used

- **ST-01 (Clear Objective Statement):** Produce a staged migration plan with guardrails, not a "we'll let AI handle it" commitment.
- **ST-02 (Structured Sequential Instructions):** Ten steps force verify → characterize → band → stages → guardrails → residual humans → next bottleneck → cascade → owner → verify.
- **CM-02 (Constraint Specification):** Must Not block forbids skipping bottleneck verification, migrating irreversible-band functions, and fold-in drift detection.
- **DS-01 (Framework Application):** Failure-cost band framework constrains migration depth; three-category judgment split calibrates AI suitability.
- **RT-07 (Cascade Effect Analysis):** Explicit cascade-failure coverage table forces the plan to address the three predictable systemic failures.
- **RT-11 (Error Recovery):** Kill switch, rollback conditions, and independent stop ensure the plan can retreat when evidence demands it.
- **QA-01 (Self-Verification):** Verification checklist + pre-mortem catches aspirational plans before they ship.
