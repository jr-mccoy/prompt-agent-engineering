---
title: "Legal Research Plan — Map the Authorities Before Opening Westlaw or Lexis"
category: specialized-fields/legal
description: "Plan legal research before paid-database time: analyze jurisdiction and the relevant courts, identify governing statutes and regulations, separate controlling from persuasive case law, locate secondary sources and agency interpretations, check for recent amendments and pending legislation, and build a sequenced search strategy with starting citations and search terms. Counters the failure of expensive, unstructured database searching that misses controlling authority."
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
  - legal
  - legal-research
  - case-law
  - jurisdiction
  - search-strategy
updated: "2026-06-18"
reasoning:
  styles: [analytic, systematic, hierarchical, decomposition]
  stakes: high
  horizon: days
  uncertainty: ambiguity
  evidence_quality: rich
  domain_complexity: regulated
  collaboration: solo_or_team
  output_format: structured
  user_role: [attorney, paralegal, law_student, individual]
  mode: [plan, synthesize]
related_prompts:
  - domain-research-academic/research_literature_review_plan.md
  - domain-business-strategy/research/technical_due_diligence_plan.md
  - domain-specialized-fields/ip/patent_landscape_scan.md
---

# Legal Research Plan

**Objective:** Produce a sequenced legal research plan before any paid-database time is spent. The plan analyzes jurisdiction and the relevant courts, identifies the governing statutes and regulations, separates controlling from merely persuasive case law, locates secondary sources and agency interpretations, checks for recent amendments and pending legislation, and lays out a search strategy with concrete starting citations, search terms, and an order of operations. The goal is to walk into Westlaw or Lexis already knowing the hierarchy of authority and the questions to resolve — not to discover the structure on the meter.

**When to use:**
- Beginning research on a discrete legal question where the controlling authority is not already known.
- Scoping a memo, brief, or opinion before drilling into sources.
- Researching across an unfamiliar jurisdiction or a multi-jurisdiction question.
- A non-lawyer researching their own legal situation rigorously enough to brief counsel.

**When NOT to use:**
- The controlling authority is already known and you only need to read or cite-check it.
- The question is a settled procedural matter answered by a single rule.
- You need legal advice rather than a research plan — this prompt plans research, it does not opine on outcomes.

**Audience:** Attorneys, paralegals, law students, in-house counsel, and sophisticated non-lawyers researching their own legal questions to a defensible standard.

---

## Inputs / Context

1. **The legal question.** As specific as possible — the issue, the parties, the operative facts that matter legally.
2. **Jurisdiction.** Country, state, locality; the forum if a dispute is anticipated.
3. **Posture.** Transactional, litigation, advisory, compliance — this shapes what authority matters.
4. **Known facts.** The facts that trigger or fit the legal elements.
5. **What is already known.** Any statutes, cases, or sources already in hand.
6. **Deadline and depth.** Quick issue scan vs. memo-grade vs. brief-grade research.

---

## Constraints

### Must
- Pin **jurisdiction precisely** and identify which court(s) bind: trial, intermediate appellate, highest court, and any federal/state interaction.
- Build the **authority hierarchy**: constitutional → statutory → regulatory → case law → secondary, with controlling distinguished from persuasive at each level.
- Separate **controlling authority** (binds this forum) from **persuasive authority** (informs but does not bind) explicitly. A persuasive case from another circuit is not a substitute for controlling precedent.
- Identify **governing statutes and regulations** by citation, with the operative sections, not just the title.
- Locate **secondary sources** appropriate to the question: treatises, restatements, law review articles, practice guides, ALR annotations.
- Check **currency**: recent amendments, pending legislation, and whether key cases are still good law (the plan must flag the need to validate/Shepardize, even before doing it).
- Identify relevant **agency interpretations** where an administrative body governs (guidance, opinion letters, adjudications, rulemakings).
- Produce a **search strategy** per source type, with starting citations, Boolean/terms-and-connectors search strings, and an order of operations that goes from cheap orientation to targeted retrieval.

### Must Not
- Treat all case law as equal; persuasive authority dressed as controlling is a research error.
- Skip secondary sources to "go straight to primary." Secondary sources orient fastest and cite the primary authority efficiently.
- Assume a statute or case is current without flagging the need to validate it.
- Ignore the regulatory and agency layer where an administrative body actually governs the question.
- Plan to start with the most expensive targeted search before cheap orientation has narrowed the question.
- Confuse a research plan with a legal conclusion — the plan identifies where the answer lives, it does not assert the answer.

---

## Instructions

1. **Frame the legal question and elements.** Restate the question as the legal issue, then break it into the elements or sub-issues that must each be researched. Identify which facts are legally operative.
2. **Analyze jurisdiction and forum.** Determine the governing jurisdiction and which courts bind it. Map federal/state interaction (preemption, diversity, parallel bodies of law). State which forum's law controls and why.
3. **Build the authority hierarchy.** For this question, lay out the levels of authority that could govern — constitutional provisions, statutes, regulations, case law, secondary sources — and which level is likely to be dispositive.
4. **Identify governing statutes and regulations.** Cite the specific statutes and regulatory provisions, with the operative sections. Note any definitional sections, exceptions, and cross-references that matter.
5. **Separate controlling from persuasive case law.** Identify the controlling precedent in the forum (highest court, then intermediate appellate, then trial-level as applicable). Separately note persuasive authority (other jurisdictions, dicta, lower courts) and flag it as such. Identify any circuit/jurisdiction splits.
6. **Locate secondary sources and agency interpretations.** Name the treatises, restatements, practice guides, and law review pieces that map this area, and the agency guidance, opinion letters, or adjudications where an administrative body governs.
7. **Check currency.** Identify what must be validated for currency: statutory amendments, pending legislation, and whether key cases remain good law (note the need to Shepardize/KeyCite before relying). Flag any recently changed or unsettled area.
8. **Build the search strategy.** For each source type, specify: starting citations (the seeds), search strings (terms and connectors / Boolean, with synonyms and field restrictions), databases or reporters, and the order of operations — cheap orientation (secondary sources, headnotes, statutory annotations) first, targeted primary retrieval second, validation last.
9. **Define the stopping point.** State what "researched enough" looks like for this question and depth: controlling authority located and validated, the elements each addressed, splits and counterarguments identified, and currency confirmed.

---

## False-Positive Prevention

1. **Persuasive-as-controlling.** Citing an on-point case from another jurisdiction as if it binds the forum. Always tag each authority controlling vs. persuasive.
2. **Skip-the-secondary error.** Diving into primary sources without orientation, missing the treatise or annotation that would have mapped the area in minutes and cited the controlling authority directly.
3. **Stale-authority reliance.** Building on a statute or case without flagging that it must be validated for currency. Good law today may be reversed or amended.
4. **Regulatory-layer blindness.** Researching only statutes and cases where an agency's regulations and interpretations actually govern day-to-day.
5. **Jurisdiction slippage.** Mixing authority from multiple jurisdictions without keeping straight which controls the forum.
6. **Element gaps.** Researching the headline issue while leaving a required element or affirmative defense un-researched.
7. **Split omission.** Failing to flag a circuit or jurisdiction split, leaving the analysis falsely settled.
8. **Expensive-first searching.** Starting with broad full-text database searches before cheap orientation narrows the terms — burning database time and missing structure.
9. **Plan-as-opinion.** Drifting from "here is where the answer lives" into asserting the legal conclusion. The plan locates authority; it does not adjudicate.
10. **Search-term naivete.** Generic keyword strings with no synonyms, terms of art, field restrictions, or connectors — returning noise instead of authority.

---

## Output Format

```
# LEGAL RESEARCH PLAN — [question]
Jurisdiction / forum: [...] | Posture: [transactional / litigation / advisory / compliance]
Depth: [issue scan / memo-grade / brief-grade]

## Legal question and elements
- Issue: [...]
- Elements / sub-issues to research:
  1. [...]
  2. [...]
- Legally operative facts: [...]

## Jurisdiction and binding courts
- Governing jurisdiction: [...]
- Binding courts (highest → trial): [...]
- Federal/state interaction (preemption / diversity / parallel law): [...]

## Authority hierarchy (this question)
| Level | Likely-relevant authority | Controlling or persuasive | Likely dispositive? |
|-------|---------------------------|---------------------------|---------------------|
| Constitutional | [...]            | [...]                     | [...]               |
| Statutory      | [cite + §]       | controlling               | [...]               |
| Regulatory     | [cite]           | controlling               | [...]               |
| Case law       | [cite]           | controlling / persuasive  | [...]               |
| Secondary      | [treatise / ALR] | persuasive (orientation)  | n/a                 |

## Governing statutes and regulations
| Citation | Operative section | Definitions / exceptions / cross-refs |
|----------|-------------------|----------------------------------------|
| [...]    | [§]               | [...]                                  |

## Case law
- Controlling precedent: [cite — holding relevant to this question]
- Persuasive authority: [cite — and why persuasive only]
- Splits / unsettled: [...]

## Secondary sources and agency interpretations
- Treatises / restatements / practice guides: [...]
- Law review / ALR: [...]
- Agency guidance / opinion letters / adjudications: [...]

## Currency to validate
- Statutory amendments / pending legislation: [...]
- Cases to Shepardize/KeyCite before relying: [...]
- Recently changed or unsettled areas: [...]

## Search strategy (order of operations)
| Step | Source type | Database / reporter | Starting citation(s) | Search string |
|------|-------------|---------------------|----------------------|---------------|
| 1 (orient) | secondary | [...]           | [...]                | [...]         |
| 2 (statutory) | annotated code | [...]      | [...]                | [...]         |
| 3 (primary cases) | [...]      | [...]           | [...]                | [terms & connectors] |
| 4 (validate) | citator      | [...]           | [...]                | n/a           |

## Stopping point
[What "researched enough" means for this question and depth.]
```

---

## Verification

- [ ] Legal question decomposed into elements / sub-issues.
- [ ] Jurisdiction pinned and binding courts identified.
- [ ] Authority hierarchy built with controlling vs. persuasive tagged at each level.
- [ ] Governing statutes/regulations cited with operative sections.
- [ ] Controlling precedent separated from persuasive; splits flagged.
- [ ] Secondary sources and agency interpretations located.
- [ ] Currency validation needs flagged (amendments, pending legislation, Shepardize/KeyCite).
- [ ] Search strategy ordered cheap-orientation-first with concrete seeds and search strings.
- [ ] Stopping point defined.
- [ ] No persuasive authority presented as controlling.
- [ ] No legal conclusion asserted in place of a research plan.
