# Expansion Roadmap — `domain-childrens-writing/`

**Status:** Brainstorm only — no prompts in this roadmap have been authored yet. This is a prioritized menu for future additions, produced from a full-domain review (all 22 existing prompts + README re-read against the age-band table and stated conventions).

**How to use this doc:** Pick an item, confirm the age-band/word-count figures against the README's quick-reference table, then author it following the same structure every existing prompt in this domain uses (frontmatter → Purpose/When to use/Don't use when/Input needed → Your Input → Instructions → Output Format → Example Output → Quality Indicators + Common pitfalls → False-Positive Prevention → Related Prompts). See any existing file (e.g. `fiction-workshops/childrens_picture_book_workshop.md`) as the template.

---

## Tier 1 — Highest-value gaps (zero current coverage, clear recurring need)

### 1. Series bible & style-guide builder
- **Suggested location:** `fiction-workshops/childrens_series_bible_builder.md`
- **Gap:** Series publishing is central to early-reader, chapter-book, and MG markets, but the domain currently addresses it only as a single short "Series Engine" step buried inside `childrens_early_reader_chapter_book_workshop.md`.
- **What it would cover:** voice/style guide for consistency across books and (possibly) ghostwriters; format template (chapter count, word-count band, recurring structural beats); character/setting continuity tracker; the "renewable problem source" that keeps a series fresh; a house-style cheat sheet for anyone writing book 4+ of an established series.
- **Related existing prompts:** `childrens_early_reader_chapter_book_workshop.md`, `childrens_character_creation.md`.

### 2. Self-publishing business track
- **Suggested location:** `publishing-business/childrens_self_publishing_prep.md`
- **Gap:** `publishing-business/` is currently 100% traditional-agent-query oriented (query letter, synopsis, pitch/comps). Nothing addresses the self-publishing path, despite `childrens_illustrator_collaboration.md`'s production-norms table already acknowledging self-pub as a real production path.
- **What it would cover:** KDP/IngramSpark format specs by book type (trim size, page count in multiples of the printer's signature requirements, bleed), ISBN acquisition, copyright registration basics, print-file/PDF prep handoff to a designer, honest expectations-setting (no fabricated sales figures — inherits the domain's publishing anti-fabrication convention).
- **Related existing prompts:** `childrens_illustrator_collaboration.md`, `childrens_synopsis_submission_package.md` (as the traditional-path counterpart).

### 3. Wordless picture book workshop
- **Suggested location:** `fiction-workshops/childrens_wordless_picture_book_workshop.md`
- **Gap:** The domain's entire text/art model (art-note discipline, "don't write what the art will show") assumes text exists to divide labor with. A wordless book has no text layer at all, so it needs its own visual-sequencing logic rather than a variant of the existing picture-book prompt.
- **What it would cover:** page-by-page visual beat mapping (the "invisible script" a wordless book still needs), emotional/story legibility without words, page-turn logic driven entirely by image composition, how to brief this to an illustrator or plan it as an author-illustrator.
- **Related existing prompts:** `childrens_picture_book_workshop.md`, `childrens_illustrator_collaboration.md`.

---

## Tier 2 — Solid secondary candidates

### 4. Choose-your-own-adventure / branching narrative workshop
- **Suggested location:** `fiction-workshops/childrens_branching_narrative_workshop.md`
- **Gap:** No coverage of interactive/branching structure at all — a distinct craft discipline (node mapping, ensuring every branch resolves satisfyingly, avoiding dead-end or "gotcha" paths that punish young readers).

### 5. Phonics-controlled decodable-reader mechanics
- **Suggested location:** `craft-tools/childrens_decodable_text_mechanics.md`
- **Gap:** The early-reader prompt covers "controlled vocabulary" generally but doesn't dig into phonics scope-and-sequence (which letter/sound patterns are decodable at which stage) — a distinct, more mechanical discipline from general vocabulary control.

### 6. Audiobook / read-aloud production considerations
- **Suggested location:** `craft-tools/childrens_audiobook_production_considerations.md`
- **Gap:** Read-aloud *craft* (rhythm, meter) is thoroughly covered by `childrens_read_aloud_rhythm_rhyme_polish.md`, but audiobook *production* (narration pacing for audio-only consumption, sound-design opportunities in enhanced editions, how dialogue tags read when there's no page to look at) is a different, unaddressed concern.

### 7. Book trailer / marketing copy
- **Suggested location:** `publishing-business/childrens_book_marketing_copy.md`
- **Gap:** The business track stops at the submission stage; nothing addresses post-deal or self-pub marketing copy (jacket copy, trailer scripts, retailer descriptions) under the same anti-fabrication discipline (no invented reviews/blurbs/sales claims).

### 8. School visit / author-event prep
- **Suggested location:** `publishing-business/childrens_school_visit_prep.md`
- **Gap:** Not addressed anywhere — a common ask once an author has a published book, covering read-aloud excerpt selection, age-appropriate activity design, and Q&A prep.

---

## Tier 3 — Smaller, rounding-out candidates

### 9. Illustration brief for hire
- **Suggested location:** `representation-collaboration/childrens_illustration_brief_for_hire.md`
- **Gap:** `childrens_illustrator_collaboration.md` covers art-note discipline and the dummy-building process well, but there's no standalone brief/checklist template for a self-publishing author *hiring* an illustrator (scope, style references, revision rounds, licensing terms — distinct from the traditional-pub art-note guidance that assumes an in-house art director).

### 10. Informational picture books beyond STEM
- **Suggested location:** `nonfiction-workshops/childrens_informational_picture_book_workshop.md`
- **Gap:** `childrens_expository_stem_concept_workshop.md` is framed specifically around STEM/concept books. History, careers, and arts-focused informational picture books (distinct from the narrative-biography form in `childrens_narrative_nonfiction_workshop.md`) don't have a dedicated home.

### 11. Translations / international rights
- **Suggested location:** `publishing-business/childrens_translation_rights_considerations.md`
- **Gap:** Not addressed anywhere in the domain — relevant for authors fielding foreign-rights offers or considering how wordplay/rhyme/cultural references will (or won't) survive translation.

### 12. Grant / fellowship application prep for kidlit authors
- **Suggested location:** `publishing-business/childrens_grant_fellowship_application_prep.md`
- **Gap:** Not addressed — e.g. SCBWI grants, We Need Diverse Books grants, residencies. Would inherit the domain's publishing anti-fabrication convention (never invent a program's actual criteria, deadlines, or acceptance rates).

---

## Explicitly not gaps (already covered, or deliberately out of scope)

- **Board-book infant/toddler split** — already handled; `childrens_board_concept_book_workshop.md` has a Target Age field distinguishing 0-18mo from 18mo-3yr.
- **Picture-book rhyming text** — already covered jointly by `childrens_picture_book_workshop.md` (form) and `childrens_read_aloud_rhythm_rhyme_polish.md` (meter/rhyme craft); a dedicated "verse picture book" prompt would mostly duplicate the two.
- **Educational/curriculum tie-in books** — deliberately excluded. The README's stated domain boundary routes this to `domain-education-teaching/`.
- **Multicultural/own-voices sourcing** — the audit-level guardrail already exists in `childrens_writing_across_difference_audit.md` (stereotype/trope scan, sensitivity-reader routing). A dedicated "how to find and work with a cultural consultant" resource is plausible as a future add-on but is not a hard gap the way Tier 1/2 items are.

---

## Cross-cutting notes for whoever authors from this list

- Every new prompt should carry the domain's three extended conventions where relevant: **representation humility** (never certify cultural accuracy), **publishing anti-fabrication** (no invented comps/sales/agency rules — flag **VERIFY**), and the **age boundary** (board books 0-3 through upper-MG/young-teen 11-14; mature YA routes to `domain-creative-writing/`).
- When linking cross-domain (e.g. to `domain-creative-writing/` or `domain-education-teaching/`), double-check the relative path depth — this review found two existing cross-domain links in the domain that were one directory level short (fixed in the prior commit).
- Keep the `related_prompts` frontmatter field at 3 entries per the repo-wide convention; don't expand it to force reciprocal linking.
