---
title: "Appellate Statement of Facts Builder — Record-Grounded and Fairly Framed"
category: legal/appellate
description: "Build the statement of the case and statement of facts for an appellate brief in which every sentence cites the record (RA/JA/ER/CT/RT or the court's designation), disputed facts are presented neutrally and in the light the standard of review requires, and persuasion comes from selection and order rather than argument or adjectives."
techniques:
  - ST-02
  - ST-03
  - IPC-07
  - QA-05
  - QA-01
difficulty: advanced
tags:
  - legal
  - appellate
  - statement-of-facts
  - record-citation
  - brief-writing
  - joint-appendix
  - telling-the-story
updated: "2026-09-24"
related_prompts:
  - domain-legal/appellate/legal_issue_selection_memo.md
  - domain-legal/appellate/legal_oral_argument_prep.md
  - domain-legal/litigation/legal_trial_theme_and_narrative_designer.md
  - domain-legal/depositions/legal_deposition_summary.md
---

**Objective:** Draft a statement of the case and statement of facts that an appellate panel can trust: every factual sentence is cited to the record using the court's citation form, disputed facts are attributed rather than asserted, the facts are framed consistently with the governing standard of review, and the narrative sets up the selected issues without arguing them.

> **Scope guard — attorney-facing only.** For licensed appellate counsel (or counsel for a prospective amicus). If the person running it appears to be an unrepresented party, stop and route them to `domain-legal/personal-self-advocacy/cross-cutting/legalprep_professional_authority_router.md` (appellate pro bono programs, law-school appellate clinics, legal aid) rather than producing strategy. This guard is not a disclaimer; the ban on "consult an attorney" boilerplate below still applies.

**When to Use:** After issue selection and assembly of the record or appendix; when converting a trial-level fact section into an appellate one; when the opposing brief's facts need a responsive counter-statement (appellee posture); before a record-citation audit.

**Distinct from:**
- `domain-legal/litigation/legal_trial_theme_and_narrative_designer.md` — builds a persuasive jury narrative from evidence expected at trial; this prompt builds a court-facing narrative confined to a closed record.
- `domain-legal/litigation/legal_motion_for_summary_judgment.md` — undisputed-facts statement at the trial level; appellate facts follow the appellate standard of review and record rules.
- `domain-legal/depositions/legal_deposition_summary.md` — summarizes one transcript; this prompt synthesizes the whole record.

---

## Your Input

- **Appellate court and jurisdiction:** [Required]
- **Record citation form:** [e.g., "JA 123", "ER 45", "1 CT 210", "RT 88:4" — per court rules; required]
- **Posture and standard(s) of review:** [Appellant/appellee; e.g., post-verdict, summary judgment, bench findings — standards as verified by the user]
- **Selected issues:** [From the issue-selection memo]
- **Record excerpts:** [Transcript passages, exhibits, orders — with record cites]
- **Procedural history:** [Filings, rulings, judgment, notice of appeal — with record cites]
- **Opposing brief's facts (if responding):** [Text]
- **Word budget for facts:** [As supplied]

---

## Constraints

**Must:**
- Cite **every** factual sentence to the record in the court's form; a sentence without a cite is flagged `[NEED RECORD CITE]`.
- Attribute contested facts to their source ("Officer Lee testified that ..." / "Ms. Diaz testified she did not ...") rather than stating them as established.
- Frame facts consistently with the standard of review the user supplies (e.g., where the verdict-winner's evidence must be credited, do not present the losing side's version as fact) and flag the framing choice in a drafting note.
- Include unfavorable facts the court will need; omitting them costs credibility and invites the other side to supply them.
- Order the narrative to set up the issues (chronological by default; topical where it serves clarity) with short headings.
- Keep the procedural history accurate to the docket: motion, ruling, date, record cite.
- Produce a **cite audit table** listing each fact and its record support.

**Must Not:**
- Argue, characterize, or use adjectives that assert conclusions ("egregious," "clearly," "admitted" when the witness did not admit).
- Cite facts outside the record, or cite the opposing brief or a trial-court brief as evidence of a fact.
- Paraphrase testimony in a way that changes meaning; quote when precision matters.
- Invent record cites, page:line references, exhibit numbers, or the court's citation rules.
- Add "consult an attorney" boilerplate.

---

## Method

1. **Record map.** Index supplied excerpts by topic and record cite.
2. **Fact inventory.** For each selected issue, list facts the court must know, favorable and unfavorable, each with a cite; mark disputed facts.
3. **Framing decision.** Apply the standard of review to disputed facts; write a one-line drafting note on how each disputed fact is presented.
4. **Outline.** Statement of the case (procedural path) → facts with headings in the order that sets up the issues.
5. **Draft.** Short declarative sentences; attribution for disputed facts; quotations for key testimony.
6. **Cite audit.** Table every sentence to its record cite; flag unsupported sentences; check that quotations match the excerpt verbatim.
7. **Tone scrub.** Remove argument words; move any inference to the argument section list.

---

## Output Format

```markdown
# STATEMENT OF THE CASE
{Nature of the case; course of proceedings; disposition below — each sentence cited.}

# STATEMENT OF FACTS
## A. {Heading}
{Facts with record cites, e.g., (JA 212).}
## B. {Heading}
{...}

---
# DRAFTING NOTES (internal)
| Disputed fact | Sources | How presented | SoR basis [VERIFY] |

# CITE AUDIT (internal)
| ¶/sentence | Fact | Record cite | Verbatim quote check | Status |

# MOVED TO ARGUMENT (internal)
- {Inferences or characterizations removed from the facts}
```

---

## Worked Example (abbreviated)

**Input:** Criminal appeal, defendant-appellant; issues: sufficiency of evidence of intent and denial of a suppression motion. Record form "JA ___". User notes sufficiency review credits the government's evidence `[verified authority supplied]`; suppression findings of fact reviewed deferentially. Excerpts: officer's testimony, defendant's testimony, the suppression order.

**Output excerpt:**
- Statement of the case: "A grand jury indicted Mr. Ortiz on one count of ... (JA 14). The district court denied his motion to suppress after a hearing (JA 88–97). A jury convicted (JA 402), and the court sentenced him to ... (JA 455). This appeal followed (JA 460)."
- Facts, suppression hearing: "The district court found that Officer Grant saw the bag on the passenger seat before opening the door (JA 94). Officer Grant testified the interior light was on (JA 61:3–9); Mr. Ortiz testified it was off (JA 77:12–18)." — findings stated as findings, contrary testimony attributed.
- Drafting note: the government's version of intent evidence is presented first and attributed, consistent with the supplied sufficiency standard; the defense's gaps are stated as absences in the record ("No witness testified that ..." with the cite to the witness list, JA 3–5).
- Moved to argument: "The officer's account is implausible."

---

## Verification

- [ ] Court and record citation form locked to the user's input.
- [ ] Every factual sentence has a record cite; unsupported sentences flagged.
- [ ] Disputed facts attributed; framing matches the supplied standard of review.
- [ ] Key unfavorable facts included.
- [ ] Quotations verified verbatim against excerpts.
- [ ] No argument words or conclusory adjectives in the facts.
- [ ] Procedural history matches the docket with cites.

---

## False-Positive Prevention

| Failure mode | Correction |
|---|---|
| Uncited sentences that "everyone knows" | Every sentence cited or flagged `[NEED RECORD CITE]` |
| Stating a contested version as fact | Attribute to the witness or to the trial court's finding |
| Ignoring the standard of review in framing | Drafting note ties each disputed fact to the supplied standard |
| Omitting bad facts | Include them in neutral terms; the other side will supply them less kindly |
| Adjectives doing argumentative work | Tone scrub; move inferences to the argument list |
| Citing a trial brief as proof of a fact | Cite testimony, exhibits, or findings — not advocacy documents |
| Paraphrase that shifts meaning ("admitted" for "did not recall") | Quote the testimony when words matter |
| Guessing page:line cites | Use only supplied cites; otherwise flag |
