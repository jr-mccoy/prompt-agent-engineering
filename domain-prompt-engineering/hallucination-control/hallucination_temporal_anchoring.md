---
title: "Temporal Anchoring — Pin Claims to Cutoff and Provided Dates"
category: prompt-engineering/hallucination-control
description: "Force the model to declare its knowledge cutoff, the reference date for the current task, and tag every time-sensitive claim with its temporal anchor."
techniques:
  - ST-01
  - ST-03
  - CM-02
  - QA-01
  - DC-01
difficulty: intermediate
tags:
  - hallucination
  - temporal
  - cutoff
  - as_of
  - time_sensitive
updated: "2026-05-10"
related_prompts:
  - domain-prompt-engineering/rag-prompts/rag_freshness_aware_prompt.md
  - domain-prompt-engineering/hallucination-control/hallucination_known_unknown_separator.md
  - domain-prompt-engineering/hallucination-control/hallucination_calibrated_uncertainty_prompt.md
---

# Temporal Anchoring

**Objective:** Every response begins with a temporal preamble (`knowledge_cutoff`, `now`, `evidence_date_range`) and every time-sensitive claim carries an explicit anchor. Stale or anchor-missing claims are downgraded or refused.

**When to use:** Tasks where the model must distinguish "what was true on training data" from "what is true now". Especially: news, prices, schedules, regulations, employment, releases, status.

---

## Inputs

1. `knowledge_cutoff` — ISO date the model's parametric knowledge ends (e.g., model card value).
2. `now` — ISO date considered "current" for this task.
3. `evidence_date_range` — `{start, end}` over the supplied evidence; `null` for parametric-only tasks.
4. `time_sensitive_classes` — subset of `[price, status, role, version, schedule, regulation, count, location]`.
5. `staleness_action` — `refuse`, `caveat`, or `as_of`.

---

## Constraints

### Must
- Begin response with a one-line preamble: `KNOWLEDGE_CUTOFF=<date>; NOW=<date>; EVIDENCE_RANGE=<start>..<end>`.
- For every claim in `time_sensitive_classes`, append `(as of <date>, source=<id|parametric>)`.
- If a claim's anchor date is older than `now - 30 days` for `price`, `now - 1 day` for `status`, etc. (configurable per class), apply `staleness_action`.
- Distinguish parametric-anchored claims (`source=parametric`, anchor=`knowledge_cutoff`) from evidence-anchored claims explicitly.
- Refuse to use the present tense ("is", "currently") on any anchor older than the class threshold.

### Must Not
- Use parametric knowledge to update an evidence-anchored claim with a newer date.
- Drop the preamble for brevity.
- Anchor a claim to a date that does not appear in the evidence or the inputs.
- Round anchor dates ("around 2024") — use the most precise date present.
- Assume `now == knowledge_cutoff` if `now` is not supplied; refuse instead.

---

## Class Staleness Defaults

| Class | Stale if anchor older than |
|---|---|
| `price` | 30 days |
| `status` | 1 day |
| `role` (employment) | 90 days |
| `version` | 14 days |
| `schedule` | 7 days |
| `regulation` | 365 days |
| `count` | 90 days |
| `location` | 365 days |

Override via input. The list is exhaustive for the prompt; new classes require explicit additions.

---

## Instructions

1. Emit preamble.
2. For each candidate claim, classify whether it falls in `time_sensitive_classes`.
3. Determine the anchor: best-supported evidence date, else `knowledge_cutoff` if parametric is allowed for this task, else refuse.
4. Compute age = `now - anchor`. If exceeds threshold, apply `staleness_action`.
5. Render: `<claim> (as of <anchor>, source=<id_or_parametric>)`.

---

## Output Format

```
KNOWLEDGE_CUTOFF=<date>; NOW=<date>; EVIDENCE_RANGE=<start>..<end>

<answer body, with each time-sensitive claim anchored>

---
ANCHOR_REPORT:
```
```json
{
  "claims": [
    {"text": "...", "class": "price", "anchor_date": "...", "source": "doc_42|parametric", "age_days": <int>, "stale": <bool>, "action_taken": "none | refused | caveat | as_of"}
  ],
  "stale_count": <int>,
  "refused_count": <int>
}
```

---

## Verification

- [ ] Preamble present and complete.
- [ ] Every time-sensitive claim has `(as of <date>, source=...)`.
- [ ] No present-tense verb on a stale claim.
- [ ] No anchor date that is not present in evidence or `knowledge_cutoff`.
- [ ] Stale claims triggered the configured action.
- [ ] Anchor report counts match body.

---

## Anti-Patterns

1. "Currently, X is …" with no date and no evidence.
2. Mixing knowledge-cutoff facts and evidence facts under one anchor.
3. Caveat = "may be outdated" without naming the age.
4. Anchor date rounded to year when the source has month-day precision.
