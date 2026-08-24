---
title: "Red Team Briefing — Build and Rehearse the Case Against Your Own Conclusion"
category: reasoning-craft/epistemic
description: "Before shipping a thesis, memo, presentation, or position, construct the strongest opposition: the most credible critic (real or composite), their strongest argument, their strongest evidence, and their single most cutting question — then pre-draft responses to each. Distinct from surfacing disconfirming evidence; this rehearses the specific adversary's attack so the author isn't surprised in the room. Counters the failure mode of shipping a position that's only ever been pressure-tested by its author."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - DS-01
  - CM-02
  - QA-01
difficulty: intermediate
tags:
  - epistemic
  - red-team
  - pre-publication
  - rehearsal
  - adversarial
updated: "2026-05-21"
reasoning:
  styles: [adversarial, dialectical, counterfactual]
  stakes: high
  horizon: variable
  uncertainty: ambiguity
  evidence_quality: variable
  domain_complexity: variable
  collaboration: solo_or_pair
  output_format: opposition_brief_plus_response_rehearsal
  user_role: [executive, founder, analyst, researcher, individual]
  mode: [rehearse, audit, synthesize]
related_prompts:
  - domain-reasoning-craft/epistemic/epistemic_evidence_against_yourself.md
  - domain-reasoning-craft/reasoning-moves/reasoning_steelman_construction.md
  - domain-reasoning-craft/reasoning-moves/reasoning_dialectical_synthesis.md
---

# Red Team Briefing

**Objective:** Build the strongest possible case *against* your own conclusion before you publish or present it, embodied in a specific opponent. Name the most credible critic (a real person, a composite, or an archetype), construct their strongest argument and strongest evidence, and write the single most cutting question they would ask. Then pre-draft your responses — and mark which responses are solid versus which expose a real weakness you need to fix before shipping. Distinct from `epistemic_evidence_against_yourself.md` (which surfaces disconfirming evidence in the abstract); this prompt rehearses a concrete adversary's attack and your reply, so you're not improvising under pressure.

**When to use:**
- You're about to present or publish a thesis, recommendation, memo, or strategy and want to survive the toughest room.
- A decision will face a skeptical reviewer, board, investor, opposing counsel, or expert panel.
- You've gathered the case *for* and want to stress-test it against the case *against* before committing.
- Preparing for a debate, defense, or high-stakes pitch where specific objections are predictable.

**When NOT to use:**
- You're still forming the view and need divergent input, not adversarial pressure — gather evidence first (`epistemic_evidence_against_yourself.md`).
- The goal is to integrate two views into a synthesis rather than defend one — use `reasoning_dialectical_synthesis.md`.
- The stakes are low and a full red-team rehearsal would be theater.

**Audience:** Executives, founders, analysts, and researchers about to defend a position in a room that will push back.

---

## Inputs / Context

1. **The conclusion / position.** What you're about to ship, stated as you'd state it to the audience.
2. **The audience and the toughest critic in it.** Who will push back, and who is the most credible, best-prepared opponent.
3. **Your strongest support.** The evidence and reasoning you're relying on.
4. **Known objections.** Anything you've already heard or anticipate.
5. **What's at stake in the room.** Approval, funding, a decision, reputation — sets how hard the rehearsal needs to be.

---

## Constraints

### Must
- Name a **specific critic** — a real person, a credible composite, or a defined archetype (the skeptical CFO, the domain expert who's seen this fail, the opposing counsel). Generic "someone might say" is too weak.
- Build the critic's case at **full strength** — steelmanned, not strawmanned. The critic gets their best argument, best evidence, and sharpest question (use `reasoning_steelman_construction.md` discipline).
- Produce the single **most cutting question** — the one you'd least want to be asked.
- Pre-draft a **response to each attack**, then **honestly grade your own response**: solid / partial / exposes-a-real-gap.
- For any response graded partial or exposing-a-gap, specify the **fix before shipping** (more evidence, a scope narrowing, a concession to fold in).
- Distinguish objections you can **answer** from weaknesses you must **concede or fix** — pretending a real gap is answerable is the failure mode.

### Must Not
- Strawman the critic so your rehearsed answers look strong. A red team that loses on purpose is worthless.
- Rehearse only the comfortable objections. Lead with the one you're most afraid of.
- Treat the rehearsal as confirmation that you're right. Its value is finding the gaps, not certifying their absence.
- Confuse a fluent response with a sound one. Grade on whether it actually withstands the attack, not on whether it sounds confident.
- Skip the "fix before shipping" step for exposed gaps — finding a gap and ignoring it is worse than not looking.

---

## Instructions

### Step 1 — State the position as you'll present it
Exactly as the audience will hear it, including the ask.

### Step 2 — Cast the critic
Name the most credible, best-prepared opponent in (or relevant to) the room. Give them standing: why their objection would carry weight.

### Step 3 — Build the critic's strongest argument
Steelman it. What is the best version of the case against your position? Not the version you can easily beat — the version that would worry you.

### Step 4 — Find the critic's strongest evidence
What's the most damaging fact, precedent, or data point they'd bring? Include the one you hope they don't know about.

### Step 5 — Write the most cutting question
The single question you'd least want asked. Write it in the critic's voice.

### Step 6 — Pre-draft and grade your responses
For each of the argument, the evidence, and the question: draft your response, then grade it solid / partial / exposes-a-gap. Be honest — a generous self-grade defeats the exercise.

### Step 7 — Fix list and ship decision
For partial/gap responses, specify the fix (evidence to add, scope to narrow, concession to fold in). Then decide: ship as is, ship with fixes, or rework. State which.

---

## False-Positive Prevention

1. **Strawman red team.** Building a weak critic so your answers shine. Steelman the opponent; the test only works if they could actually win some exchanges.
2. **Comfortable-objection bias.** Rehearsing the questions you can answer and avoiding the one you dread. The dreaded question goes first.
3. **Rehearsal-as-validation.** Using a survived red team as proof you're right. It surfaces gaps; passing it is necessary, not sufficient.
4. **Fluency mistaken for soundness.** Grading a confident-sounding answer as solid when it dodges the substance. Grade on whether the attack actually lands, not on delivery.
5. **Self-grade inflation.** Marking shaky responses solid. If in doubt, grade down; the cost of overconfidence is being caught in the room.
6. **Gap denial.** Discovering a real weakness and rationalizing it as answerable. Concede or fix; don't paper over.
7. **Generic critic.** "People might object that…" with no specific adversary. Cast a concrete, credible critic with standing.
8. **No fix path.** Listing exposed gaps without a pre-ship remedy. Each gap needs a fix or an explicit accepted-risk note.

---

## Output Format

```
# Red team briefing — [position]

## Position (as I'll present it)
[The conclusion + the ask, in the audience's terms]

## The critic
- Who: [specific person / composite / archetype]
- Standing: [why their objection carries weight]

## The critic's strongest argument (steelmanned)
[Best version of the case against — the one that would worry me]

## The critic's strongest evidence
[Most damaging fact / precedent / data point, including the one I hope they don't raise]

## The most cutting question
"[The question I'd least want to be asked, in the critic's voice]"

## My responses (drafted and graded)
| Attack | My response | Grade (solid / partial / gap) | Fix before shipping |
|--------|-------------|-------------------------------|---------------------|
| Argument | [draft] | partial | [evidence to add] |
| Evidence | [draft] | solid   | n/a |
| Question | [draft] | gap     | [concession / scope narrowing] |

## Fix list
[Concrete pre-ship actions for every partial/gap]

## Ship decision
[Ship as is / ship after fixes / rework] — because [one line]
```

---

## Verification

- [ ] A specific, credible critic is named (not "someone").
- [ ] The critic's argument and evidence are steelmanned, not strawmanned.
- [ ] The single most cutting question is written in the critic's voice.
- [ ] Each attack has a drafted response and an honest self-grade.
- [ ] Partial/gap responses each have a concrete fix-before-shipping.
- [ ] Real weaknesses are conceded or fixed, not rationalized as answerable.
- [ ] The dreaded objection is included, not avoided.
- [ ] A ship decision is stated and justified.
