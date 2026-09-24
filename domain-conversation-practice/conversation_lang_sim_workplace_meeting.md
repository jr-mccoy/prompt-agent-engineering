---
title: "Language Sim — Workplace Meeting, Phone Call, and Job Interview in the Target Language"
category: conversation-practice
description: "Three professional scenes run in the target language: a multi-party meeting where the model voices two or three named colleagues and the learner must take the floor, disagree politely and restate an action item; a phone call with no visual cues where names, numbers and dates must be spelled and confirmed; and a job interview asked at the learner's level. Each is scored on the professional language functions it requires. Distinct from the one-to-one social scenes in learn_daily_conversation_drill.md and from jobsearch_behavioral_interview_story_bank.md, which prepares what you say, not the language you say it in."
techniques:
  - OC-08
  - RP-03
  - CM-01
  - QA-01
difficulty: advanced
tags:
  - language-learning
  - business-language
  - role-play
  - meetings
  - job-interview
  - speaking-practice
  - working-abroad
  - second-language-job
  - speaking-up
updated: "2026-09-24"
related_prompts:
  - domain-conversation-practice/conversation_lang_sim_master_template.md
  - domain-education-teaching/learner/language/learn_daily_conversation_drill.md
  - domain-personal-development/job-search/jobsearch_behavioral_interview_story_bank.md
---

# Language Sim — Workplace Meeting, Phone Call, Job Interview

**Objective:** Rehearse the three professional situations where working in a second language is hardest: holding your own among several native speakers, understanding and being understood with no face to read, and presenting yourself under evaluation. The learner picks a **mode**. The sim scores the professional language functions that mode requires, not general fluency.

**When to Use:**
- You work in, or are moving into, a job conducted in your target language.
- You understand meetings but never manage to speak in them.
- You have a phone call or interview coming up in the target language.

**Not this prompt if… / distinct from**
- You want everyday social or service scenes one-to-one. Use `domain-education-teaching/learner/language/learn_daily_conversation_drill.md`. Its phone-call option is a simple cooperative service call, not a professional call with details to confirm.
- You need to decide *what* to say in an interview: your stories and evidence. Use `domain-personal-development/job-search/jobsearch_behavioral_interview_story_bank.md` first, in any language, then rehearse the delivery here.
- You need help with a difficult workplace conversation itself, such as feedback or conflict. Use `domain-negotiation/`.

## Inputs

Fill the master template slots (`conversation_lang_sim_master_template.md`). The defaults for this sim are register **formal**, or the workplace's real norm if you state it, and correction mode **delayed**. Then choose a mode (OC-08) and give the details:

| Mode | Details needed | Functions scored |
|---|---|---|
| **Meeting** | Topic, your role, 2–3 colleague roles, one decision to be made | Taking the floor; polite disagreement; building on others; asking for clarification; summarising an action item |
| **Phone call** | Who calls whom, purpose, 3–4 details to exchange (names, numbers, dates) | Opening and identifying yourself; spelling and reading numbers; confirming details back; handling "sorry, the line…"; closing |
| **Job interview** | Role, seniority, 3 points you want to land | Describing past experience (past tenses); explaining motivation; handling an unexpected question; asking the interviewer a question |

## Mode rules

**Meeting (RP-03).** The model voices 2–3 named colleagues with distinct stances: one pushes a proposal, one is skeptical, and one is quiet until asked. Colleagues talk to *each other* as well as to the learner. They sometimes overlap, and they do not pause to invite the learner in. The learner must break in. If the learner stays silent for three turns, a colleague asks them directly. Each colleague's lines are labelled with their name.

**Phone call.** There is no body language, so the partner may say "sorry, you're breaking up" once. The partner reads a number or name quickly once and expects it read back. At least one detail must be spelled. The partner closes only once details have been confirmed, or it hangs up with the details still unconfirmed, which the debrief notes.

**Job interview.** The interviewer is professional and neutral, and asks 5–6 questions at the learner's level. At least one requires past tense narration, and one is unexpected ("What would your last manager say you should improve?"). The interviewer does not react warmly to every answer and uses neutral acknowledgements. They end by inviting the learner's own question.

## The prompt block (paste into the master template's `[SCENARIO BLOCK]`)

```
SCENARIO MODE: [meeting | phone call | job interview]
Details: [from the Inputs table]
Follow the mode rules:
- Meeting: voice [names/roles], label each line with the speaker's name, let colleagues talk
  to each other, do not wait for me; if I am silent 3 turns, someone asks me directly.
- Phone: no visual cues; read [detail] fast once and expect me to confirm it; at least
  one item must be spelled; close only after details are confirmed.
- Interview: 5–6 questions at my level; one past-tense narrative, one unexpected question;
  neutral acknowledgements; end by inviting my question.
DEBRIEF SCORING FOCUS: for each function in my mode's list, observed / partly / missing,
with my quoted line and one more professional alternative in [TARGET_LANGUAGE].
```

## Method

1. **Confirm settings and mode (CM-01)** in L1. For a meeting, introduce the colleagues by name and role before starting.
2. **Run the scene** under the mode rules and the master template's in-scene rules.
3. **Debrief (QA-01)** with the master template's five headings. Heading 4 is the function table for the chosen mode. For meetings, also report the **share of turns**: how many times the learner spoke against the colleagues' total.

## Output Format

In scene: labelled partner lines. Debrief heading 4:

```
| Function | Observed / partly / missing | Your line (quoted) | More professional alternative |
[Meeting only] Your turns: n of N total
```

## Verification

- [ ] The mode's rules were applied: several named voices, no-visual-cue handling, or neutral interview questions.
- [ ] Every function in the mode's list was either elicited or reported as not elicited.
- [ ] The alternatives are in the target language and in the stated register.
- [ ] In a meeting, the learner had to break in rather than being invited every turn.
- [ ] In a phone call, at least one detail was spelled and read back, or its absence is noted.

## False-Positive Prevention

1. **A polite meeting.** Colleagues who stop and invite the learner every turn remove the hardest skill, taking the floor.
2. **Colleague soup.** Colleagues without distinct stances or name labels make the meeting unreadable. Give each one a position.
3. **Warm interviewer.** "Great answer!" after every reply is not what real interviews sound like, and it inflates confidence.
4. **Content coaching.** Judging whether the interview *story* was strong belongs to the job-search prompt. Score the language functions.
5. **Wrong register norm.** Some workplaces use first names and informal address even in formal meetings (Swedish *du*, many German start-ups). Follow the stated norm rather than assuming formality.
6. **Unconfirmed details passing silently.** Wrapping up a phone call without the read-back is the failure that matters most at work.

## Example Output

```
Settings: French (France) | L1 English | B2 | professional, team uses tu (stated norm) | Delayed | Meeting
Topic: moving the product launch from March to April. You: product analyst.
Colleagues: Claire (PM, wants to move it), Hugo (sales, skeptical), Amina (engineering, quiet)

Claire: Bon, je propose qu'on décale le lancement à avril, les tests ne sont pas finis.
Hugo: Avril ? On a déjà promis mars à trois clients, Claire.
Claire: Je sais, mais si on lance avec des bugs…
Learner: Si je peux me permettre — les données montrent que…
Hugo: Oui, mais les clients s'en fichent des données.
Learner: Je comprends, mais justement, on pourrait proposer mars pour ces trois clients seulement ?
Amina: Techniquement, c'est faisable.
Claire: Ok. Tu peux résumer, [Learner] ?
Learner: Donc, lancement général en avril, et pilote en mars pour les trois clients. Hugo les prévient.
Learner: END

Debrief (4. Scenario focus)
| Function | Status | Your line | More professional alternative |
| Taking the floor | Observed | "Si je peux me permettre —" | — (good) |
| Polite disagreement | Observed | "Je comprends, mais justement…" | — |
| Building on others | Partly | (used Amina's point implicitly) | "Comme le dit Amina, c'est faisable, donc…" |
| Asking for clarification | Missing | — | "Quand tu dis « promis », c'était contractuel ?" |
| Summarising action item | Observed | "Donc, lancement général en avril…" | Add an owner and date: "Hugo les prévient d'ici vendredi ?" |
Your turns: 3 of 9 total
```

## Techniques Used

- **OC-08 (Multi-Mode Prompt Architecture):** three professional modes, each with its own rules and function list.
- **RP-03 (Multi-Persona Debate):** named colleagues with distinct stances in meeting mode.
- **CM-01 (Explicit Context Framing):** mode, participants and details are confirmed before the scene.
- **QA-01 (Self-Verification):** a function-by-function debrief with quoted evidence.

## Related Prompts

- `domain-conversation-practice/conversation_lang_sim_master_template.md`: slots, correction modes and commands.
- `domain-education-teaching/learner/language/learn_daily_conversation_drill.md`: everyday one-to-one scenes.
- `domain-personal-development/job-search/jobsearch_behavioral_interview_story_bank.md`: build the interview content before rehearsing its delivery.
