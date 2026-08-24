---
title: "Pattern Library Builder — Turn Accumulated Debriefs Into Situation → Move → Outcome"
category: negotiation/craft
description: "Convert a pile of individual negotiation debriefs into a personal library that answers 'what works in situations like this.' Defines a record format terse enough to maintain, a situation taxonomy that groups usefully rather than by topic, the extraction pass that finds patterns across records, and the calibration check that catches your systematic errors — the ones that recur because they feel like judgment. Counters the reason careful debriefing still produces no compounding: individual retrospectives are read once and never compared."
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
  - negotiation
  - patterns
  - library
  - calibration
  - compounding
updated: "2026-07-26"
reasoning:
  styles: [analytic, evaluative, systems, reflective]
  stakes: low
  horizon: years
  uncertainty: ambiguity
  evidence_quality: moderate
  domain_complexity: variable
  collaboration: solo
  output_format: [matrix, structured]
  user_role: [executive, founder, sales, hr, lawyer, individual]
  mode: [synthesize, audit, document]
related_prompts:
  - domain-negotiation/after-the-deal/negotiation_post_negotiation_debrief.md
  - domain-negotiation/craft/negotiation_style_self_assessment.md
  - domain-negotiation/preparation/negotiation_prep_depth_triage.md
---

# Pattern Library Builder — Turn Accumulated Debriefs Into Situation → Move → Outcome

**Objective:** Careful debriefing produces surprisingly little improvement on its own, for a mundane reason: each debrief is written once, read once, and never compared with the others. The learning that matters is not in any single retrospective — it is in what recurs across twenty of them. Your systematic BATNA misestimation, the situation type where you consistently under-claim, the move that works reliably against a particular counterpart type, the tell that predicts a deal will not close. None of this is visible from inside one negotiation, and all of it is visible from a library. This prompt builds that library: a **record format terse enough to actually maintain**, a **situation taxonomy** that groups by structural similarity rather than by topic, the **extraction pass** that surfaces patterns, and the **calibration check** that catches the errors which recur precisely because they feel like judgment rather than error.

Consumes the output of `after-the-deal/negotiation_post_negotiation_debrief.md`. Feeds `preparation/negotiation_prep_depth_triage.md`, which gets better at routing as the library grows.

**When to use:**
- You have several negotiation debriefs and no way to compare them.
- You suspect you make the same mistake repeatedly but cannot name it.
- You want preparation to get faster as well as better over time.
- You are building institutional knowledge for a team that negotiates.

**When NOT to use:**
- You have fewer than five debriefs — accumulate first; a library of three is a folder.
- You want to assess one negotiation — `after-the-deal/negotiation_post_negotiation_debrief.md`.
- You want to identify your default style — `craft/negotiation_style_self_assessment.md`, which works from the same records for a different purpose.

**Audience:** Executives, founders, salespeople, people leaders, lawyers, and individuals negotiating often enough for patterns to be worth extracting.

---

## Inputs / Context

1. **Existing debriefs.** However many you have, in whatever form.
2. **Negotiation frequency.** How fast the library will accumulate.
3. **Recurring situation types.** The kinds of negotiation you actually do.
4. **Recurring counterpart types.** Procurement, founders, recruiters, agencies, individuals.
5. **Known suspicions.** Errors you think you make but have not confirmed.
6. **Who else uses this.** Whether it is personal or a team asset.

---

## Constraints

### Must
- Keep the record format **terse enough to maintain**. A format requiring twenty minutes per negotiation is abandoned, and an abandoned library is worse than none because it produces false confidence in having a system.
- Build a **situation taxonomy by structure**, not by topic. "One-shot, high asymmetry, single-issue" groups usefully; "vendor negotiations" does not.
- Record the **counterfactual** where possible — what you would do differently — since a record of what happened without that is a diary.
- Run a periodic **extraction pass** across records, because patterns are invisible from inside any one of them.
- Include a **calibration check**: how wrong your BATNA estimates were, in which direction, and by how much.
- Record **failures and no-deals**, which carry more information than successes and are the records people skip.
- Make records **searchable by situation**, so the library is usable at preparation time rather than only at review time.

### Must Not
- Design a format so detailed that it is not maintained. This is the failure mode of every personal knowledge system, and it presents as a rich schema used four times.
- Group by topic. Topical grouping puts structurally different negotiations together and structurally similar ones apart, which is exactly backwards for pattern extraction.
- Record only successes. The no-deals and the bad outcomes carry the most information and are the first records people omit.
- Treat single instances as patterns. One occurrence is an anecdote; three across different counterparts is a pattern.
- Let the library become a diary. Without the counterfactual and the extraction pass, it is a record of events with no learning attached.
- Skip the calibration check because it is uncomfortable. Systematic estimation error is the highest-value finding in the library and the one most avoided.

---

## Instructions

### Step 1 — Define the record format
Terse. Seven fields, one line each:

| Field | Content |
|---|---|
| Situation type | From the taxonomy (Step 2) |
| Counterpart type | Procurement / founder / recruiter / agency / individual / peer |
| What I did | The two or three moves that mattered |
| What happened | Outcome vs. target and floor |
| Their BATNA — estimated vs. actual | The calibration input |
| What I'd do differently | The counterfactual |
| Confidence | How sure I am about the causal read |

Five minutes per negotiation. If it takes longer, cut fields until it does not, because a maintained thin library beats an abandoned rich one by an enormous margin.

### Step 2 — Build the situation taxonomy
Group by **structure**, not subject. The dimensions that predict what works:

| Dimension | Values |
|---|---|
| Repetition | One-shot / repeated / indefinite |
| Issues | Single / multi |
| Power | Symmetric / I'm stronger / they're stronger |
| Information | Symmetric / I know more / they know more |
| Parties | Two / three-plus |
| Relationship | Transactional / relationship-primary |

A salary negotiation and a vendor renewal may share a structural type and belong together; two vendor negotiations with different power structures may not. This is the design decision that determines whether the library produces transferable findings or just sorted anecdotes.

### Step 3 — Backfill from existing debriefs
Convert what you already have into the format. It will be lossy — older debriefs will lack the calibration data — and that is fine. Mark the gaps rather than inventing entries, and accept that the library's usefulness begins from the point the format stabilizes rather than from your first negotiation.

### Step 4 — Run the extraction pass
Every ten records, or quarterly, ask four questions across the whole library:
- **What recurs?** The same move working, or failing, in the same structural type.
- **Where do I under- or over-claim?** Outcomes clustering relative to targets, by situation type.
- **What surprises me repeatedly?** A recurring surprise is a standing blind spot, not bad luck.
- **What predicted the outcome?** Any early signal that reliably indicated how a negotiation would go.

This pass is the entire point of the library. Records without it accumulate without compounding.

### Step 5 — Run the calibration check
For each record with the data: how wrong was your estimate of their BATNA, in which direction, and by how much? Then aggregate. The characteristic findings are systematic and directional — consistently over-estimating their alternatives (producing over-concession), or consistently under-estimating them (producing lost deals). Either is worth more than any individual tactic in the library, because it corrects every future negotiation at once. This is the check people skip, and skipping it removes most of the library's value.

### Step 6 — Extract the transferable findings
Write what you now believe, with the evidence count attached: *"In one-shot high-asymmetry situations, my opening anchors have been too conservative — three of four landed below the counterpart's expected range (n=4, moderate confidence)."* Attaching **n** and confidence is what stops a two-instance coincidence being promoted to a rule, which is how personal libraries generate confident errors.

### Step 7 — Make it usable at preparation time
The library only pays off if it is consulted before a negotiation rather than only reviewed after. Make records retrievable by situation type, and add the step explicitly to your preparation: `preparation/negotiation_prep_depth_triage.md` should trigger a look at the library for the matching structural type. Keep the findings on one page so the check costs a minute rather than an evening.

### Step 8 — Handle team use, if applicable
If the library is shared, add two fields — who negotiated, and what was specific to them — since a move that works for one person's style may not transfer. Then set an anonymization rule for counterpart-specific records, because a shared library containing frank assessments of named counterparts is a liability if it leaks.

### Step 9 — Adversarial check
- Which finding rests on the fewest records, and are you treating it as more established than n supports?
- Are you recording the negotiations that went badly, or quietly skipping them?
- If the calibration check says you systematically misestimate in one direction, are you actually adjusting?

---

## False-Positive Prevention

1. **Format inflation.** Designing a rich schema that takes twenty minutes per negotiation. It is used four times and abandoned, leaving a false sense of having a system in place.
2. **Topical grouping.** Sorting by subject rather than structure. It separates structurally similar negotiations and combines structurally different ones, which prevents exactly the transfer the library exists to produce.
3. **Success-only recording.** Omitting no-deals and bad outcomes. They carry the most information, and their absence biases every finding toward whatever conditions produce success.
4. **Single-instance promotion.** Treating one occurrence as a pattern. Requires three across different counterparts before it becomes a finding, and an explicit n on every claim.
5. **Diary drift.** Recording events without counterfactuals or an extraction pass. It accumulates without compounding, and it feels like diligence throughout.
6. **Calibration avoidance.** Skipping the BATNA-estimation check because the results are uncomfortable. Systematic directional error is the single most valuable finding available, precisely because it corrects everything downstream at once.
7. **Post-hoc-only use.** Building a library consulted at review but never at preparation. The value is in the check before the next negotiation, not in the archive.
8. **Confidence inflation.** Stating findings without n or confidence. Personal libraries are small, and small-n findings stated flatly become rules that then generate confident errors for years.

---

## Output Format

```
# Negotiation Pattern Library

## Record format (5 minutes max)
| Field | This record |
|---|---|
| Situation type | [from taxonomy] |
| Counterpart type | [...] |
| What I did (2–3 moves) | [...] |
| What happened (vs. target / floor) | [...] |
| Their BATNA: estimated → actual | [...] → [...] |
| What I'd do differently | [...] |
| Confidence in the causal read | [...] |

## Situation taxonomy (structural)
| Dimension | Values |
|---|---|
| Repetition | one-shot / repeated / indefinite |
| Issues | single / multi |
| Power | symmetric / me stronger / them stronger |
| Information | symmetric / me more / them more |
| Parties | two / three-plus |
| Relationship | transactional / relationship-primary |

## Library
| # | Situation type | Counterpart | Key moves | Outcome | BATNA error | Would do differently |
|---|---|---|---|---|---|---|
| 1 | [...] | [...] | [...] | [...] | [±] | [...] |
Records: [n] · No-deals included: [n] · [must not be zero if any occurred]

## Extraction pass (every 10 records / quarterly)
What recurs: [...]
Where I under- or over-claim: [...]
Repeated surprises (= standing blind spots): [...]
Early signals that predicted outcomes: [...]

## Calibration check
| Record | Their BATNA estimated | Actual | Error | Direction |
|---|---|---|---|---|
| [...] | | | | over / under |
**Systematic finding:** [consistently over/under-estimate their alternatives]
**Correction to apply:** [...]

## Transferable findings
| Finding | n | Confidence |
|---|---|---|
| [...] | [n] | low / moderate / high |

## Preparation-time use
Retrievable by: [situation type]
Trigger: prep_depth_triage step [n] → check library for matching structural type
Findings kept to: one page

## Team use (if shared)
Extra fields: who negotiated · what was person-specific
Anonymization rule for counterpart records: [...]

## Adversarial check
- Finding on fewest records, treated as more established than n supports: [...]
- Am I recording the bad ones? [...]
- If calibration shows directional error, am I actually adjusting? [...]
```

---

## Verification

- [ ] Record format fits in five minutes per negotiation.
- [ ] Situation taxonomy groups by structure across all six dimensions, not by topic.
- [ ] Existing debriefs backfilled, with gaps marked rather than invented.
- [ ] Extraction pass scheduled by record count or quarterly, covering all four questions.
- [ ] Calibration check run, with direction and magnitude of BATNA error aggregated.
- [ ] A systematic correction stated where directional error is found.
- [ ] Every transferable finding carries n and a confidence level.
- [ ] No-deals and bad outcomes present in the library.
- [ ] Library retrievable by situation type and wired into preparation, not only review.
- [ ] Findings kept to one page for preparation-time use.
- [ ] Team fields and anonymization rule added if shared.
- [ ] Adversarial check tests small-n findings and whether bad outcomes are being recorded.
- [ ] No finding promoted from a single instance.
