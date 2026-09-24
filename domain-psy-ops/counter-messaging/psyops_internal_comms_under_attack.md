---
title: "Internal Communications Under Attack — Keeping Staff Informed, Safe, and Uninstrumentalized"
category: psy-ops/counter-messaging
description: "Plan communication with your own staff during an information attack on the organization: what they are told and when, how individuals who are named, doxxed, or harassed are protected, what staff can and cannot say externally, and the line that keeps staff from being turned into an undisclosed amplification channel. Treats staff as the audience most likely to be targeted, most likely to leak, and least often told the truth first."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - CM-02
  - QA-01
difficulty: intermediate
tags:
  - psy-ops
  - internal-communications
  - crisis-communications
  - staff-safety
  - counter-messaging
  - staff-being-harassed
updated: "2026-09-24"
reasoning:
  styles: [procedural, protective, evaluative]
  stakes: high
  horizon: immediate
  uncertainty: ambiguity
  evidence_quality: weak
  domain_complexity: cross_domain
  collaboration: team
  output_format: internal_comms_plan_with_protections
  user_role: [communications, executive, hr, security]
  mode: [design, decide, act]
related_prompts:
  - domain-psy-ops/counter-messaging/psyops_crisis_communication_integrity_plan.md
  - domain-psy-ops/organizational-red-team/psyops_personnel_targeting_exposure_review.md
  - domain-psy-ops/counter-messaging/psyops_rumor_response_triage.md
---

# Internal Communications Under Attack

**Objective:** Plan communication with your **own staff** during an information attack on the organization. `psyops_crisis_communication_integrity_plan.md` treats staff as one audience in an ordered list; this prompt treats them as the audience the attack most directly reaches. Staff read the attack before leadership responds to it. Some are named, quoted out of context, doxxed, or harassed. Some are approached by journalists, by the attackers, or by people posing as either. Many have friends and family asking them what is true. And every one of them is a potential leak of whatever is said internally — which is why **internal communication must be written as if it will be published**, because some of it will be.

The prompt also holds a line that organizations under pressure cross surprisingly often: **staff are not an amplification channel.** Asking employees to post supportive content, share prepared talking points on personal accounts, or defend the organization in comment threads — without disclosing that it was requested — is inauthentic engagement, and when discovered it becomes a larger story than the attack. Staff may speak for themselves; the organization may invite them to share official statements openly; it may not script them covertly.

The protective half matters as much as the informational half. People who are individually targeted need practical help — security, account protection, leave, and a manager who knows — before they need messaging.

**When to use:**
- Your organization is under an active information attack and staff need to be told something.
- Individual employees have been named, doxxed, or targeted.
- Leadership is considering asking staff to "help" publicly and you need the line drawn.
- You are preparing an internal-communications component of a crisis plan in advance.

**When NOT to use:**
- You need the overall crisis-communication plan — start with `psyops_crisis_communication_integrity_plan.md`, then return here for the staff layer.
- You are assessing personnel exposure in advance rather than responding — use `../organizational-red-team/psyops_personnel_targeting_exposure_review.md`.
- You are deciding whether a specific external rumor warrants a public response — use `psyops_rumor_response_triage.md`.

**Audience:** Internal-communications, HR, security, and executive teams.

---

## Inputs / Context

1. **The attack.** What is being said, where, and what is established versus alleged — including whether any of it is true.
2. **Who is affected internally.** Named or targeted individuals, teams under particular scrutiny, and staff in public-facing roles.
3. **What staff already know.** What is circulating internally, and through which channels.
4. **Existing policies.** Media contact policy, social-media policy, security support, and leave provisions — and what they actually permit and require.
5. **Legal and employment constraints.** What may lawfully be required of staff, and what staff are entitled to say, as confirmed by counsel.
6. **Support available.** Security, IT account protection, employee assistance, and managers' capacity.
7. **Leadership pressure.** What leadership wants staff to do, stated plainly so it can be tested.

---

## Constraints

### Must
- Brief staff **before or at the same time as external audiences**, never after.
- Write every internal message **as if it will be published**.
- Use the **known / unknown / next-update** structure, consistent with external statements.
- Put **targeted individuals' safety first**: security contact, account protection, leave options, and manager awareness — offered, not imposed.
- Give staff a **clear, simple route** for media and unknown contacts, and warn that attackers may pose as journalists, colleagues, or IT.
- State **what staff may say**, not only what they may not, consistent with lawful policy and confirmed with counsel.
- Allow **open, voluntary sharing of official statements**, clearly attributed — and nothing beyond it.
- Provide a channel for staff to **report approaches and harassment**, and to ask questions.

### Must Not
- Ask or pressure staff to post, comment, or defend the organization on personal accounts without disclosure, or supply scripts for them to present as their own views.
- Monitor staff's personal accounts beyond what policy and law permit, or use the attack as a pretext to expand monitoring.
- Impose blanket gag orders that exceed lawful policy, or suggest that staff may not speak to regulators or exercise protected rights.
- Identify a targeted employee further, internally or externally, or discuss their situation beyond those who need to know.
- Tell staff something different from what the organization says externally.
- Blame individual staff publicly or internally for the attack's content while facts are unestablished.
- Fabricate reassurances about facts not yet known.

---

## Instructions

### Step 1 — Establish truth status and the known / unknown board
Confirm what is established, alleged, true, or unknown, and keep the internal board identical to the external one. If an allegation is true, internal communication is disclosure too.

### Step 2 — Identify and protect targeted individuals first
For each named or targeted person: a direct, private contact from their manager and security; account-protection help; leave or role adjustments offered; and agreement on what, if anything, is said about them. Do this before any all-staff message.

### Step 3 — Time the all-staff brief
Send it before or with external statements. Include what is known, what is not, what the organization is doing, when staff will hear next, and where to ask questions.

### Step 4 — Set the contact routes
Tell staff exactly where to send media enquiries and unknown contacts, and warn that impersonation of journalists, colleagues, and IT is common during attacks. Verification out of band applies internally too.

### Step 5 — State what staff may and may not say
Write the policy in plain terms, confirmed with counsel: what staff may say publicly, what is reserved to spokespeople, and what rights are unaffected. Lead with what is permitted.

### Step 6 — Draw the amplification line
Write it explicitly: staff may share official statements openly and voluntarily; the organization will not ask anyone to post on its behalf as if it were their own view. Record leadership's agreement.

### Step 7 — Set up the feedback channel and cadence
Provide a channel for questions and for reporting approaches or harassment, with an owner. Commit to an internal update cadence and keep it even when there is nothing new.

### Step 8 — Adversarial check
Read every internal message as a hostile journalist who has just received it from a leak. Argue that it contradicts external statements, pressures staff, or exposes a targeted person. Fix what that reveals.

---

## False-Positive Prevention

1. **Staff last.** Briefing media before employees, who then learn from the news and become both the leak and the second story.
2. **Internal-only candor.** Telling staff things that contradict public statements, on the assumption it will stay internal.
3. **Covert staff amplification.** Requesting undisclosed supportive posts — inauthentic engagement that becomes the story when discovered.
4. **Messaging before safety.** Sending all-staff communications before targeted individuals have been contacted and protected.
5. **Over-broad gag orders.** Silencing staff beyond lawful policy, which erodes trust and can breach protected rights.
6. **Monitoring creep.** Using the attack as a reason to watch staff's personal accounts.
7. **Premature blame.** Pointing at an individual employee before facts are established, internally or externally.
8. **Impersonation unaddressed.** Failing to warn staff that attackers pose as journalists, colleagues, or IT during exactly these periods.

---

## Output Format

```
# Internal communications plan — [situation]

## Truth status and board (identical to external)
| Known | Unknown | Next update |
|---|---|---|

## Targeted individuals (handled first, privately)
| Person (role only in shared docs) | Contacted by | Security / account help | Leave or adjustment offered | What is said about them |
|---|---|---|---|---|

## All-staff brief
Timing: [before / with external statement]
"[Known. Unknown. What we're doing. Next update at ___. Where to ask.]"

## Contact routes
Media enquiries → [...]
Unknown contacts → [...]
Impersonation warning: [journalists / colleagues / IT]

## What staff may say
Permitted: [...]
Reserved to spokespeople: [...]
Rights unaffected: [...] (confirmed with counsel on [date])

## The amplification line
Staff may share official statements openly and voluntarily.
The organization will not ask anyone to post on its behalf as their own view.
Leadership agreement: [name, date]

## Feedback channel and cadence
Channel: [...] · Owner: [...] · Cadence: [...]

## Adversarial check
[How each message reads if leaked; contradictions, pressure, or exposure found and fixed]
```

---

## Verification

- [ ] Staff are briefed before or with external audiences.
- [ ] The internal known / unknown board matches the external one.
- [ ] Targeted individuals were contacted and offered protection before the all-staff message.
- [ ] Contact routes and an impersonation warning are provided.
- [ ] What staff may say is stated plainly and confirmed with counsel, leading with what is permitted.
- [ ] The amplification line is written and agreed by leadership.
- [ ] A feedback channel and update cadence are set with an owner.
- [ ] Every message was read as if leaked.
- [ ] No request for undisclosed staff posts or scripted personal-account content appears.
- [ ] No monitoring expansion, over-broad gag order, further exposure of a targeted person, premature blame, or fabricated reassurance appears.
