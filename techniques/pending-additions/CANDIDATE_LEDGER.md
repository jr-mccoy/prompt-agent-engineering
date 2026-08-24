# Candidate Ledger

Running log of every mined candidate and its outcome. Seeded with the batch already mined so the
novelty rate is real from the start. Update after every Fable session.

## Status key
PROMOTED (in a proposed-additions doc, pending ingest) · CORRECTED (promoted after gate fix) ·
MERGE (folded into an existing entry) · HOLD · REJECT

---

## Session 0 — five authored prompts + one system review (baseline)

| # | Candidate | Type | Origin | Gate result | Status |
|---|---|---|---|---|---|
| C1 | Partial-visibility Question tier | 1 technique | PR review | NEW; final ID QA-23 (QA-21 collided) | CORRECTED |
| C2 | Input provenance tags (+sensitivity, +Overrides lane) | 1 technique | prioritization | NEW; ID TBD (EV prefix invalid) | CORRECTED |
| C3 | Two-axis verdict (decouple answer/reasoning) | 1 technique | sunk-cost | NEW; OC-13 (OC-07 collided) | CORRECTED |
| C4 | Sweep-with-proportionality-budget (+N/A-reason) | 1 technique | DoD builder | NEW; DD-family (not DS) | CORRECTED |
| C5 | Dismissed-candidates coverage table | 1 technique | concurrency | NEW; QA-25 | CORRECTED |
| C6 | Adjacent-prompt scope fencing | 1 technique | concurrency | MERGE → AG-38 (identical mechanism) | MERGE |
| C7 | House-style: 6 recurring moves | 3 standards | cross-prompt | promote w/ proportionality precedence + insufficiency fix | HOLD (v2) |
| C8 | Copy-or-Mark (never infer IDs/paths) | 2 authoring rule | review §6 | verified; root-cause fix | PROMOTE |
| C9 | Fenced-example rule; Category line | 2 authoring rule | review §1 | verified | PROMOTE |
| C10 | Concurrency audit as gold-standard exemplar | 4 exemplar | concurrency | verified technically correct | PROMOTE (post-ingest) |
| C11 | ID/family fabrication (QA-21/OC-07/SV-09/EV) | 5 anti-pattern | review §2a/§6 | verified collisions | PROMOTE → Copy-or-Mark |
| C12 | Eng-months unit slip | 5 anti-pattern | sunk-cost example | verified | PROMOTE → M2 unit rule |
| C13 | Insufficiency verdict | 1 technique / 3 standard | review M1 | fixes decision-forcing×Question conflict | PROMOTE |
| C14 | Unit & dimension header discipline | 1 technique | review M2 | verify family at ingest | HOLD |
| C15 | Hunch / evidence-pending tier | 1 technique | review M3 | verify vs QA-04 | HOLD |
| C16 | Validity-horizon tag | 1 technique | review M4 | verify family | HOLD |
| C17 | Fable's system-review method | 6 meta-capability | the review itself | codify as review skill/guide | HOLD (brief-01 targets this) |

## Novelty tracking
- Session 0 candidates: 17. New techniques: 8 (of which 1 merged, rest corrected). Non-technique
  durable assets: 9 (authoring rules, standards, exemplar, anti-patterns, 1 meta-capability).
- Duplicate/merge rate so far: 1/9 technique candidates (C6→AG-38). **Novelty still high — keep mining.**

## Next
- Session 1 = `briefs/brief-01-contrastive-review.md` (targets C17 meta-capability + fresh candidates).

---

## Session 1 — brief-01 contrastive review (API-review prompt)

| # | Candidate | Type | Gate result | Status |
|---|---|---|---|---|
| C18 | 9-step prompt-review method | 6 meta-capability | no repo review-method exists; dedup vs correctness_prompt_specification_audit on ingest | PROMOTE (→ skill/guide) |
| C19 | Two-executor divergence test | 1 technique | absent from index | PROMOTE (new) |
| C20 | Findings-vs-presentation triage | 1 technique | absent (relates to DS-06, criterion is new) | PROMOTE (new) |
| C21 | First-invented-fact test (dry-run opening) | 1 technique | absent | PROMOTE (new) |
| C22 | Pressure-minus-counterweight rule | 1/2 | related to QA-20/FPP, absent as named | PROMOTE (modest) |
| C23 | "When method doesn't apply" scope caveat | (Check-4 input) | free scope-caveat for C18 | USE |
| — | Quote-and-consequence gate | — | == house-style evidence-or-drop | MERGE |
| — | Verifiability audit; minimal-diff fix | — | scattered/standard | FOLD into C18 |

## Novelty tracking (updated)
- Session 1: 7 self-reported mechanisms → 4 new techniques + 1 meta-capability promoted; 3 merge/fold.
- Meta-lesson logged: Fable rates novelty vs general practice; we rate vs OUR catalog — mine against our gap.
- Cumulative technique candidates: 12 new + 2 merged. Novelty rate still high → keep mining.
- Operational fix: DON'T upload the kit zip to Fable; paste brief text only (Fable correctly ignored it).

---

## Session 2 — brief-02 prompt-to-prompt handoff (T7)

**Yield: highest so far — a whole new technique family, not a single technique.**
Captured in `proposed-additions/TECHNIQUE_FAMILY_inter_prompt_contracts.md`.

| # | Candidate | Type | Gate result | Status |
|---|---|---|---|---|
| C24 | **Inter-Prompt Handoff Contracts** = NEW FAMILY (13 core mechanisms) | 1 (family) | no inter-prompt contract machinery in index; AG-07/NE-20 adjacent but distinct | PROMOTE (new family) |
| C25 | Framing principle "seam = adversarial API; contract in producer, enforcement in consumer" | 3 standard/principle | family framing statement | PROMOTE |
| C26 | Data–instruction quarantine (payload = data, both sides) | 1 technique | absent as named technique; also advances T9 | PROMOTE (new, standalone) |
| C27 | "Verification is advisory across a trust boundary" (consumer re-verifies) | 1 technique | sharpens QA-01 across a boundary | PROMOTE (variant of QA-01) |
| C28 | Spec-Extractor / Test-Writer prompt pair | 4 exemplar | technically coherent; ship as reference | PROMOTE (exemplar) |
| — | Normative micro-example | — | == Example Calibration family (few-shot) | MERGE |
| — | Producer pre-emission checklist | — | == QA-01 (+cross-boundary note) | MERGE |
| — | Verbatim source anchoring | — | == house-style evidence-or-drop | MERGE/relate |

## Novelty tracking (updated)
- Session 2: 18 self-reported mechanisms → 1 NEW FAMILY (~10 catalog-absent core mechanisms) +
  1 standalone technique + 1 QA-01 variant + 1 exemplar; 3 merges.
- Key signal: tension-targeting a new task SHAPE yields a family, not a technique. Prioritize
  remaining new-shape tensions (T9 partial-hit, T11 irreversible, T18 resumable).
- Fable's "all ports, nothing novel" was again true-vs-computing / false-vs-our-catalog — confirms
  the mine-against-our-gap rule. Highest-yield session so far.
- Cumulative: ~22 new catalog-absent mechanisms + 1 new family + 4 merges across 3 sessions.

---

## Session 3 — brief-03 irreversible-action gating (T11)

**Yield: second cluster. Captured in `proposed-additions/TECHNIQUE_CLUSTER_action_gating.md`.**

| # | Candidate | Type | Gate result | Status |
|---|---|---|---|---|
| C29 | **Action-Gating cluster** (11 core mechanisms) extends Gate/Approval family | 1 (cluster) | Gate/Approval family thin+abstract; none of these named | PROMOTE (cluster) |
| C30 | Phase-gated action cycle | 1 | absent | PROMOTE |
| C31 | Manifest-bound commit (structural TOCTOU fix) | 1 | absent | PROMOTE |
| C32 | Nonce-bound confirmation (CSRF-for-chat) | 1 | absent; near-novel | PROMOTE |
| C33 | Confirm+modify = modify | 1 | absent; near-novel | PROMOTE |
| C34 | Freshness + enumerated disarm events | 1 | absent | PROMOTE |
| C35 | Pre-commit recheck (TOCTOU) | 1 | absent as named | PROMOTE |
| C36 | Blast-radius tripwires + comprehension echo | 1 | absent; tests comprehension not compliance | PROMOTE |
| C37 | **Friction budget / ceiling** | 1 + 3 standard | absent; Fable's top pick; anti-over-caution | PROMOTE (technique + standards tightening) |
| C38 | Flag-once-then-defer | 1 | absent | PROMOTE |
| C39 | No advance/conditional authorization | 1 | absent | PROMOTE |
| C40 | Post-action reconciliation & disclosure | 1 | absent as named | PROMOTE |
| C41 | Deletion-Operator prompt | 4 exemplar | honest residuals; strong | PROMOTE (exemplar) |
| — | Channel separation for authority | — | == C26 (RECURRENCE S2→S3) | MERGE→C26 |
| — | Verify-not-retry; verbatim-figures | — | == error-propagation / evidence-or-drop | MERGE/relate |

## Novelty tracking (updated)
- Session 3: 14 self-reported → ~9 catalog-absent new + 1 cluster + 1 standards tightening (friction
  ceiling) + 1 exemplar; 3 merges (incl. first CROSS-SESSION duplicate: channel separation S2→S3).
- Signal: new-shape tensions keep yielding clusters (T7, T11). Cross-session recurrence began →
  channel separation is a confirmed core cross-cutting technique; watch for saturation.
- Cumulative across 4 sessions: 2 new families/clusters + ~31 catalog-absent mechanisms + 2 exemplars
  + 1 skill + Session-0 batch. Novelty still positive; first recurrence noted.
- Remaining new-shape cell: T18 resumable state (brief-04 candidate).

---

## Session 4 — index-integrity audit (Fable given MASTER_TECHNIQUE_INDEX in clean chat)

**Yield: a meta-capability (validator) + a batch of real repo fixes. Reprioritizes to consolidation.**

| # | Candidate | Type | Gate result | Status |
|---|---|---|---|---|
| C42 | Scripted index-integrity validator (refs resolve, ID(Name) matches, dead-links, dup-defs, count reconcile) | 6 meta-capability | none exists; built + run (`proposed-additions/tooling/audit_technique_index.py`) | PROMOTE (→ CI/pre-commit) |
| C43 | Index integrity FIXES: ~53 undefined refs, 13 dead links, 264-vs-302 count, ST-03/SV-04 dup headings, MP-04 & QA-11 mislabels | 5 anti-pattern / direct fixes | validator-confirmed | PROMOTE (cleanup changeset) |

## Verification of Fable's audit (repo-side)
- Claims 1 (QS/MA undefined), 2 (13 dead links), 3 (count mismatch), 4 (mislabels) = TRUE.
- Claim 5 (QA-15 twice; "Index by Location" dup) = OVERREACH (QA-15 has 1 def; "Index by Location" 0 hits).
- Validator found the problem ~4x larger than Fable's manual scan (53 vs 12 undefined refs).
- Pattern holds: Fable airtight on checkable facts, one overreach on the fuzzy structural claim.

## DECISIONS (user delegated)
- DoD builder → move to domain-engineering-workflows/workflows/ (category engineering-workflows/planning).
- A2 error-handling resilience audit → AUTHOR (queue as short future brief).

## Reprioritization
- Index integrity is now the CONSOLIDATION PREREQUISITE: cannot cleanly ingest 31 mechanisms + 2
  families + cluster into a file with 53 dangling refs. Sequence: harden validator → index cleanup
  → ingest additions THROUGH the validator (gate).
- Mining paused at 4 sessions (2 families/clusters + ~31 mechanisms + 2 exemplars + review skill +
  validator + Session-0 batch). T18 remains the one open new-shape cell for later.
