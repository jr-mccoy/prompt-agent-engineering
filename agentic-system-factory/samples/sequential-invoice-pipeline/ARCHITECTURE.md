# ARCHITECTURE — invoice-intake-pipeline

**System:** invoice-intake-pipeline · **Author/date:** factory sample, 2026-06-20 · **Status:** approved (sample)

## 1. Use case & scope
- **One-sentence use case:** Take an uploaded invoice document, extract its fields, validate them against the matching purchase order and vendor master, and — only after deterministic checks plus a human approval — post the payable to the accounting system.
- **Job-to-be-done:** Replace manual three-way matching and keying of invoices with a sourced, validated payable that a human approves before any money moves.
- **Success criteria (observable gates):**
  - [ ] Extracted fields trace back to spans in the source document (no invented totals/payees).
  - [ ] Every posted invoice matched a real PO + vendor record (no fabricated matches).
  - [ ] No invoice posts above the approval threshold, or with any unresolved discrepancy, without a recorded human approval.
  - [ ] A retried post never double-pays (idempotency enforced).
- **Inputs:** an uploaded invoice document (**UNTRUSTED** — OCR'd text/PDF from an external party); read-only PO + vendor-master lookups (trusted system of record).
- **Outputs:** a structured, validated invoice record; a discrepancy report; on approval, a posted payable (or a dry-run preview).
- **Autonomy level:** acts on read-only lookups; **recommends-only on the money-moving post** (code + human approve, model never posts).
- **Blast radius:** **money / write** — posting creates a payable in the accounting system. Read paths are read-only.
- **Out of scope:** vendor onboarding, PO creation, payment execution/disbursement scheduling, GL period close, tax determination.

## 2. Step-0 justification (the gate)

<!-- GATE-0: JUSTIFIED -->
<!-- JUSTIFICATION-START -->
This is intentionally NOT a planning agent: the stage order (extract, then validate, then post) is fixed and code-controlled, so a single model call is too little (messy-document extraction plus multi-document discrepancy reasoning need separate model steps with different inputs and graders) while a full autonomous agent is too much (there is no runtime planning, replanning, or tool-selection freedom to justify it, and the money-moving post must be gated by deterministic code plus a human, never chosen by a model). The lowest rung that works is a code-orchestrated sequential workflow whose individual stages are model-powered.
<!-- JUSTIFICATION-END -->

- **Rung chosen:** TP-03 sequential pipeline (code-orchestrated, LLM-powered stages — the workflow rung).
- **Rejected lower rungs:** single model call (can't separate extraction grading from discrepancy grading; no place to wedge the deterministic post gate); a direct function call (no model needed — false, extraction/discrepancy reasoning over messy documents needs a model).
- **Rejected higher rungs:** TP-02 single agent / TP-06 orchestrator-workers (no input-dependent decomposition or runtime stop decision; the flow is fixed, so the extra autonomy adds blast-radius risk for no capability gain).
- **Accepted cost:** ~3 sequential model steps per invoice + lookups — justified because the alternative (one mega-prompt) makes the money-write ungovernable.

## 3. Topology & primitives
- **Topology:** TP-03 sequential pipeline (aliases: chained workflow; deterministic graph with LLM nodes; LangGraph fixed-edge chain).
- **Selection variables:** control = **code** (deterministic stage order); structure = sequential; plan = **fixed at design time** (no runtime planning).
- **Primitives:** 3 stage agents (extractor → validator → poster) run in fixed order by an orchestrating controller; tools = read-only PO/vendor lookup + a gated accounting-post; shared run-state persisted externally with idempotency key; per-stage isolated context returning a typed record; a deterministic HITL approval gate sits between validator and poster; per-stage + whole-run tracing; kill switch checked before every stage.

## 4. Architecture
### 4.1 Component map
```
invoice doc (UNTRUSTED)
   → [STAGE 1 EXTRACT]  model → typed InvoiceRecord (fields traced to spans)
   → [STAGE 2 VALIDATE] model + read-only PO/vendor lookups → DiscrepancyReport
   → [GATE: code policy] if amount ≥ THRESHOLD or any unresolved discrepancy → HUMAN APPROVAL required
   → [STAGE 3 POST]     code posts via idempotency key (dry-run option) → PostedPayable
```
The controller (deterministic code) owns the arrows. A model never decides to advance or to post.

### 4.2 Seams
| Seam | From → To | Crosses | Validation |
|------|-----------|---------|------------|
| S1 | document → extractor | untrusted OCR text | text handled as data only (SAFE-01); extractor cannot call tools or change the payee/amount target — it only emits fields |
| S2 | extractor → validator | typed InvoiceRecord | schema check: required fields present, numeric totals parse, every field carries a source span |
| S3 | validator → gate | DiscrepancyReport | deterministic policy reads amount + discrepancy flags; routes to HITL when threshold/discrepancy hit |
| S4 | gate → poster | approved record + approval token | code verifies approval token + idempotency key before any write; missing/invalid ⇒ no post |
| S5 | poster → accounting | post call | idempotency key dedupes; dry-run returns a preview with no write |

### 4.3 Context / durability
Each stage gets fresh-instruction context + only the prior stage's typed output (not raw upstream text where avoidable). Run-state (record, discrepancy report, approval token, idempotency key, stage cursor) is persisted externally; a crashed run resumes from the last completed stage and never re-posts a key already marked posted.

### 4.4 Cost / model right-sizing
| Component | Model | Why |
|-----------|-------|-----|
| Extractor | strong | messy/variable document layouts; high cost of a wrong total/payee |
| Validator | mid–strong | structured discrepancy reasoning against retrieved PO/vendor data |
| Poster | **none (deterministic code)** | posting is policy + idempotency, not a model decision |

## 6. Gates summary
- Gate 0: done (§2) · Gate A: GATE_DESIGN.md · Gate B: EVAL_HARNESS.md · Gate C: DISCLOSURE_MANIFEST.md · Kill switch: `config.halt` checked before each stage (especially before any post).

## 8. Referenced existing prompts
`aiagent_complexity_ladder_gate`, `aiagent_human_in_the_loop_design`, `aiagent_prompt_injection_untrusted_content_defense`, `aiagent_durable_execution_state_persistence`, `aiagent_hard_gates_designer`.
