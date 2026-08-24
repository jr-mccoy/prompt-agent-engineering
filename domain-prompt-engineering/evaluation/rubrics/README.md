# Evaluation — Rubrics

**Purpose:** Design, calibrate, and validate scoring rubrics for AI output evaluation — from anchor examples to LLM-as-judge prompts.

Use these prompts to build rubrics that produce consistent, reproducible scores — whether from human judges, LLM judges, or a mix. Start with calibrated anchors, then choose a scoring mode, measure agreement, and design the judge prompt.

---

## Prompt Catalog

| File | What it does |
|------|--------------|
| `rubric_calibrated_anchors.md` | Create concrete output examples anchoring each score point (1–5) on a rubric dimension, with boundary rules and a calibration mini-set |
| `rubric_pairwise_vs_pointwise.md` | Decide between pairwise and pointwise scoring modes using a factor-based decision framework, then fully design the selected mode |
| `rubric_inter_rater_agreement_protocol.md` | Measure agreement across human or LLM judges using kappa-based metrics, diagnose disagreement, and run calibration sessions |
| `rubric_llm_judge_designer.md` | Design a complete LLM-as-judge system prompt with CoT, inline rubric, bias controls, and a bias verification protocol |

---

## How to Use These Together

**Designing a rubric from scratch:**
1. `rubric_calibrated_anchors.md` — anchor each score point with concrete examples
2. `rubric_pairwise_vs_pointwise.md` — choose scoring mode
3. `rubric_llm_judge_designer.md` — if using an LLM judge, design the prompt
4. `rubric_inter_rater_agreement_protocol.md` — measure and improve agreement before launch

**Diagnosing rubric problems:**
- Scores are inconsistent across runs → `rubric_inter_rater_agreement_protocol.md`
- Scores cluster at extremes or avoid the middle → `rubric_calibrated_anchors.md` (add mid-point anchors)
- LLM judge shows length or position bias → `rubric_llm_judge_designer.md` (bias verification section)
- Unsure whether pairwise or pointwise is right → `rubric_pairwise_vs_pointwise.md`

**Switching from human to LLM judges:**
1. `rubric_inter_rater_agreement_protocol.md` — measure human baseline
2. `rubric_llm_judge_designer.md` — design LLM judge
3. Calibrate LLM against human scores (κ ≥ 0.55 required before replacing human judges)

---

## Related Folders

- `../adversarial/` — adversarial cases that can be scored with rubrics designed here
- `../regression/` — A/B tests use rubrics designed here for scoring
- `../eval-datasets/` — datasets stratified by difficulty are scored with rubrics from here
