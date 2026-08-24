# Structured Output

**Purpose:** Patterns for producing parseable, validatable output from a model — JSON, XML, markdown, dual-format — with strategies for repair, streaming, and second-pass validation.

## When to use this subdirectory

- A downstream consumer parses model output and breaks when it drifts.
- You need to choose between schema-in-prompt, native `response_format`, tool-use forcing, or XML scaffolding.
- You're seeing missing fields, type drift, near-match enums, or mid-stream parse failures.

## Prompts

| File | Description |
|------|-------------|
| `structured_json_schema_prompt_builder.md` | Convert a JSON Schema into a producer prompt; pick schema-in-prompt vs `response_format` vs tool-use forcing. |
| `structured_json_repair_pattern.md` | Detect and repair malformed JSON with an audit trail; never invent values. |
| `structured_xml_tag_pattern.md` | When XML tags beat JSON for Claude; tag conventions and a parser regex. |
| `structured_field_ordering_for_speed.md` | Reorder schema fields so consumers can short-circuit and stream usefully early. |
| `structured_optional_field_handler.md` | Pick one absence-encoding policy (null / omit / empty) per field type, aligned to consumers. |
| `structured_enum_constraint_pattern.md` | Force a value into a closed set; emit a typed `__enum_violation` instead of a near-match. |
| `structured_table_row_emitter.md` | Streamable per-row generation with per-row validation and a terminator. |
| `structured_markdown_section_contract.md` | Heading, list, and code-fence conventions a regex/AST parser can rely on. |
| `structured_dual_output_pattern.md` | Prose for users + JSON for code in one call, with a consistency check. |
| `structured_output_validator_prompt.md` | Second-pass validator that grades schema compliance and emits a typed retry instruction. |

## How they compose

- **Build → repair → validate**: `structured_json_schema_prompt_builder` produces the producer; `structured_json_repair_pattern` recovers malformed output; `structured_output_validator_prompt` grades the result.
- **Format choice**: `structured_xml_tag_pattern` and `structured_markdown_section_contract` are alternatives to JSON when prose dominates.
- **Streaming**: `structured_field_ordering_for_speed` + `structured_table_row_emitter` together make long output usefully streamable.
- **Surface contract**: `structured_optional_field_handler` and `structured_enum_constraint_pattern` define what "present" and "valid" mean across consumers.
