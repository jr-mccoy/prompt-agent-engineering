---
title: "Stuck-Bug Debugging Workflow"
category: engineering-workflows/workflows
description: "When the current debugging approach has stalled, step back to brainstorm and evidence a root cause, choose a solution from compared alternatives, instrument tracking metrics, and implement a measured, verifiable fix."
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
  - troubleshooting
  - instrumentation
  - five-whys
updated: "2026-06-07"
related_prompts:
  - domain-engineering-workflows/workflows/engineering_debugging_root_cause.md
  - domain-engineering-workflows/workflows/debug_prompt.md
  - domain-engineering-workflows/workflows/engineering_post_mortem_root_cause_ladder.md
---

# Stuck-Bug Debugging Workflow

**Objective:** When the current debugging approach isn't working, step back to systematically identify an evidence-supported root cause, choose a solution from compared alternatives, instrument tracking metrics, and implement a measured fix you can prove worked.

**When to use:**
- Stuck on a bug for more than ~30 minutes.
- Obvious fixes haven't resolved it, or the same bug keeps recurring.
- You're unsure what's actually causing the problem.
- You need to convince others the fix is correct.

**When NOT to use:**
- A trivial bug with an obvious one-line fix.
- Android/Compose-specific debugging — use `debug_prompt.md`.
- Post-incident organizational analysis — use `engineering_post_mortem_root_cause_ladder.md`.

**Audience:** Engineers stuck on a non-obvious or recurring bug.

---

## Inputs / Context

The user supplies:
1. **Problem & expected behavior** — what's happening vs. what should.
2. **What's been tried** — attempted fixes and results.
3. **Evidence** — wrap error output/stack traces in a `<logs>` tag and suspect code in a `<code>` tag.
4. **Environment** — OS, language/runtime, framework versions.

If the evidence doesn't support a confident diagnosis, say so and request more (logs, repro) before asserting a cause.

---

## Constraints

### Must
- Brainstorm 5–6 candidate causes with supporting/contradicting evidence; use Five Whys.
- Select one cause and justify it; do not proceed until confident.
- Compare 2–3 solutions (fix-likelihood, risk, complexity) and choose before implementing.
- Define and instrument metrics with a baseline before applying the fix.

### Must Not
- Jump to a solution before the cause is evidenced.
- Assert a cause the logs/code don't support.
- Implement before tracking metrics and a baseline exist.
- Fabricate logs, stack traces, or metric values.

---

## Your Input

**Problem Description:** [What's happening that shouldn't be happening, or not happening that should]

**Expected Behavior:** [What should happen instead]

**What We've Tried:** [List of attempted fixes and their results]

**Error Messages/Logs:**
```
[Paste relevant errors, stack traces, or log output]
```

**Relevant Code:**
```
[Paste the code sections you suspect are involved]
```

**Environment:** [OS, language version, framework versions, etc.]


**Instructions**

Take a step back from the current approach. This isn't working. Follow this systematic debugging process:

**Step 1: Root Cause Brainstorming**
Brainstorm 5-6 potential root causes for the problem we're seeing. Use the Five Whys technique to get to actual root causes, not just presenting symptoms.

For each potential cause, consider:
- Why would this cause the behavior we're seeing?
- What evidence supports or contradicts this cause?
- How likely is this given what we know?

**Step 2: Root Cause Selection**
Once you have confidence in the most likely root cause:
- Write it out clearly and explain your reasoning
- Present all causes you brainstormed
- Highlight the one you selected with clear rationale
- Explain what evidence led you to this conclusion

**Do not proceed until you're confident in your diagnosis.**

**Step 3: Solution Design**
Brainstorm 2-3 solutions that would fix the identified root cause:
- Solution A: [Description]
- Solution B: [Description]
- Solution C: [Description]

For each solution, evaluate:
- Likelihood of fixing the problem
- Risk of introducing new issues
- Implementation complexity
- Long-term maintainability

Select the best solution and explain:
- Why you chose it over alternatives
- How you plan to implement it
- What could go wrong

**Do NOT start implementing yet.**

**Step 4: Tracking Metrics Design**
Figure out how to measure the impact of your solution:
- What metrics will confirm the fix works?
- How will you collect these metrics?
- What baseline do you need before implementing?
- What thresholds indicate success vs. failure?

**Step 5: Implement Tracking**
Build the tracking metrics you designed:
- Add logging, monitoring, or assertions as needed
- Validate that metrics are being captured correctly
- Establish baseline measurements before the fix

**Step 6: Implement Solution**
Now proceed with implementing the selected solution:
- Make changes incrementally
- Test after each significant change
- Monitor your tracking metrics
- Document what you changed and why


**Output Format**

Structure your response as:

### Root Cause Analysis

**Brainstormed Causes:**
1. [Cause] - Likelihood: High/Medium/Low - Evidence: [What supports/contradicts]
2. [Cause] - Likelihood: High/Medium/Low - Evidence: [What supports/contradicts]
3. [Cause] - Likelihood: High/Medium/Low - Evidence: [What supports/contradicts]
4. [Cause] - Likelihood: High/Medium/Low - Evidence: [What supports/contradicts]
5. [Cause] - Likelihood: High/Medium/Low - Evidence: [What supports/contradicts]

**Selected Root Cause:** [Your diagnosis]
**Rationale:** [Why you believe this is correct]

### Solution Options

| Solution | Fix Likelihood | Risk | Complexity |
|----------|---------------|------|------------|
| A: [Name] | High/Med/Low | High/Med/Low | High/Med/Low |
| B: [Name] | High/Med/Low | High/Med/Low | High/Med/Low |
| C: [Name] | High/Med/Low | High/Med/Low | High/Med/Low |

**Selected Solution:** [Your choice]
**Implementation Plan:**
1. [Step]
2. [Step]
3. [Step]

### Tracking Plan

**Success Metrics:**
- [Metric 1]: Baseline = [X], Target = [Y]
- [Metric 2]: Baseline = [X], Target = [Y]

**Monitoring Approach:**
- [How you'll track]

### Ready to Implement
- [ ] Root cause identified with high confidence
- [ ] Solution selected with clear rationale
- [ ] Tracking metrics in place
- [ ] Baseline measurements captured


## Example Output

> Illustrative — the metric baselines/targets below are example values to show format, not real measurements.

### Root Cause Analysis

**Brainstormed Causes:**
1. **Race condition in async handler** - Likelihood: High - Evidence: Error occurs intermittently, more frequent under load
2. **Memory leak causing GC pauses** - Likelihood: Medium - Evidence: Memory grows over time but no correlation to error timing
3. **Database connection timeout** - Likelihood: Low - Evidence: DB metrics show healthy latency
4. **Null reference from cache miss** - Likelihood: Medium - Evidence: Error happens after cache TTL expires
5. **Thread pool exhaustion** - Likelihood: High - Evidence: Active threads spike before errors appear

**Selected Root Cause:** Race condition between the cache refresh task and request handlers
**Rationale:** The error pattern correlates with cache TTL cycles. When the cache refreshes, concurrent requests can read partially updated state. The stack trace shows the error occurs in the cache read path, and the timing (every ~5 minutes) matches the refresh interval.

### Solution Options

| Solution | Fix Likelihood | Risk | Complexity |
|----------|---------------|------|------------|
| A: Add read-write lock | High | Low | Medium |
| B: Double-buffered cache | High | Medium | High |
| C: Retry with backoff | Medium | Low | Low |

**Selected Solution:** A - Add read-write lock around cache access
**Implementation Plan:**
1. Add ReaderWriterLockSlim to cache class
2. Wrap all reads in read lock
3. Wrap refresh in write lock
4. Add lock acquisition timeout to prevent deadlocks

### Tracking Plan

**Success Metrics:**
- Error rate: Baseline = 12/hour, Target = 0/hour
- P99 latency: Baseline = 45ms, Target = <60ms (allowing for lock overhead)
- Lock contention: Baseline = N/A, Target = <5% of requests wait

**Monitoring Approach:**
- Add structured logging for lock acquisition time
- Alert if error rate >1/hour after deployment
- Dashboard showing lock wait time distribution

### Ready to Implement
- [x] Root cause identified with high confidence
- [x] Solution selected with clear rationale
- [ ] Tracking metrics in place
- [ ] Baseline measurements captured


**Common Debugging Pitfalls:**

| Pitfall | Problem | Better Approach |
|---------|---------|-----------------|
| Jumping to solutions | Miss the actual root cause | Complete brainstorming first |
| Fixing symptoms | Bug returns or moves | Ask "why" until you reach a systemic cause |
| No metrics | Can't prove the fix worked | Always add tracking before fixing |
| Big bang changes | Hard to isolate what helped | Change one thing, measure, repeat |
| Confirmation bias | See what you expect | Actively look for contradicting evidence |

---

## False-Positive Prevention

❌ **DON'T:**
- Don't pick the first plausible cause — weigh evidence and alternatives via Five Whys.
- Don't implement before tracking metrics and a baseline exist.
- Don't assert a cause the logs/code don't support — request more data.
- Don't fabricate logs, traces, or metric numbers to make the fix look successful.

✅ **DO:**
- Cite the evidence behind the selected cause; note what would change your diagnosis.
- Establish a baseline, then compare after the change.
- Change one thing at a time and measure.
- Actively look for contradicting evidence.

---

## Verification

- [ ] 5–6 candidate causes with supporting/contradicting evidence; Five Whys applied.
- [ ] Selected cause justified; not proceeding until confident.
- [ ] 2–3 solutions compared; one chosen with rationale before implementing.
- [ ] Tracking metrics defined and instrumented; baseline captured.
- [ ] Fix implemented incrementally and confirmed against metrics.
- [ ] No fabricated logs, traces, or metric values.

---

## Techniques Used

- **ST-01 (Clear Objective Statement):** Frames the step-back, evidence-first debugging goal.
- **ST-02 (Structured Sequential Instructions):** Brainstorm → select → solution → metrics → instrument → implement.
- **RT-02 (Multi-Dimensional Analysis):** Scores causes and solutions on likelihood, risk, and complexity.
- **QA-02 (Adversarial Self-Critique):** Forces contradicting evidence and alternatives before committing.
- **QA-01 (Self-Verification):** Metric-confirmed fix replaces "looks fixed."

---

## Related Prompts

- `domain-engineering-workflows/workflows/engineering_debugging_root_cause.md` — Same workflow, compact root-cause framing.
- `domain-engineering-workflows/workflows/debug_prompt.md` — Android/Compose-specific debugging.
- `domain-engineering-workflows/workflows/engineering_post_mortem_root_cause_ladder.md` — Analyze incidents after resolution.
