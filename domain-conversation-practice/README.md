# Domain: Conversation Practice

**Purpose:** Rehearse a conversation against a model that plays the other
person realistically, then steps out of character to coach you. The conversation
can be a hard one in your own language or an everyday one in a language you are
learning.

> **Correction (2026-09-24).** Earlier versions of this README described
> language-learning simulations in seven languages, in `spanish/`, `french/`,
> `mandarin/` and other subfolders. Those folders never existed. Language
> conversation practice now lives here as a set of language-agnostic
> `conversation_lang_sim_*` prompts: one master template, where the target language
> is a slot, and five scenario sims. There are no per-language folders.

---

## What This Domain Covers

### Language conversation sims

Target-language role-play for adult learners. Every scenario sim plugs into the
master template, which owns the shared slots (target language and variety, CEFR
level, register) and the four **correction modes**: *recast* (fixed invisibly in
the partner's next line), *explicit* (one bracketed note per turn), *delayed*
(saved for the debrief) and *off* (fluency only).

| File | What it does |
|---|---|
| [`conversation_lang_sim_master_template.md`](conversation_lang_sim_master_template.md) | The base template: slots, CEFR calibration table, the four correction modes, commands (HINT / SLOWER / PAUSE / END), and a debrief that puts the task before form |
| [`conversation_lang_sim_cefr_can_do_scenarios.md`](conversation_lang_sim_cefr_can_do_scenarios.md) | Test 2–4 specific CEFR can-do descriptors: pass criteria fixed before the scene, then Pass / Not yet / Not elicited with quoted evidence |
| [`conversation_lang_sim_service_breakdown.md`](conversation_lang_sim_service_breakdown.md) | Lost luggage, wrong order, double charge: a polite partner scripted to misunderstand, offer the wrong fix and cite policy, so you practise repair |
| [`conversation_lang_sim_workplace_meeting.md`](conversation_lang_sim_workplace_meeting.md) | A multi-voice meeting, a phone call with no visual cues, or a job interview, scored on the professional functions each requires |
| [`conversation_lang_sim_register_shift.md`](conversation_lang_sim_register_shift.md) | The same goal played formal and then informal, with your two transcripts compared marker by marker |
| [`conversation_lang_sim_native_speed_listening.md`](conversation_lang_sim_native_speed_listening.md) | Fillers, reductions and buried facts; you must catch a hidden fact checklist and ask specific clarification questions instead of bluffing |

**How they compose:** start with the master template at your level. Use the CEFR
can-do check to find which functions are not yet secure, then rehearse them in the
scenario sims. Anything that needs *teaching* rather than rehearsal goes to
`domain-education-teaching/learner/` (see "Not here" below).

### Hard-conversation and persona sims

| File | What it does |
|---|---|
| [`conversation_practice_simulator.md`](conversation_practice_simulator.md) | A configurable framework for any hard conversation. The model plays the other party, escalates or de-escalates in response to what you say, and gives targeted coaching when you ask for it. |
| [`conversation_sim_master_template.md`](conversation_sim_master_template.md) | A two-phase template (role-play, then coaching debrief) with a slot for any persona. |
| [`conversation_sim_diane_principled_educator.md`](conversation_sim_diane_principled_educator.md) | Persona: an educator with principled objections to AI |
| [`conversation_sim_frank_privacy_hawk.md`](conversation_sim_frank_privacy_hawk.md) | Persona: an older relative focused on privacy |
| [`conversation_sim_jennifer_skeptical_insider.md`](conversation_sim_jennifer_skeptical_insider.md) | Persona: a skeptical industry insider |
| [`conversation_sim_marcus_displaced_worker.md`](conversation_sim_marcus_displaced_worker.md) | Persona: a worker worried about displacement |
| [`conversation_sim_maya_cynical_zoomer.md`](conversation_sim_maya_cynical_zoomer.md) | Persona: a cynical younger skeptic |
| [`conversation_sim_pastor_james_moral_traditionalist.md`](conversation_sim_pastor_james_moral_traditionalist.md) | Persona: a moral traditionalist |

The six personas share one scenario: a productive conversation about AI with a
skeptical relative or colleague. Use the persona master template to add personas for
other topics.

---

## When to Use This Domain

- You have a conversation coming up and want to rehearse it against realistic
  pushback, not a straw man.
- You want feedback on *how* you argued (listening, validation, pacing), not
  only on what you said.
- You are learning a language and want **role-play** in it: a partner who stays in
  role at your level, reacts to what you actually said, and corrects you only in the
  way you chose.

**Not here:**
- Negotiations and difficult workplace conversations (feedback, conflict,
  firing) → [`domain-negotiation/`](../domain-negotiation/), including
  `difficult-conversations/`.
- Interview practice as the candidate, for the *content* of your answers →
  `domain-personal-development/job-search/`. To rehearse delivering an interview
  in a target language, use `conversation_lang_sim_workplace_meeting.md` here.
- Media interviews → `domain-science/public-engagement/science_media_interview_prep.md`.
- Structured language **drills and instruction** stay in
  `domain-education-teaching/learner/language/` and `learner/tutoring/`: the
  cooperative daily drill (`learn_daily_conversation_drill.md`), grammar
  explanation, topical vocabulary, idiom decoding, text-based pronunciation
  coaching, and the adaptive input-output tutoring loop. Error-log remediation is
  `learner/self-assessment/learn_error_correction_cycle.md`. Language **role-play
  and scenario simulation** routes here.
- Teaching a language class → `domain-education-teaching/instructor/subject-pedagogy/world-languages/`.
- Designing a chatbot's conversation →
  [`domain-voice-conversational-ui/`](../domain-voice-conversational-ui/).
