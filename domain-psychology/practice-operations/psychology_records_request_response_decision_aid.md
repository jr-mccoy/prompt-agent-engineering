---
title: "Records-Request Response Decision Aid"
category: psychology/practice-operations
description: "Decide how to respond to a request for mental-health records — distinguishing a HIPAA patient-access request, a valid third-party authorization, a subpoena (not self-executing), and a court order — with the psychotherapy-notes carve-out, minor/guardian and 42 CFR Part 2 wrinkles, and what to release, withhold, or require first."
techniques:
  - RT-02
  - DT-01
  - DS-02
  - CM-02
  - QA-04
difficulty: advanced
intended_use: model-testing
tags:
  - records-request
  - HIPAA
  - subpoena
  - court-order
  - psychotherapy-notes
  - 42-CFR-Part-2
  - release-of-information
updated: "2026-06-08"
related_prompts:
  - domain-psychology/practice-operations/psychology_informed_consent_template_builder.md
  - domain-psychology/risk-crisis/psychology_tarasoff_duty_to_warn_analysis.md
  - domain-psychology/supervision-professional/psychology_scope_of_practice_decision_aid.md
  - domain-psychology/care-coordination/psychology_referral_letter_generator.md
---

# Records-Request Response Decision Aid

## Objective

Walk a clinician or records custodian through a structured response to a request for mental-health records, correctly classifying the request and applying the right rule before anything is released. The four pathways behave very differently: a **HIPAA patient-access request** (the client wants their own records), a **valid HIPAA authorization** (the client directs release to a third party), a **subpoena** (a litigation demand that is **not self-executing** and generally does **not** by itself authorize disclosure of protected health information), and a **court order** signed by a judge (which does compel disclosure within its terms). On top of these sit the **psychotherapy-notes carve-out** (specially protected under 45 CFR 164.508, with the access right limited under 45 CFR 164.524), **minor/guardian** complications, and **42 CFR Part 2** for federally-assisted substance-use-disorder records, which is stricter than HIPAA. The output is a determination of what to release, what to withhold, what must be obtained first, and the timeline.

## When to Use

- Any time the practice receives a request, demand, subpoena, or order for a client's records.
- A client asks for a copy of their own chart.
- An attorney, another provider, a school, a court, or an insurer requests records.
- A subpoena arrives and the practice must decide whether (and how) to respond without breaching confidentiality.
- A request implicates SUD treatment records or a minor's records.

## Inputs / Context Required

- **Who is requesting**: the client themselves, the client's attorney, an opposing attorney, another provider, a payer, a school, a court, or a government agency.
- **The instrument**: which document arrived — a signed authorization, a subpoena (party-issued vs. court-issued), a court order signed by a judge, or an informal letter/call.
- **What is requested**: the full record, specific dates, a summary, billing only, or specifically "therapy notes."
- **Client status**: adult with capacity / minor / client under guardianship / deceased client (estate).
- **Special record categories**: does the record include **psychotherapy notes** (separately kept process notes), **SUD treatment records** subject to **42 CFR Part 2**, HIV/genetic/other state-protected categories?
- **Authorization validity elements** (if an authorization is presented): description of information, who may disclose, who may receive, purpose, expiration, signature/date, right-to-revoke statement, and signer's authority.
- **Jurisdiction**: state law may grant clients/minors greater protections or different timelines than HIPAA. `[clinician input required: controlling state law on minor consent/access, records-access timeline, and any mental-health-specific release statute]`
- `[clinician input required: whether the practice/program is a 42 CFR Part 2 program (federally-assisted SUD treatment)]`

## Constraints

### Must

- **Classify the request first** into exactly one primary pathway: (1) HIPAA patient access, (2) valid third-party authorization, (3) subpoena, (4) court order — and note if more than one instrument is present.
- Treat a **subpoena as NOT self-executing**: a subpoena alone (especially attorney-issued) generally does not authorize disclosure of PHI without **either** the client's valid HIPAA authorization, **or** "satisfactory assurances" of notice/protective order under 45 CFR 164.512(e), **or** a court order. State this explicitly and do not release on a bare subpoena.
- Treat a **court order signed by a judge** as compelling disclosure **only within the scope the order specifies** (release exactly what is ordered, no more).
- Apply the **psychotherapy-notes carve-out**: psychotherapy notes (kept separate from the rest of the record) require a **specific, separate authorization** under 45 CFR 164.508 and are **not** included in a general release; the patient's right of access under 45 CFR 164.524 generally does **not** extend to psychotherapy notes.
- Apply **45 CFR 164.524 access rules** for patient-access requests: provide access, generally within **30 days** (with one 30-day extension), in the form/format requested if readily producible; permitted denials are narrow and some are reviewable.
- Apply **42 CFR Part 2** where applicable: SUD records from a Part 2 program require Part 2-compliant consent and are **not** disclosable on a subpoena alone — a **court order meeting Part 2 criteria** (or compliant consent) is required.
- Handle **minor/guardian**: identify who holds the legal right to access (parent/guardian vs. the minor for services the minor consented to under state law), and flag where state law diverges from HIPAA.
- State a clear disposition for each requested item: **RELEASE / WITHHOLD / OBTAIN-FIRST (and what)**, plus the **timeline**.
- Note the option to provide a **summary** where permitted and to **object/move to quash** an improper subpoena rather than ignore it.

### Must Not

- Do not release PHI on a bare subpoena without authorization, satisfactory assurances, or a court order.
- Do not include psychotherapy notes in a general authorization or a patient-access release; require a separate, specific authorization.
- Do not over-release on a court order — release only what the order specifies.
- Do not disclose 42 CFR Part 2 SUD records on a subpoena alone or on a general HIPAA authorization that is not Part 2-compliant.
- Do not assume a presented authorization is valid without checking the required elements and the signer's authority.
- Do not ignore a subpoena; respond (comply if proper, or object/move to quash) within its deadline.
- Do not fabricate state-law timelines or minor-consent rules; flag with `[clinician input required]`.

## Instructions

1. **Classify the instrument**: authorization / subpoena (party vs. court) / court order / informal request / patient-access request. Identify the requester and what is sought.
2. **Patient-access pathway (164.524)**: if the client requests their own record → provide access within ~30 days (one 30-day extension allowed), in requested format if feasible; psychotherapy notes are excluded from this access right; apply narrow permitted denials.
3. **Authorization pathway (164.508)**: if a third-party release is presented → verify all validity elements and signer authority; release only the scope authorized; require a **separate** psychotherapy-notes authorization if those notes are sought.
4. **Subpoena pathway (164.512(e))**: a subpoena is not self-executing. Release only if accompanied by the client's valid authorization, by satisfactory assurances (notice to the client or a qualified protective order), or by a court order. Otherwise object / move to quash — and still respond by the deadline.
5. **Court-order pathway**: a judge-signed order compels disclosure within its exact scope; release precisely what is ordered.
6. **Special-category overlays**: if SUD records from a Part 2 program → require Part 2-compliant consent or a Part 2-qualifying court order (subpoena alone insufficient). If psychotherapy notes → specific separate authorization. If state-protected categories → apply stricter rule.
7. **Minor/guardian/decedent overlay**: determine who holds the access right under state law; flag divergences from HIPAA.
8. **Per-item disposition**: for each requested item, mark RELEASE / WITHHOLD / OBTAIN-FIRST, and state the timeline and any client-notice step.
9. Run verification.

## Output Format

```
=== RECORDS-REQUEST RESPONSE DETERMINATION ===

REQUEST INTAKE
Requester: [Client / Client's attorney / Opposing attorney / Provider / Payer / School / Court / Agency]
Instrument received: [Authorization | Subpoena (party-issued | court-issued) | Court order (judge-signed) | Informal request | Patient-access request]
What is requested: [Full record / specific dates / summary / billing only / "therapy notes"]
Client status: [Adult w/ capacity | Minor | Under guardianship | Deceased/estate]
Special categories present: [Psychotherapy notes? | 42 CFR Part 2 SUD? | State-protected category?]

PATHWAY CLASSIFICATION → [1 Patient access | 2 Authorization | 3 Subpoena | 4 Court order]
(Note if multiple instruments present.)

RULE APPLICATION
HIPAA access (164.524): [applies? timeline ~30 days +30 extension; format; psychotherapy notes excluded]
Authorization (164.508): [valid? elements present? scope? separate psychotherapy-notes auth needed?]
Subpoena (164.512(e)): [NOT self-executing — authorization / satisfactory assurances / court order present? If none → object/quash]
Court order: [scope of what is compelled — release only this]
42 CFR Part 2: [Program? → Part 2-compliant consent or qualifying court order required; subpoena alone insufficient]
Minor/guardian/decedent: [who holds access right under state law]  [clinician input required: state rule]

PER-ITEM DISPOSITION
| Requested item | Disposition | Basis | Obtain-first / Notice step |
|----------------|-------------|-------|-----------------------------|
| Full progress notes | [RELEASE/WITHHOLD/OBTAIN-FIRST] | [164.508 scope] | [...] |
| Psychotherapy (process) notes | [WITHHOLD unless specific auth] | [164.508 carve-out] | [Separate authorization] |
| SUD treatment records | [OBTAIN-FIRST] | [42 CFR Part 2] | [Part 2 consent / qualifying court order] |
| Billing / dates of service | [RELEASE?] | [...] | [...] |

DETERMINATION & TIMELINE
What to release: [...]
What to withhold: [...]
What to obtain first: [authorization / Part 2 consent / court order / satisfactory assurances]
Action on a bare subpoena: [object / move to quash / respond by deadline]
Timeline / deadline: [access ~30 days | subpoena response by [date] | order compliance by [date]]
Client notification step (if required): [...]
```

## Verification

- [ ] Request classified into one primary pathway (patient access / authorization / subpoena / court order); multiple instruments noted.
- [ ] Subpoena treated as NOT self-executing — release only with authorization, satisfactory assurances (164.512(e)), or a court order; otherwise object/quash but still respond by deadline.
- [ ] Court order honored only within its specified scope (no over-release).
- [ ] Psychotherapy-notes carve-out applied (separate 164.508 authorization; excluded from 164.524 access).
- [ ] Patient-access rules applied: ~30-day timeline (+30-day extension), format, narrow permitted denials.
- [ ] 42 CFR Part 2 applied where the program is federally-assisted SUD treatment (subpoena alone insufficient).
- [ ] Authorization validity elements and signer authority checked before release.
- [ ] Minor/guardian/decedent access right resolved with state-law flag.
- [ ] Per-item disposition (RELEASE / WITHHOLD / OBTAIN-FIRST) with basis and timeline.
- [ ] Option to provide a summary and to object/move to quash an improper subpoena noted.
- [ ] No fabricated state timelines or minor-consent rules; flagged `[clinician input required]`.
```
