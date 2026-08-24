---
title: "Pre-Meeting Rehearsal — Scripting the High-Stakes Negotiation Conversation"
category: negotiation/preparation
description: "Rehearse a high-stakes negotiation conversation before it happens. Not a brief — the actual run-through. Scripts the load-bearing moments (opening line, early questions, the ask, the response to their counter, the walkaway/exit, the close), rehearses 2–3 likely surprises with a response to each, and runs a tone and body-language check for in-person or video. Output is a set of scripted moments plus a decision tree of branches so the user has a prepared move at every fork."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - DS-01
  - CM-02
  - QA-01
difficulty: intermediate
tags:
  - negotiation
  - rehearsal
  - scripting
  - preparation
  - exit-script
updated: "2026-06-18"
reasoning:
  styles: [strategic, counterfactual, simulation]
  stakes: high
  horizon: hours
  uncertainty: ambiguity
  evidence_quality: moderate
  domain_complexity: variable
  collaboration: solo_or_pair
  output_format: [dialog, structured]
  user_role: [executive, founder, sales, hr, individual]
  mode: [rehearse, plan]
related_prompts:
  - domain-negotiation/preparation/negotiation_batna_analysis.md
  - domain-negotiation/preparation/negotiation_interest_mapping.md
  - domain-negotiation/difficult-conversations/difficultconvo_pre_brief.md
---

# Pre-Meeting Rehearsal — Scripting the High-Stakes Negotiation Conversation

**Objective:** Take the strategy you've already built (BATNA, interests, target) and rehearse the actual conversation. Most negotiations are lost not in the analysis but in the moment — the user freezes at the ask, over-explains, accepts the first counter out of relief, or fails to deliver the walkaway and so undercuts every prior word. This prompt scripts the load-bearing moments out loud: the opening line, the questions to ask before revealing anything, the moment of the ask, the response to their counter, the walkaway/exit script, and the close. It then rehearses the 2–3 surprises most likely to derail the user, with a prepared response to each, and runs a tone/body-language check for in-person or video. The deliverable is a script of moments plus a branching decision tree — so at every fork the user has a move they've already said once.

This presupposes the strategy work is done. It is the rehearsal, not the brief — `negotiation_batna_analysis.md` is the brief.

**When to use:**
- A specific high-stakes negotiation conversation is scheduled (offer, raise, contract, partnership, board ask, large purchase).
- The user has the strategy but is nervous about executing it live.
- The walkaway is real and the user has historically struggled to deliver one.
- The conversation is short enough that a few moments carry most of the weight.

**When NOT to use:**
- Strategy isn't set yet — do BATNA/interest work first; rehearsing the wrong ask is worse than not rehearsing.
- Long, multi-session, document-driven negotiations where there is no single decisive conversation to rehearse.
- Asynchronous / written negotiations — rehearsing tone and body language doesn't apply; draft and edit instead.

**Audience:** Executives, founders, salespeople, HR leaders, and individuals walking into a scheduled, consequential negotiation conversation.

---

## Inputs / Context

1. **The conversation.** With whom, when, where (in-person / video / phone), how long.
2. **Your ask.** The specific thing you're asking for, in concrete terms.
3. **Your strategy, in brief.** Your BATNA, your target, your walkaway, the interests at play (from upstream prompts).
4. **The counterpart.** Their likely position, their style (combative / agreeable / evasive / data-driven), any history.
5. **Your known weak moments.** Where you tend to fold, over-explain, fill silence, or back down. Honest self-report.
6. **Medium.** In-person, video, or phone — determines the tone/body-language layer.

---

## Constraints

### Must
- Script the **opening line** verbatim — the first thing out of the user's mouth. It sets tone and frame.
- Script **early questions** that surface the counterpart's position/interests *before* the user reveals their own ask.
- Script the **ask moment** verbatim: a clear, unhedged statement of what the user wants, followed by **silence** (the user says it and stops — no qualifying, no immediate discount).
- Script the **response to their counter** for at least three likely counters (accept-ish, push-back, lowball/insult).
- Script the **walkaway/exit** verbatim — the exact words the user says to end the conversation without a deal, in a way that preserves the relationship and the option to return.
- Script the **close** verbatim — how the user confirms and locks an acceptable agreement so it doesn't unravel after.
- Rehearse **2–3 surprises** (an unexpected objection, a new party, a re-anchored number, an emotional reaction) with a prepared response to each.
- Run a **tone / body-language check** appropriate to the medium (pace, pauses, eye line on video, posture, what to do with hands, how to handle silence).
- Produce a **branching decision tree**: at each scripted fork, what they say → what the user does next.

### Must Not
- Let the ask be hedged. "I was kind of hoping maybe we could possibly look at..." is a fold disguised as politeness. The script must be direct.
- Let the user fill the silence after the ask. The script ends the ask with a full stop and a note: *now wait.*
- Skip the walkaway script. An un-rehearsed walkaway is the one most likely to fail, and its absence makes every other move bluff.
- Script the user into a corner with a single line that has no follow-up branch.
- Coach generic "be confident" tone advice. Tone notes must be specific and medium-appropriate.

---

## Instructions

### Step 1 — Set the frame and opening line
Write the verbatim opening line. It should be warm but not apologetic, and it should set the frame the user wants (collaborative problem-solving, or firm but fair, etc.). One or two sentences. Note the intended tone.

### Step 2 — Script the early questions
Write 2–4 questions the user asks before revealing the ask, to surface the counterpart's position and interests. Ordered low-threat first. Note what each answer would tell the user and how it might adjust the ask.

### Step 3 — Script the ask moment
Write the ask verbatim: clear, specific, unhedged, no premature discount. End the script with an explicit instruction: **stop talking and wait.** Add a note on how long the silence may feel and why holding it matters.

### Step 4 — Script responses to their counter
Identify the three most likely counters: (a) near-acceptance with a small ask, (b) firm push-back / lower number, (c) lowball or dismissive move. For each, write the user's verbatim response — including, for (c), how to hold position without escalating.

### Step 5 — Script the walkaway / exit
Write the exact words for ending without a deal: calm, non-burning-bridges, leaving the door open ("I appreciate the conversation — this isn't quite where I need it to be, so I'm going to hold off for now. If something changes on your end, I'd genuinely welcome a follow-up."). Note the trigger that fires it (tie to the pre-committed walkaway from the BATNA work).

### Step 6 — Script the close
Write how the user locks an acceptable deal: restate the agreed terms aloud, confirm next steps and who sends what by when, so the agreement is concrete before the meeting ends. This prevents post-meeting drift and "I thought we said..."

### Step 7 — Rehearse the surprises
Pick the 2–3 surprises most likely to throw *this* user given their weak moments (Input 5). For each: the surprise, the user's instinctive (bad) reaction, and the prepared response. The goal is that the surprise feels familiar in the room.

### Step 8 — Tone and body-language check
Medium-specific. Video: eye line to camera, lighting, what to do in silences, neutral resting face. In-person: posture, hands, pace, matching the counterpart's energy without mirroring aggression. Phone: pace, smiling-while-speaking, comfort with dead air. Name the user's likely tell (fast talking, nervous laugh, filler words) and a countermeasure.

### Step 9 — Assemble the decision tree
Lay out the conversation as forks: opening → questions → ask → [their response branches] → counter-response → [further branches] → close OR walkaway. Each node names what they say and the user's prepared next move.

---

## False-Positive Prevention

1. **Hedged ask.** The single most common fold. If the scripted ask contains "just," "maybe," "kind of," "I was wondering," rewrite it direct.
2. **Filling the silence.** Saying the ask then immediately softening or discounting it. The script must end with *stop and wait.*
3. **No walkaway script.** Leaving the exit unscripted means it won't happen, which means the walkaway isn't credible and the whole position is a bluff. Always script it.
4. **Generic tone coaching.** "Be confident, be assertive" is useless in the moment. Give specific, medium-appropriate, tell-targeted notes.
5. **Single-line scripting.** A script with no branches breaks the instant they say something off-script. Every scripted moment needs at least one alternative continuation.
6. **Rehearsing the easy case only.** Scripting the conversation where they say yes. Rehearse the lowball and the surprise, because those are where execution fails.
7. **Over-rehearsal into rigidity.** Memorizing word-for-word so tightly that the user can't adapt and sounds robotic. Script the *moments*; rehearse the *intent* so it survives improvisation.
8. **Forgetting the close.** Winning the negotiation and then leaving terms vague, so it unravels later. Script the explicit restate-and-confirm.

---

## Output Format

```
# Rehearsal Script — [negotiation], [date / medium]

## Frame & opening line (verbatim)
"[...]"
Tone: [...]

## Early questions
1. "[question]" — tells me: [...]; may adjust ask if: [...]
2. ...

## The ask (verbatim)
"[clear, unhedged ask]."
>>> STOP TALKING AND WAIT. <<<  (note: [why the silence matters])

## Responses to their counter
- If near-acceptance + small ask: "[verbatim]"
- If firm push-back / lower number: "[verbatim]"
- If lowball / dismissive: "[verbatim — hold position, don't escalate]"

## Walkaway / exit (verbatim)
Trigger: [pre-committed walkaway condition]
"[calm, door-open exit line]"

## Close (verbatim)
"[restate agreed terms + confirm next steps, who/what/when]"

## Surprise drills
| Surprise | My bad instinct | Prepared response |
|----------|------------------|-------------------|
| [...] | [...] | [...] |

## Tone & body-language ([medium])
- Do: [...]
- My likely tell: [...] → countermeasure: [...]
- Handling silence: [...]

## Decision tree
Opening → Questions → ASK →
  ├─ They accept-ish → [close]
  ├─ They push back → [counter-response] → ...
  └─ They lowball → [hold] → ... → [close OR walkaway]
```

---

## Verification

- [ ] Opening line is scripted verbatim with a tone note.
- [ ] Early questions surface their position before the ask is revealed.
- [ ] The ask is verbatim, unhedged, and ends with an explicit "stop and wait."
- [ ] Responses scripted for all three counter types, including the lowball.
- [ ] The walkaway/exit is scripted verbatim, tied to the pre-committed trigger, door left open.
- [ ] The close is scripted with restate-and-confirm.
- [ ] 2–3 surprises rehearsed with prepared responses, chosen for this user's weak moments.
- [ ] Tone/body-language notes are specific to the medium and target a named tell.
- [ ] A branching decision tree covers the main forks to close or walkaway.
- [ ] No hedged language survives in any scripted line.
