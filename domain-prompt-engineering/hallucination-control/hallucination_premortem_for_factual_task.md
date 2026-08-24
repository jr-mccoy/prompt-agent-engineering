---
title: "Pre-Mortem for a Factual Task — Anticipate Fabrication Classes"
category: prompt-engineering/hallucination-control
description: "Before generation, enumerate the specific fabrication classes the task is most exposed to and pick a guard for each — converting risk into prompt structure."
techniques:
  - ST-01
  - ST-02
  - CM-02
  - QA-01
  - PR-03
difficulty: advanced
tags:
  - hallucination
  - premortem
  - fabrication_taxonomy
  - guard_selection
  - risk_anticipation
updated: "2026-05-10"
related_prompts:
  - domain-prompt-engineering/hallucination-control/hallucination_invented_entity_audit.md
  - domain-prompt-engineering/hallucination-control/hallucination_calibrated_uncertainty_prompt.md
  - domain-prompt-engineering/hallucination-control/hallucination_grounding_only_pattern.md
---

# Pre-Mortem for a Factual Task

**Objective:** Before generating, walk a fixed fabrication-class taxonomy against the task and emit a per-class risk score plus the chosen guard. Output is a guard manifest the calling code installs as part of the system prompt or post-hoc validators.

**When to use:** First time a new factual task is run, after a hallucination incident, or when extending a prompt to a new domain. Not a per-call check — a design-time check.

---

## Inputs

1. `task_description` — what the model is being asked to do.
2. `evidence_available` — list of evidence types and their coverage.
3. `output_audience` — `end_user`, `regulator`, `internal_reviewer`, `another_system`.
4. `prior_incidents` — optional list of past hallucinations on similar tasks, with class.
5. `guard_budget` — `light` (≤ 1 guard), `medium` (≤ 3), `heavy` (≤ 6).

---

## Constraints

### Must
- Score every class in the taxonomy as `low`, `medium`, or `high` for this task.
- Justify each score in one sentence tied to inputs.
- Pick a guard for every class scoring `medium` or `high`, up to `guard_budget`.
- If `guard_budget` is exceeded, drop the lowest-impact guard explicitly — do not silently omit.
- Include any class flagged in `prior_incidents` at minimum `medium`.

### Must Not
- Treat the taxonomy as exhaustive of all hallucination — it is a working set, name extras under `other`.
- Use vague guards like "be careful". Each guard must be a named pattern with a referenceable prompt.
- Assume `evidence_available` solves classes it does not cover (e.g., RAG does not solve numeric drift).
- Skip the taxonomy walk because the task "feels safe".

---

## Fabrication Class Taxonomy

| Class | Definition | Common guard |
|---|---|---|
| `invented_entity` | Made-up name, ID, URL, citation | `hallucination_invented_entity_audit.md` post-hoc |
| `numeric_drift` | Number paraphrased into a wrong value | `extractive_quote` mode + numeric exact-match validator |
| `temporal_blur` | Stale fact stated as current | `hallucination_temporal_anchoring.md` |
| `over_specification` | Detail beyond what evidence supports | `hallucination_known_unknown_separator.md` |
| `confident_inference` | Logical leap presented as fact | `hallucination_calibrated_uncertainty_prompt.md` |
| `evidence_overreach` | Citation pointing at unrelated passage | `rag_grounding_contract.md` + entailment eval |
| `omission_as_fact` | "Not mentioned" presented as "does not exist" | refusal contract w/ explicit `cause: NOT_IN_EVIDENCE` |
| `conflict_collapse` | Two conflicting sources averaged | `rag_conflict_resolution_across_sources.md` |
| `format_imitation` | Plausible-looking IDs, DOIs, function names | regex validator + `source_manifest` check |
| `other` | Class not on this list — describe | custom |

---

## Instructions

1. Read `task_description`. Identify the output's factual surface (entities, numbers, dates, citations).
2. For each class, score risk:
   - `high`: task output centrally depends on this dimension and evidence is incomplete.
   - `medium`: task touches it but evidence partially covers it.
   - `low`: task does not touch this dimension.
3. Apply the prior-incidents floor.
4. Select guards within budget. Prefer covering `high` over `medium`. If two guards overlap, keep the more specific.
5. Emit manifest.

---

## Output Format

```json
{
  "task": "<task_description summary>",
  "audience": "<output_audience>",
  "class_scores": [
    {"class": "invented_entity", "score": "low|medium|high", "justification": "<one sentence>"},
    "..."
  ],
  "selected_guards": [
    {"class": "...", "guard_prompt": "<path or name>", "install_point": "system_prompt | validator | both"}
  ],
  "deferred_guards": [
    {"class": "...", "reason": "budget"}
  ],
  "residual_risk": ["<one-sentence risk left after guards>", "..."]
}
```

---

## Verification

- [ ] Every class scored.
- [ ] Each guard cites a specific prompt or validator (not "be careful").
- [ ] `prior_incidents` floor honored.
- [ ] Guards within `guard_budget`; deferred guards listed explicitly.
- [ ] Residual risks named (no claim of "fully covered").

---

## Anti-Patterns

1. "We use RAG, so we are grounded" — RAG does not solve numeric drift, temporal blur, or over-specification.
2. Selecting all guards regardless of risk — increases prompt cost, slows output, and reviewer fatigues.
3. Premortem run once and never updated — model and corpus changes shift class risk.
4. No installed validator — design-time pre-mortem with no runtime enforcement is wishful thinking.
