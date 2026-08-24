---
name: pacu-flashcard-deck-builder
description: Build a flashcard deck for high-volume PACU recall topics — meds, normal ranges, landmarks, complications, reversal agents — in Anki-importable CSV and markdown formats. Use when the user asks for "flashcards", "drill cards", "spaced repetition deck", "Anki deck", or needs rapid-recall material. Produces cards with atomic front/back, tags, and source citations.
tags:
  - pacu
  - nursing-education
  - flashcards
  - spaced-repetition
updated: "2026-04-14"
---

# PACU Flashcard Deck Builder

## Purpose

Produce a flashcard deck for a PACU topic in two formats: (1) Anki-importable CSV and (2) human-readable markdown. Cards are atomic, testable, and tagged for filtering.

## When to use

- User asks for "flashcards", "drill cards", "Anki", "spaced repetition", "quick recall".
- Topic has dense discrete facts (meds, doses per source, normal ranges, landmarks, complication signs, reversal pairs, Aldrete components).

## When NOT to use

- Topic requires mechanistic reasoning → `pacu-in-depth-explainer`.
- User wants scenario-based assessment → `pacu-quiz-generator` or `pacu-case-scenario-writer`.

## Inputs required

1. **Topic(s).**
2. **Card count target** (default 30).
3. **Card types** — default mix: basic (front/back), cloze, and reverse-basic (ask both directions for paired facts like med ↔ reversal).
4. **Source chapters.**
5. **Tags** the user wants applied.

## Workflow

1. **Confirm inputs.**
2. **Extract atomic facts.** One card = one fact. Split anything compound.
3. **For each card, produce:** front, back, tag(s), source citation, card-type marker.
4. **Reverse-basic pairs** for symmetric facts (Reversal: naloxone ↔ opioid; flumazenil ↔ benzodiazepine).
5. **Cloze cards** for phrases where blanking one word tests meaningful recall.
6. **Write CSV** — Anki-compatible columns: `Front;Back;Tags;Source;Type` (semicolon separator to avoid comma conflicts; user imports with semicolon delimiter).
7. **Write markdown mirror** — same cards, human-readable table.
8. **Safety reminder. Self-check.**

## Output format

````markdown
# {Topic} — PACU Flashcard Deck

> Safety reminder: Recall aid only — memorized numbers must still be verified against current facility protocol at the bedside.

## Import instructions (Anki)
- Save the CSV block below as `{topic}-pacu-deck.csv`.
- In Anki: File → Import → set field separator to `;`.
- Mapping: Field 1 → Front, Field 2 → Back, Field 3 → Tags.

## CSV
```
Front;Back;Tags;Source;Type
"Normal Aldrete pass-to-Phase-2 score (minimum per many facilities)";"per facility protocol — often ≥ 9/10; verify your unit's cut-off";"aldrete;discharge";"per facility";"basic"
"Naloxone reverses which drug class?";"Opioids";"reversal;pharm";"Drain's Ch. XX";"reverse-basic"
...
```

## Markdown table
| # | Front | Back | Tags | Source | Type |
|---|---|---|---|---|---|
| 1 | ... | ... | ... | ... | basic |
...

## Tag taxonomy used
- `pharm`, `reversal`, `vitals`, `aldrete`, `airway`, `complication`, `landmark`, `per-facility`, ...
````

## Source-fidelity rules

- Any card with a specific number cites a source or uses *per facility protocol*.
- Reversal-agent pairs only where class-level fact is not facility-dependent.
- Do not create cards that memorize facility-specific content (paging numbers, code-cart drawer assignments) — those cards create false confidence.

## Self-check

- [ ] Each card is atomic (one fact front, one answer back).
- [ ] Paired facts use reverse-basic cards.
- [ ] Every card has source + tags.
- [ ] No cards memorize facility specifics.
- [ ] CSV uses `;` separator and includes header row.
- [ ] Safety reminder at top.
