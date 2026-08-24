---
title: "Quoting and Attribution Rules"
category: prompt-engineering/output-formatting
description: "Define verbatim vs. paraphrase quoting conventions, attribution format, and fidelity requirements for a specific output context."
techniques:
  - ST-01
  - ST-03
  - CM-02
  - QA-01
  - DC-01
difficulty: intermediate
tags:
  - quoting
  - attribution
  - citations
  - verbatim
  - paraphrase
updated: "2026-05-11"
related_prompts:
  - domain-prompt-engineering/output-formatting/format_markdown_contract.md
  - domain-prompt-engineering/rag-prompts/rag_citation_format_designer.md
  - domain-prompt-engineering/hallucination-control/hallucination_citation_required_pattern.md
---

## Objective

Design a quoting and attribution contract for a specific output context: when to quote verbatim, when to paraphrase, how to format each, and what level of source attribution is required.

## When to Use

- Outputs include excerpts from source documents and you need consistent handling across quotes.
- Legal, academic, or journalistic context requires explicit fidelity rules.
- A model is mixing verbatim and paraphrase without signaling which is which.
- **Not for:** citation format for retrieval-augmented systems (use rag_citation_format_designer.md). Not for bibliographies or reference lists.

## Quoting Decision Rules

| Condition | Quote type | Reason |
|-----------|-----------|--------|
| Source wording is legally binding (contract, regulation) | Verbatim | Paraphrase changes meaning |
| Source wording is a definition | Verbatim | Precision required |
| Source wording is ≤ 25 words and distinctive | Verbatim | Preserve voice |
| Source wording is > 40 words | Paraphrase + page/location ref | Long verbatim blocks interrupt flow |
| Claim is factual but wording is ordinary | Paraphrase + attribution | No value in exact words |
| Multiple sources agree on a claim | Synthesis + multiple attribution | Not quotable from one source |
| Source wording is unclear or dated | Paraphrase with [clarification in brackets] | Preserve meaning, update language |

## Format Options

### Verbatim quote formats

| Style | Format | Use when |
|-------|--------|---------|
| Inline short | `"Exact words" (Author, Year, p. N)` | ≤25 words |
| Block quote | `> Exact words\n> (Author, Year, p. N)` | 26–100 words |
| Inline with ellipsis | `"Exact words ... continued" (Author, Year)` | Omission; brackets for insertions |

### Paraphrase formats

| Style | Format | Use when |
|-------|--------|---------|
| Attribution tag | `According to [Author/Source], [paraphrase].` | Named source improves credibility |
| End citation | `[Paraphrase] ([Author, Year]).` | Academic or formal context |
| Unnamed synthesis | `[Paraphrase].` | Common knowledge or unnamed source |

## Inputs

| Input | Required | Notes |
|-------|----------|-------|
| Output context | Yes | e.g., "legal memo", "blog post", "research summary", "chat response" |
| Source types | Yes | e.g., "academic papers", "contract text", "interview transcripts" |
| Citation style | Optional | APA / Chicago / MLA / custom / none |
| Fidelity level | Optional | High (legal/academic) / Standard / Low (summary only) |

## Constraints

**Must:**
- Select one verbatim format and one paraphrase format for the context and apply them consistently.
- Include bracket notation rules: `[insertion]` for added context, `[...]` for omissions, `[sic]` for preserved errors.
- Specify what is required at minimum for attribution: author name only / author + year / author + year + page / URL.
- Prohibit mixing verbatim and paraphrase within the same attribution unit without a signal word.

**Must Not:**
- Present paraphrased content in quotation marks (false verbatim).
- Present verbatim content without quotation marks (invisible verbatim).
- Attribute a synthesis claim to a single source when it draws from multiple.
- Use `ibid.` or `op. cit.` in non-academic contexts.

## Instructions

1. **Define fidelity level.** Based on context, select High / Standard / Low and list what each permits.

2. **Select quote formats.** Pick one verbatim and one paraphrase format from the tables. Explain why they fit the context.

3. **Write bracket rules.** Specify how to handle insertions, omissions, errors, and translator notes.

4. **Write attribution minimums.** What must appear with every quoted or paraphrased claim.

5. **Write the enforcement block** for system prompt use.

## Output Format

```
## Quoting Contract — [Context Name]

### Fidelity Level: [High / Standard / Low]
[Definition for this context]

### Selected Formats
**Verbatim (≤25 words):** `"Exact words" ([Author], [Year], p. [N])`
**Verbatim (block, 26–100 words):** block quote with trailing attribution
**Paraphrase:** `According to [Source], [paraphrase].`

### Bracket Notation Rules
| Situation | Notation | Example |
|-----------|---------|---------|
| Inserted context | `[text]` | "the policy [adopted in 2023] requires..." |
| Omission | `[...]` | "rates increased [...] by 40%" |
| Preserved error | `[sic]` | "they're [sic] policy" |
| Translator insertion | `[trans.]` | "[trans.: the original German term]" |

### Attribution Minimums
| Quote type | Required attribution |
|-----------|---------------------|
| Verbatim | [requirements] |
| Paraphrase | [requirements] |
| Synthesis | [requirements] |

### Prohibited Patterns
- [Paraphrase inside quotation marks]
- [Verbatim without quotation marks]
- [Single-source attribution for synthesis]

### System Prompt Enforcement Block (copy-paste ready)
[Condensed block ≤150 words]
```

## Verification

- [ ] One and only one verbatim format is selected per length range (short vs. block).
- [ ] One and only one paraphrase format is selected.
- [ ] Bracket notation table covers all four cases (insertion, omission, error, translator).
- [ ] Attribution minimums table covers all three claim types (verbatim, paraphrase, synthesis).
- [ ] Prohibited patterns explicitly name the false-verbatim and invisible-verbatim cases.
