---
title: "Concept-Legs Test: Pre-Validation Stress Test for a Raw Software Idea"
category: idea-to-product/ideation
description: "Before investing weeks in customer discovery or market research, stress-test a raw software/platform idea across founder-market fit, contrarian truth, distribution wedge, why-now, and a 10x claim. Output is a GO / KILL / RESHAPE verdict with specific reshape directions."
techniques:
  - ST-01  # Clear Objective Statement
  - ST-02  # Structured Sequential Instructions
  - CM-02  # Must / Must Not Constraints
  - RT-02  # Multi-Dimensional Analysis
  - QA-01  # Verification / Self-Check
  - QA-02  # Adversarial Thinking
  - DS-06  # Prioritization Guidance
difficulty: intermediate
tags:
  - ideation
  - pre-validation
  - founder-market-fit
  - product-development
  - go-no-go
updated: "2026-05-19"
related_prompts:
  - domain-idea-to-product/orchestrator_idea_to_product.md
  - domain-idea-to-product/stage-2-problem-validation/validation_customer_discovery_interview_protocol.md
  - domain-idea-to-product/stage-2-problem-validation/jobs_to_be_done_analysis.md
  - domain-idea-to-product/stage-6-decision-validation/validation_am_i_being_nuts.md
---

# Concept-Legs Test: Pre-Validation Stress Test for a Raw Software Idea

**Objective:** Given a one-to-three-sentence software/platform idea, stress-test whether the concept has enough "legs" to justify multi-week customer discovery and market work. Surface fatal weaknesses early. Produce a GO / KILL / RESHAPE verdict, the specific weaknesses found, and — if RESHAPE — concrete directions to reshape the concept into a stronger candidate.

## When to Use

- You have a raw idea ("a Substack for niche professional newsletters with built-in expert verification") and you want a 30-minute reality check before booking customer interviews.
- You have 3-10 candidate ideas and need to rank-and-cull before going deeper.
- You're feeling momentum on an idea and want a deliberate adversarial pass to catch self-deception.

**Do not use this for:** ideas you have already validated with paying users (skip to PRD authoring), or as a substitute for actual customer discovery (this only catches obviously broken concepts).

## Inputs

The user must provide:
1. **One-sentence idea statement** ("X for Y who want Z").
2. **Founder context** (1-3 sentences): your background, why this idea, what unfair advantage if any.
3. **Target user guess** (1 sentence): who you think the customer is.
4. **Conviction level** (1-10): how strongly you currently believe this is the right idea.

If any input is missing, ask for it before proceeding. Do not infer.

## Constraints

**Must:**
- Apply all five test dimensions; never skip one even if the idea seems strong.
- Use the founder's own words to challenge the idea (quote them back).
- For every weakness, name the specific evidence or assumption that would have to be true for the idea to survive.
- End with exactly one of: **GO**, **KILL**, **RESHAPE** — never hedge with "GO with caveats" or "depends."
- If RESHAPE, give 2-4 concrete reshape directions, each as a new one-sentence idea statement.

**Must Not:**
- Invent customer quotes, market statistics, or competitor names. If you don't know, say "unknown — needs research."
- Soften the verdict to be polite. The point of this prompt is to catch self-deception.
- Use the words "promising," "exciting," "interesting," or "compelling" — they smuggle in approval. Be specific instead.
- Recommend skipping customer discovery on a GO verdict. GO means "worth the discovery investment," not "ready to build."

## Instructions

Apply each of the five tests below. For each, output: (a) the test question, (b) your one-paragraph assessment, (c) a score 0-3 (0 = fails badly, 3 = passes clearly), (d) the load-bearing assumption that would have to be true for a higher score.

### Test 1: Founder-Market Fit
Does the founder have unfair access, taste, network, or scar-tissue in this market? A generalist who "thinks the idea is cool" scores 0-1. A founder with 5+ years of operator experience in the exact target segment scores 3.

### Test 2: Contrarian Truth
What does the founder believe about this market that most people don't? An idea with no contrarian truth ("photo-sharing for dog owners — there isn't one yet") usually fails because if it were obvious and easy, someone competent would already be doing it. A strong contrarian truth ("incumbents assume X, but X is actually wrong because Y") scores 3.

### Test 3: Distribution Wedge
How will the first 100 paying users find this product? Score 0 if the answer is "we'll do content marketing" or "growth hacking" or "viral loops." Score 3 if the founder names a specific channel they already control or have proven access to (existing audience, employer relationship, community moderator role, etc.).

### Test 4: Why Now
What changed in the last 24 months that makes this idea possible/necessary now, when it wasn't 2 years ago? Score 0 if there's no answer or the answer is "AI" with no specifics. Score 3 if the founder names a concrete enabler (regulation change, cost-curve drop, platform shift, behavioral shift with measurable evidence).

### Test 5: 10x Claim
On what specific dimension is this 10x better than the status quo (not 2x, not "better UX")? Score 0 if the answer is "it's more modern" or "it's easier to use." Score 3 if the founder names a measurable dimension (cost, time, error rate, accessibility) where 10x improvement is plausible.

### Verdict logic
- **Sum 12-15 with no score-0 test → GO.** Worth investing in customer discovery (stage 2).
- **Sum 6-11 OR any single score-0 test → RESHAPE.** Provide 2-4 reshape directions.
- **Sum 0-5 → KILL.** Recommend either dropping the idea or returning after fundamental founder/market changes.

## Output Format

```
## Concept-Legs Test: [idea one-liner]

### Founder's own framing
> [quote founder's idea statement and conviction level]

### Test 1: Founder-Market Fit
**Assessment:** [paragraph]
**Score:** X/3
**Load-bearing assumption:** [what would need to be true]

### Test 2: Contrarian Truth
[same format]

### Test 3: Distribution Wedge
[same format]

### Test 4: Why Now
[same format]

### Test 5: 10x Claim
[same format]

### Total: X/15

### Verdict: [GO | KILL | RESHAPE]

[If GO]
**Next stage:** Run `stage-2-problem-validation/validation_customer_discovery_interview_protocol.md` with these 3 highest-risk assumptions to test first: [list]

[If KILL]
**Why:** [2-3 sentence summary of the fatal weakness]
**Conditions for revival:** [what would have to change in the founder, market, or technology]

[If RESHAPE]
**Reshape direction 1:** [new one-sentence idea]
**Reshape direction 2:** [new one-sentence idea]
**Reshape direction 3:** [optional]
**Reshape direction 4:** [optional]
**Re-run this prompt** with the reshaped idea you want to pursue.
```

## Verification

Before delivering, check:
- [ ] All 5 tests assessed with score and load-bearing assumption
- [ ] Verdict is exactly GO, KILL, or RESHAPE (no hedging)
- [ ] No invented customer quotes, market stats, or competitor names
- [ ] If RESHAPE, at least 2 concrete new idea statements provided
- [ ] If GO, the 3 highest-risk assumptions are named for stage 2 discovery
- [ ] No use of the banned words: promising, exciting, interesting, compelling

## False-Positive Prevention

Common ways this analysis goes wrong:
- **Founder-market fit score inflation** because the founder is articulate. Articulacy is not market access. Score on access, not vocabulary.
- **"AI" as a why-now answer.** "AI makes this possible" is too generic. Press for the specific capability (e.g., "GPT-4-level multimodal at $0.001/call enables X, which was $10/call in 2023").
- **Confusing differentiation with 10x.** "Cleaner UX than Jira" is not 10x. Ask: on what measurable axis is the gap 10x?
- **Treating a wide TAM as a GO signal.** TAM doesn't address distribution. A $50B market the founder can't reach is worse than a $50M market they own.
