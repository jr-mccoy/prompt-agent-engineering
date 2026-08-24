---
title: "Capture Context at the End of a Focus Block"
category: productivity/deep-work
description: "At the end of a focus block, produce a tight 'reload packet' the user will read next session — current state, open question, next physical action, and context that will be unrecoverable in 24 hours — so next-session startup cost drops from rediscovery to reading."
techniques:
  - ST-01
  - ST-02
  - OC-01
  - CM-02
  - QA-01
difficulty: beginner
tags:
  - deep-work
  - context-capture
  - reload
  - end-of-session
updated: "2026-04-20"
related_prompts:
  - domain-personal-development/prompts/agency/agency_end_of_session_review.md
  - domain-productivity/deep-work/deepwork_reload_ritual_design.md
  - domain-productivity/deep-work/deepwork_project_state_synthesis.md
  - domain-productivity/deep-work/deepwork_focus_block_async_summary.md
---

# Capture Context at the End of a Focus Block

**Objective:** Produce a compact reload packet — readable in under 90 seconds — that lets the user resume the same work tomorrow without rediscovery. Not a journal entry, not a status report. A packet the user's future self can execute from.

**When to use:** At the last 3–5 minutes of every focus block where the work will continue in a future session. If the work is finished, use a different prompt (post-mortem or summary).

**Audience:** The user writing to their own future self, typically 1–3 days later.

---

## Inputs Required

1. **What the user was working on this block.** One sentence.
2. **The current state** — file, draft, decision, sketch, test result — wherever the work physically lives. Path or link if possible.
3. **The open question or next decision.** What they'd ask themselves if they sat back down right now.
4. **What changed in their thinking this block.** Even if the change isn't reflected in the artifact.
5. **Anything they noticed they'd forget by tomorrow.** Small, fragile context — why they rejected an approach, a thread someone pulled in a DM, a hunch that hasn't earned its place yet.

Items 4 and 5 are the value. A reload packet without them is just a TODO.

---

## Instructions

1. **Write the packet in the fixed shape below.** Do not expand sections. Constraint is the feature.

2. **Convert the open question into a physical next action.** "Decide how to structure the onboarding email" becomes "Draft three opening lines of the onboarding email; pick one before 10:00." Physical means: something the user can start doing in < 60 seconds of sitting down.

3. **Flag any fragile context.** Thinking-in-progress, verbal agreements, hunches — things that evaporate. Mark them as "fragile:" so the future self treats them seriously.

4. **Include exactly one pointer** back to the work artifact. If there are many, pick the one that's the true current state.

5. **If the user cannot answer inputs 3, 4, or 5, say so in the packet.** Empty is honest. A fake reload packet is worse than none.

---

## Output Format

```
# Reload Packet — [date/time]

## State
- Working on: [one sentence]
- Lives at: [one pointer]
- Last touched: [timestamp]

## Next Action
[Physical, startable in <60 sec]

## Open Question
[Whatever is genuinely undecided]

## Changed This Block
- [bullet, 1–3 items]

## Fragile Context (evaporates by tomorrow)
- fragile: [item]
- fragile: [item]

## Known Unknown
[If any input was left empty, name it here.]
```

---

## Constraints

**Must:**
- Fit on one screen. No long prose.
- Contain exactly one pointer to the live artifact.
- Include a physical next action, not a verb-noun abstraction.
- Mark fragile items with the literal word "fragile:".

**Must not:**
- Summarize everything done in the block — this is not a journal.
- Rank, prioritize, or compare against other work streams.
- Produce motivational language or close with encouragement.
- Include anything that would be true of any block ("keep going," "focus tomorrow").

---

## False-Positive Prevention

- **Journal drift:** The moment the packet starts describing accomplishments, restart. Future-self does not need a progress narrative; it needs entry points.
- **Fake physicality:** "Continue working on X" is not a physical action. Force it to something startable within one minute.
- **Over-capture:** If fragile context exceeds five items, the user is using this as a dumping ground. Keep the three most unrecoverable; drop the rest.
- **Completed work:** If the work actually finished this block, do not write a reload packet. Future-self will be confused to find one for a shipped thing.

---

## Self-Verification (before finalizing)

- [ ] Packet fits on one screen.
- [ ] Exactly one pointer to the live artifact.
- [ ] Next action is physical and < 60-sec startable.
- [ ] Fragile items marked with "fragile:" literal.
- [ ] No motivational or progress-narrative language.
- [ ] If any input was empty, the Known Unknown block reflects it.
