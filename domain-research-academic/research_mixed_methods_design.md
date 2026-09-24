---
title: "Mixed-Methods Design — Core Design, Integration Points, Joint Displays, and What to Do When Strands Disagree"
category: research-academic/mixed-methods
description: "Design a mixed-methods study once the decision to combine strands is made: choose convergent, explanatory sequential or exploratory sequential from what each strand must do for the other, specify how samples relate, name every integration point (connecting, building, merging) and the procedure used there, draft the joint display, and state in advance how discordant findings will be handled and reported; distinct from `domain-science/methods-foundations/science_qualitative_vs_quantitative_decision.md` (whether to mix at all) and from the single-strand instruments `domain-research-academic/research_survey_instrument_designer.md` and `domain-research-academic/research_qualitative_coding_scheme.md`."
techniques:
  - DS-01
  - RT-06
  - OC-03
  - QA-04
  - QA-12
difficulty: advanced
tags:
  - mixed-methods
  - research-design
  - integration
  - joint-display
  - explanatory-sequential
  - convergent-design
  - surveys-plus-interviews
  - numbers-and-stories
  - results-disagree
updated: "2026-09-24"
reasoning:
  styles: [systematic, integrative, methodological]
  stakes: variable
  horizon: months
  uncertainty: ambiguity
  evidence_quality: variable
  domain_complexity: variable
  collaboration: solo_or_team
  output_format: structured
  user_role: [researcher, student, evaluator, ux_researcher, policy]
  mode: [design, plan]
related_prompts:
  - domain-science/methods-foundations/science_qualitative_vs_quantitative_decision.md
  - domain-research-academic/research_survey_instrument_designer.md
  - domain-research-academic/research_qualitative_coding_scheme.md
---

# Mixed-Methods Design

**Objective:** Turn "we'll do a survey and some interviews" into a design where each
strand has a job the other cannot do, the points where they meet are named and
procedurally specified, and the combined inference — what you know from both that you
could not know from either — has a planned place to appear. Integration is the method;
without it, a mixed-methods study is two studies in one report.

**When to Use:**
- The decision to combine qualitative and quantitative strands is made and the design must now be specified.
- A proposal, protocol or ethics application needs the mixed-methods section.
- A reviewer said the integration was "unclear" or "an afterthought".
- Results from two strands are in and nobody planned how to combine them (use Steps 5–7 retrospectively, and say so).

**Not this prompt if:**
- You have not decided whether to mix methods — `domain-science/methods-foundations/science_qualitative_vs_quantitative_decision.md`.
- You need the survey itself — `domain-research-academic/research_survey_instrument_designer.md`.
- You need the codebook — `domain-research-academic/research_qualitative_coding_scheme.md`.
- You need the interview guide — `domain-research-academic/research_interview_guide_designer.md`.
- The "qualitative" component is open-ended survey comments only; that is usually one strand with text data.

## Inputs / Context

1. **Research questions**, including the one that needs both strands (the mixed-methods question).
2. **Why each strand is needed:** what the quantitative strand cannot show, and what the qualitative strand cannot.
3. **Population and access:** can the same people take part in both strands?
4. **Timing and resources:** months available, whether strands can run in parallel, team skills.
5. **Paradigm stance** if the field or supervisor expects one stated.
6. **Reporting expectations:** journal, funder or programme conventions for mixed methods.

## Method

1. **Name the purpose of mixing.** Pick the dominant one: corroboration (do they agree?),
   explanation (why did the numbers come out this way?), development (build an instrument or
   intervention from qualitative findings), or expansion (different questions about one
   phenomenon). The purpose chooses the design.

2. **Choose the core design (DS-01).**

   | Design | Sequence | Fits purpose | First integration point |
   |---|---|---|---|
   | Convergent | Both strands at once, analysed separately | Corroboration, expansion | Merging at analysis |
   | Explanatory sequential | Quantitative → qualitative | Explanation | Connecting: quantitative results select qualitative participants and questions |
   | Exploratory sequential | Qualitative → quantitative | Development | Building: qualitative findings become items, variables or an intervention |

   State the priority (which strand the main inference rests on, or equal) and justify it.

3. **Specify how the samples relate.** Identical, nested (qualitative participants drawn from
   the quantitative sample), parallel (same population, different people) or multilevel. For
   sequential designs, state the selection rule precisely — e.g. extreme cases, residuals from a
   model, or a typology of response patterns.

4. **List every integration point with its procedure.** Design level (the mixed-methods question),
   methods level (connecting, building, merging, embedding) and interpretation level (joint
   display, meta-inferences). A point with no procedure is not integration.

5. **Draft the joint display (OC-03).** Rows are the dimensions you will compare; columns hold the
   quantitative result, the qualitative finding, the fit (confirmation / expansion / discordance)
   and the meta-inference. Draft it with placeholders now; it forces the analysis plan to produce
   comparable outputs.

6. **Plan for discordance (QA-04).** Before data: what counts as disagreement, how you will
   investigate it (re-examine data, check sample differences, gather more), and how it will be
   reported. Discordance is a finding, not a failure.

7. **Address rigour by strand and for the whole (RT-06).** Validity and reliability for the
   quantitative strand; credibility and transferability for the qualitative; and integration-
   specific threats — sample mismatch, timing gaps, one strand's findings overriding the other.

8. **Timeline and reporting.** Milestones per strand and per integration point; the reporting
   standard for each strand plus a mixed-methods reporting convention (e.g. GRAMMS), marked
   `[VERIFY]` against the target outlet.

## Output Format

```
# Mixed-methods design — [study]
Mixed-methods question: [ ]
Purpose of mixing: [corroboration / explanation / development / expansion]
Core design: [ ] · Priority: [QUAN / QUAL / equal] because [ ]

## Strands
| Strand | Question | Sample (n, how selected) | Data | Analysis |

## Sample relationship
[identical / nested / parallel / multilevel] — selection rule: [ ]

## Integration points
| Level | Point | Procedure | Output |

## Joint display (draft)
| Dimension | Quantitative result | Qualitative finding | Fit | Meta-inference |

## Discordance plan
Counts as discordance: [ ] · Investigation: [ ] · Reporting: [ ]

## Rigour
Quantitative: [ ] · Qualitative: [ ] · Integration threats and responses: [ ]

## Timeline and reporting
| Month | Milestone |
Standards: [strand standards] + [mixed-methods convention] [VERIFY]
```

## Verification

- [ ] Purpose of mixing stated and consistent with the chosen design.
- [ ] Priority stated with a reason.
- [ ] Sample relationship and, for sequential designs, an explicit selection rule.
- [ ] Every integration point has a named procedure and output.
- [ ] Joint display drafted with rows that both strands will actually produce.
- [ ] Discordance defined in advance with an investigation and reporting plan.
- [ ] Integration-specific rigour threats addressed, not only per-strand ones.
- [ ] Reporting conventions marked `[VERIFY]` against the outlet.

## False-Positive Prevention

1. **Parallel studies called mixed methods.** Two strands reported in separate chapters with a
   paragraph of comparison at the end have not been integrated.
2. **Qualitative as illustration.** Picking quotes that decorate the statistics is not
   explanation. The qualitative strand needs its own analysis and the power to contradict.
3. **Design chosen by habit.** A convergent design for an explanation purpose leaves the
   qualitative strand unable to target what the numbers revealed.
4. **Vague selection in sequential designs.** "Some participants will be invited for interview"
   is not a rule. Name the criterion that links the strands.
5. **Discordance smoothed over.** Reporting only where strands agree inflates confidence.
   Discordant rows stay in the joint display.
6. **Joint display invented after the fact.** If the analysis plan does not produce comparable
   outputs, the display will be forced. Draft it first.
7. **Sample mismatch ignored.** Comparing a national survey with interviews at one site is
   comparing populations, not methods. State the limit.

## Example Output

```
# Mixed-methods design — Burnout and intention to leave among hospital nurses
Mixed-methods question: Why do some highly burnt-out nurses intend to stay?
Purpose of mixing: explanation · Core design: explanatory sequential · Priority: QUAN, because the
policy question is prevalence and association; the qualitative strand explains an anomaly

## Strands
| QUAN | Association of burnout (validated scale) with intention to leave | 412 of 1,030 invited (40%) | Survey | Logistic regression |
| QUAL | What keeps high-burnout nurses in post | 18, nested in the survey sample | Semi-structured interviews | Reflexive thematic analysis |

## Sample relationship
Nested — selection rule: from consenting respondents, 6 high-burnout/intend-to-leave, 6 high-burnout/intend-to-stay
(the anomaly), 6 low-burnout/intend-to-stay; 6 + 6 + 6 = 18

## Integration points
| Design | Mixed-methods question | Stated in protocol | — |
| Methods | Connecting | Regression residuals + burnout score select interviewees; items with largest effects shape the guide | Sampling frame, guide |
| Interpretation | Merging | Joint display by dimension | Meta-inferences |

## Joint display (draft)
| Workload | OR for leaving per extra shift/month [ ] | [theme] | [confirm/expand/discord] | [ ] |
| Team support | [ ] | [ ] | [ ] | [ ] |
| Professional identity | not measured | [ ] | expansion | [ ] |

## Discordance plan
Counts as discordance: a theme contradicting a statistically supported association. Investigation: check whether
interviewees differ from the survey sample on covariates; re-read transcripts for the contrary case. Reporting: kept
in the joint display with both explanations considered.

## Rigour
Quantitative: validated burnout scale, non-response comparison against staff records · Qualitative: reflexive journal,
second coder on 4 transcripts · Integration threat: 40% response rate means interviewees come from the more engaged —
compare interviewees with non-responders on unit and grade, and state the limit.

## Timeline and reporting
| Months 1–3 | Survey fielded and analysed |
| Month 4 | Interview sampling frame from residuals; guide finalised |
| Months 5–7 | Interviews and analysis |
| Month 8 | Joint display and meta-inferences |
Standards: STROBE (survey) + SRQR (interviews) + GRAMMS [VERIFY with target journal]
```

## Techniques Used

- **DS-01 Framework Application** — core-design typology matched to purpose.
- **RT-06 Correlation and Cross-Analysis** — merging strands and integration-specific rigour.
- **OC-03 Markdown Table Specification** — the joint display drafted before data.
- **QA-04 Uncertainty Acknowledgment** — discordance defined and planned for in advance.
- **QA-12 False Positives Identification** — what looks like integration but is not.

## Related Prompts

- `domain-science/methods-foundations/science_qualitative_vs_quantitative_decision.md` — whether to mix at all.
- `domain-research-academic/research_survey_instrument_designer.md` — the quantitative instrument.
- `domain-research-academic/research_qualitative_coding_scheme.md` — the qualitative codebook.
- `domain-research-academic/research_interview_guide_designer.md` — the interview guide shaped by the connecting step.
- `domain-research-academic/research_thesis_dissertation_structure.md` — where the strands and the integration sit in a thesis.
