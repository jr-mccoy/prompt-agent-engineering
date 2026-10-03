---
title: "Biblical Studies Paper Self-Check — Review Your Own Draft as a Referee Would Before Submitting"
category: biblical-studies/academic-writing
description: "Review your own biblical-studies paper or chapter the way a seminar examiner or journal referee in the field would: score it on anchored scales for thesis, handling of the text and variants, original-language claims, context, engagement with the history of research and interpretation, fair treatment of alternative readings, and citation integrity; locate every finding to a page and paragraph; separate blocking from minor problems; and permit a clean pass where the draft earns one."
techniques:
  - DP-03
  - QA-01
  - QA-02
  - QA-05
  - QA-27
difficulty: advanced
tags:
  - self-review
  - peer-review
  - exegetical-fallacies
  - paper-revision
  - citation-check
  - academic-writing
  - check-my-paper-before-submitting
  - revise-seminary-paper
updated: "2026-10-03"
related_prompts:
  - domain-biblical-studies/theology-research/biblical_exegetical_fallacy_detector.md
  - domain-science/peer-review/science_peer_review_self_check.md
  - domain-biblical-studies/academic-writing/biblical_academic_exegesis_paper_scaffold.md
---

# Biblical Studies Paper Self-Check

**Objective:** Give the author of a biblical-studies paper a referee-style review of their own draft — anchored scores, located findings, blocking versus minor triage, and a revision order — so problems a field reader would catch (an unargued variant, a root-fallacy word study, an unattributed "consensus", a quotation with no page) are fixed before submission.

> **STRONG-GUARD prompt — the reviewer must not fabricate either.** The review checks the draft's claims; it does **not** supply corrections from memory. It never states what a lexicon, apparatus, commentary, or scholar actually says, so it never "corrects" a gloss, a manuscript reading, or an attribution with a counter-claim of its own. A finding says *what is unsupported or inconsistent and how to check it* — e.g. "confirm against the apparatus" — not "the correct reading is X". Every finding is located (section, paragraph, sentence) and quotes the draft's own words.

**When to use:**
- A seminar paper, exegesis paper, thesis chapter, or article draft in biblical studies is near final.
- Your instructor or supervisor flagged "method problems" and you want them named.
- You want to know which problems block submission and which are polish.

**When NOT to use:**
- You want one argument scanned specifically for word-study, grammatical, logical, and historical fallacies — use `domain-biblical-studies/theology-research/biblical_exegetical_fallacy_detector.md`; this prompt calls it for that dimension and covers the rest of the paper.
- You are checking a review you wrote of someone else's science manuscript — use `domain-science/peer-review/science_peer_review_self_check.md`; that prompt audits a referee report, this one audits your own humanities paper.
- You have not drafted yet — use `domain-biblical-studies/academic-writing/biblical_academic_exegesis_paper_scaffold.md`.
- You need every claim reconciled to a source set line by line — use `domain-research-academic/research_manuscript_fact_check_reconciler.md`.

**Audience:** Seminary and graduate students (A); pastors and scholars preparing articles (P, A).

---

## Inputs / Context

1. **The draft** (full text), with its bibliography.
2. **Assignment or venue requirements**: length, style guide and edition, required sections, rubric if any.
3. **Your thesis in one sentence** (to check against what the draft actually argues).
4. **Notes on sources** (optional): which you read in full, which you cite from secondary reports.
5. **Declared tradition of the venue (optional)**: a confessional venue may expect certain questions; the self-check still requires fair treatment of alternatives.

---

## Constraints

### Must
- Score on **anchored 1–5 scales** for: (1) thesis and argument, (2) text and variants, (3) translation and original-language claims, (4) historical and literary context, (5) engagement with history of research and interpretation, (6) treatment of alternative readings, (7) citation and quotation integrity, (8) style-guide conformity.
- **Locate** every finding with the draft's own words.
- Triage each finding: **blocking** (changes what the paper can claim) or **minor** (presentation only).
- Allow a **clean pass** on any dimension; "no finding" is a valid result when evidence supports it.
- Give a **revision order**: blocking findings first, in the order that unblocks the most.

### Must Not
- Supply a gloss, parsing, apparatus reading, scholar's position, or date as a correction.
- Manufacture findings to fill every dimension.
- Rewrite the paper.
- Penalise the paper's conclusion for its tradition; judge only how it is argued.

### Tradition-neutral stance (Must / Must Not)
- **Must:** check that the paper names the main alternative readings and attributes them before arguing against them.
- **Must Not:** mark a confessional or a critical conclusion down for being one.

---

## Instructions

### Step 1 — Thesis check
Compare the stated thesis with the conclusion actually reached. Mismatch is blocking.

### Step 2 — Dimension sweep with anchors
For each dimension use these anchors: **1** = absent or wrong in a way that undermines the thesis; **3** = present but with at least one unsupported step a field reader would query; **5** = complete, evidenced, located. Examples of what to look for: variant noticed but not argued (2); a meaning read from etymology or imported across languages without usage evidence (3); background facts with no source (4); "scholars agree" with fewer than three cited (5); an alternative reading named only to dismiss (6); quotations without page numbers, secondary citations presented as primary (7).

### Step 3 — Citation integrity sample
Sample every direct quotation and at least five other citations: does each have a page, is the source in the bibliography, did the author read it (or is it cited "as quoted in")? The self-check flags; it does not verify against the source.

### Step 4 — Fallacy pass
Run the word-study and argument claims through the fallacy categories (route detail to the fallacy-detector prompt).

### Step 5 — Triage and honesty valve
Classify each finding blocking or minor. For each dimension with no finding, write "no finding — basis: [what was checked]".

### Step 6 — Revision order
List blocking fixes in dependency order, then minor fixes, with an estimate of effort.

---

## Output Format

```
# Self-Check — [paper title] — [venue/assignment]

## Thesis vs. conclusion
## Scores
| Dimension | Score (1–5) | Basis |

## Findings
| # | Location | Draft's words | Problem | Check to run | Blocking/Minor |

## No-finding dimensions (with basis)
## Revision order
```

---

## Verification

- [ ] Every finding is located and quotes the draft.
- [ ] No correction supplied from memory; each finding names a check.
- [ ] Blocking vs. minor follows "changes what the paper can claim".
- [ ] At least the dimensions with no finding say what was checked.
- [ ] Alternative-reading treatment checked without judging the tradition of the conclusion.

---

## False-Positive Prevention

❌ **DON'T:**
- "Correct" the author's gloss with your own; you would be adding an unverified claim.
- Score every dimension 3 to look balanced; anchors decide.
- Treat a minor style-guide issue as blocking because it is easy to find.
- Call a well-argued confessional reading "biased".

✅ **DO:**
- Use the draft's own sentences as evidence for each finding.
- Pass dimensions cleanly when the anchors are met.

---

## Example Output

```
# Self-Check — "Peace with God: Romans 5:1–5 and the Grounds of Hope" — NT Exegesis II, 4,000 words

## Thesis vs. conclusion
Thesis (p.1): hope in 5:3–5 rests on the Spirit's gift, not on endurance. Conclusion (p.12) says
"endurance produces the hope that saves" — contradicts the thesis. BLOCKING.

## Scores
| Thesis & argument | 3 | thesis/conclusion mismatch |
| Text & variants | 2 | 5:1 variant mentioned in a footnote only |
| Translation & language claims | 2 | εἰρήνη paragraph imports meaning without usage evidence |
| Context | 4 | Roman setting used where a verse needs it; one unsourced claim |
| History of research/interpretation | 3 | modern commentators only; no reception before 1900 |
| Alternative readings | 4 | subjective/objective genitive in 5:5 both presented and attributed |
| Citation integrity | 2 | 3 of 7 quotations have no page |
| Style guide | 4 | footnote format consistent; abbreviations mixed |

## Findings
| 1 | p.12 ¶2 | "endurance produces the hope that saves" | contradicts thesis | revise conclusion or thesis | Blocking |
| 2 | p.3 n.4 | "Some manuscripts read 'let us have peace'" | variant affects the thesis (status vs. exhortation) but is not argued | write the text section from your apparatus work (textual-criticism primer) | Blocking |
| 3 | p.6 ¶1 | "εἰρήνη here carries the full Hebrew sense of šālôm" | transfer claim with no evidence from Paul's usage | support from usage or remove (fallacy detector: semantic transfer) | Blocking |
| 4 | p.8 ¶3 | "Scholars universally agree that 5:3–4 is a chain" | universal claim, one citation | cite the sources you read or soften | Minor |
| 5 | pp.5, 7, 9 | three block quotations | no page numbers | add pages from the copies you read | Blocking (integrity) |
| 6 | p.4 ¶2 | "Roman Christians faced daily persecution in the 50s" | historical claim, no source | source it or cut it | Minor |

## No-finding dimensions
Alternative readings (5:5 genitive) — basis: both readings stated, each attributed to sources
in the bibliography, argued against with reasons.

## Revision order
1 (thesis) → 2 (variant decides how 5:1 is framed) → 3 → 5 → 6 → 4. Est. 6–8 hours; finding 2
needs library time with the apparatus.
```

---

## Techniques Used

- **DP-03 (Anchored Scoring Scales):** Eight dimensions scored against stated 1/3/5 anchors.
- **QA-01 (Self-Verification):** The author's own draft is checked systematically before a reader sees it.
- **QA-02 (Adversarial Stress-Test):** The draft is read as a field referee would, hunting the claims a hostile reader would query.
- **QA-05 (Citation Requirements):** Quotations and citations are sampled for page, bibliography entry, and first-hand reading.
- **QA-27 (Pressure-minus-Counterweight Rule):** The demand to find problems is balanced by an explicit clean-pass valve and evidence for every finding.

## Related Prompts

- `domain-biblical-studies/theology-research/biblical_exegetical_fallacy_detector.md` — detailed fallacy scan for word-study and argument claims.
- `domain-science/peer-review/science_peer_review_self_check.md` — auditing a referee report you wrote, in the sciences.
- `domain-biblical-studies/academic-writing/biblical_academic_exegesis_paper_scaffold.md` — structure for the paper before drafting.
