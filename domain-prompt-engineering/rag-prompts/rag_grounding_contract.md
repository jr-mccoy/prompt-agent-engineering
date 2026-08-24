---
title: "RAG Grounding Contract — Answer Only From Retrieved Passages"
category: prompt-engineering/rag-prompts
description: "System-prompt contract that constrains the model to answer only from supplied passages, attach span IDs to every claim, and refuse when evidence is absent."
techniques:
  - ST-01
  - ST-03
  - CM-01
  - CM-02
  - QA-01
difficulty: intermediate
tags:
  - rag
  - grounding
  - citations
  - refusal
  - system_prompt
updated: "2026-05-10"
related_prompts:
  - domain-prompt-engineering/rag-prompts/rag_no_answer_refusal.md
  - domain-prompt-engineering/rag-prompts/rag_citation_format_designer.md
  - domain-prompt-engineering/hallucination-control/hallucination_grounding_only_pattern.md
---

# RAG Grounding Contract

**Objective:** Produce a drop-in system-prompt block that forces the model to answer only from `context_passages`, attach a span ID to every assertion, and emit a structured refusal when the passages do not support an answer.

**When to use:** Any production RAG path where unsupported claims are a defect. Especially: legal, medical, financial, internal knowledge bases, support agents.

---

## Inputs

1. `passage_schema` — how each retrieved passage is delimited (e.g., `<doc id="...">` tags, JSON array, markdown blockquote).
2. `id_field_name` — the field that uniquely identifies a passage span (e.g., `chunk_id`, `span_id`).
3. `language` — output language ISO code.
4. `min_passages_per_claim` — integer, default 1.
5. `partial_answer_policy` — `allowed` or `forbidden`.

---

## Constraints

### Must
- Reference only content present in `context_passages`. Every factual sentence ends with one or more `[<id_field_name>=...]` tags.
- If a sentence aggregates multiple passages, list all IDs.
- If `min_passages_per_claim > 1`, refuse claims supported by fewer.
- When evidence is absent or contradictory, emit the refusal block defined below — do not fall back to parametric knowledge.
- Distinguish quoted spans (`"..."` with ID) from paraphrase (no quotes, ID required).

### Must Not
- Use prior knowledge, common sense, or training-data facts to fill gaps.
- Output any sentence without an ID tag, except for the refusal block.
- Compute, infer, or estimate numbers not present in the passages.
- Resolve pronouns or entities across passages without an explicit ID per resolution.
- Add safety, ethical, or generic disclaimers.

---

## Output Format

The contract produces a block to paste into the system prompt:

```
You answer questions strictly from the supplied <context_passages>.

RULES
1. Every factual sentence ends with [<{id_field_name}>=ID] tags listing each
   passage that supports it. Use one or more tags as needed.
2. Quote verbatim spans only inside double quotes followed by their ID tag.
3. If the passages do not support a complete answer, output exactly:

   {
     "answer": null,
     "reason": "INSUFFICIENT_EVIDENCE",
     "missing": "<one-sentence description of the missing fact>",
     "queried_ids": ["..."]
   }

4. If passages contradict each other, output:

   {
     "answer": null,
     "reason": "CONFLICTING_EVIDENCE",
     "conflict_pairs": [["ID_A", "ID_B"], "..."],
     "summary": "<one sentence describing the conflict>"
   }

5. Do not add caveats, recommendations, or knowledge not in the passages.
6. Do not infer numbers, dates, or names that are not literally present.
7. Output language: {language}.
8. Partial answers are {partial_answer_policy}. If allowed, the partial
   answer must end with the INSUFFICIENT_EVIDENCE block listing the missing
   piece.
```

The contract author returns the filled block plus this metadata:

```json
{
  "id_field_name": "<string>",
  "min_passages_per_claim": <int>,
  "partial_answer_policy": "allowed | forbidden",
  "expected_failure_modes": ["<one-line risk>", "..."]
}
```

---

## Verification

- [ ] Block contains exact refusal JSON for both INSUFFICIENT and CONFLICTING.
- [ ] Block forbids parametric fallback explicitly.
- [ ] Tag syntax is unambiguous and matches `passage_schema`.
- [ ] Partial-answer policy is stated and consistent.
- [ ] No safety boilerplate added.

---

## Failure Modes to Watch For (downstream)

1. Model ID-tags a sentence with an unrelated passage to satisfy the rule. Mitigation: post-hoc grounding eval (see `rag_evaluation_harness_for_groundedness.md`).
2. Model invents a plausible ID. Mitigation: validate every emitted ID against the passage manifest.
3. Model paraphrases a number with a small drift. Mitigation: numeric span-match check in eval.
4. Model refuses on answerable questions because passages use synonyms. Mitigation: pair with `rag_query_rewriter.md` expansion.
