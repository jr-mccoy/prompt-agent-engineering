# Narrative and Delivery

Prompts for the parts of a presentation that are not slides: the argument a pitch or talk makes, the questions it will face, and the rehearsal that gets it delivered on time. The root `powerpoint_*` prompts generate decks; these prompts decide what the deck should say and prepare the person presenting it.

Files use the repo-standard `presentation_` prefix and carry full Tier-1 frontmatter.

## When to Use This Cluster

- You are raising money and the deck lists facts without making an argument.
- You have a conference or keynote slot and a topic, but not yet a talk.
- A Q&A, town hall, or board question period is the part you are dreading.
- The deck is done and you need to deliver it without reading and without overrunning.

## Prompts

| # | Prompt | Use When |
|---|--------|----------|
| 1 | [`presentation_investor_pitch_narrative.md`](presentation_investor_pitch_narrative.md) | Build the narrative spine of a pre-seed to Series A fundraising deck: thesis, evidence-ranked slide order, claim-plus-proof headlines, objections, milestone-tied ask. |
| 2 | [`presentation_keynote_talk_arc.md`](presentation_keynote_talk_arc.md) | Turn a topic and time slot into a talk: one disputable idea, an audience belief shift, a chosen structure, and a minute budget at speaking pace. |
| 3 | [`presentation_qa_hostile_question_prep.md`](presentation_qa_hostile_question_prep.md) | Map the room, build a scored question bank including hostile and loaded questions, draft honest answers, set red lines, and rehearse the hardest questions. |
| 4 | [`presentation_speaker_notes_rehearsal_coach.md`](presentation_speaker_notes_rehearsal_coach.md) | Write cue-based speaker notes and run four scored rehearsal passes with a stop rule and a day-of card. |

## How They Compose

Pitch narrative or talk arc → Q&A prep (the objection table from the pitch feeds the question bank) → speaker notes and rehearsal → deck production with a root `powerpoint_*` generator or the `ppt-creator` skill.

## Cross-References

- Deck generation: [`../powerpoint_enterprise_deck_architect.md`](../powerpoint_enterprise_deck_architect.md), [`../powerpoint_financial_storyteller.md`](../powerpoint_financial_storyteller.md)
- Market-sizing visual for pitches: [`../board-decks/boarddeck_tam_sam_som.md`](../board-decks/boarddeck_tam_sam_som.md)
- Sales decks (buyers, not investors): [`../../domain-agentic-resources/skills/marketing/sales-enablement/SKILL.md`](../../domain-agentic-resources/skills/marketing/sales-enablement/SKILL.md)
- Media interviews and testimony: [`../../domain-science/public-engagement/`](../../domain-science/public-engagement/)
- Classroom slide decks: [`../../domain-education-teaching/instructor/ed-tech/teaching_class_slide_deck_designer.md`](../../domain-education-teaching/instructor/ed-tech/teaching_class_slide_deck_designer.md)
