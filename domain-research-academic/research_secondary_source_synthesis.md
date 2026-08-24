---
title: "Secondary Source Synthesis — Combine 5–20 Sources into a Structured Narrative That Preserves Disagreement"
category: research-academic/synthesis
description: "Take a set of 5–20 sources on a topic and synthesize them into a structured narrative. Preserves disagreement explicitly rather than averaging it out, attributes claims to sources, distinguishes consensus from majority from contested, and surfaces what the sources collectively say versus what they don't address."
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
  - synthesis
  - narrative
  - attribution
  - disagreement-preservation
updated: "2026-05-10"
reasoning:
  styles: [synthetic, comparative, attributional]
  stakes: variable
  horizon: variable
  uncertainty: variable
  evidence_quality: variable
  domain_complexity: variable
  collaboration: solo_or_pair
  output_format: structured_synthesis_with_attribution_table
  user_role: [researcher, journalist, analyst, policy, consultant, student]
  mode: [synthesize, audit]
related_prompts:
  - domain-research-academic/research_literature_review_plan.md
  - domain-research-academic/research_evidence_map.md
  - domain-research-academic/research_question_formulation.md
---

# Secondary Source Synthesis

**Objective:** Take 5–20 sources on a focused topic and produce a structured synthesis that:
- Identifies the questions the sources collectively address
- Distinguishes **consensus** (all or nearly all agree), **majority** (most agree, some dissent), **contested** (genuine disagreement), and **silence** (no source addresses)
- Attributes every substantive claim to one or more sources
- Preserves disagreement explicitly rather than averaging or smoothing it
- Names what the literature does *not* address

The synthesis should be informative *and* honest about its evidentiary base, so a reader can audit it.

**When to use:**
- Mid- or post-literature-review: producing the synthesis section of a review.
- Writing a memo or briefing that draws on a defined source set.
- Comparing perspectives across 5–20 articles, books, reports, or primary documents.
- Preparing a position paper or policy recommendation grounded in cited literature.
- Any time the deliverable claims to represent "what the literature says."

**When NOT to use:**
- Source set is < 5 (just discuss them individually) or > 25 (group sources first via thematic clustering before synthesizing).
- The user wants a single answer, not a synthesis. (Synthesis preserves complexity.)
- Sources have not yet been screened for quality. Quality screen first.

**Audience:** Researchers, journalists, policy analysts, consultants, students producing literature-grounded deliverables.

---

## Inputs / Context

1. **The synthesis question.** What does the user want the synthesis to address? (e.g., "What does the literature say about whether X works under condition Y?")
2. **The source set.** 5–20 items with citations. Brief descriptions of each (or full text). Note source type (peer-reviewed, grey, journalistic, primary).
3. **Source quality assessments.** From a prior step, or to be done here. Quality affects how much weight a source carries in the synthesis.
4. **Audience for the synthesis.** Influences depth, jargon, attribution style.
5. **Length / format constraint.** A 500-word brief vs a 5000-word review chapter requires different synthesis density.

---

## Constraints

### Must
- Identify 3–7 **synthesis themes** — questions or sub-topics around which the source set has things to say.
- For each theme: state what the sources collectively conclude, distinguishing consensus, majority, contested, and silence.
- **Attribute every substantive claim** to specific source(s) inline. No floating "researchers say" — say which researchers.
- Preserve disagreement explicitly. When sources disagree, surface the disagreement with both sides cited; do not average.
- For contested themes, briefly characterize each position and the strongest source for it.
- Identify **silences** — substantive aspects of the synthesis question the sources do not address. Silences are part of the synthesis output.
- Weight sources by quality, not just volume. A high-quality dissenting source can outweigh several low-quality concurring sources.
- For each theme, note the **state of the evidence** (rich, moderate, thin, contested, silent).

### Must Not
- Smooth disagreement into false consensus ("the literature generally suggests…" when half the sources contradict it).
- Make claims that none of the cited sources support. Synthesis composes; it doesn't generate new substantive claims.
- Lose attribution by writing "studies show" without citations.
- Treat all sources as equally weighted regardless of quality.
- Pretend coverage is complete when it isn't. Silences are part of the deliverable.

---

## Instructions

### Step 1 — Sharpen the synthesis question
Restate. What is the synthesis trying to address? If the question is too broad for the source set, narrow it; if it's narrower than the source set, expand or reduce the set.

### Step 2 — Catalog sources with quality
For each source, brief catalog:
- Citation
- Source type (peer-reviewed empirical / theoretical / review / report / journalism / primary)
- Quality (high / medium / low) — using criteria appropriate to the source type
- Brief one-line summary of what the source contributes

### Step 3 — Identify synthesis themes
Walk the source set and identify 3–7 themes — sub-questions or sub-topics that multiple sources address. Themes are the structure of the synthesis. Avoid theme sprawl; merge adjacent themes.

### Step 4 — Per-theme synthesis
For each theme:
- **What sources address it:** [IDs]
- **State of evidence:** rich / moderate / thin / contested / silent
- **Position summary:** what the sources collectively say, distinguishing consensus / majority / contested / silence
- **Attribution:** every substantive claim cites one or more source IDs inline
- **Disagreements:** if contested, characterize each position with its strongest source
- **Quality note:** which sources are doing the most work (high quality, central) vs which are peripheral
- **Silence:** what aspects of the theme the sources do not address

### Step 5 — Cross-theme integration
After per-theme synthesis, integrate:
- Where do themes interact? (E.g., Theme 2's findings depend on Theme 1's assumptions.)
- Where does the literature collectively converge vs diverge?
- Are there sources that bridge multiple themes uniquely well?

### Step 6 — What the literature does not address
List 3–5 substantive aspects of the synthesis question that the source set is silent on. This is part of the deliverable, not a limitation hidden in a footnote.

### Step 7 — Confidence and limitations
- Confidence in the synthesis: [low / moderate / high], anchored on source quality, breadth, and how recent.
- Known limitations: source-set boundaries, selection effects, language / geographic bias, recency.
- Adversarial check: a critical reader would attack this synthesis on the grounds of [...].

### Step 8 — Use
- For decision support: which decisions does this synthesis inform, and which does it not?
- For further research: which silences are the highest priority to fill?
- For citation in a downstream document: how should the synthesis be attributed and bounded?

---

## False-Positive Prevention

1. **False consensus.** "The literature generally agrees" when the sources are split. Don't smooth.
2. **Floating attribution.** "Researchers find" without citations is opaque. Tie every claim to source IDs.
3. **Volume-as-weight.** Five mediocre sources do not outweigh one excellent source. Weight by quality.
4. **Silent silences.** Failing to surface what the literature doesn't address creates the impression of comprehensive coverage. Always include the silences section.
5. **Theme sprawl.** Generating 12 themes produces a mush. Merge adjacent themes; cap at 7.
6. **Hidden generation.** Synthesis sometimes drifts into generation: claims that none of the cited sources actually support, presented as synthesis. Audit by tracing every claim back to source.
7. **Recency invisibility.** A synthesis built on sources mostly from 5+ years ago may be outdated. Flag the recency profile.
8. **Disagreement-as-error.** Treating contested findings as a problem to resolve in synthesis. Often the contestation *is* the finding.

---

## Output Format

```
# Synthesis — [synthesis question]

## Synthesis question
> [Sharply stated]

## Source catalog
| ID | Citation         | Type            | Quality | One-line contribution |
|----|------------------|-----------------|---------|------------------------|
| S1 | [author yyyy]    | peer-empirical  | high    | [contribution]         |
| S2 | [author yyyy]    | report          | medium  | [contribution]         |
| …  |                  |                 |         |                        |

## Themes

### Theme 1: [name]
- **Sources addressing:** S1, S3, S5, S7
- **State of evidence:** rich / moderate / thin / contested / silent
- **Position:** [paragraph or two synthesizing the claim, with inline attributions like (S1; S3) for each substantive point]
- **Disagreements:** [if any: each position with strongest-source attribution]
- **Quality note:** [which sources carry the theme]
- **Silence within theme:** [what isn't addressed]

### Theme 2: [name]
[Same structure]

[etc., 3–7 themes]

## Cross-theme integration
- Theme interactions: [...]
- Convergences: [...]
- Divergences: [...]
- Bridging sources: [...]

## What the literature does not address
- [Silence 1]
- [Silence 2]
- [Silence 3]
- [Silence 4]

## Confidence and limitations
- Confidence: [low / moderate / high]
- Anchored on: [source quality / breadth / recency]
- Limitations: [boundaries, selection effects, biases]
- Adversarial check: [the strongest critique of this synthesis]

## Use
- Decisions this informs: [...]
- Decisions this does not inform: [...]
- Highest-priority silence to fill: [...]
- Citation bounds: [how to attribute in downstream documents]
```

---

## Verification

- [ ] 3–7 themes generated, not theme sprawl.
- [ ] Every substantive claim has inline source attribution.
- [ ] Consensus / majority / contested / silence distinguished within each theme.
- [ ] Disagreements preserved with both positions cited.
- [ ] Silences listed explicitly.
- [ ] Source quality affects weight, not just count.
- [ ] No claim made that no cited source supports.
- [ ] Confidence and limitations stated.
- [ ] Adversarial check performed.
- [ ] Recency profile flagged if synthesis is built on older sources.
