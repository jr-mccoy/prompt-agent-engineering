# Ingestion Changeset — Fable Prompt Batch (5 prompts)

Exact edits to apply when staging each prompt into the repo. Two lint rules recur, justified
by repeated evidence across the batch:

- **LINT-1 (SE category):** software-engineering prompts use `category: code-analysis/<sub>`,
  **not** `category: software-engineering/analysis/<sub>` (the directory path). Both SE prompts
  in this batch made this slip; both decision-making conventions were already correct.
- **LINT-2 (fenced example):** the `## Example Output` body must be wrapped in a fenced code
  block so its headings don't pollute the document's own heading hierarchy/TOC.

Cross-refs between batch members are **forward-references** that resolve automatically **if the
batch is ingested together**. Ingesting any one alone leaves broken links — so **batch-ingest**.

---

## 1. PR diff review  →  `domain-software-engineering/analysis/quality/quality_pull_request_diff_review.md`
- **LINT-1:** `category: software-engineering/analysis/quality` → `category: code-analysis/quality`
- Cross-ref `quality_error_handling_resilience_audit.md` is a forward-ref to prompt #? (idea A2,
  not yet authored). Either author A2 in the same batch, or drop this one link.
- Example already fenced ✓. No other changes.

## 2. Prioritization framework selector  →  `domain-decision-making/decisioning_prioritization_framework_selector.md`
- **Category decision:** `decision-making/prioritization` is a new subcategory-of-one but follows
  the modern `decision-making/<sub>` convention → **recommend KEEP as-is.**
- All three cross-refs exist ✓. Already contains a numeric self-recount step ✓. No edits needed.

## 3. Opportunity / sunk-cost audit  →  `domain-decision-making/decisioning_opportunity_sunk_cost_audit.md`
- **Category decision:** `decision-making/cost-reasoning` (new subcategory-of-one, conformant) →
  **recommend KEEP.**
- Cross-ref to `decisioning_prioritization_framework_selector.md` is a batch forward-ref (resolves).
- **CONTENT FIX (add numeric self-recount) — the one real edit in the batch.** The example's
  "Eng-months" column mixes units (v2 build shown as `4` reads as calendar months; it is
  8 engineer-months at 2 eng × 4 mo, while the switch branch's `1 + 8` is engineer-months).
  Two-part fix:
  - **(a) Prompt:** in Instructions step 6 (adversarial pass), add a sub-bullet:
    *"Numeric recount: recompute every quantity in the comparison table from its components,
    and state the unit of each column (calendar-months vs engineer-months vs cash) in the header."*
  - **(b) Example:** relabel the column and correct the v2 build figure so units are consistent
    (either express both branches in engineer-months — v2 build = 8, switch revamp = 8 — or add
    an explicit "eng-months" unit note and keep the arithmetic internally consistent).

## 4. Definition-of-Done / acceptance-criteria builder  →  PLACEMENT DECISION REQUIRED
- Current: `category: decision-making/planning` (new subcategory-of-one). Content, example, and
  2 of 3 cross-refs are software-engineering.
- **Recommended: MOVE to `domain-engineering-workflows/workflows/` with
  `category: engineering-workflows/planning`**, filename e.g.
  `workflow_definition_of_done_builder.md`. It becomes the DoD/AC exemplar that cluster lacks.
  - *Alternative (if kept in decision-making):* genericize the worked example to a non-software
    deliverable (report / event / hiring loop) to earn the general-planning placement, and use
    filename `planning_definition_of_done_builder.md`.
- Cross-refs: two forward-refs to batch members (PR review, prioritization) — resolve on batch-ingest.

## 5. Concurrency correctness audit  →  `domain-software-engineering/analysis/quality/quality_concurrency_race_condition_audit.md`
- **LINT-1:** `category: software-engineering/analysis/quality` → `category: code-analysis/quality`
- **LINT-2:** wrap the `## Example Output` body (starting `# Concurrency Correctness Audit —
  wallet-service`) in a fenced code block. (Technical content verified correct — do not alter it.)
- Cross-ref `quality_error_handling_resilience_audit.md` is a forward-ref (idea A2). Same
  resolution as #1.

---

## Global post-ingest tasks
- [ ] Update `PROMPT_INDEX.json` and `PROMPT_INDEX.md` with the 5 new entries (path, category,
      techniques, tags, description).
- [ ] Apply the technique-index additions (`TECHNIQUE_INDEX_ADDITIONS.md`) and assign final IDs;
      then update each prompt's `techniques:` list if it should cite a new ID.
- [ ] Apply the house-style block (`STANDARDS_HOUSE_STYLE_BLOCK.md`) to PROMPT_QUALITY_STANDARDS.md.
- [ ] Decide A2 (error-handling resilience audit): author it in this batch to resolve the two
      dangling cross-refs, or drop those links.
- [ ] Confirm the two subcategory-of-one categories (`decision-making/prioritization`,
      `decision-making/cost-reasoning`) are acceptable, or flatten to `decision-making`.
