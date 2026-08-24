---
title: "Wage and Hour Classification Analysis"
category: legal/employment-labor
description: "Two-part classification analysis: (1) exempt vs non-exempt under FLSA white-collar exemptions and state-law equivalents; (2) employee vs independent contractor under federal economic-reality, state ABC tests (CA AB5, MA, NJ), and CA Borello — with salary-basis, duties, and risk-mitigation outputs."
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
  - wage-and-hour
  - flsa
  - misclassification
  - independent-contractor
updated: "2026-05-11"
related_prompts:
  - domain-legal/employment-labor/legal_employment_offer_and_separation_package.md
  - domain-legal/employment-labor/legal_non_compete_enforceability_analysis.md
  - domain-legal/research/legal_jurisdiction_split_analysis.md
---

**Purpose:** Run a defensible classification analysis for a specific worker (or class of workers) under (a) the FLSA's white-collar exemptions and the controlling state's exemption rules; or (b) the federal economic-reality test for independent-contractor status, the state's ABC test (where applicable), and California's Borello multi-factor test where ABC's exceptions apply — producing a written analysis with risk findings and remediation.

**When to use:** Onboarding a new role; converting a contractor to employee or vice versa; auditing a workforce after an FLSA collective action, state PAGA action, or DOL/state DOL investigation; restructuring compensation; M&A diligence on a target's workforce.

---

## Your Input

- **Analysis type:** [Exempt/non-exempt / Employee/contractor / Both]
- **Jurisdiction:** [Primary work state + federal — state law often more protective; multi-state workforce requires per-state analysis]
- **Industry:** [Tech, financial services, construction, healthcare, transportation (motor carrier exemption?), agriculture, hospitality, gig economy — industry-specific exemptions and tests apply]
- **Role / title:** [Title is not dispositive — duties are]
- **Posture:** [Pre-hire classification / audit / post-claim defense / DOL or state DOL audit / class action discovery]
- **Compensation:**
  - Salary or hourly: [amount per period]
  - Weekly equivalent: [for FLSA salary-basis test — $684/week minimum federal as of 2024; higher state minimums in CA, NY, WA, CO, ME, AK]
  - Bonuses, commissions, draws: [structure]
  - Highly compensated total annual compensation: [if relevant for HCE exemption — $107,432/year federal threshold (subject to update); verify current at `[CITE: ...]`]
- **Duties (be specific — describe actual day-to-day, not job description):**
  - Primary duty: [most important task by importance, not time]
  - Discretion and independent judgment exercised: [examples on matters of significance]
  - Supervision: [number of FTEs supervised; hiring/firing authority]
  - Specialized knowledge: [advanced/learned profession field, prolonged course of specialized intellectual instruction]
  - Sales activity: [inside vs outside, customary travel]
  - Computer-employee work: [systems analysis, programming, software engineering, specific tasks]
- **For contractor analysis:**
  - Engagement: [project-based / ongoing; written agreement?]
  - Control: [who sets schedule, location, methods, tools]
  - Investment / equipment: [who provides]
  - Opportunity for profit/loss: [contractor's own initiative and judgment]
  - Permanence: [duration; exclusivity]
  - Integration: [task within the hirer's usual course of business]
  - Skill required: [specialized vs unskilled]
  - Other clients: [does the worker serve others; hold themselves out as a business]
- **Class size:** [Single worker / role-wide / company-wide]
- **Existing documentation:** [Job description, offer letter, contractor agreement, time records, payroll, prior classification audits]

---

## Constraints

**Must:**
- For **FLSA exempt/non-exempt** analysis, apply all three prongs where the exemption requires them:
  1. **Salary basis** — paid a predetermined amount not subject to reduction based on quality or quantity of work, subject to the seven permissible deductions in 29 C.F.R. § 541.602(b).
  2. **Salary level** — at least $684/week ($35,568/year) federal, as of the 2020 final rule; verify current threshold at `[CITE: ...]` (a 2024 final rule increased thresholds but has been the subject of court challenges; check status). State minimums often higher: CA (2× state minimum wage for employers of 26+; verify current), NY (varies by region and size), WA (multiplier of state min wage), CO, ME, AK.
  3. **Duties test** — specific to each exemption:
     - **Executive:** primary duty managing the enterprise or a customarily recognized department/subdivision; customarily and regularly directs the work of two or more other employees; authority to hire/fire or recommendations given particular weight. 29 C.F.R. § 541.100.
     - **Administrative:** primary duty office/non-manual work directly related to the management or general business operations of the employer or its customers; includes the exercise of discretion and independent judgment with respect to matters of significance. § 541.200.
     - **Professional (learned):** primary duty performance of work requiring advanced knowledge in a field of science or learning customarily acquired by a prolonged course of specialized intellectual instruction. § 541.300.
     - **Professional (creative):** primary duty work requiring invention, imagination, originality, or talent in a recognized field of artistic or creative endeavor.
     - **Computer:** primary duty in systems analysis, programming, software engineering, or similar — § 541.400; salary basis or $27.63/hour federal hourly option.
     - **Outside sales:** primary duty making sales or obtaining orders/contracts; customarily and regularly engaged away from the employer's place of business. § 541.500. No salary requirement.
     - **Highly compensated:** total annual compensation ≥ $107,432 (verify current); customarily and regularly performs at least one of the duties of executive, administrative, or professional. § 541.601.
- Apply the **more protective** of federal and state rules. CA, NY, and others have:
  - Higher salary thresholds.
  - Stricter duties tests (CA: quantitative — exempt employees must be primarily engaged, i.e., >50% of work time, in exempt duties).
  - Additional exemptions or non-exemptions (e.g., CA's specific tests for commissioned inside sales, computer professionals with separate hourly threshold).
- For **independent-contractor** analysis, apply the controlling test for the relevant claim:
  - **FLSA (federal wage-hour):** Economic-reality test. Current DOL rule (2024) restored a six-factor totality-of-circumstances analysis: opportunity for profit/loss depending on managerial skill; investments by worker and potential employer; degree of permanence; nature and degree of control; whether the work is integral to the employer's business; skill and initiative. Verify current rule status at `[CITE: ...]`.
  - **State ABC tests (where applicable):**
    - **CA AB5 / Labor Code § 2775 (codifying Dynamex):** worker is presumed an employee unless the hirer proves (A) free from control and direction in connection with the performance of the work; (B) the work is performed outside the usual course of the hirer's business; **and** (C) the worker is customarily engaged in an independently established trade, occupation, or business of the same nature. Numerous statutory exceptions (B2B, business-to-business; referral agency; professional services including some licensed professionals) — verify exception applicability.
    - **MA G.L. c. 149, § 148B:** ABC with no usual-course exception.
    - **NJ:** ABC test under wage-and-hour and unemployment statutes.
    - Other states: variations apply.
  - **CA Borello multi-factor test:** applies where AB5 exception is met or for non-Labor-Code claims (workers' comp). Right-to-control plus secondary factors.
  - **NLRA / common-law right-to-control test:** for NLRB jurisdiction.
  - **IRS 20-factor test / "common-law" test:** for federal tax (withholding, FICA, FUTA).
- Apply the test required by the claim — a worker may be a contractor for one test and an employee for another. Identify all applicable tests for the engagement.
- For multi-state remote workforce: analyze per the state of work performance, not the employer's HQ.
- Quantify **risk of misclassification damages**:
  - Federal: 2-year (or 3-year for willful) back wages plus equal liquidated damages plus attorneys' fees. 29 U.S.C. § 216(b).
  - State: often longer lookback (CA 3-4 years), waiting-time penalties (CA Labor Code § 203), itemized wage-statement penalties (CA § 226), PAGA penalties, meal/rest break premiums.
  - Tax: unpaid employer-side FICA, FUTA, state UI, federal/state withholding, plus penalties under IRC §§ 3509, 6651, 6656, 6672.
  - Benefits: ERISA misclassification exposure.
- For exempt employees losing exemption: calculate overtime owed for unrecorded hours; address record-keeping gaps under 29 C.F.R. § 516.
- Use `[CITE: ...]` placeholders for unverified authority.

**Must Not:**
- Rely on job title or written agreement label — duties and economic reality control.
- Treat the salary-basis test as satisfied if improper deductions have been taken; analyze deduction history and the safe-harbor rules at 29 C.F.R. § 541.603.
- Apply only the federal test where state law is more protective.
- Assume an ABC test exception applies without verifying every prong of the exception.
- Conflate the IRS common-law test with the FLSA economic-reality test — different standards.
- Use generic "consult counsel" disclaimers.
- Cite statutes or cases without verification.

---

## Instructions

1. **Identify all applicable tests.** For each potential claim (wage-hour, unemployment, workers' comp, tax, benefits, NLRA), list the test that governs.
2. **Build the duties profile.** Capture actual day-to-day duties — by importance, not by time — with concrete examples. Quote job description and contrast with reality.
3. **Run salary basis and salary level** (for exempt analysis). Identify weekly equivalent; compare federal and state thresholds; flag any improper deductions.
4. **Run the applicable duties test(s).** Walk through each element of the candidate exemption with specific evidence. State strength of each element.
5. **Apply the more-protective rule** — state vs federal.
6. **For contractor analysis**, run each applicable test independently. ABC, economic reality, Borello, IRS common-law, NLRA — different conclusions are possible.
7. **Flag multi-state issues** — workers in CA, MA, NJ trigger ABC; workers in CA also trigger Borello for non-wage claims.
8. **Quantify exposure** — back wages, liquidated damages, waiting-time penalties, wage-statement penalties, PAGA, taxes, benefits.
9. **Recommend remediation** — reclassification with prospective effect; rolling reclassification with back-pay; restructure duties; restructure compensation to meet salary level; restructure contractor relationship to satisfy the controlling test (delegate control, change integration, restructure for B2B exception).
10. **Document conclusions** in a privileged memorandum if counsel-directed.

---

## Output Format

```markdown
# WAGE & HOUR CLASSIFICATION ANALYSIS — {Worker / Role} | {State}

[Privilege Legend if counsel-directed]

## 1. Scope and Posture
- Analysis type: {exempt-status / contractor-status / both}
- Worker(s): {individual / role / class}
- Jurisdictions: {primary + secondary}
- Posture: {pre-hire / audit / claim defense / DOL audit / M&A diligence}

## 2. Applicable Tests
| Claim | Governing test | Authority |
|---|---|---|
| FLSA wage-hour | Economic reality (DOL 2024 rule) | [CITE: ...] |
| State wage-hour (CA) | ABC (Lab. Code § 2775) | [CITE: ...] |
| State unemployment | {test} | [CITE: ...] |
| Workers' comp (CA) | Borello | [CITE: ...] |
| Federal tax | IRS common-law | [CITE: ...] |
| ERISA / benefits | Common-law | [CITE: ...] |
| NLRA | Common-law right-to-control | [CITE: ...] |

## 3. Duties Profile
- Job title: {...}
- Job description (excerpted): {...}
- Actual primary duty (by importance): {...}
- Discretion / independent judgment examples: {...}
- Supervision: {FTEs, hire/fire authority}
- Specialized knowledge: {...}
- Sales activity: {inside/outside, %}
- Computer work: {tasks}

## 4. Salary Basis and Level (if exempt analysis)
- Salary: ${...}/{period} → weekly equivalent ${...}
- Federal threshold: $684/week [CITE: 29 C.F.R. § 541.600; verify 2024 rule status]
- State threshold ({state}): ${...} [CITE: ...]
- Threshold met: {yes/no — under which jurisdiction}
- Salary-basis compliance: {improper deductions reviewed; safe harbor analysis if needed} [CITE: 29 C.F.R. § 541.603]

## 5. Duties Test (exempt candidate)
- Candidate exemption: {executive / administrative / professional / computer / outside sales / HCE}
- Federal duties test elements:
  | Element | Evidence | Strength |
  |---|---|---|
  | {element 1} | {specific facts} | {strong/moderate/weak} |
- State duties test (if more protective):
  - CA quantitative test (>50% of time in exempt duties): {analysis}

Conclusion: {Exempt / Non-Exempt under {jurisdiction}}

## 6. Contractor-Status Analysis (if applicable)

### A. State ABC Test (e.g., CA AB5)
- (A) Free from control: {analysis}
- (B) Outside usual course of hirer's business: {analysis}
- (C) Customarily engaged in independent trade: {analysis}
- AB5 exception analysis: {B2B / referral / professional services / other — element-by-element}
- Conclusion: {Employee / Contractor under ABC}

### B. FLSA Economic Reality
- Opportunity for profit/loss: {...}
- Investments: {...}
- Permanence: {...}
- Control: {...}
- Integral to business: {...}
- Skill and initiative: {...}
- Conclusion under DOL 2024 rule: {Employee / Contractor}

### C. CA Borello (or applicable common-law test)
- Right to control (primary): {...}
- Secondary factors: {...}
- Conclusion: {Employee / Contractor}

### D. IRS Common-Law
- Behavioral / financial / relationship: {...}
- Conclusion: {Employee / Contractor for tax}

### E. NLRA Common-Law Right-to-Control
- Conclusion: {Employee / Contractor for NLRA}

## 7. Exposure Quantification (if misclassification)
- Federal back wages (2 or 3 years for willful): ${estimate}
- Liquidated damages: equal to back wages
- Attorneys' fees: 29 U.S.C. § 216(b)
- State back wages and lookback ({state}): ${...}
- Waiting-time penalties (CA § 203): ${...}
- Wage-statement penalties (CA § 226): ${...}
- PAGA penalties ({state}): ${...}
- Employer-side FICA / FUTA / state UI: ${...}
- Federal/state withholding: ${...}
- IRC § 3509 reduced rates if applicable: {analysis}
- Benefits exposure (ERISA): {analysis}
- Total exposure estimate: ${...}

## 8. Findings
| Issue | Risk level | Basis |
|---|---|---|
| {misclassification of role X} | {High/Mod/Low} | {test failed, exposure} |

## 9. Remediation
- Prospective reclassification: {steps}
- Back-pay restructuring: {scope, lookback, voluntary disclosure considerations (DOL PAID, IRS VCSP)}
- Duties restructure: {to fit exemption or to support contractor status}
- Compensation restructure: {salary level to threshold}
- Contractor relationship restructure: {control, integration, B2B factors}
- Documentation: {time records, written agreements, scope of work}

## 10. Recommendations
{Numbered actions}
```

---

## Verification

- [ ] All applicable tests identified per claim.
- [ ] Duties profile based on actual work, not job description.
- [ ] Salary basis and salary level checked against federal and the more-protective state threshold.
- [ ] Duties test walked through element by element with specific evidence.
- [ ] State quantitative test (e.g., CA >50%) applied where required.
- [ ] ABC, economic reality, Borello, IRS, NLRA tests applied independently where claim requires.
- [ ] ABC exceptions analyzed element by element, not by conclusion.
- [ ] Exposure quantified across federal back wages, liquidated damages, state penalties, tax, benefits.
- [ ] `[CITE: ...]` placeholders used; current federal rule status noted.
- [ ] Remediation includes prospective reclassification, back-pay, and structural fixes.

---

## False-Positive Prevention

| Failure mode | Correction |
|---|---|
| Treating job title as dispositive | Duties control; build a duties profile from actual work |
| Salary basis satisfied without checking improper-deduction history | Audit deductions; analyze § 541.603 safe harbor |
| Applying federal exemption where state (CA, NY, WA) has stricter test | Apply more-protective rule |
| Using job description instead of actual duties for >50% CA quantitative analysis | Build duties profile from interview / time records |
| ABC exception assumed without verifying every prong | Walk each prong; B2B and professional-services exceptions are narrow |
| Conflating IRS common-law with FLSA economic reality | Different tests, different conclusions possible |
| Ignoring waiting-time, wage-statement, and PAGA penalties in exposure | State penalties often dwarf federal back wages |
| Reclassifying without back-pay where lookback applies | Document the voluntary disclosure path; DOL PAID and IRS VCSP have eligibility requirements |
| Multi-state workforce analyzed only under HQ state | Analyze per state of work performance |
| Outdated federal threshold | Verify current rule status at `[CITE: ...]`; 2024 DOL final rule has been challenged |
| Contractor agreement treated as dispositive | The label does not control; the test controls |
| Fabricated case names or rule cites | Use `[CITE: ...]` placeholders |
