---
name: revise-manuscript
description: Revise an existing children's-book draft. Jumps to Stage 4 revision triage — diagnoses the draft, routes to only the needed craft tools, builds a prioritized fix queue, and loops until the craft-integrity gate (Gate A) passes.
---

# /revise-manuscript

Enter the Children's Book Studio at Stage 4 (revision triage) for an existing draft.

**Action:** Load and follow `childrens-book-studio/prompts/stage-4-revision-triage.md`, using the `manuscript-craft-reviewer` agent. First confirm the project's form, age band, and convention contract (run a quick Stage 0 check if unknown). Then:

1. Diagnose the draft (layered) via `domain-childrens-writing/craft-tools/childrens_revision_self_edit_pass.md`.
2. Route to only the craft tools the diagnosis points to (prune by form).
3. Consolidate one prioritized fix queue (big-to-small).
4. Apply fixes, save a new version, and re-check **Gate A** (agency · no preaching · read-aloud rhythm · reading level). Loop until it passes.

If the draft depicts an identity the author doesn't share, also run `representation-collaboration/childrens_writing_across_difference_audit.md` and keep its output as flags/questions (not a certification).

**Ends when** Gate A passes. Suggest continuing to `/build-submission-package` (via Stage 5) when ready.
