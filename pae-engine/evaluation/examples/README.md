# Examples

Generated from `pae_eval.plan.example_plan()` and
`pae_eval.pricing.example_snapshot()`. Regenerate rather than hand-edit.

**These are templates, not the sealed plan.** The model identifiers and the
prices are dated placeholders retrieved on 2026-09-02; both must be
re-verified against official provider documentation and re-pinned before
any sealed run.

Note on schemas: validation lives in the Python modules
(`plan.validate_plan`, `benchmark.validate_benchmark`,
`pricing.PricingSnapshot.from_json_obj`) rather than in parallel JSON
Schema files. One executable definition cannot disagree with itself; two
declarations of the same contract eventually do, and the JSON copy is
always the one that rots. Schema *identifiers* are versioned in
`pae_eval.constants` and are carried in every emitted artifact.
