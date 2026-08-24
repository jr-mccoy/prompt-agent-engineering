---
title: "Marital & Separate Asset and Debt Inventory Worksheet"
category: legalprep
description: "Help a self-represented or self-organizing divorce litigant build a complete inventory of their own assets and debts — description, approximate value, title/holder, acquisition date and method, and supporting document — with a column for the user's own notes about marital vs. separate character, explicitly flagged as a legal determination for counsel. Organizes the user's own information only. Does NOT characterize property, value assets, predict outcomes, or give legal or tax advice. Not legal advice."
techniques:
  - DS-01
  - DS-21
  - QA-01
  - NE-23
difficulty: intermediate
intended_use: model-testing
tags:
  - legal
  - family-law
  - self-represented
  - divorce
  - asset-inventory
  - debt-inventory
  - property-characterization
  - documentation
updated: "2026-06-05"
related_prompts:
  - domain-legal/family-self-advocacy/legalprep_financial_disclosure_organizer.md
  - domain-legal/family-self-advocacy/legalprep_attorney_handoff_brief.md
  - domain-legal/family-self-advocacy/legalprep_financial_document_gathering_checklist.md
  - domain-legal/divorce/legal_marital_property_characterization_analysis.md
---

**Purpose:** Help you build a thorough, well-organized inventory of every asset and debt you know about — yours, joint, and those you believe may be in your spouse's name — so your attorney has a complete picture for characterization, valuation, and division discussions. For each item it captures: description, approximate value (your own figure), title/account holder, acquisition date and method, and the supporting document. It includes a column for your own notes about whether you believe an item is marital, community, or separate — but that column is explicitly flagged as your understanding only, not a legal determination. It organizes **your own information** — it does **not** characterize property, value assets, predict outcomes, draft filings, or give legal or tax advice.

**When to use:** You are building the financial foundation before your first (or next) attorney meeting; you want a single-document inventory of all assets and debts before the disclosure stage; you are compiling the information your attorney will need to advise on characterization and division; you need a clean record to cross-reference with financial statements.

**When NOT to use:** You want to know whether a specific asset is marital or separate → that is a legal determination that depends on your state's law; bring this inventory to your attorney (see `domain-legal/divorce/legal_marital_property_characterization_analysis.md`). You want to value a business or pension → that requires a professional expert; flag it here for counsel. There is an active safety emergency → Safety Block first.

---

## Safety Block

Stop and use a different pathway if:
- There is domestic violence, threats, stalking, financial abuse, or coercive control → National Domestic Violence Hotline 1-800-799-7233 (US). Asset gathering in a coercive-control situation carries physical safety risk; work through counsel or a domestic-violence advocate to identify and access records safely — do not confront anyone.
- A child is unsafe → Childhelp National Child Abuse Hotline 1-800-422-4453 (US); emergencies 911. Report and route to your attorney.
- You or a child is in crisis → 988 Suicide & Crisis Lifeline (US).

This prompt is educational support for organizing your own records. It is not a substitute for legal, financial, or safety services.

---

## Scope Boundary — Read First

This **organizes an asset and debt inventory from your own knowledge and records**. It is **not legal advice, not a legal filing, not tax advice, and not a substitute for your attorney or a financial expert.** Whether any asset or debt is marital, community, or separate property is a **legal determination that depends on your state's law and the specific facts** — this prompt records your acquisition facts and your own understanding, then flags characterization *confirm with counsel.* It will **not** resolve characterization, value any asset or business (flag `[NEED VALUATION]`), predict how property will be divided, cite statutes or formulas, or fill documentation gaps with assumptions. The purpose of this inventory is to give your attorney everything they need to do those jobs. "If it's not on paper, it's not disclosed" — gather every supporting document and keep secure copies.

---

## Core Principles

1. **Inventory, don't characterize.** Record every fact about acquisition — date, method, source of funds — and note your understanding in the designated column. Resolution is for counsel.
2. **Every item gets a source document.** A title deed, account statement, loan agreement, or appraisal. If you don't have one yet, flag it `[NEED DOCUMENT:]`.
3. **Approximate values are yours to supply.** If you have a figure from a recent statement, use it. If not, use `[NEED VALUATION]` — never invent one. Business and pension valuations always require experts (*confirm with counsel*).
4. **Acquisition story matters.** When it was acquired, how (purchased, inherited, gifted, pre-marital), and with whose funds — these facts are what your attorney uses to advise on characterization.
5. **Debts belong on the inventory too.** Who owes it, when it was incurred, whose name it is in, and the current balance — all of these matter for the financial picture.
6. **Questions for counsel go in the notes column.** Not a legal conclusion — a flag to discuss.
7. **Gather early, keep copies.** Collect statements and titles before circumstances change; secure digital and paper backups outside the shared household if safety is a concern.

---

## Your Input

- **Your jurisdiction (state/country):** [required — characterization rules vary significantly; community-property and equitable-distribution states operate differently]
- **Date of marriage:** [required — affects what counts as acquired "during the marriage"]
- **Date of separation (if applicable):** [date or "not yet separated" — may affect the cutoff for marital acquisition in your state; *confirm with counsel*]
- **Your role in the case:** [petitioner / respondent / not yet filed]
- **Do you have a prenuptial or postnuptial agreement?:** [yes / no / unsure — flag for counsel]
- **Assets you are aware of (yours, joint, and spouse's):** [list broadly — real estate / accounts / retirement / vehicles / business / personal property / other]
- **Debts you are aware of:** [mortgage / car loans / credit cards / student loans / other]
- **Documents you have in hand:** [list, or "none yet"]
- **Any safety or access concern about gathering records?:** [if yes → Safety Block; organize through counsel/advocate]

---

## Constraints

**Must:**
- Require jurisdiction and date of marriage; use only facts the user supplies.
- Include an "your understanding" column for marital/separate notes, explicitly flagged as the user's own belief, not a legal determination, and flagged *confirm with counsel.*
- Flag every missing document `[NEED DOCUMENT:]` and every missing value `[NEED VALUATION]`.
- Note acquisition date and method for each asset as a factual record, without resolving characterization.
- Flag business-interest and pension valuations as requiring a professional expert.
- Route all characterization and division questions to the attorney.
- Keep tone neutral; never attribute motive to the other party.

**Must Not:**
- Characterize any asset or debt as marital or separate — that is a legal determination.
- Value any asset, business, pension, or real property — use the user's figure or `[NEED VALUATION]`.
- Predict how a court will divide assets or debts.
- Cite or invent state statutes, division formulas, or presumption rules.
- Draft any filing, declaration, or sworn statement.
- Advise the user to take, move, or liquidate any asset.
- Attribute motive to the other party (e.g., "transferred to hide it") — note the facts and flag for counsel.

---

## Instructions

### Stage 1 — Screen for Safety and Frame the Inventory
Screen for any safety or access concern (route to Safety Block). State the jurisdiction and date of marriage. Confirm the inventory's purpose: a complete, neutral record of assets and debts for the attorney's use in characterization, valuation, and division work.

### Stage 2 — Note the Marriage Date and Separation Date
Record both dates as the user provides them. Note that these dates are factually significant in property characterization under most state laws — the exact legal effect *confirm with counsel for your jurisdiction.*

### Stage 3 — Asset Inventory
Organize assets into categories: real property; bank/financial accounts; investment and brokerage accounts; retirement and pension accounts; vehicles; personal property of significant value; business interests; intellectual property and other intangibles; life insurance with cash value. For each item:
- Description (address, institution, make/model, etc.)
- Title holder or account holder
- Approximate current value (user's figure, or `[NEED VALUATION]`)
- Acquisition date and method (factual — e.g., "purchased 2018, joint funds" / "inherited from parent 2015" / "owned prior to marriage")
- User's own understanding (marital / separate / partly both — flagged *confirm with counsel*)
- Supporting document and status (Have / `[NEED DOCUMENT:]`)

### Stage 4 — Debt Inventory
Organize debts into categories: mortgage(s); home equity; vehicle loans; student loans; credit cards; personal loans; business debts; tax liabilities; other. For each item:
- Creditor and account type
- Account holder(s) / co-signer(s)
- Current balance (user's figure from most recent statement, or `[NEED STATEMENT:]`)
- Monthly payment
- When incurred (date or approximate period)
- User's own understanding (marital / separate — *confirm with counsel*)
- Most recent statement and status

### Stage 5 — Questions for Counsel Re: Characterization
Compile a list of items where the user has a question, a mixed-acquisition history (e.g., pre-marital home refinanced during marriage), or uncertainty about how to categorize. These go to counsel — they are not resolved here.

### Stage 6 — Documentation Gaps
Consolidate all `[NEED DOCUMENT:]`, `[NEED STATEMENT:]`, and `[NEED VALUATION]` flags into one list. Note how to obtain each (institution, employer, county records office, etc.). Cross-reference `legalprep_financial_document_gathering_checklist.md`.

### Stage 7 — Package and Route
Produce the inventory labeled "ASSET & DEBT INVENTORY — NOT A LEGAL FILING." Close by routing characterization, valuation, and division questions explicitly to the attorney and, where applicable, to a valuation expert. Reference `domain-legal/divorce/legal_marital_property_characterization_analysis.md` as the attorney-side tool for the legal characterization work.

---

## Output Format

```markdown
# Asset & Debt Inventory — [Your name] · [jurisdiction]
Date of marriage: [date] · Separation date: [date or N/A]
Prepared by [you], [date].
ASSET & DEBT INVENTORY — NOT A LEGAL FILING.
Records my own knowledge. Does NOT characterize property or value assets — those are for counsel and experts.

---

## ASSET INVENTORY

### Real Property
| Address / description | Title holder | Approx. value (my figure) | Acquired (date / method) | My understanding (not legal advice) | Source document | Status |
|---|---|---|---|---|---|---|
| [Address] | [names] | $[x] | [date / purchased jointly] | Believe marital — *confirm with counsel* | Deed; mortgage stmt | Have / [NEED DOCUMENT:] |
| [Address] | [names] | [NEED VALUATION] | [date / pre-marital] | Believe separate — *confirm with counsel* | Deed | [NEED DOCUMENT:] |

### Bank & Financial Accounts
| Institution | Account type | Holder(s) | Last 4 | Approx. balance | Balance date | Acquired | My understanding | Source document | Status |
|---|---|---|---|---|---|---|---|---|---|
| [Bank] | Checking | [names] | [xxxx] | $[x] | [date] | [opened during marriage] | Marital — *confirm w/ counsel* | Statement | Have |

### Retirement & Pension Accounts
| Institution | Type | Holder | Approx. balance | Statement date | Acquired / contributions | My understanding | Source document | Status |
|---|---|---|---|---|---|---|---|---|
| [Institution] | 401(k) | [name] | $[x] | [date] | [opened pre-marital; contributions during marriage] | Mixed — *confirm w/ counsel* | [NEED STATEMENT:] | — |

### Investment Accounts
| Institution | Type | Holder(s) | Approx. value | Date | Acquired | My understanding | Source document | Status |
|---|---|---|---|---|---|---|---|---|

### Vehicles
| Year / Make / Model | Title holder | Approx. value | Acquired (date/method) | My understanding | Document (title/loan) | Status |
|---|---|---|---|---|---|---|

### Personal Property (significant value)
| Description | Approx. value | Holder | Acquired | My understanding | Document | Status |
|---|---|---|---|---|---|---|

### Business Interests
| Business / entity | Ownership % | Approx. value | Acquired | My understanding | Document | Status |
|---|---|---|---|---|---|---|
| [Name] | [x%] | [NEED VALUATION — EXPERT REQUIRED] | [date / how] | *confirm w/ counsel* | Tax return / K-1 | [NEED:] |

---

## DEBT INVENTORY

| Creditor | Type | Holder(s) | Balance | Monthly pmt | When incurred | My understanding | Statement date | Status |
|---|---|---|---|---|---|---|---|---|
| [Lender] | Mortgage | [names] | $[x] | $[x] | [date] | Marital — *confirm w/ counsel* | [date] | Have |
| [Issuer] | Credit card | [name] | $[x] | $[x] | [period] | [Marital / unsure] — *confirm w/ counsel* | | [NEED STATEMENT:] |

---

## QUESTIONS FOR COUNSEL RE: CHARACTERIZATION

- [Item]: [the specific question — e.g., "pre-marital home, refinanced 2020 with joint funds — how does this affect characterization?"]
- [NEED VALUATION — EXPERT: business/pension/real property]

---

## DOCUMENTATION GAPS (to obtain)

| Item | Gap | How to obtain |
|---|---|---|
| [NEED DOCUMENT: deed for [address]] | Verify title holder | County recorder's office |
| [NEED STATEMENT: 401(k) balance] | Asset disclosure | Request from plan administrator |

---

## Note for your attorney
This inventory records my own knowledge and acquisition facts. Please advise on:
- Characterization of each flagged item as marital/community or separate. *Confirm with counsel for your jurisdiction.*
- Whether a prenuptial/postnuptial agreement affects any item. *Confirm with counsel.*
- Expert valuation for business, pension, and real property items.
- Any discovery needed for assets not yet documented.
*NOT A LEGAL FILING.*
```

---

## Verification

- [ ] Jurisdiction and date of marriage captured?
- [ ] Every asset has acquisition date/method recorded (factually, not characterized)?
- [ ] "My understanding" column present and flagged *confirm with counsel* on every row?
- [ ] No property characterized as marital or separate by the prompt — user's note only?
- [ ] No asset valued without a user-supplied figure; `[NEED VALUATION]` used where absent?
- [ ] Business and pension valuations flagged as requiring expert?
- [ ] Debt inventory includes holder, balance, and date incurred?
- [ ] Gaps consolidated into a documentation list?
- [ ] All characterization, valuation, and division questions routed to attorney?
- [ ] No filing, declaration, or advice on moving/liquidating assets?
- [ ] Safety/access concern screened and routed?

---

## False-Positive Prevention

| ❌ Don't | ✅ Do |
|---|---|
| "This is a marital asset" | Record acquisition facts; note user's understanding; flag *confirm with counsel* |
| "That inheritance is separate property" | Record "inherited from [person], [date]"; flag *confirm with counsel* |
| "Your spouse probably transferred assets to hide them" | Note factual observation; flag for attorney; never accuse or instruct surveillance |
| Supply a value for a business or pension | Enter `[NEED VALUATION — EXPERT REQUIRED]` |
| "Under [state] law, pre-marital property is yours" | Note acquisition date; flag legal standard *confirm with counsel* |
| Advise on taking, moving, or liquidating any asset | Never — route any such question to the attorney immediately |
| Fill a missing balance or value with an estimate | Flag `[NEED STATEMENT:]` or `[NEED VALUATION]` |
| Draft any court document from this inventory | Inventory feeds the attorney's drafting; it is not a filing |

---

## Adaptations

**By asset profile:**
- **Long marriage with commingled assets:** Note each item's acquisition story fully; flag commingling questions (e.g., separate funds deposited into a joint account) for counsel — this can affect characterization significantly; *confirm with counsel.*
- **Business owner:** Business-interest row is critical; flag all records needed (tax returns, operating agreement, K-1s) and note that expert valuation is required; pair with `legalprep_financial_document_gathering_checklist.md`.
- **Inherited or gifted assets:** Note the source (from whom, when, and whether kept separate or commingled); flag for counsel — commingling can affect separate-property status in many states; *confirm with counsel.*
- **Retirement accounts with pre- and post-marital contributions:** Note what the user knows about when contributions were made; flag the mixed-acquisition question for counsel.

**By situation/profile:**
- **Prenup or postnup:** Flag each asset that may be governed by the agreement; route interpretation to counsel.
- **Safety / financial-control concerns:** Organize through counsel; keep this document in a safe location the other party cannot access.
- **Short marriage:** Acquisition dates are especially important — many assets may pre-date the marriage; note carefully.

---

## Related Prompts

- `legalprep_financial_disclosure_organizer.md` — organizes the same assets and debts into affidavit-ready categories; this inventory feeds that worksheet.
- `legalprep_financial_document_gathering_checklist.md` — the document collection checklist to source every row in this inventory.
- `legalprep_attorney_handoff_brief.md` — the master case package; Section 5 (finances) pulls from this inventory.
- `domain-legal/divorce/legal_marital_property_characterization_analysis.md` — the attorney-side prompt for the legal characterization work this inventory prepares.
