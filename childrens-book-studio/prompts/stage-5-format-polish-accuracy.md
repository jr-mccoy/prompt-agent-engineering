---
title: "Stage 5 — Format Polish & Accuracy (Gate B Truth & Representation)"
category: childrens-writing/pipeline
description: "Form-specific polish plus the integrity gate. Picture books get illustrator collaboration + a dummy; verse gets rhythm/rhyme polish; illustrated/print forms get accessible-design review; nonfiction gets accuracy verification + back-matter assembly. Gate B blocks any unsourced fact, any representation certification, and any age-inappropriate content."
techniques:
  - ST-02
  - CM-02
  - RP-01
  - QA-01
  - QA-04
difficulty: advanced
tags:
  - childrens-writing
  - pipeline
  - stage-5
  - accuracy
  - representation
updated: "2026-06-24"
related_prompts:
  - childrens-book-studio/prompts/stage-4-revision-triage.md
  - domain-childrens-writing/representation-collaboration/childrens_illustrator_collaboration.md
  - domain-childrens-writing/nonfiction-workshops/childrens_narrative_nonfiction_workshop.md
---

# Stage 5 — Format Polish & Accuracy

## Objective

Bring a craft-passed draft to publishable polish in the ways the form requires, and clear the **truth-and-representation gate (Gate B)**: no fabricated nonfiction fact, no certified representation, no age-inappropriate content. This stage produces the manuscript's final companion artifacts (art notes/dummy, back matter).

## When to Use

- After Stage 4 passes Gate A.
- When a draft is craft-sound but not yet format-polished or accuracy-cleared.

## Inputs / Context

- The Stage 4 revised manuscript (Gate A passed).
- The Stage 0 form-conditioned Stage 5 path and add-ons.
- For nonfiction: the Stage 1 source plan and any open `VERIFY` markers from Stage 3.

## Constraints

**Must:**
- Run only the form's Stage 5 path:
  - **Picture book / graphic novel:** `representation-collaboration/childrens_illustrator_collaboration.md` — write disciplined art notes and a page/spread (dummy) map; confirm text/art labor division.
  - **Verse / rhyming:** `craft-tools/childrens_read_aloud_rhythm_rhyme_polish.md` — fix meter, scansion, near-rhymes, page-turn beats.
  - **Illustrated / print forms:** `representation-collaboration/childrens_accessible_inclusive_design.md` — design-in accessibility (the author controls text/content moves; flag production choices for the publisher).
  - **Nonfiction:** the matching `nonfiction-workshops/` prompt — resolve every open `VERIFY` to a source or cut the claim; assemble back matter (sources, author's note, further reading).
- Resolve EVERY open `VERIFY` marker before Gate B: either attach a real source or remove the claim. Never close a `VERIFY` by supplying a fact from memory.
- Keep any write-across-difference audit output as **flags and questions** routed to the author and a human sensitivity reader — never convert it into a "safe/authentic" verdict.
- Re-scan for age-appropriateness: confirm nothing introduced in revision exceeds the age band.

**Must Not:**
- Invent a source, date, quote, or statistic to clear a `VERIFY`.
- Emit any statement that certifies a representation as accurate, authentic, or approved.
- Let mature content slip into a young-child product.
- Narrate the illustration in the printed text.

## Instructions

1. Route to the form's Stage 5 prompt(s) per the path above.
2. **Nonfiction:** walk every `VERIFY` marker; attach a source or cut. Assemble `back-matter.md` (sources list, author's note distinguishing fact from inference, further reading).
3. **Illustrated:** produce `art-notes.md` and a dummy/page map; confirm the text doesn't describe the art.
4. **Verse/rhyming:** polish meter and rhyme to read-aloud cleanliness.
5. **Representation:** finalize the audit as a flags/questions document (`representation-audit.md`) — explicitly NOT a certification.
6. Run the Gate B check (below).

## Output Format

```
STAGE 5 — POLISH & ACCURACY ([FORM] path)
APPLIED: [illustrator collab | rhyme polish | accessible design | NF accuracy] ...
ARTIFACTS PRODUCED: [art-notes.md | back-matter.md | representation-audit.md]

NONFICTION — VERIFY LEDGER
| Claim | Resolution (source attached | claim cut) |
|-------|------------------------------------------|
open VERIFY markers remaining: 0   (must be 0 to pass)

GATE B — TRUTH & REPRESENTATION: PASS | FAIL
  - every NF specific sourced or cut (0 open VERIFY): PASS/FAIL/NA
  - back matter present (NF): PASS/FAIL/NA
  - representation audit = flags/questions only (no certification): PASS/FAIL/NA
  - no age-inappropriate content: PASS/FAIL
```

## Verification Checklist (Gate B — the orchestrator gates on this)

- [ ] Zero open `VERIFY` markers remain; every nonfiction specific is sourced or cut. No fact supplied from memory.
- [ ] (NF) Back matter is present and distinguishes verified fact from inference.
- [ ] The representation audit output is a list of risk flags and questions — it contains **no** statement certifying the portrayal as accurate/authentic/safe.
- [ ] No age-inappropriate content has entered the manuscript.
- [ ] (Illustrated) Art notes exist and the printed text does not narrate the art.
- [ ] (Verse) Read-aloud meter and rhyme are clean.

## False-Positive Prevention

- **Closing a `VERIFY` with a confident guess.** A plausible date is not a sourced date. Source it or cut it.
- **An author's note that quietly asserts invented detail.** Back matter must separate fact from inference, not launder a guess.
- **An audit that drifts into reassurance** ("this reads authentically"). Strip any certification language; keep flags and questions.
- **Mature content rationalized as "realism."** Hold the age band.
- **Accessibility bolted on as a content lecture.** Design it in; flag production choices to the publisher.
