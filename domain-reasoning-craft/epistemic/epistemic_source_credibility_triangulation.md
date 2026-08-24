---
title: "Source Credibility Triangulation — Compare Sources on Credibility, Not Content"
category: reasoning-craft/epistemic
description: "Compare three or more sources on credibility dimensions — track record on this topic, methodological transparency, conflict-of-interest disclosure, citation patterns, expertise match — to surface where credibility differs and where it converges, independent of what the sources actually claim. Counters the failure mode of weighting sources by how confident or articulate they sound, and of conflating agreement-on-content with independent-credibility."
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
  - epistemic
  - source-credibility
  - triangulation
  - source-evaluation
  - critical-appraisal
updated: "2026-05-21"
reasoning:
  styles: [evaluative, comparative, diagnostic]
  stakes: variable
  horizon: variable
  uncertainty: ambiguity
  evidence_quality: variable
  domain_complexity: cross_domain
  collaboration: solo
  output_format: credibility_profile_plus_ranking
  user_role: [researcher, analyst, journalist, individual, executive]
  mode: [audit, diagnose]
related_prompts:
  - domain-reasoning-craft/epistemic/epistemic_evidence_quality_score.md
  - domain-research-academic/research_source_triangulation.md
  - domain-research-academic/research_evidence_map.md
---

# Source Credibility Triangulation

**Objective:** Compare three or more sources on credibility — independent of the content of their claims. For each source, profile its track record on this specific topic, methodological transparency, conflict-of-interest disclosure, citation/sourcing patterns, and expertise match to the question. Then compare across sources to surface where credibility differs and where it converges. Output per-source credibility profiles and a cross-source ranking with caveats. This complements `research_source_triangulation.md` (which compares what sources *say*); here the object is the *credibility of the sources themselves*.

**When to use:**
- Several sources make related claims and you need to decide whose credibility to weight more heavily before even comparing content.
- A source is articulate and confident but you're unsure whether its credibility on *this* topic justifies the weight you're tempted to give it.
- Building a research base and assigning credibility tiers to sources.
- A consensus exists but you suspect it's an echo (sources citing each other) rather than independent corroboration.

**When NOT to use:**
- You want to cross-check whether sources *agree on the facts* — use `research_source_triangulation.md`.
- You're scoring the quality of a single evidence item, not comparing sources — use `epistemic_evidence_quality_score.md`.
- There's only one source; triangulation requires three or more.

**Audience:** Researchers, analysts, journalists, and individuals deciding whose account to trust on a contested topic.

---

## Inputs / Context

1. **The topic / question.** Credibility is topic-specific; an authority in one area may have none here.
2. **The sources.** Three or more, each identified with what's known about them (who, affiliation, funding, track record).
3. **The claims they make (briefly).** Needed only to assess expertise match and to detect echo, not to judge who's right.
4. **What's known about their relationships.** Do they cite each other, share funders, or come from the same institution?

---

## Credibility dimensions

- **Track record on this topic** — has the source been right/careful on this specific subject before? (Not general fame.)
- **Methodological transparency** — are the methods, data, and reasoning available for inspection, or is it "trust me"?
- **Conflict-of-interest disclosure** — independence from parties with a stake; whether conflicts are disclosed.
- **Citation / sourcing pattern** — does the source ground claims in checkable references, or assert? Does it cite primary sources or only secondary?
- **Expertise match** — is the source's expertise actually on-domain for this question, or adjacent/borrowed?

---

## Constraints

### Must
- Profile **each source separately** on every dimension before comparing.
- Judge credibility **independent of whether you agree with the source's conclusion**. A credible source can be wrong; a low-credibility source can be right.
- Run an **independence audit**: determine whether apparent agreement among sources is genuine corroboration or an echo chamber (shared origin, mutual citation, common funder).
- Produce a **cross-source credibility ranking** with explicit caveats, noting where the ranking is close or uncertain.
- Keep credibility **topic-scoped**: rate expertise and track record for *this* question, not the source's general reputation.

### Must Not
- Rank sources by how confident, fluent, or authoritative they *sound*. Tone is not credibility.
- Conflate agreement-on-content with independent credibility. Five sources echoing one origin is one source.
- Let your prior agreement with a source's conclusion inflate its credibility score (a credibility halo).
- Treat general prestige as topic-specific credibility. A celebrated generalist may be low-credibility on a narrow technical question.
- Produce a ranking with false precision; credibility comparisons are coarse and often have ties.

---

## Instructions

### Step 1 — Fix the topic scope
State the specific question. All credibility judgments are relative to it.

### Step 2 — Profile each source
For each source, score/characterize every dimension with a one-line justification. Use a coarse scale (high / medium / low) — false precision is worse than honest coarseness.

### Step 3 — Expertise-match check
For each source, confirm whether its expertise is on-domain for this question or borrowed from an adjacent field. Borrowed expertise is a discount, not a disqualifier.

### Step 4 — Independence audit
Map relationships: shared funders, mutual citations, common institutional origin. Determine whether the sources are independent or whether several reduce to one. Note any echo.

### Step 5 — Cross-source comparison
Lay the profiles side by side. Surface where credibility clearly differs and where it converges. Flag any source that's high on most dimensions but fatally low on one (e.g., strong track record but undisclosed major conflict).

### Step 6 — Ranking with caveats
Produce a coarse credibility ranking. State caveats: which comparisons are close, which depend on unknowns, where independence is uncertain.

### Step 7 — Decoupled reminder
Close by restating that this ranks *credibility*, not *correctness* — the ranking informs how to weight sources, after which content still has to be checked (hand to `research_source_triangulation.md`).

---

## False-Positive Prevention

1. **Confidence-as-credibility.** Weighting the source that sounds most certain. Fluency and confidence are independent of credibility; score the dimensions, not the delivery.
2. **Echo mistaken for corroboration.** Treating multiple sources that trace to one origin as independent confirmation. The independence audit exists to catch this.
3. **Credibility halo.** Inflating the credibility of a source whose conclusion you already favor. Score credibility before consulting your agreement.
4. **Prestige transfer.** Importing a source's general fame into topic-specific credibility. Scope every judgment to the question.
5. **Single-dimension dominance.** Ranking on track record alone while ignoring a disqualifying conflict of interest. Weigh all dimensions and flag fatal lows.
6. **Credibility/correctness conflation.** Concluding the most credible source is right. Credibility sets the weight; correctness still requires checking content.
7. **False precision in ranking.** Presenting a confident strict ordering when several sources are roughly tied. Allow ties and state uncertainty.
8. **Disqualifying low credibility entirely.** A low-credibility source can still be correct; the output adjusts weight, it doesn't silence a source.

---

## Output Format

```
# Source credibility triangulation — [topic]

## Question scope
[The specific question all credibility is judged against]

## Per-source profiles
### Source A: [identifier]
| Dimension                  | Rating (H/M/L) | Justification (1 line) |
|----------------------------|----------------|------------------------|
| Track record on this topic |                |                        |
| Methodological transparency|                |                        |
| Conflict-of-interest       |                |                        |
| Citation / sourcing        |                |                        |
| Expertise match            |                |                        |

(Repeat for each source.)

## Independence audit
| Relationship checked        | Finding                          |
|-----------------------------|----------------------------------|
| Shared funders              |                                  |
| Mutual citation             |                                  |
| Common institutional origin |                                  |
- Echo detected? [yes/no — which sources reduce to one]

## Cross-source comparison
[Where credibility clearly differs; where it converges; any source high-but-fatally-flawed]

## Credibility ranking (coarse, with caveats)
1. [Source] — [why]
2. [Source] — [why]  (close to #1; depends on [unknown])
3. [Source] — [why]

## Reminder
This ranks credibility, not correctness. Weight sources accordingly, then check content (→ research_source_triangulation.md).
```

---

## Verification

- [ ] Topic scope fixed before any credibility judgment.
- [ ] Each source profiled on all dimensions independently.
- [ ] Expertise-match checked per source (on-domain vs borrowed).
- [ ] Independence audit performed; echo flagged if present.
- [ ] Cross-source comparison surfaces both divergence and convergence.
- [ ] Ranking is coarse, with explicit caveats and allowed ties.
- [ ] Credibility judged independent of agreement with conclusions.
- [ ] Closing reminder separates credibility from correctness.
