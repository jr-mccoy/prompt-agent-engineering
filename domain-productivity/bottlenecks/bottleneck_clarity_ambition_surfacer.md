---
title: "Surface What You Actually Want (Clarity / Ambition Lane)"
category: productivity/bottlenecks
description: "When clarity is the binding constraint, force a concrete one-page articulation of what the user actually wants — by name, scope, timeframe, and visible end-state — instead of the moving vision-document drift that keeps the user unable to finish anything."
techniques:
  - ST-01
  - ST-02
  - DS-01
  - CM-02
  - QA-01
difficulty: intermediate
tags:
  - bottleneck
  - clarity
  - ambition
  - goals
  - vision
updated: "2026-04-20"
related_prompts:
  - domain-productivity/bottlenecks/bottleneck_locator.md
  - domain-personal-development/prompts/agency/agency_project_ownership_converter.md
  - domain-personal-development/prompts/agency/agency_next_action_spec.md
---

# Surface What You Actually Want (Clarity / Ambition Lane)

**Objective:** Produce a one-page, read-out-loud statement of what the user actually wants that is specific enough to be falsifiable — a target with name, scope, timeframe, and a visible end-state someone else could recognize. Not a vision document. Not three options.

**When to use:** After `bottleneck_locator.md` points at clarity. Or when the user has rewritten their goal four times in three months. Do not use for someone who already has a clear target but isn't executing; that's the wrong lane.

**Audience:** An individual getting honest with themselves, not pitching a vision to others.

---

## Inputs Required

1. **The user's current best attempt at stating what they want.** Verbatim.
2. **How many times it has been rewritten or redirected in the last 6 months.** Count.
3. **What they've been telling people when asked "what are you working on?"** Verbatim — the public version.
4. **What they would want if they knew it would work.** Free text, allowed to be fantastical.
5. **What they would still do even if they knew it would fail.** Free text. Can be short.
6. **What "winning" looks like in physical terms** — a number, an artifact, a title, a relationship, a location. If they can't answer, say so.

Items 4 and 5 together usually triangulate the real target better than input 1.

---

## Instructions

1. **Diff input 1 (private) vs input 3 (public).** If they're different, note that. The difference often reveals the real ambition the user is hiding from themselves.

2. **Cross-reference inputs 4 and 5.** The overlap — things they'd want if it worked AND would do even if it failed — is close to the real target. Call that out specifically.

3. **Attempt to write the target in one sentence using this template:**
   > "By [date], I want to have [visible end-state] such that [witness / measurable proof]."
   
   If the user's inputs can't populate [date], [visible end-state], or [witness/proof], say which field is empty. An empty field is the clarity bottleneck.

4. **Sanity-check specificity:**
   - Could someone else tell whether this happened on the given date? If no, not specific.
   - Could someone else argue it happened when it didn't? If yes, the proof is too fuzzy.
   - Does the end-state require other people to do something? If yes, name those dependencies — they may be the real target.

5. **Name up to two ambitions the user is carrying but not saying.** Common hidden ambitions: money at a specific level, recognition by a specific community, proving something to a specific person. If evidence from inputs 3–5 points there, name it — politely, but clearly.

6. **Produce the one-page output.** Use the structure below; resist padding with filler.

7. **Flag rewrite risk.** If input 2 shows ≥ 3 rewrites in 6 months, this one-pager is also likely to be rewritten. Name the trigger that would allow a rewrite vs. the reflex to restart. ("Only rewrite if [specific event], not because [feeling].")

---

## Output Format

```
# What I Actually Want

## Target
By [date], I want [visible end-state] such that [witness / proof].

## Public vs Private
- What I tell people: "[input 3]"
- What I'm actually reaching for: [diff, if any]

## Want-if-it-worked / Would-do-if-it-failed Overlap
[The intersection — close to the real target.]

## Specificity Check
- Datable? yes / no
- Externally witnessable? yes / no
- Independent of others' decisions? yes / mostly / no — [dependencies named]

## Hidden Ambitions (if any)
- [carried but unsaid ambition], evidence from inputs [N]
- ...

## Rewrite Rule
This one-pager may be rewritten only if [specific external event]. Emotional restarts do not qualify.

## What "Winning" Looks Like Physically
[Single concrete thing — number, artifact, relationship, location.]
```

---

## Constraints

**Must:**
- Write exactly one target sentence using the template.
- State which fields (date / end-state / witness) are empty if any.
- Surface public-vs-private discrepancy when inputs show one.
- Produce a rewrite rule that distinguishes signal from reflex.

**Must not:**
- Produce a list of three target options.
- Use aspirational language without a measurable anchor ("grow into my potential", "build something meaningful").
- Add a motivational close.
- Tell the user their ambition is wrong. Only surface it; judgment isn't the job.

---

## False-Positive Prevention

- **Vision-doc drift:** The output must fit on one page. If it spreads into sections about values, mission, and purpose, restart — this is the trap that caused input 2.
- **Proxy targets:** "Become a great writer" is a proxy. "Publish three essays that each get ≥ 10 replies from strangers" is a target. Push toward the second form.
- **Borrowed ambitions:** If inputs 3–5 read like a LinkedIn summary or a venture-capitalist pitch, the ambition may be borrowed, not owned. Name it rather than polish it.
- **Clarity confused with commitment:** The user might have clarity but not commitment. If the target is already specific and the problem is fear of naming it, don't pretend it's a clarity issue — say so.
- **Rewrite invitation:** Do not rewrite on vague dissatisfaction. The rewrite rule must name a concrete trigger.

---

## Self-Verification (before finalizing)

- [ ] Exactly one target sentence produced, or empty fields flagged.
- [ ] Public vs private diff addressed (even if "same").
- [ ] Overlap of wants-and-would-still-do is named.
- [ ] Specificity check has three answers (date / witness / dependencies).
- [ ] Rewrite rule names a concrete trigger.
- [ ] "Winning physically" is a concrete thing, not a feeling.
- [ ] Output fits on one page.
