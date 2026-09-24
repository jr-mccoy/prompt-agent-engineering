---
title: "Human-Agent Handoff Design — Triggers, the Context Packet, Warm vs Cold, and No Repeat Asks"
category: voice-conversational-ui/chatbot-design
description: "Specify the handoff from a chatbot, voice bot, or AI phone agent to a human: a trigger policy (explicit request always honored, failure limits, confidence, risk and vulnerability signals), the transfer type (warm, cold, consult, callback, async), a context-packet schema the agent sees first, what the customer is told, availability fallbacks, the return path to the bot, and measures such as repeat-ask rate; distinct from the handoff bullets in the enterprise customer-service and error-handling prompts (which this expands into a full spec) and from agent_human_in_loop_handoff.md (an AI agent pausing for human approval)."
techniques:
  - CM-02
  - OC-02
  - NE-20
  - DS-06
  - QA-01
difficulty: intermediate
tags:
  - human-handoff
  - escalation
  - warm-transfer
  - contact-center
  - chatbot-design
  - context-transfer
  - customers-repeat-themselves
  - want-a-human
  - bot-gets-stuck
updated: "2026-09-24"
related_prompts:
  - domain-voice-conversational-ui/chatbot-design/chatbot_design_enterprise_customer_service.md
  - domain-voice-conversational-ui/chatbot-design/chatbot_design_error_handling_patterns.md
  - domain-prompt-engineering/agent-workflows/agent_human_in_loop_handoff.md
---

# Human-Agent Handoff Design

**Objective:** Design the moment a conversation moves from a bot to a person
so the customer never has to repeat themselves, the agent can act within
seconds of picking up, and nobody is stranded when no agent is available.

**When to Use:**
- Customers say "I had to explain everything again" after a transfer.
- Agents complain that bot transfers arrive without useful context.
- You are adding an AI chat or voice agent in front of an existing team.
- Escalation rules are scattered across flows and nobody can state them.

**Not this prompt if:**
- You are designing the whole customer-service bot (intents, KB, tickets) →
  `domain-voice-conversational-ui/chatbot-design/chatbot_design_enterprise_customer_service.md`
  — its handoff step is the summary this prompt expands.
- You are designing no-match and reprompt behaviour →
  `chatbot_design_error_handling_patterns.md`.
- An autonomous AI agent needs a human's approval mid-task →
  `domain-prompt-engineering/agent-workflows/agent_human_in_loop_handoff.md`.
- You are designing the phone menu and where transfers occur →
  `domain-voice-conversational-ui/voice-design/voice_design_ivr_call_flow.md`.

## Inputs

1. **Channels**: web chat, messaging, voice bot, phone agent.
2. **Agent side**: platform, queues and skills, hours, typical wait times.
3. **Bot capabilities** and what it can resolve.
4. **Risk topics**: regulated advice, complaints, safety, vulnerable customers.
5. **Current transfer data**, if any: volume, reasons, repeat-ask complaints.
6. **Privacy rules** for what may be passed to agents or stored.

## Method

1. **Write the trigger policy (CM-02).** Each trigger with its rule:
   - **Explicit request** for a person — always honored; the bot may offer
     one quick alternative at most once.
   - **Failure limit** — number of consecutive no-match/failed task attempts.
   - **Low confidence** on a high-impact intent.
   - **Risk topic** — complaint, legal threat, safety, regulated advice.
   - **Vulnerability signal** — distress, bereavement, confusion; hand off
     with priority, not as a failure.
   - **Business rule** — high-value account, specific product lines.
   State which triggers are **must** (bot cannot continue) and which are **offer**.
2. **Choose the transfer type per trigger.**
   - **Warm**: agent receives the packet and joins with the customer waiting.
   - **Cold**: routed to a queue with the packet attached.
   - **Consult**: agent advises the bot or joins silently (only where the
     platform supports it).
   - **Callback / async ticket**: when no agent is available or wait is long.
3. **Define the context packet (OC-02, NE-20).** A schema the agent sees
   first, written so a stranger can act on it: a one-line reason, what the
   customer wants, authentication status, what the bot tried and its result,
   what the customer has already been told (promises, amounts, dates),
   collected fields, and a link to the full transcript. Mark sentiment and
   vulnerability flags as *signals*, not conclusions.
4. **Script the customer side.** What the bot says at the moment of handoff:
   why, what happens next, expected wait, whether they will need to repeat
   anything (the answer should be no), and how to leave a callback.
5. **Plan availability fallbacks.** Out of hours, queue over threshold, or
   no skilled agent: callback, ticket with a stated response time, or
   emergency route. Never end with "no agents available" and nothing else.
6. **Define the return path.** Can the agent hand back to the bot for a
   routine step (payment, survey)? What does the bot know about the agent's
   actions when it resumes?
7. **Prioritize (DS-06).** Rank handoff defects by customer harm: stranded
   customers and lost vulnerability flags first; repeat asks next; cosmetic
   summary issues last.
8. **Self-check (QA-01)** with the Verification list; rate each design choice
   **High / Medium / Low** confidence by the evidence behind it.

## Output Format

```
## Trigger policy
| Trigger | Rule | Must / Offer | Transfer type | Priority |
## Context packet schema (JSON)
## Agent view (what appears first, in order)
## Customer-side script at handoff
## Availability fallbacks
## Return-to-bot path
## Privacy & redaction rules
## Measures
Repeat-ask rate · time to first agent message · transfer-after-transfer rate ·
abandonment during wait · post-handoff CSAT
## Confidence and open items
```

## Verification

- [ ] An explicit request for a person is honored under every rule.
- [ ] Every trigger names a transfer type and a fallback when no agent is free.
- [ ] The context packet includes what the customer has been told.
- [ ] Authentication status is carried, so the agent does not re-verify without reason.
- [ ] Sentiment and vulnerability are labeled as signals with their source.
- [ ] Redaction rules cover card data and anything the policy excludes.
- [ ] Repeat-ask rate is measured (sampled transcripts or agent tagging).

## False-Positive Prevention

1. **A transfer is not a bot failure by definition.** Vulnerability and
   complaint handoffs are correct outcomes; do not count them against the bot.
2. **Do not make customers fight for a person.** Repeated "Are you sure?" or
   forced self-service loops before transfer raise complaints and abandonment.
3. **Do not pass the whole transcript as the summary.** Agents need the one-line
   reason and state first; the transcript is a link.
4. **Do not present sentiment scores as facts.** Automated sentiment is
   error-prone; show the triggering phrase, not a label alone.
5. **Do not pass what the policy forbids.** Card numbers, full identifiers,
   and health details follow the privacy rules even inside the company.
6. **Do not promise wait times you cannot measure.** Use live queue data or
   say "a few minutes" only if that is typical.
7. **Do not design warm transfer where the platform cannot support it.**
   Confirm platform capabilities; mark unconfirmed features Low confidence.

## Example

**Input (summary):** Online electronics retailer; web chat bot + agent
desktop; agents 8am–10pm; average wait 3 minutes. Complaint: customers
repeat order numbers and problems after transfer.

```
## Trigger policy
| Trigger | Rule | Must/Offer | Type | Priority |
|---|---|---|---|---|
| Asks for a person | Any phrasing | Must | Warm if queue < 5 min, else callback | Normal |
| Failed task | 2 consecutive failures on same intent | Offer | Cold | Normal |
| Refund > £200 | Order value rule | Must | Warm | Normal |
| Complaint / legal words | "complaint", "trading standards", "solicitor" | Must | Warm | High |
| Distress signal | e.g. "my dad died, it was his" | Must | Warm, priority queue | High |

## Context packet schema (JSON)
{
  "reason": "Refund request over £200 — bot cannot approve",
  "customer_goal": "Refund for faulty headphones",
  "auth": {"status": "verified", "method": "email + order number"},
  "order": {"id": "[order id]", "item": "headphones", "value_gbp": 249},
  "bot_attempts": [{"step": "troubleshooting guide", "result": "customer says no sound from left side"}],
  "customer_told": ["Refunds over £200 are handled by a person", "Wait is about 3 minutes"],
  "signals": [{"type": "frustration", "evidence": "\"third time I've asked\""}],
  "transcript_url": "[link]"
}

## Agent view
1. Reason + customer goal. 2. Auth status. 3. What they were told.
4. Bot attempts. 5. Signals with evidence. 6. Transcript link.

## Customer-side script
"A member of our team can approve this refund. I've passed on your order and
what you've told me, so you won't need to repeat it. The wait is about 3
minutes — or I can arrange a callback."

## Availability fallbacks
After 10pm: callback booking for next morning + ticket with a stated
response time; distress triggers show the out-of-hours contact line.

## Return-to-bot path
Agent can send the customer back to the bot for the returns-label step; the
bot resumes with the agent's refund decision in context.

## Privacy & redaction
Card numbers masked; delivery address shown only after agent opens order.

## Measures
Repeat-ask rate (weekly sample of 50 handoffs), time to first agent message,
transfer-after-transfer rate, abandonment in queue, post-handoff CSAT.

## Confidence and open items
High: triggers from complaint data. Medium: 5-minute warm/callback threshold.
Low: agent desktop's ability to show the packet in this order — confirm with vendor.
```

## Techniques Used

- **CM-02 Constraint Specification** — must/offer triggers and the always-honored request.
- **OC-02 JSON Schema Specification** — the context packet.
- **NE-20 Third-Party Handoff Package** — a packet a stranger can act on.
- **DS-06 Prioritization and Severity Guidance** — ranking handoff defects by harm.
- **QA-01 Self-Verification** — the no-stranding and no-repeat-ask checks.

## Related Prompts

- `domain-voice-conversational-ui/chatbot-design/chatbot_design_enterprise_customer_service.md` — the full service bot.
- `domain-voice-conversational-ui/chatbot-design/chatbot_design_error_handling_patterns.md` — failures that lead to handoff.
- `domain-prompt-engineering/agent-workflows/agent_human_in_loop_handoff.md` — AI agent pausing for approval.
