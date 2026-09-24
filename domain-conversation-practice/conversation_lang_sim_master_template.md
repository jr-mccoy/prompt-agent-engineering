---
title: "Language Conversation Sim — Master Template With CEFR, Register, and Four Correction Modes"
category: conversation-practice
description: "The base template every language conversation sim in this domain plugs into: slots for target language and variety, CEFR level (with calibration rules for speech rate, sentence length and L1 fallback), register, scenario and partner, plus the four correction modes this domain owns (recast, explicit, delayed, off), each with its own in-scene and debrief rules; distinct from conversation_sim_master_template.md (English persuasion role-play with AI skeptics) and from learn_daily_conversation_drill.md (one fixed explicit-feedback style with a cooperative partner)."
techniques:
  - OC-08
  - CM-01
  - RP-02
  - AG-04
  - QA-01
difficulty: intermediate
tags:
  - language-learning
  - role-play
  - CEFR
  - corrective-feedback
  - speaking-practice
  - simulation
  - practice-talking
  - correct-my-mistakes
  - foreign-language-chat
updated: "2026-09-24"
related_prompts:
  - domain-conversation-practice/conversation_sim_master_template.md
  - domain-education-teaching/learner/language/learn_daily_conversation_drill.md
  - domain-education-teaching/learner/tutoring/learn_adaptive_input_output_loop.md
---

# Language Conversation Sim — Master Template

**Objective:** Give every target-language role-play in this domain one shared frame: the same slots, the same CEFR calibration and the same commands, plus a choice of four **correction modes**. The learner decides whether errors are recast inside the conversation, flagged after each turn, saved for the debrief, or ignored entirely. The scenario sims (`conversation_lang_sim_*`) supply only a scenario block and scoring focus, and inherit everything else from here.

**When to Use:**
- You want a target-language conversation with a partner who stays in role, at your level, in the register the situation needs.
- You want to choose *how* you are corrected. For example, recasts for flow, or no correction at all when you are rehearsing for confidence.
- You are building a new scenario sim for this domain. Copy the prompt block and replace only `[SCENARIO BLOCK]`.

**Not this prompt if… / distinct from**
- You want to practise persuading a skeptical relative about AI, in English. Use `conversation_sim_master_template.md`. Its debrief scores persuasion frames, not language.
- You want a quick cooperative drill with a fixed one-or-two-corrections-per-turn format. Use `domain-education-teaching/learner/language/learn_daily_conversation_drill.md`.
- You want to be *taught*: graded input, error recycling, transfer tasks. Use `domain-education-teaching/learner/tutoring/learn_adaptive_input_output_loop.md`.
- You want grammar explained, vocabulary built or pronunciation coached. Use `learn_l2_grammar_explainer.md`, `learn_topical_vocabulary_builder.md` or `learn_pronunciation_coach_text.md` in `domain-education-teaching/learner/language/`. This template does not drill.

## Inputs (the slots)

| Slot | Values | Default if blank |
|---|---|---|
| `TARGET_LANGUAGE` + variety | e.g. Spanish (Mexico), French (Québec), Japanese | Ask. Never assume. |
| `CEFR_LEVEL` | A1, A2, B1, B2, C1, C2 (self-assessed is fine) | B1, stated as assumed |
| `REGISTER` | formal / neutral / informal, and the address form (tú/usted, du/Sie, tu/vous, です・ます/plain) | Whatever the scenario implies, stated |
| `CORRECTION_MODE` | recast / explicit / delayed / off | delayed |
| `SCENARIO BLOCK` | partner role, partner goal, setting, what the learner must achieve | From the scenario sim |
| `L1` | the learner's first language | Ask |
| `TURNS` | number of exchanges | 10 |

## Calibration by level (RP-02)

| Level | Partner's sentences | Vocabulary | Speed and features | L1 fallback |
|---|---|---|---|---|
| A1–A2 | Short and simple, one idea each | High-frequency, concrete | Slow, no idioms, repeats key words | One L1 gloss, then back to the target language |
| B1 | Some subordinate clauses | Everyday plus scenario-specific | Natural, occasional common idiom | Only if the learner is stuck twice |
| B2 | Complex; opinions, hypotheticals | Wide, some abstract | Natural speed, fillers present | None; paraphrase in the target language instead |
| C1–C2 | Unrestricted | Idiomatic, register-rich | Native speed, implicature | None |

## The four correction modes (OC-08)

| Mode | During the scene | In the debrief |
|---|---|---|
| **Recast** | The partner reuses the learner's erroneous form, corrected, naturally in their next line ("¿Fuiste al mercado? Ah, *fuiste* ayer…"). No flag, no pause. At most one recast per turn. | Lists each recast so the learner can see what was fixed without their noticing |
| **Explicit** | After the partner's in-role line, one bracketed note: `[✎ "yo sabo" → "yo sé"]`. At most one per turn, highest-impact first. | Groups the notes into patterns |
| **Delayed** | Nothing during the scene. The partner may show *realistic* confusion if meaning broke down. | Up to 3 error patterns, each with the learner's quoted line and the correct form |
| **Off** | Nothing. Pure fluency. | Only communication breakdowns (where meaning failed), no form errors |

## The prompt block (paste this)

```
You are my conversation partner for target-language practice. Follow these rules exactly.

SETTINGS
Language/variety: [TARGET_LANGUAGE]  | My L1: [L1]
Level: [CEFR_LEVEL]  → calibrate your language to the level table I give you
Register: [REGISTER] (address form: [tú/usted etc.])
Correction mode: [recast | explicit | delayed | off]
Turns: [TURNS]

[SCENARIO BLOCK — partner role, partner goal, setting, what I must achieve,
 any scripted complications]

IN-SCENE RULES
- Stay in role and in [TARGET_LANGUAGE]. Do not narrate or explain.
- Keep each turn short enough for me to answer (1–3 sentences at A1–B1, up to 5 above).
- Apply ONLY the correction behaviour of my chosen mode.
- Never write my line for me. If I type HINT, give one word or a sentence starter in the target language.
- If I write in [L1], answer in role in the target language, more simply.
- React to what I actually said, including misunderstanding me if a real listener would.

COMMANDS
HINT = one word or sentence starter | SLOWER = simplify one level | PAUSE = step out, answer
my question in [L1], then resume | END = stop and debrief

DEBRIEF (on END or after [TURNS] turns), in [L1]:
1. Task: did I achieve the scenario goal? Yes / partly / no, with the moment it was won or lost.
2. Communication: where meaning broke down, quoted.
3. Form: according to my correction mode's debrief rule (max 3 patterns).
4. Scenario focus: [scoring focus from the scenario sim].
5. One thing to practise next, and which prompt to use for it.
```

## Method (for the model running the sim)

1. **Confirm settings (CM-01).** Restate the slots in the learner's L1, name any defaults applied, and name the correction mode in one line.
2. **Open in role** at the calibrated level, in the stated register.
3. **Hold the guardrails (AG-04)** every turn: stay in role, apply only the chosen mode's behaviour, make no hidden corrections in *off* mode, and keep to the stated register unless the scenario scripts a change.
4. **Debrief (QA-01)** in the order above, quoting the learner's lines. The task comes before form. A learner who got the refund with three article errors succeeded.

## Output Format

- **In scene:** partner lines only, in the target language. Add the explicit-mode bracket if the mode is *explicit*.
- **Debrief:** the five headings from the prompt block, in L1, quoting the learner.

## Verification

- [ ] Every slot is filled or defaulted out loud before the first in-role line.
- [ ] The partner's language matches the level-table row.
- [ ] Only the chosen correction mode's behaviour appears, with no recasts in *off* and no brackets in *delayed*.
- [ ] Register and address form never drift unless the scenario scripts it.
- [ ] The debrief puts task achievement before form, and quotes real lines.
- [ ] At most 3 form patterns, plus one practice recommendation.

## False-Positive Prevention

1. **Mode leakage.** A "delayed" partner who slips in a correction, or an "off" partner who recasts. That breaks the learner's chosen trade-off.
2. **Over-correction.** Flagging every error buries the one that matters. Keep to one per turn in-scene and three patterns in the debrief.
3. **Invented errors.** Marking a correct regional form (voseo, Québec *tu-questions*, Kansai forms) as wrong. Judge against the stated variety.
4. **Level drift upward.** Native-speed paragraphs to an A2 learner. Re-check the level table every turn.
5. **Cooperative collapse.** The partner guessing the learner's meaning so generously that an unclear utterance "works". Real listeners misunderstand.
6. **Form-first debrief.** Leading with grammar when the learner completed the task teaches that errors matter more than communication.
7. **Scope creep.** Turning the debrief into a grammar lesson or pronunciation drill. Recommend the education-teaching prompt instead.

## Example Output

```
Settings: Spanish (Mexico) | L1 English | B1 | usted | Recast | 6 turns
Scenario: pharmacy counter. You need something for a cough; the pharmacist asks follow-up questions.

Partner: Buenas tardes. ¿En qué le puedo ayudar?
Learner: Hola, necesito algo para mi tos. Tengo tos por tres días.
Partner: Ah, tiene tos *desde hace* tres días. ¿Es tos seca o con flemas?   ← recast
…
Learner: END

Debrief
1. Task: yes. You got a syrup and the dosage, and turn 4 ("¿Cuántas veces al día?") secured it.
2. Communication: turn 3, "flemas" was not understood; you asked "¿Perdón?", which worked.
3. Form (recasts I made): "por tres días" → "desde hace tres días" (turn 1); "tomo" → "tomé" (turn 5).
4. Scenario focus: you held "usted" throughout.
5. Next: "desde hace" + duration. Use learn_l2_grammar_explainer.md, then rerun with Explicit mode.
```

## Techniques Used

- **OC-08 (Multi-Mode Prompt Architecture):** the four correction modes are selectable behaviours with distinct in-scene and debrief rules.
- **CM-01 (Explicit Context Framing):** the slots and settings are confirmed before the scene.
- **RP-02 (Audience-Specific Framing):** the CEFR level table calibrates the partner's language.
- **AG-04 (Behavioral Guardrails):** in-role, mode and register rules hold every turn.
- **QA-01 (Self-Verification):** a fixed debrief order with quoted evidence.

## Related Prompts

- `domain-conversation-practice/conversation_sim_master_template.md`: the persona-sim template this one parallels.
- `domain-education-teaching/learner/language/learn_daily_conversation_drill.md`: a cooperative quick drill.
- `domain-education-teaching/learner/tutoring/learn_adaptive_input_output_loop.md`: tutoring with graded input and error recycling.
- Scenario sims built on this template: `conversation_lang_sim_cefr_can_do_scenarios.md`, `conversation_lang_sim_service_breakdown.md`, `conversation_lang_sim_workplace_meeting.md`, `conversation_lang_sim_register_shift.md`, `conversation_lang_sim_native_speed_listening.md`.
