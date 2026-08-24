---
name: build-submission-package
description: Build a submission package (logline + comps, query letter, one-page synopsis, formatted sample) for a finished children's-book manuscript. Jumps to Stage 6 and enforces the publishing-honesty gate (no invented comps/agents).
---

# /build-submission-package

Enter the Children's Book Studio at Stage 6 (publishing package) for a finished manuscript.

**Action:** Load and follow `childrens-book-studio/prompts/stage-6-publishing-package.md`. Confirm the manuscript is final (ideally Gate A + Gate B passed). Then run the publishing-business prompts in order:

1. `domain-childrens-writing/publishing-business/childrens_pitch_comps_market_positioning.md` — logline + comp *criteria* (titles bracketed `[AUTHOR TO VERIFY]`).
2. `domain-childrens-writing/publishing-business/childrens_query_letter_kidlit.md` — form-specific query.
3. `domain-childrens-writing/publishing-business/childrens_synopsis_submission_package.md` — one-page synopsis + package assembly.

**Enforce Gate C (publishing honesty):** never invent a comp title, agent/publisher name, sales figure, or submission rule. Bracket every unverifiable market fact `[AUTHOR TO VERIFY]`. Flag submission formatting to confirm against each agency's actual guidelines.

**Ends when** the package is assembled, Gate C passes, and the deliverable manifest is complete. Remind the author to fill every `[AUTHOR TO VERIFY]` bracket before sending.
