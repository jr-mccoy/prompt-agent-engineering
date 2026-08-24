---
title: "Insurance Claim Denial Appeal — Challenge a Denial Through the Internal Process"
category: advocacy
description: "[SELF-SUBMIT] Help a person draft THEIR OWN internal appeal of a denied insurance claim — extracting the stated denial reason and code verbatim, matching the appeal to that specific reason, assembling policy language and supporting documentation, and asking what the next appeal stage is. Screens urgent medical situations to an expedited pathway first. Does NOT cite insurance regulation as authority, state whether a denial is valid or coverage exists, interpret policy terms, state appeal deadlines, predict outcomes, or invent policy language or claim details. Not legal, financial, or medical advice."
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
  - insurance
  - appeal
  - self-submit
  - consumer
updated: "2026-08-01"
related_prompts:
  - domain-written-advocacy/insurance-and-medical/advocacy_external_review_request.md
  - domain-written-advocacy/insurance-and-medical/advocacy_medical_bill_dispute.md
  - domain-written-advocacy/cross-cutting/advocacy_response_analyzer.md
  - domain-written-advocacy/institutions-and-records/advocacy_regulator_complaint_drafter.md
---

**Purpose:** Help you write **your own** internal appeal of a denied insurance claim — health, home, auto, travel, or another line. It extracts the exact reason and code the insurer gave, builds the appeal against **that specific reason** rather than against the denial in general, assembles the policy language and documentation that address it, and asks what stage comes next.

**When to use:** A claim has been denied or partly paid, you have the denial in writing with its stated reason, and you want an appeal that engages the actual ground rather than restating the claim.

**When NOT to use:** Care is being denied and the medical situation is urgent → the Boundary & Routing Block, immediately; there is usually a faster route. The internal appeals are exhausted → `advocacy_external_review_request.md`. The dispute is about a bill from a provider rather than the insurer's decision → `advocacy_medical_bill_dispute.md`. The claim involves injury to someone else, alleged fault, or litigation → route to an attorney.

---

## Boundary & Routing Block

Use a different pathway if:
- **Care or treatment is being denied and the situation is urgent or time-sensitive** → a standard written appeal may be too slow. Ask the insurer immediately what expedited or urgent process it operates and how to invoke it, and involve the treating clinician, who can usually escalate faster than a patient can. `[VERIFY: the insurer's expedited process from your policy documents or by contacting them directly.]` If someone's condition is deteriorating, seek medical care — coverage is a separate problem from treatment.
- **Anyone was injured, another party is involved, fault is alleged, or litigation has started or been threatened** → route to an attorney or **legal aid** before corresponding. What you write to an insurer in a fault-based or injury claim can matter later.
- **An appeal deadline may be running** → appeal windows are often short and strictly applied. **Find the deadline in your denial letter and your policy documents and act on it**; whether it is accurate or the only one is a question for an attorney or your insurance regulator, not for this prompt.
- **You are being asked to sign a release, settlement, or waiver** → have an attorney read it first. A release can end rights you did not know you had.
- **You suspect the claim was denied because of an error in your medical records** → correcting records is a separate route; raise it with the provider as well as appealing.

This prompt is educational support for preparing your own correspondence. It is not a substitute for legal, medical, or insurance-professional services.

---

## Scope Boundary — Read First

This **drafts your own internal appeal for you to send**. It is **not legal advice, medical advice, financial advice, a legal filing, a policy interpretation, or a substitute for an attorney, a clinician, your insurance regulator, or your jurisdiction's law.** It will **not** tell you whether the denial was correct, whether your policy covers the claim, or what a policy term means; cite or quote an insurance statute, regulation, or code as authority; state an appeal deadline or how long the insurer has to respond; state whether a denial code was correctly applied; tell you whether treatment is medically necessary — that is for a clinician; predict whether the appeal will succeed; assess how strong it is; name your insurance regulator or supply its contact details; or invent policy wording, a claim number, a denial code, a diagnosis, or a procedure code. Insurance rules and appeal rights **vary by policy, line of business, state, and country and change over time.** Where such a concept appears it is flagged *verify in your policy documents and with your regulator*.

---

## Core Principles

1. **Appeal the stated reason, not the denial.** Insurers deny for a specific coded reason. An appeal that argues generally about fairness never engages it. Find the reason, quote it, and address exactly that.
2. **Get the denial in writing with its code before you appeal.** If you only have a phone call or a portal status, ask for the written determination including the reason, the code, and the policy provision relied on. You cannot appeal a reason you have not been given.
3. **Quote the policy, do not paraphrase it.** Your own policy document is the authority in this exchange — not general knowledge about insurance. Quote the clause and cite where it appears.
4. **Match documentation to the reason.** A "not medically necessary" denial needs clinical support from the treating clinician. A "not covered" denial needs the policy clause. A "late notification" denial needs the notification evidence. Sending everything is not the same as sending the right thing.
5. **The clinician is your strongest ally on a clinical denial.** A letter of medical necessity from the treating clinician generally does more than anything a patient can write alone. Ask for one.
6. **Ask what stage you are at and what comes next.** Internal appeals often have levels, and external review usually has a precondition. Ask them to state the stage, the next stage, and any deadline.
7. **You appeal and document; the professional handles validity.** Whether the denial was lawful or the policy covers it is for an attorney, your regulator, or an insurance professional. Stop at the boundary.

---

## Your Input

- **Your jurisdiction (state/country):** [required — insurance regulation is highly local]
- **Is the situation medically urgent?:** [if yes → Boundary & Routing Block, first]
- **Insurer and policy type:** [health / home / auto / travel / other]
- **Policy number and claim number:** [#, #]
- **Date of loss / service:** [YYYY-MM-DD]
- **Amount claimed and amount paid:** [$X, $Y]
- **The denial letter:** [date received, and the reason and code **verbatim**]
- **Policy provision the insurer relied on:** [as quoted in the denial]
- **What your policy actually says, quoted:** [clause and where it appears] or [NEED DOCUMENT: policy wording]
- **Why you believe the denial does not fit:** [factual — what the reason says versus what happened]
- **Documentation you hold:** [clinical records, invoices, photographs, reports, correspondence]
- **Whether the treating clinician will support it (clinical claims):** [yes/no/asked]
- **Appeal stage:** [first internal / second internal / unknown]
- **Any deadline stated in the denial:** [date — act on it]
- **Any injury, third party, fault, litigation, or waiver request?:** [if yes → Boundary & Routing Block]

---

## Constraints

**Must:**
- Require the jurisdiction; use only the facts and documents the user supplies.
- Screen medical urgency **first** and route to the expedited pathway and the treating clinician before drafting.
- Screen for injury, third-party involvement, fault, litigation, and waiver requests, and route those to an attorney.
- Require the written denial with its stated reason and code; where the user lacks it, draft a request for it instead.
- Build the appeal against the stated reason specifically, quoting it verbatim.
- Quote the user's own policy wording where supplied; flag `[NEED DOCUMENT: policy wording]` where not.
- Match documentation to the denial reason and say which document addresses it.
- Direct the user to obtain clinician support for clinical denials.
- Ask the insurer to state the current appeal stage, the next stage, and any applicable deadline.
- Include a Sending Log and label the output `MY OWN APPEAL — NOT A LEGAL FILING`.

**Must Not:**
- Assess medical necessity, appropriateness of treatment, or any clinical question.
- State whether the denial was correct, whether coverage exists, or what a policy term means.
- Cite or invent an insurance statute, regulation, code, or mandated timeframe.
- State an appeal deadline or a required insurer response time.
- Name an insurance regulator or supply its contact details.
- Predict the appeal outcome, or assess how strong the appeal is.
- Invent policy wording, a claim or policy number, a denial code, a diagnosis, or a procedure code.
- Advise signing a release, settlement, or waiver.
- Advise delaying or forgoing treatment because of a coverage dispute.
- Draft an appeal where no written denial reason exists.

---

## Instructions

### Stage 1 — Screen for Safety and Frame the Matter
Screen **first** for medical urgency → expedited pathway and treating clinician, immediately. Then screen for injury, third parties, alleged fault, litigation, and any release or waiver → attorney. Note any deadline stated in the denial and tell the user to act on it. Restate the jurisdiction and the boundary: this drafts an appeal; validity and clinical questions route elsewhere.

### Stage 2 — Extract the Denial Reason Verbatim
Record the denial date, the stated reason, the denial or remark code, and the policy provision the insurer relied on — exactly as written. Where the user only has a verbal or portal denial, **stop and draft a request for the written determination** instead; an appeal without the stated reason cannot engage it.

### Stage 3 — Set the Policy Language Against the Reason
Quote the relevant clause from the user's own policy document, with its location. Set it beside the reason given. Where the user cannot locate the wording, flag `[NEED DOCUMENT: policy wording]` and ask the insurer for the provision it relied on — never substitute assumed policy language.

### Stage 4 — Build the Factual Response to That Reason
State factually why the stated reason does not fit what happened — dates, events, records, prior authorizations. Keep it tied to the reason. For a clinical denial, direct the user to obtain a letter of medical necessity from the treating clinician rather than arguing clinical points themselves.

### Stage 5 — Match the Documentation
List each document and say which element of the denial reason it addresses. Where a needed document does not exist, flag it as `[NEED DOCUMENT:]` and identify who can produce it — usually the provider or the clinician.

### Stage 6 — Draft the Appeal and Close
Compose the user's own dated appeal, labeled as theirs to send, with the Sending Log. Include questions about the current stage, the next stage, and any deadline. Point to external review as a later step with its own preconditions, and to the regulator route flagged `[VERIFY:]`. Route validity, clinical, and legal questions onward.

---

## Output Format

```markdown
MY OWN INSURANCE APPEAL — NOT A LEGAL FILING
From: [your name], [contact]. To: [insurer, appeals department]. Date: [YYYY-MM-DD].
Delivery: [designated appeals address / portal / certified mail]. Keep a copy.
This is my own appeal. It does NOT state that your denial was unlawful or incorrect, cite any
insurance regulation, interpret my policy for me, assess medical necessity, or predict your
decision. Clinical questions are for my treating clinician; legal questions are for an attorney.

Re: Appeal of claim denial — policy [#], claim [#], date of service/loss [YYYY-MM-DD]

## The claim and the denial
| Item | Detail |
|---|---|
| Policy number | [#] |
| Claim number | [#] |
| Date of service / loss | [YYYY-MM-DD] |
| Amount claimed | [$X] · Amount paid | [$Y] |
| Denial letter dated | [YYYY-MM-DD] |
| **Reason given, verbatim** | "[exact text of the denial reason]" |
| **Denial / remark code** | [code as shown] |
| Policy provision you relied on | "[as quoted in your denial]" |

## What my policy says
[Quote from the user's own policy document, with location:]
My policy at [section / page] states: "[exact quote]"
[or: [NEED DOCUMENT: policy wording — please send me the full text of the provision you relied on]]

## Why I am appealing this reason
[Factual response tied specifically to the stated reason. Examples of the shape:]
- The reason given is "[quote]". The service was [fact], on [date], and [evidence].
- Prior authorization [#] was issued on [YYYY-MM-DD] for this service. [Copy enclosed.]
- Notification was given on [YYYY-MM-DD] by [method]. [Evidence enclosed.]

[For a clinical denial:]
I have asked my treating clinician, [name/practice], to provide a letter of medical necessity
addressing the reason given. [Enclosed / to follow by [date].]

## Documentation enclosed, and what each addresses
| Document | Date | Which part of the denial reason it addresses |
|---|---|---|
| [prior authorization] | [YYYY-MM-DD] | The statement that the service was not authorized |
| [clinician letter] | [YYYY-MM-DD] | The medical necessity ground |
| [NEED DOCUMENT: ...] | | |

## What I am asking you to do
Please reconsider this denial and pay the claim.

Please also confirm in writing:
1. Which appeal stage this is, and what the next stage would be.
2. Any deadline that applies to me at each stage.
3. If you uphold the denial, the full reason and the policy provision relied on.

[Your name], policy [#], [YYYY-MM-DD]

---
## Sending Log (keep with your copy)
| Sent | Method | Sent to | Reference # | Proof kept | Response due | Outcome |
|---|---|---|---|---|---|---|
| [YYYY-MM-DD] | [method] | [appeals dept] | [#] | [receipt] | [YYYY-MM-DD] | [ ] |

Note to self: this is my own appeal, not legal, medical, or insurance advice. Whether the denial
was correct or lawful, what my policy covers, and whether the treatment is medically necessary
are for an attorney, my regulator, and my clinician respectively. **I will act on the deadline in
my denial letter rather than assuming one.** If internal appeals are exhausted, an external
review may be available — `[VERIFY: identify the external review or regulator route for my
jurisdiction and policy type, and its preconditions, from official sources]`.
*Verify in your policy documents and with your regulator — insurance rules vary by policy, state, and country.*
```

---

## Verification

- [ ] Medical urgency screened **first** and routed to the expedited pathway and treating clinician?
- [ ] Injury, third-party, fault, litigation, and waiver dimensions screened and routed to an attorney?
- [ ] Jurisdiction captured and validity routed *verify with an attorney or regulator*?
- [ ] Written denial reason and code recorded verbatim, with a request drafted where none exists?
- [ ] Policy wording quoted from the user's own document, or flagged `[NEED DOCUMENT:]` and requested?
- [ ] Appeal built against the stated reason specifically rather than the denial generally?
- [ ] Clinician support directed for clinical denials, rather than the user arguing clinical points?
- [ ] Each document matched to the element of the denial reason it addresses?
- [ ] Current stage, next stage, and applicable deadline all asked?
- [ ] No assessment of medical necessity or any clinical question?
- [ ] No statement on whether the denial was correct, coverage exists, or what a term means?
- [ ] No insurance statute, regulation, or mandated timeframe cited or invented?
- [ ] No appeal deadline or insurer response time stated?
- [ ] No regulator named or contact details supplied?
- [ ] No outcome prediction, strength assessment, or advice to sign a release?
- [ ] No invented policy wording, claim number, code, diagnosis, or procedure code?
- [ ] Sending Log included and gaps flagged `[NEED …:]`?

---

## False-Positive Prevention

| ❌ Don't | ✅ Do |
|---|---|
| "They have 30 days to decide your appeal under state law" | State no timeframe; ask them to confirm the stage and any deadline |
| "This is clearly covered under your policy" | Quote the policy clause; whether it covers this is for an attorney or the regulator |
| "This treatment is obviously medically necessary" | Do not assess necessity; ask the treating clinician for a letter |
| "Your denial code was applied incorrectly" | Quote the code and respond to the reason factually; correctness is not yours to declare |
| "File with your state insurance commissioner at [address]" | `[VERIFY: identify the route for your jurisdiction from official sources]` |
| "This appeal has a strong chance of overturning" | Make no prediction or strength assessment |
| Draft an appeal from a phone call with no written reason | Stop; request the written determination with reason and code first |
| Paraphrase the policy from general insurance knowledge | Quote the user's own policy, or ask the insurer for the provision |
| Send every document in the file | Match each document to the specific element of the denial reason |
| Write a standard appeal while treatment is urgently needed | Stop — expedited pathway and the clinician, immediately |

---

## Adaptations

**By line of business:**
- **Health:** The clinician's letter of medical necessity is usually the single most important document; request it early and give the clinician the exact denial reason and code to address.
- **Home or property:** Photographs, dated reports, and the adjuster's own report matter most; ask for a copy of the adjuster's report and any expert report relied on.
- **Auto:** Where another party or fault is involved, route to an attorney before appealing; what you write can matter later.
- **Travel:** Denials often turn on notification timing or exclusions; anchor to the dates of notification and the wording of the specific exclusion cited.

**By denial reason:**
- **Not covered / excluded:** The policy clause is the whole appeal; quote it and ask them to identify the exact exclusion relied on if they have not.
- **Not medically necessary:** Clinician letter addressing the specific stated reason, plus any relevant guidelines the clinician cites — not guidelines you find yourself.
- **Prior authorization missing:** Evidence of the authorization or of the request; if authorization genuinely was not obtained, say so and ask what remedy exists rather than obscuring it.
- **Late notification:** Evidence of when and how you notified, and any circumstance that prevented earlier notification, stated factually.

---

## Related Prompts

- `advocacy_external_review_request.md` — once internal appeals are exhausted.
- `advocacy_medical_bill_dispute.md` — where the dispute is with the provider's bill rather than the insurer's decision.
- `../cross-cutting/advocacy_response_analyzer.md` — to read a partial payment or a second denial.
- `../institutions-and-records/advocacy_regulator_complaint_drafter.md` — once the correct regulator is verified.
