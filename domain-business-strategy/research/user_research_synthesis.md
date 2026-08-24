---
title: "User Research Synthesis — Turn 10–30 Interviews into Themes, Tensions, Surprises, and Decisions"
category: business-strategy/research
description: "Synthesize a body of primary user interviews into traceable themes, contradictions, segment patterns, surprises, and concrete decisions. Runs open coding then focused coding, surfaces tensions where users contradict themselves or each other, ties every theme to quote IDs, and ends in product/strategy/messaging decisions. Counters the failure of cherry-picked quotes confirming what the team already believed."
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
  - user-research
  - qualitative-synthesis
  - thematic-coding
  - customer-discovery
  - product-decisions
updated: "2026-06-18"
reasoning:
  styles: [inductive, thematic, dialectical, pattern_matching]
  stakes: moderate
  horizon: days
  uncertainty: ambiguity
  evidence_quality: moderate
  domain_complexity: single_domain
  collaboration: small_team
  output_format: [structured, narrative]
  user_role: [pm, designer, researcher, founder, analyst]
  mode: [synthesize, diagnose, decide]
related_prompts:
  - domain-research-academic/research_secondary_source_synthesis.md
  - domain-business-strategy/research/competitor_teardown.md
  - domain-research-academic/research_evidence_map.md
---

# User Research Synthesis

**Objective:** Synthesize 10–30 primary user interviews into an analysis the team can act on: themes that recur across interviews, tensions where users contradict themselves or each other, patterns by segment, surprises the team did not expect, and decisions the findings imply. Every theme is traceable to specific quotes, so the synthesis can be audited rather than trusted on assertion. This is for primary user research — interviews, sessions, calls — and is distinct from `research_secondary_source_synthesis.md`, which is for published sources.

The dominant failure of user research is confirmation: the team mines transcripts for quotes that support the existing plan and calls it validation. This prompt counters that by coding the data before interpreting it, by surfacing contradictions deliberately, and by separating what users said from what the team wants to hear.

**When to use:**
- After running a batch of user/customer interviews and needing to convert them into direction.
- Synthesizing discovery interviews into product, positioning, or messaging decisions.
- Re-analyzing past interviews when a new question arises.
- Preparing a research readout for stakeholders who weren't in the interviews.

**When NOT to use:**
- You have fewer than ~8 interviews — patterns will be unstable; treat findings as hypotheses, not synthesis.
- The source is published literature, not primary interviews — use `research_secondary_source_synthesis.md`.
- You need a quantitative survey analysis — coding-based synthesis is for qualitative data.

**Audience:** Product managers, designers, user researchers, founders, and strategy analysts turning interview data into decisions.

---

## Inputs / Context

1. **The interviews.** Transcripts or structured summaries, ideally with a stable ID per interview (and per quote where possible).
2. **The research question.** What the interviews were meant to answer.
3. **Participant metadata.** Segment, role, tenure, or other dimensions to break patterns by.
4. **The team's priors.** What the team currently believes — stated up front so confirmation can be checked against it.
5. **The decisions on the table.** What product/strategy/messaging choices this research is meant to inform.

---

## Constraints

### Must
- **Code before interpreting.** Run open coding (tags emerging from the data) then focused coding (themes recurring across interviews) before drawing conclusions.
- Tie every theme to **quote IDs** — the evidence trail. A theme with no traceable quotes is an assertion.
- Report **prevalence honestly**: how many of N interviews support each theme. "Users want X" must mean a counted majority, not two vivid quotes.
- **Surface tensions** deliberately: places where the same user contradicts themselves, or where users disagree with each other. Present both sides with quotes.
- Break patterns by **segment** where the data supports it, and flag where a theme is segment-specific rather than universal.
- Separate **surprises** (findings that contradict the team's priors) from confirmations, and give surprises at least equal weight.
- End in **decisions**: what each finding implies for product, strategy, or messaging, with the confidence level.

### Must Not
- Cherry-pick quotes that confirm the existing plan and omit disconfirming ones.
- Report "users said" without a count, smuggling a minority view in as consensus.
- Collapse genuine tensions into a single tidy theme. The contradiction is often the most useful finding.
- Treat one articulate participant's view as representative.
- Confuse what users say they want with what their behavior or stories reveal — note the gap.
- Produce themes with no decision attached; synthesis exists to inform action.

---

## Instructions

1. **State the question and the priors.** Restate the research question and write down what the team currently believes. This is the baseline confirmation will be checked against.
2. **Open code.** Pass through the data and tag everything notable with descriptive codes that emerge from the data, not from a pre-built framework. Keep codes close to the participant's own language. Record the interview/quote ID for each tagged passage.
3. **Focused code.** Group the open codes into candidate themes — codes that recur across multiple interviews. Promote a candidate to a theme only when it appears in several interviews; note the count.
4. **Count prevalence.** For each theme, count how many of the N interviews support it and characterize intensity (mentioned in passing vs. emphatic). Report prevalence as "k of N."
5. **Surface tensions.** Find contradictions: within a single interview (user says X then reveals Y) and across interviews (segment A wants X, segment B wants the opposite). Present each tension with quotes from both sides. Do not resolve prematurely.
6. **Break by segment.** For each major theme and tension, check whether it splits by segment, role, tenure, or other metadata. Flag themes that are segment-specific rather than universal.
7. **Separate surprises from confirmations.** Sort findings into: confirmed a prior, contradicted a prior, or revealed something not on the radar. Give surprises and contradictions explicit airtime — they carry the most information.
8. **Note the say-do gap.** Where participants stated a preference that their behavior, past choices, or stories contradict, flag it. Stated preference and revealed preference often diverge.
9. **Translate to decisions.** For each significant theme, tension, and surprise, state what it implies for the decisions on the table — product, strategy, or messaging — with a confidence level (high / medium / low) grounded in prevalence and consistency.

---

## False-Positive Prevention

1. **Confirmation mining.** Reading transcripts to find support for the existing plan. State priors up front and force a surprises/contradictions section to counter it.
2. **Vivid-quote inflation.** Elevating two memorable quotes to "users want X." Always report k-of-N prevalence.
3. **Tension-collapse.** Smoothing a real contradiction into one clean theme. Keep tensions as tensions; they are often the finding.
4. **Articulate-participant capture.** Over-weighting the one eloquent interviewee. Representativeness comes from counts, not quotability.
5. **Pre-baked coding.** Forcing the data into a framework the team already had, instead of letting codes emerge. Open code first.
6. **Untraceable themes.** Asserting a theme with no quote IDs. Every theme carries its evidence.
7. **Say-do conflation.** Reporting stated preferences as if they were behavior. Flag the gap between what users say and what their stories reveal.
8. **Segment flattening.** Reporting a universal theme that is actually segment-specific, leading to a decision that serves one segment and harms another.
9. **Decision-less synthesis.** A readout full of themes with no implications. Each significant finding must connect to a decision.
10. **Overconfidence on thin data.** Drawing firm conclusions from a handful of interviews. Tie confidence to prevalence and consistency; label thin findings as hypotheses.

---

## Output Format

```
# USER RESEARCH SYNTHESIS — [research question]
Interviews: N=[..] | Segments: [...]
Team priors at start: [what we believed going in]

## Themes
| # | Theme | Prevalence (k of N) | Intensity | Supporting quote IDs |
|---|-------|---------------------|-----------|----------------------|
| 1 | [...] | 14 of 20            | emphatic  | [I3:Q2, I7:Q1, ...]  |
| 2 | [...] | 8 of 20             | passing   | [...]                |

## Tensions
| Tension | Side A (quotes) | Side B (quotes) | Within-user or across-user? | Segment split? |
|---------|-----------------|-----------------|-----------------------------|----------------|
| [...]   | [IDs]           | [IDs]           | [...]                       | [...]          |

## Segment patterns
| Theme / tension | Segment A | Segment B | Universal or segment-specific? |
|-----------------|-----------|-----------|--------------------------------|
| [...]           | [...]     | [...]     | [...]                          |

## Surprises (contradicted or off-radar vs. priors)
- [Finding] — contradicts prior that [...] | quote IDs: [...]
- [Finding] — not on our radar | quote IDs: [...]

## Say-do gaps
- Stated: [...] | Revealed by behavior/story: [...] | quote IDs: [...]

## Decisions
| Finding | Implication for product / strategy / messaging | Confidence | Basis |
|---------|------------------------------------------------|------------|-------|
| [...]   | [...]                                          | high/med/low | k-of-N + consistency |

## Open questions for the next round
- [what this batch could not resolve]
```

---

## Verification

- [ ] Team priors stated up front.
- [ ] Open coding done before interpretation; codes emerged from data.
- [ ] Themes promoted only with cross-interview recurrence and k-of-N counts.
- [ ] Every theme tied to quote IDs.
- [ ] Tensions surfaced with quotes on both sides, not collapsed.
- [ ] Segment patterns checked; segment-specific themes flagged.
- [ ] Surprises and contradictions given explicit airtime.
- [ ] Say-do gaps noted.
- [ ] Each significant finding connected to a decision with a confidence level.
- [ ] No cherry-picked confirmation.
- [ ] No vivid-quote inflation passed off as consensus.
- [ ] Thin findings labeled as hypotheses, not conclusions.
