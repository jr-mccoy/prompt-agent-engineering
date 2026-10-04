---
title: "Accessible Documents and Slides — Triage, Source-First Remediation, PDF Tagging, Reading Order, Alt Text, Contrast, and Captions for Published Files"
category: frontend-development/accessibility
description: "Audit and fix the PDFs, Word files, and slide decks an organisation publishes: triage the document estate by reach and obligation, fix at the authoring source rather than patching PDFs, check tags, reading order, alt text, tables, contrast, language and titles against WCAG-for-documents and PDF/UA, caption and transcribe embedded media, and confirm with a screen-reader read-through because checker passes are not proof."
techniques:
  - DS-32
  - QA-18
  - QA-24
  - DS-06
difficulty: intermediate
tags:
  - document-accessibility
  - pdf-ua
  - tagged-pdf
  - alt-text
  - reading-order
  - accessible-slides
  - captions
  - make-pdf-accessible
  - screen-reader-cant-read-our-report
  - accessible-powerpoint
updated: "2026-10-03"
related_prompts:
  - domain-frontend-development/accessibility/frontend_accessibility_wcag_audit.md
  - domain-frontend-development/accessibility/frontend_accessibility_screen_reader.md
  - domain-presentations/visual-planning/visualplan_visual_qa_harness.md
---

# Accessible Documents and Slides

**Objective:** Make the documents an organisation publishes — reports, forms, policies,
board and webinar decks, recorded talks — usable with screen readers, magnification, and
captions, by triaging what to fix, fixing it where it was authored, and verifying with
real assistive-technology checks rather than a checker's green tick.

**When to Use:**
- An organisation publishes PDFs or decks to the public, staff, students, or customers and
  has received a complaint, a procurement requirement, or a legal deadline.
- A flagship report is about to be exported from InDesign, Word, or PowerPoint.
- A backlog of hundreds of legacy PDFs needs a remediate / replace / archive decision.
- Recorded webinars or slide decks with embedded video are being posted.
- **Not this prompt if** the target is a **web application or site** — use
  `domain-frontend-development/accessibility/frontend_accessibility_wcag_audit.md`; if you
  need a detailed screen-reader test protocol for an interactive UI, use
  `domain-frontend-development/accessibility/frontend_accessibility_screen_reader.md`; if you
  are reviewing a single deck's visual quality (hierarchy, density, chart choice) with
  accessibility as one row, use
  `domain-presentations/visual-planning/visualplan_visual_qa_harness.md`. Setting the
  organisation's policy, conformance reporting, and procurement rules is
  `frontend_accessibility_program_governance.md`.

## Inputs / Context

1. **Document estate**: counts by type (PDF, DOCX, PPTX, video), source application, owner,
   audience, traffic or download counts, and age.
2. **Obligations**: jurisdiction and sector (e.g. Section 508, ADA, EN 301 549 clause 10,
   European Accessibility Act, AODA), and the target (normally WCAG 2.1/2.2 AA applied to
   documents per W3C's WCAG2ICT guidance; PDF/UA for PDFs).
3. **Authoring sources** available: are the original .indd/.docx/.pptx files kept?
4. **Tools at hand**: Office Accessibility Checker, Acrobat Pro, PAC (PDF Accessibility
   Checker), veraPDF, a screen reader (NVDA/JAWS/VoiceOver), caption tooling.
5. **Sample documents** to audit in depth (3–5 representative files).

## Method

1. **Triage the estate (DS-06).** Score each document group by reach (downloads,
   audience size), obligation (legally required, procurement-required, internal), and
   currency (in use vs archived). Decide per group: *remediate*, *replace with an
   accessible web page* (often cheaper for long-lived content), *archive* with a clear
   "accessible version on request" route, or *retire*. Confirm archive exceptions with
   counsel; they are jurisdiction-specific.
2. **Enumerate the applicable requirements (DS-32).** Map each obligation to concrete
   checks so findings cite a criterion, not an opinion.
3. **Fix at the source.** Headings from real styles, lists from list tools, tables built as
   tables with a header row, alt text and document language set in the authoring file,
   slide content in layout placeholders. Export with tagging enabled. Patching tags in a
   PDF is the last resort: it is lost on the next re-export.
4. **Check each sample document.**
   - Title and language set; title shown in the window bar.
   - Tag tree present; heading levels nested without skips; lists and tables tagged; table
     header cells marked; decorative content marked as artifact.
   - Reading order (tag order) matches the logical order, including sidebars, footnotes,
     multi-column layouts; slide object order matches intended reading.
   - Alt text: informative images described for their purpose; decorative ones marked;
     charts carry a short alt plus the data or key finding in text or a table.
   - Contrast: text ≥4.5:1 (≥3:1 for large text); chart lines, bars, and form-field
     borders ≥3:1 against adjacent colours; colour never the only carrier of meaning.
   - Links describe their destination; form fields have labels and tab order.
   - Slides: unique slide titles; no text baked into images; speaker notes do not
     substitute for on-slide content.
   - Media: synchronized captions for prerecorded audio (WCAG 1.2.2), audio description
     or a descriptive transcript where visuals carry information (1.2.5), transcript posted.
5. **Apply domain smell tests (QA-18).** A checker pass with wrong reading order; alt text
   that is the file name; "Figure 1" as the only chart description; scanned image PDFs with
   no OCR text layer; auto-generated captions published unedited.
6. **Verify with assistive technology.** Read each sample end to end with a screen reader;
   navigate by headings; tab through forms; check reflow/zoom at 200%. Record what was
   checked and passed (QA-24) so clean results are distinguishable from untested ones.
7. **Fix the pipeline, not only the files.** Accessible templates, export settings, an
   authoring checklist for content owners, and a pre-publication gate for high-reach files.

## Output Format

```
# Document accessibility — [organisation / collection]   Target: [WCAG x.x AA, PDF/UA]

## Estate triage
| Group | Count | Reach | Obligation | Decision (remediate/replace/archive/retire) |
## Requirements map
| Obligation | Applies to | Concrete checks |
## Sample findings
| Doc | Check | Criterion | Finding | Fix at source | Severity |
## Checked and passed
| Doc | Check | Method (checker / SR read / manual) |
## Media
| Item | Captions | Audio description / transcript | Status |
## Pipeline fixes
templates · export settings · author checklist · pre-publication gate
## Confidence and limits
```

## Verification

- [ ] Every group in the estate has a decision; archive decisions name the request route.
- [ ] Every finding cites a criterion and a fix in the authoring source.
- [ ] Reading order was checked by tag order or screen reader, not by eye on the page.
- [ ] Contrast ratios are computed for text and chart elements, with values stated.
- [ ] Charts have text equivalents beyond a title.
- [ ] Captions were reviewed by a person, not only auto-generated.
- [ ] At least one full screen-reader read-through per sample is recorded.

## False-Positive Prevention

1. **Checker pass as conformance.** Automated checkers cannot judge alt-text quality or
   logical reading order; a clean report on a mis-ordered document is still a failure.
2. **"Tagged" as accessible.** Auto-tagging a scanned or complex layout often produces a
   tag tree in the wrong order or with every line as a paragraph.
3. **Alt text for everything.** Describing decorative rules and logos at every page adds
   noise; mark them as artifacts.
4. **Remediating what should be replaced.** A 200-page report revised quarterly may be
   cheaper and better as HTML than as a re-remediated PDF each quarter.
5. **Speaker notes as access.** Notes are not exposed to audiences of an exported deck in
   most viewers; content must be on the slide or in the alt text.
6. **Auto-captions as captions.** Unedited automatic captions misrender names and terms;
   publishing them unreviewed does not meet the intent of 1.2.2.
7. **Legal conclusions.** Which documents an exception covers is a legal question; flag it.

## Example Output

```
# Document accessibility — County Public Health Dept. publications   Target: WCAG 2.1 AA, PDF/UA-1

## Estate triage
| Annual & data reports (PDF from InDesign) | 38 | 9,400 downloads/yr | public, required | remediate 2025–26 at source; replace data tables with HTML |
| Board meeting decks (PPTX → PDF) | 210 | low; FOIA-requested | required | new template now; legacy archived, on request in 5 business days |
| Forms (PDF fillable) | 22 | high | required | rebuild 6 highest-volume as web forms; remediate 16 |
| Recorded webinars | 14 | 3,100 views | required | caption review + transcripts |
| Pre-2019 scanned notices | 460 | ~0 | archived | archive notice + request route (counsel to confirm) |

## Sample findings — 2025 Annual Report (64 pp)
| Reading order | 1.3.2 | sidebars read mid-sentence on 11 pages | anchor sidebars after body text in InDesign Articles panel | High |
| Headings | 1.3.1 | all headings tagged <P>; no structure | map paragraph styles to H1–H3 in export tags | High |
| Alt text | 1.1.1 | 23 charts with alt "Chart" | 1-sentence finding + linked data table per chart | High |
| Contrast | 1.4.3 | caption grey #8a8a8a on white = 3.45:1 | darken to #595959 (7.0:1) in caption style | Medium |
| Non-text contrast | 1.4.11 | light-blue series #7fb3d5 on white = 2.26:1 | #2e6f9e (5.41:1) + direct labels | Medium |
| Use of colour | 1.4.1 | map legend by colour only | add pattern fills and labels | Medium |
| Callout box | 1.4.3 | white text on amber #f4a300 = 2.08:1 | near-black text #1a1a1a (8.36:1) | Medium |

## Checked and passed
| Annual Report | language (en-US), title, bookmarks | PAC + Acrobat properties |
| Board deck template | slide titles unique; reading order | PowerPoint Reading Order pane + NVDA |

## Media
| 14 webinars | auto-captions only | transcripts missing; slides have charts | review captions (est. 1.5 h per hour of video); add descriptive transcript |

## Pipeline fixes
Accessible InDesign and PowerPoint templates with mapped styles; export preset with tags;
one-page author checklist; pre-publication gate (PAC + 10-minute NVDA skim) for anything
linked from the home page.

## Confidence and limits
High for the 3 audited samples; Medium for extrapolation to the remaining 35 reports.
Archive exception for scanned notices is a legal call — flagged to counsel.
```

## Techniques Used

- **DS-32 Regulatory Enumeration Pattern** — obligations mapped to concrete document checks.
- **QA-18 Domain-Specific Smell Tests** — the known ways document accessibility looks done but is not.
- **QA-24 Dismissed-Candidates Coverage Table** — checked-and-passed items recorded with method.
- **DS-06 Prioritization and Severity Guidance** — estate triage by reach, obligation, and currency.

## Related Prompts

- `frontend_accessibility_wcag_audit.md` — conformance audit for web pages and apps rather than files.
- `frontend_accessibility_screen_reader.md` — detailed assistive-technology testing method.
- `domain-presentations/visual-planning/visualplan_visual_qa_harness.md` — visual QA of a single deck, where accessibility is one dimension.
