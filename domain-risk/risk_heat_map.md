---
title: "Risk Heat Map — Plot, Rank, and Force the Top-3 Question"
category: risk/visualization
description: "Plot a set of risks on a likelihood × impact heat map, force-rank them by composite score, and surface the top-N with a one-line 'what we'd do today if it triggered.' Companion to the risk register: once risks exist with scores, this prompt visualizes and sorts them, then forces the operational question — are we actually doing the top-3 mitigations right now?"
techniques:
  - ST-01
  - ST-02
  - RT-02
  - DS-01
  - CM-02
  - QA-01
difficulty: beginner
tags:
  - risk-management
  - heat-map
  - prioritization
  - likelihood-impact
  - ranking
updated: "2026-05-10"
reasoning:
  styles: [probabilistic, structural, prioritization]
  stakes: variable
  horizon: weeks
  uncertainty: risk
  evidence_quality: moderate
  domain_complexity: cross_domain
  collaboration: small_team
  output_format: matrix_ranked_list
  user_role: [pm, operator, executive, founder, analyst]
  mode: [synthesize, audit, decide]
related_prompts:
  - domain-risk/risk_register_builder.md
  - domain-risk/risk_fmea_analysis.md
  - domain-decision-making/scenario_two_by_two_matrix.md
---

# Risk Heat Map

**Objective:** Take a set of scored risks — ideally from a risk register — and (1) plot them on a 5×5 likelihood × impact heat map rendered in text, (2) force-rank them by composite score, and (3) surface the top-N (typically top 10) with a one-line "what we'd do today if it triggered." The map exists to drive one question to the surface: **are we actually executing the top-3 mitigations right now, or just admiring the chart?** Visualization without that forcing question is decoration.

**When to use:**
- A risk register exists (or a scored risk list does) and needs to be visualized and prioritized.
- Communicating risk posture to stakeholders who need to see concentration at a glance.
- A periodic risk review where you want to re-rank and check whether the top mitigations are actually in motion.
- Deciding where to spend limited mitigation attention this cycle.

**When NOT to use:**
- No scored risks exist yet — build the register first with `risk_register_builder.md`.
- You need per-step failure decomposition with detectability — use `risk_fmea_analysis.md`.
- You're hunting for risks not yet on any list — use `risk_tail_risk_scan.md`.
- Strategic two-uncertainty scenario framing — use `scenario_two_by_two_matrix.md`.

**Audience:** Project managers, operators, founders, executives, and analysts who have a risk list and need to prioritize attention and communicate concentration.

---

## Inputs / Context

1. **The risk set.** A list of risks with likelihood (1–5) and impact (1–5) scores. If they come from `risk_register_builder.md`, reuse those scores. If unscored, score them on the anchored scales below first.
2. **Mitigation status (if known).** For each risk, whether a mitigation is already in motion, planned, or absent. This drives the "are we actually doing it?" check.
3. **Top-N preference.** How many top risks to detail (default 10).
4. **Audience for the map.** Whether this is an internal working artifact or a stakeholder communication — affects how much narrative accompanies the chart.

---

## Constraints

### Must
- Render a **5×5 grid** in text with impact on one axis and likelihood on the other, and place each risk by its ID in the correct cell.
- Use **composite = likelihood × impact** for ranking, and break ties by impact (impact-dominant tie-break — a 5×3 outranks a 3×5).
- Produce a **force-ranked list** of all risks by composite, highest first.
- Detail the **top-N** with a one-line **"what we'd do today if it triggered"** — an immediate action, not a long-term mitigation.
- Run the **top-3 execution check**: for each of the top 3, state plainly whether its mitigation is in motion, planned, or absent.
- Use a consistent **zone convention** (red / amber / green or high / medium / low) tied to composite thresholds, and state the thresholds explicitly.

### Must Not
- Re-score risks differently than the register did without flagging the change — the map must stay consistent with its source.
- Rank by impact alone or likelihood alone; composite drives the order.
- Let the top-3 execution check pass silently when a mitigation is absent — name the gap.
- Produce the chart and stop; the ranked list and the execution check are the point.
- Crowd the visual so it's unreadable — if two risks share a cell, list both IDs in that cell.

---

## Instructions

### Step 1 — Confirm or assign scores
If the risks arrive scored (from the register), reuse the scores. If unscored, apply the anchored scales:
- **Likelihood (1–5):** 1 rare (<10%), 2 unlikely (~10–30%), 3 possible (~30–55%), 4 likely (~55–80%), 5 almost certain (>80%).
- **Impact (1–5):** 1 negligible, 2 minor, 3 moderate, 4 major, 5 severe.

### Step 2 — Compute composites and set zone thresholds
Composite = likelihood × impact (1–25). Set zones, e.g.:
- **Red (high):** composite ≥ 15
- **Amber (medium):** composite 8–14
- **Green (low):** composite ≤ 7

State the thresholds explicitly so the map is reproducible.

### Step 3 — Plot the 5×5 heat map
Place each risk ID in the cell for its (likelihood, impact) pair. Impact increases left→right; likelihood increases bottom→top (so the top-right is the hottest corner). If multiple risks share a cell, list all their IDs there.

### Step 4 — Force-rank by composite
List every risk highest composite first. Break ties by impact (impact-dominant). Show composite, likelihood, impact, and zone for each.

### Step 5 — Detail the top-N
For the top-N (default 10), write a one-line **"what we'd do today if it triggered"** — the immediate response, distinct from the long-term mitigation. This is the 3 a.m. action, not the roadmap item.

### Step 6 — Run the top-3 execution check
For each of the top 3 risks, state whether the mitigation is **in motion / planned / absent**. If absent or merely planned for a red-zone risk, flag it as the headline finding. The map's job is to convert "we know about it" into "we are doing something about it."

### Step 7 — Summarize concentration and the gap
Where the risks cluster (which zone is crowded), the single hottest risk, and the most important unaddressed top risk.

---

## False-Positive Prevention

1. **Chart-as-conclusion.** Producing a pretty grid and stopping. The ranked list and the top-3 execution check are the deliverable; the chart is the index.
2. **Single-dimension ranking.** Ordering by impact or likelihood alone. A 5×1 is not a 5×5. Composite drives the order, impact breaks ties.
3. **Silent absence.** A red-zone risk with no mitigation passing without comment. The execution check must name it loudly.
4. **Score drift.** Quietly re-scoring a risk so it lands in a calmer cell. If a score changes from the source, flag and justify it.
5. **Today vs someday confusion.** Writing the long-term mitigation in the "what we'd do today if it triggered" slot. That line is the immediate response under fire.
6. **Cell collision hiding.** Dropping one of two risks that share a cell. List both IDs; the crowding is information.
7. **Threshold ambiguity.** Coloring zones without stating the composite cutoffs. State them so the map is reproducible next cycle.

---

## Output Format

```
# Risk heat map — [scope]

## Zone thresholds
- Red (high): composite ≥ [X]
- Amber (medium): composite [Y]–[Z]
- Green (low): composite ≤ [W]

## Heat map (impact →, likelihood ↑)
              Impact 1   Impact 2   Impact 3   Impact 4   Impact 5
Likelihood 5 [        ] [        ] [        ] [   R3   ] [ R1,R7 ]
Likelihood 4 [        ] [        ] [   R9   ] [   R2   ] [   R4  ]
Likelihood 3 [        ] [   R11  ] [        ] [   R5   ] [   R8  ]
Likelihood 2 [        ] [        ] [   R10  ] [        ] [   R6  ]
Likelihood 1 [        ] [        ] [        ] [        ] [       ]

## Force-ranked risks
| Rank | ID | Risk | L | I | Composite | Zone |
|------|----|------|---|---|-----------|------|
| 1 | R1 | [name] | 5 | 5 | 25 | red |
| 2 | R7 | [name] | 5 | 5 | 25 | red |
| 3 | R4 | [name] | 4 | 5 | 20 | red |
| … |    |      |   |   |           |      |

## Top-[N] — what we'd do today if it triggered
1. R1 [name] — [immediate action under fire]
2. R7 [name] — [immediate action]
3. R4 [name] — [immediate action]
… (through N)

## Top-3 execution check
| Rank | ID | Mitigation status | Gap? |
|------|----|-------------------|------|
| 1 | R1 | in motion | no |
| 2 | R7 | planned   | YES — red-zone risk, mitigation not yet started |
| 3 | R4 | absent    | YES — no mitigation exists |

## Summary
- Concentration: [which zone is crowded]
- Hottest risk: [ID, why]
- Most important unaddressed top risk: [ID — the headline gap]
```

---

## Verification

- [ ] 5×5 heat map rendered with every risk placed by (likelihood, impact).
- [ ] Composite thresholds for zones stated explicitly.
- [ ] All risks force-ranked by composite, impact breaking ties.
- [ ] Top-N each have a one-line immediate "what we'd do today if it triggered."
- [ ] Top-3 execution check states in motion / planned / absent for each.
- [ ] Any red-zone risk without an active mitigation is flagged as a gap.
- [ ] Scores consistent with the source register, or changes flagged.
- [ ] Shared cells list all risk IDs.
- [ ] Summary names the hottest risk and the most important unaddressed one.
