---
title: "IVR & Phone-Agent Call-Flow Design — Speech and DTMF, Authentication Gates, Containment vs Transfer"
category: voice-conversational-ui/voice-design
description: "Design a telephone call flow for an IVR or AI phone agent: route by caller intent and volume, choose speech, DTMF, or both per node, place authentication and payment gates only where data requires them, set an explicit containment-versus-transfer policy with an always-available route to a person, and specify every node in a table a telephony team can build; distinct from the general dialog state machine prompt, the chatbot customer-service design (text channels), and the human-agent handoff prompt (what happens at the transfer itself)."
techniques:
  - CM-02
  - ST-02
  - RT-02
  - QA-08
  - OC-03
difficulty: advanced
tags:
  - ivr
  - telephony
  - dtmf
  - call-flow
  - authentication
  - containment
  - voice-design
updated: "2026-09-24"
related_prompts:
  - domain-voice-conversational-ui/dialog-architecture/dialog_architecture_state_machine_design.md
  - domain-voice-conversational-ui/chatbot-design/chatbot_design_human_agent_handoff.md
  - domain-voice-conversational-ui/voice-ux/voice_ux_error_recovery_patterns.md
---

# IVR & Phone-Agent Call-Flow Design

**Objective:** Produce a buildable call flow for a phone line — IVR or AI
voice agent — that gets each caller to resolution or to the right person in
the fewest steps, authenticates only when the task needs it, and never traps
a caller who needs a human.

**When to Use:**
- Designing a new IVR or replacing touch-tone menus with speech or an AI agent.
- Callers complain about "menu hell," repeated identity questions, or not
  reaching a person.
- Containment is being pushed up and you need a policy that does not simply
  block transfers.

**Not this prompt if:**
- You need a generic dialog state machine for any channel →
  `domain-voice-conversational-ui/dialog-architecture/dialog_architecture_state_machine_design.md`.
- You are designing a text/chat customer-service bot →
  `chatbot_design_enterprise_customer_service.md`.
- You need the detailed transfer mechanics (context packet, warm vs cold,
  queue behavior) → `chatbot_design_human_agent_handoff.md`; this prompt
  decides *when* to transfer and hands off to that one for *how*.
- You need realtime turn-taking for an LLM voice agent →
  `voice_design_realtime_turn_taking.md`.

> **Compliance note:** call recording notices, identity verification, and
> card-payment capture carry legal and industry rules that vary by
> jurisdiction and sector. This prompt marks them `[VERIFY with compliance]`
> and never asserts that a design is compliant.

## Inputs

1. **Call reasons** with approximate monthly volumes and current handling time.
2. **Which reasons can be self-served**, and which systems they need.
3. **Authentication methods available** (caller ID match, account number,
   PIN, one-time code, knowledge questions).
4. **Agent groups**, hours, and skills.
5. **Caller population**: languages, accessibility needs, typical environment
   (mobile, noisy, landline).
6. **Current flow and pain points** (abandon points, zero-out rate), if any.

## Method

1. **Set the constraints (CM-02).** Emergency or safety reasons that must reach
   a person or instruction immediately; required disclosures; languages;
   hours; and the rule that a caller can always reach a person (immediately,
   or after a stated number of attempts — decide which, per reason).
2. **Order the entry (ST-02).** Greeting → required disclosures → emergency
   triage (if any) → language (only if needed) → intent capture. Keep the
   path to intent capture under about 20 seconds.
3. **Choose the input mode per node (RT-02).** Evaluate each node on accuracy,
   privacy, and accessibility:
   - **Speech** for open intent capture ("In a few words, tell me why you're calling").
   - **DTMF** for digit strings (account numbers, PINs, card data), noisy
     environments, and callers who cannot or prefer not to speak.
   - **Both** for short menus and yes/no.
   Menus offered as lists: no more than four or five options, most frequent first.
4. **Place gates only where the data demands (QA-08).**
   - **Authentication gate** before any account-specific data or action;
     not before general information or emergencies.
   - **Step-up gate** for high-risk actions (payment method change, address change).
   - **Payment gate** with secure DTMF capture and masked audio
     `[VERIFY with compliance]`.
   Authenticate once per call and pass the result to agents so callers are not re-asked.
5. **Write the containment-vs-transfer policy.** For each intent: target
   outcome (self-serve / transfer / either), maximum failed attempts before
   transfer, and zero-out behaviour ("agent" or 0). Containment counts only
   calls resolved, not calls that hung up.
6. **Specify error handling.** No-input and no-match counts, timeouts, and the
   escalation after the limit (reprompt → rephrase with examples → DTMF
   fallback → transfer).
7. **Tabulate every node (OC-03)** so the telephony team can build it, and
   rate confidence for each design decision: **High** (backed by the supplied
   volumes or call data), **Medium** (common practice, not yet tested here),
   **Low** (assumption to validate).

## Output Format

```
## Constraints
Emergency reasons · Disclosures [VERIFY] · Languages · Hours · Reach-a-person rule
## Intent map
| Intent | Volume | Self-serve? | Needs auth? | Target outcome | Max attempts before transfer |
## Entry sequence
## Call-flow nodes
| Node | Prompt (spoken) | Input (speech/DTMF/both) | Valid inputs | No-input/no-match | Next | Gate |
## Gates
Authentication · Step-up · Payment
## Containment vs transfer policy
## Transfer points (→ handoff design)
## Measures
Resolved-in-IVR rate · zero-out rate · abandon by node · repeat-call rate within 7 days
## Confidence and open items
```

## Verification

- [ ] Emergency or safety reasons bypass authentication and menus.
- [ ] Every node has a no-input and no-match path that ends somewhere other than a hang-up.
- [ ] A person is reachable from every node under the stated rule.
- [ ] Digit strings and payment data use DTMF, with masking noted `[VERIFY]`.
- [ ] No gate precedes a task that does not need it.
- [ ] Authentication status travels with the transfer.
- [ ] Containment is measured as resolution, with repeat-call rate as a check.

## False-Positive Prevention

1. **High containment is not success on its own.** Callers who hang up or call
   back count against it; always pair it with repeat-call rate.
2. **Do not hide the route to a person.** Blocking zero-out raises abandonment
   and complaints; decide the rule openly per intent.
3. **Do not replace every menu with open speech.** Short, well-ordered DTMF
   menus often beat open speech for small, fixed option sets.
4. **Do not authenticate by default.** General information and emergencies
   should not require identity checks.
5. **Do not read sensitive data back in full.** Confirm with partial values
   ("the card ending 42").
6. **Do not claim compliance.** Mark recording, identity, and payment rules
   `[VERIFY with compliance]`.
7. **Do not design for the average caller only.** Include DTMF fallback,
   slower speech, and repeat options for accessibility.

## Example

**Input (summary):** Regional water utility, ~40,000 calls/month. Reasons:
leak or no water (22%), pay bill (30%), balance/usage (25%), move service
(15%), other (8%). Auth available: caller ID match + 6-digit account PIN.

```
## Constraints
Emergency: leak / no water → instructions + priority queue, no auth.
Disclosure: call recording notice [VERIFY with compliance]. Languages: EN, ES.
Hours: agents 7am–7pm; emergency line 24/7. Reach-a-person: immediate for
emergencies and "move service"; after 2 failed attempts elsewhere.

## Intent map
| Intent | Vol. | Self-serve? | Auth? | Target | Max attempts |
|---|---|---|---|---|---|
| Leak / no water | 22% | Partly (outage lookup by postcode) | No | Either | 1 |
| Pay bill | 30% | Yes | Yes + payment gate | Self-serve | 2 |
| Balance/usage | 25% | Yes | Yes | Self-serve | 2 |
| Move service | 15% | No | Yes | Transfer | 0 |
| Other | 8% | No | No | Transfer | 0 |

## Entry sequence
Greeting + recording notice (≈8s) → "Para español, oprima 2" → "If you're
reporting a leak or have no water, say 'leak' or press 1" → open intent capture.

## Call-flow nodes (excerpt)
| Node | Prompt | Input | Valid | No-input/no-match | Next | Gate |
|---|---|---|---|---|---|---|
| N3 Intent | "In a few words, what are you calling about?" | Speech + DTMF menu fallback | 5 intents | Reprompt with examples → DTMF menu → agent | by intent | — |
| N5 Auth | "Enter your six-digit account PIN." | DTMF | 6 digits | Reprompt → agent (auth status: failed) | N6 | Auth |
| N7 Pay | "Enter your card number, then press pound." | DTMF, masked | 13–19 digits | Reprompt → agent | N8 | Payment [VERIFY] |

## Gates
Auth: caller ID match skips to PIN only; no ID match → account number + PIN.
Step-up: none needed (no account changes in IVR). Payment: masked DTMF [VERIFY].

## Containment vs transfer policy
Target self-serve: pay, balance. Transfer immediately: move service, other.
Emergencies: outage lookup, then offer priority agent.

## Transfer points
From N3 (other/move), N5 (auth failed), N7 (payment failure), any "agent"
→ see chatbot_design_human_agent_handoff.md for context packet.

## Measures
Resolved-in-IVR for pay/balance; zero-out by node; abandon at N5; 7-day repeat calls.

## Confidence and open items
High: intent ordering (from volumes). Medium: 2-attempt limit. Low: speech
accuracy for postcode capture — test DTMF alternative. [VERIFY] recording notice
wording and payment capture with compliance.
```

## Techniques Used

- **CM-02 Constraint Specification** — emergency, disclosure, and reach-a-person rules.
- **ST-02 Structured Sequential Instructions** — entry order and error escalation.
- **RT-02 Multi-Dimensional Analysis** — input mode by accuracy, privacy, accessibility.
- **QA-08 Gate-Based Verification** — authentication, step-up, and payment gates.
- **OC-03 Markdown Table Specification** — the buildable node table.

## Related Prompts

- `domain-voice-conversational-ui/dialog-architecture/dialog_architecture_state_machine_design.md` — generic dialog states.
- `domain-voice-conversational-ui/chatbot-design/chatbot_design_human_agent_handoff.md` — the transfer itself.
- `domain-voice-conversational-ui/voice-ux/voice_ux_error_recovery_patterns.md` — reprompt escalation.
