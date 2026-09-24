---
title: "Customer Review Response — Public Reply, Private Follow-Up, and the Fix Behind It"
category: business-strategy/small-business
description: "Respond to a Google, Yelp or similar public review of a local business — triage the review type, write a short public reply future customers will read, a private follow-up to the reviewer, and the operational fix the complaint points to — without arguing, disclosing customer details, trading favours for edits, or making legal claims; distinct from ios_app_store_review_response (app-store replies about software) and support_escalation_response_drafter (a private support-queue escalation)."
techniques:
  - NE-07
  - RP-02
  - NE-04
  - CM-02
  - QA-02
difficulty: beginner
tags:
  - small-business
  - reviews
  - reputation
  - customer-service
  - google-reviews
  - local-business
updated: "2026-09-24"
related_prompts:
  - domain-software-engineering/mobile/ios/publishing/ios_app_store_review_response.md
  - domain-sales-customer/support/support_escalation_response_drafter.md
  - domain-business-strategy/small-business/smallbiz_local_marketing_plan.md
---

# Customer Review Response

**Objective:** Turn one public review into three things: a public reply written for
the next hundred people who read it, a private follow-up that gives the reviewer a
real path to resolution, and a note of what to change in the business so the
complaint does not recur.

**When to Use:**
- A new negative or mixed review has appeared and you are tempted to reply tonight.
- A glowing review deserves more than "Thanks!".
- A review looks fake, mistaken, or mentions something you cannot discuss publicly.

**Not this prompt if:**
- You are replying to app-store reviews of software —
  `domain-software-engineering/mobile/ios/publishing/ios_app_store_review_response.md`.
- The complaint arrived privately through a support queue and needs escalation —
  `domain-sales-customer/support/support_escalation_response_drafter.md`.
- The review alleges injury, illness, discrimination or a crime, or threatens legal
  action — draft nothing public beyond a holding line; talk to your insurer or a
  lawyer first.

## Inputs

1. The review text, star rating, platform, and date.
2. What your records show: order, booking, invoice, staff on duty — for your eyes,
   not for the reply.
3. What you are able and willing to offer privately (redo, refund, discount, call).
4. Your name and role for the signature.
5. Anything sector-specific: health, legal, financial and similar businesses often
   must not confirm someone is a client at all.

## Method

1. **Cool down, then triage.** Classify the review:

   | Type | Public reply aims to |
   |---|---|
   | Praise | Thank specifically; reinforce what they valued |
   | Fair complaint | Own it, say what changes, offer a private path |
   | Partly mistaken | Acknowledge the experience; correct one fact neutrally |
   | Not a customer / suspected fake | Brief, calm; say you cannot find the visit; invite contact; report through the platform's process |
   | Safety, legal, health, discrimination | Holding line only; escalate |

2. **Acknowledge before explaining (NE-07).** The first sentence recognises the
   experience in the reviewer's terms. Explanations, if any, come second and short.

3. **Write for the reader who isn't the reviewer (RP-02).** Prospective customers
   read the reply to judge how you treat people when things go wrong. Keep it under
   about 80 words.

4. **Apply the constraints (CM-02).**
   - No personal details from your records: no order contents, dates, medical,
     financial or account information. Echoing what the reviewer wrote is
     acknowledgment; adding what your records show is disclosure.
   - No arguing, no sarcasm, no blaming staff by name.
   - No compensation offered in exchange for changing or removing the review.
   - One offline path: a name and a direct contact.
   - Sign with a real name.

5. **Calibrate against a bad reply (NE-04).** Draft the defensive version in one line
   ("Actually, we told you it would take a week…") and make sure the real reply does
   none of it.

6. **Write the private follow-up.** Specific apology, what happened (as far as you
   know), what you are offering, and how to take you up on it. Sent through the
   platform's messaging or your own records, if the reviewer is a known customer.

7. **Name the fix.** What in the business caused this — process, staffing, pricing
   communication — and one change.

8. **Stress-test (QA-02).** Read the reply as the angriest possible reader and as a
   lawyer would. Remove anything that could be read as a threat, a disclosure or a
   promise you won't keep.

## Output Format

```
# Review response — [platform], [stars], [date]

## Triage
Type: [...] | Records show: [private summary] | Escalate? [no / to whom]

## Public reply
[≤ 80 words, signed]

## What the reply avoids
[the defensive one-liner, and why it's excluded]

## Private follow-up
[message]

## The fix
| Cause | Change | Owner | By when |

## Stress-test notes
```

## Verification

- [ ] The first sentence acknowledges the reviewer's experience.
- [ ] No personal or transaction details appear in the public reply.
- [ ] No offer is conditioned on editing or removing the review.
- [ ] One named offline path is given.
- [ ] An operational fix is named for any fair complaint.
- [ ] Legal, health or safety allegations were escalated, not answered.

## False-Positive Prevention

1. **Winning the argument loses the reader.** A reply that proves the customer wrong
   reads to everyone else as "this is how they'll treat me".
2. **Do not disclose to defend yourself.** "Your invoice clearly shows…" in public
   reveals a customer's business; keep facts for the private message.
3. **Never trade for an edit.** "We'll refund you if you update your review" violates
   platform rules and looks like buying reviews. Offer the remedy unconditionally.
4. **Do not accuse a suspected fake.** Say you cannot find a record and invite
   contact; report it through the platform's process.
5. **Do not template every reply identically.** Copy-paste replies read as nobody
   looked; reference one specific thing.
6. **Do not make legal statements.** "This review is defamatory" is for a lawyer to
   say, if anyone.
7. **Dual failure:** not replying at all to a fair complaint is also a reply — and
   over-apologising for something that didn't happen misleads readers too.

## Example Output

```
# Review response — Google, 2 stars, 19 Sep 2026

## Triage
Type: Fair complaint (partly). Records (private): tune-up booked 8 Sep, ready 17 Sep;
quoted $65, charged $85 — added a $20 brake cable replacement with a mechanic's note
but no call to the customer. Escalate: no.

## Public reply
Hi Dana — you're right that nine days is too long for a tune-up, and you should have
had a call before anything was added to your bill. That's on us. We've changed how
we handle both, and I'd like to put this right: please reach me directly at the shop
number and ask for Sam.
— Sam Reyes, owner, Harbor Street Bike Repair

## What the reply avoids
"The extra $20 was a brake cable you needed, as noted on your ticket." — true, but it
argues, discloses the job, and sounds like the $20 was her fault.

## Private follow-up
Dana, I'm sorry — we were short a mechanic that week and didn't call you about the
wait or the brake cable. We should have asked before replacing it. I've refunded the
$20 to your card today, whatever you decide about the review, and your next tune-up
is on us if you'd like it. — Sam

## The fix
| Cause | Change | Owner | By when |
| Added work without approval | Any addition over $0 needs a call or text approval, logged | Sam | Now |
| No update on delays | Text an update if a job passes its promised date | Front desk | 1 Oct |

## Stress-test notes
Removed "we were short-staffed" from the public reply (reads as an excuse); kept it
private. Refund stated as unconditional.
```

## Techniques Used

- **NE-07 Emotional Validation First:** acknowledge the experience before any explanation.
- **RP-02 Audience-Specific Framing:** the public reply is written for future customers.
- **NE-04 Good vs Bad Example Calibration:** the defensive reply is named and excluded.
- **CM-02 Constraint Specification:** privacy, no trade-for-edit, one offline path.
- **QA-02 Adversarial Stress-Test:** read as the angriest reader and as a lawyer.

## Related Prompts

- `domain-software-engineering/mobile/ios/publishing/ios_app_store_review_response.md` — app-store replies
- `domain-sales-customer/support/support_escalation_response_drafter.md` — private support escalations
- `domain-business-strategy/small-business/smallbiz_local_marketing_plan.md` — the review-request process that feeds this
