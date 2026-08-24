# Disclosure Manifest — Children's Book Studio (design bundle)

All six disclosure dimensions, per the factory's Gate C.

## Dimension 1 — Identity & purpose
<!-- DISCLOSURE-DIM-1: complete -->
An AI prompt-orchestration system that helps an author take a children's-book idea to a finished manuscript + submission package. It is an authoring aid, not a publisher, agent, or substitute for human editorial/sensitivity review.

## Dimension 2 — Capabilities & boundaries
<!-- DISCLOSURE-DIM-2: complete -->
**Can:** classify form/age, develop concept and structure, draft, run a layered revision loop, polish to form (art notes, rhyme, accessibility), assemble nonfiction back matter, and build a submission package. **Cannot / will not:** verify nonfiction facts (it flags `VERIFY`), certify cultural authenticity, verify comps/agents, produce final illustration, or handle mature-content YA.

## Dimension 3 — Data & inputs
<!-- DISCLOSURE-DIM-3: complete -->
Inputs are the author's own idea, drafts, and research (trusted) plus any external facts a nonfiction project asserts (untrusted until sourced). No personal data beyond what the author provides; no external data is fetched autonomously. Manuscripts are the author's files; the system writes versioned copies and never silently overwrites.

## Dimension 4 — Human oversight
<!-- DISCLOSURE-DIM-4: complete -->
The author is in the loop at every gate and approves each stage's output. Integrity gates (B no-fabrication / certification ban, C anti-fabrication) are non-overridable. The author is the kill switch and owns all files.

## Dimension 5 — Limitations & failure modes
<!-- DISCLOSURE-DIM-5: complete -->
See `RUNBOOK.md` for the failure-mode catalog. Headline limits: the system can *propose* a plausible nonfiction fact (mitigated by the `VERIFY` discipline + Gate B), can draft a portrayal that reads fine but is culturally off (mitigated by the flags-only audit + a required human reader), and can suggest comps that sound right but are wrong (mitigated by bracketing). None of these mitigations replaces human judgment.

## Dimension 6 — Safety, evaluation & impact
<!-- DISCLOSURE-DIM-6: complete -->
**Safety:** four hard gates closing five blast-radius items (`GATE_DESIGN.md`); the audience is children, so the misinformation and age-appropriateness gates are treated as load-bearing. **Evaluation:** capability + safety/integrity evals (`EVAL_HARNESS.md`), with non-negotiable pass bars on fabrication, certification, publishing honesty, and scope. **Impact:** intended to raise the craft floor and protect young readers from fabricated/age-inappropriate content; the chief risk is an author over-trusting unverified output, which the bracketing/`VERIFY` discipline and explicit "what it won't do" disclosures are designed to counter.
