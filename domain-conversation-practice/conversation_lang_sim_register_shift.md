---
title: "Language Sim — Register Shift: The Same Scene Played Formal, Then Informal"
category: conversation-practice
description: "Run one communicative goal twice in the target language, once with a formal counterpart (landlord, professor, older neighbour) and once with an informal one (a friend or peer), then contrast the learner's two transcripts on the register markers that language actually uses (address forms, verb morphology or speech levels, greetings and closings, softeners, lexical choice) and flag mismatches in both directions; distinct from learn_idiom_decoder.md, which decodes the register of one expression you met, where this prompt has you produce a whole scene at two registers."
techniques:
  - CM-01
  - RT-02
  - OC-03
  - QA-01
difficulty: intermediate
tags:
  - language-learning
  - register
  - politeness
  - sociolinguistics
  - role-play
  - speaking-practice
updated: "2026-09-24"
related_prompts:
  - domain-conversation-practice/conversation_lang_sim_master_template.md
  - domain-education-teaching/learner/language/learn_idiom_decoder.md
  - domain-education-teaching/learner/language/learn_l2_grammar_explainer.md
---

# Language Sim — Register Shift

**Objective:** Make register a skill the learner *produces*, not only one they recognise. The same goal is played twice, first with someone who needs formality and then with a friend. The learner's own two versions are compared side by side on the markers that carry register in the target language. Sounding too formal counts as a mismatch just as much as sounding too casual.

**When to Use:**
- You know *vous* from *tu* (or 敬語 from plain form, or 존댓말 from 반말) on paper but default to one of them under pressure.
- You sound like a textbook with friends, or too casual with officials.
- You are moving to a country where getting register wrong has real social cost.

**Not this prompt if… / distinct from**
- You met one expression and want to know what it means and how formal it is. Use `domain-education-teaching/learner/language/learn_idiom_decoder.md`.
- You want the grammar of the formal forms explained (conjugations, honorific morphology). Use `domain-education-teaching/learner/language/learn_l2_grammar_explainer.md` first, then practise here.
- You want a single scene at one register. Any other `conversation_lang_sim_*` prompt covers that. Set `REGISTER` in the master template.

## Inputs

Fill the master template slots (`conversation_lang_sim_master_template.md`), with correction mode **delayed** by default, because the contrast is the lesson. Then give:

1. **The goal**, the same in both scenes: ask for a favour, decline an invitation, complain about noise, ask to reschedule, give bad news.
2. **The formal counterpart**, such as a landlord, professor, client or older neighbour, or accept the default for the goal.
3. **The informal counterpart**: a friend, sibling or peer.
4. **Any local norm you know**, for example that people under 30 use *du* at this workplace.

## Method

1. **State the register system (CM-01).** Before either scene, describe in 3–5 lines how register works *in this language and variety*: address forms, verb morphology or speech levels, typical formal and informal openings and closings, and characteristic softeners. Do not describe it as English politeness with the words swapped. If the variety differs from the standard (Brazilian *você*, Argentine *vos*, Québec *tu*), say so.

2. **Scene A — formal.** Run the goal with the formal counterpart. The counterpart reacts *realistically* to register errors. For example, a slightly cooler reply after an unwarranted *tu*, or no reaction at all where a native speaker would let it pass.

3. **Scene B — informal.** Same goal, informal counterpart. They react to excessive formality, for example with a joke about it, or with "why so formal?" in the target language.

4. **Contrast the two transcripts (RT-02, OC-03).** Build a table of the markers the language uses. For each marker, record what the learner produced in A, what they produced in B, and whether each fits its scene. Quote the learner's lines.

5. **Flag mismatches in both directions.** Mark *too formal* and *too informal* explicitly. Also flag **mixing** within one scene, such as *vous* with a *tu*-form imperative. Mixing is the most common intermediate error and the most noticeable one.

6. **Debrief (QA-01)** with the master template's five headings. Heading 4 is the contrast table plus the mismatch list. Heading 5 names the single marker to work on.

## The prompt block (paste into the master template's `[SCENARIO BLOCK]`)

```
SCENARIO: register shift. Same goal twice: [goal].
Scene A: you are [formal counterpart]. Scene B: you are [informal counterpart].
Before Scene A, explain briefly in [L1] how register works in [TARGET_LANGUAGE/variety].
In each scene react realistically to register errors (a cooler reply, a joke, or a native
speaker's tolerance), but never correct me in-scene.
After Scene A say only "— Scene B —" and continue.
DEBRIEF SCORING FOCUS: a contrast table of register markers A vs. B with my quoted lines,
fit in each scene, mismatches in both directions, and any mixing within a scene.
```

## Output Format

Debrief heading 4:

```
| Marker | Scene A (formal) — quoted | Fits? | Scene B (informal) — quoted | Fits? |
Mismatches: too formal → … | too informal → … | mixed within a scene → …
```

## Verification

- [ ] The register system was described for this language and variety before Scene A.
- [ ] Both scenes had the same communicative goal.
- [ ] Counterparts reacted to register the way a native speaker plausibly would, including tolerating minor slips.
- [ ] The contrast table uses markers this language actually has.
- [ ] Mismatches are reported in both directions, and mixing is checked.
- [ ] Variety norms were respected, so a correct regional form is not marked wrong.

## False-Positive Prevention

1. **English politeness in translation.** Treating "please" and "could you" as the register system of Japanese or Korean misses the verb morphology that carries it.
2. **Formal = correct.** Over-formality with friends is an error. Flag it.
3. **Standard-variety bias.** Marking Argentine *vos* or Brazilian *você* as informal errors. Judge by the stated variety.
4. **Over-sensitive counterparts.** Real speakers tolerate many learner slips. Only a counterpart reaction that a native speaker would plausibly have is useful feedback.
5. **Vocabulary-only contrast.** Swapping *bouffe* for *nourriture* while keeping *vous* is not a register shift. The table must include address forms and grammar.
6. **Ignoring mixing.** A scene that is "mostly formal" with one informal imperative sounds worse than a consistently informal one.

## Example Output

```
Settings: German (Germany) | L1 English | B1 | Delayed | Goal: ask to borrow a ladder
Register system: Sie + 3rd-person-plural verb forms vs. du + 2nd-person-singular; "Guten Tag"/"Hallo";
"Könnten Sie…" (Konjunktiv II) as a softener; "Tschüss" is informal; "Auf Wiedersehen" is neutral to formal.

Scene A — neighbour Frau Keller (70s)
Learner: Hallo Frau Keller! Hast du vielleicht eine Leiter?
Keller: (slightly cooler) Guten Tag. Ja… ich habe eine. Wofür brauchen Sie sie denn?
— Scene B — friend Jonas
Learner: Guten Tag, Jonas. Könnten Sie mir Ihre Leiter leihen?
Jonas: Haha, "Sie"? Seit wann siezen wir uns? Klar, kannst du haben.
Learner: END

Debrief (4. Scenario focus)
| Marker | Scene A — quoted | Fits? | Scene B — quoted | Fits? |
| Address | "Hast du" | No: too informal | "Könnten Sie" | No: too formal |
| Greeting | "Hallo Frau Keller" | Acceptable | "Guten Tag, Jonas" | Stiff |
| Softener | none | Missing: "Könnten Sie…" | Konjunktiv II | Fine, but unneeded with du |
Mismatches: registers reversed across scenes. Mixed within a scene: A mixed "Frau Keller" with "du".
5. Next: address-form switching. Rerun with a different formal counterpart until "Sie" comes first.
```

## Techniques Used

- **CM-01 (Explicit Context Framing):** the target language's register system is stated before any production.
- **RT-02 (Multi-Dimensional Analysis):** register is broken into markers and compared across the two scenes.
- **OC-03 (Markdown Table Specification):** the A-versus-B contrast table with quoted evidence.
- **QA-01 (Self-Verification):** mismatches are checked in both directions, plus mixing, against the stated variety.

## Related Prompts

- `domain-conversation-practice/conversation_lang_sim_master_template.md`: slots, correction modes and commands.
- `domain-education-teaching/learner/language/learn_idiom_decoder.md`: decode one expression's meaning and register.
- `domain-education-teaching/learner/language/learn_l2_grammar_explainer.md`: learn the formal forms before practising them.
