---
title: "Worst Idea First — Generate Terrible Ideas, Then Mine the Kernels"
category: ideation/inversion
description: "Deliberately generate 10–15 of the worst possible ideas — offensive, illegal, stupid, opposite-of-the-brief, technically impossible — then for each, name exactly what makes it bad and ask whether changing one thing turns the kernel into something real. Breaking the politeness reflex that suppresses odd ideas is the point; the inversions of bad ideas are often surprisingly fresh."
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
  - worst-idea
  - inversion
  - groupthink-breaking
  - kernel-extraction
updated: "2026-05-27"
reasoning:
  styles: [inversive, divergent, generative]
  stakes: low_to_moderate
  horizon: variable
  uncertainty: variable
  evidence_quality: not_applicable
  domain_complexity: variable
  collaboration: solo_or_team
  output_format: structured
  user_role: [pm, designer, founder, marketer, facilitator, individual]
  mode: [diverge]
related_prompts:
  - domain-ideation/ideation_inverse_problem.md
  - domain-ideation/ideation_crazy_eights.md
  - domain-ideation/ideation_persona_what_would_x_do.md
---

# Worst Idea First — Generate Terrible Ideas, Then Mine the Kernels

**Objective:** Deliberately generate the *worst* possible ideas for a brief — offensive, illegal, stupid, exactly-opposite-of-the-goal, technically impossible — and then mine them for usable kernels. The technique works on two levels. First, the permission to be terrible removes the social and self-imposed politeness that quietly censors the odd ideas where breakthroughs hide; it's far easier to say a wild thing once it's framed as "the worst idea." Second, bad ideas carry structure: naming *why* an idea is bad points directly at a constraint, and inverting or lightly modifying a bad idea often lands somewhere genuinely fresh. The discipline is the second half — most teams enjoy the bad-idea generation and skip the kernel extraction, which is where the value is.

**When to use:**
- A group is being too polite or cautious; everyone is proposing safe, similar ideas.
- You want to break groupthink and lower the stakes on contribution (it's safe to say a bad idea on purpose).
- The brief feels constrained and you can't tell which constraints are real — bad ideas surface them by violating them.
- As a fun, fast workshop energizer that still produces usable material.

**When NOT to use:**
- You need refined, evaluated options now — this is upstream of selection.
- The "bad ideas" would describe real harm you intend to carry out. This is a generative/diagnostic exercise; harmful kernels are flagged and dropped, not built.
- The group is already aligned and converging; this reopens divergence.

**Audience:** PMs, designers, founders, marketers, and facilitators breaking a too-polite or stuck group; individuals who censor their own odd ideas.

---

## Inputs / Context

1. **The brief.** What ideas are being generated for, and the actual goal.
2. **What "good" would look like.** So "the opposite of the brief" is well-defined enough to invert.
3. **Real constraints.** So the kernel-extraction can tell "violates a hard limit" from "violates a soft assumption."
4. **Tone.** Workshop-playful or analytical — affects framing, not the method.
5. **Sensitivity flags.** Any topics where "offensive" bad ideas should stay abstract rather than specific (for taste, not censorship of the method).

---

## Constraints

### Must
- Generate **10–15 deliberately terrible ideas**, spanning several flavors of bad: opposite-of-the-goal, illegal/unethical, absurdly expensive, technically impossible, insulting to the user, maximally boring, comically over-engineered.
- For **each** bad idea, name **precisely what makes it bad** — the specific failure (illegal, hated by users, impossible, off-brief). The diagnosis is the bridge to the kernel.
- For each, ask the **one-change question**: "if we changed only [one specific thing], could the kernel of this become a real idea?" Generate the modified version where one exists.
- Separate kernels into: **real candidate** (the modified idea is genuinely usable), **provocation** (no usable version, but it reframed the problem), and **dead** (bad with no salvageable kernel).
- Identify which **constraint each bad idea violated** — the pattern reveals which constraints are load-bearing and which are merely assumed.
- Drop any bad idea whose kernel still describes **real harm to others**; do not extract or build it.

### Must Not
- Skip the kernel extraction. Generating bad ideas without mining them is entertainment, not ideation.
- Soften the bad ideas into mediocre ones. "A slightly worse version of our plan" isn't a worst idea; it's a tepid one. Go all the way to terrible.
- Extract kernels from genuinely harmful ideas. The method uses "offensive/illegal" to break politeness, not to design harm — harmful kernels are flagged and dropped.
- Treat every bad idea as having a usable kernel. Many are simply dead; honest tagging matters.
- Let the bad ideas all be the same flavor of bad. Spread across the flavors so different constraints get violated.

---

## Flavors of bad (spread across these)

- **Opposite-of-goal:** does the exact reverse of what success requires.
- **Illegal / unethical:** would get you sued or shamed.
- **Impossible:** violates physics, budget, or time by orders of magnitude.
- **User-hostile:** actively annoys, insults, or punishes the user.
- **Maximally boring:** the most generic, forgettable version imaginable.
- **Over-engineered:** absurdly complex solution to a simple need.

---

## Instructions

### Step 1 — Frame the permission
Restate the brief and the real goal. Explicitly grant permission: the next ideas should be *bad on purpose*. State that nothing here is a commitment.

### Step 2 — Generate 10–15 terrible ideas
Produce bad ideas fast, spreading across the flavors. Each is one sentence. Push to genuinely terrible, not merely weak.

### Step 3 — Diagnose the badness
For each bad idea, name the specific failure: *why* exactly is it bad? (Illegal? Impossible? Users would hate it? Off-brief?) Note which constraint it violates.

### Step 4 — Apply the one-change question
For each, ask: change only one thing — what's the kernel, and does a single modification make it real? Write the modified version where one exists. (E.g., "charge users to file a complaint" → bad → kernel: friction filters low-value complaints → real version: a structured, free triage form that front-loads the effort.)

### Step 5 — Tag the kernels
Tag each: **real candidate** / **provocation** / **dead**. Drop any kernel describing real harm to others.

### Step 6 — Read the constraint map
Collect which constraints the bad ideas violated. Which were hard (legal, physics) and which were merely assumed (brand tone, "we don't do that")? The assumed ones are candidates for a constraint flip.

### Step 7 — Candidate set
Collect the "real candidate" kernels and the most useful "provocations." Hand off to convergence.

### Step 8 — Hand off
Pass the candidates to `ideation_idea_convergence_dot_voting.md` or `ideation_idea_kill_list.md`. Note the provocations separately as reframing material.

---

## False-Positive Prevention

1. **Extraction skip.** The most common failure: a fun list of terrible ideas and no kernels mined. The second half is the value; do not stop at Step 2.
2. **Tepid badness.** "A slightly clunkier UI" is weak, not worst. If the bad ideas don't make people laugh or wince, they aren't bad enough to break the politeness reflex.
3. **Harm extraction.** Using "illegal/offensive" to actually design harm is a category error. Those flavors exist to free the imagination; harmful kernels are dropped, not built.
4. **Forced kernels.** Not every bad idea hides a good one. Inventing a strained kernel for a genuinely dead idea wastes the step. Tag it dead.
5. **Flavor monoculture.** Ten "impossible" ideas violate one constraint ten times. Spread across flavors so the constraint map is informative.
6. **One-change inflation.** "Change one thing" means one. If a bad idea needs five changes to be good, it's a different idea — note it but don't pretend it was the kernel.
7. **Constraint-map neglect.** Skipping Step 6 misses the free diagnostic: which "rules" are real and which are just habit.
8. **Commitment creep.** Treating a bad idea as a real proposal mid-list re-engages the editor and kills the permission. Nothing is a commitment until the candidate set.

---

## Output Format

```
# Worst idea first — [brief]

## Brief
> [Restated]
- Real goal: [...]
- What "good" looks like: [...]
- Real constraints: [...]

## Terrible ideas + kernels
| # | Bad idea (1 sentence) | Flavor | Why it's bad / constraint violated | One-change kernel | Tag |
|---|------------------------|--------|------------------------------------|-------------------|-----|
| 1 | [...] | opposite-of-goal | [...] | [modified version] | real candidate |
| 2 | [...] | user-hostile | [...] | [modified version] | provocation |
| 3 | [...] | impossible | [...] | — | dead |
| … | | | | | |
(10–15 rows)

## Constraint map
- Hard constraints violated: [legal, physics, budget — these are real]
- Assumed constraints violated: [brand tone, "we don't do that" — flip candidates]

## Candidate set
- Real-candidate kernels: [...]
- Useful provocations (reframing material): [...]
- Harmful kernels dropped: [count]
- Hand off to: ideation_idea_convergence_dot_voting.md or ideation_idea_kill_list.md
```

---

## Verification

- [ ] 10–15 deliberately terrible ideas generated, spread across flavors.
- [ ] Each bad idea diagnosed for *why* it's bad and which constraint it violates.
- [ ] One-change kernel question applied to each.
- [ ] Kernels tagged real candidate / provocation / dead.
- [ ] Harmful kernels flagged and dropped, not extracted.
- [ ] Constraint map distinguishes hard from merely-assumed constraints.
- [ ] Candidate set = real kernels + useful provocations.
- [ ] No forced kernels for dead ideas; no tepid "bad" ideas.
