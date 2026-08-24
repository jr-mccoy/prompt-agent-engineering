---
title: "Follow-Up & Deadline Tracker — Chase What Is Outstanding Without Weakening the Record"
category: advocacy
description: "Help a person track what they are waiting on across one or more open requests — the response window they set, commitments made to them with dates, and conditions they must meet — and draft proportionate follow-ups when a date passes. Does NOT state or validate legal deadlines, tell the user how long an organization has to respond as a matter of law, predict outcomes, or draft escalating threats. Legal time limits route to an attorney or legal aid. Not legal advice."
techniques:
  - CM-01
  - DS-01
  - DS-21
  - ST-03
  - QA-01
difficulty: intermediate
intended_use: model-testing
tags:
  - written-advocacy
  - self-advocacy
  - follow-up
  - documentation
  - record-keeping
  - consumer
updated: "2026-08-01"
related_prompts:
  - domain-written-advocacy/cross-cutting/advocacy_response_analyzer.md
  - domain-written-advocacy/cross-cutting/advocacy_escalation_ladder_designer.md
  - domain-written-advocacy/cross-cutting/advocacy_correspondence_log_builder.md
  - domain-written-advocacy/cross-cutting/advocacy_request_letter_architect.md
---

**Purpose:** Help you keep track of **what you are waiting on** across your open requests — the response windows you set, the commitments made to you with dates attached, and the conditions you were asked to meet — and write a proportionate follow-up when a date passes. The aim is a short, factual chase that strengthens the record rather than a stream of increasingly annoyed emails that weakens it.

**When to use:** You have one or more requests outstanding, dates are passing, and you want a single view of what is due when and what to send.

**When NOT to use:** A reply arrived and you are unsure what it commits to → `advocacy_response_analyzer.md`. Internal follow-ups have run out and you need to escalate → `advocacy_escalation_ladder_designer.md`. You need to know a legal time limit for a claim, appeal, or dispute → that is legal analysis; route to an attorney or legal aid immediately.

---

## Boundary & Routing Block

Use a different pathway if:
- **A legal claim, appeal, or dispute deadline may be running** — these are strict, they differ by matter and jurisdiction, and **waiting for a company to reply does not necessarily pause them.** This prompt tracks only the windows *you* set and the dates *they* gave you. **Any legal time limit is for an attorney or legal aid** — contact them promptly rather than after the follow-up cycle.
- **You have been sued, threatened with suit, or served with anything** → route to an attorney or legal aid; do not manage it as a follow-up schedule.
- **The organization stated a deadline for you to act** → note it, meet it if you can, and route the question of whether it is accurate or the only applicable one to an attorney.
- **The matter involves suspected fraud or identity theft** → official reporting channels take priority over a follow-up schedule.
- **The other party is an abuser or subject to a protective order** → do not contact them directly; route through counsel or an advocate.

This prompt is educational support for organizing your own correspondence. It is not a substitute for legal services.

---

## Scope Boundary — Read First

This **tracks the response windows you set and the dates you were given, and drafts your own follow-ups**. It is **not legal advice, legal strategy, a legal filing, or a substitute for an attorney, legal aid, or your jurisdiction's law.** It will **not** tell you how long an organization has to respond as a matter of law; state, validate, or calculate any legal claim, appeal, or limitation deadline; tell you whether waiting affects a deadline; predict whether a follow-up will produce a response; assess how strong your position is; cite a statute or regulation as authority; or draft a threat. Statutory response periods and limitation periods **vary by matter, state, and country and change over time** — every date in this tracker is one you set or one they gave you, never one this prompt supplies.

---

## Core Principles

1. **Track only two kinds of date: the window you set, and the date they gave you.** Everything else — how long they "should" take, what the law allows — is outside this tool and belongs to an attorney.
2. **A follow-up restates; it does not re-argue.** Reference the original letter by date and delivery proof, restate the unchanged ask in one line, and ask for a response by a new date. Rewriting the case from scratch invites a fresh round of the same non-answer.
3. **Escalate the rung, not the volume.** When two follow-ups produce nothing, the answer is a different recipient, not a louder message to the same one. Tone should stay flat as the record grows.
4. **Space follow-ups so the record reads as reasonable.** Chasing the day after a window closes reads as impatient; chasing three months later reads as abandoned. A short interval, applied consistently, reads as diligent.
5. **A missed commitment is a distinct and valuable fact.** "On [date] you said the refund would issue by [date]; as of [date] it has not" is far stronger than a general complaint about delay, and it names the thing that failed.
6. **Track your own conditions too.** If they are waiting on something from you, that is not their delay. Meeting the condition — and recording that you did, with the date — removes their reason and restarts the clock cleanly.
7. **You track and chase; the professional handles time limits.** Whether any legal clock is running, and what pauses it, is for an attorney. Stop at the boundary.

---

## Your Input

- **Your jurisdiction (state/city/country):** [required]
- **Open items:** [for each: what was requested, recipient, date sent, channel, delivery proof, response window you set]
- **Commitments made to you:** [what, by whom, promised by when, source — letter or call]
- **Conditions you were asked to meet:** [what, by when if stated, whether you have done it]
- **Follow-ups already sent:** [dates and whether answered]
- **Today's date:** [YYYY-MM-DD]
- **Any legal claim, appeal, or dispute deadline you are aware of:** [flag → Boundary & Routing Block; route to an attorney]
- **Any legal dispute, fraud, or safety dimension?:** [if yes → Boundary & Routing Block]

---

## Constraints

**Must:**
- Require the jurisdiction and today's date; use only windows the user set and dates the organization gave.
- Route any legal claim, appeal, or limitation deadline to an attorney or legal aid before scheduling anything.
- Show each open item with what is due, when, from whom, and its current status.
- Track commitments and user-side conditions separately from response windows.
- Keep every follow-up short, factual, and unchanged in its ask, referencing the original by date and delivery proof.
- Recommend escalation rather than a third follow-up to the same recipient.
- Keep tone flat across successive follow-ups.
- Flag missing dates and delivery proof as `[NEED DATE:]` / `[NEED DOCUMENT:]`.

**Must Not:**
- State how long an organization has to respond as a matter of law, or cite any statutory response period.
- State, validate, calculate, or imply any legal claim, appeal, or limitation deadline.
- Suggest that waiting for a reply pauses, extends, or preserves any legal deadline.
- Predict whether a follow-up will produce a response or a favourable outcome.
- Assess how strong the user's position is.
- Escalate the tone, add new demands, or introduce a legal threat in a follow-up.
- Characterize the organization or attribute motive to a delay.
- Invent a send date, delivery proof, or commitment the user did not supply.

---

## Instructions

### Stage 1 — Screen for Safety and Frame the Matter
Screen for a legal claim, appeal, or limitation deadline, an active dispute, a fraud dimension, or a safety concern → route per the Boundary & Routing Block **before** building any schedule. Restate the jurisdiction and today's date, and confirm the boundary: this tracks the user's own windows; legal time limits are for an attorney.

### Stage 2 — Inventory What Is Outstanding
List every open item: what was requested, from whom, when it was sent, by what channel, what proof of sending exists, and the response window the user set. Flag missing dates and proof rather than estimating them.

### Stage 3 — Separate Commitments and Conditions
Build two further lists: commitments made *to* the user with dates and owners, and conditions placed *on* the user. Mark which conditions are met and when. Anything waiting on the user is not the organization's delay and should not be chased as if it were.

### Stage 4 — Compute Status Against Today
For each item, compare its due date to today and mark: not yet due, due today, overdue by n days, or met. Rank the overdue items by how long they have been outstanding. Use only supplied dates.

### Stage 5 — Decide the Action for Each Overdue Item
Choose one action per item: wait (not yet due); meet an outstanding condition first; send a first follow-up; send a second and final follow-up; or escalate a rung. Apply the rule that a third chase to the same recipient becomes an escalation rather than another message.

### Stage 6 — Draft the Follow-Ups and Close
Compose each due follow-up in the user's first-person voice — short, factual, unchanged in its ask, referencing the original letter by date and delivery proof, and setting a new response date. Set the next review date. Route legal time-limit questions to an attorney or legal aid.

---

## Output Format

```markdown
MY OWN FOLLOW-UP TRACKER — NOT A LEGAL FILING
Prepared [YYYY-MM-DD]. Every date here is one I set or one they gave me. This tracker does NOT
state how long anyone has to respond in law, calculate or validate any legal deadline, suggest
that waiting preserves any deadline, or predict any outcome. Legal time limits are for an
attorney or legal aid — I will contact them separately and promptly if any may apply.

## Open items
| # | What I asked for | Recipient | Sent | Proof | Window I set | Due | Status |
|---|---|---|---|---|---|---|---|
| 1 | [ask] | [org / dept] | [YYYY-MM-DD] | [receipt / ticket #] | [14 days] | [YYYY-MM-DD] | Overdue [n] days |
| 2 | [ask] | [org / dept] | [YYYY-MM-DD] | [NEED DOCUMENT:] | [30 days] | [YYYY-MM-DD] | Not yet due |

## Commitments made to me
| What | By whom | Source | Promised by | Status as of today |
|---|---|---|---|---|
| [refund $X] | [name / dept] | [call YYYY-MM-DD] | [YYYY-MM-DD] | Not received — overdue [n] days |

## Conditions on me
| Condition | Asked on | Due (if stated) | Done? | Date done |
|---|---|---|---|---|
| [send proof of purchase] | [YYYY-MM-DD] | [YYYY-MM-DD] | [Yes/No] | [YYYY-MM-DD] |

## Action for each item
| # | Action | Why |
|---|---|---|
| 1 | Send first follow-up | Window closed [n] days ago; no response |
| 2 | Wait | Not due until [date] |
| 3 | Escalate one rung | Two follow-ups sent, no response — see escalation ladder |
| 4 | Meet condition first | They are waiting on me; this is not their delay |

## Follow-up message (my own words)
> Re: [subject] — account [#]. Follow-up to my letter of [date].
>
> I wrote to you on [date] via [channel] requesting [the ask]. [Proof: certified mail receipt
> [#] / ticket [#] / sent copy.] I asked for a response by [date] and have not received one.
>
> My request is unchanged: [the ask, one line].
>
> Please respond in writing by [new date].
>
> [Your name], [account #], [YYYY-MM-DD]

## Second and final follow-up (if the first produces nothing)
> Re: [subject] — account [#]. Second follow-up.
>
> I wrote on [date] and followed up on [date]; I have had no response to either.
> [Proof: ...]
>
> My request is unchanged: [the ask].
>
> Please respond in writing by [new date]. If I do not hear from you, I will take this up
> through your complaints process.
>
> [Your name], [account #], [YYYY-MM-DD]

## Next review: [YYYY-MM-DD]

---
Note to self: this is my own tracker, not legal advice. The dates here are mine or theirs, not
legal deadlines. If any legal claim, appeal, or limitation period may apply to this matter, that
is for an attorney or legal aid and waiting on a reply may not pause it.
*Verify for your jurisdiction — response periods and time limits vary by matter, state, and country.*
```

---

## Verification

- [ ] Jurisdiction and today's date captured; any possible legal deadline routed to an attorney *before* scheduling?
- [ ] Every open item shows request, recipient, send date, proof, window, due date, and status?
- [ ] Commitments and user-side conditions tracked separately from response windows?
- [ ] Status computed only from dates the user supplied?
- [ ] No statutory response period or legal time limit stated, calculated, or implied?
- [ ] No suggestion that waiting for a reply preserves or extends any deadline?
- [ ] Every follow-up short, factual, and unchanged in its ask?
- [ ] Each follow-up references the original by date and delivery proof?
- [ ] Tone flat across successive follow-ups, with no escalating threat?
- [ ] Third chase to the same recipient converted into an escalation?
- [ ] No outcome prediction, strength assessment, or motive attribution?
- [ ] Missing dates and delivery proof flagged `[NEED …:]`, not estimated?
- [ ] Legal-dispute, fraud, or safety dimension screened and routed?

---

## False-Positive Prevention

| ❌ Don't | ✅ Do |
|---|---|
| "They legally have 30 days to respond" | Track only the window *you* set; statutory periods are for an attorney |
| "You still have two years to bring a claim" | Do not state or calculate any limitation period; route to an attorney or legal aid |
| "Keep waiting — the clock is paused while they review" | Never imply waiting preserves a deadline; route the timing question to an attorney |
| "One more email and they'll respond" | Make no prediction; choose the action by the rule, not by hope |
| Third follow-up to the same inbox, more strongly worded | Escalate the rung instead — see the escalation ladder |
| "Respond this week or I'm taking legal action" | "Please respond in writing by [date]" — threats route to an attorney |
| "They're stalling deliberately" | "No response as of [date], [n] days after the date I requested" |
| Chase an item that is waiting on the user's own document | Mark it a condition on you; meet it and record the date |
| Estimate the send date because the user cannot recall | Flag `[NEED DATE:]` / `[NEED DOCUMENT:]` |
| Manage a served claim or lawsuit as a follow-up schedule | Stop, use the Boundary & Routing Block, route to an attorney |

---

## Adaptations

**By item type:**
- **Commitment with a date:** Chase on the date named, quoting the commitment and its source; this is the strongest kind of follow-up.
- **Commitment with no date:** The first follow-up asks for the date rather than the outcome — that converts a vague promise into a trackable one.
- **Conditional on you:** Meet the condition, record the date and proof of sending, and only then treat the clock as running.
- **No acknowledgement at all:** Note that even receipt was never confirmed; that fact carries into the escalation.

**By situation/profile:**
- **Several open items with one organization:** Number them and chase in a single letter with a numbered list; separate emails get separate tickets and lose the pattern.
- **Items across several organizations:** Keep one tracker but sort by due date, so the next action is always visible at the top.
- **Long-running matter:** Note the total elapsed time since the first request — a plain fact that carries weight at escalation.
- **Legal, fraud, or safety dimension:** Boundary & Routing Block first; do not schedule around a possible legal deadline.

---

## Related Prompts

- `advocacy_response_analyzer.md` — when a reply arrives and you need to know what it committed to.
- `advocacy_escalation_ladder_designer.md` — when follow-ups are exhausted and the rung must change.
- `advocacy_correspondence_log_builder.md` — the running record this tracker draws its dates from.
- `advocacy_request_letter_architect.md` — the original request being chased.
