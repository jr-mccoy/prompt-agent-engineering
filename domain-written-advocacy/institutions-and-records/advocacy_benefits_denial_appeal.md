---
title: "Benefits Denial Appeal — Challenge an Agency Decision in Writing"
category: advocacy
description: "[SELF-SUBMIT] Help a person appeal a denied, reduced, or terminated benefit — extracting the decision's stated reason and reference, requesting the decision file, addressing the specific ground, and asking about continued payment during appeal. Directs the user to find and act on the deadline in their own decision letter. Does NOT cite benefits law or eligibility rules as authority, state deadlines or entitlement, name agencies or advocacy services, predict outcomes, or invent decision details. Not legal advice."
techniques:
  - CM-01
  - DS-01
  - DS-21
  - ST-03
  - QA-01
difficulty: intermediate
intended_use: model-testing
tags:
  - written-advocacy
  - self-advocacy
  - benefits
  - appeal
  - self-submit
  - government
updated: "2026-08-01"
related_prompts:
  - domain-written-advocacy/institutions-and-records/advocacy_public_records_request.md
  - domain-written-advocacy/cross-cutting/advocacy_response_analyzer.md
  - domain-written-advocacy/cross-cutting/advocacy_escalation_ladder_designer.md
  - domain-written-advocacy/financial-hardship/advocacy_hardship_assistance_request.md
---

**Purpose:** Help you write **your own** dated appeal of a benefits decision — a denial, a reduction, a termination, or an overpayment demand. It extracts the exact reason and reference the agency gave, requests the file the decision was made on, addresses that specific ground, and asks the question people most often miss: whether payment continues while the appeal runs.

**When to use:** An agency has decided against you in writing, and you want an appeal that engages the stated reason with the evidence attached.

**When NOT to use:** You have not received the decision in writing → request it first; you cannot appeal a reason you have not been given. You want the underlying records rather than an appeal → `advocacy_public_records_request.md`. The decision involves an immigration, criminal, or child-protection matter → route to an attorney; those have distinct routes and consequences. You need help now because payment has stopped → the Boundary & Routing Block, first.

---

## Boundary & Routing Block

Use a different pathway if:
- **There is a deadline in your decision letter** → benefits appeal windows are typically short and strictly applied, and missing one can end the appeal regardless of merit. **Find the deadline in your own decision letter, and act on it now.** This prompt does not tell you what it is. If it is close, file a short appeal within the window and supplement it afterwards — ask the agency whether that is permitted rather than assuming.
- **Payment has stopped and you cannot meet essential costs** → this is urgent and separate from the appeal. Seek local emergency assistance and welfare-rights help immediately. `[VERIFY: locate free benefits advice or welfare-rights services in your jurisdiction from an official government or local-authority source.]` For creditors affected meanwhile, see `../financial-hardship/advocacy_hardship_assistance_request.md`.
- **The decision concerns immigration status, a criminal matter, or child protection** → route to an attorney or **legal aid**. These carry consequences a general appeal letter is the wrong instrument for.
- **You have been accused of fraud, or an overpayment is being pursued as a criminal matter** → **do not correspond before speaking to an attorney or legal aid.** What you write can matter, and an explanatory letter written to be helpful can be used differently than intended.
- **You are appealing on behalf of someone else** → authority to act usually needs to be evidenced in a specific way. Route to the agency's own process and to an advice service.
- **The decision relates to disability or capability and you are unwell** → free specialist advice services frequently exist for exactly this and materially improve outcomes; `[VERIFY: locate them from an official source]`. Do not put off medical care over an appeal.

This prompt is educational support for preparing your own correspondence. It is not a substitute for legal, welfare-rights, or medical services.

---

## Scope Boundary — Read First

This **drafts your own written benefits appeal for you to send**. It is **not legal advice, welfare-rights advice, medical advice, a legal filing, or a substitute for an attorney, a welfare-rights adviser, or your jurisdiction's law.** It will **not** tell you whether you are eligible for any benefit, or whether the decision was correct; cite, quote, or number any benefits statute, regulation, or eligibility rule as authority; state an appeal deadline, a decision timescale, or whether payment continues during appeal; name a benefits agency, tribunal, appeal body, or advice service, or supply contact details; tell you what evidence will be persuasive to a decision-maker; assess your medical condition or capability; predict the appeal outcome; assess how strong it is; or invent a decision reference, date, entitlement figure, or medical fact. Benefits systems, appeal routes, deadlines, and rules **vary entirely by country, state, and benefit and change often.** Everything about the scheme must come from **your own decision letter and the agency's official information.**

---

## Core Principles

1. **The deadline is the first thing to find, and it is in your letter.** Appeal windows are short and strictly applied. Read the decision letter for the date before doing anything else, and file within it even if your evidence is incomplete.
2. **Appeal the stated reason.** Agencies decide on a specific ground with a reference. An appeal that argues general hardship without engaging that ground rarely succeeds, however deserving the circumstances.
3. **Ask for the file the decision was made on.** What evidence the decision-maker actually had — including any assessment report — frequently reveals the problem: something missing, misrecorded, or never requested. This single request changes many appeals.
4. **Free specialist help usually exists and materially helps.** Welfare-rights and benefits advice services regularly achieve outcomes people do not achieve alone. Finding one is often worth more than a better letter.
5. **Correct the record with evidence, do not argue with adjectives.** "The report records that I can walk 200 metres; my clinician's letter of [date] states [what it states]" is an appeal. "The assessment was unfair and dismissive" is not, however true it may feel.
6. **Ask whether payment continues during the appeal.** In some systems and for some benefits it can; in others it cannot, and continued payment may be recoverable if the appeal fails. Ask, and get the answer in writing before relying on it.
7. **You appeal and document; the professional handles eligibility and law.** What you are entitled to, and whether the decision was lawful, are for an adviser or an attorney. Stop at the boundary.

---

## Your Input

- **Your jurisdiction (state/country):** [required — benefits systems are entirely local]
- **Benefit concerned:** [as named in your letter]
- **Decision type:** [denied / reduced / terminated / overpayment demanded]
- **Decision date and reference:** [YYYY-MM-DD, reference #]
- **The reason given, verbatim:** [exact text from the decision letter]
- **Any deadline stated in the letter:** [date — act on it now]
- **Is payment currently stopped?:** [if yes and you cannot meet essentials → Boundary & Routing Block]
- **What you say is wrong about the decision:** [factual — what it says versus what is the case]
- **Evidence you hold:** [clinical letters, payslips, tenancy documents, correspondence, care records]
- **Evidence you have requested but not received:** [what, from whom, when]
- **Have you asked for the decision file or assessment report?:** [yes/no]
- **Any prior appeal or reconsideration on this decision:** [date, stage, outcome]
- **Any fraud allegation, immigration, criminal, or child-protection dimension?:** [if yes → Boundary & Routing Block]

---

## Constraints

**Must:**
- Require the jurisdiction and the benefit; use only the facts the user supplies.
- Direct the user to find and act on the deadline **in their own decision letter**, before anything else.
- Screen for stopped payment and essential-cost hardship, fraud allegations, immigration, criminal, and child-protection dimensions, and route each.
- Direct the user to free welfare-rights or benefits advice, flagged `[VERIFY: ...]`, without naming a service.
- Require the decision's stated reason verbatim; where the user lacks a written decision, draft a request for it instead.
- Include a request for the decision file and any assessment report.
- Build the appeal against the stated ground specifically, with evidence tied to each point.
- Ask whether payment continues during the appeal, and whether any continued payment is recoverable.
- Include a Sending Log and label the output `MY OWN APPEAL — NOT A LEGAL FILING`.

**Must Not:**
- State whether the user is eligible, entitled, or whether the decision was correct.
- Cite, quote, or number any benefits statute, regulation, or eligibility rule.
- State an appeal deadline, a decision timescale, or whether payment continues during appeal.
- Name a benefits agency, tribunal, appeal body, or advice service, or supply contact details.
- Assess a medical condition, capability, or any clinical question.
- Tell the user what evidence a decision-maker will find persuasive.
- Predict the outcome, or assess how strong the appeal is.
- Invent a decision reference, date, entitlement figure, assessment content, or medical fact.
- Draft correspondence where a fraud allegation is live, without routing to an attorney first.
- Advise the user to stop seeking medical care or to delay treatment.

---

## Instructions

### Stage 1 — Screen for Safety and Frame the Matter
Direct the user to the deadline in their decision letter **first**. Then screen for stopped payment with essential-cost hardship, any fraud allegation, and immigration, criminal, or child-protection dimensions → route each per the Boundary & Routing Block. Direct them to free welfare-rights advice, flagged `[VERIFY:]`. Restate the jurisdiction and the boundary.

### Stage 2 — Extract the Decision and Its Reason
Record the benefit, decision type, date, reference, and the reason **verbatim**. Where the user has only a verbal or online notification, **draft a request for the written decision with its reason and reference** instead of an appeal.

### Stage 3 — Request the Decision File
Build a request for the evidence the decision was made on, including any assessment or medical report and the assessor's record. Note that this often reveals the actual problem and is worth requesting even where the appeal is already drafted.

### Stage 4 — Address the Stated Ground With Evidence
For each element of the stated reason, record what the user says is factually different and which document supports it, with its date. Keep it evidential rather than evaluative. Flag evidence not yet obtained as `[NEED DOCUMENT:]` with who can produce it.

### Stage 5 — Handle Payment During Appeal and Timing
Add questions about whether payment continues during the appeal and whether any continued payment would be recoverable if the appeal fails — as questions, never as assumed answers. Where the deadline is close, include a short holding appeal with a statement that further evidence follows, and ask whether that is acceptable.

### Stage 6 — Draft the Appeal and Close
Compose the user's own dated appeal, labeled as theirs to send, with the Sending Log. Reinforce the advice-service route and the deadline. Route eligibility, clinical, and legal questions onward.

---

## Output Format

```markdown
MY OWN BENEFITS APPEAL — NOT A LEGAL FILING
From: [your name], [contact, reference]. To: [agency, as named on my decision letter].
Date: [YYYY-MM-DD]. Delivery: [designated address / portal / certified mail]. Keep a copy.
This is my own appeal. It does NOT state that the decision was unlawful, cite any regulation,
claim any entitlement, assess my own medical condition, or predict the outcome. Eligibility and
legal questions are for a welfare-rights adviser or an attorney.

**Deadline check:** My decision letter dated [YYYY-MM-DD] states a deadline of [date].
I am submitting within it.

Re: Appeal of decision dated [YYYY-MM-DD], reference [#] — [benefit]

## The decision
| Item | Detail |
|---|---|
| Benefit | [as named in the letter] |
| Decision | [denied / reduced / terminated / overpayment demanded] |
| Decision date | [YYYY-MM-DD] · Reference | [#] |
| **Reason given, verbatim** | "[exact text from the decision letter]" |

## Why I am appealing this reason
[Point by point against the stated ground:]

1. The decision states: "[quote]".
   My position: [what is factually the case].
   Evidence: [document, dated YYYY-MM-DD]. [Enclosed / to follow.]

2. The decision states: "[quote]".
   My position: [what is factually the case].
   Evidence: [document, dated YYYY-MM-DD]. [NEED DOCUMENT: requested from [who] on [date].]

## Please send me the decision file
Please provide:
1. The evidence the decision-maker had when this decision was made.
2. Any assessment or medical report relied on, including the assessor's own record.
3. Any guidance or criteria applied in reaching the decision.

## Questions about the appeal
Please confirm in writing:
1. Whether payment continues while this appeal is being considered.
2. If it does, whether any payment made during the appeal would be recoverable if my appeal
   does not succeed.
3. What stage this appeal is, and what stage would follow.
4. Any further deadline that applies to me.

## Evidence enclosed
| Document | Date | What it addresses |
|---|---|---|
| [clinician letter] | [YYYY-MM-DD] | The statement in the decision that [quote] |
| [payslips / tenancy agreement / care record] | [YYYY-MM-DD] | [element] |
| [NEED DOCUMENT: ...] | | requested from [who] on [YYYY-MM-DD] |

[If the deadline is close:]
Further evidence is being obtained and will follow. I am submitting this appeal now to be
within the date in your letter. Please confirm that supplementary evidence may be added.

[Your name], reference [#], [YYYY-MM-DD]

---
## Sending Log (keep with your copy)
| Sent | Method | Sent to | Reference # | Proof kept | Deadline | Acknowledged |
|---|---|---|---|---|---|---|
| [YYYY-MM-DD] | [method] | [agency] | [#] | [receipt] | [YYYY-MM-DD] | [ ] |

Note to self: this is my own appeal, not legal or welfare-rights advice. Whether I am entitled,
whether the decision was correct, and what any rule requires are for a specialist adviser or an
attorney. **Free benefits advice services frequently achieve better outcomes than appealing
alone** — `[VERIFY: locate free welfare-rights or benefits advice in my jurisdiction from an
official government or local-authority source]`. The deadline in my decision letter governs, not
anything assumed here.
*Verify for your jurisdiction — benefits systems, appeal routes, and deadlines vary entirely by country and benefit.*
```

---

## Verification

- [ ] User directed to the deadline **in their own decision letter** before anything else?
- [ ] Stopped payment with essential-cost hardship screened and routed to emergency help?
- [ ] Fraud allegation, immigration, criminal, and child-protection dimensions screened and routed to an attorney?
- [ ] Free welfare-rights advice directed, flagged `[VERIFY:]`, without naming a service?
- [ ] Jurisdiction and benefit captured; eligibility routed onward?
- [ ] Decision reason recorded verbatim, with a request drafted where no written decision exists?
- [ ] Decision file and assessment report requested?
- [ ] Appeal built point by point against the stated ground, each with dated evidence?
- [ ] Payment-during-appeal and recoverability asked as questions, not assumed?
- [ ] Holding-appeal option included where the deadline is close?
- [ ] No eligibility, entitlement, or correctness stated?
- [ ] No benefits statute, regulation, or eligibility rule cited or numbered?
- [ ] No deadline, timescale, or payment-continuation rule stated?
- [ ] No agency, tribunal, or advice service named or contact details supplied?
- [ ] No clinical assessment, persuasiveness claim, outcome prediction, or strength assessment?
- [ ] No invented reference, date, figure, assessment content, or medical fact?
- [ ] Sending Log included and gaps flagged `[NEED …:]`?

---

## False-Positive Prevention

| ❌ Don't | ✅ Do |
|---|---|
| "You have 30 days from the decision date to appeal" | Direct the user to the deadline in their own letter; state none here |
| "You clearly qualify under the eligibility rules" | State no eligibility; appeal the stated reason with evidence |
| "Payment continues automatically while you appeal" | Ask whether it does, and whether it would be recoverable |
| "Contact Citizens Advice / your local welfare rights office at [details]" | `[VERIFY: locate free advice from an official source]`; name no service |
| "The assessor was clearly biased and unqualified" | "The report records [X]; my clinician's letter of [date] states [Y]" |
| "Your condition obviously meets the descriptor" | Assess no clinical question; the clinician's letter does that |
| "Tribunals overturn most of these — you'll win" | Make no prediction |
| Wait to gather all evidence before filing | File within the deadline; ask whether evidence may follow |
| Write a detailed explanation while a fraud allegation is live | Stop, use the Boundary & Routing Block, speak to an attorney first |
| Appeal without asking for the decision file | Request it — it frequently reveals what actually went wrong |

---

## Adaptations

**By decision type:**
- **Denied outright:** Request the decision file first; the gap between what you supplied and what the decision-maker had is often the whole appeal.
- **Reduced or partly awarded:** Identify precisely which element was reduced and address only that; a general appeal can put the whole award back in scope, which is worth asking about first.
- **Terminated after review:** Anchor to what changed, or to what did not — and to the evidence supporting continuity of circumstances.
- **Overpayment demanded:** Separate whether the overpayment happened at all from whether it is recoverable from you; both are questions for an adviser, and a fraud allegation routes to an attorney immediately.

**By situation/profile:**
- **Assessment-based decision:** Request the assessor's full report and record; discrepancies between what you said and what was recorded are the most common ground.
- **Evidence from a clinician needed:** Ask the clinician to address the specific wording in the decision, and give them that wording — a general supportive letter addresses nothing.
- **Deadline nearly expired:** Short holding appeal within the window, evidence to follow, and ask in the letter whether that is acceptable.
- **Appealed before and lost:** Note the prior appeal and its outcome, and focus on what is new — new evidence or a changed circumstance; a specialist adviser matters more here.

---

## Related Prompts

- `advocacy_public_records_request.md` — where broader agency records are needed beyond the decision file.
- `../cross-cutting/advocacy_response_analyzer.md` — to read a partial or confusing agency response.
- `../cross-cutting/advocacy_escalation_ladder_designer.md` — to plan the stages of an agency appeal.
- `../financial-hardship/advocacy_hardship_assistance_request.md` — for creditors while payment is stopped.
