---
title: "Source Triangulation — Cross-Check a Claim Across 3+ Independent Source Types"
category: research-academic/triangulation
description: "Take a single claim and check it against 3+ sources of different types (peer-reviewed, primary, journalistic, expert, industry, regulatory). Surface where they converge, diverge, and where dependencies between sources inflate apparent agreement. Output is a triangulated verdict with confidence anchored on diversity and quality of convergence."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - DS-01
  - CM-02
  - QA-01
difficulty: intermediate
tags:
  - research
  - triangulation
  - source-evaluation
  - independence
  - verification
updated: "2026-05-10"
reasoning:
  styles: [comparative, independence-aware]
  stakes: variable
  horizon: variable
  uncertainty: variable
  evidence_quality: variable
  domain_complexity: variable
  collaboration: solo
  output_format: source_grid_plus_verdict
  user_role: [researcher, journalist, analyst, fact-checker, individual]
  mode: [audit, verify]
related_prompts:
  - domain-research-academic/research_evidence_map.md
  - domain-reasoning-craft/epistemic/epistemic_source_credibility_triangulation.md
  - domain-reasoning-craft/reasoning-moves/reasoning_bayesian_belief_update.md
---

# Source Triangulation

**Objective:** Take a single claim and verify it against 3+ sources of different types. Surface where the sources converge, where they diverge, and where dependencies inflate apparent agreement. Produce a triangulated verdict with confidence calibrated on the *diversity* and *quality* of the convergence — not just the count.

**When to use:**
- Verifying a claim before citing or acting on it.
- A single high-impact source needs corroboration before being trusted.
- A widely-repeated claim feels like consensus — checking whether the consensus is independent agreement or one source repeated.
- Adversarial collaboration where parties trust different sources.

**When NOT to use:**
- The claim is trivially verifiable from one authoritative primary source (e.g., a court ruling text).
- Triangulation would slow a time-critical decision and the claim is well-aligned with prior knowledge.

**Audience:** Researchers, journalists, analysts, fact-checkers, anyone evaluating a claim before propagating it.

---

## Inputs / Context

1. **The claim.** One sentence, sharp enough to evaluate as supported / contradicted / qualified per source.
2. **Candidate sources.** At least 3 of *different types*: peer-reviewed academic, primary documents (court records, government data, financial filings), journalistic reporting, expert testimony, industry / trade publications, regulatory filings, NGO reports.
3. **Why this claim matters.** What action depends on it.
4. **Time pressure.** Affects depth of triangulation.

---

## Constraints

### Must
- Use **3+ source types** (not just 3 sources of the same type — five op-eds is one source type, not five sources).
- Per source: cite, type, date, author / institution, what the source actually says about the claim (verbatim or paraphrased), direction (supports / contradicts / qualifies / silent).
- Run an **independence audit**: do sources draw on each other? A journalist citing a study, an op-ed citing the same study, and the study itself are *one* piece of evidence, not three.
- Surface **convergence pattern**: do sources of different types agree, or only sources of one type?
- Produce a **verdict** on the claim: supported, contradicted, mixed, insufficient, supported-with-qualification.
- State **confidence**, anchored on diversity of source types AND quality of convergence (diverse + high-quality = high confidence).

### Must Not
- Treat 5 sources of the same type as triangulation.
- Count chained sources as independent (op-ed citing study citing primary).
- Verdict "supported" because count favors it without checking independence.
- Smooth divergence ("most sources say...") when sources actually contradict.
- Skip the silence finding — if 4 of 5 sources don't address the claim, that's a finding.

---

## Instructions

### Step 1 — Restate the claim
One sharp sentence. If the claim has a quantitative element, isolate the number being claimed.

### Step 2 — Catalog sources
For each source: bibliographic info, type, date, position on claim (verbatim quote where possible).

### Step 3 — Independence audit
Map citations and reuse:
- Source A cites Source B → not independent on the cited point
- Source A and Source B both cite Source C → both rely on C
- Source A is journalist's interpretation of Source B → not independent
Group sources into **independent clusters**. The triangulation count is the number of clusters, not sources.

### Step 4 — Convergence pattern
Across independent clusters:
- All converge → strong triangulation
- Diverge along type lines (academics agree, industry disagrees) → suspicious; investigate why
- Mixed within types → genuine contestation
- One cluster, others silent → not triangulated

### Step 5 — Quality weight
Within each cluster, rate the strongest source on standard quality criteria (design, evidence, conflicts, recency). Triangulation weight is not just count of clusters but quality-weighted count.

### Step 6 — Verdict
- **Supported:** ≥3 independent clusters of decent quality converge.
- **Supported-with-qualification:** convergence on the core but divergence on a specific element.
- **Contradicted:** independent high-quality clusters disagree with the claim.
- **Mixed:** genuine independent disagreement.
- **Insufficient:** fewer than 3 independent clusters; can't triangulate.

### Step 7 — Confidence
- High: 4+ independent clusters, diverse types, quality is solid, no troubling silences.
- Moderate: 3 clusters, some quality concerns, no major contradictions.
- Low: 2 clusters or major silences or quality issues.

### Step 8 — What would change the verdict
Name the single piece of additional evidence that would most move the verdict.

---

## False-Positive Prevention

1. **Same-type stacking.** Five academic papers ≠ five source types.
2. **Citation chain inflation.** Three sources citing the same study are one independent observation.
3. **Silent dismissal.** Sources that don't address the claim aren't supporters; their silence is information.
4. **Quality-blind counting.** A weak source agreeing doesn't strengthen a strong source disagreeing.
5. **Pattern-blindness.** Type-based divergence (industry vs academic) often signals interest-based reasoning; investigate before averaging.
6. **Convergence theater.** Saying "sources agree" when they're paraphrasing each other.

---

## Output Format

```
# Source triangulation — [claim]

## Claim
> [Sharp]

## Sources
| # | Source        | Type        | Date | Says about claim (verbatim or paraphrased) | Direction |
|---|---------------|-------------|------|---------------------------------------------|-----------|
| 1 | [citation]    | peer-academic | yyyy | [...]                                     | supports  |
| 2 | [...]         | journalistic | yyyy | [...]                                      | qualifies |
| ... |             |              |      |                                            |           |

## Independence audit
- Cluster A (independent): sources [1, 4]
- Cluster B (chained — all cite source X): sources [2, 3, 5]
- Cluster C (independent): source [6]
- Independent clusters: 3

## Convergence pattern
- Across clusters: [all converge / diverge by type / mixed]
- Notable silences: [...]

## Quality weight
| Cluster | Strongest source | Quality | Direction |
|---------|------------------|---------|-----------|
| A       | [#]              | high    | supports  |
| B       | [#]              | medium  | supports  |
| C       | [#]              | high    | qualifies |

## Verdict
- [Supported / Supported-with-qualification / Contradicted / Mixed / Insufficient]
- Reasoning: [one paragraph]

## Confidence
- [High / Moderate / Low]
- Anchored on: [diversity, quality, silences]

## What would change the verdict
- [Specific additional evidence]
```

---

## Verification

- [ ] 3+ source types, not 3+ same-type sources.
- [ ] Per-source position is verbatim or close paraphrase.
- [ ] Independence clusters identified and chained sources collapsed.
- [ ] Convergence pattern named (full / type-divergent / mixed / one-sided).
- [ ] Quality weighted, not just counted.
- [ ] Verdict explicit (not "more research needed" alone).
- [ ] Confidence anchored on diversity AND quality.
- [ ] Silences flagged.
