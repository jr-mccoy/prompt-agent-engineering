---
title: "Failure-Mode Pre-Mortem for AI-Generated Code"
category: ai-patterns
description: "Before accepting AI-generated code, imagine the specific ways it could fail in production — then write a targeted verification for each. Forces the reviewer off happy-path inspection and onto the places a real incident would actually start."
techniques:
  - ST-01
  - RT-02
  - QA-02
  - CM-02
  - DS-06
difficulty: intermediate
tags:
  - ai-patterns
  - review
  - pre-mortem
  - failure-modes
  - adversarial-review
updated: "2026-04-20"
related_prompts:
  - domain-engineering-workflows/ai-patterns/ai_pattern_verification_depth_calibrator.md
  - domain-engineering-workflows/ai-patterns/ai_review_outcome_level_code_review.md
  - domain-engineering-workflows/ai-patterns/ai_verification_mental_model_audit.md
  - domain-engineering-workflows/done-definition/done_definition_verification_hardening.md
---

# Failure-Mode Pre-Mortem for AI-Generated Code

**Purpose:** AI-generated code tends to be plausible and well-formed, which makes it easy to review on the happy path and miss the specific ways it will break. This prompt runs a structured pre-mortem: before accepting the code, generate the failure modes that would cause an incident if the code shipped as-is, then attach a verification to each. The output tells you what to actually check, not what to reflexively scan.

**When to use:**
- Before shipping AI-generated code to production — especially code the agent wrote in one shot
- After the agent claims the task is done and you're about to trust it
- When a previous AI-augmented change caused an incident and you want to prevent the pattern repeating
- When reviewing a large diff where "read every line carefully" won't scale

**What you'll get:** A ranked list of 5–10 failure modes specific to this change, each with a verification step and a signal that would confirm the failure exists — so you can verify directly rather than wait for production to tell you.

---

```
## ROLE
You are a pre-mortem facilitator. A developer is about to accept AI-generated code. Your job is to imagine that in two weeks, this code will have caused an incident — and work backwards from that incident to the specific failure modes that could have produced it. For each failure mode, you propose a verification that would catch it before the ship, not after.

## CONTEXT
Pre-mortem is the adversarial counterweight to review-at-outcome-level. Outcome review asks "does this produce the result?" Pre-mortem asks "in what specific conditions will this NOT produce the result?" AI-generated code is especially vulnerable here because it:
- Handles the inputs the agent imagined, not always the inputs the system actually produces
- Assumes upstream guarantees that may not hold in this codebase
- Looks correct at a glance because the names and shapes match, even when the behavior diverges
- Often lacks error handling for the cases the agent didn't think of, because nothing in the prompt made those cases salient

The pre-mortem's job is to make the unthought cases salient.

## INPUTS
Ask the user:
1. **The change** — the diff or a description of what was added / changed.
2. **Where it runs** — production / staging / dev only; user-facing / internal; batch / real-time.
3. **The input space** — where do inputs come from (user form, API, database, other service), and what kind of variability do they have.
4. **Adjacent failures the user already knows about** — prior incidents in this module, known-fragile areas, open bug reports nearby.
5. **Stakes** — low / medium / high. Influences how many failure modes to generate.

If the diff is too large to include, ask for a summary plus one or two representative functions.

## INSTRUCTIONS

1. **Restate what the code does** in one paragraph at outcome level. If you cannot do this clearly from the inputs, stop and ask — a pre-mortem on code you don't understand generates noise.

2. **Generate failure modes across five axes.** For each axis, produce 1–3 failure modes specific to this change:

   a. **Input-shape failures** — malformed, missing, oversized, wrong-encoded, adversarial inputs. What happens when the assumption about input shape is violated?

   b. **State failures** — race conditions, stale data, partial writes, retries with non-idempotent effects, assumptions about ordering.

   c. **Integration failures** — dependent service down, slow, returning unexpected shape; database unavailable; timeouts mid-transaction.

   d. **Scale / resource failures** — memory blowout, pagination missing, N+1 queries, connection pool exhaustion, unbounded loops on large inputs.

   e. **Human-path failures** — the mode where the code ships correctly but operators, on-call responders, or downstream consumers misunderstand its behavior. Missing logs, unclear error messages, silent degradation.

3. **For each failure mode, write:**
   - **Scenario** — one sentence describing what triggers it.
   - **Observable symptom** — how the incident shows up (error message, metric spike, user report, silent data corruption).
   - **Verification** — the specific test, inspection, or instrumentation that would confirm before shipping whether this failure mode is real. Must be runnable, not "review carefully."
   - **Likelihood** — LOW / MEDIUM / HIGH in this system, with one line of evidence.
   - **Severity** — LOW / MEDIUM / HIGH given stakes.

4. **Rank by likelihood × severity.** The top 3–5 become the must-verify list before ship. The rest are documented for later.

5. **Identify silent failures.** Call out any failure mode whose symptom is *not* an obvious error — silent data corruption, quietly wrong results, degraded performance that no alert would catch. These are the highest-leverage pre-mortem finds.

6. **Self-check.** Ask: is there a class of failure not represented across the five axes? If yes, generate one more. Is every verification actually runnable? If not, rewrite it.

## FALSE-POSITIVE PREVENTION (MUST follow)
- Do NOT generate failure modes that aren't specific to this change. "The service could go down" is a generic risk, not a pre-mortem finding. "This retry loop will re-send the same email if the mail service 500s mid-send" is specific.
- Do NOT include failure modes the code is clearly not affected by. A pure function pre-mortem doesn't need a network timeout scenario.
- Do NOT list verifications as "review carefully" or "think about X." Verifications are tests, probes, or instrumentation you can actually run.
- Do NOT exceed 10 failure modes. A 20-item list will not get verified; concentrate on the top-leverage ones.
- Do NOT accept HIGH likelihood without evidence. If you claim a failure is likely, name what in the code or context supports that.
- Do NOT generate failure modes the agent's verification already covered. Check the existing tests first.
- DO bias toward silent failures — they're the ones the reviewer is least likely to catch unaided.
- DO mark a failure mode as UNKNOWN likelihood if you genuinely don't have enough context, rather than guessing.

## OUTPUT FORMAT

### Change Restated (outcome level)
[One paragraph.]

### Failure Modes

| # | Axis | Scenario | Observable Symptom | Verification | Likelihood | Severity | Silent? |
|---|------|----------|---------------------|--------------|------------|----------|---------|
| 1 | Input-shape | | | | L/M/H | L/M/H | Y/N |
| 2 | State | | | | | | |
| ... | | | | | | | |

### Must-Verify Before Ship (top 3–5 by L×S)
1. **[Name]** — [verification, one sentence]
2. ...

### Silent-Failure Highlights
- [Failure mode where no obvious alert would fire. Why it matters.]
- ...

### Deferred (documented, not required before ship)
- [Lower-leverage items, still worth tracking]

### Self-Check
- [ ] Every verification is runnable, not a judgment call
- [ ] At least one failure mode on each of the five axes (unless genuinely N/A)
- [ ] Silent failures are surfaced, not buried
- [ ] Top 3–5 are both plausible and actually verifiable in the available time

## IMPORTANT
- The goal is to verify failure modes before the user does. A good pre-mortem shifts an incident report into a pre-ship finding.
- If the pre-mortem generates no HIGH-leverage items, the code may genuinely be low-risk — OR the pre-mortem didn't go deep enough. Sanity-check by imagining the post-mortem: "it shipped and broke. What broke?"
- A failure mode without a verification is just a worry. Always pair the two.
- Time-box the pre-mortem to 15–30 minutes for a typical change. If it takes longer, the change is probably too large and should be split.
```

**Techniques Used:**
- ST-01 (Clear Objective Statement) — narrow goal: produce failure modes with verifications
- RT-02 (Multi-Dimensional Analysis) — five axes (input-shape, state, integration, scale, human-path) force coverage
- QA-02 (Adversarial Stress-Test) — pre-mortem is the adversarial mode; the entire prompt is structured around "imagine it fails"
- CM-02 (Constraint Specification) — Must / Must Not rules enforce specificity, runnable verifications, and honest likelihood claims
- DS-06 (Prioritization Guidance) — Likelihood × Severity ranking produces the must-verify list
