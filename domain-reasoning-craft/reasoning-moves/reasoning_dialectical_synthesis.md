---
title: "Dialectical Synthesis — Thesis, Antithesis, Genuine Synthesis"
category: reasoning-craft/reasoning-moves
description: "On a contested question, build the strongest version of the thesis, the strongest version of the antithesis, then a genuine synthesis that integrates both — distinct from compromise (which splits the difference) and from majority verdict (which picks a side). Surface what each side gives up and what survives intact. End with: is this synthesis real, or rhetoric concealing one side's victory?"
techniques:
  - ST-01
  - ST-02
  - RT-02
  - DS-01
  - CM-02
  - QA-01
difficulty: advanced
tags:
  - dialectical
  - synthesis
  - hegelian
  - integration
  - argumentation
updated: "2026-05-10"
reasoning:
  styles: [dialectical, integrative, structural]
  stakes: variable
  horizon: variable
  uncertainty: ambiguity
  evidence_quality: variable
  domain_complexity: variable
  collaboration: solo_or_pair
  output_format: thesis_antithesis_synthesis
  user_role: [analyst, writer, executive, mediator, policy, individual]
  mode: [synthesize, audit]
related_prompts:
  - domain-reasoning-craft/reasoning-moves/reasoning_steelman_construction.md
  - domain-reasoning-craft/epistemic/epistemic_disagreement_diagnosis.md
  - domain-decision-making/decisioning_blind_spot_mirror_see_what_im_missing.md
---

# Dialectical Synthesis

**Objective:** On a contested question, build the strongest **thesis**, the strongest **antithesis** (steelmanned), then attempt a genuine **synthesis** that integrates the substantive concerns of both — distinct from *compromise* (which splits the difference numerically) and *majority verdict* (which picks one side). Surface what each side gives up in the synthesis and what survives intact. End with an honest verdict: is this synthesis real, or is it rhetoric concealing that one side actually won?

**When to use:**
- A contested question where both sides have substantive grounding.
- Strategic / policy / design tradeoffs where the temptation to "balance" is strong.
- Personal life decisions where two values seem to conflict.
- Mediation between parties whose disagreement runs deep.
- Pre-publication: you've taken a position, and want to test if your position absorbs the strongest opposing view.

**When NOT to use:**
- One side is empirically wrong; pretend-synthesis is dishonest.
- The question has a clear winner once examined; manufactured synthesis wastes effort.
- Pure preference disagreement with no shared decision context.

**Audience:** Analysts, writers, executives, mediators, policy people, individuals working through values conflicts.

---

## Inputs / Context

1. **The contested question.**
2. **Thesis position** (often the user's current lean).
3. **Antithesis position** (the strongest opposing view).
4. **Stake.** What decision or position will use the synthesis.

---

## Constraints

### Must
- Build thesis at full strength (using `reasoning_steelman_construction.md` discipline if needed).
- Build antithesis at full strength.
- Identify the **substantive concerns** of each side: what each is *protecting* or *demanding*.
- Attempt synthesis that **honors both substantive concerns** — not by splitting the difference but by finding a frame, mechanism, or sequencing that gives each side what it needs.
- Surface what each side **gives up** in the synthesis and what they **keep intact**.
- End with a verdict: **genuine synthesis**, **partial synthesis** (one substantive concern not honored), or **rhetorical synthesis** (one side won, dressed as integration).
- If rhetorical: declare the actual winner explicitly.

### Must Not
- Default to compromise. Splitting the difference is rarely synthesis.
- Force synthesis where one side is genuinely correct.
- Hide the winner in feigned both-sides language.
- Treat synthesis as inherently better than picking a side. Sometimes one side is right.
- Confuse "we found shared values" with "we synthesized the disagreement."

---

## Instructions

### Step 1 — State the question
Single sentence. Acknowledge the disagreement is real.

### Step 2 — Thesis at full strength
- Position
- Strongest empirical evidence
- Underlying values / interests
- What thesis is fundamentally protecting or demanding

### Step 3 — Antithesis at full strength
- Position
- Strongest empirical evidence
- Underlying values / interests
- What antithesis is fundamentally protecting or demanding

### Step 4 — Identify substantive concerns
For each side, the *non-negotiable substantive concern* (what they cannot give up and still feel honored). Distinguish from positions (which can be compromised).

### Step 5 — Attempt synthesis
Try frames that honor both substantive concerns:
- **Reframe:** new conceptual frame in which both concerns fit
- **Mechanism:** technical / institutional design that delivers on both
- **Sequencing:** time-ordered approach that addresses one then the other
- **Domain split:** different conditions get different answers
- **Joint commitment:** both sides commit to a third thing that addresses both concerns

### Step 6 — Honor check
For each side: does the proposed synthesis actually honor your substantive concern? If "no" from either side, the synthesis fails as synthesis (it's compromise or pick-a-side).

### Step 7 — What's given up, what survives
- Thesis gives up: [...] / keeps: [...]
- Antithesis gives up: [...] / keeps: [...]

If one side gives up almost everything, it's not synthesis — it's that side losing.

### Step 8 — Verdict
- **Genuine synthesis:** both substantive concerns honored; both sides give up something but keep their core.
- **Partial synthesis:** one substantive concern only partially honored. Acknowledge.
- **Rhetorical synthesis:** one side won. Name the winner.
- **No synthesis possible:** the substantive concerns are genuinely incompatible. Recommend pick-a-side or shared-decision-rule (vote, defer, parallel paths).

### Step 9 — If genuine synthesis, write the synthesis position
A clear statement of the integrated view that both sides could sign.

---

## False-Positive Prevention

1. **Compromise-as-synthesis.** "60% your way, 40% mine" averaged is not integration.
2. **Both-sides-ism when one side is wrong.** Manufactured synthesis on empirical questions is dishonest.
3. **Synthesis-as-rhetoric.** Dressing up one side's victory as integration. The verdict step exists to defeat this.
4. **Position-confusion.** Synthesizing positions (often impossible) when the actual move is synthesizing underlying interests.
5. **Synthesis worship.** Sometimes the right move is to pick a side or accept incompatibility.
6. **Honor-check skip.** Without checking that both sides feel honored, you've described a frame, not done synthesis.

---

## Output Format

```
# Dialectical synthesis — [question]

## Question
> [Contested]

## Thesis (full strength)
- Position: [...]
- Strongest evidence: [...]
- Underlying values / interests: [...]
- Substantive concern (non-negotiable): [...]

## Antithesis (full strength)
- Position: [...]
- Strongest evidence: [...]
- Underlying values / interests: [...]
- Substantive concern (non-negotiable): [...]

## Synthesis attempt
- Frame / mechanism / sequencing / domain-split / joint commitment used: [...]
- Synthesis statement: [paragraph integrating both]

## Honor check
- Does thesis's substantive concern get honored? [yes / partial / no]
- Does antithesis's substantive concern get honored? [yes / partial / no]

## What's given up, what survives
- Thesis gives up: [...]
- Thesis keeps: [...]
- Antithesis gives up: [...]
- Antithesis keeps: [...]

## Verdict
- [Genuine synthesis / Partial / Rhetorical / No synthesis possible]
- If rhetorical: actual winner is [...]
- If no synthesis: recommended path is [pick-a-side / shared-decision-rule]

## Synthesis position (if genuine)
> [Clear statement both sides could sign]
```

---

## Verification

- [ ] Thesis and antithesis both at full strength.
- [ ] Substantive concerns identified separately from positions.
- [ ] Synthesis attempts a real integration mechanism, not split-the-difference.
- [ ] Honor check performed for both sides.
- [ ] What's given up vs kept, surfaced for both sides.
- [ ] Verdict explicit (genuine / partial / rhetorical / none possible).
- [ ] If rhetorical, winner named.
- [ ] No false synthesis when one side is empirically right.
