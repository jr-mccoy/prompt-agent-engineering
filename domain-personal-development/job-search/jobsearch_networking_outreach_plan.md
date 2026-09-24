---
title: "Networking Outreach Plan — A Ranked Contact List, One Ask Each, and a Follow-Up Rule"
category: personal-development/job-search
description: "Build a candidate's job-search outreach plan: a contact list ranked by proximity to the target role, one specific and easy-to-decline ask per contact (referral, informational conversation, or introduction), short messages written for each tie strength, and a two-touch follow-up rule — the job seeker's side of outreach, not a recruiter's sourcing or a sales sequence."
techniques:
  - RP-02
  - CM-02
  - DS-06
  - DS-40
  - QA-20
difficulty: intermediate
tags:
  - job-search
  - networking
  - referrals
  - informational-interview
  - outreach
  - candidate
updated: "2026-09-24"
related_prompts:
  - domain-hr-management/hiring/hr_sourcing_outreach.md
  - domain-agentic-resources/skills/marketing/cold-email/SKILL.md
  - domain-personal-development/job-search/jobsearch_pipeline_tracker_and_cadence.md
---

# Networking Outreach Plan

**Objective:** Produce a ranked list of 15–30 contacts for one target role
family, each with a single specific ask, a message written for that
relationship, and a follow-up date — sized to what the candidate can send and
answer in a week.

**When to Use:**
- Cold applications are getting little response and you have not asked
  anyone you know.
- You want referrals into specific companies and do not know how to ask
  without it feeling transactional.
- You are changing field and need conversations with people who do the target
  job before you apply.
- **Not this prompt if** you are a recruiter or hiring manager contacting a
  passive candidate — that is `domain-hr-management/hiring/hr_sourcing_outreach.md`,
  the employer side of the same channel.
- **Not this prompt if** you are selling something. `domain-agentic-resources/skills/marketing/cold-email/`
  writes B2B prospecting sequences; its multi-touch persistence is wrong for a
  job seeker asking a favour.
- **Not this prompt if** the goal is maintaining friendships rather than a
  search — see `prompts/relationships/relationships_network_cultivation_plan.md`.
  For long-term sponsor relationships at work, see
  `prompts/stakeholder/stakeholder_mentor_sponsor_cultivation.md`.

## Inputs / Context

**Required:**
1. **The target role family** and 5–15 target companies.
2. **A raw list of people**: former colleagues and managers, classmates,
   people met at events, second-degree connections at target companies. For
   each: how you know them, when you last spoke, where they work now.
3. **Hours per week available for outreach** and conversations.
4. **Whether the search is confidential.**

**Optional:**
- LinkedIn profile (outreach sends people there; audit it first).
- Alumni or professional association directories.

## Method

1. **Classify each contact by tie and proximity.**
   - Tie: **Strong** (would take your call today), **Warm** (know you, not
     recently), **Weak** (met once, or shared affiliation), **Cold** (no
     connection; found through search).
   - Proximity to target: **Inside** (works at a target company in or near
     the target role), **Adjacent** (in the target family elsewhere, or at a
     target company in another role), **Connector** (knows people who are).

2. **Match one ask to each contact (CM-02).** One ask per message, fitting tie
   and proximity:
   - Strong + Inside → referral to a named, posted role.
   - Warm or Weak + Inside/Adjacent → a 20-minute conversation about how the
     team works; no referral ask in the first message.
   - Connector → a named introduction, with a forwardable two-line blurb.
   - Cold → a question only this person can answer, or nothing.
   Each ask must be easy to decline, and say so.

3. **Write messages for the relationship (RP-02).** Under 120 words. Open with
   the real connection; state the ask in the first three sentences; make it
   specific (a role link, a named team, a date range); close with an easy out.
   Strong-tie messages can be casual; weak-tie messages must say who you are
   and why them.

4. **Rank and size the week (DS-06).** Order by expected value: Strong+Inside
   first, then Connectors with Inside reach, then Warm+Adjacent. Cap the
   week at what the stated hours allow — roughly 15 minutes per message and
   45 per conversation including prep and a thank-you. Anything beyond the
   cap waits.

5. **Set the follow-up rule.** One follow-up after 7–10 days if no reply,
   adding something (a new posting, a short update), then stop. No third
   message. A decline is thanked and closed.

6. **Extract the actions (DS-40).** A table of this week's sends with dates,
   and a line for each conversation to log in the pipeline tracker.

7. **Test for both failure modes (QA-20).** Harmful: a message that pressures,
   misstates the relationship, or exposes a confidential search. Needlessly
   unhelpful: a message so hedged the ask cannot be found.

## Output Format

```
# Outreach plan — [target family], week of [date]

## Contacts
| # | Name | Tie | Proximity | Company / role | Ask | Send by | Follow-up by |

## Messages
### [Name] — [tie], [ask]
[message]

## This week's capacity
Hours available: [n] | Planned: [n] sends, [n] conversations = [n] hrs

## Follow-up rule
[one follow-up after n days with ...; then close]

## Log to pipeline tracker
- [contact] — [ask] — [date]
```

## Verification

- [ ] Every contact has one tie, one proximity class and exactly one ask.
- [ ] No first message to a Warm, Weak or Cold tie asks for a referral.
- [ ] Every message is under 120 words, states the ask within three sentences, and includes an easy out.
- [ ] Planned hours do not exceed hours available.
- [ ] The follow-up rule allows one follow-up, then stops.
- [ ] No message mentions the search to anyone who could expose it, if confidential.

## False-Positive Prevention

1. **Volume is not outreach.** Fifty identical messages look like progress and
   produce fewer conversations than ten specific ones. The capacity cap exists
   to stop this.
2. **An informational conversation that is a disguised referral ask burns the
   contact.** If the real ask is a referral, and the tie is too weak for it,
   the plan should say "not yet", not disguise it.
3. **Sales cadence is the wrong model.** Five-touch sequences that work for
   prospecting read as pressure from a job seeker. One follow-up, then stop.
4. **"Pick your brain" is not an ask.** It hands the other person the work of
   deciding what you want. Every ask names what, how long, and about what.
5. **A strong tie is not automatically useful.** A close friend in an
   unrelated field ranks below a warm tie inside a target company for this
   plan; closeness and proximity are different axes.
6. **Referral without a posting is a favour with no handle.** Ask for a
   referral to a named, open role, or ask for a conversation instead.
7. **Do not overstate the relationship.** "We worked together" for someone
   met at one conference is the fastest way to a non-reply.

## Example Output

```
# Outreach plan — Data analytics (health-tech), week of 2026-09-28

## Contacts
| # | Name | Tie | Proximity | Company / role | Ask | Send by | Follow-up by |
|---|---|---|---|---|---|---|---|
| 1 | Jordan L. | Strong | Inside | Analytics Manager, telehealth co. | Referral to posted Analyst II role | Mon | Oct 8 |
| 2 | Sam K. | Warm | Connector | Ex-manager; now VP Ops at a clinic network | Intro to their data lead | Mon | Oct 8 |
| 3 | Rita M. | Weak | Adjacent | Analyst at a digital-pharmacy startup; met at a Denver meetup | 20-min call on how their team is structured | Tue | Oct 9 |
| 4 | Dr. A. N. | Cold | Inside | Director of Analytics, target hospital system | none this week — no specific question yet | — | — |

## Messages
### Jordan L. — Strong, referral
Hey Jordan — I saw the Analyst II opening on your team (link). I'm moving to Denver in November and this is close to the claims-data work I did at [current employer]. Would you be comfortable referring me? If it's awkward for any reason, no problem at all — I'd still love to hear how the team's doing.

### Rita M. — Weak, conversation
Hi Rita — we met at the Denver Data meetup in August; you mentioned your team had just split into product and ops analytics. I'm moving into health-tech analytics and would value 20 minutes on how that split works day to day. Any week in October; completely fine if you're swamped.

## This week's capacity
Hours available: 4 | Planned: 3 sends (45 min) + 2 conversations if accepted (90 min) + prep = ~3 hrs

## Follow-up rule
One follow-up at day 8–10 with a new detail (a new posting or a moving date); then close. Thank every decline.

## Log to pipeline tracker
- Jordan L. — referral, Analyst II — sent 2026-09-28
- Sam K. — intro request — sent 2026-09-28
- Rita M. — conversation request — sent 2026-09-29
```

## Techniques Used

- **RP-02 Audience-Specific Framing** — messages written for each tie strength.
- **CM-02 Constraint Specification** — one ask, 120 words, easy out, one follow-up.
- **DS-06 Prioritization Guidance** — contacts ranked by tie × proximity and cut to capacity.
- **DS-40 Follow-Up Action Extraction** — sends and conversations become dated actions for the tracker.
- **QA-20 Dual-Failure Quality Test** — checks for both pressuring and uselessly hedged messages.

## Related Prompts

- `domain-hr-management/hiring/hr_sourcing_outreach.md` — the recruiter-side counterpart.
- `domain-agentic-resources/skills/marketing/cold-email/SKILL.md` — B2B prospecting; contrast its cadence with this one.
- `domain-personal-development/job-search/jobsearch_pipeline_tracker_and_cadence.md` — where outreach is logged and measured.
