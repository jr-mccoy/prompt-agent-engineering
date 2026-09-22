---
title: "Reference Check Guide — Targeted at the Open Question, Not a Formality"
category: hr-management/hiring
description: "Run a reference check that resolves the loop's remaining uncertainty: the specific open question carried forward from the debrief, referee selection that includes someone who managed the candidate, questions that invite calibration rather than endorsement, and a written record. Refuses generic reference calls and backchannel enquiries the candidate has not consented to."
techniques:
  - ST-02
  - CM-02
  - RT-05
  - QA-04
  - OC-03
difficulty: intermediate
tags:
  - hiring
  - reference-check
  - due-diligence
  - consent
  - evidence-based
updated: "2026-09-22"
related_prompts:
  - domain-hr-management/hiring/hr_interview_loop_design.md
  - domain-hr-management/hiring/hr_structured_scorecard.md
  - domain-hr-management/performance-reviews/hr_reviewer_approach_guide.md
---

# Reference Check Guide

**Objective:** Turn the reference check from a formality into the stage that resolves
the loop's **one remaining open question**. Output: the question carried forward from
debrief, a referee list that includes someone who managed the candidate, questions
designed to elicit calibration rather than endorsement, and a written record that
enters the decision the same way a scorecard does.

**When to Use:**
- The loop has produced a likely hire with a specific residual uncertainty.
- An attribute came back INSUFFICIENT EVIDENCE and the loop cannot re-test it.
- A candidate is strong but one interviewer dissented and named a concrete concern.

**When NOT to use:**
- You have no open question. A reference call with nothing to resolve produces
  confirmation and costs the referee an hour — either skip it or name the question
  first.
- You want to check facts only (dates, title, eligibility) — that is a verification
  task, often outsourced, and needs none of this.
- You are contacting people the candidate has not named and has not agreed to. See the
  boundary below; this prompt will not design a backchannel.
- You need a performance review of a current employee — that is
  `../performance-reviews/hr_reviewer_approach_guide.md`.

---

## The consent boundary, before anything else

**Only speak to referees the candidate has named or explicitly agreed you may contact.**

Backchannel references — asking a mutual contact about someone without their knowledge
— are common and are three separate problems: they can put a candidate's current
employment at risk, they collect unverifiable hearsay that cannot be tested or
appealed, and in several jurisdictions they raise data-protection and defamation
exposure.

If someone volunteers unsolicited information about a candidate, note that it was
unsolicited, do not act on it as evidence, and if it is material, put the substance —
not the source — to the candidate and let them answer.

Also: do not contact a current employer without explicit, specific permission. Assume
the candidate's job is at risk if you do.

**This is not legal advice.** What may be asked and disclosed varies by jurisdiction,
and some regions restrict reference content sharply. See
`../../domain-legal/employment-labor/`.

---

## Context Gathering

1. **The open question**
   - "From the debrief: what is the one thing you still do not know?"
   - "Which attribute came back insufficient, or was disputed?"
   - "If the reference resolved it in the worst plausible direction, would that change
     the decision?"

2. **The referees offered**
   - "Who has the candidate named? What was each relationship, and when?"
   - "Is any of them someone who managed the candidate? If none, ask for one."
   - "Is any of them a friend rather than a colleague?"

3. **The candidate's account**
   - "What has the candidate said about the period each referee covers?"
   - "Anything they flagged themselves — a difficult manager, a project that failed, a
     short tenure?"

The last question is the one that makes the check useful. A candidate who has already
told you a tenure ended badly has given you something to calibrate rather than
discover, and the reference either corroborates their account or does not.

---

## Method

### Step 1 — Name the open question, in writing, before calling

One or two questions, carried forward from the debrief. Write them down. A call without
them becomes a pleasant conversation in which a referee says positive things and the
loop learns nothing while feeling reassured.

If the debrief cannot produce an open question, the honest output is: no reference call
needed. Record that.

### Step 2 — Get at least one referee who managed the candidate

Peers describe collaboration; managers describe performance against a bar, which is
usually the open question. If the candidate offers only peers, ask directly for a
former manager and treat a refusal as information worth understanding rather than
disqualifying — there are good reasons (a hostile former manager, a company that has
closed, a manager who has died).

Two or three referees. More produces diminishing returns and a larger imposition.

### Step 3 — Ask questions that invite calibration, not endorsement

Referees default to endorsement. Questions that break the default:

| Weak (invites endorsement) | Strong (invites calibration) |
|---|---|
| "Was she good at her job?" | "Of the people you have managed at that level, where would she sit — top quarter, middle, and what puts her there?" |
| "Would you hire him again?" | "What role would you hire him into, and what role would you not?" |
| "Any weaknesses?" | "What did you find yourself coaching him on more than once?" |
| "How were her communication skills?" | "Tell me about a time she had to explain something contested to someone senior. What happened?" |
| "Did he work well in a team?" | "Who on the team found him hardest to work with, and why?" |

Then the two questions that do most of the work:

- **"What would you want to know, if you were hiring them into [this specific role]?"**
  Describe the role first. A referee who knows the role gives targeted information.
- **"What support did they need to do their best work?"** Reads as helpful, answers the
  development question, and surfaces constraints a direct weakness question will not.

### Step 4 — Probe the open question specifically

Ask about the actual concern, in behavioural terms, without leading:

> "One thing we are still weighing is how they handle a situation where the
> requirements change late. Can you think of a time that happened, and what they did?"

Not: "We were worried they might be inflexible — were they?" A leading question
produces agreement, and agreement is not evidence.

If a referee is reticent, note the reticence rather than interpreting it. Silence has
many causes: company policy limiting references to dates and title, a bad ending that
is not the candidate's fault, a referee who barely remembers. Ask "is there a policy
about what you can discuss?" — it resolves most of it.

### Step 5 — Record it like a scorecard

Same discipline as `hr_structured_scorecard.md`: the answer to the open question, the
evidence for it, an explicit INSUFFICIENT EVIDENCE option, and a separate statement of
what it changes. Referee reticence is recorded as reticence, not as a negative
inference.

### Step 6 — Close the loop with the candidate

If the reference raises something material, put the substance to the candidate before
deciding. They may have context; they may disagree; a decision made on an unexamined
third-party account of a disputed event is the kind that turns out wrong and is
indefensible afterwards.

Never attribute. "Something came up about how the Meridian project ended — can you walk
me through it?" gets the answer without exposing the referee.

---

## Output Format

```markdown
## Reference check — [candidate], [role]

### Open question carried from debrief
1. [the specific uncertainty]
   *If resolved badly, would it change the decision?* [yes / no — if no, do not call]

### Consent
- Referees named by candidate: [list, with relationship and period]
- At least one former manager: [yes / no — if no, asked and the reason given]
- Current employer contacted: [no / yes, with explicit specific permission on date]

### Calls
#### [Referee], [relationship], [period], [date of call]
| Question | Answer | Evidence given |
|---|---|---|
**On the open question:** [what they said]
**Reticence noted:** [none / policy-limited / other — recorded, not interpreted]

### Result
| Open question | Verdict | Evidence | Insufficient evidence? |
|---|---|---|---|

**What this changes:** [nothing / proceed with this development plan / do not proceed]

### Put to the candidate
- Raised: [substance, no attribution] on [date]
- Their account: [summary]

### Unsolicited information received
[none / received and not acted on as evidence; substance put to candidate]
```

---

## Verification

- [ ] The open question was written down before any call
- [ ] If there was no open question, the call was skipped and that was recorded
- [ ] Every referee was named or explicitly agreed by the candidate
- [ ] No current employer was contacted without specific permission
- [ ] At least one referee managed the candidate, or the absence is explained
- [ ] Questions invite calibration; none is a leading yes/no
- [ ] The open-question probe is behavioural and does not name the concern as a concern
- [ ] Reticence is recorded as reticence, not interpreted as a negative
- [ ] Anything material was put to the candidate before the decision
- [ ] No backchannel enquiry was made

**False-positive prevention.** The dominant failure is treating a lukewarm reference as
a negative signal. Referees are lukewarm for many reasons unrelated to the candidate:
company policy, weak recollection, a rushed call, discomfort with the format, a bad
relationship that was mutual. A single hesitant reference is not evidence of anything.
What is evidence: a specific behavioural account, given unprompted, that recurs across
two referees.

The inverse failure matters as much. A glowing reference from a friend is the default
outcome of asking a candidate to nominate people who like them, and it should not
increase confidence. Weight the specificity, not the warmth: a referee who says "top
quarter of the twelve engineers I've managed, because she was the only one who would
rewrite her own work after review" has told you something. "He was great to work with"
has not.

The third failure is asking leading questions about the concern. "Were they
disorganised?" produces a yes from a referee trying to be helpful. Ask for the
situation and let the behaviour describe itself.

The fourth is letting the reference decide. It resolves one question. If the loop
produced a hire recommendation and the reference corroborates the candidate's own
account of a difficult period, that is a pass, not a flag.

**Evidence-anchored, bias-checked and legally careful**, per this domain's standing
principles — with consent as the additional gate that this stage, uniquely, can violate.

---

## Related

- `hr_interview_loop_design.md` — where the open question comes from
- `hr_structured_scorecard.md` — the recording discipline this borrows
- `../performance-reviews/hr_reviewer_approach_guide.md` — evidence-gathering for reviews
- `../../domain-legal/employment-labor/` — what may be asked and disclosed
