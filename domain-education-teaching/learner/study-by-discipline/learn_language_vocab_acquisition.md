---
title: "Language Vocabulary Acquisition"
category: education-teaching/learner/study-by-discipline
description: "Spaced vocabulary acquisition system for language learners: generates definition, example sentence, cognate analysis, anti-confusion pairs, usage register notes, and a review interval recommendation for each target word."
techniques:
  - ST-01
  - ST-02
  - ED-04
  - RT-04
  - CM-10
difficulty: beginner
tags:
  - language-learning
  - vocabulary
  - spaced-repetition
  - anti-confusion
  - cognates
  - register
updated: "2026-05-15"
related_prompts:
  - domain-education-teaching/learner/study-by-discipline/learn_language_grammar_drill.md
  - domain-education-teaching/learner/memory-and-recall/learn_spaced_review_scheduler.md
  - domain-education-teaching/learner/memory-and-recall/learn_flashcard_quality_auditor.md
---

## Objective

Generate a complete vocabulary acquisition package for each target word: definition in the target language, natural example sentence, cognate analysis (is there a helpful or dangerous false cognate?), an anti-confusion pair (the word most likely confused with this one and how to tell them apart), usage register (formal/informal/colloquial/written only), and a spaced review interval based on word difficulty.

## When to Use

- When encountering new vocabulary in a target language and wanting to encode it durably, not just recognize it once
- When building vocabulary lists for an exam (DELF, DELE, JLPT, HSK, IELTS, GRE, etc.)
- When a learner keeps recognizing words in reading but cannot produce them in speaking or writing (recognition-production gap)
- When vocabulary confusion errors keep appearing (learner conflates two similar-sounding words)

**Do not use** for vocabulary in the learner's first language (L1) — this prompt is designed for second language (L2) acquisition mechanics (false cognates, register, anti-confusion pairs). For grammar pattern practice in the target language, use `learnstudy_language_grammar_drill.md`.

## Instructions

1. **Collect inputs.**
   - Ask: "What target language are you learning?"
   - Ask: "What is your first language (L1)?"
   - Ask: "What is your current level? (A1/A2 beginner, B1/B2 intermediate, C1/C2 advanced, or equivalent)"
   - Ask: "Provide the vocabulary list. For each word, include: the word itself, any context you've seen it in (optional), and the domain (academic, everyday, business, literary, colloquial)"

2. **For each word, generate a vocabulary card with 7 components.**

   **Component 1 — Core definition:**
   - In the target language first (immersive), then in the learner's L1 for verification
   - Include word class (noun/verb/adjective/adverb/preposition) and any grammatical features (gender, irregular conjugation, countable/uncountable, transitive/intransitive)

   **Component 2 — Natural example sentence:**
   - One sentence in the target language at the learner's current level + one more complex sentence for C1+ learners
   - Translation of each sentence
   - Highlight the target word in context

   **Component 3 — Cognate analysis:**
   - Is this word a cognate with a word in the learner's L1? If so:
     - True cognate: same meaning → note as memory aid
     - False cognate (faux ami): similar form but different meaning → **prominently flag as a confusion risk**
   - If no cognate: note the etymological root if it aids encoding

   **Component 4 — Anti-confusion pair:**
   - Name the word most likely to be confused with this word (similar sound, similar form, or similar domain)
   - Provide a minimal distinguishing rule: one sentence or contrast pair that makes the difference memorable

   **Component 5 — Usage register:**
   - Formal / Neutral / Informal / Colloquial / Written only / Spoken only / Literary / Technical
   - One-sentence register note: "This word is appropriate in [context] but sounds [wrong/strange/overly formal] in [other context]."

   **Component 6 — Encoding hook:**
   - A memory technique tailored to the word: visual image, story fragment, sound-alike in L1, spatial anchor, or emotional association
   - This is personalized — if the learner provides L1 sound-alikes, use them

   **Component 7 — Review interval recommendation:**
   Based on the following difficulty factors:
   - Has no cognate in L1: +1 difficulty point
   - Has a dangerous false cognate: +2 difficulty points
   - Has a common anti-confusion pair: +1 difficulty point
   - Abstract (vs. concrete) meaning: +1 difficulty point
   - Irregular grammar: +1 difficulty point
   
   Assign interval:
   - 0–1 points: Review in 5–7 days (easy)
   - 2–3 points: Review in 2–3 days (medium)
   - 4–5 points: Review daily for 3 days, then extend (hard)

3. **Flag false cognates prominently.**
   Any word with a false cognate gets a ⚠ False Friend alert at the top of its card, in red-style formatting.

4. **Generate a session summary.**
   After all cards:
   - Total words this session
   - Count by difficulty: Easy / Medium / Hard
   - Words to review tomorrow (Hard tier)
   - Words to review in 2–3 days (Medium tier)
   - False friends to watch out for this week

## Output Format

```
# Vocabulary Acquisition: [Target Language] — Session [N]
Target language: [language] | L1: [learner's language] | Level: [level] | Words: N

---

## Word [#]: [Target word] ([pronunciation if non-Latin script])

[⚠ FALSE FRIEND ALERT if applicable]

**1. Definition:**
[Target language definition]
([L1 translation])
Word class: [noun/verb/adj/etc.] | [Grammatical notes]

**2. Example sentences:**
• [Target language sentence with word in **bold**] → "[L1 translation]"

**3. Cognate analysis:**
[True cognate / False cognate / No cognate — with explanation]

**4. Anti-confusion pair:**
[Target word] vs. [Confusion word]: [Minimal distinguishing rule]

**5. Register:**
[Register label] — [One-sentence note on where to use / avoid]

**6. Encoding hook:**
[Personalized memory technique]

**7. Review interval:**
Difficulty: [0–5 points] → Review in [N days]

---

[Repeat for each word]

---

## Session Summary

Words this session: N
- Easy (5–7 days): [list]
- Medium (2–3 days): [list]
- Hard (daily): [list]
- ⚠ False friends to watch: [list]

Next review: [Date for Hard tier]
```

## Example Output

---

**Input:** Target language: Spanish | L1: English | Level: B1 | 5 words from a literature reading: *embarazada, sensible, comprometido, realizar, actual*

---

# Vocabulary Acquisition: Spanish — Session 4
Target language: Spanish | L1: English | Level: B1 | Words: 5

---

## Word 1: embarazada

⚠ **FALSE FRIEND ALERT**

**1. Definition:**
*Estar embarazada* = estar en estado de gestación, esperando un bebé
(English: to be pregnant — NOT "embarrassed")
Word class: adjective (feminine past participle used as predicative adjective) | Note: Only used with *estar*, not *ser*

**2. Example sentences:**
• "María está **embarazada** de seis meses." → "María is six months pregnant."
• "Descubrió que estaba **embarazada** después de la boda." → "She found out she was pregnant after the wedding."

**3. Cognate analysis:**
⚠ **FALSE COGNATE (Faux Ami):** "Embarazada" looks like "embarrassed" but means "pregnant." Using this word to say "I was embarrassed" in Spanish will cause a very memorable (and embarrassing) misunderstanding. The Spanish word for embarrassed is **"avergonzado/a"** or **"sonrojado/a"**.

**4. Anti-confusion pair:**
*embarazada* (pregnant) vs. *avergonzada* (embarrassed)
Rule: If your face is red, use *avergonzada*. If you're expecting a baby, use *embarazada*. The "baraza" in *embarazada* comes from "obstruction" — the bump! (folk etymology, but memorable)

**5. Register:**
Neutral/standard — appropriate in formal and informal contexts alike. Can also say *estar esperando un bebé* (informal) or *estar en estado de buena esperanza* (formal/literary).

**6. Encoding hook:**
PICTURE: A very large baby bump making it hard to move through a narrow door — the "embarrassment" is about not fitting, but the word means pregnant. Or: "bara" in the middle sounds like "Bara" = a big round shape. A round belly. Pregnant.

**7. Review interval:**
Difficulty: False cognate (+2) + common confusion pair (+1) = **3 points → Review in 2–3 days**

---

## Word 2: sensible

⚠ **FALSE FRIEND ALERT**

**1. Definition:**
*Sensible* = que muestra buen juicio, razonable; OR que percibe sensaciones (sensitive)
(English: "sensible" in Spanish means SENSITIVE or REASONABLE — NOT "sensible" as in practical/reasonable in the same way)
Word class: adjective

More precisely:
- *sensible* in Spanish = sensitive (to emotions, sensations) → "Es muy sensible, llora fácilmente"
- "Sensible" as in practical/reasonable in English = *sensato/a* in Spanish

**2. Example sentences:**
• "Es una persona muy **sensible** al frío." → "She is very sensitive to cold."
• "La decisión más **sensata** sería esperar." → "The most sensible decision would be to wait." *(Note: sensata, not sensible!)*

**3. Cognate analysis:**
⚠ **FALSE COGNATE:** "Sensible" in Spanish ≠ "sensible" in English. English "sensible" = Spanish *sensato*. Spanish *sensible* = English "sensitive."

**4. Anti-confusion pair:**
*sensible* (sensitive, emotionally responsive) vs. *sensato* (sensible, reasonable, prudent)
Rule: A **sensible** person cries at movies (*sensible* = sensitive). A **sensato** person saves money (*sensato* = sensible/practical).

**5. Register:**
Neutral — used in both formal and informal contexts. *Sensato* is slightly more formal.

**6. Encoding hook:**
Sound-alike: *sensible* in Spanish sounds like "sensible" in English but means the OPPOSITE in nuance. Remember: Spanish *sensible* = English "sensitive" (both refer to feelings/sensations). If you want the English meaning of "sensible," reach for *sensato*.

**7. Review interval:**
Difficulty: False cognate (+2) + anti-confusion pair (+1) = **3 points → Review in 2–3 days**

---

## Word 3: comprometido/a

**1. Definition:**
*Comprometido/a* (from *comprometerse*) = (1) engaged to be married; (2) committed to a cause or ideology; (3) in a difficult/compromising situation
(English: no single equivalent — "committed," "engaged," or "compromised" depending on context)
Word class: adjective / past participle | Irregular: from *comprometer* (not *comprometir*)

**2. Example sentences:**
• "Están **comprometidos** desde el verano pasado." → "They've been engaged since last summer."
• "Es un artista muy **comprometido** con los derechos humanos." → "He's an artist deeply committed to human rights."
• "La situación lo dejó en una posición **comprometida**." → "The situation left him in a compromising position."

**3. Cognate analysis:**
Partial cognate: "compromised/committed" → Related but context-dependent. Requires knowing which of the three meanings applies from context.

**4. Anti-confusion pair:**
*comprometido* (engaged/committed) vs. *comprensivo* (understanding/sympathetic)
These are confused because both contain "compren-/comprom-" and are positive adjectives. Rule: *comprometido* involves obligation/action; *comprensivo* involves emotional understanding.

**5. Register:**
Neutral in all three meanings. The "engaged to be married" meaning is the most common in everyday speech. The "politically committed" meaning is common in journalistic and academic writing.

**6. Encoding hook:**
"Comprometerse" → "to make a promise" → A promise is a commitment. If you're *comprometido* with a person, you promised to marry them. If you're *comprometido* with a cause, you promised to fight for it.

**7. Review interval:**
Difficulty: No dangerous false cognate (+0) + multiple meanings (abstract, +1) = **1 point → Review in 5–7 days**

---

## Word 4: realizar

⚠ **FALSE FRIEND ALERT**

**1. Definition:**
*Realizar* = (1) to carry out, to accomplish, to do (a task); (2) in some contexts: to realize/fulfill (a dream or goal)
(English: does NOT primarily mean "to realize" as in "to become aware of")
Word class: verb | Regular -ar conjugation

The English meaning "to realize" (to become aware) = **darse cuenta de** in Spanish.

**2. Example sentences:**
• "Vamos a **realizar** el proyecto en tres etapas." → "We are going to carry out the project in three stages."
• "*Me **di cuenta de*** que había olvidado las llaves." → "I **realized** I had forgotten the keys." *(Note: darse cuenta, not realizar!)*

**3. Cognate analysis:**
⚠ **FALSE COGNATE:** "Realizar" looks like "realize" but primarily means "to carry out/accomplish." For the English sense "I realized something," use *darse cuenta de*.

**4. Anti-confusion pair:**
*realizar* (to accomplish, carry out) vs. *darse cuenta de* (to realize/become aware of)
Rule: If you DID something, use *realizar*. If you UNDERSTOOD something suddenly, use *darse cuenta de*.

**5. Register:**
Slightly formal — more common in written/professional contexts. In everyday speech, "hacer" is often used instead ("hicimos el proyecto"). In bureaucratic and academic writing, *realizar* is standard.

**6. Encoding hook:**
*Realizar* = "to make real" → to realize a plan = to make it real = to accomplish it. The "become aware of" meaning (English) is a separate cognition — not making something happen, but noticing it happened.

**7. Review interval:**
Difficulty: False cognate (+2) + register note (+0) + abstract meaning (+1) = **3 points → Review in 2–3 days**

---

## Word 5: actual / actualmente

**1. Definition:**
*Actual* = current, present, contemporary (NOT "actual" in the English sense of "real/genuine")
*Actualmente* = currently, at the present time (NOT "actually" as in "in fact")
(English: "actual" = real, genuine; "actually" = in fact/really → these are false cognates)
Word class: adjective (*actual*) / adverb (*actualmente*)

**2. Example sentences:**
• "El presidente **actual** tomó posesión en enero." → "The current president took office in January."
• "**Actualmente**, vivo en Madrid." → "Currently, I live in Madrid."
• "La situación **actual** es preocupante." → "The current situation is worrying."

**3. Cognate analysis:**
⚠ **FALSE COGNATE:** "Actual" in Spanish = "current/present," not "real." "Actualmente" = "currently," not "actually." The English word "actual" = *verdadero/real* in Spanish. The English word "actually" = *en realidad* or *de hecho* in Spanish.

**4. Anti-confusion pair:**
*actual* (current) vs. *verdadero* (actual/real/genuine)
*actualmente* (currently) vs. *en realidad / de hecho* (actually/in fact)
Rule: If you mean "right now / present-day," use *actual/actualmente*. If you mean "for real / in truth," use *verdadero/en realidad*.

**5. Register:**
Neutral — common in both written and spoken Spanish. *Actualmente* is slightly more formal than *ahora mismo* (right now) or *hoy en día* (nowadays).

**6. Encoding hook:**
"Actual" in Spanish refers to what is "actual" at this moment — what's happening now, in the news, in the current era. Don't confuse with the English use where "actual" = "genuine." Mnemonic: "The **actual** news" → *las noticias **actuales***" (current events).

**7. Review interval:**
Difficulty: False cognate (+2) + anti-confusion pair (+1) = **3 points → Review in 2–3 days**

---

## Session Summary

Words this session: 5
- **Easy (review in 5–7 days):** comprometido/a
- **Medium (review in 2–3 days):** embarazada, sensible, realizar, actual/actualmente
- **Hard (review daily):** none this session
- ⚠ **False friends to watch this week:** embarazada, sensible, realizar, actual/actualmente

**Next review:**
- Tomorrow or day after: embarazada, sensible, realizar, actual
- In 5–7 days: comprometido/a

*Tip: These 4 false friends are among the most common Spanish errors for English speakers. Use them in one sentence each today (out loud if possible) before the next review session.*

---

## False-Positive Prevention

**❌ DON'T** mark a word as "learned" after recognizing it once in context. Recognition ≠ production fluency.

**✅ DO** test production explicitly: can the learner write the word in a new sentence from scratch, without seeing it, before marking it as acquired?

**❌ DON'T** skip the anti-confusion pair. The most common vocabulary errors in exams and conversation come from confusing two similar words — preventing this is as important as learning the target word.

**✅ DO** include one anti-confusion pair for every word, even if the confusable word is outside the current word list.

**❌ DON'T** treat a true cognate as automatically "easy." Cognates still require encoding the register, grammatical gender/class, and usage context — especially if the learner's L1 cognate has drifted in meaning.

**✅ DO** provide a register note for cognates and flag if the grammatical gender or word class differs from what the learner might expect by analogy.

**❌ DON'T** assign the same review interval to all words regardless of false-cognate risk. False cognates need more frequent review because interference from L1 reactivates the wrong meaning.

**✅ DO** use the difficulty scoring system to differentiate review intervals, and flag false cognates in the session summary for weekly monitoring.

## Quality Criteria

- [ ] Every card has all 7 components (definition, example, cognate, anti-confusion, register, encoding hook, review interval)
- [ ] False cognates are flagged prominently at the top of the card (⚠ alert)
- [ ] Anti-confusion pair provides a minimal distinguishing rule (not just names both words)
- [ ] Example sentences are in the target language first, with translation
- [ ] Review intervals are differentiated by difficulty score (not uniform)
- [ ] Session summary includes false friends list

## Techniques Used

- **ST-01 (Clear Objective Statement):** Objective specifies recognition-production gap as the core problem being solved — not vocabulary list generation
- **ST-02 (Structured Sequential Instructions):** Four-step process ensures input collection → card generation → false-cognate flagging → session summary in order
- **ED-04 (Personalization):** Encoding hooks are tailored to the learner's L1 — a sound-alike in English is only a hook for an English speaker
- **RT-04 (Memory Encoding):** Encoding hook component applies elaborative encoding, imagery, and sound-based memory techniques
- **CM-10 (Memory Scaffold Architecture):** Review interval system creates a persistent spaced-review structure across sessions — this is not a one-time vocabulary list
