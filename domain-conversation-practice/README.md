# Domain: Conversation Practice

**Purpose:** Rehearse a hard conversation against a model that plays the other
person realistically, then steps out of character to coach you.

> **Correction (2026-09-24).** Earlier versions of this README described
> language-learning simulations in seven languages, in `spanish/`, `french/`,
> `mandarin/` and other subfolders. Those folders never existed. The domain
> actually holds a general role-play simulator and a set of skeptical-persona
> simulations. Language conversation practice is planned for coverage Wave 2 in
> [`meta/COVERAGE_ROADMAP.md`](../meta/COVERAGE_ROADMAP.md). Until then, use
> `domain-education-teaching/learner/language/`.

---

## What This Domain Covers

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
skeptical relative or colleague. Use the master template to add personas for
other topics.

---

## When to Use This Domain

- You have a conversation coming up and want to rehearse it against realistic
  pushback, not a straw man.
- You want feedback on *how* you argued (listening, validation, pacing), not
  only on what you said.

**Not here:**
- Negotiations and difficult workplace conversations (feedback, conflict,
  firing) → [`domain-negotiation/`](../domain-negotiation/), including
  `difficult-conversations/`.
- Interview practice as the candidate →
  `domain-personal-development/job-search/`.
- Media interviews → `domain-science/public-engagement/science_media_interview_prep.md`.
- Language learning → `domain-education-teaching/learner/language/`.
- Designing a chatbot's conversation →
  [`domain-voice-conversational-ui/`](../domain-voice-conversational-ui/).
