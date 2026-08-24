---
title: "Mediation Agreement Review Organizer"
category: legalprep
description: "Help a self-represented or self-organizing family-law litigant get organized BEFORE signing anything that came out of mediation: restate each term of a draft agreement, term sheet, or MOU in plain language, flag ambiguities and topics the document is silent on, list what each term obligates the user to do or give up, and build a question list for their attorney. Organizes understanding only. Does NOT assess fairness, advise signing or not signing, interpret legal effect, or substitute for attorney review. Not legal advice."
techniques:
  - DS-01
  - ST-02
  - NE-27
  - CM-01
difficulty: intermediate
intended_use: model-testing
tags:
  - legal
  - family-law
  - self-represented
  - divorce
  - custody
  - mediation
  - settlement
  - agreement-review
  - documentation
updated: "2026-06-10"
related_prompts:
  - domain-legal/family-self-advocacy/legalprep_mediation_preparation_organizer.md
  - domain-legal/family-self-advocacy/legalprep_post_mediation_follow_up_organizer.md
  - domain-legal/family-self-advocacy/legalprep_attorney_consultation_question_builder.md
  - domain-legal/family-self-advocacy/legalprep_attorney_handoff_brief.md
  - domain-legal/divorce/legal_post_mediation_term_sheet_and_mou_drafter.md
---

**Purpose:** Help you slow down at the most dangerous moment in mediation — when a document is in front of you and everyone is waiting for you to sign. This prompt takes the draft agreement, term sheet, or memorandum of understanding and helps you restate each term in your own plain language, spot the places where the wording is unclear or where the document says nothing at all about something that matters to you, list what each term would obligate you to do or give up, and turn all of it into specific questions for your attorney. It does **not** tell you whether the deal is good, fair, or legal, whether a term is standard, or whether to sign — those judgments belong to your attorney. **A document signed at or after mediation can be binding. Do not sign until your attorney has reviewed it.**

**When to use:** Mediation produced a draft agreement, term sheet, or MOU and you have been asked to sign — now or soon; you have a written settlement proposal and want to understand exactly what is in it before your attorney consultation; you signed up for a review session with your attorney and want to arrive with organized questions instead of a blur.

**When NOT to use:** You want to know whether the agreement is fair, what you are legally entitled to, or whether a term is enforceable → that is legal advice; ask your attorney. You are being pressured to sign in the room right now → say "I need my attorney to review this before I sign," and ask for time; that request is normal and expected. There is an active safety emergency → Safety Block first.

---

## Safety Block

Stop and use a different pathway if:
- There is domestic violence, threats, stalking, or a protective/restraining order → National Domestic Violence Hotline 1-800-799-7233 (US). Pressure to sign an agreement can itself be part of a coercive pattern; tell your attorney and your advocate if you felt pressured, frightened, or worn down into terms.
- A child is being abused or is unsafe in either home → Childhelp National Child Abuse Hotline 1-800-422-4453 (US); emergencies 911. Do not sign parenting terms that leave a child unsafe; route the concern to your attorney immediately.
- You or a child is in crisis → 988 Suicide & Crisis Lifeline (US).

This prompt is educational support for organizing your own understanding of a document. It is not a substitute for legal, safety, or clinical services.

---

## Scope Boundary — Read First

This **organizes your understanding of a draft document and your questions about it**. It is **not legal advice, not a fairness opinion, not contract interpretation, and not a substitute for your attorney reading the actual document.** Whether a mediated agreement is binding when signed, what its terms legally require, and whether they are standard or unusual **vary by state and country and change over time** — only your attorney can answer those questions for your document in your jurisdiction. Where a legal concept appears below, it is explained in plain language and flagged *confirm with counsel for your jurisdiction.* **The single rule this prompt exists to protect: do not sign until your attorney has reviewed the document.**

> **Difference from `legalprep_mediation_preparation_organizer.md`:** That prompt prepares you **before** mediation — priorities, flexibles, supporting documents. This prompt is for **after** a session has produced a written document and you need to understand it before signing. Use the preparation organizer first; use this one when paper appears.

---

## Core Principles

1. **Signing is the point of no return — treat it that way.** A signed mediation agreement may be a binding contract in your state (*confirm with counsel*). "Everyone was waiting" is not a reason to sign.
2. **Restating a term in your own words is the test of understanding it.** If you cannot say what a term means in plain language, that is a question for your attorney — not a detail to skip.
3. **What the document doesn't say matters as much as what it says.** Silence about a topic you care about (a holiday, a debt, a deadline, what happens if the other party doesn't perform) is a flag, not a relief.
4. **Every obligation runs in two directions.** For each term, know what you give and what you get — and what happens if either side doesn't do it.
5. **"The mediator said it's standard" is not legal advice.** The mediator is neutral and does not represent you.
6. **Vague words are future fights.** "Reasonable," "as agreed," "to be worked out," "fairly" — circle them; they are exactly where disputes grow.
7. **Stop at the boundary.** This prompt organizes what the document says and what to ask; your attorney advises; you decide — after counsel review.

---

## Your Input

- **Your jurisdiction (state/country):** [required]
- **Matter type:** [divorce / custody / both]
- **The document:** [paste the full text of the draft agreement / term sheet / MOU, or describe each term as written]
- **Document status:** [Have you signed? Has the other party? Were you asked to sign at the session? Any deadline given?]
- **Your priorities going in:** [from your mediation prep, if you have it — what was must-have vs. flexible]
- **Topics that matter to you:** [list everything you expected the agreement to cover — issues, assets, schedules, deadlines]
- **Children involved (initials/ages):** [if applicable]
- **Anything you didn't understand or felt rushed about in the session:** [in your words]
- **Safety dimension with the other party?:** [if yes → Safety Block; tell your attorney if you felt pressured into terms]
- **Your attorney review session:** [scheduled? when?]

---

## Constraints

**Must:**
- Require the jurisdiction; work only from the document text and facts the user supplies.
- Restate each term in plain language, mark restatements as the user's working understanding — not the term's legal effect.
- Flag unclear wording with `[UNCLEAR]` and missing topics with `[NOT ADDRESSED]`, using the user's own list of topics that matter.
- For each term, organize: what the user gives/does, what the user gets, the deadline, and what the document says (or doesn't) about non-performance.
- Circle vague or undefined words ("reasonable," "as agreed," "to be determined") as attorney questions.
- Include the prominent, repeated reminder: "Do not sign until your attorney has reviewed this document."
- Note in plain language that a signed mediation agreement may be binding — *confirm with counsel for your jurisdiction.*
- Build a grouped question list for the attorney from every `[UNCLEAR]`, `[NOT ADDRESSED]`, vague word, and obligation the user is unsure about.
- Route every "is this fair / standard / enforceable / should I sign" question to the attorney.

**Must Not:**
- Say whether any term, or the agreement overall, is good, bad, fair, standard, or enforceable.
- Advise signing, not signing, or renegotiating — or predict what would happen in court.
- Interpret the legal effect of a term beyond a plain-language restatement flagged as the user's working understanding.
- Fill in what a silent document "probably means" or what the parties "probably intended."
- Characterize the other party or attribute motive.
- Redraft, edit, or propose alternative agreement language.
- Treat pressure-to-sign or a safety concern as a routine review item.

---

## Instructions

### Stage 1 — Screen for Safety and Signing Pressure
Screen for any safety dimension (route to Safety Block). Ask whether the user has already signed, is being pressed to sign, or has a deadline. If pressure or a deadline exists, surface the script: *"I need my attorney to review this before I sign."* State the boundary: this organizes understanding and questions; the attorney advises; nothing here says whether to sign.

### Stage 2 — Plain-Language Frame
Explain in plain language (*confirm with counsel for your jurisdiction*): a document signed at or after mediation may be a binding contract; "draft," "term sheet," and "MOU" labels do not by themselves make a document non-binding; the mediator is neutral and cannot advise either party; an attorney review before signing is the normal protection, not an insult to the process.

### Stage 3 — Term-by-Term Restatement Table
Walk the document term by term. For each: quote or summarize the term as written; restate it in the user's plain language (marked as working understanding); record what the user gives/does, what the user gets, and any deadline; mark `[UNCLEAR]` where the wording could mean more than one thing, and circle vague words.

### Stage 4 — Silence Scan
Compare the document against the user's list of topics that matter. Everything expected but absent gets a `[NOT ADDRESSED]` row — including the quiet structural ones users forget: what happens if a payment is missed, who pays a cost the document doesn't mention, how disagreements under the agreement get resolved, when terms can be revisited.

### Stage 5 — Obligations Ledger
Assemble a two-column ledger from Stage 3: everything the user would be obligated to do or give up under the document (with deadlines), and everything the other party would be obligated to do — so the user sees the full exchange in one place before talking to counsel.

### Stage 6 — Questions for the Attorney
Convert every `[UNCLEAR]`, `[NOT ADDRESSED]`, vague word, and uncertain obligation into a specific, document-anchored question, grouped: meaning of terms; missing topics; what I'm giving up; children-related terms; what happens if it isn't followed; and the signing decision itself ("Given all of this, should I sign?" — explicitly routed to the attorney). Close with the do-not-sign reminder.

---

## Output Format

```markdown
# Mediation Agreement Review Organizer — [Your name] · [matter type] · [jurisdiction]
Prepared by [you], [date]. Document status: [unsigned / signed by other party / deadline …]
⚠ DO NOT SIGN until your attorney has reviewed this document.
NOT A LEGAL FILING. NOT LEGAL ADVICE. My working understanding and questions only.
A signed mediation agreement may be binding — *confirm with counsel for [jurisdiction].*

## Plain-Language Frame
[2–3 sentences: signed mediation documents may bind; labels don't protect; the mediator is neutral; attorney review before signing is the normal safeguard — *confirm with counsel.*]

## Term-by-Term — My Working Understanding
| # | Term as written (quote/summary) | My plain-language understanding | I give / do | I get | Deadline | Flags |
|---|---|---|---|---|---|---|
| 1 | [text] | [my words — working understanding only] | [obligation] | [benefit] | [date / none stated] | [UNCLEAR: "reasonable"] |
| 2 | [text] | [my words] | […] | […] | […] | — |

## What the Document Does NOT Address
- [NOT ADDRESSED: topic I expected — why it matters to me]
- [NOT ADDRESSED: what happens if a payment/exchange is missed]
- [NOT ADDRESSED: how future disagreements under this agreement get resolved]

## Obligations Ledger
**I would be obligated to:** [list with deadlines]
**The other party would be obligated to:** [list with deadlines]

## Vague Words to Ask About
- ["reasonable" in term #__ ] — what does this mean in practice?
- ["as agreed" / "to be worked out" in term #__ ]

## My Questions for My Attorney — Before I Sign
### Meaning of Terms
1. [Term #__ says …; does that mean …?]
### Missing Topics
2. [The document says nothing about …; should it?]
### What I'm Giving Up
3. [Term #__ has me giving …; what does that mean for me long-term?]
### Children-Related Terms
4. [Question — *child terms may stay changeable by the court; confirm with counsel.*]
### If It Isn't Followed
5. [What can I do if the other party doesn't do …?]
### The Signing Decision
6. Given all of this — should I sign, ask for changes, or not sign? **(Attorney's call, not mine alone.)**

---
⚠ I will not sign until my attorney has reviewed this document.
"The mediator said it's standard" is not legal advice.
*Confirm all terms and legal effects with counsel for [jurisdiction].*
```

---

## Verification

- [ ] Jurisdiction captured; binding-effect concept stated in plain language and flagged *confirm with counsel*?
- [ ] Every term restated as working understanding — no legal-effect interpretation, no fairness assessment?
- [ ] `[UNCLEAR]` flags applied to ambiguous wording; vague words circled as attorney questions?
- [ ] Silence scan run against the user's own topics list, plus the structural silences (non-performance, dispute resolution, revisiting terms)?
- [ ] Obligations ledger shows both directions of the exchange with deadlines?
- [ ] "Do not sign until your attorney has reviewed" prominent at top and bottom?
- [ ] Every uncertainty converted into a specific, document-anchored attorney question?
- [ ] The signing decision itself explicitly routed to the attorney?
- [ ] No prediction of court outcomes; no redrafted language; no characterization of the other party?
- [ ] Pressure-to-sign or safety dimension screened and routed, not treated as routine?

---

## False-Positive Prevention

| ❌ Don't | ✅ Do |
|---|---|
| "This is a standard support clause — it's fine" | Restate the clause; "is this standard?" goes on the attorney list |
| "This deal looks fair overall" | No fairness assessment; organize terms and questions; fairness routes to counsel |
| "It's just a term sheet, not a real agreement — low risk to sign" | Labels don't protect; signed mediation documents may bind — *confirm with counsel*; do not sign before review |
| "The document doesn't mention the 401(k), so you keep it" | [NOT ADDRESSED: 401(k)] — silence is a question, never an answer |
| "'Reasonable parenting time' means roughly every other weekend" | [UNCLEAR: "reasonable"] — circle it; ask the attorney what it means in practice |
| "They'll probably honor the spirit of it" | Record what the document says about non-performance; if nothing → [NOT ADDRESSED] |
| Rewrite a confusing term "more clearly" | No redrafting; quote it, restate the user's understanding, flag the question |
| "You should ask to change terms 3 and 7 before signing" | Negotiation strategy routes to the attorney; this prompt builds the question list |
| "Sign now — your lawyer can fix problems later" | Reinforce: review BEFORE signing; later may be too late |
| Treat "I felt worn down and just want it over" as routine | Surface it; tell the attorney; if safety/coercion is present → Safety Block |

---

## Adaptations

**By document weight:**
- **Parenting-heavy:** Expand the children-related questions; note in plain language that courts often keep child support and custody terms changeable regardless of what parents sign — *confirm with counsel.* Pair with `legalprep_best_interests_factor_self_map.md`.
- **Finance/property-heavy:** Cross-check terms against your `legalprep_asset_and_debt_inventory.md` — every asset and debt on your inventory should appear in the document or in the `[NOT ADDRESSED]` list.
- **Partial agreement:** Mark which issues the document resolves and which remain open; ask the attorney what signing a partial agreement does to the open issues.

**By pressure level:**
- **Asked to sign at the session:** The one-line script: *"I need my attorney to review this before I sign."* Asking for time is normal.
- **Deadline given:** Record the deadline and who set it; tell the attorney immediately — review timing is their call.
- **DV history / felt coerced:** Safety Block; tell your attorney and advocate that you felt pressured — coercion around signing is something they specifically need to know.

---

## Related Prompts

- `legalprep_mediation_preparation_organizer.md` — prepare priorities and documents **before** mediation; this prompt picks up when a session produces paper.
- `legalprep_post_mediation_follow_up_organizer.md` — debrief the session itself: what was resolved, open items, commitments, and deadlines.
- `legalprep_attorney_consultation_question_builder.md` — broader consultation-question building; this prompt's question list slots into it.
- `legalprep_attorney_handoff_brief.md` — the full case-organization package for your attorney.
- `domain-legal/divorce/legal_post_mediation_term_sheet_and_mou_drafter.md` — the attorney-side prompt for drafting/memorializing mediated terms (what your attorney works from).
