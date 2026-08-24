# Family Law — Self-Advocacy (Litigant-Facing Preparation)

Prompts for an **individual handling their own side** of a divorce or custody matter — self-represented, or represented but organizing their own materials. They help you **organize, document, and prepare**: build chronologies, inventory evidence and finances, structure factual responses to allegations, prepare for hearings and evaluations, and assemble a clean handoff package for your attorney.

> ## Read This First — What These Prompts Are (and Are Not)
>
> **They organize, document, and prepare your own information.** They do **not** give legal advice, legal strategy, or legal filings, and they are **not** a substitute for a licensed attorney or your jurisdiction's family law. They will **not** predict court outcomes, assess how strong your case is, cite or invent statutes or case law, tell you what to file, or claim your materials "prove" anything. Those questions are **routed to your attorney.**
>
> **This is the one subsection of `domain-legal/` that inverts the domain's attorney-only, disclaimer-free convention.** The rest of `domain-legal/` is written for practitioners and deliberately omits disclaimers. This subsection is written for a **layperson**, in plain language, with an explicit and load-bearing not-legal-advice boundary.

## Conventions (every prompt in this set)

- **Audience:** a layperson preparing their own side. Plain language, second person.
- **Required jurisdiction input.** Family-law standards, factor lists, disclosure forms, and procedure **vary by state/country and change over time.** Any legal concept is rendered as plain-language literacy flagged *confirm with counsel for your jurisdiction.*
- **No fabrication of facts.** These prompts organize **only your own information**. They never invent facts, dates, documents, witnesses, dollar amounts, or events; never characterize or attribute motive to the other party; never coach you to exaggerate, manufacture, or provoke. Missing items are flagged as **gaps to obtain** (`[NEED DOCUMENT:]`, `[NEED DATE:]`), never filled with assumptions.
- **Every fact dated and sourced; neutral tone throughout.** Neutral, sourced records are more credible and more useful to counsel than argument.
- **Child's needs, not the other parent's flaws.** Where children are involved, everything is framed around the children's stability and routine.
- **Mandatory Safety Block.** Abuse, domestic violence, stalking, threats, or a child-safety emergency → stop and use the safety pathway: **National DV Hotline 1-800-799-7233 · Childhelp 1-800-422-4453 · 988 Suicide & Crisis Lifeline · 911** (US). Work through counsel/an advocate. Documentation supports but never replaces protective action.
- **Verification + false-positive block** end every prompt (jurisdiction flagged; facts dated and sourced; neutral; no characterization; no outcome prediction; no invented standards; legal questions routed; safety screened).
- **File naming:** `legalprep_{function}.md`.

## File Map

**Anchor / handoff**
| File | Use |
|---|---|
| `legalprep_attorney_handoff_brief.md` | **Flagship** — assemble your whole case into one clean package for your lawyer |
| `legalprep_attorney_consultation_question_builder.md` | Prioritized questions to get the most from a (paid) consultation |

**Case organization & evidence**
| File | Use |
|---|---|
| `legalprep_case_chronology_builder.md` | Neutral, dated master timeline of the relationship and disputed events |
| `legalprep_evidence_inventory_organizer.md` | Sourced, labeled evidence/exhibit index mapped to issues |
| `legalprep_communication_record_compiler.md` | Compile texts/emails/app messages into a clean dated record |
| `legalprep_incident_documentation_organizer.md` | Turn a recalled event into a factual, source-anchored record |
| `legalprep_witness_and_source_map.md` | Match witnesses and documents to the facts they corroborate |

**Financial preparation**
| File | Use |
|---|---|
| `legalprep_financial_disclosure_organizer.md` | Organize income/assets/debts into the categories a disclosure will need |
| `legalprep_asset_and_debt_inventory.md` | Complete marital/separate asset & debt worksheet with document tracking |
| `legalprep_monthly_budget_and_expense_worksheet.md` | Household budget for support/needs discussions |
| `legalprep_financial_document_gathering_checklist.md` | Tailored checklist of financial documents to collect |

**Responding & defending**
| File | Use |
|---|---|
| `legalprep_allegation_response_organizer.md` | Answer allegations with facts and evidence, point by point |
| `legalprep_my_account_factual_statement.md` | Neutral first-person factual account for your attorney (not a sworn statement) |
| `legalprep_concerns_about_other_party_organizer.md` | Organize genuine concerns into a sourced, non-inflammatory record for counsel |

**Hearing / court / process prep**
| File | Use |
|---|---|
| `legalprep_hearing_preparation_organizer.md` | Prepare for an upcoming hearing: what to bring, points, questions for counsel |
| `legalprep_testimony_practice_factual_recall.md` | Practice answering factual questions truthfully and calmly (roleplay) |
| `legalprep_deposition_preparation_organizer.md` | Orient to a deposition; organize your facts and questions for counsel |
| `legalprep_court_process_explainer.md` | Plain-language map of the family-court process and roles |
| `legalprep_mediation_preparation_organizer.md` | Organize priorities and supporting facts before mediation/settlement |
| `legalprep_post_mediation_follow_up_organizer.md` | Capture a mediation session: resolved vs. open, commitments, documents, next steps |
| `legalprep_mediation_agreement_review_organizer.md` | Understand a draft mediation agreement and build attorney questions before signing |

**Working with evaluators**
| File | Use |
|---|---|
| `legalprep_custody_evaluation_preparation_organizer.md` | Prepare for a custody evaluation / GAL interview and home visit |
| `legalprep_best_interests_factor_self_map.md` | Map your facts to the general best-interests factor categories |

## How These Compose — the "Organize → Hand Off" Pipeline

```
chronology + evidence inventory + communication/incident records
        + financial disclosure organizer + asset/debt inventory
        + allegation response + best-interests self-map
                              ↓
        legalprep_attorney_handoff_brief.md   →   your attorney
                              ↓
   hearing / deposition / custody-evaluation / mediation prep
                              ↓
   post-mediation follow-up + agreement review (before signing)
```

## Where These Route (boundaries)

- **Legal advice, strategy, citations, outcome prediction, filings** → your attorney. The attorney-side counterparts live in `../divorce/` and `../custody/` (your lawyer's tools).
- **The emotional and relational side of separation and co-parenting** (telling the kids, two-homes adjustment, BIFF messaging, high-conflict co-parenting) → `domain-parenting/caregiver-facing/{divorce,custody,co-parenting}/`. Those sets intentionally refuse legal-case prep and point here for it.
- **An active safety emergency** → the Safety Block pathway, an advocate, and your attorney — not a document.
