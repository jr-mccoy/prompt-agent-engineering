# `domain-science/writing-communication/`

The dissemination layer: turning verified results into manuscripts, abstracts, figures, tables, posters, preprints, lay summaries, and the editorial correspondence that gets a paper through review. Composes on top of [`../methods-foundations/`](../methods-foundations/) (the methods section, reporting standards) and [`../statistics/`](../statistics/) (what the numbers do and don't support).

**Load-bearing convention for this directory:** these prompts **draft only from user-supplied results**. They never invent data, p-values, citations, journal metrics, decision times, editor identities, or reviewer text. Every missing fact is `[user-supplied]` or "verify on the venue/journal site." Inflation vocabulary ("novel," "groundbreaking," "first-ever," "unprecedented") is banned from drafted output and replaced with specific, falsifiable claims.

## Map (Phase 2E — 14 prompts)

### Manuscript core

| File | Coverage |
|---|---|
| [`science_imrad_paper_drafter.md`](science_imrad_paper_drafter.md) | Skeleton-first IMRaD draft from supplied results; structural critique pass; EQUATOR-guideline content check |
| [`science_figure_first_paper_skeleton.md`](science_figure_first_paper_skeleton.md) | Figure-first outlining: lock the figure→claim sequence, then derive Results and Discussion |
| [`science_abstract_compressor.md`](science_abstract_compressor.md) | Structured/unstructured abstract to a word limit; primary result foregrounded, exploratory labeled |
| [`science_lay_summary_translator.md`](science_lay_summary_translator.md) | Plain-language summary for a stated audience; preserves scope/uncertainty; "what this does NOT mean" guard |

### Figures & tables

| File | Coverage |
|---|---|
| [`science_figure_legend_drafter.md`](science_figure_legend_drafter.md) | Self-contained legend: n, error-bar meaning, test, scale bar, replicate type — all stated |
| [`science_figure_design_critique.md`](science_figure_design_critique.md) | Color-blind safety, data-ink/chart-junk, encoding honesty (axis truncation, bar-of-mean), accessibility |
| [`science_table_design_critique.md`](science_table_design_critique.md) | Significant-figure discipline, units, missingness convention, footnote economy |

### Venue selection & editorial correspondence

| File | Coverage |
|---|---|
| [`science_journal_target_selector.md`](science_journal_target_selector.md) | Scope/audience/OA/decision-speed decision matrix; Think-Check-Submit predatory screen (DORA-aware) |
| [`science_cover_letter_to_editor.md`](science_cover_letter_to_editor.md) | One-page cover letter: scope fit, significance without hype, declarations, suggested editors/reviewers |
| [`science_response_to_reviewers.md`](science_response_to_reviewers.md) | Point-by-point response classifying each reply acceded / argued / partial, with a change log |
| [`science_appeal_to_editor_after_rejection.md`](science_appeal_to_editor_after_rejection.md) | Warranted-vs-not gate first, then a measured COPE-aligned appeal draft |

### Conference & open dissemination

| File | Coverage |
|---|---|
| [`science_conference_abstract_drafter.md`](science_conference_abstract_drafter.md) | Portal-aware oral/poster/lightning abstract to the submission limit |
| [`science_poster_designer.md`](science_poster_designer.md) | Three-zone scan-path poster content+layout spec; hands rendering off to `domain-image-generation/` |
| [`science_preprint_release_plan.md`](science_preprint_release_plan.md) | Server selection, CC-license choice, journal-policy verification, versioning, availability statement |

## Floor (per [`../README.md`](../README.md))

Every prompt requires discipline + finding context + target venue/audience; forbids fabrication of results, citations, and venue facts (`[user-supplied]` / "verify on the site"); locks the output format; names the relevant convention (IMRaD, the matching EQUATOR guideline, COPE, ICMJE, DORA, Creative Commons); preserves the confirmatory-vs-exploratory distinction in any claim it drafts; defaults to the Open Science branch (preprint + data/code availability); and ends with a verification checklist + false-positive matrix.

See [`../EXPANSION_ROADMAP.md`](../EXPANSION_ROADMAP.md) for the remaining phases and build order.
