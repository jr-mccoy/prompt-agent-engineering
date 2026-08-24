---
title: "Pretext Recognition — Verifying Who Is Actually Contacting You"
category: psy-ops/personal-defense
description: "Assess an unexpected approach — call, message, email, or in-person — for the structure shared by social engineering attempts: a manufactured reason to be contacting you, urgency that prevents verification, and an action that must happen now. Centers on out-of-band verification through a channel you found yourself, which defeats the entire class regardless of how convincing the approach is."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - CM-02
  - QA-01
difficulty: beginner
tags:
  - psy-ops
  - social-engineering
  - phishing
  - fraud
  - personal-defense
updated: "2026-07-28"
reasoning:
  styles: [analytic, procedural, protective]
  stakes: high
  horizon: immediate
  uncertainty: ambiguity
  evidence_quality: moderate
  domain_complexity: single_domain
  collaboration: solo
  output_format: verification_decision
  user_role: [individual, employee]
  mode: [assess, decide, act]
related_prompts:
  - domain-psy-ops/technique-analysis/psyops_persuasion_pressure_audit.md
  - domain-psy-ops/personal-defense/psyops_cognitive_security_hygiene_plan.md
  - domain-psy-ops/organizational-red-team/psyops_personnel_targeting_exposure_review.md
---

# Pretext Recognition

**Objective:** Assess an unexpected approach — a phone call, message, email, or someone at the door — for the structure that every social engineering attempt shares, whatever its cover story: a **manufactured reason** the contact is happening now, **urgency that prevents verification**, and an **action that cannot wait**. The cover stories are endless and constantly updated. The structure is not, which is why structure is what you check.

The whole prompt resolves to one move: **out-of-band verification**. Hang up, close the message, and reach the organization through a channel you found yourself — a number from your own card, statement, or a site you navigated to independently. This defeats the entire class of attack regardless of how convincing the approach was, how much the caller knew about you, or how legitimate the number looked. Caller ID is forgeable, sender addresses are forgeable, and knowing your details proves only that your details are known, which for most people they widely are.

The other half of the job is not becoming unable to answer the phone. Most unexpected contact is legitimate. The goal is a cheap habit that costs a few minutes on real calls and defeats fraudulent ones entirely.

> **Safety.** **If you have already sent money, shared a code or password, or given someone remote access, stop reading and act now** — contact your bank and the relevant national fraud reporting body immediately, using numbers you look up yourself from your own card, statement, or an independently navigated official site. **Do not use a number given to you by the contact, and do not rely on a number stated from memory by an AI, including this one.** Speed is what limits the damage. If you are being threatened or feel unsafe, contact your local police or emergency services. Falling for one of these is not a failure of intelligence — they are professionally built and they work on careful, informed people.

**When to use:**
- Someone has contacted you unexpectedly and wants an action, a payment, a credential, or information.
- A message claims a problem with an account, a delivery, a payment, or a legal matter.
- Someone claims to be from your bank, a government agency, tech support, or your own IT department.
- A colleague or family member messages from an unfamiliar number or account asking for something urgent.

**When NOT to use:**
- You have already given information or money — stop and contact your bank and the relevant authority immediately through numbers you look up yourself. Speed matters more than analysis now.
- You want to audit an offer's commercial pressure rather than verify an identity — use `../technique-analysis/psyops_persuasion_pressure_audit.md`.
- You are assessing organizational exposure rather than one approach — use `../organizational-red-team/psyops_personnel_targeting_exposure_review.md`.

**Audience:** Anyone. No technical background assumed.

---

## Inputs / Context

1. **The approach.** What arrived, through what channel, and exactly what it said.
2. **The claimed identity.** Who they say they are and what organization.
3. **The requested action.** What they want you to do, send, click, install, confirm, or move.
4. **The stated reason for urgency.** Why it supposedly cannot wait.
5. **What they knew about you.** Details they cited — and note that this is not evidence of legitimacy.
6. **Whether you initiated contact.** If you called a number you looked up yourself, most of this does not apply.

---

## Constraints

### Must
- Resolve to **out-of-band verification** as the primary recommendation in essentially every case.
- Treat **urgency as the diagnostic**, not the cover story. Legitimate organizations tolerate you calling them back.
- Explicitly note that **knowing your personal details proves nothing** — breach data, public records, and social media make most details widely available.
- Note that **caller ID, sender addresses, and website appearance are all forgeable**, including numbers that match an official one.
- Cover **the reverse-verification trap**: a caller offering to "prove" identity by telling you something about your account, or inviting you to call a number they supply.
- Give a **specific verification procedure**: end the contact, find the number independently, call, and describe the contact.
- Address **authority pressure** — claims of police, tax, immigration, or legal consequence, which are designed to prevent exactly the verification step.
- Keep the standing rule simple enough to use under pressure.

### Must Not
- Advise engaging to gather information, string the caller along, or test them. It increases risk and marks the number as live.
- Suggest that fluent language, a professional manner, a legitimate-looking address, or accurate personal details indicate legitimacy.
- Provide guidance on constructing pretexts, writing convincing approaches, or testing people without authorization.
- Fabricate an organization's real contact details. Instruct the user to find them from their own documents or by navigating independently.
- Shame the user for having engaged, or for nearly doing so. These approaches are professionally built and work on cautious, informed people.
- Suggest clicking a link, opening an attachment, or installing anything "to check."

---

## Instructions

### Step 1 — Stop the clock
Whatever the urgency, nothing needs to be done during this contact. Ending a call, closing a message, or saying "I'll call back" is always available and is never the wrong move.

### Step 2 — Identify the requested action
Name precisely what they want: a payment, a code, a password, remote access, an install, a confirmation, a document, or a move of funds. The nature of the ask sets the risk.

### Step 3 — Examine the urgency, not the story
Write the stated reason it cannot wait. Then ask what actually happens if you call back in an hour. Real organizations accommodate this; frauds cannot, because the window is the attack.

### Step 4 — Discount everything that is forgeable
Caller ID, sender address, logos, site appearance, reference numbers, and personal details about you — all cheap to forge or already public. Strike them from your assessment entirely.

### Step 5 — Watch for the reverse-verification trap
If they offer to prove themselves, or supply a number for you to call, or invite you to check a website they name — that is the attack, not the solution. Verification only counts through a channel you sourced yourself.

### Step 6 — Verify out of band
End the contact. Find the organization's number on your own card, statement, or by navigating to their site yourself. Call and describe what happened. Note that fraudsters sometimes keep a line open — on a landline, wait or use a different phone.

### Step 7 — Apply the specific pressure tests
Requests for codes, passwords, remote access, or moving money to a "safe account" are essentially never legitimate. Threats of arrest, deportation, or immediate legal action from an unexpected caller are almost always fraudulent — real processes do not begin with a surprise call demanding payment.

### Step 8 — Decide, and set the standing rule
Verified / not verified / unresolved and not proceeding. Then write your one-line standing rule for next time.

---

## False-Positive Prevention

1. **Knowledge treated as proof.** "They knew my address and last transaction." Breach data and public records make that routine; it is the oldest trick in the category.
2. **Forgeable signals trusted.** Caller ID matching the official number, a convincing address, correct branding. All trivially spoofed.
3. **Verification through their channel.** Calling the number they gave, or visiting the site they named. This is the trap, and it is the single most common way careful people are caught.
4. **Fluency read as legitimacy.** Professional, calm, well-spoken contact is the norm for organized fraud, not evidence against it.
5. **Engagement to investigate.** Playing along to find out more. It raises risk and confirms a live target.
6. **Paralysis.** Becoming unable to transact with anyone. Out-of-band verification is cheap enough to apply always, which is what keeps it usable.
7. **Authority pressure honored.** Complying because the caller claimed police, tax, or immigration authority. That claim is the pressure mechanism; verification applies most strongly there.
8. **Shame after the fact.** Treating susceptibility as stupidity, which stops people reporting quickly — and speed is what limits the damage.

---

## Output Format

```
# Approach assessment

## What arrived
[Channel, claimed identity, exact ask, stated urgency]

## The requested action
[Payment / code / password / remote access / install / information / fund transfer] — risk: [high/med/low]

## Urgency test
Stated reason it can't wait: [...]
What actually happens if I call back in an hour: [...]

## Forgeable signals — struck from the assessment
| Signal | Why it proves nothing |
|---|---|
| Caller ID / sender address | Spoofable, including exact official numbers |
| Knew my details | Breach data and public records |
| Professional manner / branding | Standard for organized fraud |

## Reverse-verification check
[Did they offer proof, supply a number, or name a site? → that is the attack, not verification]

## Out-of-band verification
1. End the contact.
2. Find the number myself: [own card / statement / independently navigated site]
3. Call and describe the contact.
4. [If landline: use a different phone or wait — lines can be held open.]

## Specific red lines (essentially never legitimate)
- Codes, passwords, or one-time passcodes requested
- Remote access requested
- Moving money to a "safe account"
- Threat of arrest, deportation, or immediate legal action from an unexpected contact

## Decision
[Verified — proceeding / Not verified — not proceeding / Unresolved — not proceeding]

## My standing rule
"[One line I can use under pressure next time]"

## If I already acted
Contact my bank and the relevant authority now, using numbers I look up myself. Speed limits the damage.
This is not a failure of intelligence — these are professionally built and they work on careful people.
```

---

## Verification

- [ ] Out-of-band verification is the primary recommendation, with a concrete procedure.
- [ ] Urgency is treated as the diagnostic rather than the cover story.
- [ ] All forgeable signals are explicitly struck, including accurate personal details.
- [ ] The reverse-verification trap is covered.
- [ ] Specific red-line requests are listed.
- [ ] Authority-pressure claims are addressed as pressure mechanisms rather than reasons to comply.
- [ ] No advice to engage, investigate, test, click, or install appears anywhere.
- [ ] No organizational contact details were fabricated; the user is directed to source them independently.
- [ ] No pretext-construction guidance appears anywhere.
- [ ] The output includes the already-acted path and does not shame the user.
