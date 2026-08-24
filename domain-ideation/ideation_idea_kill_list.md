---
title: "Idea Kill-List — Eliminate 80%, Defend the Survivors"
category: ideation/convergence
description: "An aggressive elimination round: given a long idea list, kill roughly 80% of it with a stated reason for each death, then defend the survivors. The discipline of killing — and naming exactly why each idea dies (unoriginal, infeasible, off-brief, a variant of another, or borrowed and not actually believed in) — forces a commitment that ranking does not. Ends with a small short-list, each survivor justified by the specific reason it survived."
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
  - convergence
  - elimination
  - kill-list
  - commitment
updated: "2026-05-27"
reasoning:
  styles: [convergent, evaluative, eliminative]
  stakes: moderate
  horizon: variable
  uncertainty: ambiguity
  evidence_quality: moderate
  domain_complexity: variable
  collaboration: solo_or_team
  output_format: structured
  user_role: [pm, founder, designer, strategist, individual]
  mode: [converge, decide]
related_prompts:
  - domain-ideation/ideation_idea_convergence_dot_voting.md
  - domain-ideation/ideation_forced_quantity_100_ideas.md
  - domain-decision-making/tradeoff_multi_criteria_decision_analysis.md
---

# Idea Kill-List — Eliminate 80%, Defend the Survivors

**Objective:** Narrow a long idea list by *killing* — deliberately eliminating roughly 80% of it, with a stated reason for each death — rather than by ranking. Killing and ranking feel similar but produce different discipline: ranking lets every idea survive in some diminished form ("we'll keep it in the backlog"), which is a way of avoiding commitment. Forcing a kill — and naming *exactly* why each idea dies — makes you confront which ideas you actually believe in. The reasons matter as much as the deaths: an idea killed for being unoriginal teaches something different from one killed for being infeasible or one killed because it's secretly someone else's idea you don't really believe. The output is a small short-list where every survivor is justified by the specific reason it earned its place.

**When to use:**
- A long idea list (post-divergence) needs hard narrowing and the team keeps everything "just in case."
- Commitment is the bottleneck — you have plenty of ideas and too little conviction.
- A backlog has bloated with ideas nobody actually believes in and needs a cull.
- As a sharper, more decisive companion to dot-voting when the group is conflict-averse.

**When NOT to use:**
- You're still diverging or the list is thin (≤7 ideas) — killing 80% of a small list leaves too little.
- The ideas need careful comparative scoring on multiple criteria — use `ideation_idea_convergence_dot_voting.md` or, for committed options, multi-criteria decision analysis.
- The stakes make irreversible elimination risky and you want a softer narrowing. (Kill-list is intentionally aggressive.)

**Audience:** PMs, founders, designers, and strategists who have too many ideas and too little conviction; individuals decluttering a personal idea backlog.

---

## Inputs / Context

1. **The idea list.** The full set, each idea stated clearly enough to judge.
2. **The brief / goal.** What the ideas are meant to serve — the standard against which "off-brief" is judged.
3. **Kill target.** Default ~80% eliminated (so ~20% survives). State the rough survivor count up front.
4. **Belief check.** Whether to apply the "do you actually believe in this?" filter — the most uncomfortable and most useful kill reason.
5. **Reversibility.** Whether killed ideas are archived (recoverable) or genuinely discarded — affects how aggressively to cut.

---

## Constraints

### Must
- **Kill roughly 80%.** State the target survivor count before starting so the round can't quietly keep everything.
- Give **every killed idea a stated reason**, drawn from a fixed taxonomy (below). No idea dies "just because."
- Apply the **belief filter** to ideas that survive on paper: "do I actually believe in this, or am I keeping it to be polite / because someone senior proposed it / because it sounds impressive?" Borrowed-conviction ideas get killed.
- **Defend each survivor** with the specific reason it lived — not "it's good" but "it's the only idea that serves [job X] and we believe we can ship it."
- Distinguish **kill** (gone) from **merge** (folded into a stronger idea — the kernel survives inside another) from **park** (explicitly archived with a revisit trigger). Most should be kill, not park — parking is how lists avoid commitment.
- Note any idea killed that you feel a **pang about** — the pang is a signal to double-check the kill reason, not to reverse it reflexively.

### Must Not
- Soften kills into parks to avoid the discomfort. If most of the list ends up "parked", the round failed — that's ranking in disguise.
- Kill without a reason from the taxonomy. Reasonless kills are gut calls that can't be examined.
- Spare an idea purely because of who proposed it. The belief filter exists precisely to kill politically-protected ideas.
- Keep multiple variants of the same idea — kill all but the strongest variant (or merge them) and say so.
- Treat survival as endorsement-to-build. Survivors advance to testing; the kill-list narrows, it doesn't launch.

---

## Kill-reason taxonomy

Every death cites one (occasionally two) of these:

| Reason | Kills ideas that… |
|--------|-------------------|
| **Unoriginal** | are obvious / already exist / everyone would propose them |
| **Infeasible** | can't be built within real constraints (time, budget, tech, legal) |
| **Off-brief** | don't actually serve the goal, however clever |
| **Variant** | are a weaker version of another idea on the list |
| **Borrowed conviction** | you're keeping out of politeness / status / fashion, not belief |
| **No champion** | nobody will actually carry it forward |
| **Untestable** | can't be validated cheaply enough to justify the bet |

---

## Instructions

### Step 1 — Set the target
Restate the brief. State the survivor count (~20% of the list). Confirm whether killed ideas are archived or discarded.

### Step 2 — First pass: obvious kills
Sweep the list and kill the clear non-starters — unoriginal, infeasible, off-brief — citing the reason for each. This usually removes 40–50% fast.

### Step 3 — Variant collapse
Group near-duplicates. Keep the strongest of each group; kill the rest as **variant**, or **merge** weaker ones whose kernel improves the survivor. Say which.

### Step 4 — Belief filter
On the remaining ideas, apply the uncomfortable question: do you actually believe in this? Kill the borrowed-conviction and no-champion ideas, naming why each was really being kept.

### Step 5 — Check the kill rate
Count survivors. If far more than the target survive, you've been soft — run the belief filter again, harder. If far fewer survive, confirm you didn't over-cut a genuinely strong idea.

### Step 6 — Defend the survivors
For each survivor, write the specific reason it lived: which part of the brief it uniquely serves, why you believe in it, and what makes it worth the next step. A survivor you can't defend specifically is a kill you missed.

### Step 7 — Pang audit
List any kill you feel a pang about. For each, re-read the kill reason. If the reason holds, the kill stands; if the pang exposes a real flaw in the reasoning, revise — but don't reverse kills just to feel better.

### Step 8 — Hand off
Survivors advance to a test or prototype, or to `ideation_idea_convergence_dot_voting.md` if further scoring is needed. Note the parked ideas (if any) with their revisit triggers.

---

## False-Positive Prevention

1. **Park-as-escape.** Converting kills to "parked for later" so nothing actually dies. That's ranking wearing a kill-list costume. Most of the list should be genuinely killed.
2. **Reasonless kills.** Killing on vibe ("nah") forfeits the learning. Every death cites a taxonomy reason that can be examined.
3. **Political protection.** Sparing the CEO's idea regardless of merit corrupts the round. The belief filter targets exactly these.
4. **Variant hoarding.** Keeping six flavors of the same idea is keeping one idea six times. Collapse to the strongest or merge.
5. **Borrowed conviction.** The subtlest survivor is the impressive-sounding idea nobody actually believes. If you can't say why *you* believe it, kill it.
6. **Pang-driven reversal.** Reviving a killed idea because it feels sad to lose it re-bloats the list. Re-examine the reason; reverse only if the reasoning was flawed.
7. **Indefensible survivors.** A survivor you can only defend with "it's good" is under-examined. Specific defense or it's a missed kill.
8. **Survival-as-greenlight.** Treating survivors as approved-to-build skips testing. The kill-list narrows; it doesn't authorize a launch.

---

## Output Format

```
# Idea kill-list — [brief]

## Setup
> Brief / goal: [...]
- Starting count: [N] | Target survivors: ~[20%] = [M]
- Killed ideas: [archived / discarded]

## The kills
| # | Idea (short) | Kill reason | Note (e.g., merged into #, variant of #) |
|---|--------------|-------------|-------------------------------------------|
| 1 | [...] | unoriginal | — |
| 2 | [...] | variant | merged kernel into #14 |
| 3 | [...] | borrowed conviction | kept out of politeness; nobody believes it |
| 4 | [...] | infeasible | violates [constraint] |
| … | | | |

## Kill-rate check
- Survivors after passes: [count] (target [M])
- Soft? ran belief filter again: [yes/no]

## Survivors (defended)
| Idea | Why it lived (specific) | What it uniquely serves | Next step |
|------|--------------------------|--------------------------|-----------|
| [...] | [belief + uniqueness] | [job/brief element] | [test] |
| … | | | |

## Pang audit
- Kills I felt a pang about: [#s] — reason re-checked: [holds / revised]

## Parked (if any — keep minimal)
- [idea] — revisit trigger: [specific condition]

- Survivors advance to: test/prototype, or ideation_idea_convergence_dot_voting.md for scoring.
```

---

## Verification

- [ ] Target survivor count (~20%) stated before the round.
- [ ] ~80% of the list actually killed (not parked).
- [ ] Every kill cites a reason from the taxonomy.
- [ ] Variants collapsed to the strongest (or merged), with notes.
- [ ] Belief filter applied; borrowed-conviction and no-champion ideas killed.
- [ ] Kill-rate checked; belief filter re-run if too soft.
- [ ] Each survivor defended with a specific, non-generic reason.
- [ ] Pang audit done; reversals only on flawed reasoning, not feeling.
- [ ] Parked ideas (if any) kept minimal, each with a revisit trigger.
- [ ] Survivors framed as advancing to test, not greenlit to build.
