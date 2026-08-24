---
title: "Explain-Like-I'm-Nine Converter — Plain-Language Rewrite That Keeps the Truth Intact"
category: personal-development
description: "Rewrite a technical or jargon-heavy passage so a smart nine-year-old could follow it, without dumbing down the actual claims, then prove nothing true was lost or distorted."
techniques:
  - ST-01
  - ST-02
  - RP-02
  - QA-01
  - QA-04
difficulty: beginner
tags:
  - plain-language
  - simplification
  - jargon
  - accuracy
  - communication
updated: "2026-06-21"
related_prompts:
  - domain-personal-development/prompts/thinking/thinking_mindset_shift_reframe.md
  - domain-prompt-engineering/prompt-improvement/README.md
  - domain-research-academic/research_interview_guide_designer.md
---

# Explain-Like-I'm-Nine Converter

**Objective:** Convert a technical or jargon-heavy chunk of text into a version a curious, capable nine-year-old could follow — preserving every true claim exactly, replacing jargon with honest plain words, and then auditing the rewrite to confirm nothing accurate was lost, softened, or distorted.

**When to Use:**
- You understand something well and need to explain it to a non-expert (a manager, a client, a family member, a cross-functional teammate) without losing precision.
- A document is technically correct but unreadable to its actual audience.
- You want to test your own understanding — if you cannot say it simply and truthfully, you may not understand it as well as you think.
- You are drafting an FAQ, onboarding doc, or "ELI5" section and need the simplification to be trustworthy, not just friendly.

**When NOT to use:**
- The audience IS expert and the jargon is the precise, load-bearing vocabulary they expect — simplifying would remove signal, not noise.
- The text is legally or clinically operative (a contract clause, dosing instruction, regulatory filing) where the exact original wording is what matters — paraphrase changes meaning. Summarize *alongside* the original instead of replacing it.
- You want a shorter version, not a simpler one — that is summarization, a different task.

---

## Inputs / Context

Provide the following. If something is missing, the model should state its assumption rather than guess silently.

1. **Source text** — the passage to convert, pasted between the `<source_text>` tags below.
2. **Audience reality (optional)** — who actually reads this. "Nine-year-old" is the *reading level* target, not necessarily the literal reader; a busy executive often wants nine-year-old clarity with adult framing. Note any adult framing needed.
3. **Non-negotiable terms (optional)** — any jargon that MUST be kept (e.g., a product name, a legally precise term) even if explained.
4. **Domain (optional)** — the field, so analogies are chosen honestly and not misleadingly.

```
<source_text>
[Paste the technical or jargon-heavy passage here]
</source_text>
```

---

## Constraints

### Must
- Preserve **every factual claim** in the source. If the source says a process takes "up to 30 days," the rewrite must keep "up to 30 days," not "about a month" (which drops the ceiling) or "a month" (which asserts a typical value the source never stated).
- Replace jargon with **honest** plain words — words that mean the same thing, not words that merely sound friendlier.
- Keep **hedges and qualifiers** ("usually," "may," "in most cases," "estimated"). Stripping a hedge turns a careful claim into a false certainty.
- Use **short sentences and concrete nouns**, but never invent details to make a sentence concrete.
- Use analogies **only** where they map accurately; flag any analogy that simplifies at the cost of a small inaccuracy.
- Produce the three required outputs: (a) the plain-language version, (b) a jargon-replacement table, (c) an accuracy-preservation check.

### Must Not
- Add facts, numbers, examples, or causes that are not in the source.
- Drop conditions, exceptions, or limits ("except when…", "only if…", "not including…").
- Replace a precise quantity with a vague one, or a vague one with a precise one.
- Use an analogy that is memorable but wrong (e.g., "antibodies are like soldiers that hunt down every germ" overstates specificity).
- Convert uncertainty into certainty, or a correlation into a cause.
- Add cheerful filler ("It's actually pretty simple!") that adds no information.

---

## Instructions

1. **Read for meaning, not just words.** Identify, as a private list, every distinct factual claim in `<source_text>`: each assertion, quantity, condition, exception, and hedge. This list is your fidelity checklist for later.

2. **Tag the jargon.** Mark each term, acronym, or phrase that a nine-year-old (or non-expert in this domain) would not know. For each, decide: replace it, or keep-and-define it (use keep-and-define only for non-negotiable terms or terms with no honest plain equivalent).

3. **Rewrite in plain language.**
   - One idea per sentence where possible.
   - Prefer everyday words; keep the original meaning exact.
   - Preserve order of logic so cause/effect and conditions stay attached to the right claim.
   - Keep every hedge and limit from your Step 1 checklist.

4. **Choose analogies carefully.** For any concept that benefits from a comparison, pick one only if it maps accurately. State the comparison and, if it breaks down anywhere relevant, name the limit in one short clause ("…though unlike a key, it can fit more than one lock").

5. **Build the jargon-replacement table.** For each tagged term: the original term, what you replaced it with (or "kept + defined"), and a one-line note confirming the replacement means the same thing.

6. **Run the accuracy-preservation check (QA-01).** Walk your Step 1 fidelity checklist item by item against the rewrite. For each claim, confirm it survived intact, or flag exactly what changed. Resolve any flag by fixing the rewrite, not by lowering the bar.

7. **Acknowledge residual uncertainty (QA-04).** If the source itself was ambiguous, or if a faithful plain version is still slightly harder than nine-year-old level because the concept is irreducibly complex, say so plainly rather than over-simplifying into inaccuracy.

---

## False-Positive Prevention

A "false simplification" reads clearly and feels helpful but has quietly changed what is true. Guard against each:

1. **Hedge-stripping.** "Symptoms *may* appear within a week" → "Symptoms appear within a week." The rewrite reads cleaner but asserts something the source did not. Keep the hedge.
2. **Quantity drift.** "Up to 40%" → "almost half"; "around 1 in 100,000" → "very rare." Keep the original number; add a plain gloss only beside it, never instead of it.
3. **Condition-dropping.** "Eligible *if filed before the deadline*" → "Eligible." The condition is the whole point. Keep every "if," "unless," "except."
4. **Misleading analogy.** An analogy that is vivid but wrong on a point that matters (overstating, oversimplifying a mechanism). If it cannot map accurately, drop it.
5. **Cause invented from correlation.** "X is linked to Y" → "X causes Y." Keep the weaker, accurate relationship.
6. **Confidence inflation.** "Estimated," "preliminary," "in this sample" carry epistemic weight. Do not delete them to sound more authoritative.
7. **Helpful-sounding additions.** Inserting an example or reason that "must be true" — but isn't in the source — is fabrication dressed as clarity. Add nothing.
8. **Over-flattening the irreducible.** Some ideas cannot be made nine-year-old-simple without becoming wrong. When that happens, get as simple as honesty allows and say the rest is genuinely hard — do not paper over it.

---

## Expected Output

```
## Plain-Language Version
[The rewritten passage — short sentences, honest words, every claim and hedge preserved.]

## Jargon Replaced
| Original term | Replaced with (or "kept + defined") | Same meaning? (note) |
|---------------|-------------------------------------|----------------------|
| [term]        | [plain words]                       | [why it's equivalent]|
| [term]        | [plain words]                       | [why it's equivalent]|

## Accuracy-Preservation Check
For each original claim, confirm it survived intact or flag what changed:
- [Claim 1]: PRESERVED — [where it appears in the rewrite]
- [Claim 2]: PRESERVED — [where it appears in the rewrite]
- [Claim N]: [PRESERVED | ADJUSTED — what changed and why it's still faithful]

**Hedges & limits kept:** [list every "may / usually / up to / unless / except" carried over]
**Analogies used:** [analogy → what it accurately maps → where it breaks down, if anywhere]
**Residual uncertainty:** [anything irreducibly complex, or ambiguous in the source]

**Verdict:** Nothing true was lost or distorted. | The following needs a human check: [...]
```

---

## Verification

- [ ] Every factual claim from the source appears in the plain version (checked item by item).
- [ ] No new facts, numbers, examples, or causes were introduced.
- [ ] All hedges, conditions, exceptions, and limits were preserved.
- [ ] No quantity was made vaguer or more precise than the original.
- [ ] Every jargon term is in the replacement table, with an equivalence note.
- [ ] Analogies map accurately; any that break down are flagged.
- [ ] Confidence/uncertainty language was kept, not inflated.
- [ ] The accuracy-preservation check confirms each claim or flags exactly what changed.
- [ ] Irreducibly complex points are stated honestly rather than over-simplified.
