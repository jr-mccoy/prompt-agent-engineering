---
title: "Morphological Matrix — Decompose the Solution Space and Recombine It"
category: ideation/combinatorial
description: "Break a design problem into 4–7 independent parameters, list 3–6 options for each, prune impossible option pairs with a cross-consistency check, then deliberately sample combinations — the obvious one, the extremes, and randomised draws — to surface configurations nobody proposed. Distinct from ideation_scamper.md, which transforms one existing thing along seven lenses; the matrix builds the whole space of possible configurations from parts."
techniques:
  - DT-01
  - RT-02
  - OC-03
  - CM-02
  - QA-01
difficulty: intermediate
tags:
  - ideation
  - morphological-analysis
  - combinatorial
  - concept-generation
  - product-design
  - zwicky-box
  - ideas-look-alike
  - explore-all-options
  - mix-and-match
updated: "2026-09-24"
reasoning:
  styles: [combinatorial, systematic, divergent]
  stakes: low_to_moderate
  horizon: variable
  uncertainty: ambiguity
  evidence_quality: not_applicable
  domain_complexity: moderate
  collaboration: solo_or_team
  output_format: matrix
  user_role: [pm, designer, engineer, founder, strategist]
  mode: [diverge]
related_prompts:
  - domain-ideation/ideation_scamper.md
  - domain-ideation/ideation_forced_quantity_100_ideas.md
  - domain-ideation/ideation_idea_convergence_dot_voting.md
---

# Morphological Matrix — Decompose the Solution Space and Recombine It

**Objective:** Generate concepts by structure rather than inspiration. Decompose the problem into a small number of independent parameters (the dimensions any solution must decide), list the realistic options for each, remove the pairs that cannot coexist, and then sample the remaining combinations on purpose. The method (Fritz Zwicky's morphological analysis, often drawn as a "Zwicky box") is useful precisely because the space grows multiplicatively: five parameters with four options each is 1,024 configurations, and the team has usually considered three of them.

---

## When to Use

- The problem is multi-part and every proposed concept is a variant of the same configuration.
- You want to know what the full option space looks like before committing.
- A team needs a shared, inspectable map of design choices rather than competing whole concepts.
- You are designing a service, product, process, or campaign with separable decisions.

**Distinct from:**
- `domain-ideation/ideation_scamper.md` — starts from one existing thing and transforms it. The matrix starts from the problem's dimensions and builds configurations; use SCAMPER when you have a thing, the matrix when you have a problem with parts.
- `domain-ideation/ideation_forced_quantity_100_ideas.md` — unstructured breadth. The matrix gives structured breadth and shows *which* choices differ between ideas.
- `domain-decision-making/tradeoff_pugh_matrix.md` — compares a few finished concepts against a datum. Use it after this prompt, on the configurations you select.

**When NOT to use:**
- The problem does not decompose — the parameters are so entangled that choosing one fixes the rest.
- You need one surprising leap, not a map; use random stimulus or analogy mining.

---

## Inputs / Context

1. **The design problem.** What the solution must accomplish, for whom.
2. **Candidate parameters.** Any decisions the user already knows must be made (optional; derived in Step 1 otherwise).
3. **Known options.** Current or competitor choices per parameter.
4. **Hard constraints.** Rule out options before the matrix is built.
5. **Selection intent.** What the output feeds — concept testing, a pitch, a roadmap.

---

## Method

### Step 1 — Identify 4–7 parameters
List the decisions every solution must make. Test each for **independence**: can it vary while the others stay fixed? Merge or drop parameters that are really consequences of another. Fewer than four is usually too coarse; more than seven becomes unreadable.

### Step 2 — List 3–6 options per parameter
Options must be mutually exclusive within a parameter and cover the realistic range, including at least one unconventional option per parameter. Remove options that violate hard constraints, and record them as excluded.

### Step 3 — Cross-consistency check
For each pair of parameters, mark option pairs that cannot coexist (logically impossible, physically incompatible, or ruled out by a constraint). Record the reason for each exclusion. State the number of configurations before and after pruning.

### Step 4 — Sample configurations deliberately
Pick 8–12 configurations from the pruned space:
- **The current default** — what the team or market does now.
- **Two extremes** — take the most conventional option on every parameter, then the least conventional.
- **One-change neighbours** — the default with one parameter changed, for 2–3 parameters.
- **Randomised draws** — 3–4 combinations selected by position (e.g., rolling a die per parameter), kept even if odd.

### Step 5 — Name and describe each configuration
Give each a short name and a two-sentence description of how it would work end to end. A configuration that cannot be described coherently is a hidden inconsistency; add it to Step 3.

### Step 6 — Flag for convergence
Tag each described configuration with feasibility and novelty (low / medium / high). Do not rank; hand 4–6 to convergence.

---

## Output Format

```
# Morphological matrix — [problem]

## Parameters and options
| Parameter | Option 1 | Option 2 | Option 3 | Option 4 | ... |
Excluded options (constraint): [...]

## Cross-consistency exclusions
| Pair | Reason |
Configurations: [N before] → [N after pruning]

## Sampled configurations
| Name | P1 | P2 | P3 | P4 | P5 | How sampled |

## Descriptions
### [Name]
[two sentences] — Feasibility: [ ] Novelty: [ ]

## Hand-off (4–6)
- ...
```

---

## Verification

- [ ] 4–7 parameters, each tested for independence.
- [ ] 3–6 mutually exclusive options per parameter, at least one unconventional.
- [ ] Every cross-consistency exclusion has a reason; before/after counts shown.
- [ ] Sample includes default, both extremes, one-change neighbours, and random draws.
- [ ] Each sampled configuration described end to end in two sentences.
- [ ] Hand-off list is 4–6 configurations, unranked.

---

## False-Positive Prevention

1. **Dependent parameters.** "Price" and "tier count" often move together. If choosing one mostly fixes the other, merge them, or the matrix inflates with meaningless combinations.
2. **Overlapping options.** "Mobile app" and "iPhone app" in the same row are not exclusive. Options must partition the parameter.
3. **Cherry-picked sampling.** Choosing only configurations that already appeal defeats the method. The random draws stay in the sample even when they look odd.
4. **Unexplained pruning.** Excluding a pair "because it won't work" without a reason quietly removes the novel region. Every exclusion needs a stated reason.
5. **Confusing count with coverage.** 1,024 configurations is not 1,024 ideas; most differ trivially. The value is the map plus the deliberate sample.
6. **Incoherent configurations.** A row of options that cannot be described as one working thing is a missed inconsistency, not a creative leap.
7. **Ranking inside the matrix.** This prompt diverges. Scoring belongs in convergence.

---

## Example

**Problem:** get groceries to residents of mid-rise apartment buildings without anyone waiting at home.

| Parameter | Options |
|-----------|---------|
| Ordering | App · Standing weekly list · Voice message · Building-wide group order |
| Vehicle | Van · Cargo bike · Resident on their commute · Building-owned locker restock |
| Hand-off point | Door · Refrigerated lobby locker · Neighbour pickup · Workplace |
| Timing | On demand · Fixed weekly slot · Overnight |
| Payment | Per order · Subscription · Added to rent |

Pruning: cargo bike × overnight (restricted riding hours under the local ordinance supplied) · door × overnight (no building access overnight) · added-to-rent × on demand (landlord billing cannot itemise ad hoc). 4×4×4×3×3 = 576 → 428 after pruning (48 + 48 − 12 overlap + 64 removed).

Sampled (5 of 10 shown):
- **Default:** App · Van · Door · On demand · Per order.
- **One-change:** default with Hand-off → Refrigerated lobby locker — no one needs to be home.
- **Extreme unconventional:** Group order · Resident on commute · Neighbour pickup · Fixed weekly · Added to rent — "Building Pantry": one resident a week collects the building order, reimbursed by rent credit.
- **Random draw:** Voice message · Cargo bike · Workplace · Fixed weekly · Subscription — groceries delivered to office buildings on a weekly bike round for elderly-parent orders placed by voice.
- **Random draw:** Standing list · Locker restock · Lobby locker · Overnight · Subscription — "Fridge that fills itself": a building locker restocked overnight from standing lists.

Hand-off: lobby-locker one-change, Building Pantry, Fridge that fills itself, the workplace draw.

---

## Techniques Used

- **DT-01 Hierarchical Task Breakdown** — decomposition into independent parameters.
- **RT-02 Multi-Dimensional Analysis Framework** — the parameter-by-option space.
- **OC-03 Markdown Table Specification** — matrix, exclusions, and sample tables.
- **CM-02 Constraint Specification** — parameter/option counts and reasoned exclusions.
- **QA-01 Self-Verification** — coherence check on each sampled configuration.

---

## Related Prompts

- `domain-ideation/ideation_scamper.md` — transform one existing thing rather than build the space.
- `domain-ideation/ideation_forced_quantity_100_ideas.md` — unstructured breadth.
- `domain-ideation/ideation_idea_convergence_dot_voting.md` — narrow the sampled configurations.
