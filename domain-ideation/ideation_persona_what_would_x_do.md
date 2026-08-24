---
title: "What Would X Do — Ideation Through Five Generative Personas"
category: ideation/perspective-shift
description: "Generate ideas by adopting five generative perspectives — contrarian, beginner, regulator, competitor, and child — each of which naturally reaches ideas your default frame suppresses. The output isn't the persona's literal voice; it's the perspective shift each one forces. Distinct from market personas (which describe customers); these are reasoning lenses for divergence. Optionally add 1–2 user-supplied personas."
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
  - personas
  - perspective-shift
  - divergence
  - reframing
updated: "2026-05-27"
reasoning:
  styles: [perspectival, divergent, dialectical]
  stakes: low_to_moderate
  horizon: variable
  uncertainty: variable
  evidence_quality: not_applicable
  domain_complexity: variable
  collaboration: solo_or_team
  output_format: structured
  user_role: [pm, designer, founder, marketer, strategist, individual]
  mode: [diverge]
related_prompts:
  - domain-ideation/ideation_forced_quantity_100_ideas.md
  - domain-ideation/ideation_jobs_to_be_done_reframe.md
  - domain-ideation/ideation_worst_idea_first.md
---

# What Would X Do — Ideation Through Five Generative Personas

**Objective:** Break out of a single default frame by generating ideas from five distinct perspectives, each of which reliably reaches ideas the default suppresses. The five core lenses — **contrarian, beginner, regulator, competitor, child** — are chosen because each forces a different cognitive move: the contrarian inverts assumptions, the beginner ignores "how it's done," the regulator surfaces what must not happen, the competitor attacks your weak points, and the child asks the naive question that exposes the obvious-but-unspoken. The point is *not* the persona's literal output — it's the perspective shift each one forces on you. These are generative reasoning lenses, not market personas: they describe how to *think*, not who buys.

**When to use:**
- A single perspective (usually your own discipline's) is dominating the ideation.
- You want a structured, fast way to triangulate a problem from incompatible angles.
- Surfacing blind spots before committing — the regulator and competitor lenses double as a light pre-mortem.
- Workshop ideation where assigning personas to people defeats groupthink.

**When NOT to use:**
- You need *market* personas describing real customer segments. That's a research task, not this.
- The problem has one correct answer and perspective doesn't change it (factual / computational tasks).
- You've already triangulated the perspectives and need to converge. Hand off to selection.

**Audience:** PMs, designers, founders, marketers, and strategists whose ideation is bounded by their own professional frame; facilitators running multi-angle sessions.

---

## Inputs / Context

1. **The brief.** What ideas are being generated for.
2. **The default frame.** Whose perspective currently dominates (e.g., "engineering-led", "founder's vision", "marketing"). Naming it makes the shifts sharper.
3. **Optional extra personas.** 1–2 user-supplied lenses — an admired figure ("what would [a known builder] do?"), a specific stakeholder, or a domain archetype. Used in addition to the five core lenses.
4. **Hard constraints.** Real limits, so the regulator and competitor lenses stay grounded.
5. **The goal.** What a good idea achieves — used to flag, not to filter during generation.

---

## Constraints

### Must
- Run **all five core lenses**, generating **4–5 ideas each** (20–25 total), plus 4–5 per any user-supplied persona.
- For each lens, state the **perspective shift** it forces *before* generating — what this persona refuses to assume that you assume by default.
- Make each idea **specific to the persona's actual logic**, not your idea voiced as the persona. The contrarian's idea should be one *you* would resist; the child's should be one you'd dismiss as naive.
- Note which lens produced the **idea you'd least likely have reached** on your own — that lens is the most valuable for this brief.
- Keep generation and evaluation separate: flag promising ideas in one pass at the end.

### Must Not
- Produce persona theater — your own ideas wearing a costume. If the contrarian's ideas are all things you already believe, you haven't shifted perspective.
- Confuse these with market personas. No "Sarah, 34, busy mom" demographics; these are reasoning stances.
- Soften the uncomfortable lenses. The regulator and competitor exist to say things you don't want to hear; let them.
- Filter during generation. The naive / contrarian ideas often hold the kernel.
- Collapse two lenses (e.g., contrarian and competitor) into one. Each forces a distinct move.

---

## The five core lenses

| Persona | Cognitive move | The question it forces |
|---------|----------------|------------------------|
| **Contrarian** | Inverts the shared assumption | "What if the opposite of the obvious approach is right?" |
| **Beginner** | Ignores "how it's done" | "Why does it work this way at all? What if I didn't know the rules?" |
| **Regulator** | Surfaces what must not happen | "How could this harm, fail, or be abused — and what would I require?" |
| **Competitor** | Attacks your weak points | "Where are they soft, and how would I beat them or make this irrelevant?" |
| **Child** | Asks the naive, exposing question | "Why? Why not just…? What if it were a game / free / instant?" |

---

## Instructions

### Step 1 — State brief and default frame
Restate the brief. Name the perspective currently dominating, so each lens is a deliberate departure from it.

### Step 2 — Contrarian
State the shared assumption the contrarian rejects. Generate 4–5 ideas that follow from rejecting it. These should be ideas you'd instinctively argue against.

### Step 3 — Beginner
Drop the "how it's done" knowledge. Generate 4–5 ideas a smart newcomer would propose precisely because they don't know the constraints insiders take for granted.

### Step 4 — Regulator
Adopt the stance of someone responsible for preventing harm and failure. Generate 4–5 ideas: requirements, guardrails, or designs that the safety/compliance lens produces — several of which double as features.

### Step 5 — Competitor
Adopt a rival's stance. Generate 4–5 ideas for how a competitor would beat you, undercut you, or make your approach irrelevant — then keep them as ideas *you* could run first.

### Step 6 — Child
Ask the naive questions. Generate 4–5 ideas from "why not just…?", "why is it so complicated?", "what if it were a game?" — the ideas adults dismiss as too simple.

### Step 7 — User-supplied personas (optional)
For each extra persona, state its cognitive move and generate 4–5 ideas in its logic.

### Step 8 — Cross-lens audit and flag
Identify the lens that produced the idea you'd least likely have reached alone. Flag the 3–7 most promising ideas across all lenses in one pass. Hand off to convergence.

---

## False-Positive Prevention

1. **Persona theater.** The clearest failure: every persona generates ideas you already hold, just relabeled. Test — if the contrarian's ideas don't make you wince, you didn't shift.
2. **Market-persona confusion.** Slipping into "this persona is a 28-year-old urban professional" turns a reasoning lens into a customer segment. These describe thinking, not buying.
3. **Softening the hard lenses.** Letting the regulator be polite or the competitor be gentle wastes the two most diagnostic lenses. They're supposed to be uncomfortable.
4. **Naive-idea dismissal.** Discarding the child's ideas as too simple loses the ones that expose needless complexity. Keep them; simplicity is often the breakthrough.
5. **Lens collapse.** Treating contrarian and competitor as the same move halves the triangulation. Contrarian inverts your assumption; competitor attacks your position.
6. **Shift-statement skip.** Generating without first naming what the persona refuses to assume produces shallow, in-frame ideas. State the shift first.
7. **Generation-time filtering.** Killing an idea because "we'd never do that" caps the output at your comfort zone. Flag at the end.
8. **Persona overload.** Adding six extra personas dilutes each. Cap user-supplied at 1–2.

---

## Output Format

```
# What would X do — [brief]

## Brief
> [Restated]
- Default frame currently dominating: [...]
- Goal: [...]
- Hard constraints: [...]

## Contrarian — shift: [assumption rejected]
1. [idea you'd resist]
2. …
(4–5)

## Beginner — shift: [knowledge dropped]
1. …
(4–5)

## Regulator — shift: [harm/failure focus]
1. …
(4–5)

## Competitor — shift: [attack your weak point]
1. …
(4–5)

## Child — shift: [naive question]
1. …
(4–5)

## [User persona, if any] — shift: [...]
1. …
(4–5)

## Cross-lens audit
- Most valuable lens for this brief: [persona] — produced [idea] I'd least likely reach alone.
- Flagged candidates (3–7): [#s across lenses]
- Hand off to: ideation_idea_convergence_dot_voting.md
```

---

## Verification

- [ ] All five core lenses run, 4–5 ideas each (20–25 total).
- [ ] Each lens states the perspective shift before generating.
- [ ] Ideas reflect the persona's actual logic, not the user's ideas in costume.
- [ ] Regulator and competitor lenses kept uncomfortable, not softened.
- [ ] These treated as reasoning lenses, not market/customer personas.
- [ ] User-supplied personas (if any) capped at 1–2, with stated cognitive move.
- [ ] Most valuable lens identified.
- [ ] No generation-time filtering; flagging done in one final pass.
