---
title: "Stage 4 — Revision Triage (Dynamic Loop; Gate A Craft Integrity)"
category: childrens-writing/pipeline
description: "The agentic core: diagnoses a full draft, routes to only the craft tools the manuscript actually needs, consolidates a prioritized fix queue, applies fixes, and loops until the craft-integrity gate (Gate A) passes — child agency, no preaching, read-aloud rhythm, reading level on band."
techniques:
  - ST-02
  - DS-02
  - DS-06
  - RT-05
  - QA-01
  - QA-02
difficulty: advanced
tags:
  - childrens-writing
  - pipeline
  - stage-4
  - revision
  - evaluator-optimizer
updated: "2026-06-24"
related_prompts:
  - childrens-book-studio/prompts/stage-3-draft-generation.md
  - domain-childrens-writing/craft-tools/childrens_revision_self_edit_pass.md
  - domain-childrens-writing/representation-collaboration/childrens_writing_across_difference_audit.md
---

# Stage 4 — Revision Triage (Dynamic Loop)

## Objective

Take a complete first draft to craft-integrity. This is the studio's **evaluator-optimizer loop**: diagnose the manuscript, route to *only* the craft tools it needs, consolidate a prioritized (big-to-small) fix queue, apply fixes, and re-check **Gate A**. Repeat until Gate A passes.

## When to Use

- After a full first draft exists (Stage 3), or as the entry point for revising any existing draft (`/revise-manuscript`).

## Inputs / Context

- The Stage 3 draft (`manuscript.md`).
- The Stage 0 form, age band, convention contract, and form-conditioned craft-pass list.
- The Stage 1 agency moment and theme (the things Gate A protects).

## Constraints

**Must:**
- Start with `domain-childrens-writing/craft-tools/childrens_revision_self_edit_pass.md` for the layered diagnosis (story → structure → character/voice → line → form-specific).
- Route to only the applicable craft tools (prune by form — see `PIPELINE_OVERVIEW.md` branching):
  - `craft-tools/childrens_opening_pages_hook.md` — if the opening doesn't pull.
  - `craft-tools/childrens_kid_dialogue_workshop.md` — if dialogue reads adult/cute/on-the-nose (forms with dialogue).
  - `craft-tools/childrens_character_creation.md` — if the protagonist or cast is thin.
  - `craft-tools/childrens_age_reading_level_calibrator.md` — if the reading level is off the target band.
  - `craft-tools/childrens_sensitive_topics_framing.md` — if a hard topic is handled bluntly or preachily.
  - `representation-collaboration/childrens_writing_across_difference_audit.md` — if the manuscript depicts an identity the author doesn't share (its *output is reviewed at Gate B*, but run it here).
- Consolidate findings into ONE prioritized fix queue (highest-impact first), not parallel unmerged notes.
- Loop: apply the top fixes, re-diagnose, re-check Gate A. Stop when Gate A passes or no new high-impact issues surface.
- Save each revision as a new version; never silently overwrite.

**Must Not:**
- Run every craft tool reflexively. Route by what the diagnosis surfaces.
- Line-edit before structural problems are fixed (don't polish a scene you'll cut).
- Declare done while child agency is missing, the theme is preached, or the reading level is off band.
- Treat the across-difference audit as resolved here — its findings go to the author and a human reader; Gate B checks it was kept as flags, not certified.

## Instructions

1. **Diagnose:** run the revision self-edit pass to produce a layered problem list.
2. **Route:** select only the craft tools the diagnosis points to (and the across-difference audit if applicable).
3. **Consolidate:** merge all findings into one fix queue, ranked by impact (story/agency/theme first, line-level last).
4. **Apply:** make the top fixes; save a new version.
5. **Re-check Gate A** (the checklist below). If any item FAILs, return to step 1 on the affected layer.
6. Repeat until Gate A passes. Record how many passes ran and what changed.

## Output Format

```
REVISION TRIAGE — pass [N]
DIAGNOSIS (layered): story / structure / character-voice / line / form-specific findings
ROUTED TOOLS: [list of craft tools actually used + why]
FIX QUEUE (priority order):
  1. [highest impact] ...
  2. ...
APPLIED THIS PASS: ...
SAVED AS: manuscript-v[N].md

GATE A — CRAFT INTEGRITY: PASS | FAIL
  - child drives climax: PASS/FAIL
  - theme carried by action (no stated moral): PASS/FAIL
  - read-aloud rhythm (if PB/early reader/verse): PASS/FAIL/NA
  - reading level on target band: PASS/FAIL
[if FAIL: loop — name the layer to revisit]
```

## Verification Checklist (Gate A — the orchestrator gates on this)

- [ ] The child protagonist drives the climax (no adult rescue).
- [ ] The theme is carried by action; no stated moral remains.
- [ ] For picture books / early readers / verse, the read-aloud rhythm holds (no stumbles).
- [ ] The reading level matches the target age band.
- [ ] Only the needed craft tools were run (no reflexive full sweep), and findings were consolidated into one prioritized queue.
- [ ] (If depicting unshared identity) the across-difference audit was run and its output is a list of flags/questions, not a self-certification.

## False-Positive Prevention

- **Polishing prose while a structural fix is pending.** Fix big before small; the fix queue is ranked for this reason.
- **Calling it done because it "reads nicely."** Gate A is specific: agency, no preaching, rhythm, reading level. Check each.
- **Running every craft tool to look thorough.** Route by diagnosis; an unneeded pass wastes effort and can flatten voice.
- **Letting the across-difference audit read like approval.** It is risks and questions for a human reader; never a green light.
- **Infinite looping.** If a pass surfaces no new high-impact issue and Gate A passes, stop.
