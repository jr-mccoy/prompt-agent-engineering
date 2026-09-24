---
title: "Title Commitment Review — Requirements, Exceptions, Endorsement Strategy and Cure Plan"
category: legal/real-estate
description: "Review a title insurance commitment for a real estate acquisition or financing: check Schedule A against the deal, sort every Schedule B-I requirement by who must satisfy it and by when, classify every Schedule B-II exception (standard, survey-dependent, recorded instrument, lien, lease, unrecorded matter) against the recorded documents and survey, decide object / accept / insure-over, map endorsements to the risks that remain, and produce a dated title objection letter and cure plan. Attorney work product; distinct from the PSA redline that sets the objection mechanics and from a non-legal buyer's inspection triage."
techniques:
  - ST-02
  - RT-05
  - DS-06
  - OC-03
  - QA-01
difficulty: advanced
tags:
  - legal
  - real-estate
  - title-insurance
  - title-commitment
  - schedule-b
  - endorsements
  - survey
  - due-diligence
updated: "2026-09-24"
reasoning:
  styles: [analytic, classificatory, evidential]
  stakes: high
  horizon: days
  uncertainty: ambiguity
  evidence_quality: rich
  domain_complexity: regulated
  collaboration: small_team
  output_format: [structured, matrix]
  user_role: [attorney, paralegal, title_examiner]
  mode: [audit, diagnose, draft]
related_prompts:
  - domain-legal/real-estate/legal_purchase_agreement_redline.md
  - domain-legal/real-estate/legal_easement_drafter.md
  - domain-legal/corporate-ma/legal_due_diligence_findings_memo.md
  - domain-specialized-fields/real-estate/realestate_inspection_report_triage.md
---

## Objective

Turn a title commitment, its exception documents and the survey into (1) a
line-by-line review table, (2) a title objection letter that meets the PSA's objection
deadline, and (3) an endorsement request and cure plan showing what will and will not
be insured at closing.

## When to Use

- A title commitment (and ideally the survey and copies of every exception document)
  has arrived during an acquisition or loan closing.
- A pro forma policy has been issued and you are checking it against the agreed cure.
- A lender's counsel has sent title requirements and you represent the borrower.

**Distinct from:**
- `domain-legal/real-estate/legal_purchase_agreement_redline.md` — drafts the PSA's
  objection, cure and new-matter *mechanics*; this prompt *uses* them.
- `domain-specialized-fields/real-estate/realestate_inspection_report_triage.md` — a
  buyer's triage of physical defects; no title or record-document analysis.
- `domain-legal/corporate-ma/legal_due_diligence_findings_memo.md` — entity-level
  diligence findings; use it to roll title findings into a wider deal memo.

## Your Input

- **Jurisdiction (required):** state and county of the property. Commitment forms,
  promulgated endorsements, and insurability practice differ by state; some states use
  their own promulgated forms and schedule labels `[VERIFY: form family in use]`.
- **Posture:** Buyer / Borrower / Lender / Seller.
- **Commitment** (all schedules), **exception documents**, **survey** (with its
  certification and table items, if an ALTA/NSPS-style survey), **vesting deed**,
  and the **PSA** objection clause and deadline.
- **Intended use of the property** and any planned development — this drives which
  exceptions matter.
- **Lender requirements**, if financed.

## Constraints

**Must:**
- Check Schedule A (effective date, proposed insured, amount, estate, vesting, legal
  description) against the PSA, the vesting deed and the survey.
- Classify every Schedule B-II exception and state, for each: what it is, whether the
  document was reviewed, whether the survey plots it, whether it affects the intended
  use, and the recommended action (object / accept / insure over / endorse / clarify).
- Sort every B-I requirement by responsible party (seller, buyer, lender, title
  company) and by deadline, and flag any that the buyer cannot satisfy alone.
- Compute the objection deadline from the PSA and state it as a calendar date,
  showing the calculation; mark it `[VERIFY]` if the trigger date is not confirmed.
- Tie each endorsement request to a specific residual risk.

**Must Not:**
- Characterise an exception document you have not seen. If only the recording
  reference is given, the finding is "document not reviewed — obtain copy".
- Invent recording references, endorsement form numbers, statutes, or state
  insurability rules. Use `[VERIFY: …]` / `[CITE: …]`.
- Treat "standard exceptions" as harmless by default; say what it takes to delete them
  (owner's affidavit, survey, gap indemnity) `[VERIFY: underwriter practice]`.
- Offer a title opinion; this is a review of an insurer's offer to insure.

## Method

1. **Schedule A match.** Compare each field against the deal documents. Any vesting or
   legal-description mismatch is Critical until explained.
2. **Legal description reconciliation.** Compare commitment, vesting deed and survey
   descriptions; note closure, acreage and any gaps, gores or overlaps the surveyor
   reports.
3. **B-I requirements.** For each: what must be recorded, paid, delivered or signed;
   by whom; supporting document; whether it is within the client's control. Flag
   entity-authority requirements (good-standing, resolutions) and payoff letters early.
4. **B-II exceptions — classify.** Standard/general; taxes and assessments;
   recorded easements and restrictions; mortgages and liens; leases and rights of
   parties in possession; survey matters; mineral/water reservations; unrecorded or
   "subject to" matters.
5. **B-II exceptions — analyse.** Read each document. Record purpose, burdened and
   benefitted area, whether plotted, whether it conflicts with current or intended
   improvements, maintenance or cost-sharing obligations, and any reversion, forfeiture
   or right-of-first-refusal.
6. **Decide the action.** Object (seller must cure — especially monetary liens),
   accept (benign and acknowledged), insure over or endorse (residual risk transferable
   to the insurer), clarify (exception too vague — ask for it to be limited to its
   recorded terms or a specific location).
7. **Endorsement map.** For each residual risk choose the endorsement type by function
   (access, contiguity, survey accuracy, zoning, restrictions/encroachments, tax
   parcel, subdivision, utility access, environmental lien), marking form and
   availability `[VERIFY: state and underwriter]`.
8. **Objection letter and cure plan.** Draft the letter, dated within the deadline,
   listing objections with the specific cure requested. Build the cure plan with owner,
   deadline and fallback if seller elects not to cure.

## Output Format

```markdown
# Title Commitment Review — [Property], [County, State]
**Commitment No.:** [#] · **Effective date:** [date] · **Posture:** [ ]
**PSA objection deadline:** [date] ([calculation])

## Schedule A check
| Field | Commitment | Deal documents | Match? | Action |
|---|---|---|---|---|

## Schedule B-I requirements
| # | Requirement | Responsible | Deadline | Within client control? | Status |
|---|---|---|---|---|---|

## Schedule B-II exceptions
| # | Exception | Type | Doc reviewed? | Plotted? | Affects intended use? | Action | Endorsement |
|---|---|---|---|---|---|---|---|

## Endorsement requests
| Endorsement (function) | Residual risk addressed | Form / availability |
|---|---|---|

## Title objection letter
[Letterhead / date / PSA section / numbered objections / cure requested / reservation of new-matter rights]

## Cure plan
| Objection | Cure | Owner | Deadline | If not cured |
|---|---|---|---|---|
```

## Worked Example

**Input (abridged):** Buyer posture; 4.1-acre parcel acquired for a drive-through
restaurant; PSA gives 15 days from the later of receipt of commitment and survey;
commitment received 3 June, survey received 10 June.

**Deadline:** later of 3 June and 10 June = 10 June; + 15 days = **25 June**
`[VERIFY: PSA day-count convention and whether weekends extend]`.

| # | Exception | Type | Doc reviewed? | Plotted? | Affects use? | Action | Endorsement |
|---|---|---|---|---|---|---|---|
| 5 | Easement to [utility] per instrument at [recording ref] | Recorded easement | Yes | Yes — 20-ft strip along east line | **Yes** — survey shows it under planned drive-through lane | Clarify location; seek partial release or relocation from holder; else redesign | Survey-accuracy endorsement for location |
| 7 | Declaration of restrictions at [recording ref] | Restriction | Yes | N/A | **Yes** — prohibits "restaurants with drive-up windows" | **Object** — use-killing; seller cure = recorded amendment or release by required parties | Restrictions endorsement insufficient: a prohibition of the intended use is not an insurable "violation" risk |
| 9 | Rights of parties in possession | Standard | N/A | N/A | Possible — billboard lease visible on survey | Object; require delivery of billboard lease and estoppel, or termination | — |
| 11 | "Any easements not of record" | Standard | N/A | N/A | Unknown | Delete on owner's affidavit + survey `[VERIFY: underwriter practice]` | — |

**Objection letter excerpt:** "Objection 2 (Exception 7): the Declaration prohibits
the Property's use for a restaurant with a drive-up window. Buyer requires, as a
condition of closing, a recorded amendment or release executed by all parties whose
consent the Declaration requires `[VERIFY: amendment threshold in Declaration §__]`."

## Verification

- [ ] Every Schedule A field checked; any vesting or description mismatch is flagged.
- [ ] Every B-I requirement has an owner and deadline.
- [ ] Every B-II exception is classified, and each has a reviewed/not-reviewed status.
- [ ] Every exception affecting the intended use has an action other than "accept".
- [ ] Each endorsement is tied to a named residual risk; forms marked `[VERIFY]`.
- [ ] Objection deadline computed and shown; letter dated before it.
- [ ] No recording reference, endorsement number, statute or insurability rule is
      stated that the user did not supply or that is not marked `[VERIFY]`/`[CITE]`.

## False-Positive Prevention

| Failure mode | Correction |
|---|---|
| Summarising an exception from its one-line description | The commitment's caption is not the document; state "not reviewed" until the copy is read |
| Accepting exceptions because "they're standard" | Standard exceptions hide possession, survey and unrecorded rights; say what deletes each |
| Treating an endorsement as a cure for a use prohibition | Endorsements insure against loss from specified matters; they do not make a prohibited use permitted |
| Ignoring the survey | Many exceptions only matter once plotted against improvements; cross-check every plottable exception |
| Missing the objection deadline mechanics | Compute the date from the PSA trigger and show the arithmetic; flag unconfirmed trigger dates |
| Treating monetary liens like other objections | Seller-created monetary liens are usually mandatory cure in the PSA; confirm and list them for payoff |
| Asserting form numbers or state practice from memory | Promulgated forms and underwriter practice vary by state; mark `[VERIFY]` |

## Related

- `domain-legal/real-estate/legal_purchase_agreement_redline.md` — objection, cure and new-matter mechanics
- `domain-legal/real-estate/legal_easement_drafter.md` — drafting a relocation, partial release or new access easement to cure
- `domain-legal/real-estate/legal_zoning_use_analysis.md` — when a restriction or easement interacts with permitted use
- `domain-legal/corporate-ma/legal_due_diligence_findings_memo.md` — rolling title findings into a deal-level memo
