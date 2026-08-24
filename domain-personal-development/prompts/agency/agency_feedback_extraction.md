---
title: "Extract Useful Feedback from People Who've Seen the Work"
category: personal-development/agency
description: "Convert informal reactions and polite compliments from people who've encountered the user's shipped work into concrete, usable signal — what actually landed, what didn't, and what to change, without depending on them to be expert critics."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - CM-02
  - QA-01
difficulty: intermediate
tags:
  - agency
  - feedback
  - signal-extraction
  - audience
  - iteration
updated: "2026-04-20"
related_prompts:
  - domain-personal-development/prompts/agency/agency_end_of_session_review.md
  - domain-personal-development/prompts/agency/agency_weekly_review.md
  - domain-personal-development/prompts/agency/agency_proof_of_work_portfolio.md
---

# Extract Useful Feedback from People Who've Seen the Work

**Objective:** Take a set of reactions, comments, DMs, and conversations from people who encountered the user's shipped work, and extract usable signal from them: what actually landed, what slid past, what confused, what to change. Treat feedback-givers as evidence, not authorities.

**When to use:** The user has shipped something (essay, app, talk, product, video) and received reactions of varying quality. They're trying to figure out what's real feedback and what's just noise or politeness. Or: they're preparing specific questions to ask real viewers before the next iteration.

**Audience:** The user, who cannot be objective about their own work. They want to translate other humans' messy reactions into a change-set.

---

## Inputs Required

1. **What was shipped.** One sentence describing the work and where it lived publicly.
2. **Who encountered it.** Rough description: strangers, peers, target audience, friends, mixed.
3. **Raw reactions.** The actual text (paste as much as possible) — DMs, comments, email, screenshots of conversations, verbatim recollections. Mixed-quality is fine.
4. **What the user was hoping the reactions would tell them.** One sentence. If they say "I want to know if it's good," push past that to specifics.
5. **Any numerical data** (views, completion rate, saves, shares, signups, retention) — if relevant.

If there are fewer than 5 distinct reactions, flag: the signal may be too thin to be useful, and the answer might be "ship to more people."

---

## Instructions

### Step 1 — Classify each reaction by type

Sort each reaction into one of these buckets. Quote the reaction verbatim and label it:

- **Politeness signal.** "Loved it!" "Great work!" "This is awesome." Low information — it tells you the sender is social, not that the work landed.
- **Specific-praise signal.** Names a specific part, phrase, feature, moment. Higher information; tells you something actually landed.
- **Specific-confusion signal.** Names a specific part that confused, tripped, or lost them. Very high information.
- **Specific-critique signal.** Names a specific part they would change, with a reason. High information.
- **Use-signal.** The person used the thing, referenced it, shared it forward, acted on it, came back for more. Highest information — behavior over words.
- **Off-topic signal.** Reaction is about something other than the work (meta-comments on the user, the medium, the author's career). Noise for this purpose.

Each reaction gets one label. Don't merge them.

### Step 2 — Weight by source and context

Adjust each reaction's weight based on:

- **Does the reactor match the target audience?** If yes, up-weight. If the work is for indie developers and the reactor is the user's mom, the reaction is not noise, but it's not target-audience signal either.
- **Did the reaction arrive unprompted or was it asked for?** Unprompted is stronger signal.
- **Did the reactor engage with the work itself or just the title/pitch?** Engagement-with-content is stronger.

Produce a short weighted view: which handful of reactions deserve the most weight, and why.

### Step 3 — Extract the actual findings

From the weighted reactions, produce three sections:

**What landed.** Points where specific-praise, use-signal, and behavior agree. One sentence each. No more than three findings; if you have more, rank and cut.

**What missed.** Points where specific-confusion or specific-critique cluster, or where use-signal was absent where it was expected. One sentence each. Max three.

**What's genuinely ambiguous.** Places where reactions conflict, or where you cannot tell from the signal available. List plainly; don't resolve falsely.

### Step 4 — Convert findings into change candidates

For each "missed" finding, write one candidate change the user could make to the next version. Each change is:

- Specific (what exactly changes in the artifact).
- Bounded (size of work to make the change).
- Reversible or cheap (no burn-the-work rewrites on weak signal).

Do NOT propose changes for every "landed" item — landed things usually don't need changing.

Mark any change whose signal comes from a non-target-audience reactor as "low-confidence, want target-audience confirmation."

### Step 5 — Identify a targeted follow-up

Name one thing the user still can't tell from the current feedback set, and propose a specific question to ask two or three target-audience people directly. Questions should be:

- Closed or scoped, not "what did you think?"
- Asked of the specific right person, not broadcast.
- Able to be answered in one reply.

Example: "For the two people who completed it and didn't share it forward: what would have to change in the last section for you to have shared it?"

### Step 6 — Name the traps

Briefly flag two reader-specific traps in the user's feedback set:

- **Politeness-as-validation.** How much of the "landed" signal is actually politeness signal in disguise?
- **Squeaky-wheel over-weighting.** If one critic is very vocal and unusual, say so — their voice shouldn't rewrite the work on its own.

---

## Constraints

### Must
- Quote reactions verbatim when classifying them.
- Distinguish politeness from specific-praise explicitly.
- Weight by target-audience match and behavior vs words.
- Limit "landed" and "missed" findings to three each.
- Produce change candidates only for "missed," not for everything.
- Mark non-target-audience-sourced changes as low-confidence.

### Must Not
- Tell the user their work is good or bad. The prompt extracts signal, not a verdict.
- Invent feedback the reactors didn't give.
- Recommend large rewrites on weak signal.
- Treat emotional reactions as irrelevant — they're data about what the work evoked — but don't convert them to change requests.
- Aggregate everything into a single "sentiment score." Signal types don't average.

---

## False-Positive Prevention

1. **Politeness is not praise.** "I loved it!" from someone who read 30 seconds of it is not signal about content; it's signal about the relationship. Keep these separate.
2. **Silence is data.** The people who didn't react, didn't share, didn't come back — that's often the strongest signal. Note it rather than assuming reactions are the whole audience.
3. **Don't over-fit to a single reactor.** One sharp critique isn't a mandate to change. Pattern across multiple target-audience reactors is.
4. **Don't ignore use-signal because it's quieter than words.** Someone using the thing beats someone praising the thing.
5. **Don't ask everyone for feedback.** Broadcast feedback-requests produce broadcast-quality feedback (i.e., low quality). Target the follow-up.

---

## Output Format

```
# Feedback extraction: [what was shipped]

## Classified reactions
- "[Verbatim reaction]" → [label] (source: [target / peer / friend / stranger], [prompted / unprompted])
- "[Verbatim reaction]" → [label] (source: ...)
- ...

## Most-weighted reactions
[Brief view: which reactions carry the most weight and why.]

## What landed (max 3)
1. [Specific finding] — supported by: [quoted reactions or behavior]
2. ...

## What missed (max 3)
1. [Specific finding] — supported by: [quoted reactions or behavior]
2. ...

## Genuinely ambiguous
- [Conflict or gap in signal]

## Change candidates (from "missed")
1. **[Change]** — bounded at [size] — confidence: [high / low; why]
2. ...

## Targeted follow-up
Ask [specific named person or small group]: "[scoped question]"

## Traps in this feedback set
- Politeness-as-validation: [how much and where]
- Squeaky-wheel: [who, what, handle how]

## Silence note
[What the absence of reaction tells us.]
```

---

## Verification

- [ ] Every classified reaction was quoted verbatim.
- [ ] Politeness signal is called out as politeness, not misread as praise.
- [ ] Findings limited to three per side.
- [ ] Change candidates are only for "missed" items.
- [ ] Non-target-audience-sourced changes are flagged low-confidence.
- [ ] Silence was considered, not just the reactions that arrived.
- [ ] No verdict on whether the work is "good."
