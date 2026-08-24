---
title: "Non-Compete and Restrictive-Covenant Enforceability Analysis"
category: legal/employment-labor
description: "Multi-state enforceability analysis of non-competes, non-solicits (employees and customers), and confidentiality / IP covenants under current state law, FTC rule status, and choice-of-law principles — with garden leave, blue-pencil vs reformation vs strict-construction outcomes, and concrete remediation."
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
  - non-compete
  - restrictive-covenants
  - trade-secrets
  - choice-of-law
updated: "2026-05-11"
related_prompts:
  - domain-legal/employment-labor/legal_employment_offer_and_separation_package.md
  - domain-legal/employment-labor/legal_wage_hour_classification_analysis.md
  - domain-legal/research/legal_jurisdiction_split_analysis.md
  - domain-legal/contracts-transactional/legal_contract_clause_redline_targeted.md
---

**Purpose:** Produce a multi-jurisdictional enforceability assessment of a restrictive-covenant package (non-compete, employee non-solicit, customer non-solicit, confidentiality/IP) — applying the controlling state's substantive rules, choice-of-law constraints, blue-pencil/reformation/strict-construction doctrine, the FTC's non-compete rule status, and recent state reforms (MN, MA, CO, WA, OR, NV, VA, IL, NM and others).

**When to use:** Drafting or reviewing a covenant before hiring or promotion; analyzing whether to enforce against a departing employee; defending a worker against a former employer's covenant; pre-litigation injunction analysis; M&A diligence on a target's restrictive-covenant book; post-departure cease-and-desist strategy.

---

## Your Input

- **Posture:** [Drafting / pre-enforcement evaluation / TRO/PI analysis / defending against enforcement / diligence]
- **Employer state(s):** [State of incorporation, principal place of business, where the covenant was signed]
- **Employee state(s):** [State of residence and primary work; for remote workers, the state of actual work performance — often controlling]
- **Choice-of-law and forum-selection clauses in the covenant:** [As written]
- **Role and access:** [Title, level, duties, customer-facing, access to trade secrets or strategic info, R&D access]
- **Consideration provided:** [Initial employment, promotion, equity grant, sign-on bonus, garden leave, continued employment only]
- **Compensation:** [Base, total comp — relevant to state salary-threshold rules]
- **Covenant scope:**
  - Non-compete: duration, geography, scope of restricted activity
  - Employee non-solicit: duration, scope (all employees / those with whom employee worked)
  - Customer non-solicit: duration, scope (all customers / those with whom employee worked / those known to employee)
  - Confidentiality: scope and duration
  - IP assignment: scope and state carve-out
- **Industry:** [Sector — some states (CA broadcasters, MA physicians, healthcare workers in many states, low-wage workers in WA/OR/IL) have industry-specific bans]
- **Legitimate business interest claimed:** [Trade secrets, confidential information, customer relationships, goodwill, specialized training, investment in employee]
- **Trigger event:** [Departure date; new employer (if known); whether departure is voluntary or termination without cause — affects enforceability in some states (e.g., MA "garden leave" implications; IL involuntary-termination caveats)]
- **Notice and review period provided at signing:** [Days prior to start date; advice to consult counsel]

---

## Constraints

**Must:**
- Run a **per-state enforceability analysis** for every state implicated (employer, employee work state, covenant's choice-of-law state).
- Apply each state's **substantive rule**:
  - **California:** Non-competes between employee and employer are void as to post-employment activity. Cal. Bus. & Prof. Code § 16600. Effective 2024, CA SB 699 / AB 1076 expand the prohibition — employers must give notice of voidness to current and former employees with such covenants. Narrow sale-of-business and dissolution-of-partnership exceptions only. [CITE: ...]
  - **North Dakota:** Non-competes void. N.D. Cent. Code § 9-08-06. [CITE: ...]
  - **Oklahoma:** Non-competes void except limited non-solicit. Okla. Stat. tit. 15, § 219A. [CITE: ...]
  - **Minnesota:** Effective July 1, 2023 — non-competes void for all employees and independent contractors (prospective only). Minn. Stat. § 181.988. Non-solicits and confidentiality survive. [CITE: ...]
  - **Massachusetts:** Massachusetts Noncompetition Agreement Act, M.G.L. c. 149, § 24L: enforceable only if in writing, signed by both parties, advance notice (10 business days before start or with offer, whichever is earlier), advice to consult counsel, duration ≤ 12 months (24 months if employee breached fiduciary duty or unlawfully took employer property), supported by garden leave (50% of base) or other mutually-agreed consideration. Non-solicits and customer-non-solicits not subject to the Act. [CITE: ...]
  - **Washington:** RCW 49.62 — non-compete enforceable only if employee earns above the statutory threshold (verify current — $120,559.99 for employees, $301,399.98 for contractors, indexed annually; verify at `[CITE: ...]`), notice at time of offer, garden-leave or layoff-pay requirement, duration > 18 months presumed unreasonable.
  - **Colorado:** HB 22-1317 — non-competes generally void except for highly compensated workers (verify current threshold; > $123,750 in 2024, indexed) plus trade-secret protection purpose; customer non-solicits require highly compensated × 60% threshold. Notice requirements (14 days). [CITE: ...]
  - **Oregon:** ORS 653.295 — enforceable only for salaried/exempt employees above the median family income for a 4-person family (verify current), 12-month max duration, notice 2 weeks before start.
  - **Illinois:** Illinois Freedom to Work Act, 820 ILCS 90 — non-compete enforceable only if employee earns > $75,000 (indexed; verify current); non-solicit > $45,000. Notice requirement; advice to consult counsel; 14-day review. Carve-outs for involuntary termination during COVID-era; verify ongoing application.
  - **Virginia:** Va. Code § 40.1-28.7:8 — non-competes void for "low-wage employees" (defined by reference to state weekly average wage; verify current).
  - **New Mexico, Maryland, Maine, New Hampshire, Rhode Island, Nevada:** various income thresholds and industry restrictions; verify each at `[CITE: ...]`.
  - **New York:** No statutory non-compete prohibition yet (the 2023 bill was vetoed); common-law BDO Seidman / Reed Elsevier reasonableness test — legitimate interest, reasonable in time and geography, not harmful to public, not unduly burdensome on employee. Heightened scrutiny for broadcast / media / financial-services / professional services. [CITE: ...]
  - **Texas:** Tex. Bus. & Com. Code § 15.50 — enforceable if ancillary to otherwise enforceable agreement and reasonable in time, geographic area, and scope of activity. Court must reform overbroad covenants (mandatory reformation, not blue pencil). [CITE: ...]
  - **Florida:** Fla. Stat. § 542.335 — enforceable with legitimate business interest; statutory presumptions of reasonable duration; mandatory reformation if overbroad.
  - **Other states:** apply the controlling test — typically reasonableness on duration, geography, scope; protectable interest; consideration sufficiency; public-interest balancing.
- Apply **federal layer**:
  - **FTC Non-Compete Rule** (16 C.F.R. § 910): the FTC's final rule banning most non-competes (issued April 2024, effective date September 4, 2024) was vacated nationwide by the Northern District of Texas in *Ryan LLC v. FTC* (August 2024); status on appeal — verify current status at `[CITE: ...]` before relying.
  - **Defend Trade Secrets Act** (18 U.S.C. § 1836) — federal cause of action for trade-secret misappropriation; inevitable-disclosure doctrine varies by state and is generally unavailable in CA.
- Apply the **choice-of-law analysis** under Restatement (Second) Conflict of Laws § 187:
  - A choice-of-law clause selecting a non-compete-friendly state will not be honored if (a) the chosen state has no substantial relationship to the parties or transaction and there is no other reasonable basis, or (b) the chosen-state law is contrary to a fundamental policy of a state with a materially greater interest — and that state would be the law applied absent choice (e.g., CA's anti-non-compete policy generally overrides choice-of-law).
  - California enacted **Cal. Lab. Code § 925** — restricts forum-selection and choice-of-law clauses for employees primarily working in CA; covered employees can void such clauses unless represented by counsel in negotiation. [CITE: ...]
- Apply **consideration sufficiency** per state:
  - Continued employment alone is sufficient consideration in some states (TX, MA for non-solicits) and insufficient in others (IL: 2+ years of continued employment required after Fifield v. Premier Dealer Services; PA: not sufficient without independent consideration). Identify the rule for each state.
- Apply the state's **judicial-reformation approach**:
  - **Blue-pencil:** court may strike unreasonable portions but cannot rewrite (e.g., GA historically, though modified by 2011 reforms; some states).
  - **Equitable reformation:** court may rewrite to make reasonable (FL, TX (mandatory), MA, OH, NJ in many cases).
  - **Strict construction / red-pencil:** court voids the entire covenant if any portion is overbroad (VA, NE, WI historically — verify current).
  - This determines the litigation risk: in strict-construction states, an overbroad covenant is unenforceable in its entirety.
- For **garden leave**: address whether it is required (MA) or beneficial (WA, CO) and whether the covenant is compensable enough to be enforced.
- Analyze whether the **trigger event** affects enforceability: many states (IL, MA, NJ, WI lines of authority) limit enforcement after involuntary termination without cause.
- Analyze **inevitable disclosure**: available in some states (IL, OH); rejected in CA; varies elsewhere. Identify per jurisdiction.
- Quantify the **practical enforceability**: TRO/PI likelihood, irreparable harm showing, balance of equities, public interest, bond requirements.
- Use `[CITE: ...]` placeholders for any authority not verified.

**Must Not:**
- Treat a choice-of-law clause as decisive; analyze §187 against the employee's actual work state.
- Apply pre-reform analysis in states that have changed law (MN 2023, MA 2018, CO 2022, IL 2022, WA 2020).
- Assume the FTC non-compete rule is in effect — its status is litigation-contingent; verify.
- Conflate non-competes with non-solicits / confidentiality / IP — each has its own enforceability rules; many states (MN, CA) ban non-competes but permit narrowed non-solicits and confidentiality.
- Rely on "trade secret protection" as a magic phrase — must identify the protectable interest with specificity.
- Use generic "consult counsel" disclaimers.
- Cite cases or statutes without verification.

---

## Instructions

1. **Identify all implicated states.** Employer state, employee work state, covenant choice-of-law, prospective new employer's state. Build the state matrix.
2. **Per state, run the substantive enforceability analysis.** Apply the controlling rule, thresholds, notice requirements, consideration rules, garden-leave/notice rules, duration caps, and industry restrictions.
3. **Run the choice-of-law analysis** under §187. Identify the state whose law would apply absent the clause; assess whether the clause survives.
4. **Run the consideration analysis** per state.
5. **Run the reformation analysis** per state — blue pencil / equitable reformation / strict construction. Map the practical impact: in strict-construction states, an overbroad clause fails entirely.
6. **Run the trigger-event analysis** — involuntary termination, RIF, sale of business.
7. **Distinguish covenant types** — non-compete, employee non-solicit, customer non-solicit, confidentiality, IP. State enforceability separately for each.
8. **Run the FTC rule status** check — note the *Ryan LLC* ruling and appellate posture; do not assume the rule is in effect.
9. **For enforcement posture** — assess TRO/PI likelihood: protectable interest, breach, irreparable harm, balance of equities, public interest, bond.
10. **For drafting posture** — produce a calibrated covenant set that maximizes enforceability across the relevant states; flag if a state's law makes any covenant void.
11. **For defense posture** — identify defenses (overbreadth, lack of consideration, change in role since signing, employer breach, public interest).
12. **Recommendations** — with concrete actions.

---

## Output Format

```markdown
# RESTRICTIVE-COVENANT ENFORCEABILITY ANALYSIS

[Privilege Legend if counsel-directed]

## 1. Posture and Scope
- Posture: {drafting / enforcement / defense / diligence}
- Employee: {role, level, access}
- States implicated: {employer / work / choice-of-law / new employer}
- Covenant components: {non-compete / employee non-solicit / customer non-solicit / confidentiality / IP}

## 2. State Matrix
| State | Role | Non-compete enforceability | Notes |
|---|---|---|---|
| {state} | {employer / work} | {Enforceable / Void / Conditional} | {salary threshold, notice, duration cap} |

## 3. Per-State Substantive Analysis

### {State 1} — {role: employer / work / new employer}
- Statute / rule: [CITE: ...]
- Threshold (income / role): {met / not met}
- Notice requirement: {met / not met}
- Garden leave / notice pay: {required / provided / absent}
- Duration cap: {months}
- Scope reasonableness: {analysis}
- Legitimate business interest: {identified — trade secrets / customer relationships / goodwill / specialized training}
- Consideration sufficiency: {analysis per state rule}
- Reformation approach: {blue pencil / equitable / strict construction}
- Trigger-event impact: {analysis}
- Industry-specific bans: {none / physician / broadcaster / low-wage / other}
- Enforceability conclusion: {Enforceable / Void / Reformable / Partially enforceable}

### {State 2} ...

## 4. Choice-of-Law Analysis (Restatement § 187)
- Clause selects: {state}
- Substantial relationship: {analysis}
- Default state (absent clause): {state}
- Default-state fundamental policy: {anti-non-compete in CA / other}
- Materially greater interest: {analysis}
- CA § 925 analysis (if employee primarily in CA): {applicable / not applicable}
- Conclusion: {clause honored / overridden / partially honored}

## 5. FTC Non-Compete Rule Status
- Final rule (16 C.F.R. § 910) status as of {date}: {vacated nationwide in Ryan LLC v. FTC; appeal pending — verify at [CITE: ...]}
- Practical effect: {currently no federal-rule prohibition; state law controls}

## 6. Covenant-by-Covenant Enforceability
| Component | {State 1} | {State 2} | {State 3} |
|---|---|---|---|
| Non-compete | {result} | | |
| Employee non-solicit | | | |
| Customer non-solicit | | | |
| Confidentiality | | | |
| IP assignment | | | |

## 7. Enforcement Posture (if applicable)
- Protectable interest: {trade secret / customer relationship / specialized training}
- Breach: {evidence}
- Irreparable harm: {showing}
- Balance of equities: {analysis}
- Public interest: {analysis}
- TRO/PI likelihood: {high / moderate / low}
- Bond requirement: {typical for jurisdiction}
- Inevitable disclosure: {available / unavailable in jurisdiction}
- DTSA federal claim viability: {analysis}

## 8. Defense Posture (if applicable)
- Overbreadth: {analysis}
- Consideration insufficiency: {analysis}
- Material change in role since signing: {analysis}
- Employer breach: {analysis}
- Public-interest defenses: {analysis}
- Strict-construction-state argument: {analysis}

## 9. Findings
| Issue | Risk / Strength |
|---|---|
| {item} | {high / moderate / low} |

## 10. Recommendations
- Drafting: {calibrated covenant set with state-specific carve-outs}
- Enforcement: {pre-suit cease-and-desist; TRO/PI strategy; DTSA alternative}
- Defense: {strongest defenses, motion strategy}
- Operational: {notice issuance under CA SB 699; garden-leave funding; trade-secret protections to substitute for unenforceable non-compete}
```

---

## Verification

- [ ] All implicated states identified.
- [ ] Per-state substantive analysis run with current statute and threshold.
- [ ] Notice, consideration, garden-leave, and duration-cap rules applied per state.
- [ ] Reformation doctrine per state identified — strict construction states flagged.
- [ ] Choice-of-law analysis under §187 (and CA § 925) run.
- [ ] FTC rule status verified at `[CITE: ...]`; not assumed in effect or void.
- [ ] Each covenant component (non-compete, non-solicit, confidentiality, IP) analyzed separately.
- [ ] Trigger-event analysis run for involuntary termination, RIF, sale.
- [ ] Industry-specific bans checked.
- [ ] Practical enforcement factors (TRO/PI, irreparable harm, bond) assessed if enforcement posture.
- [ ] DTSA federal cause of action considered as alternative or supplement.
- [ ] `[CITE: ...]` placeholders used for unverified authority.

---

## False-Positive Prevention

| Failure mode | Correction |
|---|---|
| Treating choice-of-law clause as dispositive | Run §187; CA work state generally overrides; CA § 925 controls for CA employees |
| Assuming FTC rule prohibits the covenant | Rule vacated nationwide in *Ryan LLC*; verify current status |
| Applying pre-reform law in MN, MA, CO, WA, IL, NM, VA | Apply current statutory regime with thresholds and notice |
| Bundling non-compete + non-solicit + confidentiality as one analysis | Each component has its own rules; many anti-non-compete states permit non-solicits |
| Overbroad clause in a strict-construction state | Void in entirety — re-draft with conservative scope |
| "Continued employment" as consideration in IL or PA | Insufficient under controlling state rule; add independent consideration |
| Skipping garden leave in MA | Required by statute; without it, non-compete unenforceable |
| Salary threshold missed in WA, CO, IL, OR, VA, NV, MD | Non-compete void as to employee below threshold |
| Trade-secret invocation without specific interest | Identify the specific trade secret or confidential information; generic invocation fails |
| Inevitable-disclosure doctrine asserted in CA | Doctrine unavailable; pursue DTSA or specific misappropriation |
| Industry ban missed (physician, broadcaster, low-wage) | Check industry-specific statutes per state |
| Failure to issue CA SB 699 notice to current/former employees with void covenants | Issue notice; penalties for non-compliance |
| Fabricated cites | Use `[CITE: ...]` placeholders |
