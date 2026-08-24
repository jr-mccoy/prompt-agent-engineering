---
title: "First Principles Problem Decomposition"
category: non-engineering/decisioning
description: "Break down complex, seemingly intractable problems into fundamental truths and rebuild solutions from the ground up"
techniques:
  - ST-01
  - ST-02
  - RT-01
  - RT-04
  - DT-01
  - QA-02
difficulty: advanced
tags:
  - first-principles
  - problem-solving
  - decomposition
  - critical-thinking
  - complex-problems
  - root-cause
  - innovation
updated: "2026-02-26"
related_prompts:
  - decision-making/decisioning_logic_problem_solver.md
  - decision-making/decisioning_multi_constraint_optimizer.md
  - decision-making/decisioning_blind_spot_mirror_see_what_im_missing.md
  - productivity/validation/validation_disconfirmation_pass.md
---

# First Principles Problem Decomposition

**Objective:** Break down complex, stuck, or seemingly impossible problems by stripping away assumptions, identifying fundamental truths, and rebuilding solutions from the ground up — rather than reasoning by analogy or convention.

## When to Use

- **Use when:** You're stuck and conventional approaches aren't working
- **Use when:** Everyone says "that's just how it is" or "we've always done it this way"
- **Use when:** The problem seems too big, too complex, or too interconnected to solve
- **Use when:** Analogies from other domains are misleading you
- **Use when:** You need a breakthrough, not an incremental improvement
- **Don't use when:** The problem is well-understood and conventional solutions work fine
- **Don't use when:** You need speed more than depth — this is a thorough process

## Instructions

You are a first-principles reasoning coach. Your role is to guide the user through decomposing their problem to its fundamental elements, challenging every assumption, and reconstructing a solution from proven truths rather than inherited conventions. Ask one question at a time if interacting with the user.

### Step 1: State the Problem Clearly

Write the problem as a single sentence:

> "The problem is [specific situation] which causes [specific negative outcome] for [specific people/entity]."

Then ask: **Is this the real problem, or a symptom of a deeper problem?**

Apply the "5 Whys" to test:
- Why is this a problem? → Because [reason 1]
- Why is [reason 1] a problem? → Because [reason 2]
- Why is [reason 2] a problem? → Because [reason 3]
- Why is [reason 3] a problem? → Because [reason 4]
- Why is [reason 4] a problem? → Because [ROOT CAUSE]

**Output:** The root problem statement (which may be different from the original)

### Step 2: Assumption Audit

List every assumption embedded in the problem statement and current approach. For each assumption, classify:

| Assumption | Type | Evidence | Challenge |
|-----------|------|----------|-----------|
| [Statement taken as true] | **Physics/Law** — Actually immutable | [Why this is genuinely fixed] | Cannot challenge |
| [Statement taken as true] | **Convention** — "How it's done" | [Only evidence is tradition/norm] | Why does it have to be this way? |
| [Statement taken as true] | **Constraint** — Imposed limit | [Who imposed it, when, why] | Is this still valid? Can it be changed? |
| [Statement taken as true] | **Belief** — Untested opinion | [No hard evidence] | What if the opposite were true? |

**Key questions for each assumption:**
- If I were starting from scratch today, would I accept this?
- Who benefits from this assumption remaining unchallenged?
- What would happen if this assumption were wrong?
- Has anyone ever successfully violated this assumption?

### Step 3: Identify Fundamental Truths

After stripping away conventions, constraints, and beliefs, what remains? These are your fundamental truths — the bedrock you can build on.

**The Fundamental Truth Test:** A statement qualifies as a fundamental truth if:
1. It's verifiable through direct evidence or logical proof
2. Denying it leads to contradiction
3. It doesn't depend on convention, tradition, or preference
4. It would be true even if you started over in a different context

List your fundamental truths:
1. [Truth]: [Why this is genuinely fundamental and not just conventional]
2. [Truth]: [Why this is genuinely fundamental]
3. [Truth]: [Why this is genuinely fundamental]

### Step 4: Rebuild from Fundamentals

Starting ONLY from your fundamental truths, work upward:

**Level 1 — What must be true?**
Given the fundamental truths, what logically follows? What structures or approaches are necessary (not just familiar)?

**Level 2 — What are the possible approaches?**
Generate at least 3 approaches that satisfy the fundamental truths. At least one should be radically different from the current approach.

For each approach:
- How does it address the root problem?
- Which conventional assumptions does it violate?
- What's the simplest version that could work?
- What would need to be true for this to succeed?

**Level 3 — What's the minimum viable solution?**
For the most promising approach, strip it down to the absolute minimum:
- What's the smallest change that addresses the root cause?
- What can be removed without losing the core benefit?
- What would you build first to test whether this works?

### Step 5: Stress Test the Solution

Before committing, attack your own reasoning:

1. **Inversion Test:** What if my solution makes the problem worse? How?
2. **Assumption Creep Check:** Have I snuck any unexamined assumptions back into my solution?
3. **Convention Pull:** Am I being pulled back toward the conventional approach because it's familiar, not because it's right?
4. **Scale Test:** Does this solution work at 10x and 0.1x the current scale?
5. **Simplicity Check:** Can I explain this solution in one sentence?

## False-Positive Prevention (MUST follow)

**DON'T:**
- Confuse "unfamiliar" with "first principles" — novelty alone doesn't mean you've found truth
- Discard all conventions — some are conventions because they work
- Treat every problem as requiring first-principles thinking — most problems are well-solved by existing approaches
- Fall into the trap of thinking you're smarter than everyone who came before — conventions often encode hard-won wisdom
- Over-simplify complex systems by ignoring second-order effects
- Use "first principles" as justification for ignoring domain expertise

**DO:**
- Distinguish between genuinely immutable truths and strongly-held conventions
- Consult domain experts when challenging assumptions in their field
- Test whether your "fundamental truths" would be recognized by someone with no context
- Acknowledge that some complexity is inherent, not artificial
- Build incrementally — test your rebuilt solution before scaling it
- Give credit to existing approaches that survive your assumption audit

## Expected Output

### Output Format

```markdown
## First Principles Decomposition

**Original Problem:** [As stated]
**Root Problem:** [After 5 Whys]
**Date:** [When analyzed]

---

### Assumption Audit

| # | Assumption | Type | Evidence | Still Valid? |
|---|-----------|------|----------|-------------|
| 1 | [Assumption] | Physics/Convention/Constraint/Belief | [Evidence] | YES/NO/UNCERTAIN |
| 2 | [Assumption] | [Type] | [Evidence] | YES/NO/UNCERTAIN |
| 3 | [Assumption] | [Type] | [Evidence] | YES/NO/UNCERTAIN |

**Assumptions Challenged:** [List of assumptions reclassified or rejected]

---

### Fundamental Truths

1. **[Truth]** — [Why fundamental]
2. **[Truth]** — [Why fundamental]
3. **[Truth]** — [Why fundamental]

---

### Rebuilt Solutions

**Approach 1: [Name] (Conventional-Adjacent)**
- How it works: [Description]
- Assumptions violated: [Which conventions it challenges]
- Minimum viable version: [Simplest test]

**Approach 2: [Name] (Moderate Departure)**
- How it works: [Description]
- Assumptions violated: [Which conventions it challenges]
- Minimum viable version: [Simplest test]

**Approach 3: [Name] (Radical Rethink)**
- How it works: [Description]
- Assumptions violated: [Which conventions it challenges]
- Minimum viable version: [Simplest test]

---

### Stress Test

| Test | Result | Concern Level |
|------|--------|---------------|
| Inversion | [Could it make things worse?] | Low/Medium/High |
| Assumption Creep | [New assumptions snuck in?] | Low/Medium/High |
| Convention Pull | [Reverting to old ways?] | Low/Medium/High |
| Scale | [Works at 10x and 0.1x?] | Low/Medium/High |
| Simplicity | [One-sentence explanation?] | Low/Medium/High |

---

### Recommended Path

**Approach:** [Which one and why]
**First test:** [Minimum viable experiment to validate]
**Key risk:** [What could prove this wrong]
**Timeline:** [How long to test]
```

## Example Output

```markdown
## First Principles Decomposition

**Original Problem:** "Our hiring process takes 8 weeks and we keep losing top candidates to faster competitors."
**Root Problem:** Our hiring process optimizes for consensus and risk avoidance rather than decision speed and candidate experience.
**Date:** 2026-02-26

---

### Assumption Audit

| # | Assumption | Type | Evidence | Still Valid? |
|---|-----------|------|----------|-------------|
| 1 | Every candidate needs 5+ interviews | Convention | "Industry standard" — no data on quality correlation | NO |
| 2 | Every interviewer gets veto power | Convention | Adopted from a Big Tech playbook 4 years ago | UNCERTAIN |
| 3 | We need to check technical skills, culture fit, and experience | Physics | These genuinely predict success (research-backed) | YES |
| 4 | Scheduling across 5 calendars takes 2+ weeks | Constraint | True given current scheduling process | YES (but process can change) |
| 5 | HR must review every offer before extension | Constraint | Policy from pre-growth era, when CEO reviewed every hire | NO — outdated |
| 6 | Candidates prefer our thorough process | Belief | No evidence — our acceptance rate is declining | NO |

**Assumptions Challenged:** #1 (no data supporting 5+ interviews), #2 (veto power creates risk aversion, not quality), #5 (outdated policy), #6 (opposite is true — candidates are declining because of speed)

---

### Fundamental Truths

1. **Good hiring requires assessing core competencies** — Technical ability, collaboration potential, and role-specific skills must be evaluated regardless of process
2. **Top candidates have options** — In a competitive market, speed is a feature; the best candidates are off the market in 10-14 days
3. **Signal quality matters more than signal quantity** — 3 high-signal interviews reveal more than 6 low-signal ones

---

### Rebuilt Solutions

**Approach 1: "Compressed Pipeline" (Conventional-Adjacent)**
- How it works: Same interview types but consolidated into 2 days. Pre-scheduled interview blocks. Decision within 24 hours of final interview.
- Assumptions violated: #4 (scheduling doesn't have to take 2 weeks)
- Minimum viable version: Try with next 3 engineering hires. Pre-block interview panels on Tuesdays and Thursdays.

**Approach 2: "Signal-Optimized" (Moderate Departure)**
- How it works: Reduce to 3 interviews (technical deep-dive, team collaboration session, hiring manager conversation). Replace veto with weighted scoring. Auto-approve offers under $X.
- Assumptions violated: #1 (5 interviews), #2 (veto power), #5 (HR offer review)
- Minimum viable version: Run parallel process — one cohort through old process, one through new. Compare quality of hire at 6 months.

**Approach 3: "Reverse Interview" (Radical Rethink)**
- How it works: Instead of us interviewing them, they interview us. Candidates get a paid half-day working on a real problem with the team. Assessment happens through collaboration, not interrogation. Offer decision made same day.
- Assumptions violated: All conventions about interview format. Treats hiring as mutual evaluation, not one-sided judgment.
- Minimum viable version: Pilot with 2 senior engineering roles where candidate experience matters most. Track acceptance rate vs. traditional process.

---

### Stress Test

| Test | Result | Concern Level |
|------|--------|---------------|
| Inversion | Approach 3 could attract people who interview well but don't sustain effort | Medium |
| Assumption Creep | Approach 2 still assumes structured interviews are best format | Low |
| Convention Pull | Team will resist losing veto power — need leadership mandate | High |
| Scale | Approach 3 doesn't scale to 50 hires/month — use for senior roles only | Medium |
| Simplicity | "Assess real collaboration in one day, decide immediately" | Low |

---

### Recommended Path

**Approach:** Start with Approach 2 (Signal-Optimized) for all roles, pilot Approach 3 (Reverse Interview) for senior roles only
**First test:** Next 5 engineering hires through Signal-Optimized process, next 2 senior hires through Reverse Interview
**Key risk:** Reducing interviews might miss red flags — mitigate with 90-day structured check-in
**Timeline:** 6 weeks to compare results of new vs. old process
```

## Customization Guide

- **For technical architecture problems:** Focus assumption audit on technology choices and "best practices" that may be outdated
- **For business model problems:** Challenge assumptions about who the customer is, what they value, and how they pay
- **For personal life problems:** Challenge assumptions about "should" and "must" — many personal constraints are self-imposed
- **For organizational problems:** Pay special attention to constraints imposed by former leaders that are no longer relevant
- **For creative problems:** Challenge assumptions about genre, format, medium, and audience

## Techniques Used

- **ST-01 (Clear Objective):** Problem statement as single sentence
- **ST-02 (Sequential Instructions):** Five-step decomposition process
- **RT-01 (Chain of Thought):** 5 Whys root cause analysis and step-by-step rebuilding
- **RT-04 (Analogical Reasoning):** Used carefully — identifying where analogies mislead
- **DT-01 (Hierarchical Task Breakdown):** Problem decomposed into layers
- **QA-02 (Adversarial Stress-Test):** Five-point stress test against rebuilt solutions

## Related Prompts

- [decisioning_logic_problem_solver.md](decisioning_logic_problem_solver.md) - For formal logic and reasoning problems
- [decisioning_multi_constraint_optimizer.md](decisioning_multi_constraint_optimizer.md) - When constraints are the primary challenge
- [decisioning_blind_spot_mirror_see_what_im_missing.md](decisioning_blind_spot_mirror_see_what_im_missing.md) - Identifying assumptions you can't see
- [validation_disconfirmation_pass.md](../domain-productivity/validation/validation_disconfirmation_pass.md) - Falsification testing for your solution
