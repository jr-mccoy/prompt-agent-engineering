---
title: "Rapid-Start Mode: Begin Meaningful Work Within a Minute"
category: personal-development/agency
description: "A 60-second protocol for moving from 'sitting at the desk' to 'producing an artifact' — designed for days when warm-up rituals have expanded to fill the session, and for low-energy moments when the only move is to start."
techniques:
  - ST-01
  - ST-02
  - CM-02
  - QA-01
difficulty: beginner
tags:
  - agency
  - rapid-start
  - activation-energy
  - execution
  - low-energy
updated: "2026-04-20"
related_prompts:
  - domain-personal-development/prompts/agency/agency_next_action_spec.md
  - domain-personal-development/prompts/agency/agency_end_of_session_review.md
  - domain-personal-development/prompts/agency/agency_stuck_diagnosis.md
---

# Rapid-Start Mode: Begin Meaningful Work Within a Minute

**Objective:** A protocol that gets the user from "opening the laptop" to "producing an artifact" within 60 seconds. Designed for days when the warm-up phase of the session has grown to consume the session; or when the user sits down tired and knows they'll bail if anything slows them down.

**When to use:** The user has a short window (under 90 minutes). The user is tired, resistant, or knows their warm-up is unreliable. The project is already defined and the user already knows roughly what needs to happen; this prompt isn't about defining work, it's about starting.

**Audience:** An individual with an active project and an idea of what they should be doing, but inconsistent activation energy.

---

## Inputs Required

1. **The project.** Already named, already underway.
2. **A last-session context pointer.** From the prior session's review, or best-recall: file, branch, paragraph, question.
3. **Window length.** How much time is available.
4. **Energy level.** Low / medium / high. Honest, not aspirational.

If there is no prior context pointer and no active artifact, rapid-start mode will fail; run `agency_next_action_spec.md` instead.

---

## Instructions

### The 60-second protocol

Output five lines, in this exact form, tailored to the user's inputs:

1. **Open [specific file/tool/URL].** One thing. Not a list.
2. **Scroll/navigate to [specific location in the artifact].** Named by paragraph, line, section, or visible landmark.
3. **First keystrokes: [specific text to type].** Either the first words of what's coming, or the edit being made. Has to be concrete enough to execute without deciding.
4. **Timer: 25 minutes.** That's the first block. Nothing else.
5. **End state: [one-line artifact change that will exist at the timer].**

That's it. No preamble. No warm-up. No "get settled." The protocol is five lines because any more is friction.

### Low-energy adjustments

If the user reported low energy, shrink step 5's end state to the smallest meaningful change: "one sentence added," "one comment resolved," "one bug ruled out," "one commit pushed even if trivial." A bad-but-real artifact ends the resistance. A good-but-unstarted plan doesn't.

### Forbid warm-ups

Explicitly name, in the output, what the user is NOT doing during the 60 seconds:

- Not opening email.
- Not checking metrics/analytics.
- Not reading yesterday's notes beyond the context pointer.
- Not adjusting tool settings.
- Not brewing coffee-then-starting.
- Not writing a plan for the session.

The session starts with the keystrokes, not with the preparation.

### Handle the trap: "I need to get back up to speed"

If the user says they need to "re-familiarize" before working, the protocol takes a different shape:

- Open the last end-of-session review (see `agency_end_of_session_review.md`) or the prior session's context pointers.
- Read it once, aloud or in head. No more than 60 seconds.
- Then execute steps 3–5 above.

"Getting back up to speed" is real, but it is 60 seconds, not 20 minutes. If 60 seconds isn't enough, the prior session's context capture was too thin and that's fixable next time.

### Handle the trap: "I don't know what I should work on"

If this is true, rapid-start mode is the wrong mode. The user needs:

- `agency_next_action_spec.md` for choosing the next action, or
- `agency_stuck_diagnosis.md` if there's a deeper block.

Don't fake a rapid start when the real issue is selection.

---

## Constraints

### Must
- Produce exactly five lines of protocol.
- Each line is immediately executable without further decision.
- First keystrokes are specific text, not an instruction to "start writing."
- Forbid-list of warm-ups is included in the output.
- Low-energy mode uses a smaller end state, not the same one.

### Must Not
- Recommend preparation rituals, breathing exercises, or "setting intention."
- Use motivational language.
- Expand into a full session plan. The protocol is five lines.
- Assume the user knows what to do. Every line names a specific thing.
- Fake a rapid start when the real block is selection or a deeper issue.

---

## False-Positive Prevention

1. **Don't propose warm-up-disguised-as-rapid-start.** "Quickly review your notes" is a 20-minute rabbit hole. The protocol bypasses that.
2. **Don't pretend the 60-second claim works without a real context pointer.** If there's no prior-session pointer, the user cannot rapid-start; say so.
3. **Don't require motivation.** The protocol works when motivation is zero. If the output contains "try to" or "when you feel ready," rewrite.
4. **Don't over-engineer the low-energy version.** Smaller end state, not a different protocol.
5. **Don't normalize rapid-start as the only way to work.** Some sessions need proper warm-ups. This prompt is for the sessions that don't have time or energy for that.

---

## Output Format

```
# Rapid start — [project name], [window length], [energy]

## The five lines
1. Open: [specific file/tool/URL]
2. Go to: [specific location]
3. First keystrokes: [specific text]
4. Timer: 25 minutes
5. End state: [one-line artifact change]

## Not doing during the 60 seconds
- No email
- No metrics check
- No tool settings
- No plan for the session
- No coffee-then-start
- No re-reading beyond 60 seconds of context

## If the context pointer is thin
Spend up to 60 seconds on: [specific source — the last review, the last commit message, the top of the context doc]. Then go.

## If this isn't a rapid-start problem
- Don't know what to work on → `agency_next_action_spec.md`
- Deeper block → `agency_stuck_diagnosis.md`
```

---

## Verification

- [ ] Protocol is exactly five lines.
- [ ] Line 3 contains specific text, not an instruction.
- [ ] Forbid-list names at least five specific warm-ups.
- [ ] Low-energy mode uses a smaller end state when applicable.
- [ ] The prompt points to another prompt when rapid-start isn't the right mode.
- [ ] No motivational language.
