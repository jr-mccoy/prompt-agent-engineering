---
title: "Donor Appeal Letter — Segmented Ask, Real Gift Math, One Clear Reply"
category: business-strategy/nonprofit
description: "Draft a direct-mail or email fundraising appeal for a nonprofit, segmented by donor history (current, lapsed, first-time, monthly) with an ask ladder derived from each segment's last gift, gift-impact lines that reconcile to the budget, and a reply device — distinct from the copywriting and email-sequence marketing skills, which write conversion copy for a product rather than a gift appeal to people who already know the cause."
techniques:
  - RP-02
  - NE-17
  - NE-04
  - CM-02
  - QA-01
difficulty: beginner
tags:
  - nonprofit
  - fundraising
  - appeal-letter
  - direct-mail
  - donor-retention
  - year-end-giving
updated: "2026-09-24"
related_prompts:
  - domain-agentic-resources/skills/marketing/copywriting/SKILL.md
  - domain-agentic-resources/skills/marketing/email-sequence/SKILL.md
  - domain-business-strategy/nonprofit/nonprofit_case_for_support.md
---

# Donor Appeal Letter

**Objective:** Produce an appeal — letter, email, or both — that asks a specific
donor segment for a specific amount, shows truthfully what that amount does, and
makes replying easy, with versions for each segment rather than one letter for all.

**When to Use:**
- Year-end, spring or emergency appeal to an existing donor file.
- A lapsed-donor reactivation mailing.
- A first appeal to people who attended an event or volunteered.

**Not this prompt if:**
- You need conversion copy for a product page or a launch —
  `domain-agentic-resources/skills/marketing/copywriting/`.
- You need a multi-step automated nurture or onboarding flow —
  `domain-agentic-resources/skills/marketing/email-sequence/`. This prompt writes one
  appeal and its segment variants.
- You have no case for support yet — draft it first with
  `nonprofit_case_for_support.md`; an appeal cut from nothing invents its facts.
- The ask is a face-to-face major gift — `nonprofit_major_gift_ask_plan.md`.

## Inputs

1. The case for support, or at minimum: the need, the plan, the budget unit costs.
2. **Donor file summary by segment:** count, typical last gift, last gift date.
3. The appeal's purpose, deadline and the real reason for the deadline (if any).
4. A consented story, or permission to use program data instead.
5. Channel (mail, email, both), signer, and reply mechanism (envelope, link, phone).
6. Receipting language the organisation's accountant has approved.

## Method

1. **Segment before writing (RP-02).** At minimum:
   - **Current** (gave in the last 12 months): thank first, then ask.
   - **Lapsed** (gave 13–36 months ago): acknowledge the gap without guilt.
   - **First-time prospects** (event attendees, volunteers): explain the work in one
     sentence before asking.
   - **Monthly donors:** do not ask for a one-off gift by default; thank, report,
     and optionally invite an upgrade.

2. **Build the ask ladder from last gift.** Three amounts per segment: roughly last
   gift, 1.5×, and 2.5×, rounded to natural numbers. Prospects with no history get
   the organisation's median first gift as the middle amount. The first box is the
   one most people tick — never set it below what they gave last time.

3. **Write the letter in this order.**
   - **Opening:** one person, one moment, or one number — concrete, consented.
   - **Problem:** one short paragraph from the case.
   - **What your gift does:** the gift lines, each true at budget unit cost (CM-02).
   - **The ask:** an amount, a verb, a deadline if real. Ask at least twice.
   - **Thanks** that credits the donor, not the organisation.
   - **P.S.:** restates the ask and the most concrete gift line — many readers read
     only this.

4. **Calibrate against a weak version (NE-04).** Produce one short "what this is not"
   example — institutional voice, no amount, "we need your support" — and check the
   draft does none of it.

5. **Close with a single reply path (NE-17).** One primary action per channel: the
   reply envelope, the donation link, or the phone number. Pre-fill the ask amounts
   on the reply device.

6. **Check (QA-01).** Gift math, consent, receipting language, segment ladders,
   and reading level (aim for plain language a 12-year-old could follow).

## Output Format

```
# Appeal — [campaign], [channel]

## Segment plan
| Segment | Count | Last gift (typical) | Ask ladder | Opening variant |

## Master letter
[full text, with {{segment}} variation points marked]

## Segment variations
Current: … / Lapsed: … / Prospect: … / Monthly: …

## Reply device
[amount boxes per segment, reply path, receipting line]

## Email version (if requested)
Subject lines (3): … | Preview text: … | Body: …

## Checks
| Check | Result |
```

## Verification

- [ ] Every "your gift does" line reconciles to a budget unit cost.
- [ ] The lowest ask for current donors is not below their last gift.
- [ ] The ask appears at least twice and in the P.S.
- [ ] Any deadline is real, and its reason is stated.
- [ ] Stories are consented; otherwise program data is used.
- [ ] Receipting and tax-deductibility language is the accountant-approved wording.

## False-Positive Prevention

1. **"Please give generously" is not an ask.** An ask has an amount.
2. **Do not invent urgency.** A fake matching gift or deadline is a trust debt paid
   the next time the donor reads a real one. If a match exists, name the matcher's
   terms as agreed.
3. **Do not fabricate the story.** No composite presented as one person; no details
   beyond the consent given.
4. **One letter for everyone underperforms.** Thanking a lapsed donor for their
   "continued support" tells them nobody looked.
5. **Organisation-as-hero copy fails.** "We served 80 learners" becomes "You helped
   80 adults learn to read."
6. **No tax advice.** Do not state what a donor can deduct; use the organisation's
   approved receipt wording and leave personal tax questions to the donor's adviser.
7. **Dual failure:** a letter so cautious it never asks is as broken as one that
   pressures. Clarity is not pressure.

## Example Output

```
# Appeal — Riverbend Literacy year-end, mail + email

## Segment plan
| Segment | Count | Typical last gift | Ask ladder | Opening |
| Current | 212 | $100 | $100 / $150 / $250 | Thank-you first |
| Lapsed (13–36 mo) | 138 | $50 | $50 / $75 / $125 | "It's been a while" |
| Prospects (event) | 95 | none; median first gift $60 | $35 / $60 / $100 | One-line intro |
| Monthly | 27 | $20/mo | no one-off ask; upgrade to $25/mo | Report + thanks |

## Master letter (current-donor version)
Dear {{first_name}},

On 1 August, 64 adults in Marion County were on our waiting list to learn to read.

Last year, because of you, 72 adults worked with a volunteer tutor — and 42 of
them moved up a full reading level. [58% of 72 = 41.8, reported as 42]

This year we want no one waiting longer than three months. Here is what your
gift does:
  • $45 covers one learner's reading assessments for the year.
  • $91 covers one month of an adult's tutoring program.
  • $1,093 funds one adult's full program year.

Will you give $150 by 31 December to help clear the waitlist?

Thank you for being part of this.
[Signer], Executive Director

P.S. $150 before 31 December covers more than three learners' assessments for a
year — and 64 people are waiting.

## Reply device
[ ] $100  [ ] $150  [ ] $250  [ ] Other $____   Reply envelope enclosed.
Receipt line: [accountant-approved wording]

## Checks
| Check | Result |
| $45 = assessments $3,600 / 80 | ✓ |
| $91 = $1,092.50 / 12 months | ✓ |
| $150 / $45 = 3.3 learners' assessments | ✓ |
| Deadline reason | Calendar-year receipt timing — stated in email version |
| Story consent | No story used; program data only |
```

## Techniques Used

- **RP-02 Audience-Specific Framing:** four segment variants from donor history.
- **NE-17 Call-to-Action Mandatory Close:** one reply path, amounts pre-filled.
- **NE-04 Good vs Bad Example Calibration:** the draft is checked against a weak version.
- **CM-02 Constraint Specification:** gift lines are bound to budget unit costs.
- **QA-01 Self-Verification:** the checks table closes the output.

## Related Prompts

- `domain-agentic-resources/skills/marketing/copywriting/SKILL.md` — commercial conversion copy
- `domain-agentic-resources/skills/marketing/email-sequence/SKILL.md` — automated multi-email flows
- `domain-business-strategy/nonprofit/nonprofit_case_for_support.md` — the source this letter is cut from
