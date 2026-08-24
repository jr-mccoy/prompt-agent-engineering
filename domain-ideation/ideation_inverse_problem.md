---
title: "Inverse Problem — Solve It By Inverting It"
category: ideation/inversion
description: "Take a problem and invert it. Instead of 'how do we achieve X?', ask 'how would we guarantee NOT-X?' or 'how would we make this fail?' The inverted problem often surfaces failure modes, hidden assumptions, and asymmetric leverage points faster than the direct framing — and the inverse answers often translate back into solutions that the direct framing missed."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - DS-01
  - CM-02
  - QA-01
difficulty: intermediate
tags:
  - ideation
  - inversion
  - lateral-thinking
  - failure-modes
  - assumption-surfacing
updated: "2026-05-10"
reasoning:
  styles: [inversive, adversarial, structural]
  stakes: variable
  horizon: variable
  uncertainty: variable
  evidence_quality: variable
  domain_complexity: variable
  collaboration: solo_or_team
  output_format: inversion_then_translation
  user_role: [founder, pm, designer, strategist, engineer, individual]
  mode: [diverge, audit, diagnose]
related_prompts:
  - domain-ideation/ideation_forced_quantity_100_ideas.md
  - domain-ideation/ideation_cross_domain_analogy_mining.md
  - domain-prompt-engineering/evaluation/correctness_pre_mortem.md
---

# Inverse Problem

**Objective:** Solve a problem by inverting it. Instead of asking "how do we achieve X?", ask "how would we guarantee NOT-X?" or "what would we do if we *wanted* to make this fail?" Inversion exploits a useful asymmetry: failure modes and threat surfaces are often easier to enumerate concretely than success paths, and listing what to avoid can be more diagnostic than listing what to do. The inverted answers then translate back into the direct problem as constraints, design rules, or interventions.

**When to use:**
- Stuck on a positive framing where the path forward feels diffuse.
- Designing a system whose failure modes you want to surface before launch.
- Pre-mortem on a strategy or plan.
- Diagnosing why something isn't working — invert to "what would I do if I wanted it to fail like this?"
- Personal contexts: "what would I do if I wanted to stay stuck?" often surfaces what's keeping you stuck.

**When NOT to use:**
- The problem is purely generative and has no negative form (e.g., "write a poem about autumn"). Inversion would produce nothing.
- The user is in distress and inversion would feel cruel. (Inverting "how do I get unstuck?" into "how do I stay stuck?" is sometimes useful and sometimes harmful; read context.)
- The problem has been worked through positively in detail and inversion would be redundant.

**Audience:** Founders, PMs, designers, strategists, engineers, anyone who's bouncing off a problem in its direct form.

---

## Inputs / Context

1. **The problem in its direct form.** What is being attempted: "How do we [achieve X]?"
2. **What's been tried so far.** So inversion can hit different surface area.
3. **The system or person whose action would matter.** Inversion needs an actor whose moves we're enumerating.
4. **Stakes.** What it costs if the problem isn't solved.
5. **Reverse-permission check.** Some inversions ("how would we cause harm to users?") need the user to have a legitimate purpose (e.g., security review, threat modeling). Surface this before generating, not for paternalism but for context-matched output.

---

## Constraints

### Must
- Restate the problem in inverted form. Multiple inversions are possible — surface 2–3 framings and pick:
  - **NOT-X:** "How would we guarantee NOT-X?"
  - **Fail:** "What would we do if we wanted this to fail?"
  - **Worst case:** "What would the worst possible outcome look like and how would we engineer it?"
  - **Sustain failure:** "What's keeping the current bad state in place?"
- Generate at least 8–15 specific moves that would produce the inverted outcome. Each is a concrete action or design choice, not a generality.
- For each inverse move, identify whether it's currently happening (in part) in the actual system. The current happenings are the load-bearing diagnostic.
- **Translate back:** for each inverse move, derive the corresponding direct-action — what would we do (or stop doing) to prevent the inverse from occurring?
- Identify the **highest-leverage inverse move** — the one whose elimination would most improve the direct outcome.
- Note any inverse moves that have no direct translation (sometimes inversion exposes failure modes that aren't actionable; flag and discuss).

### Must Not
- Generate vibes-level inversions ("be lazy", "don't try"). Inverse moves should be specific actions or design choices.
- Use inversion to license harmful action design (this prompt is for diagnosis and avoidance, not for actually constructing harm).
- Translate every inverse move into a direct action without sanity-checking — sometimes the direct translation is naive, and the inverse move is informative without being directly actionable.
- Stop after generating inverses without translation. The translation step is where the value lands.
- Ignore inverse moves that the user is currently making. Those are diagnostic.

---

## Instructions

### Step 1 — Restate the direct problem
"How do we [X]?" — the user's current framing.

### Step 2 — Generate 2–3 inversion framings
- NOT-X
- Engineer failure
- Worst case design
- Sustain current bad state (if diagnosing a stuck situation)

Pick the framing that's likely to be most generative for this problem. Sometimes run two.

### Step 3 — Generate 8–15 specific inverse moves
Each inverse move is a concrete action or design choice that would produce the inverted outcome. Be specific:

- Bad: "Write a confusing user guide."
- Good: "Use 5+ different terms for the same concept across the guide; don't define them; bury the most critical step on page 23 in a paragraph; assume the reader knows what 'configure the daemon' means."

### Step 4 — Mark currently-happening moves
For each inverse move, mark whether the actual system / person / strategy is currently doing it (in whole or in part). Currently-happening inverse moves are the diagnostic gold.

### Step 5 — Translate back
For each inverse move, derive the direct action that would prevent it. Some translations are straightforward inversions ("don't do that"); others require designing a positive replacement ("provide a glossary upfront with 5 terms locked").

### Step 6 — Identify highest-leverage inverse
Which inverse move, if eliminated, would most improve the direct outcome? Often this is the one currently happening that has the largest effect.

### Step 7 — Surface non-translatable inverses
Some inverse moves don't translate cleanly into actions ("if a key person quit, the project would die" — you can't fully prevent that). These are still informative as risk surface; capture them.

### Step 8 — Action set
A small set of concrete direct actions, derived from the translation step:
- Stop doing: [list]
- Start doing: [list]
- Design in: [list]
- Watch for: [non-translatable but worth monitoring]

---

## False-Positive Prevention

1. **Vibes inversion.** "Be bad at it" is not an inverse move. Specificity is the entire value.
2. **Translation skip.** Listing inverses without translating back is half the exercise.
3. **Self-blaming theater.** When inversion exposes that the user is currently doing several inverse moves, the response is action, not self-flagellation. Move to step 8.
4. **Currently-happening blindness.** Generating inverse moves "the system might do" while ignoring the ones it's already doing. The current ones are the diagnostic.
5. **Cruelty drift.** "How would I keep myself stuck?" can be cathartic-and-useful or cruel-and-useless depending on context. Read whose problem this is and whether the inversion frame helps.
6. **Harmful-design license.** This prompt is for diagnosis and prevention, not for designing actual harm. If the inverse moves describe harms to others, the only legitimate next step is prevention design.
7. **Non-translatable dismissal.** Inverse moves with no direct translation aren't useless — they're risk surface. Capture them in the watch-list.
8. **Single-framing tunneling.** Picking one inversion framing and missing the others. Run 2–3 framings if the first is unproductive.

---

## Output Format

```
# Inverse problem — [direct problem]

## Direct problem
> "How do we [X]?"

## Inversion framings considered
1. NOT-X: [framing]
2. Engineer failure: [framing]
3. Sustain bad state: [framing]
- Selected: [which framing(s)]

## Inverse moves
| # | Inverse move (specific action) | Currently happening? | Effect size if removed | Translates to direct action? |
|---|--------------------------------|----------------------|------------------------|------------------------------|
| 1 | [specific]                     | yes — partial        | high                   | yes — [direct action]        |
| 2 | [specific]                     | no                   | medium                 | yes — [direct action]        |
| 3 | [specific]                     | yes — fully          | high                   | yes — [direct action]        |
| 4 | [specific]                     | no                   | low                    | not directly                 |
| … |                                |                      |                        |                              |

## Highest-leverage inverse
- Inverse move #: [N]
- Why: [largest currently-happening effect]
- Direct action to remove it: [...]

## Non-translatable inverses (watch list)
- [Inverse move that's not directly preventable but worth monitoring]
- [...]

## Action set
**Stop doing**
- [...]
- [...]

**Start doing**
- [...]
- [...]

**Design in**
- [...]

**Watch for**
- [non-translatable risks to monitor]
```

---

## Verification

- [ ] At least 2 inversion framings considered before picking.
- [ ] 8–15 specific inverse moves generated (not vibes).
- [ ] Each inverse move marked for currently-happening status.
- [ ] Each inverse move has a direct-action translation (or marked non-translatable).
- [ ] Highest-leverage inverse identified and direct action specified.
- [ ] Non-translatable inverses captured in a watch list.
- [ ] Final action set has Stop / Start / Design-in / Watch sections.
- [ ] No vibes-level inverses.
- [ ] No skipped translation step.
- [ ] No harmful-design output (if the inverse describes harms, the output is prevention).
