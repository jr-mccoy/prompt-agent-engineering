---
title: "Evidence Map — Map Known Evidence Onto a Claim / Anti-Claim Grid"
category: research-academic/evidence-synthesis
description: "Take a claim under investigation and map all known evidence onto a grid: supporting / contradicting / mixed / inconclusive, plotted against evidence quality. Surfaces what the evidence base actually looks like (often: thinner than expected, with the strongest signals coming from weak studies), and identifies gaps where targeted research would shift the picture."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - DS-01
  - DS-02
  - CM-02
  - QA-01
difficulty: intermediate
tags:
  - research
  - evidence-synthesis
  - mapping
  - gap-analysis
  - quality-assessment
updated: "2026-05-10"
reasoning:
  styles: [systematic, taxonomic, gap-analysis]
  stakes: variable
  horizon: weeks_to_months
  uncertainty: variable
  evidence_quality: variable
  domain_complexity: variable
  collaboration: solo_or_pair
  output_format: matrix_plus_gap_list
  user_role: [researcher, analyst, policy, founder, consultant]
  mode: [audit, synthesize]
related_prompts:
  - domain-research-academic/research_literature_review_plan.md
  - domain-research-academic/research_secondary_source_synthesis.md
  - domain-research-academic/research_hypothesis_generator.md
---

# Evidence Map

**Objective:** For a claim under investigation, map all known evidence onto a grid: supporting / contradicting / mixed / inconclusive on one axis, evidence quality (high / medium / low) on the other. The map shows at a glance whether the evidence base is one-sided or contested, whether the strongest signals come from strong studies or weak ones, and where targeted research would meaningfully shift the picture.

**When to use:**
- Mid-literature-review: synthesizing what's been found before writing the review.
- Decision support: an evidence-based decision is pending and the user needs to see the actual state of the evidence.
- Pre-research planning: identifying gaps where a new study or analysis would be high-leverage.
- Adversarial collaboration: two parties disagreeing about a claim need to see what the evidence base actually contains.
- Auditing a published claim or position.

**When NOT to use:**
- Evidence base is too small to map (< ~5 sources). Just list and discuss.
- The claim is normative, not empirical. Evidence maps are for empirical claims.
- The user wants a single answer, not a map. (The map's value is precisely that it doesn't collapse to a single answer.)

**Audience:** Researchers, analysts, policy people, founders, consultants — anyone who needs to communicate "here's what the evidence actually looks like, and here's where it doesn't yet exist."

---

## Inputs / Context

1. **The claim.** A single empirical proposition that could be true or false. Sharp enough to evaluate evidence against.
2. **The evidence base.** A list of sources (studies, reports, datasets, observations) the user has identified. Coming out of `research_literature_review_plan.md` execution is ideal.
3. **Evidence-quality criteria.** What makes a source high / medium / low quality for this claim (study design, sample size, replication, methodology rigor, conflicts of interest, age).
4. **Stakes and use.** Why the claim's evidence base matters; what action it informs.
5. **Adversarial check.** Who would dispute this map's construction, and on what grounds?

---

## Constraints

### Must
- Plot every relevant source on the grid (supporting / contradicting / mixed / inconclusive × high / medium / low quality).
- Define the **quality criteria** explicitly before plotting. Hidden quality criteria are how motivated reasoning enters.
- For each source, record: citation, design / method, key finding, direction (supports / contradicts / mixed / inconclusive), quality with reason.
- Identify **clusters and gaps**. Gaps are sometimes more informative than clusters.
- Distinguish between **independent** evidence and **chained** evidence (a meta-analysis citing the same primary studies as separate reviews — these are not independent observations).
- Compute and report a verdict on the evidence base: **strong support**, **moderate support**, **mixed**, **weak**, **insufficient**, **strong against**, **moderate against**.
- Identify the **highest-leverage gap** — what study, dataset, or analysis would most change the picture if it existed.

### Must Not
- Treat all sources as equally weighted. The grid's quality axis exists precisely because not all evidence is equal.
- Score sources on quality after seeing their direction. Quality assessment should be blind to outcome.
- Confuse number of sources with weight of evidence. Five low-quality studies can be outweighed by one high-quality one.
- Pretend a thin evidence base is thick by counting tangentially-related sources.
- Hide independent-vs-chained evidence relationships. Chained evidence inflates apparent support.

---

## Instructions

### Step 1 — State the claim
One sentence. Sharp enough that "supports" / "contradicts" is meaningful for each source.

### Step 2 — Define quality criteria
What makes a source high / medium / low quality for this specific claim? Examples:
- Study design strength (RCT > quasi-experimental > observational > case study)
- Sample size adequate to detect effects
- Replication or independent confirmation
- Methodology transparency
- Conflict-of-interest disclosure
- Age of source (more recent often better, but not always)
- Source credibility (peer-reviewed > preprint > grey > advocacy)

State the criteria *before* plotting. Then apply them blind to direction.

### Step 3 — Plot each source
Build a table of every relevant source. For each:
- Citation
- Design / method
- Key finding
- Direction relative to claim: supports / contradicts / mixed / inconclusive
- Quality: high / medium / low (with reason)
- Independent or chained (note other sources it draws on)

### Step 4 — Render the grid
Build the 4x3 grid (direction × quality):

|                | High quality | Medium quality | Low quality |
|----------------|--------------|----------------|-------------|
| Supports       | [source IDs] | [...]          | [...]       |
| Contradicts    | [source IDs] | [...]          | [...]       |
| Mixed          | [...]        | [...]          | [...]       |
| Inconclusive   | [...]        | [...]          | [...]       |

### Step 5 — Pattern read
Look at the grid. Common patterns:
- **High-quality concentrated on one side:** strong evidence, lean accordingly.
- **High-quality mixed or contradicting; low-quality concentrated on one side:** the apparent direction is being driven by weak studies. Not strong evidence.
- **Sparse high-quality, dense low-quality:** evidence base is weaker than the volume suggests.
- **Sparse all around:** insufficient evidence; primary research needed.
- **Mostly chained / dependent:** apparent breadth is illusory.

### Step 6 — Independence audit
Mark any sources that share data, primary studies, or authorship. Adjust the apparent weight downward where chains exist.

### Step 7 — Verdict
- Verdict on the evidence base: [strong support / moderate / mixed / weak / insufficient / moderate against / strong against]
- Confidence in the verdict: [low / moderate / high]
- Anchored on: [which cells of the grid carry the verdict]

### Step 8 — Gaps
- What's missing? (Specific designs, populations, time windows, geographies, outcome measures.)
- Highest-leverage gap: which single piece of evidence would most change the verdict if it existed.
- Feasibility of filling the gap: easy / moderate / hard / not feasible.

### Step 9 — Adversarial check
- A skeptic of this map would dispute: [what — quality criteria, source selection, classification of direction, independence assessment].
- Counter-argument: [user's response].
- Remaining vulnerability: [what survives the counter-argument].

### Step 10 — Use
- For decision support: which decision does this verdict imply?
- For research planning: which gap to fill next?
- For communication: how to summarize this map for the audience without misrepresenting it?

---

## False-Positive Prevention

1. **Outcome-aware quality scoring.** Scoring quality after seeing direction allows motivated reasoning. Score quality blind, then plot.
2. **Vote-counting fallacy.** Treating "more sources on side X" as decisive. Quality and independence dominate count.
3. **Chained evidence inflation.** Five reviews citing the same three primary studies are not five independent observations. Chained evidence collapses to the primary studies.
4. **Selective inclusion.** Including sources that support the user's lean and excluding ones that don't (often unconsciously). Cross-check inclusion criteria with the original literature plan.
5. **Quality-dimension monoculture.** Using only one quality criterion (e.g., "peer-reviewed = high") misses important dimensions (sample size, methodology, conflict). Use a multi-dimensional rubric.
6. **Mixing claims.** Plotting evidence about a slightly different claim as if it were about the target claim. Sources that address adjacent questions go in a separate section.
7. **Gap-blindness.** Not surfacing what's missing. The empty cells of the grid are part of the deliverable.
8. **Verdict avoidance.** Refusing to issue a verdict because "the evidence is mixed" — when actually the evidence has a discernible pattern. Mixed is itself a verdict, distinct from insufficient.

---

## Output Format

```
# Evidence map — [claim]

## Claim
> [Sharp empirical proposition]

## Quality criteria (defined first, applied blind to direction)
- [Criterion 1]
- [Criterion 2]
- [Criterion 3]
- [Criterion 4]
- High = [meets ≥ N criteria], Medium = [...], Low = [...]

## Sources
| ID | Citation       | Design       | Key finding             | Direction       | Quality | Quality reason | Indep / chained |
|----|----------------|--------------|-------------------------|-----------------|---------|----------------|-----------------|
| 1  | [author yyyy]  | RCT          | [finding]               | supports        | high    | [reason]       | independent     |
| 2  | […]            | observational| […]                     | contradicts     | medium  | […]            | chained to 5,6  |
| …  |                |              |                         |                 |         |                |                 |

## Grid
|                | High quality | Medium quality | Low quality |
|----------------|--------------|----------------|-------------|
| Supports       | [IDs]        | [IDs]          | [IDs]       |
| Contradicts    | [IDs]        | [IDs]          | [IDs]       |
| Mixed          | [IDs]        | [IDs]          | [IDs]       |
| Inconclusive   | [IDs]        | [IDs]          | [IDs]       |

## Pattern read
[2–4 sentences describing what the grid shows: concentration, sparsity, quality-direction relationship]

## Independence audit
- Chained groups: [list, with effective independent count]
- Adjusted weight: [discussion]

## Verdict
- **Evidence base:** [strong support / moderate / mixed / weak / insufficient / moderate against / strong against]
- **Confidence:** [low / moderate / high]
- **Anchored on:** [which cells]

## Gaps
| Gap                                        | Highest-leverage? | Feasibility |
|--------------------------------------------|-------------------|-------------|
| [missing study type / population / etc.]   | yes               | moderate    |
| […]                                        | no                | easy        |

## Adversarial check
- Skeptic's strongest objection: [...]
- Counter: [...]
- Residual vulnerability: [...]

## Use
- For decision support: [implication]
- For research planning: [next gap to fill]
- Communication summary: [one sentence honest summary]
```

---

## Verification

- [ ] Quality criteria defined before sources are plotted.
- [ ] Every source plotted with citation, design, finding, direction, quality, independence.
- [ ] Grid is fully rendered with all four direction rows and three quality columns.
- [ ] Independence audit identifies chained evidence and adjusts weight.
- [ ] Pattern read names the dominant pattern (e.g., "high-quality contradicts; apparent support driven by low-quality").
- [ ] Verdict issued (not avoided) with confidence level.
- [ ] Highest-leverage gap identified.
- [ ] Adversarial check performed.
- [ ] No outcome-aware quality scoring.
- [ ] No vote-counting without weighting.
