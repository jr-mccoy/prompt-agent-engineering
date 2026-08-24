---
title: "Policy Options Memo — Compare 3–5 Policy Options on Feasibility, Cost, Equity, and Political Viability"
category: policy/options-analysis
description: "Structure a policy options memo that compares 3–5 distinct policy options against a defined problem. Each option is evaluated on effectiveness, implementation feasibility, fiscal cost, equity / distributional effects, political viability, reversibility, and unintended consequences. Includes a recommendation with explicit naming of the values tradeoffs the recommendation rests on."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - DS-01
  - DS-02
  - CM-02
  - QA-01
difficulty: advanced
tags:
  - policy
  - options-memo
  - public-policy
  - implementation
  - equity
updated: "2026-05-10"
reasoning:
  styles: [analytic, comparative, normative, structural]
  stakes: high
  horizon: years
  uncertainty: deep
  evidence_quality: variable
  domain_complexity: regulated
  collaboration: team
  output_format: structured_policy_memo
  user_role: [policy, executive, analyst, consultant, advocate]
  mode: [synthesize, document, decide]
related_prompts:
  - domain-decision-making/documentation/decisiondoc_options_memo.md
  - domain-reasoning-craft/systems/systems_unintended_consequence_scan.md
  - domain-reasoning-craft/epistemic/epistemic_disagreement_diagnosis.md
---

# Policy Options Memo

**Objective:** Produce a structured policy options memo that compares 3–5 distinct policy options against a defined policy problem. Each option is evaluated on effectiveness, implementation feasibility, fiscal cost, equity / distributional effects, political viability, reversibility, and unintended consequences. The memo ends with a recommendation that names the values tradeoffs the recommendation rests on — because policy choices are rarely empirically determined and pretending they are is the most common failure mode of policy memos.

This is a documentation prompt. The deliberation should already be done (research, modeling, stakeholder input); the memo communicates the analysis in a form that supports decision by a principal who wasn't in the working sessions.

**When to use:**
- Government, foundation, NGO, or corporate-government-affairs context where a principal needs to choose among policy responses to a problem.
- Internal recommendation to a board, leadership, or coalition partner on which policy posture to advocate.
- Academic or think-tank analysis comparing options for an external audience.
- Personal-civic context: organizing one's own thinking on a policy debate.

**When NOT to use:**
- The recommendation is binary (do / don't do something) — use a simpler decision memo.
- The "policy" is internal operations rather than public policy. Use `decisiondoc_options_memo.md`.
- Persuasion is the goal rather than auditable analysis. Use a different format.

**Audience:** Policy analysts, executives, consultants, advocates, civic-minded individuals — anyone who needs to communicate "here are the options, here is what each implies, and here is what the choice depends on."

---

## Inputs / Context

1. **The policy problem.** Sharply stated: what is the problem, who is affected, what is the magnitude, what is the trajectory if nothing changes.
2. **Scope.** Jurisdictional, temporal, sectoral.
3. **Audience for the memo.** Which principal or body is choosing.
4. **Constraints.** Legal, constitutional, fiscal, political, administrative.
5. **Existing options on the table.** Including any current policy and any "do nothing" option.
6. **Available evidence.** Research, modeling, comparable jurisdiction experience, stakeholder input.
7. **Values context.** What the principal or constituency cares about (the values that will shape the recommendation).

---

## Memo structure (mandatory sections)

1. **Executive summary** — recommendation up top
2. **Problem definition** — what, who, magnitude, trajectory
3. **Goals and criteria** — what success looks like
4. **Options considered** — 3–5 distinct policy options
5. **Comparison** — option × criteria matrix
6. **Per-option deep-dive** — each option analyzed
7. **Recommendation** — with reasoning and values acknowledgment
8. **Implementation considerations** — what would need to happen for the recommended option to work
9. **Risks and mitigations** — including unintended consequences
10. **Stakeholder reactions** — anticipated by group
11. **Reversibility and tripwires** — how the policy could be revisited
12. **Equity / distributional analysis** — who wins, who loses
13. **Decision needed by** — date and principal

---

## Constraints

### Must
- Define the **problem** sharply and separately from the options. Many policy memos mistake "X policy is needed" for the problem statement.
- Include a **status-quo option** ("no change") with full analysis. The status quo is a policy choice, not a non-choice.
- Generate **distinct** policy options — not three flavors of the same option. Distinct on mechanism, not just degree.
- Apply consistent criteria across all options. Standard set:
  - **Effectiveness:** how well does this address the problem
  - **Implementation feasibility:** can this actually be operated
  - **Fiscal cost:** to government, to private actors, to consumers
  - **Equity / distributional effects:** who benefits, who bears costs
  - **Political viability:** can this be passed and maintained
  - **Reversibility:** how hard to undo if it goes wrong
  - **Unintended consequences:** behavioral, structural, second-order
- For the recommendation, name the **values tradeoffs** explicitly: "this option prioritizes X over Y; an analyst with different values would land elsewhere because…"
- Distinguish **empirical claims** (resolvable by evidence) from **normative claims** (about what should be valued). Don't smuggle one inside the other.
- Surface **stakeholder reactions** by group, including likely opposition.

### Must Not
- Present one option as the "real" choice and others as straw alternatives.
- Skip the status-quo option.
- Pretend the values choice is determined by evidence. Evidence shapes; values choose.
- Use technocratic language to obscure the distributional question. "Net welfare improvement" hides who pays.
- Hide political feasibility issues. They're part of the analysis.
- Treat unintended consequences as a footnote. They are often the load-bearing risk.

---

## Instructions

### Step 1 — Problem definition
- One paragraph: the problem in plain language
- Magnitude: how big, how many affected, by what measure
- Trajectory: what happens under current policy / no intervention
- What evidence supports the problem characterization
- What's contested about the problem characterization

### Step 2 — Goals and criteria
- What outcomes a successful policy would produce
- How those outcomes will be measured
- Standard policy criteria (effectiveness, feasibility, cost, equity, political viability, reversibility, unintended consequences)
- Any criteria specific to this problem (e.g., constitutional limits, treaty obligations)

### Step 3 — Options considered
3–5 distinct options including status quo. For each:
- **Name and one-line description**
- **Mechanism:** how the policy works
- **Who acts:** government, regulated entity, beneficiary, third party
- **Lever:** mandate, tax, subsidy, information, infrastructure, default rule, voluntary

Options should be mechanism-distinct. Three different funding levels of the same program are not three options; they're three calibrations of one option (combine).

### Step 4 — Per-option analysis
For each option, address each criterion:

#### Effectiveness
- What does the evidence say about how well this works (in this jurisdiction, in comparable jurisdictions, in modeling)?
- What's the central estimate, what's the uncertainty band?
- What conditions would have to hold for it to work as expected?

#### Implementation feasibility
- What administrative capacity is needed?
- What is the implementation timeline?
- What dependencies exist (legislation, regulation, funding, agency capacity)?
- What's the failure rate of similar implementation efforts?

#### Fiscal cost
- Direct cost to government (annual + cumulative)
- Indirect cost (administrative burden on regulated entities, compliance cost)
- Pass-through cost to consumers / taxpayers
- Cost over time — front-loaded, ongoing, declining?

#### Equity / distributional effects
- Who benefits (by demographic, geography, sector, income, etc.)
- Who bears costs
- Net distribution: progressive / flat / regressive
- Any specific population disproportionately affected (positively or negatively)

#### Political viability
- Likely supporting coalition
- Likely opposition
- Procedural path (legislation, rule, order, ballot)
- Sustainability across changes in administration

#### Reversibility
- How easily can the policy be modified or reversed
- What dependencies build up that make reversal harder over time
- Sunset provisions

#### Unintended consequences
- Behavioral responses likely from each affected actor
- Gaming / Goodhart concerns
- Second-order effects on adjacent systems
- Spillovers (positive or negative)

### Step 5 — Comparison matrix
Summarize per-option scores in a single matrix. Use qualitative ratings (strong / moderate / weak / negative) rather than false-precision numbers.

### Step 6 — Recommendation
- Recommended option
- Reasoning: which criteria favored it, which it lost on
- **Values tradeoffs explicit:** "This recommendation prioritizes [value X] over [value Y]. An analyst prioritizing differently would recommend [alternative]."
- Confidence: high / medium / low

### Step 7 — Implementation considerations
For the recommended option:
- Sequencing
- Capacity-building required
- Stakeholder engagement plan
- Pilots vs full launch
- Monitoring and evaluation plan

### Step 8 — Risks and mitigations
For the recommended option:
- Top risks (effectiveness, implementation, political, fiscal, unintended)
- Mitigations
- Risks that cannot be mitigated and must be accepted

### Step 9 — Stakeholder reactions
By group:
- Likely supporters and why
- Likely opponents and why
- Key swing actors
- Coalition required to advance

### Step 10 — Reversibility and tripwires
- How would we know the policy is failing?
- What are the off-ramps?
- Sunset / review schedule
- Re-opening conditions

### Step 11 — Equity / distributional summary
A standalone section because distributional effects are often the buried lead.

### Step 12 — Decision needed
- Principal
- Decision deadline
- What additional input would meaningfully improve the analysis

---

## False-Positive Prevention

1. **Problem-as-solution.** Stating the problem as "we need policy X" rather than "this problem exists." The problem is empirical; the solution is contested.
2. **Status-quo invisibility.** Failing to include "do nothing" as a serious option. Doing nothing is a policy choice with effects.
3. **False-distinct options.** Three flavors of the same option presented as alternatives. Distinguish by mechanism.
4. **Technocratic equity hiding.** "Net welfare gain" without distributional breakdown obscures who pays.
5. **Values-as-evidence.** Pretending the recommendation falls out of the analysis when it actually depends on a values choice. Name the values.
6. **Political-feasibility omission.** A great policy that cannot pass is not a great option for a memo. Either include feasibility or label the analysis "ignoring political constraints" explicitly.
7. **Unintended-consequences footnoting.** Treating unintended effects as a small disclaimer when they're often the load-bearing risk.
8. **Stakeholder silence.** Not surfacing likely opposition. The opposition will speak; better to know what they'll say in advance.
9. **Reversibility optimism.** "We can adjust as we go" — most policies build constituencies that resist adjustment. Test reversibility honestly.
10. **Single-jurisdiction tunneling.** Ignoring evidence from comparable jurisdictions because it's politically inconvenient.

---

## Output Format

```
# POLICY OPTIONS MEMO — [problem / topic]

## Executive summary
**Recommendation:** [option]
**For:** [principal / body]
**By:** [date]
**Top reasoning:** [1–2 sentences]
**Top risk:** [1 sentence]
**Values tradeoff this rests on:** [1 sentence]

## Problem definition
[Sharply stated, with magnitude, trajectory, evidence base, contested elements]

## Goals and criteria
- Outcomes a successful policy produces: [list]
- Measurement: [how we'd know it worked]
- Criteria applied: effectiveness | feasibility | cost | equity | political viability | reversibility | unintended consequences

## Options considered

### Option 1: Status quo
- Mechanism: [...]
- Who acts: [...]

### Option 2: [name]
- Mechanism: [...]
- Lever: [mandate / tax / subsidy / etc.]

### Option 3: [name]
[...]

### Option 4 (optional): [name]
### Option 5 (optional): [name]

## Per-option analysis

### Option 1 — Status quo
- Effectiveness: [...]
- Implementation feasibility: [...]
- Fiscal cost: [...]
- Equity: [...]
- Political viability: [...]
- Reversibility: [...]
- Unintended consequences: [...]

### Option 2 — [name]
[Same structure]

### Option 3 — …

## Comparison matrix
| Criterion        | Status quo | Option 2 | Option 3 | Option 4 |
|------------------|------------|----------|----------|----------|
| Effectiveness    | weak       | strong   | moderate | strong   |
| Feasibility      | n/a        | strong   | moderate | weak     |
| Fiscal cost      | low        | high     | medium   | high     |
| Equity           | regressive | progressive | mixed | progressive |
| Political viability | n/a    | strong   | weak     | moderate |
| Reversibility    | n/a        | moderate | strong   | weak     |
| Unintended consequences | low | medium  | low      | high     |

## Recommendation
- **Recommended:** Option [N]
- Reasoning: [paragraph naming which criteria favored it and which it lost on]
- **Values tradeoff:** "This recommendation prioritizes [X] over [Y]. An analyst prioritizing [Y] would recommend Option [M]."
- Confidence: [high / medium / low]

## Implementation considerations
- Sequencing: [...]
- Capacity: [...]
- Stakeholder engagement: [...]
- Pilots vs full launch: [...]
- M&E plan: [...]

## Risks and mitigations
| Risk | Likelihood | Impact | Mitigation | Owner |
|------|------------|--------|------------|-------|
| [...]| medium     | high   | [...]      | [name]|
| …    |            |        |            |       |

- Risks that cannot be mitigated and must be accepted: [list]

## Stakeholder reactions
- Likely supporters: [groups, why]
- Likely opponents: [groups, why]
- Swing actors: [groups]
- Coalition required: [...]

## Reversibility and tripwires
- Failure signals: [...]
- Off-ramps: [...]
- Sunset / review: [date]
- Re-opening conditions: [...]

## Equity / distributional summary
- Beneficiaries: [...]
- Cost-bearers: [...]
- Net distribution: [progressive / flat / regressive]
- Special populations: [disproportionate effects]

## Decision needed
- Principal: [name / body]
- Deadline: [date]
- Additional input that would improve the analysis: [...]
```

---

## Verification

- [ ] Problem stated empirically, separate from options.
- [ ] Status-quo option included with full analysis.
- [ ] 3–5 mechanism-distinct options.
- [ ] All seven criteria applied to all options.
- [ ] Values tradeoff named in recommendation.
- [ ] Distributional / equity analysis is a standalone section, not buried.
- [ ] Stakeholder reactions surfaced by group.
- [ ] Reversibility and tripwires specified.
- [ ] Implementation considerations realistic.
- [ ] Risks explicit; non-mitigable risks named.
- [ ] No problem-as-solution framing.
- [ ] No values-as-evidence smuggling.
- [ ] Decision principal and deadline named.
