# Prompt Structure Guide

**Purpose:** How to structure a prompt so the model reliably separates *your instructions* from *the material it operates on* — and how to diagnose a prompt that isn't working. Use this alongside [NEW_PROMPT_TEMPLATE.md](NEW_PROMPT_TEMPLATE.md) when authoring any prompt in this repository.

> **This is not a format change.** Repo prompts stay markdown-structured. This guide adds one missing layer: telling the model where injected content begins and ends.

---

## Two layers of structure

A prompt has two structural layers, and they are not in competition:

| Layer | What it is | How to structure it |
|-------|-----------|---------------------|
| **Instructional layer** | The prompt body the *author* writes — Objective, Constraints, Steps, Output Format | Markdown headers and lists (what this repo already does) |
| **Injected-content layer** | Runtime material the *model reads* — pasted data, documents, code, transcripts, drafts, examples | Named XML-style tags: `<codebase>...</codebase>` |

Markdown is excellent for the instructional layer: it organizes the prompt for the author and the model reads it fine. But markdown headers do **not** reliably mark where a pasted document ends and your next instruction begins — a `## ` inside a pasted file looks identical to a `## ` you wrote. Named tags remove that ambiguity. The model is told, explicitly, "everything between `<contract_text>` and `</contract_text>` is the thing to analyze, not an instruction."

---

## Delimiting injected content

### When to do it

Add tags whenever the prompt instructs the model to consume content that is pasted in at use time:

- Source code or a codebase
- A document, contract, transcript, email thread, or research notes
- A dataset, log, or table
- A draft to be improved
- Few-shot examples

If the prompt has no injected content — a pure instruction like "convert this CSV to JSON" where the CSV is the only thing present — tags add nothing. Skip them.

### Tag conventions

- Lowercase `snake_case`, descriptive, short (≤ 24 chars): `<student_draft>`, `<q3_financials>`, `<codebase>`, `<meeting_transcript>`.
- Prefer a specific name over a generic one. `<data>` works; `<q3_financials>` is better and never collides.
- Open and close tags on their own lines; don't wrap inline tags around individual words.
- Reference the tag name in the instructions: "Summarize the figures in `<q3_financials>`," not "Summarize the figures above."
- For *output* tagging (the model emitting tags a parser will consume) and parser regexes, see [`domain-prompt-engineering/structured-output/structured_xml_tag_pattern.md`](../domain-prompt-engineering/structured-output/structured_xml_tag_pattern.md) — stricter rules apply there.

### Before / after

**Before** — data pasted inline; the model has to guess where the brief ends:

```
Summarize this for the board:
Q3 Revenue: $4.2M (down 11% YoY)
Division A overhead: $1.8M, contributing $900K revenue
Focus on overhead risk and keep it to three bullets.
```

**After** — instruction and content are unambiguously separated:

```
Summarize the figures in <q3_financials> for the board.
Focus on overhead risk. Output: exactly three bullets, one sentence each.

<q3_financials>
Q3 Revenue: $4.2M (down 11% YoY)
Division A overhead: $1.8M, contributing $900K revenue
</q3_financials>
```

In the "before," `Focus on overhead risk...` could be read as part of the data. In the "after," it can't.

---

## Cross-vendor note

This pattern is safe across model vendors:

- **Anthropic** explicitly recommends XML tags to separate instructions, context, and data in prompts.
- **OpenAI's** GPT-5.x prompting guidance uses Markdown headers for instructional hierarchy plus XML-style tags to delimit sections and injected content.

So "markdown instructional body + XML-style tags around injected content" is the cross-vendor-safe default. It does not lock a prompt to one model.

> **Accurate framing:** structured delimiting makes output *more consistent* and reduces *structural* ambiguity (the model spends less effort guessing what's data vs. instruction). It does not make a probabilistic model "deterministic," and there is no credible fixed accuracy multiplier — avoid claims like "10x" or "deterministic output."

---

## Context dimensions: capture *why*, not just *what*

A prompt that states only the task ("write a summary of this meeting") leaves the model to invent the situation. Strong prompts capture four context dimensions in the **Inputs / Context** section:

1. **Background situation** — who the user is, what they're working on.
2. **Audience** — who the output is for; their knowledge level, role, what they need.
3. **Fixed constraints / prior decisions** — what is already decided and not up for reconsideration.
4. **Downstream purpose** — what the output is *for*: what decision it informs, where it goes next, who consumes it.

The fourth is the one most often missed. "Write a summary of this meeting" produces a different (and better) result when it also says "...so a director who wasn't there can decide whether to greenlight the project." Capture the **task** (what to do) *and* the **purpose** (why / what it feeds into) — they steer the output differently.

---

## Two quick diagnostics

**The colleague test.** Read the prompt as if you were a capable person seeing it cold, with no prior context. Could you do the task competently, or would you need to ask clarifying questions first? Those clarifying questions are exactly the gaps that make a model guess. (This mirrors Anthropic's official "show your prompt to a colleague" rule.)

**The two-reasonable-people test.** Could two reasonable people read this prompt and produce legitimately *different* outputs? If yes, it needs more structure (tighter Objective, more Constraints, clearer Output Format). If no — the instruction is already precise — added structure is just overhead.

---

## Iterating on a prompt that isn't working

Change **one** component per revision. If you change three things at once and the output improves, you've learned nothing about which one mattered. Diagnose by symptom:

| Symptom | Likely missing component | Repo section to fix |
|---------|--------------------------|---------------------|
| Output is generic / could apply to anyone | Context or Role too thin | Inputs / Context (CM-01) |
| Right content, wrong shape | Format unspecified | Output Format (ST-03) |
| Keeps including something you don't want | No rule against it | Constraints → Must Not (CM-02) |
| Almost right, but the style is off | No example of "good" | add a delimited example |
| Right, but too long / short / mis-structured | Objective or Steps under-specified | Objective (ST-01) / Steps (ST-02) |
| Model treats your instruction as data (or vice versa) | Injected content not delimited | tag the injected content (ST-04) |

---

## How this maps to the repo's technique taxonomy

Nothing here is a new technique — it's guidance on applying existing ones well:

| Idea in this guide | Technique ID |
|--------------------|--------------|
| Clear single-sentence Objective | ST-01 |
| Numbered Steps that reference tagged inputs by name | ST-02 |
| Explicit Output Format | ST-03 |
| Delimiting injected content with named tags | ST-04 (Delimited Sections) |
| Four context dimensions in Inputs / Context | CM-01 |
| Must / Must Not constraints | CM-02 |

---

## Related resources

- [NEW_PROMPT_TEMPLATE.md](NEW_PROMPT_TEMPLATE.md) — the copy-paste prompt template
- [TECHNIQUE_PICKER_FAST.md](TECHNIQUE_PICKER_FAST.md) — pick techniques by intent
- [../techniques/MASTER_TECHNIQUE_INDEX.md](../techniques/MASTER_TECHNIQUE_INDEX.md) — full technique catalog (see ST-04)
- [../domain-prompt-engineering/structured-output/structured_xml_tag_pattern.md](../domain-prompt-engineering/structured-output/structured_xml_tag_pattern.md) — tag conventions and parser regexes for *output* tagging
- [../PROMPT_QUALITY_STANDARDS.md](../PROMPT_QUALITY_STANDARDS.md) — quality tiers and checklist

---

**Last Updated:** 2026-05-14
