---
title: "Debugging: Root Cause Mode"
category: engineering-workflows/workflows
description: "A gated debugging workflow that backs up from a non-working fix, brainstorms and selects an evidence-supported root cause, designs and chooses a solution, then instruments and implements it with confirming metrics."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - QA-02
  - QA-01
difficulty: intermediate
tags:
  - debugging
  - root-cause-analysis
  - five-whys
  - instrumentation
  - troubleshooting
updated: "2026-06-07"
related_prompts:
  - domain-engineering-workflows/workflows/engineering_prompt_for_debugging_code.md
  - domain-engineering-workflows/workflows/debug_prompt.md
  - domain-engineering-workflows/workflows/engineering_post_mortem_root_cause_ladder.md
---

# Debugging: Root Cause Mode

**Objective:** When a fix isn't working, back up, identify the true root cause with evidence, choose a solution deliberately, and verify it with instrumentation — instead of patching symptoms.

**When to use:**
- A bug persists after one or more attempted fixes.
- The same issue keeps recurring.
- You suspect you've been treating symptoms, not the cause.
- You need to prove to others that the fix actually worked.

**When NOT to use:**
- A trivial, well-understood bug with an obvious one-line fix.
- Android/Compose-specific debugging — use `debug_prompt.md`.
- Post-incident organizational analysis — use `engineering_post_mortem_root_cause_ladder.md`.

**Audience:** Engineers stuck on a recurring or non-obvious bug.

---

## Inputs / Context

The user supplies:
1. **Observed behavior** — what's happening vs. what should happen.
2. **What's been tried** — prior fixes and their results.
3. **Evidence** — wrap error output/stack traces in a `<logs>` tag and suspect code in a `<code>` tag.
4. **Environment** — OS, language/runtime, framework versions.

If evidence is insufficient to support a cause, say so and request logs/repro before asserting one.

---

## Constraints

### Must
- Brainstorm 5–6 candidate root causes; use Five Whys to reach system-level causes.
- Select one cause and justify it against the observed evidence.
- Propose 2–3 solutions and pick one with explicit reasoning before implementing.
- Define and build confirming metrics/instrumentation before (or alongside) the fix.

### Must Not
- Jump to a solution before the cause is evidenced.
- Assert a root cause the logs/code don't support — request more data instead.
- Implement the fix before metrics exist to confirm it.
- Fabricate log lines, stack traces, or metric values.

---

## Instructions

1. **Brainstorm root causes.** List 5–6 plausible causes. For each, note why it could produce the behavior and what evidence supports or contradicts it. Apply Five Whys to push past surface errors.
2. **Select and justify the cause.** Write the most likely root cause clearly; show all candidates and explain why this one wins on the evidence. Do not proceed until confident.
3. **Design solution paths.** Brainstorm 2–3 solutions addressing the cause directly. Compare fix-likelihood, risk, and complexity. Choose one and explain. Do not implement yet.
4. **Plan tracking metrics.** Define what would confirm the fix worked, how you'll collect it, and the baseline needed.
5. **Build instrumentation.** Add the metrics/logging/assertions; validate they capture the right signals; record the baseline.
6. **Implement the solution.** Apply the chosen fix incrementally; verify against the metrics.
7. **Self-check before reporting.** Confirm: cause is evidenced, alternatives were weighed, metrics exist and show the expected change, nothing fabricated.

---

## False-Positive Prevention

❌ **DON'T:**
- Don't pick a root cause because it's the first plausible one — weigh it against the evidence and alternatives.
- Don't skip instrumentation; "it seems fixed" is not confirmation.
- Don't claim a cause the logs/code don't support — ask for more data.
- Don't invent metric numbers or log output to make the fix look successful.

✅ **DO:**
- Cite the evidence (log line, stack frame, code path) behind the chosen cause.
- Establish a baseline before the fix and compare after.
- Keep changes incremental so you can attribute the improvement.
- State confidence and what would change your diagnosis.

---

## Output Format

```markdown
## Root Cause Analysis
**Candidates (5–6):**
1. [cause] — supports/contradicts: [evidence]
...
**Selected cause:** [...]   **Why:** [evidence-based rationale]

## Solution Options
| Solution | Fix likelihood | Risk | Complexity |
|----------|----------------|------|------------|
**Chosen:** [...]   **Why:** [...]

## Tracking Plan
- Metric — baseline → target; collection method

## Implementation
- [incremental steps + verification against metrics]
```

## Example Output

```markdown
## Root Cause Analysis
**Candidates:**
1. Race condition in cache refresh — supports: errors cluster at TTL boundary
2. Connection timeout — contradicts: DB latency metrics healthy
3. Null from cache miss — supports: errors begin after TTL expiry
4. Thread-pool exhaustion — supports: active threads spike pre-error
5. GC pause — contradicts: no memory/error correlation

**Selected cause:** Race between cache refresh and concurrent reads — readers see partially-updated state.
**Why:** Error timing matches the 5-minute refresh interval and the stack trace lands in the cache read path.

## Solution Options
| Solution | Fix likelihood | Risk | Complexity |
|----------|----------------|------|------------|
| Read-write lock | High | Low | Medium |
| Double-buffered cache | High | Medium | High |
| Retry with backoff | Medium | Low | Low |

**Chosen:** Read-write lock — addresses the cause directly with low risk.

## Tracking Plan
- Error rate — baseline (to be measured) → 0/hour
- Lock wait time — baseline (to be measured) → <5% of reads wait

## Implementation
- Add lock around cache reads/refresh with acquisition timeout; deploy behind metrics; compare error rate vs. baseline.
```

---

## Verification

- [ ] 5–6 candidate causes brainstormed; Five Whys applied.
- [ ] Selected cause justified against observed evidence.
- [ ] 2–3 solutions compared; one chosen with rationale, before implementing.
- [ ] Metrics defined and instrumented; baseline captured.
- [ ] Fix implemented incrementally and confirmed against metrics.
- [ ] No fabricated logs, traces, or metric values.

---

## Techniques Used

- **ST-01 (Clear Objective Statement):** Frames the back-up-and-find-the-real-cause goal.
- **ST-02 (Structured Sequential Instructions):** Six gated steps from brainstorm to verified fix.
- **RT-02 (Multi-Dimensional Analysis):** Weighs each cause/solution on multiple axes (likelihood, risk, complexity).
- **QA-02 (Adversarial Self-Critique):** Forces contradicting evidence and alternatives before committing.
- **QA-01 (Self-Verification):** Metrics-based confirmation replaces "seems fixed."

---

## Related Prompts

- `domain-engineering-workflows/workflows/engineering_prompt_for_debugging_code.md` — Fuller stuck-bug version with input scaffolding.
- `domain-engineering-workflows/workflows/debug_prompt.md` — Android/Compose-specific debugging workflow.
- `domain-engineering-workflows/workflows/engineering_post_mortem_root_cause_ladder.md` — Post-incident root-cause analysis.
