---
title: "Content Research for Writing"
category: business-strategy/research
description: "Research a topic to prepare for writing an article, presentation, or report — gathering source-cited statistics, expert perspectives, examples, and counter-arguments, with credibility assessment and strict separation of evidence from inference."
techniques:
  - ST-01
  - RT-02
  - DS-02
  - RT-05
  - QA-01
difficulty: intermediate
tags:
  - research
  - content-research
  - writing-preparation
  - source-evaluation
  - web-research
updated: "2026-06-07"
related_prompts:
  - domain-business-strategy/research/research_industry_trends.md
  - domain-business-strategy/research/research_company_deep_dive.md
  - domain-business-strategy/organization/organization_content_audit.md
---

# Content Research for Writing

**Objective:** Gather and organize source material for a piece of writing — statistics, expert perspectives, examples, and counter-arguments — so it's ready for synthesis, with every claim sourced, credibility assessed, and counter-evidence included to keep the research honest.

**When to use:**
- Preparing to write an article, presentation, report, or speech.
- Building a sourced evidence base behind a thesis or argument.
- Thought-leadership content that must withstand scrutiny.

**When NOT to use:**
- You're drafting/editing prose, not gathering sources.
- The topic needs original data collection (surveys, interviews) rather than secondary research.
- You want a one-sided list of supporting points — this prompt deliberately includes counter-arguments.

**Audience:** Writers, content marketers, analysts, communications and PR professionals.

---

## Inputs / Context

The user should supply (or the research should flag what is missing):

1. **Topic** and **content type** (article, presentation, report, speech).
2. **Audience** for the final piece.
3. **Angle/thesis** the research will support — stated explicitly so counter-evidence can be sought.
4. **Quantities** wanted per section (e.g., how many statistics, quotes, examples).
5. **Available sources** the researcher can reach, and any recency or source-type constraints.

---

## Constraints

### Must
- **Cite a source for every statistic, quote, and example** — link, source name, and publication date; link statistics to the **original study/data**, not a secondary article.
- **Never invent** statistics, quotes, experts, studies, or sources. If something can't be found, say so.
- Prioritize **primary and high-credibility sources** (peer-reviewed research, official data, named experts) over opinion blogs and content farms.
- Include **counter-arguments and at least one perspective that challenges the thesis** — do not cherry-pick.
- For each major source, give a **credibility assessment** (rating, potential bias/conflict, primary vs. synthesis).
- Note paywalled sources (user may not verify) and flag any claim found in only one source.

### Must Not
- Fabricate or paraphrase a quote so it reads as verbatim when it isn't.
- Present a frequently-cited statistic as solid when its original source is weak (flag it instead).
- Strip out context that complicates the thesis.
- Treat a secondary article's restatement of a number as the source of record.

---

## Instructions

1. **Restate the brief.** Topic, content type, audience, and thesis; the quantities per section.
2. **Gather key statistics.** Most relevant data points; for each: the stat, what it means, original source, date, URL, and methodology/sample if it affects credibility.
3. **Collect expert perspectives.** Verbatim quotes from named, credentialed experts with source and date; include at least one that challenges the thesis.
4. **Find case studies/examples.** Concrete, recent (prefer past 2 years) examples that illustrate the points, each sourced.
5. **Develop counter-arguments.** The strongest opposing case, who makes it, and how proponents of the thesis typically respond.
6. **Assess source quality.** Per major source: credibility (High/Med/Low), bias/conflict, primary vs. synthesis; flag paywalls and single-source claims.
7. **Add story hooks and gaps.** A few compelling openings/surprising findings, then what couldn't be found that would strengthen the piece.
8. **Verify (verification step).** Re-read: is every stat/quote sourced and verifiable? Any invented or unattributed claim? Are statistics linked to originals, not secondary coverage? Is counter-evidence genuinely included?

---

## False-Positive Prevention

❌ **DON'T:**
- Cite a statistic to a news article when the number comes from an underlying study.
- Invent a plausible expert quote or attribute a real-sounding name without a source.
- Present a viral stat as authoritative without checking its origin.
- Omit counter-arguments to make the thesis look stronger.
- Let a single blog post stand in for evidence.

✅ **DO:**
- Link statistics to the original study/data with date and methodology notes.
- Quote experts verbatim with name, credentials, source, and date.
- Flag weak-origin stats, paywalls, and single-source claims explicitly.
- Include at least one credible challenge to the thesis.
- Separate evidence (sourced) from inference (your synthesis) and name research gaps.

---

## Output Format

```
# Content Research: [Topic]
*Content type: [...] | Audience: [...] | Thesis: [...]*

## Key Statistics
- [Statistic] — meaning; [original source], [date], [URL]; methodology/sample: [...]

## Expert Perspectives
- "[Verbatim quote]" — [Name], [credentials], [source], [date]
- (include ≥1 that challenges the thesis)

## Case Studies / Examples
- [What happened] — why it matters; [source, date]

## Counter-Arguments
- [Strongest opposing argument] — who makes it; typical rebuttal

## Source Quality Assessment
| Source | Credibility | Bias/Conflict | Primary or Synthesis | Notes (paywall, single-source) |
|--------|-------------|---------------|----------------------|--------------------------------|
| ...    | H/M/L       | ...           | ...                  | ...                            |

## Story Hooks
- [Surprising fact / opening angle]

## Gaps & Follow-Up
- [What couldn't be found; additional research/interviews that would help]
```

---

## Example Output

```
# Content Research: Remote Work and Team Productivity (placeholder topic)
*Content type: article | Audience: people-ops leaders | Thesis: hybrid models outperform fully-remote on collaboration*

## Key Statistics
- A [year] meta-analysis (placeholder) reports a moderate effect of co-located days on cross-team project throughput — [original study, journal, date, DOI/URL]; sample/methodology: [N teams, observational], which limits causal claims.
  (Note: cite the study, not the magazine that summarized it.)
- [Survey] of knowledge workers found X% prefer hybrid (placeholder) — [survey org report, date, URL]; self-reported, so attitudinal not behavioral.

## Expert Perspectives
- "[Verbatim quote on coordination cost]" — [Researcher Name], [affiliation], [talk/paper, date].
- Challenge to thesis: "[Verbatim quote arguing fully-remote can match hybrid with the right async practices]" — [Practitioner Name], [source, date].

## Case Studies / Examples
- [Company, placeholder] shifted to two anchor days and reported faster launch cycles — [their engineering blog, date] (note: company-authored, treat as claim).

## Counter-Arguments
- Strongest opposition: hybrid gains are confounded by selection (high-performing teams choose hybrid). Made by [skeptic, source]. Typical rebuttal: cite controlled pilots that randomize anchor days.

## Source Quality Assessment
| Source | Credibility | Bias/Conflict | Primary or Synthesis | Notes |
|--------|-------------|---------------|----------------------|-------|
| Meta-analysis | High | none apparent | Primary | behind paywall — abstract only |
| Company blog | Low–Med | self-promotional | Primary (self-report) | marketing context |
| Survey report | Medium | vendor-sponsored | Primary | self-reported attitudes |

## Story Hooks
- The counterintuitive finding that *fewer* office days correlated with higher reported focus — a tension worth opening on.

## Gaps & Follow-Up
- No randomized study found isolating anchor-day effects — flag this limitation in the piece.
- An interview with a people-ops leader who reversed a remote policy would add a primary voice.
```

---

## Verification

- [ ] Every statistic, quote, and example has a dated source.
- [ ] Statistics link to the original study/data, not secondary coverage.
- [ ] No invented stats, quotes, experts, or studies.
- [ ] At least one credible challenge to the thesis is included.
- [ ] Each major source has a credibility assessment; paywalls and single-source claims flagged.
- [ ] Weak-origin "viral" stats are flagged, not asserted.
- [ ] Evidence is separated from the researcher's inference; research gaps named.

---

## Techniques Used

- **ST-01 (Clear Objective Statement):** Frames the task as assembling a sourced, balanced evidence base for writing.
- **RT-02 (Multi-Dimensional Analysis Framework):** Organizes research across statistics, expert views, examples, and counter-arguments.
- **DS-02 (Evidence-Based Decision Making):** Requires sourced, original-data citations and forbids fabrication.
- **RT-05 (Evidence-Based Reasoning):** Conclusions and hooks must follow from cited evidence, with inference labeled.
- **QA-01 (Self-Critique Triggers):** Final verification audits for unsourced claims, cherry-picking, and secondary-source citation.

---

## Related Prompts

- `domain-business-strategy/research/research_industry_trends.md` — Research broader trends that contextualize the piece.
- `domain-business-strategy/research/research_company_deep_dive.md` — Profile a specific company referenced in the writing.
- `domain-business-strategy/organization/organization_content_audit.md` — Organize and maintain the content you produce.
