---
title: "Sourcing Outreach — Specific, Honest, and Easy to Decline"
category: hr-management/hiring
description: "Write outreach to a passive candidate: the specific reason you approached this person, what the role would give them that their current one does not, compensation stated up front, and an explicit easy decline. Refuses templated flattery, undisclosed ranges, and multi-touch sequences that ignore a no."
techniques:
  - CM-01
  - ST-03
  - NE-23
  - QA-04
  - OC-03
difficulty: beginner
tags:
  - hiring
  - sourcing
  - outreach
  - passive-candidates
  - candidate-experience
updated: "2026-09-22"
related_prompts:
  - domain-hr-management/hiring/hr_job_description_writer.md
  - domain-hr-management/hiring/hr_interview_loop_design.md
  - domain-hr-management/people-ops/hr_compensation_banding.md
---

# Sourcing Outreach

**Objective:** Write outreach a passive candidate will answer: one specific reason you
approached **them**, an honest account of what this role offers that their current one
does not, the compensation range stated in the first message, and a decline made
genuinely easy. Templated flattery, undisclosed ranges and sequences that continue past
a no are refused.

**When to Use:**
- You are approaching someone who is not looking, by email, LinkedIn or referral.
- Your outreach response rate is low and you suspect the message rather than the list.
- A hiring manager wants to reach out personally and asked for help with the wording.

**When NOT to use:**
- You are writing **sales** outreach — that is
  `../../domain-agentic-resources/skills/marketing/cold-email/`. Different reader,
  different artifact, different ask: a sales email opens a commercial conversation; this
  asks someone to consider changing their livelihood, which is a larger favour and
  carries different honesty obligations.
- You are writing the posting itself — that is `hr_job_description_writer.md`.
- You are recruiting volunteers rather than employees — route to
  `../../domain-biblical-studies/church-staff-ministry-ops/biblical_churchstaff_volunteer_recruitment_role_design.md`.
- You are negotiating an offer with someone already in process — that is
  `../../domain-negotiation/contexts/negotiation_hiring_offer_employer_side.md`.

---

## Context Gathering

1. **This specific person**
   - "What did you actually see that made you contact them — a project, a talk, a
     commit, a paper, a referral?"
   - "What are they doing now, and roughly how long have they been doing it?"
   - "What would plausibly be frustrating about their current situation?"

2. **The role, honestly**
   - "What does this role offer that their current one probably does not?"
   - "What would they be giving up?"
   - "Compensation range, level, location and remote policy."

3. **Your position**
   - "Why would they believe you? Do you have a shared connection, a public artifact,
     a reputation in this niche?"
   - "Who is sending this — a recruiter, the hiring manager, a future peer?"

If the answer to the first question is "they came up in a search for the job title",
stop. There is no honest specific reason, and a message that pretends otherwise is the
one that gets ignored. Either find a real reason or send a short, plainly generic
message that admits what it is — which performs better than fake personalisation.

---

## Method

### Step 1 — Lead with the specific reason

The first sentence names what you saw. Not "your impressive background" — the thing.

| Fails | Works |
|---|---|
| "I was impressed by your experience at Acme" | "I read your write-up on cutting the Acme deploy pipeline from 40 to 6 minutes" |
| "Your profile stood out" | "Priya said you were the person who untangled their billing migration" |
| "I'm reaching out to top talent in the space" | "You've maintained `libfoo` for six years, which is most of why I'm writing" |

The test: could this sentence be sent to a hundred people? If yes, it is not a reason,
it is a greeting.

### Step 2 — State the ask in one sentence, and make it small

The ask is a conversation, not an application. "Would you be open to a 20-minute call
in the next couple of weeks?" is a real ask. "Apply here" asks a passive candidate to
do work before they know anything.

### Step 3 — Say what is in it for them, specifically

One or two things this role offers that theirs plausibly does not: scope, ownership,
technical problem, stage, team, compensation, remote policy, reduced travel. Grounded
in what you know about their situation, not in what you think is exciting about your
company.

And name what they would give up — a smaller company means less stability, a bigger one
means more process. Saying it costs nothing and is the single strongest credibility
signal available in a cold message.

### Step 4 — Put the compensation range in the first message

Not "competitive". Not "depends on experience". The range, the level, and the location
policy that affects it.

This is the highest-leverage line in the message. It respects the reader's time, it
removes the most common reason a conversation dies at stage four, and it signals that
you are not going to waste three weeks before disclosing something you already knew.
Where publication is legally required, it is required anyway.

Range from `../people-ops/hr_compensation_banding.md`.

### Step 5 — Make declining genuinely easy

An explicit line: "if this isn't interesting, no reply needed at all — and if you know
someone it might suit, I'd welcome the pointer."

Two effects. It raises response rates, because the reader is not agreeing to a
negotiation by replying. And it is honest: they owe you nothing.

### Step 6 — Keep it short, and bound the follow-up

Under 150 words. A passive candidate reads it on a phone between other things.

Follow-up rule: **one** follow-up, at least a week later, shorter than the first, adding
one new piece of information rather than repeating. Then stop. A third message is not
persistence; it is a decision that your convenience outweighs their silence, and it is
remembered.

**A no ends the sequence immediately.** Any tooling that continues touching after a
decline is not a sequence design problem, it is a respect problem, and it damages the
employer brand far beyond the one candidate.

---

## Output Format

```markdown
## Outreach — [name], [role]

**Specific reason:** [what you actually saw]
**Sender:** [who, and why them]
**Range disclosed:** [the range]

### Message
> Subject: [specific — names the thing, not the role]
>
> [1: the specific reason you're writing]
> [2: the ask, small and dated]
> [3: what this offers them that their current role plausibly doesn't — and what they'd give up]
> [4: range, level, location policy]
> [5: the easy decline, plus the referral invitation]

**Word count:** [must be under 150]

### Follow-up (one only)
**Send:** [date, ≥7 days later] · **Adds:** [the one new thing]
> [shorter than the first message]

**Then stop.** A decline ends the sequence immediately.
```

---

## Verification

- [ ] The first sentence names something specific that could not be sent to a hundred people
- [ ] The ask is a short conversation, not an application
- [ ] What they would give up is stated, not only what they would gain
- [ ] The compensation range appears in the first message
- [ ] An explicit easy-decline line is present
- [ ] Under 150 words
- [ ] Exactly one follow-up is planned, adding new information
- [ ] A decline ends the sequence

**False-positive prevention.** The dominant failure is fake personalisation — a
templated message with one variable slot filled from a profile. Readers detect it
immediately, and it performs worse than an honest generic note, because it adds a small
deception to an unsolicited request. If there is no real reason, either find one or
write the generic message and say so: "I don't know your work, but your background
matches something I'm hiring for closely enough that it seemed worth one message."

The second failure is withholding the range to preserve negotiating room. What it
actually preserves is the risk of discovering at stage four that you were never in the
same range, having spent the candidate's time and your interviewers'. The information
asymmetry is not worth the cost.

The third is a multi-touch sequence borrowed from sales tooling. Sales cadences assume
a business buyer evaluating a purchase; this is a person being asked to consider
leaving their job. Four automated touches read as harassment and are discussed
publicly.

**Legally careful, per this domain's standing principles.** Outreach that references a
protected characteristic — even approvingly, even as diversity-motivated encouragement —
creates exposure. Reference work, not identity. And check whether your jurisdiction
requires pay disclosure in the first communication; several now do.

---

## Related

- `hr_job_description_writer.md` — the role this outreach points at
- `hr_interview_loop_design.md` — what happens if they say yes, which the message should be able to summarise
- `../people-ops/hr_compensation_banding.md` — the range
- `../../domain-agentic-resources/skills/marketing/cold-email/` — the sales counterpart, deliberately different
