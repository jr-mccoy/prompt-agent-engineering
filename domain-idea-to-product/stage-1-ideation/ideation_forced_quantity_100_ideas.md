---
title: "Forced Quantity — 100 Ideas to Break the Median Pattern"
category: ideation/divergence
description: "Force generation of 100 distinct ideas in response to a prompt, with no premature filtering. The first 20 are predictable, the next 30 are variants, and the most surprising ideas tend to appear in the 60–100 range. Designed for divergence breadth, not convergence; pair with a separate selection step."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - DS-01
  - CM-02
  - QA-01
difficulty: beginner
tags:
  - ideation
  - divergence
  - brainstorming
  - quantity-pressure
  - creativity
updated: "2026-05-10"
reasoning:
  styles: [divergent, generative]
  stakes: low_to_moderate
  horizon: variable
  uncertainty: variable
  evidence_quality: not_applicable
  domain_complexity: variable
  collaboration: solo_or_team
  output_format: numbered_idea_list
  user_role: [pm, designer, writer, founder, marketer, individual]
  mode: [diverge]
related_prompts:
  - domain-ideation/ideation_cross_domain_analogy_mining.md
  - domain-ideation/ideation_inverse_problem.md
  - domain-decision-making/decisioning_fresh_perspective_generator.md
---

# Forced Quantity — 100 Ideas

**Objective:** Force the generation of 100 distinct ideas for a brief, with no premature filtering. The discipline of quantity is the entire point: the first 20 ideas are usually predictable (median responses, conventional moves), 21–60 are variants and combinations of the first 20, and 61–100 is where genuinely surprising ideas tend to emerge — precisely because the obvious answers are exhausted. This prompt is for *divergence*, not selection. Pair with a separate convergence step.

**When to use:**
- A brief for naming, positioning, feature ideation, marketing concepts, plot ideas, side-project ideas, problem reframings — any task where you want to escape the median.
- The user has a few ideas they like and is at risk of locking in too early.
- Workshop facilitation where you want to defeat groupthink before voting.
- Personal ideation when stuck in a familiar frame.
- Pre-strategy: generating an option space before strategy reduces it.

**When NOT to use:**
- Decision-making — this prompt diverges; it does not converge. Hand off to selection.
- Tasks where the answer is well-defined and quantity is irrelevant (math problems, factual questions).
- Time pressure that doesn't allow for the discipline (this is a 30–90 minute exercise).
- The user wants quality over quantity. Quantity *generates* quality on the long tail; if quality alone is the goal, use a different prompt.

**Audience:** PMs, designers, writers, founders, marketers, anyone whose default is to stop at 5 ideas.

---

## Inputs / Context

1. **The brief.** What ideas are being generated for. Specific enough that "is this a valid idea for this brief" is binary.
2. **The success criteria** *for the brief* (not for the idea-generation step). What makes an idea good — but applied later, not during generation.
3. **Hard constraints.** Real-world non-negotiables (budget, technology, ethics, scope). These bound the idea space without filtering within it.
4. **Forbidden patterns.** Ideas the user has already considered and rejected, or that are off-table for known reasons. Stated up front to keep the generation fresh.
5. **Adjacent inspirations.** Related domains, brands, products, or examples to mine for analogical material.

---

## Constraints

### Must
- Generate **exactly 100** distinct ideas. Not 60, not 87. The discipline of the number is part of the exercise.
- Each idea is a **single sentence** capturing the essence — not a paragraph.
- Each idea is **distinct** from the others. Not "blue version of #42" unless the variant itself is the idea worth keeping.
- **No filtering during generation.** Bad-seeming ideas are recorded; selection happens after.
- Apply **stretch heuristics** every 20 ideas to break out of local clusters: cross-domain analogy, opposite-day, persona-swap, constraint flip, time-shift, scale shift, audience swap.
- Mark which ideas were generated under which heuristic so the variety is visible.
- After 100, perform a **light tagging pass** (not selection): tag each idea with 1–2 categories. The tagging makes the list searchable but does not score.

### Must Not
- Filter "bad" ideas during generation. The bad-seeming ideas often hold the kernel of a great idea.
- Generate variants of a single idea to pad the count. Variants are allowed when they're distinct on a meaningful dimension; mere relabelings are not.
- Stop early. If you stop at 65 because "we have enough," you've stopped exactly where the surprising ideas were going to start.
- Apply success criteria during generation. Success criteria are the convergence step, not divergence.
- Cluster too tightly within categories. The list should sprawl across the heuristics.

---

## Stretch heuristics (apply every ~20 ideas)

After ideas 1–20 (the obvious zone), rotate through these to break local optima:

1. **Cross-domain analogy:** "If this brief existed in [adjacent industry / nature / a game / a sport / cooking / music], it would be…"
2. **Opposite-day / inversion:** "What's the opposite of the obvious move? What if the goal were to fail at this?"
3. **Persona-swap:** "What would [a contrarian / a child / a regulator / a competitor / a 90-year-old / a 5-year-old / a designer from the 1970s] do?"
4. **Constraint flip:** "Drop one of the constraints. Now what becomes possible? Add a constraint that didn't exist. Now what?"
5. **Time-shift:** "How would this be done in 1920? In 2080? Tomorrow if all current tools disappeared?"
6. **Scale shift:** "What if the user base were 10? 10 million? What if the budget were $100? $100M?"
7. **Audience swap:** "What if this were for [a totally different audience]? Take the best version, then translate back."

---

## Instructions

### Step 1 — Sharpen the brief
Restate the brief in one sentence. Confirm hard constraints and forbidden patterns.

### Step 2 — First 20 (the obvious zone)
Generate ideas 1–20 fast and unfiltered. These will be the median ideas — what most people would propose. Don't try to be clever yet; flush the obvious answers out.

### Step 3 — Apply stretch heuristic 1 (analogy) for ideas 21–40
For each of the next 20, generate from cross-domain analogy.

### Step 4 — Apply stretch heuristic 2 (inversion) for ideas 41–55
Inversion-based ideas. Often the most surprising kernels emerge here.

### Step 5 — Persona-swap for ideas 56–70
Rotate through 3–5 personas, generating 4–5 ideas per persona.

### Step 6 — Constraint / scale / time shifts for ideas 71–90
Mix the remaining heuristics. By now, the obvious space is exhausted; the long tail starts here.

### Step 7 — Wildcard / freestyle for ideas 91–100
The final 10. By now you'll be tempted to repeat. Don't. Force one more pass through the heuristics or generate from genuine free association.

### Step 8 — Tag pass
After 100 ideas, tag each with 1–2 categories (e.g., feature / positioning / channel / brand / model / mechanism). The tagging surfaces the shape of the list.

### Step 9 — Surprise audit
Mark the 5–10 ideas that surprised you (or would surprise the user). Note which heuristic generated each. This is intelligence about which heuristics are most generative for this brief.

### Step 10 — Hand off
Stop. Do not select. Hand off to a convergence step (`ideation_idea_convergence_dot_voting.md` or a manual review against success criteria).

---

## False-Positive Prevention

1. **Premature filtering.** "I'm not going to write that one down because it's bad." Write it down. The kernel might be salvageable.
2. **Pad-by-variant.** Listing "X with blue", "X with red", "X with green" as three ideas is padding. One idea, three colors.
3. **Heuristic monoculture.** Generating all 100 ideas through the same heuristic produces a narrow list. Rotate.
4. **Stopping at 60.** "I have enough." You don't. The surprising ideas are in 61–100.
5. **Selection contamination.** Filtering as you generate caps the list at the median. The whole point is to escape the median.
6. **Persona theater.** Persona-swap that just generates ideas the user would generate, but voiced as someone else. Force the persona to actually push the idea space.
7. **Cleverness inflation.** Trying to make every idea "great" slows generation and biases toward the user's existing taste. Speed and quantity beat curation here.
8. **Over-tagging.** Tagging is a light pass; if it becomes a categorization project, you've drifted into selection.

---

## Output Format

```
# 100 ideas — [brief]

## Brief
> [Restated]
- Hard constraints: [...]
- Forbidden patterns: [...]
- Adjacent inspirations: [...]

## Ideas

### 1–20: Obvious zone
1. [idea]
2. [idea]
…
20. [idea]

### 21–40: Cross-domain analogy
21. [analogy: from cooking — idea]
22. [analogy: from nature — idea]
…

### 41–55: Inversion
41. [opposite-of-obvious — idea]
…

### 56–70: Persona-swap
56. [persona: contrarian — idea]
57. [persona: 5-year-old — idea]
…

### 71–90: Constraint / scale / time
71. [constraint flip: drop budget — idea]
72. [scale shift: 10 users — idea]
…

### 91–100: Wildcard
91. […]
…
100. [final]

## Tag pass
| #  | Idea (short)         | Tags                  |
|----|----------------------|------------------------|
| 1  | [...]                | feature, positioning  |
| 2  | [...]                | channel               |
| …  |                      |                        |

## Surprise audit
- Ideas that genuinely surprised: [#7, #43, #67, #91, ...]
- Heuristics that generated the surprises: [analogy, persona-swap, scale shift]
- Implication for next ideation session: [which heuristics worked]

## Handoff
- This list is unfiltered. Hand off to selection: `ideation_idea_convergence_dot_voting.md` or manual review against success criteria.
```

---

## Verification

- [ ] Exactly 100 ideas generated.
- [ ] Each idea is a single sentence.
- [ ] No two ideas are mere relabelings of each other.
- [ ] Stretch heuristics rotated through (analogy, inversion, persona, constraint, scale, time, wildcard).
- [ ] No filtering during generation.
- [ ] Tag pass completed.
- [ ] Surprise audit identifies the most surprising 5–10 ideas and their generating heuristic.
- [ ] No selection performed (handed off to convergence step).
- [ ] Heuristic source noted for ideas 21–100.
- [ ] No padding via mere variants.
