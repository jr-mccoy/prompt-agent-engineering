# Gate Design — Children's Book Studio (design bundle)

Four hard gates, mapped to the factory's Gate 0/A/B/C, adapted to a content-generation system whose blast radius is craft quality and integrity (not money or security).

## Enforcement model

<!-- ENFORCEMENT: orchestrator-critique -->
<!-- DEFENSE-IN-DEPTH: 3-layers -->

Gates are enforced by **orchestrator critique**: each stage prompt ends with a Verification Checklist; the orchestrator applies each item PASS/FAIL and refuses to advance on any FAIL. Three layers of defense, in depth:
1. **In-prompt constraints** — each stage prompt's Must / Must-Not block steers the model away from violations during generation.
2. **Stage Verification Checklist** — the orchestrator's gate check after generation.
3. **Agent authority boundaries** — the role agents (`agents/*.md`) carry non-negotiable "Never" rules (no fabrication, no certification) that hold even mid-stage.

Only layer 2 blocks advancement. This is the analog of the factory's deterministic policy layer, realized as critique because the criteria are semantic.

**Why not scripts (code-not-trust):** the gate criteria ("does the child drive the climax," "is the theme preached," "is this audit a certification") are semantic judgments a lexical script can only approximate, and the blast radius is content quality rather than irreversible real-world action. A future scripted layer *could* mechanically check the computable subset — word-count band (numeric), Flesch-Kincaid vs. age band (stdlib), preaching lexical scan ("learned that…", "the lesson is…"), publishing comp/agent bracket scan, representation certification-language scan ("authentic", "accurate", "safe", "approved"), nonfiction unsourced-specific heuristic — but it is not required for this blast radius.

## Gate 0 — Age boundary (Stage 0)

<!-- GATE-0: JUSTIFIED -->

**Passes when:** a valid form + age band is selected AND the content is not mature-YA (explicit content / adult themes, ages 14+).
**On fail:** redirect the project to `domain-creative-writing/`; do not proceed.
**Closes blast-radius item:** #3 (age-inappropriate content).

## Gate A — Craft integrity (Stage 4)

<!-- SAFE-01: enforced -->  (analog: integrity of the core craft contract)
<!-- SAFE-04: na: the system's tools are read-mostly (read a domain prompt, read/write a versioned manuscript the author owns, estimate reading level); there is no network, money, or destructive operation, so least-privilege tool-restriction has no high-impact surface to bound -->

**Passes when ALL:**
- The child protagonist drives the climax (no adult rescue).
- The theme is carried by action; no stated moral remains.
- For picture books / early readers / verse, the read-aloud rhythm holds.
- The reading level matches the target age band.
**On fail:** return to Stage 4; loop the evaluator-optimizer on the failing layer.
**Override policy:** craft/stylistic flags may be overridden with a logged author decision. The four items above are the gate's core and should not be waived.

## Gate B — Truth & representation (Stage 5)

<!-- SAFE-02: enforced -->  (analog: deterministic integrity policy — non-overridable)
<!-- GATE-B-SAFETY: present -->

**Passes when ALL:**
- Every nonfiction specific traces to a real source or is cut — zero open `VERIFY` markers; none supplied from memory.
- Back matter present (NF), separating verified fact from inference.
- The write-across-difference audit output is risk flags + questions only — it contains **no** statement certifying the portrayal as accurate/authentic/safe.
- No age-inappropriate content has entered the manuscript.
**On fail:** return to Stage 5.
**Override policy:** **non-negotiable.** No-fabrication and the certification ban cannot be overridden. This is the system's load-bearing safety gate.
**Closes blast-radius items:** #1 (NF fabrication), #2 (representation over-certification), #3 (age-appropriateness re-check).

## Gate C — Publishing honesty / disclosure (Stage 6)

<!-- DISCLOSURE: see DISCLOSURE_MANIFEST.md -->
<!-- ROLLBACK: present -->  (revert to prior manuscript version; see RUNBOOK.md)

**Passes when ALL:**
- No fabricated comp titles, agent/publisher names, sales/advance figures, or submission rules — every unverifiable item bracketed `[AUTHOR TO VERIFY]`.
- Submission formatting flagged to confirm against each agency's actual guidelines.
- The deliverable manifest is complete for the form.
**On fail:** return to Stage 6.
**Override policy:** **non-negotiable** for the anti-fabrication items.
**Closes blast-radius item:** #4 (publishing fabrication).

## Kill switch

<!-- KILL-SWITCH: present -->

The author is the kill switch: because the system proposes versioned edits and never silently overwrites, the author can stop at any gate, reject a stage's output, or revert to a prior manuscript version (blast-radius item #5). There is no autonomous action that proceeds without the author's per-stage approval.
