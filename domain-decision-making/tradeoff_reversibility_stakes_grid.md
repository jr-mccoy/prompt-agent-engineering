---
title: "Reversibility × Stakes Grid — Decision Sequencing by 2x2"
category: decision-making/tradeoffs
description: "Plot a decision (or set of decisions) on a 2x2 grid: reversibility (one-way / two-way door) × stakes (low / high). Each quadrant has a different rule for how much analysis to invest, who to involve, and how fast to move. Counters the most common decision pathology: applying high-analysis processes to two-way-door decisions and rushing one-way-door decisions."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - DS-01
  - CM-02
  - QA-01
difficulty: beginner
tags:
  - decision-making
  - reversibility
  - stakes
  - sequencing
  - meta-decision
updated: "2026-05-10"
reasoning:
  styles: [taxonomic, meta-decision]
  stakes: variable
  horizon: variable
  uncertainty: variable
  evidence_quality: variable
  domain_complexity: variable
  collaboration: solo_or_team
  output_format: 2x2_with_quadrant_rules
  user_role: [executive, founder, pm, individual, manager, operator]
  mode: [diagnose, decide, audit]
related_prompts:
  - domain-decision-making/decisioning_time_boxed_decision_protocol.md
  - domain-decision-making/tradeoff_multi_criteria_decision_analysis.md
  - domain-decision-making/decisioning_regret_minimization.md
---

# Reversibility × Stakes Grid

**Objective:** Plot a decision (or batch of decisions) on a 2x2 grid:
- **Reversibility:** *two-way door* (cheap to reverse) vs *one-way door* (costly or impossible to reverse)
- **Stakes:** *low* (small consequence either way) vs *high* (large consequence)

Each quadrant has a different rule for: how much analysis to invest, who to involve, how fast to move, what kind of buy-in to require, and what kind of follow-through to plan.

The deliverable is a meta-decision tool: it doesn't make decisions, it tells you *how* to make each decision. The most common decision pathology this prompt counters is applying heavyweight analysis to two-way-door decisions (slow + over-deliberated for no reason) while rushing one-way-door decisions ("we'll figure it out as we go").

**When to use:**
- Triaging a queue of pending decisions to figure out which need deep analysis and which can be made now.
- A team is over-processing small decisions and under-processing big ones.
- Planning a quarter / sprint and you have many decisions to make in sequence.
- Personal context: you're agonizing over a decision; the grid often reveals it's two-way-door and the agonizing is wasted.
- Coaching others to triage their own decision queue.

**When NOT to use:**
- A single decision you've already classified. Just make it.
- A decision whose reversibility or stakes are already obvious. The grid is for triage, not deliberation about a single known case.

**Audience:** Executives, founders, PMs, managers, operators, individuals — anyone with more than 1 decision pending and finite analysis bandwidth.

---

## Inputs / Context

1. **The decision(s).** A list of pending decisions. Each named in one sentence.
2. **For each decision:** the user's gut sense of stakes and reversibility (we'll refine).
3. **Decision-making bandwidth.** How much time / attention is available for analysis this period.
4. **Who can make each decision.** Decision rights matter — some decisions are yours, some require buy-in.

---

## Quadrant rules

| Quadrant | Reversibility | Stakes | Rule | Time budget | Process |
|----------|---------------|--------|------|-------------|---------|
| **A** | Two-way | Low | Just decide. Don't optimize. | Minutes | Solo, no review |
| **B** | Two-way | High | Run a small experiment; the experiment IS the decision. Reverse fast if the result is bad. | Hours-days | Solo or small group, time-boxed |
| **C** | One-way | Low | Pick a default and document. Re-examine only if the consequences look out of band. | Minutes | Solo with note |
| **D** | One-way | High | Slow down. Apply MCDA / deep analysis / multi-perspective review. Build buy-in. Plan tripwires. | Days-weeks | Multi-person, structured |

**The pathologies to counter:**
- **Pathology 1 (most common):** treating Quadrant A decisions like Quadrant D ones — agonizing over a reversible low-stakes choice. Cost: time and attention.
- **Pathology 2:** treating Quadrant D decisions like Quadrant A ones — rushing a one-way-door high-stakes choice. Cost: irreversible bad outcome.
- **Pathology 3:** classifying a Quadrant D decision as Quadrant B (assuming reversibility you don't actually have). Cost: discovering after the fact that you can't reverse it.

---

## Constraints

### Must
- For each decision, classify reversibility and stakes against **specific tests** (not gut), then place on the grid.
- For each quadrant, apply the corresponding process rule. Do not deviate without a stated reason.
- Test reversibility honestly: cost to reverse includes financial, reputational, relational, and opportunity cost. Many "reversible" decisions are reversible only on paper.
- Test stakes against the time horizon: a Quadrant A decision today might become Quadrant D over 5 years if it compounds.
- Surface decisions where the user's intuitive classification differs from the test-based classification.
- For Quadrant D decisions, verify that the user has accepted the time-and-process budget. If not, either downgrade the decision or upgrade the budget.

### Must Not
- Skip the reversibility / stakes test in favor of gut feel. The whole point is to override gut.
- Process every decision the same way. The quadrant rules exist precisely because uniform process is wasteful.
- Assume reversibility you don't have. Pre-test the reversal.
- Apply Quadrant D process to Quadrant A out of risk-aversion. The cost of over-process is real.
- Apply Quadrant A process to Quadrant D out of speed-bias. The cost of under-process can be unrecoverable.

---

## Reversibility test

A decision is **two-way door** if **all** of the following are true:
- Reversal cost is small relative to total stakes (rough rule: <10% of decision's total value).
- Reversal can be done within a reasonable time window.
- Reversal does not require permission from parties who might not grant it.
- No third parties have made dependent commitments that would be broken by reversal.

If any of these fails, the decision is **one-way door** for practical purposes.

## Stakes test

A decision is **high stakes** if **any** of the following are true:
- Outcome materially affects the user's / team's / company's / family's situation for >12 months.
- Outcome involves a sum of money / time / opportunity cost above a domain-specific threshold (e.g., >5% of annual budget; >1 month of work time).
- Outcome touches identity, relationships, or trust.
- Outcome creates path-dependence that locks in further decisions.

If none of these is true, the decision is **low stakes**.

---

## Instructions

### Step 1 — List pending decisions
For each: one-sentence statement, gut classification (which quadrant the user thinks it's in).

### Step 2 — Test reversibility per decision
Apply the reversibility test. Score binary (two-way / one-way). Note any factor that flipped a "two-way" intuition to "one-way" (or vice versa).

### Step 3 — Test stakes per decision
Apply the stakes test. Score binary (low / high). Note any factor that flipped intuition.

### Step 4 — Place on grid
| Decision | Reversibility | Stakes | Quadrant |
|----------|---------------|--------|----------|
| [name]   | one-way       | high   | D        |
| [name]   | two-way       | low    | A        |
| …        |               |        |          |

### Step 5 — Surface mis-classifications
Decisions where intuitive quadrant ≠ tested quadrant. These are the highest-leverage findings — they're where the user is currently wasting time or risking unrecoverable outcomes.

### Step 6 — Apply quadrant rules
For each decision, state:
- The applicable process (per quadrant rule)
- Time budget
- Who decides
- Reversal plan (for B and D especially)
- Tripwire / monitoring (for D especially)

### Step 7 — Sequence
Within the constraints of dependencies:
- Quadrant A decisions: make immediately, don't queue.
- Quadrant B decisions: schedule small experiments.
- Quadrant C decisions: pick default, document, move on.
- Quadrant D decisions: schedule structured analysis sessions; do not rush.

### Step 8 — Bandwidth check
Sum the time budgets across decisions. Compare to available bandwidth.
- If under-budget: good, proceed.
- If over-budget: either defer some Quadrant D decisions, downgrade some Quadrant D classifications (if defensible), or accept partial coverage.

### Step 9 — Audit
- Are any decisions in the user's "agonize" pile actually Quadrant A or B? If so, decide them now.
- Are any decisions being rushed that are actually Quadrant D? If so, slow down.

---

## False-Positive Prevention

1. **Reversibility theater.** Marking a decision two-way without testing reversal cost honestly. Apply the four-part test.
2. **Stakes inflation.** Marking small decisions high-stakes from anxiety. Apply the stakes test; if no criterion fires, it's low-stakes.
3. **Stakes deflation.** Marking actually-high-stakes decisions low to justify a quick choice. Adversarial check: would I judge this as low-stakes if a peer brought it to me?
4. **One-quadrant-fits-all.** Treating all decisions the same way ("all decisions deserve careful analysis" or "all decisions should be made fast"). Use the grid.
5. **Dependency blindness.** Some Quadrant A decisions are actually B or D once dependent decisions are factored in. Audit dependencies.
6. **Quadrant-D evasion.** Reclassifying Quadrant D decisions as Quadrant B because "we'll just reverse if it goes badly" — when reversal is, in fact, costly. Test reversal honestly.
7. **Over-process bias.** Risk-averse users default to Quadrant D for everything. Cost: bandwidth wasted on decisions that don't need it.
8. **Speed bias.** Action-oriented users default to Quadrant A for everything. Cost: occasional unrecoverable bad calls.

---

## Output Format

```
# Reversibility × Stakes grid — [decision queue]

## Decisions
| # | Decision (one sentence)         | Gut quadrant | Tested quadrant | Mis-class? |
|---|---------------------------------|--------------|-----------------|------------|
| 1 | [...]                           | D            | A               | yes        |
| 2 | [...]                           | A            | D               | yes        |
| 3 | [...]                           | B            | B               | no         |
| … |                                 |              |                 |            |

## Mis-classifications (highest leverage findings)
- Decision #1 felt like D but tests as A: [implication — stop agonizing, decide now]
- Decision #2 felt like A but tests as D: [implication — slow down, apply structured process]
- …

## Per-decision process
| # | Quadrant | Process              | Time budget | Decider | Reversal plan | Tripwires |
|---|----------|----------------------|-------------|---------|---------------|-----------|
| 1 | A        | Just decide          | minutes     | self    | n/a           | n/a       |
| 2 | D        | MCDA + multi-perspective + buy-in | days | named | full backout cost: $X, takes Y weeks | [tripwire] |
| 3 | B        | Small experiment     | days        | small group | revert via [path] | [signal] |
| … |          |                      |             |         |               |           |

## Sequencing
- Decide now (Quadrant A): [list]
- Pick default + document (C): [list]
- Schedule small experiment (B): [list, with experiment design pointer]
- Schedule deep analysis (D): [list, with session date]

## Bandwidth check
- Total time budget needed: [hours / days]
- Available bandwidth: [hours / days]
- Status: [under / over budget]
- Adjustments if over: [defer / downgrade / accept partial]

## Audit
- "Agonize" pile that should be Quadrant A or B: [list]
- "Rush" pile that should be Quadrant D: [list]
- Recommended next action: [the highest-leverage move from this audit]
```

---

## Verification

- [ ] Every decision tested for reversibility against the four-part test.
- [ ] Every decision tested for stakes against the criteria.
- [ ] Mis-classifications surfaced (intuition vs test).
- [ ] Per-decision process matched to quadrant rule.
- [ ] Reversal plan stated for Quadrants B and D.
- [ ] Tripwires stated for Quadrant D.
- [ ] Bandwidth check performed.
- [ ] Sequencing decisions specified.
- [ ] No reversibility-theater or stakes-inflation/deflation undetected.
- [ ] No one-quadrant-fits-all process applied uniformly.
