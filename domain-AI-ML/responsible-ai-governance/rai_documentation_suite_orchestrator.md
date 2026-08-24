---
title: "RAI Model Documentation Suite Orchestrator"
category: AI-ML/responsible-ai-governance
description: "Orchestrate the full model documentation bundle — model card, dataset datasheet, risk register, and evaluation report — into one coherent, cross-referenced suite with a single source of truth so shared facts never diverge across documents."
techniques:
  - ST-03
  - DS-01
  - DS-02
  - QA-12
  - RP-02
difficulty: advanced
tags:
  - documentation-suite
  - orchestration
  - single-source-of-truth
  - cross-references
  - responsible-ai
updated: "2026-06-19"
related_prompts:
  - domain-AI-ML/responsible-ai-governance/rai_model_card_authoring.md
  - domain-AI-ML/data-for-ml/mldata_datasheet_authoring.md
  - domain-AI-ML/responsible-ai-governance/rai_model_risk_register.md
---

# RAI Model Documentation Suite Orchestrator

**Objective:** Coordinate the model card, dataset datasheet, risk register, and evaluation report into a single coherent suite — defining what each artifact owns, how they cross-reference, and how consistency is enforced — so facts are stated once and never contradict each other.

**When to Use:**
- You are producing more than one governance document for the same model and need them to agree.
- Shared facts (metrics, data composition, intended use) currently live in multiple places and risk drifting apart.
- Audit or compliance requires a documented, cross-referenced documentation bundle rather than scattered files.

**When NOT to Use:**
- You only need to author one document — use the specific authoring prompt (e.g., `rai_model_card_authoring.md` or `mldata_datasheet_authoring.md`) directly; this prompt coordinates, it does not re-author.
- You are checking an existing suite for staleness — that is a freshness audit, not orchestration.

## Inputs / Context

- **Model inventory** — which documents are in scope (card, datasheet, register, eval report) and their current state.
- **Shared facts** — the canonical metrics, dataset composition, intended use, and limitations that recur across documents.
- **Audience & compliance needs** — who reads each artifact and any regulatory format requirements.
- **Source-of-truth location** — where canonical facts will live (e.g., a facts ledger or the eval report).
- **Existing drafts** — any already-written documents to reconcile.

## Constraints

**Must:**
- Define a single source of truth for each shared fact and require other documents to reference it, not restate it.
- Assign clear ownership: state which artifact owns each category of information.
- Specify the cross-references between documents and a consistency-check pass before sign-off.
- Produce an assembly/review workflow with named gates.

**Must Not:**
- Never invent metric values, dataset percentages, dates, or evaluation results. Pull only from the shared-facts input; mark gaps as `UNKNOWN — pending source document`.
- Do not duplicate a fact's full value in multiple documents (that creates drift); reference the source instead.
- Do not re-author the underlying documents here — delegate to the individual authoring prompts.

**Instructions:**

1. **Map ownership.** Assign each information category to exactly one owning artifact (e.g., per-group performance → eval report; data composition → datasheet).
2. **Establish the source of truth.** Designate where each shared fact is canonically stated and how others reference it.
3. **Define cross-references.** List the explicit pointers between documents (card → datasheet, register → eval report, etc.).
4. **Delegate authoring.** Route each artifact to its authoring prompt; collect outputs without rewriting them.
5. **Run consistency checks.** Verify shared facts match across all documents and that no value is independently restated.
6. **Specify the workflow.** Define assembly order, review gates, and the sign-off that locks the suite.

**Output Format:**

An "Ownership Map" table, a "Source of Truth & Cross-Reference" table, a "Consistency Checklist," and an "Assembly & Review Workflow" section. Mark missing facts as `UNKNOWN`.

## Verification

- [ ] Each information category has exactly one owning artifact.
- [ ] Every shared fact has a single source of truth; others reference it.
- [ ] Cross-references between documents are explicit and bidirectional where needed.
- [ ] No metric or composition value is independently restated in two documents.
- [ ] The workflow defines assembly order and sign-off gates.

## False-Positive Prevention

❌ **DON'T:**
- Copy the headline accuracy number into the card, the register, AND the eval report — three places to fall out of sync.
- Let two documents each "own" intended use, producing subtly different scope statements.
- Treat the suite as assembled when documents merely sit in the same folder with no cross-references.
- Fill an empty datasheet field with a value inferred from the model card to "make it consistent."

✅ **DO:**
- State the metric once in the eval report; the card and register link to it.
- Give intended use a single owner (the model card) and point the register at it.
- Require explicit "see [document §X]" references that a reviewer can follow.
- Leave unknown fields as `UNKNOWN — pending [source document]` and queue them.

## Example Output

```markdown
# Documentation Suite Plan — Fraud Detection Model v2.1

## Ownership Map
| Information Category | Owning Artifact | Referenced By |
|----------------------|-----------------|---------------|
| Intended use & scope | Model Card | Risk Register, Eval Report |
| Training data composition | Datasheet | Model Card, Eval Report |
| Per-group performance metrics | Eval Report | Model Card, Risk Register |
| Open risks & residual scores | Risk Register | Model Card (limitations) |

### Source of Truth & Cross-References
| Shared Fact | Canonical Source | How Others Reference It |
|-------------|-----------------|-------------------------|
| Overall AUC = 0.91 | Eval Report §3 | Card §Performance → "see Eval Report §3" |
| 18% synthetic minority samples | Datasheet §2 | Eval Report §1 → "see Datasheet §2" |
| Recourse process | UNKNOWN — pending Risk Register MR-03 | n/a (queued) |

### Consistency Checklist
- [ ] Intended-use wording identical (by reference) across card + register
- [ ] AUC stated only in Eval Report; card/register link, not restate
- [ ] Data composition figures match Datasheet exactly

### Assembly & Review Workflow
1. Author Datasheet → 2. Author Eval Report → 3. Author Model Card (references 1–2) →
4. Author Risk Register (references 1–3) → 5. Consistency pass → 6. Governance sign-off (locks suite).
```

**Techniques Used:**
- **ST-03 (Output Format Specification):** Locks the ownership/cross-reference tables so the suite has a consistent backbone.
- **DS-01 (Decomposition):** Breaks the bundle into discrete artifacts with explicit boundaries.
- **DS-02 (Sequential Reasoning):** Orders authoring so each document can reference completed upstream sources.
- **QA-12 (Uncertainty Flagging):** `UNKNOWN — pending source` prevents fabricated facts from filling gaps to force false consistency.
- **RP-02 (Role Priming):** Frames the author as a coordinator, not a re-author of underlying documents.

**Related Prompts:**
- `rai_model_card_authoring.md` — authors the model card this orchestrator coordinates and cross-references.
- `mldata_datasheet_authoring.md` — authors the dataset datasheet that owns data-composition facts.
- `rai_model_risk_register.md` — the living register the orchestrator wires into the card's limitations section.
