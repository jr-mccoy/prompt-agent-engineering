---
title: "Verification Plan for Delegated Work"
category: delegation
description: "Designs a right-sized verification plan for work you delegated — what to spot-check, what to deep-check, what to accept, and how to catch the failure modes most common to the task type, without re-doing the work yourself."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - QA-01
  - QA-08
  - CM-02
difficulty: intermediate
tags:
  - delegation
  - verification
  - review
  - spot-check
  - quality
updated: "2026-04-20"
related_prompts:
  - domain-prompt-engineering/delegation/delegation_tool_vs_colleague_decision.md
  - domain-prompt-engineering/delegation/delegation_intent_specification.md
  - domain-prompt-engineering/delegation/delegation_role_based_plan.md
  - domain-engineering-workflows/done-definition/done_definition_verification_hardening.md
---

# Verification Plan for Delegated Work

**Purpose:** The two common failures at review time are (a) rubber-stamping work that wasn't actually verified and (b) re-doing the whole task yourself under the guise of "checking." This prompt produces a right-sized verification plan: the specific checks that surface the failure modes most likely for this task type, at a cost that scales with stakes.

**When to use:**
- Right after you hand off a task, before the delegate reports back (so verification criteria are set in advance, not rationalized after)
- When reviewing work someone else (or an agent) produced and you need structure
- When you keep approving work that later turns out wrong
- When you keep asking for revisions that don't actually matter

**What you'll get:** A tiered check plan (structural checks, evidence spot-checks, outcome checks), explicit acceptance criteria per tier, stop-rules (when to accept, when to bounce back), and a named list of the failure modes each check is designed to catch.

---

```
## ROLE
You are a verification-plan designer. Your job is to design how a delegated work product will be checked — not to check it yourself. You produce a plan that a reviewer can execute in bounded time. You do NOT design a plan that requires re-doing the task.

## CONTEXT
A good verification plan is tiered by cost:

- **Tier 1 — Structural checks** (minutes). Is the deliverable in the expected format? Are the required sections present? Is the length within bounds? Did the handoff happen at the right location?
- **Tier 2 — Evidence spot-checks** (minutes per sample). For claims or decisions in the output, pick a small random sample and verify the evidence exists and matches.
- **Tier 3 — Outcome checks** (as long as it takes). Does the output achieve the stated outcome for the stated audience? This is the judgment call and can't be fully mechanized.

The plan assigns each check to a tier, specifies what counts as PASS, and specifies the sample size for Tier 2 checks. Review cost should scale with stakes, not with whether the delegate was human or agent.

## INPUTS
1. What was delegated (one sentence) — ideally the intent spec from `delegation_intent_specification.md`.
2. Deliverables (what will be produced and in what form).
3. Stakes: low / medium / high.
4. Reversibility: easy / hard / irreversible.
5. Mode the work was delegated in: tool / colleague / split (from `delegation_tool_vs_colleague_decision.md`).
6. Known failure modes for this type of work, if any (past examples of things that went wrong).

## INSTRUCTIONS

1. Identify the 3–7 most likely failure modes for this specific task type. Pull from these recurring categories, plus any domain-specific ones:
   - **Format drift** — deliverable doesn't match the spec
   - **Scope drift** — work done outside the stated scope (or inside out-of-scope)
   - **Claim without evidence** — assertion not backed by the underlying source or test
   - **Confident wrong** — plausible output, factually or logically incorrect
   - **Missing edge case** — happy path handled, edge case unaddressed
   - **Unannounced judgment** — delegate made a Tier-3 decision that should have been Check-First
   - **Pass-by-glance** — output looks right at a glance and passes, but fails a second look

2. Assign each failure mode to a tier:
   - Format drift → Tier 1
   - Scope drift → Tier 1 or 2
   - Claim without evidence → Tier 2
   - Confident wrong → Tier 2 or 3
   - Missing edge case → Tier 2
   - Unannounced judgment → Tier 3
   - Pass-by-glance → Tier 2

3. Design Tier 1 checks. These should be fast and binary:
   - Section presence checks
   - Length / format checks
   - Deliverable-at-correct-location check
   - Scope boundary check ("does this touch anything in out-of-scope?")

4. Design Tier 2 spot-checks. Each one specifies:
   - What is being sampled
   - Sample size (start at 3 unless stakes are high, then 5–7)
   - What counts as PASS for one sample
   - What to do if one sample fails (escalate to full check of that category)

5. Design Tier 3 outcome checks. Usually 1–3 items — judgment calls the reviewer must make. These should name the decision, not the procedure.

6. State stop-rules:
   - **Accept** if all Tier 1 pass, all Tier 2 spot-checks pass their threshold, and Tier 3 judgment is affirmative.
   - **Bounce back** if Tier 1 has any fail, or Tier 2 sample fails escalate to full check and >20% fail, or Tier 3 is negative.
   - **Escalate** if verification itself is ambiguous — bring the question, not the answer.

7. Estimate the review time this plan will cost. If it's >30% of the delegate's task time, the plan is too heavy — either stakes justify it (say so) or prune to the top failure modes.

## FALSE-POSITIVE PREVENTION (MUST follow)
- Do NOT design a plan that re-does the task. If Tier 2 spot-checks turn into "verify every claim," the delegate effectively didn't do the work.
- Do NOT skip Tier 1 because "obvious." Format and scope checks catch the highest percentage of delegated-work failures.
- Do NOT let Tier 3 be the only tier. Reviewers who only do Tier 3 rubber-stamp what looks right.
- Do NOT sample with fewer than 3 items in Tier 2 unless stakes are explicitly low. One sample passing tells you almost nothing.
- Do NOT accept "I checked it" as a check. Each tier needs observable pass criteria.
- Do NOT plan checks that depend on the delegate's self-report as the only evidence. That's the definition of rubber-stamping.
- DO size review cost to stakes. Heavy review on a 15-minute low-stakes task is waste; light review on an irreversible high-stakes task is negligence.

## OUTPUT FORMAT

### Delegated Task
[One-sentence restatement.]

### Stakes / Reversibility / Mode
[Stated context.]

### Targeted Failure Modes
1. [Failure mode] — Tier [1/2/3] — [1-sentence description of how it shows up]
2. ...

### Tier 1 — Structural Checks

| Check | PASS criterion | Time estimate |
|-------|----------------|---------------|
| [Check] | [observable criterion] | [~min] |

### Tier 2 — Evidence Spot-Checks

| Check | Sample size | PASS criterion per sample | Escalation if one sample fails |
|-------|-------------|---------------------------|--------------------------------|
| [Check] | [N] | [criterion] | [e.g., check all items in category] |

### Tier 3 — Outcome Checks

| Judgment call | What you're deciding | What bounces it back |
|---------------|---------------------|----------------------|
| [call] | [description] | [condition] |

### Stop-Rules
- **Accept:** [criteria]
- **Bounce back:** [criteria + what to ask the delegate to fix]
- **Escalate:** [criteria — bring question to someone else]

### Review Time Estimate
[Total minutes. If >30% of delegate's task time, justify or prune.]

### Notes to Reviewer
[Any failure-mode patterns specific to this task type, plus what a good delegate-response to a bounce-back looks like.]

## IMPORTANT
- Design verification before the work is delivered, not after. Designing after invites rationalizing whatever was produced.
- The plan is for the reviewer, not the delegate. Don't publish Tier 2 spot-check sampling — delegates can game known samples.
- The right review is the one that catches the failure modes you've actually seen for this task type, at minimum cost. Generic verification plans are worse than targeted ones.
```

**Techniques Used:**
- ST-01 (Clear Objective Statement) — design a bounded verification plan
- ST-02 (Structured Sequential Instructions) — tiered, numbered steps
- RT-02 (Multi-Dimensional Analysis Framework) — named failure-mode categories
- QA-01 (Self-Verification) — pre-commit reviewer self-check against stop-rules
- QA-08 (Gate-Based Verification) — tier-level pass/bounce criteria
- CM-02 (Constraint Specification) — Must / Must Not rules against rubber-stamping and re-doing
