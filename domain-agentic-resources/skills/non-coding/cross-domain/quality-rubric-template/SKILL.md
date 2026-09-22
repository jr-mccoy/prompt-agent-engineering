---
name: quality-rubric-template
description: Build a scoring rubric that two independent assessors apply the same way. Use this skill to "make a rubric", "score submissions consistently", "define what good looks like", "our reviewers disagree", "turn this checklist into a score", or when you need weighted criteria with behavioural anchors, an explicit insufficient-evidence verdict, load-bearing minimums that cap the total, and an inter-rater agreement check. Domain-agnostic — the same structure serves hiring scorecards, vendor selection, submission grading, document review and audit findings.
tags:
  - rubric
  - scoring
  - behavioural-anchors
  - inter-rater-agreement
  - evaluation
  - cross-domain
updated: "2026-09-22"
---

# Quality Rubric Template

A domain-agnostic pattern for building a rubric that produces the **same score from two
independent assessors**. If it does not do that, it is recording the assessor rather than
the thing assessed.

## When to Use This Skill

- Reviewers disagree and nobody can say why
- A checklist needs to become a score
- Submissions, vendors, candidates or documents must be compared fairly
- An audit needs defensible findings rather than opinions
- You are about to write "rate this 1–5" and want to do better

## Not for

- **Deciding what to assess.** A rubric scores against criteria someone chose; choosing
  them is the domain's job. See `../../business/competitive-analysis/` for vendor criteria,
  `../../../../../domain-hr-management/hiring/hr_structured_scorecard.md` for hiring
  attributes, `../../../../../domain-education-teaching/program/outcomes-assessment/` for
  learning outcomes.
- **Existing domain rubrics.** Four 100-point rubrics already exist for authoring
  resources: `authoring/skill-patterns/SKILL_QUALITY_RUBRIC.md` and its agent, command
  and system siblings. Use those directly rather than rebuilding them.
- **LLM-as-judge design**, which has its own methodology — see
  `../../../../../domain-prompt-engineering/evaluation/rubrics/rubric_llm_judge_designer.md`
  and `rubric_calibrated_anchors.md`.

## The Pattern

### 1. One criterion per thing you actually care about

Three to seven criteria. Each must be **independently observable** — if moving one
necessarily moves another, they are one criterion wearing two names, and scoring both
double-counts it.

Name each criterion as a noun phrase describing an attribute, not a judgement:
"acceptance criteria present and testable", not "quality of specification".

### 2. Weight by consequence, not by effort

Weights reflect how much the criterion matters to the decision, not how hard it is to
assess or how long the section is. Publish the weights with the rubric: a hidden
weighting is a hidden opinion.

| Criterion | Weight | Why this weight |
|---|---|---|

### 3. Anchor every level behaviourally

**This is the step that makes a rubric reproducible.** An unanchored numeric scale
records the assessor's personal calibration, which is why two people produce a 3 and a 5.

Write what each level **looks like**, as something observable about the artifact:

| Level | Anchor shape |
|---|---|
| Above bar | The specific observable state that exceeds the requirement |
| At bar | The specific observable state that meets it |
| Approaching | The specific observable state that falls short in a named way |
| Below bar | The specific observable state that fails |

Use **four levels, not five.** The middle of an odd scale absorbs every uncertain rating
and the rubric stops discriminating.

Test each anchor: could two people looking at the same artifact disagree about whether
the anchor was met? If yes, it describes a judgement. Rewrite it as a property of the
thing.

### 4. Make insufficient evidence a selectable verdict

Every criterion offers **INSUFFICIENT EVIDENCE**, ranked alongside the levels rather
than left as a blank.

Assessors rate criteria they could not actually assess, because the form has a box and a
blank looks careless. Given a legitimate option they use it, and the result learns
something true: this criterion was not established. A blank teaches nothing.

### 5. Require evidence beside every rating

A mandatory adjacent field: **what in the artifact supports this.** A quote, a location,
a described observation — not a restatement of the rating.

State the enforcement on the rubric itself: **a rating with no evidence does not count.**
Without that line the field fills with "see above".

### 6. Add load-bearing minimums that cap the total

Some criteria are not tradeable. A submission that fails a safety criterion is not
rescued by excelling elsewhere, and a weighted total will quietly average it away.

| Criterion | Minimum | Effect if unmet |
|---|---|---|
| [criterion] | [score] | Total is capped at [x] regardless, or the verdict is Fail |

This is the pattern `agentic-system-factory/scripts/score_rubric.py` implements in code —
a security minimum that caps the tier however high the total. Copy the mechanism: without
it, weighted totals launder unacceptable failures.

### 7. Set bands, and say what each triggers

A score with no consequence is trivia.

| Band | Range | What happens |
|---|---|---|
| | | Accept as is |
| | | Accept with named conditions |
| | | Revise and resubmit |
| | | Reject |

### 8. Check inter-rater agreement before trusting it

The rubric is a measuring instrument and instruments get calibrated.

Have two assessors score the same three artifacts independently, then compare:

- **Agreement within one level on every criterion** → usable.
- **A two-level gap on any criterion** → that criterion's anchors are ambiguous. Fix the
  anchors, not the assessors.
- **Systematic divergence** (one assessor consistently lower) → the bar itself is
  unstated; agree it explicitly and re-anchor.

Re-run whenever assessors change or the rubric is edited. The protocol is in
`../../../../../domain-prompt-engineering/evaluation/rubrics/rubric_inter_rater_agreement_protocol.md`.

### 9. Score independently, then discuss

Assessors submit before seeing each other's scores. Otherwise the rubric produces one
opinion held by several people — the thing it was built to prevent. Resolve disagreement
by identifying the disputed criterion and the evidence that would settle it, never by
averaging.

## Output Template

```markdown
## Rubric — [what is being assessed]
**Version:** [x] · **Last calibrated:** [date, agreement result]

| # | Criterion | Weight | Load-bearing minimum |
|---|---|---|---|

### [Criterion 1] — weight [x]
*Assesses:* [one line]

| Level | Anchor (observable state of the artifact) | Points |
|---|---|---|
| Above bar | | |
| At bar | | |
| Approaching | | |
| Below bar | | |
| **Insufficient evidence** | Not assessable from what was supplied | — |

**Rating:** ☐ Above ☐ At ☐ Approaching ☐ Below ☐ Insufficient evidence
**Evidence (required — a rating with no evidence does not count):**
> ___

---
### Result
| Criterion | Rating | Weighted | Minimum met? |
|---|---|---|---|
| **Total** | | | |

**Caps applied:** [none / total capped at x because criterion y unmet]
**Band:** [x] → [what happens]

*Scored independently before discussion. Submitted by [assessor] on [date].*
```

## Verification

- [ ] Three to seven criteria, each independently observable
- [ ] Weights published with a reason
- [ ] Four levels, each anchored to an observable state of the artifact
- [ ] No anchor phrased as a judgement or an adjective
- [ ] INSUFFICIENT EVIDENCE selectable on every criterion
- [ ] Mandatory evidence field, with the does-not-count rule printed
- [ ] Load-bearing minimums identified, with their capping effect stated
- [ ] Bands map to actions
- [ ] Inter-rater agreement checked on at least three artifacts
- [ ] Independent submission before discussion is specified
- [ ] The rubric carries a version, so a score can name what produced it

**False-positive prevention.** The dominant failure is adjectival anchors — "excellent",
"adequate", "poor". That is the unanchored scale with extra words and it produces the
same divergence. Anchor to the artifact: "every deliverable names a format and an
acceptance condition" is checkable; "well specified" is not.

The second failure is a weighted total that averages away an unacceptable failure. Any
criterion where failure should be disqualifying needs a load-bearing minimum, or the
arithmetic will launder it.

The third is skipping calibration. An uncalibrated rubric feels rigorous and may be
producing two-level disagreements on half its criteria. Three artifacts, two assessors,
one comparison — it is an hour, and it is the only evidence the instrument works.

The fourth is a score with no band and no consequence, which generates a number nobody
acts on and quietly discredits the next rubric.

## Related

- `../intake-triage-pattern/` — the sibling pattern for routing before scoring
- `../handoff-approval-workflow/` — where a rubric band becomes an approval gate
- `../../../../../domain-prompt-engineering/evaluation/rubrics/rubric_inter_rater_agreement_protocol.md` — the calibration protocol
- `../../../../../domain-prompt-engineering/evaluation/rubrics/rubric_calibrated_anchors.md` — anchor writing in depth
- `../../../../../domain-hr-management/hiring/hr_structured_scorecard.md` — this pattern applied to hiring
