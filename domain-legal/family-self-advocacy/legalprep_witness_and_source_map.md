---
title: "Witness & Source Map (Match People and Documents to the Facts They Support)"
category: legalprep
description: "Help a self-represented or self-organizing family-law litigant map potential witnesses and documentary sources to the specific facts each could corroborate, and surface gaps where a claimed fact has no support yet. Organizes the user's own knowledge only. Does NOT coach witnesses, advise on whom to call, predict outcomes, or assess evidentiary weight — those are for the attorney. Not legal advice."
techniques:
  - DS-01
  - ST-02
  - QA-01
  - NE-23
difficulty: intermediate
intended_use: model-testing
tags:
  - legal
  - family-law
  - self-represented
  - divorce
  - custody
  - witnesses
  - corroboration
  - documentation
  - evidence
updated: "2026-06-05"
related_prompts:
  - domain-legal/family-self-advocacy/legalprep_attorney_handoff_brief.md
  - domain-legal/family-self-advocacy/legalprep_evidence_inventory_organizer.md
  - domain-legal/family-self-advocacy/legalprep_case_chronology_builder.md
  - domain-legal/family-self-advocacy/legalprep_incident_documentation_organizer.md
  - domain-legal/divorce/legal_divorce_intake_and_case_assessment.md
  - domain-legal/depositions/legal_deposition_outline_witness.md
---

**Purpose:** Help you build a clear map between the facts you assert and the people or documents that could corroborate each one. The output is a matrix: for each fact, which witnesses could speak to it directly, which documents support it, and where the corroboration gap is. Seeing gaps clearly before your first attorney meeting is far more useful than discovering them at a deposition. This organizes **your own knowledge** — it does **not** tell you whom to call as a witness, coach or script witnesses, assess how persuasive a witness will be, or predict what a court will believe. Those decisions belong to you and your attorney.

**When to use:** You have a list of facts you want to establish and you want to map each fact to the evidence that backs it; you are preparing to hand off materials to an attorney and want to show what is corroborated and what still needs support; you have a hearing approaching and want your attorney to see at a glance where the record is strong and where it has holes.

**When NOT to use:** You want to know whom to call as a witness or how to question them → those are strategic decisions for your attorney. You want to coach a witness on what to say → do not. Coaching witnesses to match a narrative is improper; witnesses testify to what they personally know. You want a full exhibit index → use `legalprep_evidence_inventory_organizer.md`. There is an active safety emergency → Safety Block first.

---

## Safety Block

Stop and use a different pathway if:
- There is domestic violence, threats, stalking, or a protective/restraining order → National Domestic Violence Hotline 1-800-799-7233 (US). Keep records securely; work through counsel/advocate; do not confront anyone.
- A child is being abused or is unsafe in either home → Childhelp National Child Abuse Hotline 1-800-422-4453 (US); emergencies 911. Report and route to your attorney immediately.
- You or a child is in crisis → 988 Suicide & Crisis Lifeline (US).

This prompt is educational support for organizing your own records. It is not a substitute for legal, safety, or clinical services.

---

## Scope Boundary — Read First

This **maps your own knowledge of potential witnesses and sources to the facts you assert**. It is **not legal advice, legal strategy, a legal filing, or a substitute for an attorney or your jurisdiction's family law.** It will **not** tell you whom to call as a witness, how to question them, assess their credibility or persuasiveness, predict how a court will weigh their testimony, cite or invent evidentiary rules or cases, or advise you to contact any witness without your attorney's guidance. Whether and how to use witnesses, disclose them, depose them, or call them at trial **vary by state and country and change over time** and are entirely for your attorney. Where a legal concept (competency, foundation, hearsay) appears, it is explained in plain language and flagged *confirm with counsel for your jurisdiction.* Do **not** contact or coach potential witnesses without your attorney's direction.

---

## Core Principles

1. **Match fact to source, not source to conclusion.** The map starts with a specific factual assertion ("child was at my home on [date]") and asks what corroborates it — not the reverse.
2. **A witness can only corroborate what they personally observed.** A person's value as a witness is limited to their first-hand knowledge. The map notes what each person actually observed — not what they believe or have been told.
3. **Do not coach witnesses.** Recording that a witness exists and what they observed is organizing information. Telling a witness what to say, how to frame it, or what to emphasize is improper and can harm your case. Every witness testifies to their own independent knowledge.
4. **Gaps in corroboration are information, not emergencies.** A fact with no documentary or witness support is a gap to discuss with your attorney — not a prompt to manufacture support.
5. **If it is not on paper, it is not yet disclosed.** Documentary sources anchor facts with contemporaneous evidence; witness memory is subject to challenge. Where a document could exist, flag it.
6. **Neutral toward all witnesses.** The map identifies potential witnesses neutrally; it does not assess loyalty, credibility, or reliability — those are your attorney's domain.
7. **The attorney decides whom to call.** The map is a menu; selecting from it is counsel's job at trial or in declarations.

---

## Your Input

- **Your jurisdiction (state/country):** [required]
- **Matter type:** [divorce / custody / both]
- **Key facts you need to establish:** [list each fact you assert — be specific and factual, e.g., "Child was at my home consistently from [date] to [date]," "I paid all household expenses from [account] during [period]"]
- **Potential witnesses you can identify:** [for each: name/initials, relationship to you, what they personally observed or experienced]
- **Documents you have:** [list — or reference your evidence inventory if already compiled]
- **Known corroboration gaps:** [facts you assert that currently have no document or witness support]
- **Any witnesses you are uncertain about (bias, reliability)?:** [flag for attorney review — do not assess here]
- **Any safety dimension?:** [if yes → Safety Block]

---

## Constraints

**Must:**
- Require the jurisdiction; build the map from only the facts and knowledge the user supplies.
- Start each row with a specific factual assertion; map witnesses and documents to it.
- Limit witness entries to what each person personally observed — label clearly.
- Flag every corroboration gap as `[GAP: no witness/document yet]`.
- Keep tone neutral toward all witnesses; flag credibility/bias questions for attorney review without assessing them.
- Route all "whom to call," strategy, and filing questions to the attorney.
- Explicitly warn against contacting or coaching witnesses without attorney direction.

**Must Not:**
- Assess witness credibility, persuasiveness, or reliability.
- Tell the user whom to call as a witness or in what order.
- Coach or script any witness's expected testimony.
- Assess the evidentiary weight of any source or claim the map "proves" anything.
- Characterize the other party or attribute motive.
- Cite or invent evidentiary rules, cases, or legal standards.
- Fill corroboration gaps with assumption, inference, or invented sources.

---

## Instructions

### Stage 1 — Screen for Safety and Frame the Map
Screen for any safety dimension (route to Safety Block). Restate the matter type and jurisdiction. Confirm the boundary: this maps facts to potential sources; what to do with that map is for the attorney. State explicitly: do not contact or coach any potential witness without attorney direction.

### Stage 2 — List and Clarify the Facts to Establish
Work through the user's list of factual assertions. Sharpen any vague assertion into a specific, dated, factual claim. Strip characterizations: "he is a bad parent" becomes individual specific facts like "child missed [X] school days during other parent's parenting time, [date range]."

### Stage 3 — Map Witnesses to Facts
For each potential witness the user identifies, note: (a) their relationship to the user; (b) the specific facts they personally observed (limit to direct observation only); (c) how they came to be in a position to observe those facts (were present at X on date Y). Note any credibility or bias flags the user raises — do not assess them; flag for attorney.

### Stage 4 — Map Documents to Facts
For each fact, list the documentary sources from the user's evidence inventory (or their description) that support it. Note the document type, date, and what it shows factually. Flag any fact that has no documentary corroboration.

### Stage 5 — Build the Corroboration Matrix
Assemble the map into a matrix: Fact → Witnesses (with what they observed) → Documents (with what they show) → Gap (if any). Each row is one factual assertion.

### Stage 6 — Summarize the Gaps
Produce a standalone gap list: facts with no witness, facts with no document, and facts where the only support is the user's own assertion. These are the attorney's priority items for discovery, declaration, or witness outreach.

### Stage 7 — Package and Close
Assemble the full map under the handoff header. Close with a reminder that contacting or preparing witnesses is the attorney's domain; route all witness-selection and strategy questions to counsel.

---

## Output Format

```markdown
# Witness & Source Map — [Your name] · [matter type] · [jurisdiction]
Compiled by [you], [date]. FOR YOUR ATTORNEY — NOT A LEGAL FILING.
Does NOT assess witness credibility, advise whom to call, or predict outcomes.
⚠ Do NOT contact or coach any listed witness without your attorney's direction.

## Corroboration Matrix
| Fact (specific, dated) | Potential Witness(es) — what they observed directly | Supporting Document(s) — what they show | Gap |
|---|---|---|---|
| Child resided primarily with me from [date] to [date] | [Neighbor — initials]: observed child at my home daily during [months]; [Teacher — initials]: child's school enrolled at my address [date] | School enrollment letter [date]; lease [date] | — |
| Other party missed scheduled pick-up on [date] | [Babysitter — initials]: present at my home at scheduled exchange time; observed other party did not arrive | Text to other party sent [time] that day (no response); co-parenting app message [date/time] | [NEED DOCUMENT: app export for that date] |
| Joint account [XXXX] balance was $X on [date] | — | Bank statement [date] | No witness to this financial fact; document is the primary source |
| [Fact with no support yet] | [GAP: no witness identified] | [GAP: no document yet] | ⚠ Discuss with attorney — currently unsupported |

## Potential Witness Index
| Witness (initials/role) | Relationship to me | Facts they could speak to (first-hand only) | Attorney Flag |
|---|---|---|---|
| [Neighbor — initials] | Neighbor for [X] years | Observed child at my home regularly; present for [specific incident on date] | — |
| [Teacher — initials] | Child's teacher [school year] | Child's school attendance, homework completion, behavioral observations during [period] | — |
| [Friend — initials] | Personal friend | ⚠ Has known me throughout marriage; may have perceived partiality — flag for attorney | ⚠ Flag: credibility/bias — confirm with counsel |

## Corroboration Gaps (priority items for attorney)
- [Fact: X] — no witness; only my own assertion. Options: document request, declaration, discovery.
- [Fact: Y] — witness identified but no document anchor; consider request for [record type].
- [Fact: Z] — both witness and document available; confirm production status with attorney.

---
For my attorney: please advise on whom to contact, how to disclose witnesses,
what discovery to use for gaps, and how to use this map.
⚠ I have NOT contacted or coached any witness listed above.
*Confirm with counsel for your jurisdiction.*
```

---

## Verification

- [ ] Jurisdiction captured and legal concepts flagged *confirm with counsel*?
- [ ] Every fact specific, dated, and factual (not characterizations)?
- [ ] Each witness entry limited to their first-hand observations only?
- [ ] No coaching, scripting, or assessment of witness credibility?
- [ ] Documents mapped to facts factually (what they show, not what they "prove")?
- [ ] Corroboration gaps flagged `[GAP:]`; not filled with assumption or invented sources?
- [ ] No characterization of or motive attributed to the other party?
- [ ] No assessment of evidentiary weight or outcome prediction?
- [ ] Explicit warning included: do not contact or coach witnesses without attorney direction?
- [ ] All witness-selection, strategy, and filing questions routed to the attorney?
- [ ] Any safety dimension screened and routed?

---

## False-Positive Prevention

| ❌ Don't | ✅ Do |
|---|---|
| "My neighbor will be a great witness for custody" | Note what neighbor personally observed; credibility assessment routes to counsel |
| Coach a witness: "Tell them you saw the child every day" | Record what the witness independently observed; witnesses testify to their own knowledge |
| "This witness corroborates that he's an unfit parent" | Map the witness to specific factual assertions; legal conclusions route to attorney |
| List a fact with no support and hope the gap isn't noticed | Flag every unsupported fact `[GAP:]`; your attorney needs the honest picture |
| "Under [state] rules, this witness qualifies as an expert" | Do not classify witnesses legally; flag for attorney review |
| Use a witness to fill a gap you have no real support for | Gaps are discussion items for counsel, not prompts to manufacture corroboration |
| Contact potential witnesses before attorney review | Include warning ⚠ in every output; do not contact witnesses without counsel direction |
| Combine "what they observed" with "what they believe" | Limit witness entries to direct observation; belief/opinion routes to counsel |

---

## Adaptations

**By posture:**
- **Pre-filing:** Focus on Stage 6 (gaps) — knowing which facts are unsupported before filing is the highest-value output.
- **Discovery open:** Align the gap list with discovery requests already served; flag each gap against what has been requested and received.
- **Hearing imminent:** Narrow the matrix to the issues on for the hearing; pair with `legalprep_evidence_inventory_organizer.md` to confirm every relevant fact has an exhibit number.

**By situation/profile:**
- **Custody-heavy:** Expand the witness index with teachers, pediatricians, coaches, and childcare providers — anyone who directly observed the child's routine, school engagement, or home stability. Each entry is limited to their observations.
- **Finance-heavy:** Documentary sources dominate; witness entries are sparse and limited to people present at specific financial events. Flag financial documents in the evidence inventory.
- **High conflict:** Keep every entry factual and scrupulously neutral; flag any witness the user suspects may be hostile or conflicted for attorney review; do not contact them.
- **Possible expert witnesses (valuators, custody evaluators, doctors):** Note the category and the factual question they might address; whether to retain or call an expert is entirely for counsel — do not approach experts without attorney direction.

---

## Related Prompts

- `legalprep_attorney_handoff_brief.md` — this witness/source map informs the evidence and questions sections of the handoff package.
- `legalprep_evidence_inventory_organizer.md` — the documentary sources in this map are cataloged in full detail there.
- `legalprep_case_chronology_builder.md` — the facts in this map correspond to rows in the master timeline; gaps here often reveal gaps there.
- `legalprep_incident_documentation_organizer.md` — each incident record names witnesses who appear in this map.
- `../discovery/legal_discovery_deposition_fact_witness_outline.md` — the attorney-side tool for preparing to depose the witnesses identified here.
