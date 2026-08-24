---
title: "Email / Doc / Chat Format Variants"
category: prompt-engineering/output-formatting
description: "Generate three format-appropriate shapes of the same content from a single prompt: email, document, and chat message."
techniques:
  - ST-01
  - ST-02
  - ST-03
  - CM-02
  - QA-01
  - PR-02
difficulty: intermediate
tags:
  - format_variants
  - email
  - document
  - chat
  - output_format
updated: "2026-05-11"
related_prompts:
  - domain-prompt-engineering/output-formatting/format_markdown_contract.md
  - domain-prompt-engineering/output-formatting/format_length_budget_designer.md
  - domain-prompt-engineering/output-formatting/format_no_preamble_no_postamble.md
---

## Objective

Given a content brief, produce three structurally distinct format variants — email, document, and chat message — each shaped by the conventions, length norms, and reading context of its medium, while containing the same factual content.

## When to Use

- You need to distribute the same information across multiple channels without manually reformatting.
- You are building a prompt that must route output to different downstream systems.
- You want to audit whether a model is truly adapting structure and length, not just pasting the same text three times.
- **Not for:** translating content between audiences (that is style_audience_adaptation_prompt.md). Not for creating three pieces of different content.

## Format Specs

### Email
| Attribute | Rule |
|-----------|------|
| Subject line | Required; ≤8 words; no "FW:" or "RE:" unless context demands |
| Salutation | Required for external; optional for internal |
| Body length | 80–200 words |
| Structure | 3 paragraphs max: context → action/content → next step |
| Sign-off | Required |
| Bullets | Permitted, max 1 list, max 5 items |
| Attachments ref | "See attached [name]" if relevant |

### Document
| Attribute | Rule |
|-----------|------|
| Title | Required |
| Sections | H2 headings; min 2 sections; max 5 |
| Length | 300–800 words |
| Structure | Title → Summary (optional, ≤50 words) → Sections → [Appendix if needed] |
| Tables | Permitted for 2D data |
| Lists | Permitted; prefer numbered for sequential content |
| Audience note | Optional header comment |

### Chat
| Attribute | Rule |
|-----------|------|
| Length | ≤80 words |
| Structure | 1–3 sentences or a flat list (max 4 items) |
| Headings | Banned |
| Bold | At most 1 bold phrase per message |
| Emojis | Permitted only if register is casual |
| Tone | Matches register of the conversation |
| Links | Inline, no separate reference section |

## Inputs

| Input | Required | Notes |
|-------|----------|-------|
| Content brief | Yes | The information to convey: facts, recommendations, decisions |
| Format selection | Yes | "all three" / "email only" / "doc + chat" / any subset |
| Register | Recommended | Formal / Neutral / Casual |
| Audience | Recommended | Per format if different audiences |
| Fact-lock items | Optional | Specific facts that must appear in all selected variants |

## Constraints

**Must:**
- Every fact in the fact-lock list appears in every selected variant.
- Every variant must satisfy all rules in its format spec table.
- No variant may introduce facts not in the content brief.
- Produce a conformance check table after all variants.

**Must Not:**
- Produce a document variant that is just an email with headings added.
- Produce a chat variant that exceeds 80 words.
- Use the same subject line as the document title.
- Include emojis in Formal or Neutral register variants.

## Instructions

1. **Extract core claims** from the content brief. Label each C1, C2, …Cn. Identify which are fact-lock items.

2. **Write email variant.** Subject → salutation → para 1 (context) → para 2 (content/action) → para 3 (next step) → sign-off.

3. **Write document variant.** Title → optional summary → sections → confirm each core claim appears.

4. **Write chat variant.** Start directly with the most important claim. Keep under 80 words. Confirm all fact-lock items.

5. **Conformance check.** Fill table against each format spec.

## Output Format

```
## Email Variant
Subject: [subject line]

[Salutation],

[Para 1 — context]

[Para 2 — content/action]

[Para 3 — next step]

[Sign-off]

---

## Document Variant
# [Title]

## [Section 1]
...

---

## Chat Variant
[Message, ≤80 words]

---

## Conformance Check
| Rule | Email ✓/✗ | Doc ✓/✗ | Chat ✓/✗ |
|------|-----------|---------|---------|
| Fact-lock items present | | | |
| Length within spec | | | |
| Structure matches spec | | | |
| No invented facts | | | |
| Register consistent | | | |
```

## Verification

- [ ] Email body is 80–200 words and has a subject line.
- [ ] Document has ≥ 2 H2 sections and a title.
- [ ] Chat message is ≤ 80 words and contains no headings.
- [ ] All fact-lock items appear in every variant (cross-check using claim labels C1…Cn).
- [ ] Conformance check table is fully populated (no blank cells).
