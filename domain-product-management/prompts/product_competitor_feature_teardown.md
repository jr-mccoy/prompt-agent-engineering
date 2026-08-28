---
title: "Competitor Feature Teardown — Comparison Matrix, Pattern Surfacing, and Defensible Differentiation"
category: product-management/prompts
description: "Run a feature-by-feature teardown across 3+ named competitors: build a comparison matrix, surface patterns and table-stakes vs. differentiators, identify gaps, and recommend a defensible position. Requires real named competitors; never fabricates competitor features and flags every claim the user must verify."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - DS-06
  - CM-02
  - QA-04
difficulty: intermediate
tags:
  - competitive-analysis
  - feature-comparison
  - product-strategy
  - differentiation
  - market-positioning
updated: "2026-06-07"
related_prompts:
  - domain-business-strategy/research/research_competitive_landscape.md
  - domain-product-management/prompts/product_product_idea_vetting_will_it_fly_or_flop.md
  - domain-software-engineering/analysis/business/swot_analysis.md
---

# Competitor Feature Teardown

**Objective:** Compare a product (or product concept) against 3+ named real competitors feature-by-feature, surface what's table-stakes vs. genuinely differentiated, identify exploitable gaps, and recommend a defensible position — without fabricating any competitor capability.

**When to Use:**
- You are positioning a product and need to know where rivals are strong, weak, and identical.
- You are deciding which features are table-stakes (must-have to be considered) vs. differentiators (reason to switch).
- You are preparing a competitive section for a PRD, board deck, or GTM plan.
- A vague "we're better than them" claim needs to be made concrete and defensible.

**When NOT to use:**
- You can't name at least 3 real competitors — without named competitors this prompt cannot run honestly (do market discovery first via `research_competitive_landscape.md`).
- You want full market sizing or landscape mapping — that's a broader research task.
- You want a SWOT of your own product — use `swot_analysis.md`.

## Inputs / Context

The user supplies (wrap pasted competitor notes in `<competitor_notes>` tags):

1. **Your product/concept** — name, one-line description, and the value proposition you believe in.
2. **Named competitors (3+ required)** — real company/product names. The teardown will not proceed on hypothetical or anonymized competitors.
3. **Feature/dimension list** — the capabilities to compare (e.g., onboarding, pricing model, integrations, mobile, support, security). If absent, the prompt proposes a starter set for confirmation.
4. **Target buyer** — who decides and what they care about most.
5. **Source material the user has** — pasted product pages, pricing tables, review excerpts, hands-on notes. Anything the user provides is treated as evidence; anything they don't is treated as unknown.

## Constraints

### Must
- Require at least 3 **named, real** competitors before producing a matrix.
- Mark every cell of the comparison matrix with a **source/confidence tag**: `[user-provided]`, `[publicly-known — verify]`, or `[unknown — user must check]`.
- Distinguish **table-stakes** (everyone has it) from **differentiators** (a real reason to choose one product).
- Identify **gaps**: capabilities no competitor serves well, or where the user's product could be uniquely strong.
- Recommend a **defensible position** — one that is hard to copy quickly, tied to a real gap, not a feature any competitor can ship next quarter.
- Flag every claim about a competitor that the prompt did not receive as evidence, with a verification instruction.

### Must Not
- Invent, estimate, or assume competitor features, pricing, or capabilities the user did not provide. If it's not in the inputs, it is `[unknown — user must check]`.
- Present "publicly known" claims as verified facts — public claims drift; flag them for verification.
- Recommend a differentiation based on a feature any competitor can trivially replicate.
- Treat the user's own value-proposition belief as established fact — test it against the matrix.
- Fabricate review quotes, ratings, user counts, or market-share figures.

## Instructions

1. **Validate inputs (CM-02).**
   - Confirm 3+ named real competitors exist. If not, stop and ask the user to name them.
   - Confirm or propose the comparison dimensions; lock the list before building the matrix.

2. **Build the comparison matrix (RT-02).**
   - Rows = features/dimensions; columns = your product + each competitor.
   - Fill each cell ONLY from supplied evidence. Tag every cell `[user-provided]`, `[publicly-known — verify]`, or `[unknown — user must check]`.
   - Never leave a cell falsely confident — an unknown is an unknown.

3. **Surface patterns.**
   - Identify **table-stakes**: dimensions where every (or nearly every) competitor is present and comparable.
   - Identify **clustering**: where the field converges (a likely standard) and where it splits (a strategic choice).
   - Identify **differentiators**: dimensions where one product clearly leads.

4. **Identify gaps (DS-06).**
   - Underserved dimensions: capabilities weak or absent across the field.
   - Buyer-priority misalignment: where the field over-invests in things the target buyer doesn't value, or under-invests in things they do.
   - Rank gaps by buyer value × field weakness.

5. **Test defensibility.**
   - For each candidate differentiation, ask: how fast could a competitor copy it? Is it tied to a structural advantage (data, network, integration depth, domain expertise) or just a feature?
   - Keep only positions that are slow to copy AND tied to a real gap.

6. **Acknowledge uncertainty explicitly (QA-04).**
   - State which conclusions rest on `[user-provided]` evidence (higher confidence) vs. `[publicly-known]` or `[unknown]` cells (lower confidence).
   - List the highest-leverage facts to verify before acting on the recommendation.

7. **Recommend a position.**
   - One primary defensible position + the 2–3 facts that, if confirmed, validate it.

## False-Positive Prevention

1. **Fabricated features.** The most dangerous failure: filling a matrix cell with a plausible-but-unverified competitor capability. If the user didn't provide it and you can't tag it `[publicly-known — verify]`, it is `[unknown — user must check]`. Never guess.
2. **Stale public claims as fact.** Pricing pages, feature lists, and roadmaps change. Anything labeled `[publicly-known]` carries a "verify" flag — it is a lead, not a fact.
3. **Feature-parity theater.** Two products both "having integrations" is not parity — depth, breadth, and quality differ. Don't collapse different things into the same cell because they share a label.
4. **Copyable differentiation.** A "differentiator" any competitor can build in a sprint is not defensible. Pressure-test every recommendation against speed-to-copy.
5. **Confirmation of the user's belief.** Do not bend the matrix to validate the user's stated value proposition. If the evidence contradicts it, say so.
6. **Invented social proof.** No fabricated star ratings, review quotes, NPS, user counts, or market share. If the user didn't supply it, it doesn't enter the analysis.
7. **Anonymized competitors.** "A major competitor" is not analyzable. Real names or the teardown doesn't run.

## Output Format

```
# Competitor Feature Teardown — [your product]

## Scope
- Your product: [name + value prop being tested]
- Competitors (named, real): [A], [B], [C], ...
- Target buyer: [who, top priority]
- Dimensions compared: [list]

## Evidence legend
[user-provided] = supplied by user · [publicly-known — verify] = commonly stated, must confirm · [unknown — user must check] = no evidence

## Comparison matrix
| Dimension | Your product | [Competitor A] | [Competitor B] | [Competitor C] |
|-----------|--------------|----------------|----------------|----------------|
| [feature] | [value] [tag]| [value] [tag]  | [value] [tag]  | [value] [tag]  |

## Patterns
- **Table-stakes (everyone has):** [...]
- **Field convergence (likely standard):** [...]
- **Field split (strategic choice):** [...]
- **Current differentiators (who leads where):** [...]

## Gaps (ranked by buyer value × field weakness)
| # | Gap | Buyer value | Field weakness | Note |
|---|-----|-------------|----------------|------|
| 1 | [...]| High        | High           | [...]|

## Defensibility test
| Candidate position | Speed-to-copy | Tied to structural advantage? | Keep? |
|--------------------|---------------|-------------------------------|-------|
| [...]              | Slow/Fast     | [yes/no — what]               | [Y/N] |

## Recommended position
- **Primary:** [defensible position]
- **Why defensible:** [structural advantage / gap it exploits]
- **Confidence:** [High/Medium/Low] — rests on: [user-provided vs. unverified evidence]

## Verify before acting (highest-leverage unknowns)
- [ ] [fact to confirm] — affects: [which conclusion]
- [ ] [fact to confirm] — affects: [which conclusion]
```

## Verification

- [ ] At least 3 named, real competitors present (not anonymized).
- [ ] Every matrix cell carries a source/confidence tag.
- [ ] No competitor feature stated without evidence or a verify-flag.
- [ ] Table-stakes distinguished from genuine differentiators.
- [ ] Gaps ranked by buyer value × field weakness.
- [ ] Each recommended position passed the speed-to-copy / structural-advantage test.
- [ ] User's own value proposition tested against the matrix, not assumed true.
- [ ] No fabricated ratings, quotes, counts, or market share.
- [ ] Highest-leverage facts-to-verify listed before the recommendation is acted on.
- [ ] Confidence level stated and tied to evidence quality.
