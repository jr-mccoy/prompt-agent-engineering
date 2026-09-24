---
title: "Support Agent QA Scorecard — Anchored Behaviors, Critical Fails, Fair Sampling, and One Coaching Point per Review"
category: sales-customer/support
description: "Build and apply a quality scorecard for human support agents' calls, chats, and tickets: behavior-anchored dimensions, critical-fail items that override the score, a sample that is fair to every agent, calibration between reviewers, and a coaching note that separates what the agent controlled from what the process caused — distinct from the bot transcript rubric and from scoring a single written reply."
techniques:
  - QA-17
  - CM-02
  - QA-12
  - QA-01
difficulty: intermediate
tags:
  - support
  - quality-assurance
  - agent-coaching
  - contact-center
  - scorecard
  - call-review
  - reviewing-support-calls
  - coaching-my-team
updated: "2026-09-24"
related_prompts:
  - domain-voice-conversational-ui/analytics/analytics_transcript_qa_rubric.md
  - domain-professional-writing/content-quality/quality_slop_support_response.md
  - domain-sales-customer/support/support_escalation_response_drafter.md
---

# Support Agent QA Scorecard

**Objective:** Give a support team a scorecard that turns one human agent's call,
chat, or ticket into a reproducible score, a list of named defects with evidence,
and one coaching point — and a sampling and calibration routine that makes the
weekly QA numbers fair to every agent and honest about what the process, not the
person, got wrong.

**When to Use:**
- You lead a support or contact-center team and QA is done by gut feel, or not
  at all.
- Two reviewers score the same call ten points apart and agents have stopped
  trusting the scores.
- QA scores are high but customers still complain, or low but CSAT is fine.
- You are coaching a new agent and need to show what "good" looks like with
  evidence from their own interactions.
- A policy changed (refunds, identity checks, disclosures) and you need to check
  it is being followed on real contacts.

**Not this prompt if:**
- The conversations are with a chatbot, voice bot, or AI phone agent →
  `domain-voice-conversational-ui/analytics/analytics_transcript_qa_rubric.md`.
- You want to grade one written reply's quality before or after sending it →
  `domain-professional-writing/content-quality/quality_slop_support_response.md`.
- You are writing an agent's performance review →
  `domain-hr-management/performance-reviews/hr_manager_writing_employee_review.md`;
  QA evidence can feed it, but a scorecard is not a review.
- You need to route or prioritize the queue →
  `domain-sales-customer/support/support_ticket_triage_and_routing.md`.

## Inputs

1. **Channels and contact types** in scope: phone, chat, email/ticket; the top
   contact reasons.
2. **Policies an agent must follow:** identity verification, required
   disclosures, refund/credit authority, data-handling rules, escalation rules.
3. **What "resolved" means** for this team, and how reopen/recontact is measured.
4. **The interactions to review:** transcripts, recordings or ticket threads,
   with metadata (agent, date, contact reason, outcome, CSAT if any). Remove or
   mask customer personal data before pasting.
5. **Team size, review capacity per week,** and number of reviewers.
6. **Known problems** (optional): tooling outages, a confusing policy, a recent
   macro change.

## Method

1. **Separate the three questions.** Quality QA answers "did the agent handle
   this contact well?" — not "was the customer happy?" (CSAT) and not "was it
   fast?" (handle time). Keep speed and satisfaction out of the score; report
   them alongside it. A scorecard that rewards short calls teaches agents to
   end calls.

2. **Define 4–6 dimensions as observable behaviors (QA-17).** Typical set:
   - **Resolution accuracy** — the answer or action was correct and complete for
     this customer's issue.
   - **Process and policy** — verification, disclosures, authority limits,
     documentation done as required.
   - **Understanding** — the agent established the real problem before solving
     (asked, confirmed, didn't solve the wrong issue).
   - **Clarity** — the customer could follow what happens next and when.
   - **Ownership** — next steps, promises, and handoffs were explicit and kept.
   - **Tone in action** — respectful, calm, adapted to the customer's state,
     shown by behavior (listened, didn't interrupt, acknowledged impact), not by
     counting empathy phrases.

3. **Anchor every dimension on a 0-1-2 scale.** Write what a 0, 1 and 2 look
   like, with a short example of each from this team's own contacts. Allow N/A
   where a behavior cannot apply (no verification needed on a general
   question); N/A is excluded from the denominator, never scored as 2.

4. **List critical fails (CM-02).** Items that fail the whole interaction
   regardless of the other scores, e.g.: skipped required identity check;
   disclosed another customer's data; gave a refund or promise beyond authority;
   gave information that is wrong and harmful (wrong safety, legal or billing
   consequence); abusive or discriminatory conduct. Keep the list short — if
   everything is critical, nothing is.

5. **Mark cause for every defect.** For each deduction record: **agent** (a
   behavior the agent controlled), **process** (policy, macro, or knowledge
   base told them to do it), or **tool** (system down, missing data). Only
   agent-caused defects go into the agent's score and coaching; process and tool
   defects go to a separate fix list for the team lead.

6. **Sample fairly.** Per agent per period, draw a fixed number at random across
   channels and contact reasons, then add a small risk-stratified sample (escalations,
   reopened tickets, low-CSAT contacts) reported separately. Never score an agent
   only on complaints; never let an agent choose their own samples. State the
   sample size next to every score — four reviews is an anecdote, not a trend.

7. **Calibrate reviewers (QA-01).** Before scores count, have every reviewer
   score the same 5–10 interactions independently, compare per dimension, and
   rewrite any anchor two reviewers read differently. Repeat monthly and when a
   new reviewer joins. Record agreement per dimension; a dimension that won't
   converge is badly anchored, not a lazy reviewer.

8. **Write one coaching point.** Per review: one behavior to keep (quoted
   evidence), one behavior to change (quoted evidence, what to do instead, and
   why it matters to the customer). One change, not a list — agents improve on
   the thing they can remember.

9. **Guard the use of scores.** Even when QA is only for coaching: agents are
   told in advance that contacts are reviewed and against which scorecard, they
   see their own reviews, and they can dispute a score. If scores feed pay or
   discipline, the sample, calibration, cause-marking and the dispute path must
   be written down first. Employee-monitoring notice, data-protection rules,
   customer call-recording consent, any works council or union agreement, and
   extra obligations if an AI system does the scoring all vary by jurisdiction
   `[VERIFY with HR and legal]`.

## Output Format

```
## Scorecard (reusable)
| Dimension | 0 | 1 | 2 | N/A allowed? |
Critical fails: [list]
Scoring: total = sum of scored dimensions / (2 × scored count), where N/A and process/tool-caused
  dimensions are excluded from both numerator and denominator; any critical fail → FAIL

## Review: [contact ID] — agent [role/initials], [channel], [contact reason]
| Dimension | Score | Evidence (quote/timestamp) | Cause (agent/process/tool) |
Critical fail: none | [item + evidence]
Score: [x.xx] (n scored dimensions)
Keep: [behavior + quote]
Change: [behavior + quote → instead do … because …]

## Process / tool fix list (not in agent score)
| Defect | Evidence | Cause | Suggested owner |

## Period summary (per agent)
Sample: random [n] + risk [n]   Mean (random only): [x]   Critical fails: [n]
Trend note (only if n ≥ agreed minimum)

## Calibration record
| Dimension | Reviewer agreement | Anchor changed? |
```

## Verification

- [ ] Every dimension describes an observable behavior with 0/1/2 anchors, and
      no dimension measures speed or CSAT.
- [ ] Every deduction has quoted evidence and a cause label; process and tool
      defects are excluded from the agent's score.
- [ ] Critical fails are listed before scoring and applied only with evidence.
- [ ] N/A and process/tool-caused dimensions are excluded from both the numerator
      and the denominator.
- [ ] Each agent's score shows its sample size, and the random sample is
      reported separately from the risk sample.
- [ ] The coaching note has exactly one keep and one change, each with evidence.
- [ ] No customer personal data appears in the output.

## False-Positive Prevention

1. **Missing a script phrase is not a defect.** Score whether the behavior
   happened (impact acknowledged, next step clear), not whether the macro
   wording was used. Checklists of phrases reward robotic calls.
2. **A policy the agent followed is not the agent's error.** If the knowledge
   base gave the wrong answer, the defect is `process`; penalizing the agent
   teaches them to ignore the knowledge base.
3. **An angry customer is not evidence of poor handling.** Score the agent's
   behavior against the anchors; the customer's mood at the end is context.
4. **A long call is not a bad call.** Complex issues take time; handle time
   stays out of the quality score.
5. **A small or complaint-heavy sample is not a trend.** Do not rank agents or
   draw trends from fewer reviews than the team agreed, or from risk samples
   alone.
6. **Accent, dialect and speech characteristics are never a defect.** Score
   whether the customer understood and was understood, not how the agent
   sounds — including non-native speech or speech affected by disability.
7. **Do not reconstruct what was said.** If the recording or thread is
   incomplete, mark the dimension "not assessable" rather than inferring.

## Example

**Input (abridged):** Chat, billing question. Customer: "I was charged twice this
month." Agent verifies the account with two factors, checks billing, says "I can
see two charges on the 3rd — one is a pending authorization that will drop off
within a few business days," and closes. Customer replies a day later: the
second charge posted. The knowledge-base article the agent followed says
duplicate pending authorizations "always" drop off.

**Output (abridged):**

| Dimension | Score | Evidence | Cause |
|---|---|---|---|
| Resolution accuracy | 0 | "one is a pending authorization that will drop off" — second charge posted | process (KB says "always") |
| Process and policy | 2 | Two-factor verification before account details | — |
| Understanding | 2 | Checked billing and identified the pending authorization | — |
| Clarity | 1 | "within a few business days" — no date the customer could check against | agent |
| Ownership | 1 | Stated the charge "will drop off" as certain and offered no follow-up if it posted | agent |
| Tone in action | 2 | Acknowledged the worry, plain language | — |

Critical fail: none. Score (agent-caused only; resolution defect moved to the
fix list): (2 + 2 + 1 + 1 + 2) / (2 × 5) = 0.80 — the resolution-accuracy 0 is
recorded but excluded because its cause is `process`.
Keep: verified identity before discussing charges.
Change: "will drop off within a few business days" → "should drop off by
[date]; if it posts instead, I'll refund it — reply here" — because the
customer came back with the same problem a day later.
Fix list: KB article "duplicate pending authorizations always drop off" is
wrong for this case → billing knowledge owner.
