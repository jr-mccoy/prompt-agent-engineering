---
title: "Exit Interview — Run by Someone Neutral, Aggregated Before Acted On"
category: hr-management/people-ops
description: "Run and use an exit interview: separating regretted from non-regretted attrition, an interviewer who is not the departing person's manager, questions that surface the decision's real trigger and its earlier reversible moment, confidentiality stated honestly, and aggregation across leavers before anything is acted on. Refuses manager-run exits and single-leaver policy changes."
techniques:
  - ST-02
  - CM-01
  - RT-09
  - QA-04
  - OC-03
difficulty: intermediate
tags:
  - attrition
  - exit-interview
  - retention
  - people-analytics
  - confidentiality
updated: "2026-09-22"
related_prompts:
  - domain-hr-management/people-ops/hr_compensation_banding.md
  - domain-hr-management/performance-reviews/hr_calibration_facilitator.md
  - domain-hr-management/onboarding/hr_onboarding_thirty_sixty_ninety.md
---

# Exit Interview

**Objective:** Get truthful, usable information from someone leaving, and convert it into
change without over-reacting to one voice. Output: an attrition classification, a
conversation run by someone who is **not** their manager, the decision's real trigger
and the earlier moment at which it was still reversible, an honest confidentiality
statement, and a finding that is only acted on once it appears across leavers.

**When to Use:**
- Someone has resigned and you want to know why, actually.
- Attrition has risen and you have exit notes that say "pursuing a new opportunity".
- You want a process that produces something other than politeness.

**When NOT to use:**
- The person is being dismissed or made redundant. That conversation has different
  legal and human requirements and must not be repurposed as data collection.
- You want to change someone's mind — that is a retention conversation, and it happens
  **before** the resignation, which is most of this prompt's point.
- You need to review a completed decision's quality rather than a departure — route to
  `../../domain-decision-making/documentation/decisiondoc_after_action_report.md`.
- You need a team retrospective after an incident — route to
  `../../domain-risk/risk_after_action_review.md`.

---

## Method

### Step 1 — Classify the attrition before scheduling anything

Not all departures deserve the same attention, and pretending otherwise wastes the
process.

| Class | Meaning | What the exit interview is for |
|---|---|---|
| **Regretted** | You wanted to keep them | The full conversation. This is where the value is |
| **Non-regretted** | Performance or fit was already a live issue | Short and courteous. Their view still matters, but do not mine it for policy |
| **Structural** | Relocation, study, family, career change out of the field | Brief. The cause is not you, and pressing for a hidden reason is intrusive |

Classify honestly and before the conversation. Retrospectively reclassifying a
regretted departure as non-regretted is the commonest way organisations avoid learning
anything.

### Step 2 — Do not let their manager run it

The manager is frequently a cause, is always a party, and holds a reference the person
may need. A leaver will not tell their manager that their manager was the reason.

Run it: HR or people ops, a skip-level, or a neutral peer manager. If the organisation
is too small for any of those, use a written form and say plainly who will read it —
a small company cannot manufacture anonymity, and pretending it can is worse than
admitting it cannot.

### Step 3 — State confidentiality honestly

Say exactly what will happen to what they say:

- Who reads the raw notes.
- What is aggregated and what is attributed.
- Whether their manager will see it, and in what form.
- What you are **obliged** to act on regardless of their wishes — a disclosure of
  harassment, discrimination or a safety issue cannot be held in confidence, and
  they must know that before they speak, not after.

Overpromising confidentiality and then breaking it is the fastest way to make every
future exit interview useless, because people talk to each other after they leave.

### Step 4 — Time it properly

Best in the **last week**, once they have disengaged enough to be candid and while
detail is fresh. Not on the last day, which is logistics and goodbyes.

Then a second, optional contact **three to six months later**. Ex-employees are
markedly more honest once the new job has started and nothing is at stake, and that
follow-up routinely produces the real reason when the exit interview produced the
polite one.

### Step 5 — Ask questions that find the trigger and the reversible moment

Most exit notes record the *occasion* of leaving (a recruiter called) rather than the
*cause* (they had been open to a call for four months). Two questions do most of the
work:

- **"When did you first start thinking about leaving?"** Then: "what was happening
  then?" The gap between that date and the resignation is your actual window, and it is
  usually months.
- **"What would have had to change for you to stay?"** Asked without any attempt to
  act on it now. If the answer is something you could have done and did not know about,
  that is the finding.

The rest, ordered from easiest to hardest:

| Question | What it surfaces |
|---|---|
| "What was the best part of working here?" | What to protect — and it opens the conversation warmly |
| "What was the most frustrating part?" | The daily friction managers stop noticing |
| "How did the job compare to what you expected when you joined?" | A hiring or onboarding accuracy problem |
| "Did you have what you needed to do the job well?" | Tooling, clarity, access, authority |
| "How would you describe your manager's strengths, and where did they not help?" | Asked neutrally, by someone who is not them |
| "How did you find out about the opportunity you're going to?" | Whether you are losing people to one competitor or to a pattern |
| "Was compensation a factor? Where would it have needed to be?" | Feeds `hr_compensation_banding.md`'s compression audit |
| "Would you work here again? Would you recommend it to a friend?" | The summary judgement — and the honest answer to the second is often "yes, but not on that team" |
| "Is there anything you think we don't know?" | The catch-all, and it is where the significant disclosures usually arrive |

Ask the compensation question specifically. People leave over money and say it was
growth, because saying it was money feels mercenary. A direct question with a number
attached gets a direct answer, and it is the input the banding audit needs.

### Step 6 — Aggregate before acting

**The single most important discipline here: one leaver is an anecdote.**

A departing person is a self-selected sample, speaking at a moment of maximum
frustration, with imperfect visibility. Acting on one exit interview means restructuring
around the opinion of the person least invested in the outcome — and it is visible to
everyone who stayed.

So: log every exit against a fixed set of themes, review quarterly, and act when a
theme appears across independent leavers. The exception is a disclosure of harassment,
discrimination or a safety issue, which is acted on immediately and on its own.

| Theme | Leavers citing it | Regretted? | Same team? | Action threshold met? |
|---|---|---|---|---|

Cross-reference the themes with your 90-day checkpoints
(`../onboarding/hr_onboarding_thirty_sixty_ninety.md`): if leavers consistently say the
job differed from expectations, the defect is upstream in the posting and the loop.

### Step 7 — Close the loop with the people who stayed

When an aggregated theme produces a change, say so — that it came from exit feedback,
without attributing it. It is the only evidence current employees have that the process
is more than a formality, and it markedly improves what the next leaver tells you.

---

## Output Format

```markdown
## Exit interview — [role], [tenure], [last day]

**Attrition class:** regretted / non-regretted / structural — because [reason]
**Interviewer:** [name, role] — *not the departing person's manager*
**Confidentiality stated:** who reads raw notes · what is aggregated · what the manager
sees · what must be acted on regardless
**Timing:** [date, in the final week] · Follow-up scheduled: [date, +3–6 months]

### The decision
| | |
|---|---|
| First started thinking about leaving | [date] — [what was happening] |
| **Reversible window** | [months between that and resignation] |
| Occasion of resignation | |
| What would have had to change to stay | |
| Compensation a factor? | [y/n — and the number, if given] |
| How they found the new role | |

### Responses
| Question | Response | Theme |
|---|---|---|

### Would work here again / recommend
[answer, verbatim where possible]

### Anything we don't know
[verbatim]

### Disclosures requiring action regardless of confidentiality
[none / substance, routed to [who] on [date]]

---
## Quarterly aggregation
| Theme | Leavers | Regretted | Concentrated in one team? | Threshold met | Action | Owner |
|---|---|---|---|---|---|---|

**Acted on this quarter:** [change] — communicated to staff on [date], attributed to
exit feedback without naming anyone
```

---

## Verification

- [ ] Attrition classified before the conversation, honestly
- [ ] The interviewer is not the departing person's manager
- [ ] Confidentiality stated specifically, including what must be acted on regardless
- [ ] Held in the final week, not on the last day
- [ ] A 3–6 month follow-up is scheduled
- [ ] "When did you first start thinking about leaving" was asked, and the reversible
      window computed
- [ ] The compensation question was asked directly, with a number invited
- [ ] Responses are logged against fixed themes
- [ ] No policy change is proposed from this single interview
- [ ] Any harassment, discrimination or safety disclosure was routed immediately
- [ ] Aggregated changes are communicated back to current staff

**False-positive prevention.** The dominant failure is acting on one articulate
leaver. The information is real but the sample is one, self-selected, at peak
frustration, and partially informed. Restructuring on it is how organisations make
changes that the people who stayed can see are wrong. Aggregate, with a stated
threshold, and hold the line — with the single exception of a disclosure you are
obliged to act on.

The second failure is the manager-run exit interview, which reliably produces
"pursuing a new opportunity" and nothing else. If a leaver's answer to the manager
question is uniformly positive and the rest of the interview is thin, check who ran it.

The third failure is overpromising confidentiality. A small organisation cannot make a
single leaver's feedback unattributable, and saying otherwise means the next person
finds out and tells nobody anything. State the real limits.

The fourth is recording the occasion as the cause. "A recruiter called" is not why they
left; it is when they answered. The first-thought question is what locates the actual
cause, and the months between are the window you could have used.

**Legally careful, per this domain's standing principles. This is not legal advice.**
Disclosures of harassment, discrimination or safety issues carry mandatory obligations
in most jurisdictions that override any confidentiality you offered; data-protection
rules govern how exit notes are stored and how long; and notes can be discoverable in
a later claim. Route disclosures per policy immediately and see
`../../domain-legal/employment-labor/`.

---

## Related

- `hr_compensation_banding.md` — consumes the compensation answers for its compression audit
- `../onboarding/hr_onboarding_thirty_sixty_ninety.md` — where job-versus-expectation themes point
- `../hiring/hr_job_description_writer.md` — the upstream fix when expectations mismatch
- `../performance-reviews/hr_calibration_facilitator.md` — where rating-fairness themes belong
- `../../domain-negotiation/difficult-conversations/difficultconvo_post_review.md` — the adjacent hard conversation
