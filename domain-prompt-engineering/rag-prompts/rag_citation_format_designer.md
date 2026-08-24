---
title: "Design a Citation Format for RAG Output"
category: prompt-engineering/rag-prompts
description: "Pick and specify a citation format — inline, footnote, hover-token, per-claim or per-paragraph — given the rendering surface, audience, and verifier path."
techniques:
  - ST-01
  - ST-03
  - CM-02
  - DC-01
  - QA-01
difficulty: intermediate
tags:
  - rag
  - citations
  - output_format
  - ux
  - verifiability
updated: "2026-05-10"
related_prompts:
  - domain-prompt-engineering/rag-prompts/rag_grounding_contract.md
  - domain-prompt-engineering/hallucination-control/hallucination_citation_required_pattern.md
  - domain-prompt-engineering/rag-prompts/rag_evaluation_harness_for_groundedness.md
---

# Design a Citation Format for RAG Output

**Objective:** Choose one citation pattern per surface and produce the exact emit-format string the model must follow, plus the renderer-side rule for resolving each citation token to a source.

**When to use:** Before deploying a RAG product. Citation format is a frozen interface contract — changing it later breaks downstream parsers and reviewer workflow.

---

## Inputs

1. `surface` — `chat_ui`, `markdown_doc`, `pdf_export`, `voice`, `api_only`.
2. `audience` — `end_user`, `internal_reviewer`, `auditor`, `developer`.
3. `granularity` — `per_claim` or `per_paragraph`.
4. `verifier_path` — `click_to_source`, `cmd_f_in_source`, `manual_lookup`, `none`.
5. `max_tokens_budget` — soft cap on citation overhead per response.

---

## Constraints

### Must
- Pick exactly one inline pattern (e.g., `[1]`, `[doc:42#span:7]`, `⟨src⟩`).
- Pick exactly one resolver (footnote list, JSON sidecar, hover tooltip metadata).
- For `per_claim`, every sentence with a factual assertion gets a citation.
- For `per_paragraph`, the citation list at paragraph end covers every claim made in that paragraph.
- For `voice`, citation appears as a spoken phrase only at the end (e.g., "Source: Smith 2024"); no inline tokens.
- Token cost per citation must fit `max_tokens_budget / expected_response_length`.

### Must Not
- Mix inline numeric and bracketed-ID styles in one response.
- Use a pattern that requires a renderer the surface does not support (e.g., hover on voice, click on markdown export).
- Allow citations without a resolvable target (token must round-trip to a source).
- Add prose like "according to the source" — the citation token does that work.

---

## Decision Table

| Surface | Audience | Recommended pattern | Resolver |
|---|---|---|---|
| chat_ui | end_user | `[1]` numeric, paragraph-end | numbered footnote list |
| chat_ui | internal_reviewer | `[doc=42#span=7]` inline | sidecar JSON |
| markdown_doc | end_user | superscript `^1` | footnote section |
| pdf_export | auditor | full citation parenthetical | bibliography |
| voice | end_user | spoken-source-only at end | none |
| api_only | developer | per-claim JSON `{text, span_ids:[...]}` | response object |

If the input combo is not in the table, the prompt returns `UNSUPPORTED_COMBINATION` with the closest two rows.

---

## Output Format

```json
{
  "inline_pattern": "<exact regex or literal template>",
  "resolver": "<footnote_list | sidecar_json | bibliography | hover_metadata | none>",
  "granularity": "per_claim | per_paragraph",
  "model_emit_rule": "<one-paragraph instruction to paste into the system prompt>",
  "renderer_rule": "<one-paragraph instruction for the UI/API layer>",
  "token_overhead_estimate_per_citation": <int>,
  "rejected_patterns": [{"pattern": "...", "reason": "..."}]
}
```

---

## Examples

- **chat_ui + end_user + per_paragraph.** `model_emit_rule`: "End each paragraph with `[n,n,...]` numbered references that map to the footnote list at the end of the message." Renderer renders `[1]` as a clickable chip resolving to passage span 1.
- **api_only + developer + per_claim.** Model emits `{"sentences": [{"text": "...", "span_ids": ["chunk_42:7"]}]}`. No inline tokens.

---

## Verification

- [ ] Exactly one inline pattern and one resolver chosen.
- [ ] Combination appears in decision table or `UNSUPPORTED_COMBINATION` returned.
- [ ] Citation overhead within budget (computed, not asserted).
- [ ] Round-trip rule stated (token → source) is unambiguous.
- [ ] No "according to" prose mixed with tokens.

---

## Anti-Patterns

1. Numeric citations without a footnote list — token has no resolver.
2. Hover metadata on a markdown export — surface drops the metadata.
3. Per-paragraph granularity with paragraph-spanning claims — reviewer cannot tell which source covers which sentence.
4. Author-date style for an internal corpus with no author field — citation is not constructible from data.
