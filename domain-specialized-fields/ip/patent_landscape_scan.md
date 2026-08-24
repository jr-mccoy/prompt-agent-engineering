---
title: "Patent Landscape Scan — Search Strategy, Clustering, and IP Whitespace Analysis"
category: specialized-fields/ip
description: "Plan a patent landscape scan and whitespace analysis for a defined technology area and goal (freedom-to-operate check, competitive intelligence, whitespace identification, or acquisition screening). Walks through scope definition, patent classification (USPC/IPC/CPC), query construction, database selection, relevance screening, clustering by assignee/technology/time, and identification of both whitespace (low density) and crowding (high density), ending in a strategic recommendation. Counters keyword-only searches that miss class-coded prior art and confuse 'no results' with 'whitespace.'"
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
  - intellectual-property
  - patent-search
  - freedom-to-operate
  - whitespace-analysis
  - competitive-intelligence
updated: "2026-06-18"
reasoning:
  styles: [analytic, systematic, classificatory, strategic]
  stakes: high
  horizon: weeks
  uncertainty: ambiguity
  evidence_quality: rich
  domain_complexity: regulated
  collaboration: small_team
  output_format: [structured, matrix]
  user_role: [founder, engineering_leader, attorney, analyst]
  mode: [plan, synthesize, diagnose]
related_prompts:
  - domain-specialized-fields/legal/legal_research_plan.md
  - domain-business-strategy/research/technical_due_diligence_plan.md
  - domain-research-academic/research_literature_review_plan.md
---

# Patent Landscape Scan

**Objective:** Plan a patent landscape scan and IP whitespace analysis for a defined technology area and a stated goal. The plan defines what counts as in-scope, identifies the relevant patent classifications, constructs a search query that combines classes with claim-language terms and synonyms, selects databases, screens for relevance, clusters the resulting set by assignee, technology sub-area, and time, and then reads the structure: where patents are dense (crowding to avoid or design around) and where they are sparse (whitespace to pursue — or a signal that no one bothers because the area is unworkable or commercially dead). The output is a strategic recommendation tied to the goal.

**When to use:**
- **Freedom-to-operate (FTO):** checking whether a planned product risks infringing live patents.
- **Competitive intelligence:** mapping what competitors are patenting and where they are investing.
- **Whitespace identification:** finding low-density technical areas to claim.
- **Acquisition / target screening:** assessing the strength and coverage of a target's patent portfolio.

**When NOT to use:**
- You need a legal infringement opinion or validity opinion — this plans the scan; a clearance opinion is a separate legal work product.
- The technology area is so broad that no coherent scope can be defined — narrow it first.
- You need general legal research rather than patent search — use `legal_research_plan.md`.

**Audience:** IP-aware founders, R&D and engineering leaders, patent attorneys and agents, corporate-development analysts, and innovation strategists.

---

## Inputs / Context

1. **Technology area.** The field, described in both plain terms and technical terms of art.
2. **Goal.** FTO / competitive intelligence / whitespace / acquisition screening — this changes the search and the read.
3. **Product or concept (if FTO).** The specific features that might read on a claim.
4. **Geographic scope.** Which jurisdictions matter for protection or freedom (US, EP, CN, JP, PCT).
5. **Time horizon.** Whether expired patents matter (they are free to use) and how recent the relevant art is.
6. **Known players.** Competitors, likely assignees, or a target company.

---

## Constraints

### Must
- Define **what counts as in-scope** technically — features, mechanisms, applications — and what is explicitly excluded.
- Identify relevant **patent classifications** (USPC, IPC, CPC) — class-based search is what catches art that keyword search misses.
- Build a **search query** combining classification codes with claim-language terms, synonyms, and acronyms; specify field restrictions (claims vs. abstract vs. full text).
- Select **databases** appropriate to scope (USPTO PatFT/AppFT, EPO Espacenet, WIPO PATENTSCOPE, Google Patents, and commercial tools where available), and note coverage differences.
- **Screen for relevance** with stated inclusion criteria, distinguishing on-point art from adjacent noise.
- **Cluster** the set by assignee, technology sub-area, and filing date — to reveal who, what, and when.
- Distinguish **whitespace** (genuinely low patent density worth pursuing) from **dead space** (low density because the area is unworkable, off-market, or covered by non-patent means).
- For FTO specifically, separate **live patents** (in force, infringement risk) from **expired or abandoned** (free to use) and flag claims that may read on the product.
- End with a **strategic recommendation** tied to the stated goal.

### Must Not
- Search by keywords alone — patents use idiosyncratic terminology and class codes are essential.
- Equate "zero search results" with "whitespace." Empty results usually mean a bad query, wrong classes, or a dead area.
- Ignore non-patent prior art (publications, products) when the goal is whitespace — a publication can block patentability even with no patent on file.
- Conflate a patent existing with a patent being infringed; infringement is a claim-by-claim analysis, not a topic match.
- Treat expired patents as a risk in FTO — they are free to practice.
- Skip jurisdiction: a patent enforceable in one country says nothing about freedom in another.

---

## Instructions

1. **Define scope precisely.** State the technology in plain and technical terms. List the features/mechanisms in-scope and the boundary cases excluded. For FTO, list the specific product features that could read on a claim.
2. **Identify patent classifications.** Find the relevant CPC/IPC (and USPC where useful) classes and subclasses for the technology. Use a seed patent or two to read off their assigned classes, then expand. Class codes are the backbone of a defensible search.
3. **Build the search query.** Combine classification codes with terms-and-connectors search: claim-language terms, synonyms, acronyms, and applicant/assignee names. Specify whether each term searches claims, abstract, title, or full text. Include and exclude terms to control noise.
4. **Select databases and run plan.** Choose databases for the jurisdictions in scope and note their coverage (e.g., Espacenet for global families, USPTO for US specifics, Google Patents for full-text and citation graph). State the order: classification browse → query refinement → retrieval.
5. **Screen for relevance.** Apply inclusion criteria to the raw hits. Tag each as on-point, adjacent, or noise. For FTO, additionally tag live vs. expired/abandoned and whether claims plausibly read on the product feature (flag for attorney review — not a clearance opinion).
6. **Cluster the set.** Group by assignee (who owns the space), by technology sub-area (what is being claimed), and by filing date (when activity peaked or accelerated). Build a density picture across these axes.
7. **Read density and whitespace.** Identify high-density clusters (crowded — design-around territory or licensing targets) and low-density regions. For each low-density region, test whether it is true whitespace (workable, on-market, simply unclaimed) or dead space (unworkable, off-market, or covered by non-patent means). Cite the reasoning.
8. **Produce the strategic recommendation.** Tie the read to the goal:
   - **FTO:** which live patents pose risk, which features need design-around or clearance opinion, residual risk.
   - **Competitive intelligence:** where each competitor is investing, gaps and overlaps, likely roadmap signals.
   - **Whitespace:** which low-density areas are worth claiming, with the patentability and commercial rationale.
   - **Acquisition screening:** portfolio strength, coverage breadth, and gaps relative to the target's product.

---

## False-Positive Prevention

1. **Keyword-only search.** Searching by terms alone and missing class-coded prior art that uses different words. Always anchor on CPC/IPC classes.
2. **Empty-results-as-whitespace.** Reading zero hits as opportunity when it usually means a broken query, wrong classes, or a dead area. Validate the query against known seed patents first.
3. **Whitespace/dead-space confusion.** Recommending a low-density area without testing why it is empty. Some spaces are empty because they do not work or have no market.
4. **Non-patent-art blindness.** For whitespace, ignoring publications and products that can defeat patentability even with no patent filed.
5. **Topic-match-as-infringement.** Treating a patent on the same topic as an infringement risk without claim-level reading. Infringement is claim-by-claim; flag for attorney analysis rather than asserting it.
6. **Expired-patent panic.** Flagging expired patents as FTO risk. Expired patents are free to practice; they matter only as prior art for your own filings.
7. **Jurisdiction collapse.** Mixing patents from multiple jurisdictions without tracking where each is enforceable. FTO is per-jurisdiction.
8. **Assignee-name naivete.** Missing patents held under subsidiaries, acquired entities, or assignment changes. Track assignee variants and reassignments.
9. **Stale family confusion.** Counting members of one patent family as separate patents, inflating density. De-duplicate by family.
10. **Goal-free clustering.** Producing clusters with no recommendation. The clusters exist to answer the stated goal; end with the answer.

---

## Output Format

```
# PATENT LANDSCAPE SCAN — [technology area]
Goal: [FTO / competitive intelligence / whitespace / acquisition screening]
Jurisdictions: [...] | Time horizon: [...]

## Scope
- In-scope features / mechanisms: [...]
- Excluded boundary cases: [...]
- (FTO) Product features that could read on a claim: [...]

## Classification
| Class system | Class / subclass | What it covers |
|--------------|------------------|----------------|
| CPC          | [...]            | [...]          |
| IPC          | [...]            | [...]          |
| USPC         | [...]            | [...]          |
Seed patents used to derive classes: [...]

## Search query
- Classification terms: [...]
- Claim-language terms (with synonyms/acronyms): [...]
- Field restrictions: [claims / abstract / full text]
- Include / exclude terms: [...]

## Databases
| Database | Jurisdiction coverage | Use |
|----------|-----------------------|-----|
| [...]    | [...]                 | [...] |

## Screening result
| Patent / family | Assignee | Sub-area | Filing date | Status | Relevance | (FTO) reads on feature? |
|-----------------|----------|----------|-------------|--------|-----------|-------------------------|
| [...]           | [...]    | [...]    | [...]       | live / expired / abandoned | on-point / adjacent / noise | flag for attorney |

## Clusters and density
- By assignee: [who owns what]
- By sub-area: [what is densely vs. sparsely claimed]
- By time: [when activity peaked / accelerated]
- High-density (crowded): [...]
- Low-density regions: [...]

## Whitespace vs. dead space
| Low-density region | True whitespace or dead space? | Reasoning |
|--------------------|--------------------------------|-----------|
| [...]              | whitespace                     | workable + on-market + unclaimed |
| [...]              | dead space                     | [unworkable / off-market / covered otherwise] |

## Strategic recommendation
[Tied to the goal: FTO risk + design-around; or competitor investment map; or whitespace to claim with rationale; or portfolio strength assessment.]
```

---

## Verification

- [ ] Scope defined in plain and technical terms, with exclusions.
- [ ] Relevant CPC/IPC (and USPC) classes identified from seed patents.
- [ ] Query combines class codes with claim-language terms, synonyms, and field restrictions.
- [ ] Databases selected for the in-scope jurisdictions with coverage noted.
- [ ] Hits screened with inclusion criteria; relevance tagged.
- [ ] Set clustered by assignee, sub-area, and filing date; patent families de-duplicated.
- [ ] Low-density regions tested for whitespace vs. dead space with reasoning.
- [ ] (FTO) Live patents separated from expired/abandoned; potential claim reads flagged for attorney review, not asserted.
- [ ] Jurisdiction tracked per patent.
- [ ] Strategic recommendation tied to the stated goal.
- [ ] No keyword-only search; no empty-results-as-whitespace.
- [ ] No topic-match presented as infringement.
