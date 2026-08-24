---
title: "External Review Request — Take a Denial Beyond the Insurer"
category: advocacy
description: "[SELF-SUBMIT] Help a person prepare a request for independent or external review of an upheld insurance denial — confirming internal appeals are exhausted, assembling the full appeal history and final determination, and organizing the record for a review body the user identifies themselves. Does NOT name external review bodies or supply their details, cite insurance regulation, state eligibility or deadlines, assess the denial's validity, or predict the reviewer's decision. Not legal, financial, or medical advice."
techniques:
  - CM-01
  - DS-01
  - DS-33
  - ST-03
  - QA-01
difficulty: intermediate
intended_use: model-testing
tags:
  - written-advocacy
  - self-advocacy
  - insurance
  - external-review
  - self-submit
  - escalation
updated: "2026-08-01"
related_prompts:
  - domain-written-advocacy/insurance-and-medical/advocacy_insurance_claim_denial_appeal.md
  - domain-written-advocacy/institutions-and-records/advocacy_regulator_complaint_drafter.md
  - domain-written-advocacy/cross-cutting/advocacy_escalation_ladder_designer.md
  - domain-written-advocacy/cross-cutting/advocacy_response_analyzer.md
---

**Purpose:** Help you prepare **your own** request for an independent or external review after an insurer has upheld a denial — confirming the internal process is genuinely exhausted, assembling the complete appeal history and the final determination, and organizing the record in the form a review body will want. It does not tell you which body that is: that depends on where you live and what kind of policy you hold, and getting it wrong costs months.

**When to use:** You have appealed internally, the insurer has upheld its denial or issued a final determination, and you want to take it to an independent reviewer.

**When NOT to use:** You have not completed the internal appeal → `advocacy_insurance_claim_denial_appeal.md` first; most external routes require it. The situation is medically urgent → the Boundary & Routing Block; expedited routes usually exist and are faster. You want to complain about the insurer's conduct rather than the coverage decision → `../institutions-and-records/advocacy_regulator_complaint_drafter.md`. Litigation is involved → route to an attorney.

---

## Boundary & Routing Block

Use a different pathway if:
- **The medical situation is urgent** → expedited external review often exists and is far faster than the standard route. Ask the insurer and the review body what expedited process applies and how to invoke it, and involve the treating clinician, who can usually escalate faster. If a condition is deteriorating, seek care — coverage is a separate problem from treatment.
- **A filing deadline may be running** → external review windows are typically short, strictly applied, and start from the final determination. **Find the deadline in your final determination letter and from the review body itself, and act on it now.** This prompt does not state deadlines, and assuming one is a common and costly error.
- **You have been offered a settlement, release, or waiver** → have an attorney read it before signing; accepting can end the review route entirely.
- **Litigation has started or been threatened, or an injury or third party is involved** → route to an attorney or **legal aid** before filing anything.
- **You are unsure whether internal appeals are actually exhausted** → ask the insurer to confirm in writing that its determination is final and that internal options are exhausted; filing externally too early is a common reason a request is rejected.

This prompt is educational support for preparing your own submission. It is not a substitute for legal, medical, or insurance-professional services.

---

## Scope Boundary — Read First

This **organizes your own record and drafts your own external review request**. It is **not legal advice, medical advice, a legal filing, a policy interpretation, or a substitute for an attorney, a clinician, your insurance regulator, or your jurisdiction's law.** It will **not** name an external review body, independent review organization, ombudsman, or regulator, or supply its address, portal, or form; tell you whether you are eligible for external review, or which route applies to your policy type; cite or quote an insurance statute, regulation, or review scheme as authority; state any filing deadline or review timescale; tell you whether the denial was correct or your policy covers the claim; assess medical necessity; predict the reviewer's decision; assess how strong your case is; or invent a determination, code, policy provision, or clinical fact. Which body reviews what — and whether external review exists at all for your policy type — **varies enormously by state, country, policy type, and whether the plan is self-funded or insured, and changes over time.** Every body must be one **you** identify from official sources.

---

## Core Principles

1. **Confirm exhaustion in writing before you file.** Ask the insurer to state that its determination is final and internal appeals are exhausted. A request filed early is commonly rejected, and the deadline may keep running while you re-file.
2. **The deadline is the thing to establish first.** External review windows are short and strict, and they usually run from the final determination date. Find it in the determination letter and confirm it with the review body — before you spend time assembling documents.
3. **You must identify the right body yourself.** It depends on your policy type, your state or country, and sometimes on whether your employer's plan is self-funded. There is no general answer, and a wrong filing wastes the window.
4. **Submit the complete record, organized.** The reviewer generally sees only what is submitted. A clear index, the full appeal history, the final determination, the policy language, and the clinical documentation — assembled, not scattered.
5. **The stated reason still governs.** The reviewer is examining the insurer's stated ground. Keep the submission focused on that, exactly as in the internal appeal.
6. **Clinical support carries clinical reviews.** An independent reviewer on a medical-necessity question is usually a clinician. The treating clinician's letter addressing the stated reason is the document that speaks their language.
7. **You assemble and submit; the professional assesses merits and eligibility.** Whether you qualify, and whether the denial was lawful, are for an attorney, your regulator, or the review body. Stop at the boundary.

---

## Your Input

- **Your jurisdiction (state/country):** [required]
- **Is the situation medically urgent?:** [if yes → Boundary & Routing Block, first]
- **Insurer and policy type:** [health / home / auto / travel / other]
- **If health: is the plan through an employer, and do you know if it is self-funded?:** [yes/no/unknown]
- **Policy and claim numbers:** [#, #]
- **The original denial:** [date, reason verbatim, code]
- **Internal appeals filed:** [for each: date sent, stage, outcome, date of outcome]
- **The final determination:** [date, whether it says it is final, reason verbatim]
- **Has the insurer confirmed internal appeals are exhausted?:** [yes/no — if no, ask first]
- **Deadline stated in the final determination:** [date — act on it]
- **Documents you hold:** [policy, denial letters, appeal letters, clinical records, clinician letters, reports]
- **Clinician support (clinical claims):** [held / requested / not applicable]
- **Any settlement offer, litigation, injury, or third party?:** [if yes → Boundary & Routing Block]

---

## Constraints

**Must:**
- Require the jurisdiction; use only the facts and documents the user supplies.
- Screen medical urgency **first** and route to the expedited pathway and the treating clinician.
- Establish the deadline from the user's final determination and instruct them to confirm it with the review body **before** assembling documents.
- Require written confirmation that internal appeals are exhausted, or draft a request for it first.
- Require the user to identify the review body themselves, flagged `[VERIFY: ...]`, and state plainly that this prompt does not know which applies.
- Assemble a complete, indexed record: appeal history, determinations, policy language, documentation.
- Keep the submission focused on the insurer's stated ground.
- Direct the user to obtain clinician support for clinical reviews.
- Include a Sending Log and label the output `MY OWN SUBMISSION — NOT A LEGAL FILING`.

**Must Not:**
- Name an external review body, independent review organization, ombudsman, or regulator, or supply contact details, forms, or URLs.
- State whether the user is eligible for external review, or which route applies to their policy type.
- Cite or invent an insurance statute, regulation, or review scheme.
- State a filing deadline or a review timescale.
- State whether the denial was correct, or whether the policy covers the claim.
- Assess medical necessity or any clinical question.
- Predict the reviewer's decision, or assess how strong the case is.
- Advise signing a settlement, release, or waiver.
- Invent a determination, denial code, policy provision, or clinical fact.
- Advise filing externally before internal exhaustion is confirmed.

---

## Instructions

### Stage 1 — Screen for Safety and Frame the Matter
Screen medical urgency **first** → expedited route and treating clinician. Then screen for settlement offers, litigation, injury, and third parties → attorney. Establish the deadline in the final determination and instruct the user to confirm it with the review body immediately. Restate the jurisdiction and the boundary.

### Stage 2 — Confirm Internal Exhaustion
Establish whether the insurer has stated in writing that its determination is final and internal appeals are exhausted. Where it has not, **draft a short request for that confirmation first** and note that filing early is a common cause of rejection.

### Stage 3 — Identify the Route (User-Verified)
State plainly that which body reviews the matter depends on jurisdiction, policy type, and — for employer health plans — potentially on how the plan is funded. Flag `[VERIFY: ...]` and direct the user to official sources to identify the body, confirm eligibility, obtain the correct form, and confirm the deadline. Do not name a body.

### Stage 4 — Assemble the Appeal History
Build a dated table of every step: original claim, denial, each internal appeal, each determination — with dates, reasons verbatim, and proof of sending. This is the spine of the submission and what a reviewer reads first.

### Stage 5 — Index the Documentation
Build a numbered index of every document with its date and what it establishes, tied to the insurer's stated ground. Flag documents not yet obtained as `[NEED DOCUMENT:]` and identify who produces them — usually the provider, the clinician, or the insurer's own file.

### Stage 6 — Draft the Submission and Close
Compose the user's own dated covering submission, labeled as theirs to send, with the index and Sending Log. Note that the review body's own form usually governs and this covering document supports rather than replaces it. Route eligibility, validity, and clinical questions onward.

---

## Output Format

```markdown
MY OWN EXTERNAL REVIEW SUBMISSION — NOT A LEGAL FILING
Prepared [YYYY-MM-DD]. This is my own record and covering submission. It does NOT state that I am
eligible for external review, name the body that handles it, cite any regulation, state any
deadline, assess medical necessity, or predict the outcome. Eligibility and the correct route are
for me to confirm from official sources; validity is for an attorney or my regulator.

## First: the deadline and the route
`[VERIFY — before anything else: identify the external review body for my jurisdiction and policy
type, confirm whether I am eligible, obtain its current form, and confirm the filing deadline,
from official sources. For an employer health plan, whether the plan is self-funded may change
which route applies. This document does not tell me any of that.]`

Deadline stated in my final determination: [YYYY-MM-DD]
Deadline confirmed with the review body on: [YYYY-MM-DD] — [confirmed date]

## Internal appeals exhausted?
[The insurer confirmed in writing on [YYYY-MM-DD] that its determination is final.]
[or: Not yet confirmed — I am requesting written confirmation first, see the request below.]

## The claim
| Item | Detail |
|---|---|
| Insurer | [name] |
| Policy number | [#] · Claim number | [#] |
| Policy type | [health / home / auto / travel] |
| Date of service / loss | [YYYY-MM-DD] |
| Amount in dispute | [$X] |

## Appeal history
| # | Date | Step | Reason given (verbatim) | Proof of sending |
|---|---|---|---|---|
| 1 | [YYYY-MM-DD] | Claim submitted | — | [receipt] |
| 2 | [YYYY-MM-DD] | Denied | "[exact reason]" code [#] | [letter held] |
| 3 | [YYYY-MM-DD] | First internal appeal sent | — | [certified mail #] |
| 4 | [YYYY-MM-DD] | Appeal denied | "[exact reason]" | [letter held] |
| 5 | [YYYY-MM-DD] | Second internal appeal sent | — | [receipt] |
| 6 | [YYYY-MM-DD] | Final determination | "[exact reason]" | [letter held] |

## The ground the insurer relies on
> "[verbatim quote from the final determination]"

Policy provision cited by the insurer: "[as quoted in the determination]"
The provision in my policy at [section/page] reads: "[exact quote]" or [NEED DOCUMENT:]

## Why I am asking for review
[Factual response tied to the stated ground — the same focus as the internal appeal, not a
restatement of the whole claim.]

[For a clinical matter:]
My treating clinician, [name/practice], has provided a letter dated [YYYY-MM-DD] addressing
the stated ground. [Enclosed as item [n].]

## Document index
| # | Document | Date | What it establishes |
|---|---|---|---|
| 1 | Policy schedule and wording | [YYYY-MM-DD] | The provision relied on |
| 2 | Original denial letter | [YYYY-MM-DD] | The reason and code |
| 3 | Internal appeal letters | [dates] | What I raised and when |
| 4 | Final determination | [YYYY-MM-DD] | Exhaustion and the final ground |
| 5 | Clinician letter | [YYYY-MM-DD] | The clinical ground |
| 6 | [NEED DOCUMENT: ...] | | |

---
## If exhaustion is not yet confirmed — request to the insurer
> To: [insurer, appeals department] · Date: [YYYY-MM-DD]
> Re: Policy [#], claim [#] — confirmation of final determination
>
> Further to your determination of [date], please confirm in writing:
> 1. Whether that determination is final.
> 2. Whether my internal appeal rights are now exhausted.
> 3. What external review or independent review route, if any, is available to me, and any
>    deadline that applies.
>
> [Your name], policy [#], [YYYY-MM-DD]

## Sending Log
| Sent | To | Method | Reference # | Proof kept | Deadline | Acknowledged |
|---|---|---|---|---|---|---|
| [YYYY-MM-DD] | [review body — VERIFY] | [method] | [#] | [receipt] | [YYYY-MM-DD] | [ ] |

Note to self: this is my own submission, not legal, medical, or insurance advice. The review
body's own form usually governs and this covering document supports it rather than replacing it.
Whether I am eligible, whether the denial was correct, and whether the treatment is medically
necessary are for the review body, an attorney, and my clinician respectively. **The deadline is
the first thing to confirm, not the last.**
*Verify for your jurisdiction — external review routes vary by state, country, and policy type.*
```

---

## Verification

- [ ] Medical urgency screened **first** and routed to the expedited pathway and clinician?
- [ ] Deadline established from the final determination and flagged for confirmation with the body **before** document assembly?
- [ ] Internal exhaustion confirmed in writing, or a request for confirmation drafted first?
- [ ] Review body left unnamed and flagged `[VERIFY:]`, with the self-funded-plan complication noted for employer health plans?
- [ ] Appeal history assembled with dates, verbatim reasons, and proof of sending?
- [ ] Submission focused on the insurer's stated ground rather than restating the whole claim?
- [ ] Document index numbered, dated, and tied to what each establishes?
- [ ] Clinician support directed for clinical reviews?
- [ ] **No review body, ombudsman, or regulator named, and no address, form, or URL supplied?**
- [ ] No eligibility determination, and no statement of which route applies?
- [ ] No insurance statute, regulation, or scheme cited or invented?
- [ ] No filing deadline or review timescale stated?
- [ ] No assessment of denial validity, coverage, or medical necessity?
- [ ] No outcome prediction or strength assessment?
- [ ] No advice to sign a settlement, release, or waiver?
- [ ] Sending Log included and gaps flagged `[NEED …:]`?

---

## False-Positive Prevention

| ❌ Don't | ✅ Do |
|---|---|
| "File with your state's independent review organization at [address]" | `[VERIFY: identify the body for your jurisdiction and policy type from official sources]` |
| "You have 120 days from the final denial" | State no deadline; the user confirms it from the determination and the body |
| "You're eligible for external review — all health plans have it" | Determine no eligibility; self-funded employer plans and non-health lines differ |
| "The reviewer will almost certainly overturn this" | Make no prediction about the reviewer |
| "This treatment is clearly medically necessary" | Assess no clinical question; the treating clinician's letter does that |
| File externally before the insurer confirms exhaustion | Request written confirmation first; early filing is commonly rejected |
| Send the whole file unsorted | Index every document with what it establishes |
| "Accept their settlement offer, it's a good outcome" | Route any settlement or release to an attorney before signing |
| Spend a week assembling documents, then check the deadline | Confirm the deadline **first** — it is short and strict |
| Restate the entire claim history as the argument | Stay on the insurer's stated ground, as in the internal appeal |

---

## Adaptations

**By policy type:**
- **Employer health plan:** Whether the plan is self-funded can change the route entirely; ask your employer's benefits administrator in writing which applies, and verify from there.
- **Individually purchased health cover:** The route is usually jurisdictional — verify from your regulator's official source rather than from the insurer alone.
- **Property or auto:** External review may be an ombudsman, a regulator complaint, or nothing at all depending on jurisdiction; verify what exists before assuming a review right.
- **Travel or specialty lines:** Often the least standardised; ask the insurer in writing what external route it participates in, and verify independently.

**By situation/profile:**
- **Urgent clinical need:** Expedited route, clinician involvement, and immediate contact with both insurer and review body — the standard sequence is too slow.
- **Insurer will not confirm exhaustion:** Record the request and the non-response; a review body may accept that as evidence, and the non-response is itself a fact.
- **Documents held by the provider or insurer:** Request the complete claim file in writing early; assembling a submission around missing records wastes the window.
- **Deadline very close:** Confirm the deadline and file within it even if documentation is incomplete, asking whether supplementary material may follow — ask the body, do not assume.

---

## Related Prompts

- `advocacy_insurance_claim_denial_appeal.md` — the internal appeal that must come first.
- `advocacy_medical_bill_dispute.md` — where the provider's bill, not the insurer's decision, is the issue.
- `../institutions-and-records/advocacy_regulator_complaint_drafter.md` — for conduct complaints rather than coverage decisions.
- `../cross-cutting/advocacy_escalation_ladder_designer.md` — to plan the sequence across both tracks.
