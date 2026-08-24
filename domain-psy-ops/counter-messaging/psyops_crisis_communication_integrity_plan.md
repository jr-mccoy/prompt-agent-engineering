---
title: "Crisis Communication Integrity — Speaking Honestly While Under Attack"
category: psy-ops/counter-messaging
description: "Plan communication during an active information attack without adopting the opponent's methods: what is known versus unknown, what can be said now, who decides at 3am, and which lines will not be crossed regardless of pressure. Pre-commits the integrity limits before the pressure arrives, because they are decided badly under it, and treats admitting uncertainty as a durability strategy rather than a weakness."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - CM-02
  - QA-01
difficulty: advanced
tags:
  - psy-ops
  - crisis-communications
  - integrity
  - organizational-resilience
  - counter-messaging
updated: "2026-07-28"
reasoning:
  styles: [procedural, evaluative, protective]
  stakes: critical
  horizon: immediate
  uncertainty: ambiguity
  evidence_quality: weak
  domain_complexity: cross_domain
  collaboration: team
  output_format: crisis_plan_with_precommitments
  user_role: [communications, executive, policy, legal]
  mode: [design, decide, act]
related_prompts:
  - domain-psy-ops/counter-messaging/psyops_rumor_response_triage.md
  - domain-psy-ops/counter-messaging/psyops_debunk_and_correction_design.md
  - domain-psy-ops/organizational-red-team/psyops_org_influence_threat_model.md
---

# Crisis Communication Integrity Plan

**Objective:** Plan how to communicate during an active information attack **without adopting the attacker's methods**. The pressure in a live crisis pushes hard and consistently in one direction: toward certainty you do not have, toward denials broader than the facts support, toward attacking the messenger, and toward channels and tactics you would not defend in daylight. Every one of those feels correct at 2am with an executive demanding action, and every one of them converts a survivable incident into a second, larger story about the response.

So the plan's core is **pre-commitment**. The integrity limits are decided now, while nobody is shouting, and written down where they can be pointed at later. The other half is decision architecture: **who can approve what, at what hour, without waiting for someone who is asleep.** Most crisis failures are not failures of messaging judgment. They are the predictable output of an organization that had no one empowered to speak for nine hours and then over-corrected.

The counter-intuitive commitment is that **admitting uncertainty is a durability strategy**. "Here is what we know, here is what we do not know yet, here is when we will next update" survives new facts. A confident denial does not, and the retraction is worse than the original disclosure would have been.

**When to use:**
- You are under active attack, or expect to be within days.
- You are building a crisis plan before you need it — the only good time.
- A previous crisis response went badly and you are rebuilding the approach.
- Leadership is pressing for a response you think crosses a line, and you need the limits written down.

**When NOT to use:**
- You are deciding whether to respond to a single claim — use `psyops_rumor_response_triage.md`.
- You need a specific correction built — use `psyops_debunk_and_correction_design.md`.
- You are modeling exposure in advance rather than planning response — use `../organizational-red-team/psyops_org_influence_threat_model.md`.

**Audience:** Communications leads, executives, legal, and policy teams.

---

## Inputs / Context

1. **The situation.** What is happening, and — separately — what is actually established versus alleged.
2. **The known-unknown split.** What you know, what you do not know, and when you expect to know more. This is the spine of everything you will say.
3. **Whether any of it is true.** Honestly. Response strategy for a true allegation is entirely different and denial is fatal.
4. **Audiences and their order of priority.** Staff, customers, regulators, partners, media, public. Staff are usually underweighted and usually first to matter.
5. **Decision authority.** Who can approve what, and their actual availability at 3am and at weekends.
6. **Constraints.** Legal, regulatory, and contractual limits on what can be said, and by when.
7. **The pressure.** What internal voices are pushing for, so it can be named rather than absorbed.

---

## Constraints

### Must
- Establish the **known / unknown / next-update** structure as the basis of every statement.
- Determine **whether the allegation is true** before designing any response, and switch to disclosure if it is.
- Write **pre-committed integrity limits** — the things you will not do regardless of pressure — before the pressure arrives.
- Define **decision authority by hour**, including who can approve a holding statement without waking anyone.
- Prioritize **staff communication**, who learn from the news otherwise and become the leak, the story, or both.
- Commit to a **next-update time** in every statement, and meet it even when there is nothing new.
- Plan for **being wrong**: how you will correct your own statements, which is more likely than anyone plans for.
- Distinguish **legal constraint from reputational preference**, since "we can't comment" is used for both and the audience cannot tell them apart.

### Must Not
- Deny beyond what you know. The broad early denial that later needs qualifying is the single most reliable way to convert an incident into a scandal.
- Attack the messenger, question a journalist's motives publicly, or make the critic the story.
- Use undisclosed channels, third-party amplification, sockpuppets, or paid advocacy presented as organic. This is the line the domain exists on.
- Fabricate timelines, internal findings, or supportive facts under deadline pressure.
- Let legal review silence a statement that integrity requires without that being an explicit, recorded executive decision with the risk named.
- Wait for complete information before saying anything. Silence during an active crisis is itself a statement, and it is read as confirmation.
- Prioritize the media over staff and directly affected people.

---

## Instructions

### Step 1 — Establish truth status honestly, before anything else
Is the allegation true, partly true, false, or unknown? Everything downstream depends on this, and getting it wrong here cannot be recovered by good messaging. If it is true or partly true, this is a disclosure problem — proceed accordingly.

### Step 2 — Build the known / unknown / next-update board
Three columns, maintained live. This is the spine of every statement, and keeping it current is the single highest-value activity during a crisis.

### Step 3 — Write the pre-committed integrity limits now
The specific things you will not do: no denial beyond established facts, no attacking the messenger, no undisclosed amplification, no statement without a next-update commitment, no blaming individual junior staff. Get them signed off while calm and keep them visible in the room.

### Step 4 — Define decision authority by hour
Who approves a holding statement at 3am. Who approves a substantive statement. Who can commit to remediation. Name people, name deputies, and confirm each knows. Test it against a real weekend.

### Step 5 — Order the audiences
Usually staff and directly affected people first, then regulators and partners, then media and public. Staff who learn from the news become the story's second act.

### Step 6 — Draft the holding statement now
What is known, what is not, what you are doing, and when you will update. It should be usable within minutes and require only the facts to be slotted in.

### Step 7 — Plan for being wrong
How you correct your own statement: who decides, how fast, and through which channel. Pre-committing to this makes the correction possible; without it, the instinct is to defend the error.

### Step 8 — Separate legal constraint from preference, then run the adversarial check
For each thing you cannot say, mark whether it is a genuine legal constraint or a reputational preference, and record who decided. Then argue that this plan will produce silence and defensiveness under real pressure, and fix what that reveals.

---

## False-Positive Prevention

1. **Denial beyond the facts.** The most reliable escalation available. A qualified early statement survives new information; a broad denial does not.
2. **Attacking the messenger.** Making the journalist or critic the subject, which shifts the story to your conduct and guarantees a follow-up.
3. **Covert response.** Undisclosed amplification, third-party advocacy, or sockpuppets. If discovered — and it is discovered — it becomes a larger story than the original.
4. **Waiting for complete facts.** Silence during an active crisis is read as confirmation. Say what is known and commit to an update.
5. **Staff last.** Briefing media before employees, who then learn from the news and become both the leak and the second story.
6. **Legal used as cover.** Attributing a reputational choice to legal advice, which erodes internal trust and does not survive scrutiny.
7. **Authority untested.** A plan requiring approval from someone unreachable at the hour it will actually be needed.
8. **No correction path.** Having no pre-agreed way to fix your own statement, so the instinct becomes defending the error.

---

## Output Format

```
# Crisis communication plan — [situation]

## Truth status (established first)
[True / partly true / false / unknown]
**If true or partly true → this is disclosure, not defense. Denial will make it worse.**

## Known / Unknown / Next update
| Known (established) | Unknown | When we expect to know |
|---|---|---|
| [...] | [...] | [...] |

## Pre-committed integrity limits (signed off while calm)
1. No denial beyond established facts.
2. No attacking the messenger or questioning a critic's motives publicly.
3. No undisclosed channels, third-party amplification, or inauthentic advocacy.
4. No statement without a next-update commitment.
5. No blaming individual junior staff.
6. [Organization-specific]

**Signed off by:** [name, role, date]

## Decision authority by hour
| Decision | Business hours | Out of hours | Deputy |
|---|---|---|---|
| Holding statement | [name] | [name] | [name] |
| Substantive statement | | | |
| Remediation commitment | | | |
**Tested against a real weekend scenario?** [yes/no]

## Audience order
1. Staff and directly affected people
2. Regulators and partners
3. Media and public
[Rationale for any deviation]

## Holding statement (drafted now)
"[What we know. What we don't yet know. What we're doing. When we'll update — specific time.]"

## Being wrong
[Who decides we got something wrong, how fast we correct, through which channel]

## Can't say / won't say
| Thing | Legal constraint or reputational preference? | Decided by |
|---|---|---|

## Adversarial check
[The case that this plan collapses into silence and defensiveness under real pressure — and what was fixed]
```

---

## Verification

- [ ] Truth status is established first, and a true or partly-true allegation switches the plan to disclosure.
- [ ] The known / unknown / next-update structure is in place and is the basis of statements.
- [ ] Pre-committed integrity limits are written and signed off before the pressure.
- [ ] Decision authority is defined by hour with named deputies, and tested against an out-of-hours scenario.
- [ ] Staff and directly affected people are prioritized over media.
- [ ] A holding statement is drafted in advance and commits to a specific next update.
- [ ] A correction path for the organization's own errors is pre-agreed.
- [ ] Legal constraints are distinguished from reputational preferences, with the decider recorded.
- [ ] No denial beyond established facts, no attacking the messenger, and no covert or undisclosed response appears anywhere in the plan.
- [ ] No timeline, finding, or supporting fact was fabricated.
