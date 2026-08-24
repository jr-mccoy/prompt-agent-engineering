# Referenced Prompts — stage → domain-prompt routing

The Children's Book Studio **references** the existing 22 prompts in [`domain-childrens-writing/`](../../domain-childrens-writing/) rather than vendoring copies. This index maps each pipeline stage to the domain prompt(s) it routes to. All paths are relative to the repo root.

If a path here ever fails to resolve, the studio's routing is stale — fix it here and in the stage prompt.

## Stage → domain prompt

### Stage 0 — Project setup
- Routing/age-band reference: `domain-childrens-writing/README.md`

### Stage 1 — Concept foundation
- Protagonist + agency: `domain-childrens-writing/craft-tools/childrens_character_creation.md`
- Form workshop (premise/foundation) — one of the Stage-2/3 workshops below, per form.

### Stage 2 — Structure & beat map · Stage 3 — Draft generation
The form's workshop prompt supplies both the structure framework and the drafting mode:

| Form | Workshop prompt |
|------|-----------------|
| Board / concept (0-3) | `domain-childrens-writing/fiction-workshops/childrens_board_concept_book_workshop.md` |
| Picture book (2-8) | `domain-childrens-writing/fiction-workshops/childrens_picture_book_workshop.md` |
| Early reader / chapter (5-10) | `domain-childrens-writing/fiction-workshops/childrens_early_reader_chapter_book_workshop.md` |
| Middle grade (8-12) | `domain-childrens-writing/fiction-workshops/childrens_middle_grade_fiction_workshop.md` |
| Upper-MG / crossover (11-14) | `domain-childrens-writing/fiction-workshops/childrens_ya_crossover_workshop.md` |
| Verse novel (8-12) | `domain-childrens-writing/fiction-workshops/childrens_verse_novel_workshop.md` |
| Graphic novel (6-12) | `domain-childrens-writing/fiction-workshops/childrens_graphic_novel_comics_workshop.md` |
| Narrative nonfiction | `domain-childrens-writing/nonfiction-workshops/childrens_narrative_nonfiction_workshop.md` |
| Expository / STEM | `domain-childrens-writing/nonfiction-workshops/childrens_expository_stem_concept_workshop.md` |

### Stage 4 — Revision triage (route by diagnosis; prune by form)
- Layered diagnosis (always first): `domain-childrens-writing/craft-tools/childrens_revision_self_edit_pass.md`
- Opening hook: `domain-childrens-writing/craft-tools/childrens_opening_pages_hook.md`
- Kid dialogue: `domain-childrens-writing/craft-tools/childrens_kid_dialogue_workshop.md`
- Character: `domain-childrens-writing/craft-tools/childrens_character_creation.md`
- Reading-level calibration: `domain-childrens-writing/craft-tools/childrens_age_reading_level_calibrator.md`
- Sensitive topics: `domain-childrens-writing/craft-tools/childrens_sensitive_topics_framing.md`
- Writing across difference (audit; output stays flags-only): `domain-childrens-writing/representation-collaboration/childrens_writing_across_difference_audit.md`

### Stage 5 — Format polish & accuracy (route by form path)
- Illustrator collaboration / dummy (PB, GN): `domain-childrens-writing/representation-collaboration/childrens_illustrator_collaboration.md`
- Read-aloud rhythm & rhyme (verse / rhyming): `domain-childrens-writing/craft-tools/childrens_read_aloud_rhythm_rhyme_polish.md`
- Accessible & inclusive design (illustrated/print): `domain-childrens-writing/representation-collaboration/childrens_accessible_inclusive_design.md`
- Nonfiction accuracy + back matter: the matching `domain-childrens-writing/nonfiction-workshops/` prompt

### Stage 6 — Publishing package (run in order)
1. `domain-childrens-writing/publishing-business/childrens_pitch_comps_market_positioning.md`
2. `domain-childrens-writing/publishing-business/childrens_query_letter_kidlit.md`
3. `domain-childrens-writing/publishing-business/childrens_synopsis_submission_package.md`
