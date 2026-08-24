---
title: "Meeting Pre-Read Drafter — The Document That Front-Loads a Decision Meeting"
category: business-strategy/chief-of-staff
description: "Draft the pre-read sent to attendees before a high-stakes decision meeting — the artifact, not the prep ritual. Front-loads the reading so the meeting decides rather than presents: decision sought, one-paragraph context, only the relevant data, 2–4 real options, a recommendation, the questions the meeting must resolve, and an explicit definition of success. Counters the meeting that spends 25 minutes on background and 5 on the decision."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - DS-01
  - CM-02
  - QA-01
difficulty: intermediate
tags:
  - chief-of-staff
  - meetings
  - decision-making
  - executive-communication
  - pre-read
updated: "2026-06-18"
reasoning:
  styles: [analytic, structured, persuasive, decision_oriented]
  stakes: moderate
  horizon: days
  uncertainty: ambiguity
  evidence_quality: moderate
  domain_complexity: single_domain
  collaboration: small_team
  output_format: [memo, structured]
  user_role: [executive, chief_of_staff, pm, founder, analyst]
  mode: [document, decide, synthesize]
related_prompts:
  - domain-business-strategy/chief-of-staff/cos_meeting_prep_and_process.md
  - domain-decision-making/documentation/decisiondoc_options_memo.md
  - domain-policy/policy_options_memo.md
---

# Meeting Pre-Read Drafter

**Objective:** Draft the pre-read document that goes to attendees before a high-stakes meeting whose purpose is to *decide*, not to be presented to. The pre-read front-loads everything readable so the meeting itself is spent on judgment, debate, and decision. It states the decision sought, gives one paragraph of context, includes only the data that bears on the decision, lays out 2–4 genuine options, makes a recommendation, lists the questions the meeting must resolve, and defines what leaving with a decision looks like. A good pre-read is the reason a decision meeting can be 30 minutes instead of an hour.

This is the artifact, distinct from `cos_meeting_prep_and_process.md`, which covers preparing for and processing a meeting. This prompt produces the document attendees read beforehand.

**When to use:**
- A meeting exists to make a specific decision and you want it to actually make that decision.
- Convening senior people whose time is expensive and who should arrive informed.
- Replacing a "let me walk you through some slides" meeting with a decision meeting.
- Any recurring forum (steering committee, exec staff) where decisions stall because background eats the clock.

**When NOT to use:**
- The meeting is a working session, brainstorm, or status sync with no decision to make — a pre-read forcing a decision is the wrong shape.
- You need a full options analysis as a standalone deliverable — use `decisiondoc_options_memo.md` or `policy_options_memo.md`; the pre-read is leaner.
- The decision is trivial or already made — a pre-read is overhead.

**Audience:** Chiefs of staff, executives, founders, product leaders, and anyone who owns a decision meeting and wants it to produce a decision.

---

## Inputs / Context

1. **The decision sought.** The specific choice the meeting must make — phrased as a decision, not a topic.
2. **The decider(s).** Who has authority to decide, and who else is in the room.
3. **Context.** The minimum background needed to make this decision make sense.
4. **The options.** The 2–4 real paths, including any do-nothing.
5. **Relevant data.** The few facts that actually bear on the choice.
6. **Your recommendation.** Which option you favor and why (or "no recommendation, need the room").
7. **Meeting length.** The time budget the pre-read is meant to protect.

---

## Constraints

### Must
- State the **decision sought** at the very top, as a specific decision ("approve X for $Y by Z"), not a topic ("discuss X").
- Keep **context to one paragraph.** If background needs more, the meeting is not ready to decide.
- Include **only data that bears on the decision.** Every chart or number must change someone's answer; if it wouldn't, cut it.
- Present **2–4 genuine options**, each with its tradeoff — not one real option and decoys.
- Make a **recommendation** with reasoning, or explicitly say "no recommendation — here's why the room must decide."
- List the **key questions the meeting must resolve** — the open points debate should focus on.
- Define **what success looks like**: "we leave having decided X by [criterion], with owner and date." Make the exit condition unambiguous.
- Be **short enough to read in 5–10 minutes.** The pre-read trades reading time for meeting time; it fails if it is itself a deck.

### Must Not
- Open with background and bury the decision on page 3.
- Pad with context that doesn't change the decision.
- Present a fake set of options where only one is viable.
- Hide the recommendation, or make a recommendation while pretending to be neutral.
- Leave the success condition vague ("align on next steps") so the meeting can end without deciding.
- Turn the pre-read into a presentation — if it needs to be walked through, it isn't a pre-read.

---

## Instructions

1. **Write the decision sought first.** One sentence, phrased as the actual choice with its parameters (what, how much, by when). If you cannot phrase it as a decision, the meeting may not have a decision to make — flag that.
2. **Compress context to one paragraph.** Give only the background a reader needs to understand why this decision is live now. Cut history that doesn't bear on the choice.
3. **Curate the data.** Include the handful of facts that move the decision. For each, it should be obvious how it bears on which option. Delete anything decorative.
4. **Lay out the options.** Present 2–4 real options including do-nothing where relevant. For each: one-line description, the core tradeoff, and what it costs/requires. Options must be genuinely distinct and genuinely live.
5. **Recommend.** State which option you favor and the two or three reasons. Name the main argument against your recommendation and why it doesn't change your view. If you have no recommendation, say so and explain what the room needs to supply.
6. **List the questions the meeting must resolve.** Surface the open points — the disagreements, the unknowns, the judgment calls — so debate goes straight to them instead of rediscovering them.
7. **Define success.** Write the exit condition explicitly: "Success = we leave having decided [X], with [owner] accountable by [date]." Make it impossible to end the meeting ambiguously.
8. **Trim to reading length.** Cut until the whole thing reads in 5–10 minutes. If a section needs verbal walkthrough, either tighten it or move detail to an appendix the decision doesn't depend on.

---

## False-Positive Prevention

1. **Buried decision.** The decision sought appears late or is phrased as a topic. It must be the first line and phrased as a choice.
2. **Context bloat.** A page of history where a paragraph would do. If background exceeds a paragraph, the decision usually isn't ripe.
3. **Decorative data.** Charts that don't change anyone's answer. Every datum must bear on an option or be cut.
4. **Fake options.** Decoy alternatives that exist to make the preferred one look obvious. The room can tell, and it wastes the discussion.
5. **Hidden recommendation.** Pretending to be neutral while steering, or omitting a view you actually hold. State the recommendation or state honestly that you have none.
6. **Vague success condition.** "Align on next steps" lets the meeting end without deciding. Define the exit as a named decision with owner and date.
7. **Deck-in-disguise.** A pre-read so long it needs to be presented. If it can't be read in 5–10 minutes, it failed its purpose.
8. **Missing the do-nothing option.** Omitting status quo when it is a real choice. Inaction is a decision with consequences.
9. **Question-free pre-read.** No stated open questions, so the meeting rediscovers the disagreements live. Pre-list them.
10. **Unowned outcome.** A decision with no accountable owner or date attached, guaranteeing it doesn't move after the meeting.

---

## Output Format

```
# PRE-READ — [meeting], [date]
Read time: ~[N] min | Meeting length: [N] min

## Decision sought
> [The specific decision, with parameters: what / how much / by when.]
Decider(s): [name(s)]

## Context (one paragraph)
[Why this decision is live now. Only what's needed to understand the choice.]

## What matters (relevant data only)
- [Fact] → bears on [which option / how]
- [Fact] → [...]

## Options
### Option A — [name]
- What: [one line]
- Tradeoff: [...]
- Cost / requires: [...]

### Option B — [name]
[...]

### Option C / Do-nothing (as relevant)
[...]

## Recommendation
- Recommended: Option [X]
- Why: [2–3 reasons]
- Strongest argument against, and why it doesn't change the call: [...]
(or: "No recommendation — the room must supply [judgment / information].")

## Questions for the meeting
1. [open question / disagreement / judgment call]
2. [...]

## What success looks like
> We leave having decided [X], with [owner] accountable, by [date].

## Appendix (optional — not load-bearing for the decision)
[Detail a reader can skip and still decide.]
```

---

## Verification

- [ ] Decision sought is the first line and phrased as a specific choice.
- [ ] Context is one paragraph.
- [ ] Every data point bears on an option; nothing decorative.
- [ ] 2–4 genuine, distinct options including do-nothing where relevant.
- [ ] Recommendation stated (or explicit "no recommendation" with reason), including the best counter-argument.
- [ ] Questions the meeting must resolve are listed.
- [ ] Success defined as a named decision with owner and date.
- [ ] Whole pre-read reads in 5–10 minutes.
- [ ] No buried decision, no context bloat, no fake options.
- [ ] No vague "align on next steps" exit condition.
- [ ] Not a deck-in-disguise.
