---
title: "Policy Stakeholder & Coalition Map — Positions, Blockers, and Swing Actors"
category: policy/stakeholder-analysis
description: "Map every stakeholder around a policy proposal on position, intensity, influence, true interests, coalition affiliation, and movability — then derive the structures that determine outcomes: coalitions (who moves together), blockers (high influence + opposed), and swing actors (low intensity + medium-to-high influence, where coalition-building leverage actually lives). Counters the failure of counting headcount instead of weighing power and persuadability."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - DS-01
  - CM-02
  - QA-01
difficulty: advanced
tags:
  - policy
  - stakeholder-mapping
  - coalition-building
  - power-analysis
  - advocacy
updated: "2026-06-18"
reasoning:
  styles: [analytic, structural, strategic, game_theoretic]
  stakes: high
  horizon: months
  uncertainty: ambiguity
  evidence_quality: moderate
  domain_complexity: politically_charged
  collaboration: small_team
  output_format: [matrix, structured]
  user_role: [policy, advocate, executive, analyst]
  mode: [diagnose, synthesize, plan]
related_prompts:
  - domain-policy/policy_problem_framing.md
  - domain-policy/policy_options_memo.md
  - domain-policy/policy_implementation_feasibility.md
---

# Policy Stakeholder & Coalition Map

**Objective:** Produce a stakeholder grid and a coalition strategy for a policy proposal. The grid characterizes each stakeholder on position, intensity, influence, true interests, coalition affiliation, and movability. The strategy reads the structure off the grid: which actors move together (coalitions), which can stop the proposal (blockers), and which are persuadable and powerful enough to matter (swing actors). The point is to move from "who is for and against" — a headcount — to "where does leverage live" — a power and persuadability analysis.

**When to use:**
- A policy proposal is real enough to have supporters and opponents, and you need a strategy to advance or defeat it.
- Building an advocacy or government-affairs campaign plan.
- Diagnosing why a proposal is stuck despite apparent majority support (usually a blocker problem).
- Before a negotiation, hearing, board vote, or coalition launch.

**When NOT to use:**
- The problem is not yet framed — run `policy_problem_framing.md` first; stakeholder positions depend on the frame.
- There is genuinely one decision-maker and no coalition dynamics — a simpler influence note suffices.
- You need implementation feasibility, not political feasibility — use `policy_implementation_feasibility.md`.

**Audience:** Advocates, lobbyists, government affairs and public affairs leads, campaign managers, coalition organizers, and policy strategists.

---

## Inputs / Context

1. **The proposal.** Specific enough that an actor can be for or against it.
2. **The decision arena.** Legislature, agency, ballot, board, court — and the decision rule (majority, supermajority, single decider, consensus).
3. **The stakeholder universe.** Every actor with a stake: organized interests, agencies, elected officials, firms, unions, advocacy groups, affected publics, media, funders.
4. **What is known about each.** Public statements, past votes, financial interests, constituencies, relationships.
5. **Your position and assets.** What you can offer (money, votes, cover, information, relationships, public pressure).

---

## Constraints

### Must
- Score every stakeholder on all six dimensions: **position, intensity, influence, interests, coalition affiliation, movability.**
- Distinguish **stated position** from **true interest** — what they say versus what they actually want. These diverge constantly and the gap is where deals live.
- Rate **intensity** (mild / strong / decisive) separately from **position** — a mild supporter and a decisive supporter are not interchangeable.
- Rate **influence** (low / medium / high) in *this specific arena*, not generic prominence.
- Identify **coalitions** as groups that move together, with the glue holding them (shared interest, leadership, money, identity).
- Identify **blockers**: high influence + opposed. These set the difficulty of the whole effort.
- Identify **swing actors**: low-to-mild intensity + medium-to-high influence. This is where persuasion has the highest marginal return.
- For each movable actor, specify **who can move them and with what** — not "they could be persuaded" but the lever and the messenger.

### Must Not
- Equate number of supporters with likelihood of passage. One high-influence decisive blocker can beat a hundred mild supporters.
- Take stated positions at face value when interests suggest otherwise.
- Rate influence as generic reputation rather than power in this arena under this decision rule.
- Treat "neutral" and "unaware" as the same — unaware actors can be activated by either side.
- Plan to convert decisive opponents while ignoring persuadable swing actors. Spend effort where movability is highest.
- Omit your own coalition's internal fractures. Allies have divergent interests too.

---

## Instructions

1. **Enumerate the stakeholder universe.** List every actor with a stake, including those currently unaware. Group obvious clusters but keep individual decision-makers distinct.
2. **Score position and intensity.** For each: position (support / oppose / neutral / unaware) and intensity (mild / strong / decisive). A decisive opponent will spend to defeat this; a mild one will not lift a finger.
3. **Score influence in this arena.** Rate low / medium / high based on power *in this decision* — votes, veto points, money, mobilization, agenda control, expertise the decider relies on. A senator is high in a legislature, low in an agency rulemaking.
4. **Surface true interests behind stated positions.** For each, write what they actually want — re-election, market protection, budget, mission, reputation, avoiding blame. Note where stated position and interest diverge; that gap is negotiable space.
5. **Map coalition affiliations.** Identify groups that move together and name the glue. Note actors who bridge coalitions and actors whose membership is soft.
6. **Identify blockers.** Cross influence with position: high influence + opposed = blocker. For each blocker, state what would neutralize, delay, or co-opt them, and whether that is feasible.
7. **Identify swing actors.** Cross intensity with influence: low/mild intensity + medium/high influence = swing. These move cheaply and matter. Rank them by leverage (influence × movability).
8. **Specify movement plans for movable actors.** For each swing actor and each soft opponent: who is the credible messenger to them, what is the lever (interest-based offer, information, public pressure, relationship), and what is the realistic delta (oppose→neutral, neutral→support).
9. **Derive the coalition strategy.** State the path to the needed decision threshold: which coalition to build, which swing actors to win in what order, which blockers to neutralize or route around, and what your assets buy. Include the opponent's likely counter-strategy.

---

## False-Positive Prevention

1. **Headcount illusion.** Counting supporters and declaring victory. Weight by influence and intensity; a map without power weighting is just a poll.
2. **Stated-position trap.** Recording what actors say and stopping there. Always write the true interest; the divergence is the strategy.
3. **Generic-influence error.** Rating influence by fame rather than power in this arena under this decision rule. A media figure may be high-influence on public opinion and zero-influence on a committee vote.
4. **Intensity blindness.** Treating all supporters or all opponents as equal. A mild supporter is nearly free; a decisive opponent is expensive.
5. **Swing-actor neglect.** Pouring effort into converting decisive opponents (low movability) while ignoring persuadable, powerful swing actors (high marginal return).
6. **Coalition reification.** Treating a coalition as monolithic when its glue is weak. Note which memberships are soft and could defect.
7. **Vague movability.** "Could be persuaded" with no messenger and no lever. Movability must name who and with what.
8. **Friendly-fire omission.** Ignoring fractures inside your own coalition. Allies defect over interest divergence; map them too.
9. **Static snapshot.** Treating the map as fixed when positions shift with events. Note which scores are volatile and what would move them.
10. **Opponent passivity assumption.** Planning your moves while assuming opponents stand still. Include their counter-strategy.

---

## Output Format

```
# STAKEHOLDER & COALITION MAP — [proposal]
Arena: [...] | Decision rule: [majority / supermajority / single decider / consensus]
Threshold to win: [e.g., 5 of 9 votes; agency head sign-off]

## Stakeholder grid
| Stakeholder | Position | Intensity | Influence (this arena) | Stated position | True interest | Coalition | Movability (who/lever) |
|-------------|----------|-----------|------------------------|-----------------|---------------|-----------|------------------------|
| [...]       | oppose   | decisive  | high                   | "[...]"         | [...]         | [...]     | low — [...]            |
| [...]       | neutral  | mild      | medium                 | "[...]"         | [...]         | [...]     | high — [messenger / lever] |

## Coalitions
| Coalition | Members | Glue | Soft members (defection risk) |
|-----------|---------|------|-------------------------------|
| [...]     | [...]   | [...]| [...]                         |

## Blockers (high influence + opposed)
| Blocker | Influence | Why opposed (interest) | Neutralize / delay / co-opt? | Feasible? |
|---------|-----------|------------------------|------------------------------|-----------|
| [...]   | high      | [...]                  | [...]                        | [y/n]     |

## Swing actors (low/mild intensity + medium/high influence)
Ranked by leverage (influence × movability):
| Swing actor | Influence | Movability | Messenger | Lever | Realistic delta |
|-------------|-----------|------------|-----------|-------|-----------------|
| [...]       | high      | high       | [...]     | [...] | neutral→support |

## Coalition strategy
- Path to threshold: [...]
- Coalition to build: [...]
- Swing actors to win, in order: [...]
- Blockers to neutralize or route around: [...]
- Assets to deploy and on whom: [...]
- Opponent's likely counter-strategy: [...]
- Earliest tripwire that the map is wrong: [...]
```

---

## Verification

- [ ] Every stakeholder scored on all six dimensions.
- [ ] Stated position distinguished from true interest for each.
- [ ] Intensity rated separately from position.
- [ ] Influence rated for this specific arena and decision rule.
- [ ] Coalitions named with their glue and soft members.
- [ ] Blockers identified with neutralization assessment.
- [ ] Swing actors identified and ranked by leverage.
- [ ] Movability specifies messenger and lever, not just "persuadable."
- [ ] Coalition strategy reaches the stated decision threshold.
- [ ] Own-coalition fractures included.
- [ ] Opponent counter-strategy included.
- [ ] No headcount-as-outcome reasoning.
