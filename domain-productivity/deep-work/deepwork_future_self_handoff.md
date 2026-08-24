---
title: "Write a Handoff to Tomorrow's (or Next Week's) Self"
category: productivity/deep-work
description: "At session/week end, produce a handoff artifact with re-entry context, blockers, decisions deferred, and the next physical action — sized so future-self saves at least one re-load cycle on resume."
techniques:
  - ST-01
  - ST-02
  - NE-20
  - CM-08
  - OC-06
difficulty: beginner
tags:
  - handoff
  - future-self
  - context-capture
  - reload
  - deep-work
updated: "2026-05-08"
related_prompts:
  - domain-productivity/deep-work/deepwork_block_end_context_capture.md
  - domain-productivity/deep-work/deepwork_project_state_synthesis.md
  - domain-productivity/deep-work/deepwork_reload_ritual_design.md
  - domain-productivity/reviews/reviews_weekly_systems_review.md
  - domain-personal-development/prompts/agency/agency_end_of_session_review.md
---

# Write a Handoff to Tomorrow's (or Next Week's) Self

**Objective:** Produce a *handoff artifact* — a short, structured note from current-self to future-self bridging a non-trivial time gap (overnight, multi-day, week-long, vacation-return) so future-self can re-enter the work without paying a full reload cost. Distinct from per-block context capture and project-state synthesis: this prompt designs the handoff for *resumption across a real gap*.

**When to use:** End of day before a multi-day gap, end of week before a real weekend break, before a vacation, or before any planned absence longer than a single working session. Run before closing the work, while context is still loaded.

**Audience:** An individual writing to themselves. Not for delegating to a colleague — that's `NE-20` Third-Party Handoff Package proper. This is a self-handoff.

---

## Inputs Required

1. **Length of the gap.** Hours / days / weeks until you'll resume.
2. **What you were working on right before this handoff.** Project, file, function, document, decision — the most-loaded context in your head right now.
3. **The state of that thing.** What's done, what's in-progress, what was being attempted at the moment of stopping.
4. **The thing you would do next if you had 10 more minutes.** The very next physical motion.
5. **Decisions in flight.** What was the active question, dilemma, or trade-off being worked through at stopping time? With your current preference if you have one.
6. **External dependencies.** What's waiting on someone else, or on something to land — and what the trigger condition is to act when it lands.
7. **Things you'll forget.** Specific items: a reference url, a concept name, a counterintuitive constraint, a colleague's offhand comment that mattered. The little stuff that isn't in any commit message or doc.
8. **Things you don't need to handle yet, but will surprise future-self if forgotten.** Latent items: an upcoming deadline, an expiring auth token, a dependency about to ship, a person waiting on a reply.

If input 1 (gap length) is < 4 hours within the same workday, this prompt is overkill — use `deepwork_block_end_context_capture.md` instead.

---

## Instructions

### Step 1 — Match the handoff size to the gap size

Different gaps require different handoff depth. Don't over-handoff for a one-night gap; don't under-handoff for a vacation.

| Gap | Handoff depth | Time to write |
|---|---|---|
| **Overnight** | Light — one short note, focused on inputs 4 and 7. | 3–5 min |
| **2–4 days** | Medium — full structure, but inputs 5 (decisions) and 6 (dependencies) often light. | 8–12 min |
| **5–10 days** | Full — every section, including input 8 (latent items). | 15–25 min |
| **> 2 weeks (vacation, sabbatical, leave)** | Full + inbound-buffer plan: what to do with what arrives during the gap. | 30–60 min |

State which depth applies and proceed at that depth.

### Step 2 — Write the re-entry block (CM-08 file-based state)

The first section of the handoff is the re-entry block — what future-self reads first to load context faster. Structure:

```
## Re-entry (read first)
- **Working on:** [input 2, in one sentence]
- **Last state:** [input 3, in one sentence]
- **Next action:** [input 4 — physical, one sentence]
- **First minute on resume:** [the literal action — open this file, run this command, re-read this paragraph]
```

The "first minute on resume" line is the prompt's most distinctive feature. It is the action future-self does on returning, *before* loading any other context. It's almost always a re-read of one specific thing — a paragraph, a function, a decision log entry — that re-primes the relevant state.

### Step 3 — Write the decisions-in-flight section

For each item in input 5:

- The active question, in plain language.
- The current preference, if any, with the reason.
- The minimum information that would resolve it.

This section often saves the most reload time on resume. Without it, future-self spends 30–60 minutes reconstructing what current-self already knew.

### Step 4 — Write the dependencies section

For each item in input 6:

- What's pending.
- Who/what it depends on.
- The trigger condition for action.
- The action when triggered.

Format as a short list, not a paragraph. Future-self scans this on Monday morning.

### Step 5 — Write the things-you'll-forget section

For each item in input 7, write a one-line catch-fact. These are the items most likely to evaporate during the gap. Examples:

- "The migration assumes int32; the upstream is already int64. Convert at the boundary; do not at the call site."
- "Do not delete the redirect rule on the old path until [date] — analytics still reference it."
- "Olivia's offhand point in the Tuesday call was the actual blocker; the documented blocker is downstream."

Resist the urge to expand each into a paragraph. One line per item. The format is constraint: if a fact requires a paragraph, it goes in the relevant work doc, not the handoff.

### Step 6 — Write the latent-items section (input 8)

For each item, state:

- The item.
- The horizon (when does it become urgent).
- One sentence of what to do when it does.

Latent items that surface during the gap as surprises are the most expensive failures of poor handoffs. List them.

### Step 7 — For gaps > 10 days: write the inbound-buffer plan

For long gaps (vacation / sabbatical / parental leave), the handoff also addresses what arrives during the gap. Two questions:

1. **Filtering.** What gets through to future-self even during the gap (genuine emergencies, named exceptions). Default: nothing except specific named emergencies.
2. **Triage on return.** What does future-self do with the accumulated inbox at the start of the resume? Default: bulk archive after a date threshold; only items addressed to the user by name are reviewed; everything else is presumed handled or no-longer-relevant.

State both. The inbound-buffer plan is what protects the gap from creeping back into the user's mind during the gap itself.

### Step 8 — Save it where future-self will find it

State explicitly where the handoff lives: a file at the top of the project, an entry in the daily log, a calendar event for the resume time with the handoff in the body, a pinned note. The handoff is useless if future-self can't locate it.

If the user has no consistent location for handoffs across projects, propose one (single file at repo root: `HANDOFF.md`; or per-day file: `handoff/2026-05-08.md`). Repeat the location across handoffs so future-self always knows where to look.

### Step 9 — Predict the reload savings

State explicitly what reload cycle this handoff saves. Examples:

- "Saves the 20–30 minute 'where was I' wandering on resume."
- "Saves the 45-minute reconstruction of the deferred decision."
- "Saves the surprise of the [X] deadline becoming visible mid-week."

The point is to make the handoff's value explicit, so future-self trusts it and current-self keeps writing them.

---

## Constraints

### Must
- Match handoff depth to gap length.
- Lead with the re-entry block, including the "first minute on resume" line.
- Cover decisions-in-flight, dependencies, things-you'll-forget, and latent items at appropriate depth.
- Save the handoff to a known, repeated location.
- Predict the reload-cycle savings.

### Must Not
- Write the handoff in prose paragraphs throughout. Bullet lists for scannability.
- Re-write project documentation. The handoff supplements docs; it does not replace them.
- Include sentimental content ("hope you have a good weekend"). The handoff is functional.
- Plan future work in the handoff. ("On Monday, I'll do X, then Y, then Z.") Future-self plans on resume; current-self writes the resume context, not the future plan.
- Run this prompt for gaps < 4 hours within the same day.

---

## False-Positive Prevention

1. **Don't over-handoff a short gap.** A one-night gap with a one-sentence "next action" is the right size. Long handoffs for short gaps create their own reload cost.
2. **Don't under-handoff a long gap.** Vacations end with worse productivity costs than the vacation if return-state is unscoped. Use the inbound-buffer plan.
3. **Don't conflate this with project documentation.** Project-state belongs in `deepwork_project_state_synthesis.md` or in the project's own docs. The handoff is just the bridge across this gap.
4. **Don't assume future-self will remember context that current-self can write down in 30 seconds.** When in doubt, write it down.
5. **Don't write the handoff after stopping work and turning off the laptop.** Context is gone by then. Write while loaded.
6. **Don't recommend a tool that requires daily upkeep.** The handoff is a per-gap artifact, not a system. Plain text is fine.

---

## Output Format

```
# Handoff — [date / gap description]
**Gap:** [length] | **Handoff depth:** [Light / Medium / Full / Full + inbound-buffer]

## Re-entry (read first)
- **Working on:** ...
- **Last state:** ...
- **Next action:** ...
- **First minute on resume:** ...

## Decisions in flight
- [Question] | Current preference: [...] | Minimum info to resolve: [...]
- ...

## Dependencies
- [Pending] | Depends on: [...] | Trigger: [...] | Action when triggered: [...]
- ...

## Things you'll forget
- [one-line catch-fact]
- ...

## Latent items (surprises if forgotten)
- [item] | Horizon: [when] | Action when due: [one sentence]
- ...

## (Long gaps only) Inbound-buffer plan
- **Filter during gap:** [named exceptions only / nothing]
- **Triage on return:** [rule, e.g., bulk-archive after threshold; review only by-name items]

## Saved at
[Specific path or location.]

## Predicted reload savings
[One sentence — what reload cycle this handoff replaces.]
```

---

## Verification

- [ ] Handoff depth matches gap length per the table.
- [ ] Re-entry block leads, including "first minute on resume."
- [ ] Decisions-in-flight, dependencies, things-you'll-forget, latent items all addressed at the appropriate depth.
- [ ] Inbound-buffer plan included for gaps > 10 days.
- [ ] Saved location stated and consistent with prior handoffs.
- [ ] Reload savings prediction stated.
- [ ] No prose paragraphs where bullet lists belong.
- [ ] No sentimental content; no future-week planning.
