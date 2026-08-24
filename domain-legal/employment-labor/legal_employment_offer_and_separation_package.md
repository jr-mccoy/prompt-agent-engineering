---
title: "Employment Offer and Separation Package Drafter"
category: legal/employment-labor
description: "Draft a coordinated employment package — offer letter, IP/confidentiality agreement, restrictive covenants, and separation/release — calibrated to the controlling state and the employee's role, with at-will language, state-mandated IP carve-outs, ADEA/OWBPA windows, and §409A coordination."
techniques:
  - ST-01
  - ST-02
  - ST-03
  - CM-02
  - DS-02
  - QA-01
difficulty: advanced
tags:
  - legal
  - employment
  - offer-letter
  - separation
  - release
  - restrictive-covenants
updated: "2026-05-11"
related_prompts:
  - domain-legal/employment-labor/legal_non_compete_enforceability_analysis.md
  - domain-legal/employment-labor/legal_pip_and_termination_risk_review.md
  - domain-legal/contracts-transactional/legal_contract_clause_redline_targeted.md
  - domain-legal/research/legal_jurisdiction_split_analysis.md
---

**Purpose:** Produce a coordinated employment-lifecycle document set — offer letter (or amendment) plus separation agreement with general release — that is internally consistent on at-will status, IP ownership, restrictive covenants, compensation, and post-employment obligations, and is calibrated to the controlling state's mandatory rules.

**When to use:** Onboarding a new hire (executive or rank-and-file), amending material terms (promotion, equity grant, relocation), or negotiating an exit (RIF, performance-based separation, voluntary departure). Use for a single coordinated package so the offer-side and exit-side documents do not contradict each other.

---

## Your Input

- **Jurisdiction:** [Employee's primary work state — controls IP carve-outs, non-compete enforceability, release rules; plus any federal contractor status]
- **Federal coverage:** [Title VII / ADEA / ADA / FMLA / ERISA applicability based on employer size and benefits]
- **Industry:** [Tech, financial services, healthcare, manufacturing, etc. — regulatory overlays]
- **Role:** [Title, level, exempt/non-exempt status, executive or rank-and-file]
- **Posture:** [Onboarding / mid-employment amendment / negotiated separation / involuntary RIF / for-cause termination]
- **Compensation structure:** [Base, bonus, commission, equity grant type (ISO/NSO/RSU/PSU), deferred comp, severance amount and form]
- **Employee age:** [40+ triggers ADEA/OWBPA — required for release sizing]
- **Group separation?** [Yes/no — OWBPA group disclosure schedule requirement]
- **Existing agreements:** [Prior offer letter, equity plan, bonus plan, confidentiality/IP, restrictive covenant terms still in force]
- **Restrictive covenants requested:** [Non-compete duration/geography, non-solicit of employees, non-solicit of customers, non-disparagement]
- **Benefits affected on exit:** [Health (COBRA), unemployment posture, equity vesting acceleration, 401(k), deferred comp]
- **Claims to release / carve out:** [Workers' comp, unemployment, vested benefits, §7 NLRA rights, whistleblower/SEC, ADEA-specific]

---

## Constraints

**Must:**
- State at-will employment expressly in the offer letter and reaffirm it everywhere employment status is described; ensure no language (e.g., "permanent," "guaranteed term," progressive-discipline references) undermines at-will.
- Include IP assignment with the state-mandated carve-out for inventions developed on the employee's own time without employer resources, where required:
  - **CA Labor Code § 2870** carve-out and written notice.
  - **WA RCW 49.44.140**, **DE 19 Del. C. § 805**, **IL 765 ILCS 1060/2**, **KS K.S.A. 44-130**, **MN Minn. Stat. § 181.78**, **NC N.C.G.S. § 66-57.1**, **UT Utah Code § 34-39-3** — include the substantively equivalent carve-out.
  - Confirm cite for the specific state at `[CITE: ...]`.
- Calibrate restrictive covenants to state enforceability (see `legal_non_compete_enforceability_analysis.md`): in CA, ND, OK, and MN (effective 2023), do not include post-employment non-competes for employees covered by those bans; in MA, comply with garden-leave + 10-business-day review (M.G.L. c. 149, § 24L); in WA, comply with salary threshold; in CO, comply with HB 22-1317 thresholds and notice.
- For employees age **40 or older** offered severance in exchange for a release of age claims:
  - **Individual separation:** 21-day consideration period and 7-day post-signing revocation window (ADEA/OWBPA, 29 U.S.C. § 626(f)).
  - **Group separation / RIF (2+ employees):** 45-day consideration period, 7-day revocation, and OWBPA group disclosure schedule (job titles and ages of selected vs. non-selected employees in the decisional unit).
  - Written advice to consult counsel before signing.
  - Release must be knowing and voluntary; cannot waive claims arising after signing.
- Include state-specific release-validity requirements:
  - **CA § 1542** waiver with the prescribed waiver language, plus separate older-worker considerations under the **Older Workers Benefit Protection Act** as overlaid with state law.
  - **MN** 15-day rescission for state-law claims.
  - **NJ** specific release requirements for state discrimination claims under the **NJ LAD**; restrictions on NDAs covering discrimination/harassment/retaliation post-2019.
  - State NDA bans on discrimination/harassment claims (NY, NJ, CA, IL, WA, OR, NV, etc.) — carve those claims out of any confidentiality/non-disparagement clause.
- Coordinate severance payment timing with **IRC § 409A**: either fit a short-term-deferral exception (paid by 2½ months after end of tax year of vesting), the separation-pay exception (limits on amount and timing), or comply with § 409A's payment-event and timing rules. Do not allow employee election that accelerates payment in violation of § 409A.
- Address equity treatment explicitly: which grants vest, accelerate, are forfeited; whether stock options' post-termination exercise window runs; whether the separation triggers a "good reason" or "for cause" definition.
- Address **COBRA** continuation coverage and any employer subsidy (taxability under IRC § 4980B and ARPA-era considerations if relevant).
- Address unemployment-benefits coordination: do not require the employee to falsely characterize the separation; state any agreement on the employer's UI-contest position (or non-contest).
- Preserve protected rights in every release and confidentiality clause:
  - Right to file a charge with EEOC/NLRB/SEC/OSHA/state agencies (cannot waive the right to file, only personal monetary recovery, and even that not for SEC whistleblower bounties under Dodd-Frank).
  - NLRA § 7 rights to discuss wages and working conditions.
  - Defend Trade Secrets Act (DTSA) whistleblower immunity notice under 18 U.S.C. § 1833(b) — required in any agreement governing trade-secret use.
- Use defined terms consistently across the offer and separation documents.

**Must Not:**
- Promise employment for a specific term or imply termination only "for cause" if at-will is intended.
- Include a non-compete in a state where it is void as to this employee (CA, ND, OK; MN for post-2023; FTC rule status — note current status with `[CITE: ...]`).
- Use a generic "consult an attorney" clause as a substitute for ADEA/OWBPA's specific advice and timing requirements.
- Waive claims that cannot legally be waived: future claims, unemployment compensation, workers' compensation, vested ERISA benefits, FLSA wage claims absent DOL/court supervision in some jurisdictions, certain state wage claims, child-support, and SEC whistleblower awards.
- Include a confidentiality or non-disparagement clause that purports to silence the employee on discrimination, harassment, or retaliation claims in states banning such NDAs (NY, NJ, CA, IL, WA, OR, NV, ME, HI, VT, and others — verify cite at `[CITE: ...]`).
- Restructure severance into installments after the release is signed in a way that triggers § 409A penalties.
- Cite statutes or cases without verification; use `[CITE: ...]` placeholders.
- Include generic "consult counsel" disclaimers in lieu of substantive guardrails.

---

## Instructions

1. **Confirm posture, state, age, and group status.** These four facts drive most mandatory rules. Flag any missing.
2. **Map existing obligations.** List all prior agreements (offer letter, equity, bonus, restrictive covenants, arbitration) and note which survive, which are superseded, and which are amended.
3. **Draft / amend the offer letter** with: position and reporting line; start date; at-will statement; base compensation and pay schedule; bonus or commission terms (with eligibility and earned-versus-paid rules); equity grant reference (subject to board approval and plan documents); benefits eligibility; FLSA exempt/non-exempt designation; conditions precedent (background check, I-9, drug test where lawful); reference to and execution requirement of confidentiality/IP and restrictive-covenant agreements.
4. **Draft the IP/confidentiality agreement** with: assignment of inventions; state-mandated carve-out with required notice; prior inventions schedule; confidentiality with reasonable scope and duration; return-of-property obligation; DTSA whistleblower notice; carve-outs for protected disclosures.
5. **Draft restrictive covenants calibrated to state law** with duration, geography, and scope tied to legitimate business interests; include consideration analysis (continued employment may or may not be sufficient depending on state); include garden-leave or notice requirements where state law requires.
6. **For separation, draft the separation agreement** with: separation date; final wage payment compliant with state final-paycheck law; severance amount, form, and timing (with § 409A analysis); benefits continuation (COBRA, subsidies); equity treatment; release of claims (general release with carve-outs); reaffirmation of surviving obligations (confidentiality, IP, restrictive covenants); non-disparagement (with state-required carve-outs); cooperation clause; references policy; return of property; consideration period and revocation window sized to age and group status; signature blocks.
7. **Layer in protected-rights carve-outs** in every release, confidentiality, and non-disparagement clause: agency-filing rights, § 7 NLRA, SEC/Dodd-Frank, DTSA, state discrimination/harassment NDA bans.
8. **Coordinate the documents.** Ensure the offer letter, IP agreement, restrictive covenants, and any prior agreements are consistent on definitions, choice of law, dispute resolution (arbitration, jury waiver — note enforceability constraints), and surviving obligations.
9. **Run the verification checklist** and the false-positive table.

---

## Output Format

Deliver as a coordinated set. Use this skeleton; expand each section to a full draft.

```markdown
# EMPLOYMENT PACKAGE — {Employee Name} | {Role} | {State}

## SUMMARY OF TERMS
- Posture: {onboarding / amendment / separation}
- State: {state} | Federal coverage: {Title VII / ADEA / ADA / FMLA / ERISA — yes/no}
- Age 40+: {yes/no} | Group separation: {yes/no}
- § 409A analysis: {short-term deferral / separation-pay exception / compliant deferred comp}

---

## DOCUMENT 1 — OFFER LETTER (or AMENDMENT)
{Date}
{Employee name and address}

Dear {Name}:
1. Position and Reporting: {...}
2. Start Date / Effective Date: {...}
3. At-Will Employment: Your employment with {Company} is at-will. Either you or the Company may terminate the employment relationship at any time, with or without cause and with or without notice. No statement in this letter, any handbook, or any communication shall create an express or implied contract of employment for any specific duration or alter the at-will nature of the relationship.
4. Compensation: Base salary of ${...} per {year/pay period}, less applicable withholdings.
5. Bonus / Commission: {Plan reference, eligibility, earned-versus-paid rules}.
6. Equity: {Grant type, share count, vesting schedule — subject to board approval and the {Plan Name}}.
7. Benefits: {...}
8. FLSA Status: {Exempt / Non-Exempt}, classified as {executive / administrative / professional / computer / outside sales / highly compensated / non-exempt under FLSA and {state} law}.
9. Conditions: {I-9, background check, drug test where lawful, execution of attached IP and Restrictive Covenant Agreements}.
10. Entire Agreement; Governing Law: {state}. [CITE: state-specific choice-of-law constraint if any]

Signed,
{Company representative}

Accepted: ___________________________  Date: __________

---

## DOCUMENT 2 — CONFIDENTIALITY AND INVENTION ASSIGNMENT AGREEMENT
1. Confidential Information — definition and obligations.
2. Assignment of Inventions — {full assignment, subject to state carve-out below}.
3. State Carve-Out (REQUIRED for {CA / WA / DE / IL / KS / MN / NC / UT}): NOTICE — This Agreement does not require assignment of any invention that the Employee developed entirely on the Employee's own time without using the Company's equipment, supplies, facilities, or trade secret information, except for inventions that (a) relate at the time of conception or reduction to practice to the Company's business or actual or demonstrably anticipated research or development, or (b) result from work performed by the Employee for the Company. [CITE: {state statute}]
4. Prior Inventions Schedule — Exhibit A.
5. Return of Property.
6. DTSA Whistleblower Immunity Notice (18 U.S.C. § 1833(b)): An individual shall not be held criminally or civilly liable under any federal or state trade secret law for the disclosure of a trade secret that (i) is made in confidence to a federal, state, or local government official, either directly or indirectly, or to an attorney; and (ii) is made solely for the purpose of reporting or investigating a suspected violation of law; or is made in a complaint or other document filed in a lawsuit or other proceeding, if such filing is made under seal.
7. Protected Activity Carve-Out — Nothing in this Agreement limits the Employee's right to file a charge with the EEOC, NLRB, SEC, OSHA, or any state agency, to participate in such proceedings, to receive a whistleblower award, or to engage in protected concerted activity under § 7 of the NLRA.

---

## DOCUMENT 3 — RESTRICTIVE COVENANTS (calibrated to {state})
1. Non-Solicit of Employees: {duration / scope}.
2. Non-Solicit of Customers: {duration / scope tied to employee's customer-facing role}.
3. Non-Compete: {INCLUDE only if enforceable in {state}; otherwise mark "Omitted — void under {state} law per [CITE: ...]"}.
4. Garden Leave / Notice (if MA / required): {...}.
5. Consideration: {sign-on amount / equity grant / continued employment — analyze sufficiency under {state} law}.
6. Choice of Law / Venue: {state} — note enforceability of choice-of-law against employee's home state under §187 Restatement.
7. Blue Pencil / Reformation: {state-appropriate clause — strict construction states do not reform}.

---

## DOCUMENT 4 — SEPARATION AGREEMENT AND GENERAL RELEASE (if posture = separation)
1. Separation Date.
2. Final Wages: Paid in compliance with {state} final-pay law ({immediate / next regular payday / [CITE: state statute]}).
3. Severance: ${...} payable {lump sum / installments}, subject to and conditioned on this Release becoming effective. § 409A treatment: {short-term deferral / separation-pay exception / compliant deferral}.
4. Equity: {accelerated / forfeited / continued vesting; option exercise window}.
5. Benefits: COBRA notice will issue; {employer subsidy if any, taxability noted}.
6. General Release: Employee releases all claims arising on or before the Effective Date, including {Title VII, ADEA, ADA, FMLA, ERISA, state FEHA/LAD/equivalent, wage-hour claims to the extent waivable}, EXCEPT: workers' comp, unemployment, vested benefits, claims arising after signing, non-waivable claims, and the protected-rights carve-out below.
7. ADEA/OWBPA (if Employee age 40+):
   - Individual: 21-day consideration period; 7-day revocation; advice to consult counsel.
   - Group: 45-day consideration period; 7-day revocation; OWBPA disclosure schedule attached as Exhibit B (job titles and ages of selected and non-selected employees in the decisional unit).
8. CA § 1542 Waiver (if CA): {required statutory language}.
9. {State} Rescission Period (if MN / required): 15 days.
10. Protected Rights: Nothing in this Agreement limits Employee's right to file a charge with the EEOC, NLRB, SEC, OSHA, DOL, or state agencies, to participate in agency proceedings, to receive an SEC whistleblower award, or to engage in § 7 NLRA activity. Employee is not required to notify Company of any such filing.
11. Confidentiality / Non-Disparagement: Mutual, with carve-outs for protected disclosures and {state} NDA bans on discrimination/harassment/retaliation claims [CITE: state statute].
12. Reaffirmation of Surviving Obligations: confidentiality, IP, restrictive covenants (to the extent enforceable).
13. References Policy: {neutral / agreed statement}.
14. Return of Property.
15. Cooperation: reasonable post-employment cooperation in litigation/investigations.
16. Tax: 1099/W-2 treatment of severance; allocation between wages and other consideration.
17. Choice of Law / Venue / Dispute Resolution.
18. Entire Agreement.

Signed: ____________________ {Employee}  Date: ________
Signed: ____________________ {Company}   Date: ________
```

---

## Verification

- [ ] At-will language present in offer letter and not undermined elsewhere.
- [ ] IP assignment includes state-mandated carve-out with required statutory notice, with `[CITE: ...]` placeholder verified.
- [ ] Restrictive covenants calibrated to state enforceability; non-compete omitted in banned states.
- [ ] ADEA/OWBPA consideration window (21 or 45 days), 7-day revocation, and group disclosure schedule applied where Employee is 40+ and severance is offered for a release of age claims.
- [ ] § 1542 waiver included for CA; analogous state requirements addressed.
- [ ] § 409A analysis documented — short-term deferral, separation-pay exception, or compliant deferred comp.
- [ ] COBRA, unemployment, and equity treatment all addressed.
- [ ] Protected-rights carve-out (EEOC/NLRB/SEC/OSHA/§7 NLRA/DTSA) appears in every release, confidentiality, and non-disparagement clause.
- [ ] State NDA bans on discrimination/harassment/retaliation claims respected.
- [ ] No invented citations — all statutory references marked `[CITE: ...]` if not verified in source.
- [ ] Definitions and surviving obligations are internally consistent across documents.

---

## False-Positive Prevention

| Failure mode | Correction |
|---|---|
| Offer letter promises "long-term" or "career" employment, undermining at-will | Strike aspirational language; preserve at-will defense |
| IP assignment without CA § 2870 / WA / DE / IL / KS / MN / NC / UT carve-out and notice | Add the statutorily-required notice text verbatim; cite at `[CITE: ...]` |
| Including a post-employment non-compete in CA, ND, OK, or for MN employees post-2023 | Omit and use non-solicit / IP / confidentiality protections instead |
| 21-day ADEA window applied to a group separation | Group separations require 45 days plus the OWBPA disclosure schedule |
| Generic release that purports to waive workers' comp, unemployment, or future claims | Carve out non-waivable claims explicitly |
| Confidentiality or non-disparagement clause silencing discrimination/harassment claims in a banned-NDA state | Add carve-out for those claims with `[CITE: state statute]` |
| Severance paid in installments crossing two tax years without § 409A analysis | Restructure for short-term deferral, separation-pay exception, or compliant deferred comp |
| Choice-of-law clause selecting a non-compete-friendly state for an employee in CA | Analyze §187 Restatement and likely challenge; do not assume enforceability |
| Treating "continued employment" as sufficient consideration for new restrictive covenants in a state requiring additional consideration | Provide a sign-on or equity grant tied to the covenant |
| Omitting DTSA whistleblower notice in IP/confidentiality agreement | Add 18 U.S.C. § 1833(b) notice — required to recover exemplary damages and fees under DTSA |
| Restricting employee from filing EEOC/NLRB/SEC charges | Cannot be waived; add protected-rights carve-out |
| Fabricated case names or statutory cites | Use `[CITE: ...]` placeholders; do not invent authority |
