# Domain-Operations Expansion Roadmap

**Status as of 2026-09-24:** Wave 1 shipped (coverage roadmap) — **8 prompts** across
`process-improvement/` (4), `supply-chain-procurement/` (3), and `project-delivery/` (1).
Planned and scoped in [`../meta/COVERAGE_ROADMAP.md`](../meta/COVERAGE_ROADMAP.md),
which records the nearest-neighbour boundaries each prompt was written against.

---

## Wave 2 — candidates (not yet built)

| Candidate | Likely folder | Distinct from |
|---|---|---|
| **S&OP cadence** — monthly demand/supply/finance reconciliation and the decision meeting | `supply-chain-procurement/` | `ops_inventory_reorder_policy.md` (SKU-level policy, not the monthly plan); `domain-productivity/operating-cadence/` (individual cadence) |
| **Logistics / freight mode choice** — parcel vs. LTL vs. FTL vs. intermodal, landed cost and service trade-off | `supply-chain-procurement/` | `ops_supplier_selection_scorecard.md` (supplier, not carrier mode) |
| **Standard work + kaizen event plan** — takt, standard work sheet, a scoped 3–5 day event | `process-improvement/` | `ops_process_map_and_waste_scan.md` (diagnosis); `business_writing_sop.md` (writing the procedure) |
| **Supplier quality / corrective action (SCAR)** — issuing, tracking, and verifying a supplier's 8D response | `supply-chain-procurement/` | `ops_root_cause_a3_report.md` (your own problem, not the supplier's) |
| **Facility layout** — flow-based layout, travel distance, adjacency | `process-improvement/` | `ops_capacity_and_bottleneck_model.md` (capacity, not space) |

---

## Conventions for future authors

1. Prefix `ops_` in every subfolder; `category: operations/<subfolder>`.
2. Match Wave 1 structure: Objective → When to Use (with a "Not this prompt if…"
   line) → Inputs → Method → Output Format → Verification → False-Positive
   Prevention → one coherent Example Output with numbers that add up → Techniques
   Used → Related Prompts. Exactly three `related_prompts`.
3. Label modeled figures as modeled; tag inputs `measured` / `sampled (n=)` /
   `estimated`. Flag safety-critical and regulated work for qualified review.
4. Technique IDs must exist in `techniques/MASTER_TECHNIQUE_INDEX.md`.
5. After adding files, regenerate the index: `python3 scripts/generate_prompt_index.py`.
