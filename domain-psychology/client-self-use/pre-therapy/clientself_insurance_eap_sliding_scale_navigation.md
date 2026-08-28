---
title: "Affordable Therapy Navigator — Insurance, EAP, Sliding Scale"
category: psychology/client-self-use/pre-therapy
description: "Build a step-by-step plan to find affordable therapy across insurance, EAP, sliding-scale, training clinics, and community mental health — with call scripts and the cost questions to ask."
techniques:
  - ST-04
  - DT-02
  - CM-02
  - ED-04
difficulty: beginner
tags:
  - client-self-use
  - pre-therapy
  - affordability
  - insurance
  - sliding-scale
intended_use: model-testing
updated: "2026-06-08"
related_prompts:
  - domain-psychology/client-self-use/pre-therapy/clientself_finding_therapist_search_criteria.md
  - domain-psychology/client-self-use/pre-therapy/clientself_do_i_need_therapy_decision_aid.md
  - domain-psychology/client-self-use/pre-therapy/clientself_modality_fit_selector.md
---

# Affordable Therapy Navigator — Insurance, EAP, Sliding Scale

## Objective

Help me find therapy I can actually afford by walking the realistic options in order — insurance, employer EAP, sliding-scale therapists, university training clinics, and community mental health — and hand me the exact scripts and cost questions to use when I call. The output should be a checklist I can work through, not a lecture on the healthcare system.

## When to Use

- Cost is the main reason I haven't started therapy.
- My insurance is confusing and I don't know what's covered.
- I'm uninsured or underinsured and need lower-cost routes.
- I want to know what EAP / sliding scale / training clinics actually are and whether they fit me.

## Inputs / Context

- Whether I have health insurance, and if so, the plan type (HMO/PPO/EPO/Medicaid/Medicare) if I know it.
- Whether my employer (or a partner's) might have an EAP.
- Roughly what I can pay per session, and how many sessions feel sustainable.
- Whether I'm near a university or teaching hospital (for training clinics).
- Any preferences from my search (telehealth, identity factors) so cost routing stays aligned.

## Constraints

### Must

- Output sections in order: **My Money Situation**, **Routes to Try (in order)**, **Call Scripts**, **Cost Questions to Always Ask**, **My Tracker**, **If I'm in Crisis and Can't Pay**.
- Order routes by realistic likelihood given my inputs (e.g., EAP first if I have one, since it's usually free for a set number of sessions).
- For each route, say in one line what it is, who it fits, and the typical catch (e.g., training clinics = lower cost, supervised trainees, waitlists possible).
- Provide verbatim call scripts I can read to my insurer and to an EAP line.
- The cost-questions list must include the terms that change my bill: in-network vs out-of-network, deductible, copay/coinsurance, session limits, prior authorization, superbill/out-of-network reimbursement.
- Include a crisis carve-out: free/low-cost options that don't depend on ability to pay.

### Must Not

- Don't quote specific dollar amounts, copays, or coverage as facts — those depend on my plan; tell me to confirm.
- Don't name specific insurers, employers, or clinics as endorsements.
- Don't imply lower-cost care is lower-quality care.
- Don't give tax or legal advice about FSA/HSA beyond noting they may be usable and to confirm with my plan.

## Instructions

1. Reflect back my money situation and what's sustainable.
2. Order the routes by what's most likely to work for me, with the one-line what/who/catch for each.
3. Give verbatim scripts for the insurer call and the EAP call.
4. List the cost questions that actually move my bill.
5. Give a simple tracker to log what each route said.
6. Add the crisis carve-out for not-able-to-pay situations.

## Output Format

```
=== AFFORDABLE THERAPY NAVIGATOR ===

My Money Situation:
- Insurance: [yes/no + plan type if known]
- EAP available: [yes/no/unsure]
- Sustainable per session: [$__ / need free or near-free]

Routes to Try (in order for me):
1. [EAP] — what it is / who it fits / typical catch
2. [In-network insurance] — ...
3. [Sliding-scale therapists / Open Path-style networks] — ...
4. [University or teaching-hospital training clinics] — ...
5. [Community mental health center] — ...
(Reordered to match my inputs.)

Call Scripts:
> To my insurer:
"Hi, I want to confirm my outpatient mental health benefits. Is therapy covered?
What's my copay or coinsurance per session, and have I met my deductible?
Do I need a referral or prior authorization? Can you give me a list of in-network therapists?"

> To an EAP line:
"Hi, I'd like to use my EAP for counseling. How many sessions are covered, at no cost to me?
Can I pick my own provider, and what happens after the covered sessions run out?"

Cost Questions to Always Ask:
- In-network or out-of-network for me?
- Deductible met? Copay or coinsurance per session?
- Any session limit or prior authorization?
- If out-of-network: do you give a superbill so I can seek reimbursement?
- Sliding scale or reduced rate, and how do I qualify?

My Tracker:
| Route | Who I spoke to / date | Cost to me | Waitlist? | Next step |
|-------|-----------------------|-----------|-----------|-----------|
| ...   |                       |           |           |           |

If I'm in Crisis and Can't Pay:
- 988 Suicide & Crisis Lifeline (US): call or text 988 — free, 24/7.
- Community mental health centers and ERs cannot turn me away in an emergency for inability to pay.
- Bring affordability barriers to any clinician I reach; they often know local low-cost options.
```

## Verification

- [ ] Routes ordered by realistic fit to my inputs, each with what/who/catch.
- [ ] Verbatim scripts for both insurer and EAP calls.
- [ ] Cost questions include the bill-moving terms (in/out-of-network, deductible, copay, limits, prior auth, superbill).
- [ ] No invented dollar figures, no named-entity endorsements, no "cheap = worse" framing.
- [ ] Crisis carve-out present (988 + can't-be-turned-away note).
- [ ] Tracker included.
