---
title: "Language Sim — Native-Speed Listening: Fillers, Fast Speech, and Asking for Clarification"
category: conversation-practice
description: "The partner speaks as natives actually do: fillers, false starts, reduced and elided forms written as spoken, run-on turns with key facts buried mid-stream. The learner must extract a hidden checklist of facts and use target-language clarification requests (specific rather than generic) instead of pretending to understand, and is scored on facts captured, clarification quality and bluffing detected. Deliberately ungraded input, distinct from the i+1 comprehensible input of learn_adaptive_input_output_loop.md and from pronunciation production in learn_pronunciation_coach_text.md."
techniques:
  - CM-01
  - ST-16
  - QA-11
  - QA-04
difficulty: advanced
tags:
  - language-learning
  - listening
  - authentic-input
  - clarification-strategies
  - role-play
  - fluency
  - natives-talk-fast
  - lost-in-conversation
  - asking-to-repeat
updated: "2026-09-24"
related_prompts:
  - domain-conversation-practice/conversation_lang_sim_master_template.md
  - domain-education-teaching/learner/tutoring/learn_adaptive_input_output_loop.md
  - domain-education-teaching/learner/language/learn_pronunciation_coach_text.md
---

# Language Sim — Native-Speed Listening

**Objective:** Close the gap between course dialogues and real speech. The partner talks the way natives do, with fillers, false starts, reductions and a key fact tucked into the middle of a ramble. The learner's job is to *get the facts* and to *ask well* when they miss something. Asking well means a specific clarification in the target language, not "what?", and never nodding along.

**When to Use:**
- You understand your teacher and your textbook audio but lose native speakers after a few seconds.
- You catch yourself saying "yes, yes" to things you did not understand.
- You want to practise the phrases that buy time and pin down details: "Sorry, did you say Tuesday or Thursday?"

**Not this prompt if… / distinct from**
- You want input pitched *just* above your level so you can learn from it. Use `domain-education-teaching/learner/tutoring/learn_adaptive_input_output_loop.md`. That input is graded on purpose. This input is deliberately ungraded.
- You want to work on *producing* sounds, stress and connected speech. Use `domain-education-teaching/learner/language/learn_pronunciation_coach_text.md`.
- You are below about B1. Authentic-speed input is frustrating before then. Use the master template at your level instead.

## Text-mode caveat

A text model cannot produce audio speed. This sim **writes fast speech as it sounds**: reduced forms (French *chuis* for *je suis*, *y'a* for *il y a*; Spanish *pa'* for *para*, *'tá* for *está*; English *gonna*, *d'you*), fillers (*euh, bah, pues, o sea, bueno, 那个, えーと*), false starts and self-corrections. If you use a voice interface, add: "Speak at natural native speed; do not slow down unless I ask."

## Inputs

Fill the master template slots (`conversation_lang_sim_master_template.md`). Level must be B1 or above. Correction mode is **off** by default, because listening is the skill here and the debrief handles comprehension. Then give:

1. **Setting**: a friend giving directions, a colleague explaining a change of plan, a landlord explaining building rules, a voicemail-style monologue.
2. **Number of hidden facts**: 4–6 by default.

## Partner behaviour (ST-16)

- Before the scene, the model **privately fixes a checklist** of 4–6 concrete facts (times, places, names, numbers, conditions) and states only *how many* there are.
- Turns are 3–6 sentences long, with at least one filler and one reduction per turn. Each key fact is placed mid-turn, never first or last.
- At least once, the partner **self-corrects** a fact ("Tuesday — no, wait, Wednesday").
- When the learner asks for clarification, the partner behaves like a real speaker. A *specific* request ("Did you say 7:30?") gets a direct answer. A *generic* request ("What?") gets the whole thing again, a bit faster or rephrased, not slower. The partner repeats something slowly **once** per fact if the learner asks for it explicitly. After that, they rephrase.
- If the learner replies as though they understood when a fact was missed, the partner does not correct them. The bluff is recorded for the debrief.

## The prompt block (paste into the master template's `[SCENARIO BLOCK]`)

```
SCENARIO: native-speed listening. Setting: [setting].
Privately fix [N] concrete facts I must catch. Tell me only how many.
Speak as natives do: fillers, false starts, reduced forms written as spoken,
3–6 sentences per turn, key facts mid-turn, one self-correction during the scene.
When I ask for clarification: answer specific questions directly; answer vague ones by
repeating faster or rephrasing; slow down only once per fact and only if I ask.
If I respond as if I understood but didn't, do not correct me; note it.
DEBRIEF SCORING FOCUS: (a) the fact checklist, each marked caught / caught after
clarification / missed / bluffed; (b) each clarification request I made, quoted,
rated specific or generic, with a more specific version in [TARGET_LANGUAGE];
(c) the reduced forms and fillers that caused misses, with their full forms.
```

## Method

1. **Confirm settings (CM-01)** in L1. State the number of hidden facts and remind the learner that asking is allowed and scored.
2. **Run the scene** under the partner behaviour rules.
3. **Score the facts (QA-11).** For each fact on the checklist, mark it *caught*, *caught after clarification*, *missed* or *bluffed* (the learner acted as though they understood but did not). Bluffing is the most important outcome to surface.
4. **Rate the clarification requests.** Quote each one and rate it *specific* ("¿El martes o el jueves?") or *generic* ("¿Qué?"). Give a more specific version for every generic one.
5. **Name the culprits (QA-04).** For each missed or bluffed fact, name the feature that hid it: a reduction, a filler run, the self-correction, or a mid-turn position. Give the full form. Where the cause is uncertain, say so rather than guessing.
6. **Debrief** with the master template's five headings. Heading 4 contains steps 3–5. Heading 5 gives the single most useful clarification phrase to take away.

## Output Format

Debrief heading 4:

```
Facts: [n caught] / [N] — clarification-assisted: [n] — missed: [n] — bluffed: [n]
| Fact | Status | Where it was hidden |
| Your clarification requests | Specific / generic | Better version |
| Reduced form or filler that caused a miss | Full form |
```

## Verification

- [ ] The fact checklist was fixed before the scene, and only its size was announced.
- [ ] Every turn contained natural fillers or reductions, and one self-correction occurred.
- [ ] Specific and generic clarification requests got different, realistic responses.
- [ ] Bluffs were not corrected in-scene and were reported in the debrief.
- [ ] Every missed fact is traced to a feature, or marked uncertain.
- [ ] Reduced forms belong to the stated variety.

## False-Positive Prevention

1. **Graded speech by stealth.** Drifting back to clean textbook sentences after two turns defeats the sim. Keep the fillers and reductions every turn.
2. **Invented reductions.** Writing a contraction that natives of this variety do not use. If unsure, use fewer and more standard reductions.
3. **Endless patience.** A partner who slows down every time teaches the learner to rely on it. Slow down once per fact, then rephrase.
4. **Rewarding "yes, yes".** A learner who agreed without understanding must not be scored as having caught the fact.
5. **Buried to impossible.** Hiding facts under three layers of self-correction at B1 is noise, not practice. Scale the density to level.
6. **Blaming the learner for a missing fact.** If a checklist fact was never actually said, the scene failed. Check the transcript.
7. **Comprehension as grammar.** The debrief is about what was understood and how the learner asked. Leave production errors out unless they blocked a clarification.

## Example Output

```
Settings: Spanish (Spain) | L1 English | B2 | Off | Colleague explains a change of plan | 5 facts

Partner: Oye, pues nada, que lo de mañana… bueno, que la reunión ya no es a las diez, eh, la han
pasado a las doce y media porque Marta — la de ventas, sabes — tiene médico, o sea que…
Learner: Vale.
Partner: …y otra cosa, que no es en la sala grande, es en la tres, la del fondo. Pa' que lo sepas.
Learner: Perdona, ¿la tres o la diez?
Partner: La tres, la tres. Al fondo del pasillo. Y trae el portátil, que vamos a ver lo del
presupuesto — bueno, no, el informe del trimestre, perdón.
Learner: ¿Qué?
Partner: Que traigas el portátil, que vamos a ver el informe del trimestre, no el presupuesto.
Learner: END

Debrief (4. Scenario focus)
Facts: 3 / 5 — clarification-assisted: 3 — missed: 1 — bluffed: 1
| Fact | Status | Where it was hidden |
| New time 12:30 | Bluffed ("Vale") | Mid-turn, after "bueno", next to the old time |
| Reason: Marta at the doctor | Missed | Aside inside dashes |
| Room 3 | Caught after clarification | — |
| Bring laptop | Caught after clarification | — |
| Quarterly report, not budget | Caught after clarification | Self-correction |
| Your requests | Rating | Better version |
| "¿La tres o la diez?" | Specific | — (excellent) |
| "¿Qué?" | Generic | "Perdona, ¿qué hay que traer?" |
| Reduced form | Full form |
| pa' | para |
5. Take away: "Perdona, ¿a qué hora dijiste?" Your "Vale" in turn 1 cost you the new time.
```

## Techniques Used

- **CM-01 (Explicit Context Framing):** the setting and the number of hidden facts are fixed up front.
- **ST-16 (Behavioral Trait Declarations):** the partner's native-speech features and realistic clarification behaviour are declared.
- **QA-11 (Pass/Fail Test Harness):** a hidden fact checklist with four statuses, including bluffed.
- **QA-04 (Uncertainty Acknowledgment):** misses are traced to a named feature, or marked uncertain.

## Related Prompts

- `domain-conversation-practice/conversation_lang_sim_master_template.md`: slots, correction modes and commands.
- `domain-education-teaching/learner/tutoring/learn_adaptive_input_output_loop.md`: graded input when native speed is too much.
- `domain-education-teaching/learner/language/learn_pronunciation_coach_text.md`: producing the connected-speech features you learned to hear.
