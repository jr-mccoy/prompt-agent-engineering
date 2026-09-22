---
title: "Business Insurance Coverage Review — Exposures First, Then the Gaps Between Policies"
category: finance/risk-management
description: "Review commercial insurance against actual exposures: an exposure inventory built before any policy is opened, coverage mapped exposure by exposure, the gaps between policies where claims are declined, limits tested against a realistic worst case, exclusions and conditions read for the ones that void cover, and a retained-risk statement. Refuses reviews that start from the policy schedule and reviews that report limits without testing them."
techniques:
  - RT-05
  - CM-02
  - QA-04
  - QA-18
  - OC-03
difficulty: advanced
tags:
  - insurance
  - commercial-lines
  - coverage-gaps
  - risk-transfer
  - retained-risk
  - small-business
updated: "2026-09-22"
related_prompts:
  - domain-risk/risk_appetite_statement.md
  - domain-risk/risk_business_continuity_plan.md
  - domain-finance/personal-finance-planning/finance_insurance_needs_analysis.md
---

# Business Insurance Coverage Review

**Objective:** Establish what a business is actually exposed to, then check what is
covered — in that order. Output: an exposure inventory built **before** any policy is
opened, coverage mapped exposure by exposure, the gaps *between* policies where claims
get declined, limits tested against a realistic worst case rather than reported, the
exclusions and conditions that void cover, and a statement of retained risk that feeds
the risk appetite. Reviews that start from the policy schedule are refused, as are
reviews that report a limit without testing it.

**When to Use:**
- Renewal is approaching and the broker has sent last year's schedule to re-sign.
- A client, landlord, lender or platform requires evidence of specific cover.
- The business has changed — new premises, staff, jurisdiction, product, or a first
  employee — and nobody has revisited the policies.
- A claim was declined and you want to know what else is exposed the same way.

**Scope note.** This domain's roadmap positions it as institution-grade practitioner
finance. This prompt is deliberately the small-business and owner-managed exception,
following the precedent already set in-domain by `../tax-planning/solo_dev_tax_strategy.md`
and `../personal-finance-planning/solo_dev_financial_planning.md`. A large enterprise
with a captive insurer and a risk-management function needs a different instrument.

**When NOT to use:**
- You need **personal** lines — life, income protection, household, personal health —
  that is `../personal-finance-planning/finance_insurance_needs_analysis.md`. Different
  policies, different tax treatment, different decision.
- You need to compare specific quoted policies as prose for a client — that is
  `../../domain-professional-writing/domain-specific/domain_writing_insurance_comparison.md`.
- You need counterparty credit or hedging — that is
  `finance_counterparty_risk_assessment.md` and `finance_hedging_strategy_designer.md`.
- You need the risk register or the appetite statement — those are
  `../../domain-risk/risk_register_builder.md` and
  `../../domain-risk/risk_appetite_statement.md`, which consume this review's retained-risk
  output.

**This is not insurance, legal or tax advice.** Policy wordings, statutory compulsory
cover, and the tax treatment of premiums and proceeds vary by jurisdiction and by
insurer, and two policies with the same name cover different things. This produces an
exposure map and a question list for a broker and, where a wording is contested, a
lawyer. Only the policy document decides what is covered.

---

## Context Gathering

1. **The business**
   - "Legal structure, jurisdictions of operation, revenue, and headcount including
     contractors."
   - "What do you actually do, and what could go wrong for a customer because of it?"
   - "Premises: owned, leased, home, none? Any premises you are contractually
     responsible for?"

2. **Assets and obligations**
   - "Physical assets, and their replacement cost — not book value."
   - "Data you hold about other people."
   - "Contracts requiring you to carry specific cover at specific limits."
   - "Anyone depending on you continuing to trade — a lender, a landlord, a franchise."

3. **Current cover — collected but not read yet**
   - "Every policy, its limits, its excess, and its renewal date."
   - "Any claims in the last five years, and their outcome."

4. **Change since last review**
   - "New products, new markets, new jurisdictions, first employee, first premises,
     first subcontractor, remote staff in another country?"

**Do not open the policy schedule until step 1 is complete.** Reading it first anchors
the review on what is already bought, and the gaps become invisible — which is precisely
the failure this ordering prevents.

---

## Method

### Step 1 — Inventory the exposures, policy-blind

Work through the categories and write down what could actually happen, in this business.

| Exposure | Could it happen here? | Realistic worst case | Frequency |
|---|---|---|---|
| Injury to a member of the public or a visitor | | | |
| Injury to an employee | | | |
| Damage to someone else's property | | | |
| Professional error causing a client financial loss | | | |
| Product defect causing loss or injury | | | |
| Loss of or damage to your own assets | | | |
| Business interruption following any of the above | | | |
| Data breach — your data, and data you hold for others | | | |
| Cyber extortion, funds transfer fraud, social engineering | | | |
| Employment dispute, discrimination or wrongful dismissal claim | | | |
| Director or officer personal liability | | | |
| Key-person absence | | | |
| Contractual liability you have accepted | | | |
| Vehicle use, including personal vehicles used for work | | | |
| Loss of a critical supplier | | | |

The realistic worst case is a number, reasoned. Not the theoretical maximum and not last
year's loss.

### Step 2 — Note compulsory and contractual cover separately

Some cover is not a choice:

- **Statutory compulsory** — in most jurisdictions employer's liability once you have
  employees, and motor cover for vehicles; regulated professions frequently mandate
  professional indemnity at a minimum limit. Confirm what applies to you; this varies
  and this prompt does not know your jurisdiction.
- **Contractually required** — limits and cover types named in client contracts,
  leases, loan covenants or platform terms. Check
  `../../domain-legal/contracts-transactional/legal_subcontractor_flow_down_check.md` if
  you subcontract: cover your contract requires of you must flow down to anyone
  delivering on your behalf.

A contractual requirement you do not meet is a breach independent of whether anything
goes wrong.

### Step 3 — Map coverage onto exposures, and look at the seams

Only now open the schedule.

| Exposure | Policy | Limit | Excess | Basis | Covered? |
|---|---|---|---|---|---|

**Basis** matters more than it looks. *Claims-made* cover responds only while the policy
is live, so cancelling professional indemnity leaves historic work uncovered unless run-off
cover is bought — one of the most expensive and least-known traps for anyone closing or
selling a business. *Occurrence* cover responds to events in the period whenever the claim
arrives.

Then the part the review exists for — **the seams between policies**, where claims are
declined not because cover was absent but because each insurer points at the other:

| Classic seam | What falls through |
|---|---|
| Professional indemnity vs public liability | Advice causing physical injury |
| Cyber vs crime vs PI | Funds transferred after a social-engineering email; each may exclude it |
| Property vs business interruption | Interruption with no physical damage — a supplier outage, a denial of access |
| Product liability vs product recall | The cost of the recall itself, as distinct from injury caused |
| Employer's liability vs employment practices | Stress and harassment claims |
| Own damage vs contractual liability assumed | Liability you accepted in a contract that the policy does not cover |
| Cover territory vs where you operate | Remote staff or clients in a jurisdiction outside the territorial limit |

For each seam, one written question to the broker: **"if this specific scenario happened,
which policy pays?"** A broker who cannot answer in one sentence has found you a gap.

### Step 4 — Test the limits instead of reporting them

A reported limit is a number in a schedule. A tested limit has been compared to a
scenario.

| Exposure | Realistic worst case | Limit | Adequate? | If not, gap |
|---|---|---|---|---|

Three checks that routinely fail:

- **Aggregate versus each-claim.** An aggregate limit is the annual total across all
  claims. Two mid-sized claims can exhaust it, leaving the rest of the year bare.
- **Defence costs inside or outside the limit.** Inside-the-limit defence costs can
  consume most of a small limit before any settlement, and legal costs frequently exceed
  the claim.
- **Reinstatement versus indemnity on property.** Indemnity pays depreciated value;
  replacing the asset costs replacement cost.

And for business interruption: the **indemnity period**. A twelve-month period sounds
generous and is short if rebuilding premises or requalifying a product takes eighteen.

### Step 5 — Read the exclusions and the conditions precedent

Exclusions are expected. **Conditions precedent** are the ones that catch people: they
void cover for reasons unrelated to the loss.

| Condition | What voids cover | Are we compliant? | Evidence |
|---|---|---|---|
| Notification period | Late notification of a claim or circumstance | | |
| Security measures | Alarm not set, MFA not enabled, patching not current | | |
| Subcontractor requirements | Using an uninsured subcontractor | | |
| Disclosure at inception | A material fact not disclosed | | |
| Survey requirements | A risk-improvement condition not completed | | |

Two of these deserve emphasis. Cyber policies increasingly make specific controls —
multi-factor authentication, offline backups, patch currency — conditions rather than
recommendations, and a breach with MFA disabled can be uncovered entirely. And
non-disclosure at inception can void a policy retrospectively: if anything material has
changed since the last renewal, disclose it, in writing, and keep the reply.

### Step 6 — State the retained risk, and route it

Everything uncovered, uninsurable, below the excess, or above the limit is retained —
which means it is a risk the business is carrying deliberately or by accident.

| Retained exposure | Why retained | Worst case | Can we absorb it? | Accepted by |
|---|---|---|---|---|

Route this table into `../../domain-risk/risk_appetite_statement.md` for formal
acceptance and into `../../domain-risk/risk_business_continuity_plan.md`, whose gap list
this directly informs. Insurance is one of four responses to a risk — the others are
avoid, reduce and accept — and a coverage review that never considers reducing the
exposure has only shopped, not managed.

### Step 7 — Produce the broker question list

End with numbered questions, each naming a scenario. Not "do we have enough cover?" but
"a client alleges our advice caused a six-figure loss and sues in Ireland — which policy
responds, is Ireland inside the territorial limit, and are defence costs inside the
limit?"

Specific scenario questions are the only ones that get specific answers, and the answers
belong in writing.

---

## Output Format

```markdown
## Insurance coverage review — [business], [date]

**Structure:** [x] · **Jurisdictions:** [x] · **Revenue:** [x] · **Headcount:** [x incl. contractors]
**Changes since last review:** [list]

### Exposure inventory (built before opening the schedule)
| Exposure | Live here? | Realistic worst case | Frequency |
|---|---|---|---|

### Compulsory and contractual
| Requirement | Source | Limit required | Held? |
|---|---|---|---|

### Coverage map
| Exposure | Policy | Limit | Excess | Basis (claims-made / occurrence) | Covered? |
|---|---|---|---|---|---|

### Seams — one question each to the broker
| Scenario | Candidate policies | Which pays? | Broker answer (written) |
|---|---|---|---|

### Limits tested
| Exposure | Worst case | Limit | Aggregate or each-claim | Defence costs in/out | Adequate? |
|---|---|---|---|---|---|
Property basis: [reinstatement / indemnity] · BI indemnity period: [x] vs realistic recovery [x]

### Conditions precedent
| Condition | Voids cover if | Compliant? | Evidence |
|---|---|---|---|

### Retained risk
| Exposure | Why retained | Worst case | Absorbable? | Accepted by |
|---|---|---|---|---|
→ routed to `risk_appetite_statement.md` and `risk_business_continuity_plan.md`

### Questions for the broker
1. [scenario-specific question]

**Not insurance, legal or tax advice. Only the policy wording decides cover.**
```

---

## Verification

- [ ] The exposure inventory was built before the policy schedule was opened
- [ ] Every realistic worst case is a reasoned number, not a theoretical maximum
- [ ] Compulsory and contractually required cover are identified separately
- [ ] Coverage is mapped exposure by exposure, not policy by policy
- [ ] Every policy's basis (claims-made or occurrence) is recorded, and run-off considered
      where claims-made cover might lapse
- [ ] At least the seven classic seams are checked, each with a scenario question
- [ ] Limits are tested against worst cases, not reported
- [ ] Aggregate-versus-each-claim and defence-costs-inside-or-outside are both checked
- [ ] Property basis and BI indemnity period are checked against realistic recovery time
- [ ] Conditions precedent are listed with a compliance answer and evidence
- [ ] Retained risk is stated and routed for formal acceptance
- [ ] Broker questions name specific scenarios
- [ ] The advice disclaimer is present

**False-positive prevention.** The dominant failure is starting from the schedule. A
review that walks the existing policies confirms what is covered and is structurally
incapable of finding what is not, because absent cover leaves no trace in the document
you are reading. Build the exposure list first, policy-blind. If the inventory is written
after the schedule has been read, it will mirror it.

The second failure is treating a limit as adequacy. £1m of professional indemnity sounds
ample until the exposure is a client's six-figure loss plus defence costs inside the
limit plus a second claim in the same year against an aggregate. The limit is an input to
the adequacy question, not the answer.

The third is ignoring conditions precedent because they read as boilerplate. They are the
mechanism by which a valid-looking claim is declined for a reason unconnected to the
loss — backups not offline, MFA not enabled, a claim notified late, a change not
disclosed. Check compliance and keep the evidence.

The fourth is assuming policy names mean anything. "Cyber" covers materially different
things between insurers, and social-engineering funds transfer is excluded by many cyber
policies, many crime policies and many PI policies simultaneously. Ask the scenario
question and get the answer in writing.

The fifth is buying cover for a risk you should reduce or avoid. Insurance transfers
financial consequence; it does not prevent the event, restore the client relationship, or
satisfy a regulator. If the exposure is reducible at less than the premium, reduce it.

---

## Related

- `../../domain-risk/risk_appetite_statement.md` — where retained risk is formally accepted
- `../../domain-risk/risk_business_continuity_plan.md` — the gap list this informs
- `../../domain-risk/risk_dependency_chain_audit.md` — supplier and key-person exposures
- `../personal-finance-planning/finance_insurance_needs_analysis.md` — the personal-lines counterpart
- `../../domain-legal/contracts-transactional/legal_subcontractor_flow_down_check.md` — cover that must flow down
- `../../domain-professional-writing/domain-specific/domain_writing_insurance_comparison.md` — writing the comparison up
