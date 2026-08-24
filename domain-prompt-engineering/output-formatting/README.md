# Output Formatting

**Purpose:** Prompts for designing, enforcing, and verifying the structural and length properties of model output — independent of voice or content.

---

## When to Use This Subdirectory

- You need to lock down heading depth, list style, or code-fence usage across a prompt.
- You want hard word/token caps with a self-check method the model can apply.
- You need to eliminate preamble/postamble patterns from responses.
- You are designing for a specific delivery surface (email, streaming UI, chat) and need format-appropriate output.

---

## Prompts

| File | One-line description |
|------|---------------------|
| `format_markdown_contract.md` | Design exact heading depth, list style, code-fence, and table rules for a rendering environment; produces a copy-paste system prompt block. |
| `format_length_budget_designer.md` | Define hard caps on total words, tokens, and per-section counts with a self-check enforcement block. |
| `format_table_design_prompt.md` | Choose columns, sort order, and alignment for a table; applies a list-vs-table decision rule first. |
| `format_no_preamble_no_postamble.md` | Eliminate opener affirmations and sign-off lines with a system prompt block and regex detection patterns. |
| `format_one_sentence_answer_pattern.md` | Enforce a one-sentence brevity contract with a sufficiency checklist and defined fallback structures. |
| `format_streaming_friendly_design.md` | Reorder output so the first 50 tokens are maximally useful in a streaming UI; diagnoses anti-patterns by token position. |
| `format_email_vs_doc_vs_chat_variants.md` | Generate email, document, and chat-message variants of the same content from one prompt, each conforming to its medium's conventions. |
| `format_quoting_and_attribution_rules.md` | Define verbatim vs. paraphrase quoting rules, bracket notation, and attribution minimums for a specific output context. |

---

## Decision Guide: Which Prompt to Use

| Situation | Start here |
|-----------|-----------|
| Markdown rendering is broken or inconsistent | `format_markdown_contract.md` |
| Output is too long / token budget exceeded | `format_length_budget_designer.md` |
| Need a table but unsure of structure | `format_table_design_prompt.md` |
| Responses start with "Sure," or end with "Let me know..." | `format_no_preamble_no_postamble.md` |
| Need single-sentence answers | `format_one_sentence_answer_pattern.md` |
| Streaming UI feels slow despite fast tokens | `format_streaming_friendly_design.md` |
| Same content needed in email + doc + chat | `format_email_vs_doc_vs_chat_variants.md` |
| Mixing verbatim and paraphrase quotes inconsistently | `format_quoting_and_attribution_rules.md` |

---

## Related Subdirectories

- `style-and-voice/` — for voice, tone, register, and density rules (complements formatting)
- `domain-prompt-engineering/structured-output/` — for schema-level output (JSON, XML, typed fields)
- `domain-prompt-engineering/compression-and-cost/` — for token reduction and cost optimization
