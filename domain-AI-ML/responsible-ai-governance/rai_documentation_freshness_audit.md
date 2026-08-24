---
title: "RAI Documentation Freshness Audit"
category: AI-ML/responsible-ai-governance
description: "Audit an existing documentation suite for staleness and drift against the currently deployed model and data — detecting stale metrics, superseded versions, changed data composition, expired reviews, and claims monitoring now contradicts — and emit a per-claim freshness verdict and refresh work-queue."
techniques:
  - ST-03
  - DS-01
  - RT-05
  - QA-12
  - RP-02
difficulty: advanced
tags:
  - documentation-audit
  - freshness
  - drift
  - staleness-detection
  - responsible-ai
updated: "2026-06-19"
related_prompts:
  - domain-AI-ML/responsible-ai-governance/rai_documentation_suite_orchestrator.md
  - domain-AI-ML/production-monitoring/mlmonitor_drift_detection_design.md
  - domain-AI-ML/responsible-ai-governance/rai_model_card_authoring.md
---

# RAI Documentation Freshness Audit

**Objective:** Compare an existing documentation suite (model card, datasheet, risk register) against the currently deployed model and live data, classify each material claim as current / stale / unverifiable, and produce a prioritized refresh work-queue.

**When to Use:**
- A documentation suite was written some time ago and you need to know whether it still describes the deployed system.
- A model was retrained, a data source changed, or monitoring surfaced drift, and the docs may now be wrong.
- A periodic review (e.g., quarterly governance) requires evidence that documentation reflects production reality.

**When NOT to Use:**
- The documents don't exist yet or need assembling — use `rai_documentation_suite_orchestrator.md` to build the coherent suite first.
- You are designing the drift detectors themselves — use `mlmonitor_drift_detection_design.md`; this prompt consumes their signals.

## Inputs / Context

- **Existing documents** — the model card, datasheet, and/or risk register to audit (with their stated dates/versions).
- **Deployed-model facts** — current model version, deployment date, and active configuration.
- **Current data snapshot** — present-day composition, volume, and source provenance.
- **Monitoring signals** — recent drift reports, per-group metric trends, incident logs.
- **Review policy** — required review intervals and expiry rules for each document type.

**Instructions:**

1. **Extract material claims.** Pull each verifiable claim from the docs: metrics, model version, data composition, intended use, limitations, review dates.
2. **Pair with ground truth.** Match each claim to the corresponding deployed-model fact, data snapshot, or monitoring signal.
3. **Assign a verdict.** Classify each claim as `CURRENT` (matches), `STALE` (contradicted/expired), or `UNVERIFIABLE` (no ground-truth source available).
4. **Detect version & date drift.** Flag superseded model versions, expired review dates, and changed data sources.
5. **Cross-check monitoring.** Mark any documented claim that live monitoring now contradicts (e.g., a stated per-group parity that has since degraded).
6. **Build the refresh queue.** Rank stale/unverifiable items by impact and assign owners and target refresh dates.

## Constraints

**Must:**
- Render a per-claim verdict (`CURRENT` / `STALE` / `UNVERIFIABLE`), never a blanket "looks fine."
- Tie every `STALE` verdict to the specific ground-truth fact or signal that contradicts the claim.
- Treat expired review dates and superseded model versions as automatic staleness flags.
- Output a prioritized refresh work-queue with owners and target dates.

**Must Not:**
- Never invent current metrics, deployed versions, data percentages, or dates to fill missing ground truth. If no source exists, the verdict is `UNVERIFIABLE` — do not guess `CURRENT` or `STALE`.
- Do not declare a claim current just because it is plausible or unchanged in wording.
- Do not silently drop claims you cannot map; list them as `UNVERIFIABLE` with the missing source named.

**Output Format:**

A per-claim freshness table (claim, document, documented value, ground-truth value, verdict, evidence), followed by a ranked "Refresh Work-Queue" with owner and target date.

The verdict column enumerates `CURRENT`, `STALE`, and `UNVERIFIABLE` — the last being this prompt's name for the insufficient-evidence outcome, and a first-class verdict rather than a gap in the table. It is the correct verdict wherever no ground-truth source was consulted for the claim, and every instance must name the unblocking datum: the specific artifact — the training run's config, the registry entry, the serving metrics dashboard, the dataset card — that would let the claim be judged. A claim recorded as `CURRENT` because nothing contradicted it has been assumed, not verified.

## Verification

- [ ] Every material claim has an explicit verdict; none left unjudged.
- [ ] Each `STALE` verdict cites the contradicting ground-truth fact or signal.
- [ ] Expired review dates and superseded versions are flagged stale automatically.
- [ ] Missing ground truth yields `UNVERIFIABLE`, not a guessed verdict.
- [ ] Every `UNVERIFIABLE` names the specific artifact that would resolve it, and no claim is marked `CURRENT` merely because no source was consulted.
- [ ] The work-queue is prioritized with owners and target dates.

## False-Positive Prevention

❌ **DON'T:**
- Mark a metric `CURRENT` because the documented number "seems reasonable" without comparing it to the live value.
- Assume the documented model version is deployed when the version field is blank or unconfirmed.
- Treat a document as fresh because its review date is recent, while its metrics predate the last retrain.
- Invent a current per-group fairness number to "confirm" the documented one matches.

✅ **DO:**
- Compare each documented metric to an actual current measurement or mark it `UNVERIFIABLE`.
- Cross-check the documented version against the deployed-model facts and flag mismatches as `STALE`.
- Distinguish "review date current" from "content current" — both must hold for `CURRENT`.
- Name the missing source (e.g., "no current per-group eval") when classifying `UNVERIFIABLE`.

## Example Output

```markdown
# Freshness Audit — Recommender Model Documentation (audited 2026-06-19)

| Claim | Document | Documented | Ground Truth | Verdict | Evidence |
|-------|----------|------------|--------------|---------|----------|
| Model version v3.0 | Card §1 | v3.0 | Deployed: v3.2 | STALE | Deploy log 2026-05 retrain |
| Overall NDCG = 0.42 | Eval Report | 0.42 (v3.0) | No v3.2 eval run | UNVERIFIABLE | Missing post-retrain eval |
| Training data 60% EU | Datasheet | 60% EU | Snapshot: 41% EU | STALE | New APAC source added Q2 |
| Per-group parity within 3% | Card §Limits | within 3% | Monitor: gap now 9% | STALE | Drift report 2026-06-10 |
| Intended use: ranking only | Card §Use | ranking only | Unchanged | CURRENT | Scope review 2026-06 |
| Last review 2025-11 | Register | 2025-11 | Policy interval: 6mo | STALE | Review expired 2026-05 |

## Refresh Work-Queue (priority order)
1. **Re-run evaluation on v3.2** → owner: ML eval team → target 2026-06-30 (unblocks 2 UNVERIFIABLE/STALE).
2. **Update per-group limitations** (parity 9%) → owner: RAI lead → target 2026-06-25.
3. **Correct version + data composition** → owner: doc owner → target 2026-07-05.
4. **Run overdue register review** → owner: governance → target 2026-06-22.
```

**Techniques Used:**
- **ST-03 (Output Format Specification):** Locks the per-claim verdict table and work-queue structure for auditability.
- **DS-01 (Decomposition):** Reduces "is the doc current?" to per-claim comparisons against ground truth.
- **RT-05 (Self-Verification):** The checklist forces a verdict and evidence on every claim before the audit is trusted.
- **QA-12 (Uncertainty Flagging):** The `UNVERIFIABLE` verdict prevents fabricated current values from masking gaps.
- **RP-02 (Role Priming):** Frames the model as an auditor comparing documents to reality, not a re-author.

**Related Prompts:**
- `rai_documentation_suite_orchestrator.md` — builds the coherent suite this audit later checks for staleness.
- `mlmonitor_drift_detection_design.md` — produces the drift signals this audit uses as ground truth.
- `rai_model_card_authoring.md` — the authoring prompt used to refresh stale card claims found here.
