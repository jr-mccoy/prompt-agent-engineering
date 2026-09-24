---
title: "Language Sim — Service Breakdown: Repairing a Conversation That Is Going Wrong"
category: conversation-practice
description: "A target-language service scene (lost luggage, wrong order, double charge, hotel mix-up) in which the partner is polite but scripted to go wrong in three beats (a misunderstanding, a wrong fix, a policy wall), so the learner must use repair strategies to reach a confirmed outcome, scored on repair moves rather than grammar; distinct from the cooperative partner in learn_daily_conversation_drill.md and from conversation_practice_simulator.md Preset D, where you calm an angry customer in your own language."
techniques:
  - CM-01
  - ST-16
  - DS-01
  - QA-01
difficulty: intermediate
tags:
  - language-learning
  - role-play
  - repair-strategies
  - travel
  - customer-service
  - speaking-practice
updated: "2026-09-24"
related_prompts:
  - domain-conversation-practice/conversation_lang_sim_master_template.md
  - domain-education-teaching/learner/language/learn_daily_conversation_drill.md
  - domain-conversation-practice/conversation_practice_simulator.md
---

# Language Sim — Service Breakdown

**Objective:** Practise the moment a textbook dialogue never covers: the clerk misunderstands, offers the wrong fix, or cites a rule. The partner is courteous but constrained, and the scene is scripted to go wrong three times. The learner succeeds by **repairing** the conversation until the outcome is confirmed, not by producing perfect sentences.

**When to Use:**
- You can order food and book a room when things go right, but freeze when they go wrong.
- You are travelling or moving abroad soon and want rehearsal for lost bags, wrong orders, billing errors and booking mix-ups.
- You tend to accept the first offer, even the wrong one, because arguing in the target language feels too hard.

**Not this prompt if… / distinct from**
- You want a smooth, cooperative exchange. Use `domain-education-teaching/learner/language/learn_daily_conversation_drill.md`. Its partner helps you. This partner is scripted to obstruct, politely.
- You are the agent calming an angry customer, in your own language. Use `conversation_practice_simulator.md` Preset D. The roles and the skill are reversed there.
- You have a real dispute and need to document it. Use `domain-legal/personal-self-advocacy/consumer-scams/legalprep_consumer_complaint_documentation_organizer.md`.

## Inputs

Fill the master template's slots (`conversation_lang_sim_master_template.md`): language and variety, L1, level, register (the default is formal), and correction mode (the default is **delayed**, because repair needs uninterrupted flow). Then choose one of:

| Scenario | Partner | Goal the learner must reach |
|---|---|---|
| Lost luggage | Airline desk agent | A file reference number, a delivery address confirmed, an interim-expenses answer |
| Wrong order | Restaurant server | The correct dish, or removal from the bill |
| Double charge | Shop cashier or bank line | A refund route with a timeframe |
| Hotel mix-up | Receptionist | The booked room type, or a stated remedy |
| Custom | Any service role | Stated by the learner |

## The three breakdown beats (ST-16)

The partner is **polite, busy and constrained, never hostile**. Across the scene they play each beat once, in this order, and move on only when the learner performs a repair (or after two failed attempts, when the partner partly concedes so the scene can continue):

1. **Misunderstanding.** The partner mishears one key detail: the flight number, the dish, the amount. They act on the wrong detail until the learner corrects it.
2. **Wrong fix.** The partner offers a plausible but wrong solution ("I can give you a voucher"). Accepting it ends the beat as *accepted wrong fix*.
3. **Policy wall.** "That's not possible, it's the policy." The learner must ask for an alternative, ask who can decide, or restate their need.

## Repair-strategy taxonomy used for scoring (DS-01)

| Strategy | Example (English gloss) |
|---|---|
| Clarify / correct | "No, not 214, it's 241." |
| Spell or confirm a detail | "B as in Barcelona…" / "So that's the 15th?" |
| Reject an offer politely | "Thank you, but I'd prefer…" |
| Restate the need | "What I need is my bag delivered to…" |
| Ask for an alternative or escalation | "Is there another option?" / "Could I speak to…?" |
| Check understanding | "Did you mean I have to come back?" |
| Close with confirmation | "So, reference ABC123, delivery tomorrow, correct?" |

## The prompt block (paste into the master template's `[SCENARIO BLOCK]`)

```
SCENARIO: [scenario] — you are [partner role]. I am the customer.
My goal: [goal from the table].
Play these three breakdown beats in order, once each, at natural moments:
1) Misunderstand one key detail I give you and act on the wrong version.
2) Offer a plausible but wrong solution.
3) Cite a policy that blocks my first request.
Stay polite, busy and realistic. Never hostile, never helpful beyond your role.
Move past a beat only when I repair it (correct, reject, restate, ask for an alternative),
or after two failed attempts, when you partly concede.
DEBRIEF SCORING FOCUS: for each beat, which repair strategy I used (quote me),
whether it worked, and one better line in [TARGET_LANGUAGE]. Say whether I confirmed
the outcome before closing.
```

## Method

1. **Confirm settings and scenario (CM-01)** in L1. Name the goal. Do *not* reveal the beats. They must surprise the learner.
2. **Run the scene** under the master template's rules and the beat order.
3. **Debrief (QA-01)** using the master template's five headings. Heading 4, the scenario focus, is a per-beat table: beat, the learner's repair (quoted), strategy, outcome, and a better line in the target language.

## Output Format

In scene: partner lines only. The debrief adds this table under heading 4:

```
| Beat | Your repair (quoted) | Strategy | Outcome | Stronger line |
Closed with confirmation? yes/no — [quote]
```

## Verification

- [ ] All three beats occurred, in order, and none was announced in advance.
- [ ] The partner stayed polite, never hostile, and never solved the problem for the learner.
- [ ] Each beat's outcome is one of: repaired, partly conceded after two attempts, or accepted wrong fix.
- [ ] The debrief scores repair strategies before form errors.
- [ ] A closing confirmation was checked for.

## False-Positive Prevention

1. **Hostile partner.** Turning the clerk into an antagonist makes it a composure exercise, not repair practice. Keep them busy and constrained.
2. **Instant fold.** A partner who accepts the first correction removes the practice. Hold each beat until a genuine repair.
3. **Endless wall.** A partner who never concedes traps a lower-level learner. Partly concede after two attempts.
4. **Grammar over repair.** "Scusi, può *ripete*?" (for *ripetere*) still repaired the beat. Score the repair first.
5. **Accepted wrong fix counted as success.** Leaving with a voucher when you needed your bag is a failed outcome, however fluent the exchange.
6. **Missing close.** Leaving without confirming the reference number or time is the most common real-world failure. Always check for it.

## Example Output

```
Settings: Italian | L1 English | A2+ | Lei | Delayed | Lost luggage at Bologna airport

Partner: Buongiorno. Mi dice il numero del volo?
Learner: AZ 1327 da Londra.
Partner: AZ 1237… mi dispiace, quel volo è arrivato ieri.        ← beat 1
Learner: No, scusi: uno-tre-due-sette. Oggi.
Partner: Ah, 1327. Sì. Le posso dare un buono per il bar, intanto.  ← beat 2
Learner: Grazie, ma ho bisogno della valigia. Può mandarla all'hotel?
Partner: Consegniamo solo agli indirizzi di residenza, è la regola. ← beat 3
Learner: C'è un'altra possibilità?
Partner: Può ritirarla qui domani dopo le 10.
Learner: Va bene. Allora: numero pratica…?
Partner: BLQAZ48213.
Learner: END

Debrief (4. Scenario focus)
| Beat | Your repair | Strategy | Outcome | Stronger line |
| 1 | "No, scusi: uno-tre-due-sette" | Clarify, digit by digit | Repaired | — |
| 2 | "Grazie, ma ho bisogno della valigia" | Reject + restate need | Repaired | — |
| 3 | "C'è un'altra possibilità?" | Ask for alternative | Repaired (pickup) | "E per le spese nel frattempo?" (interim expenses were missed) |
Closed with confirmation? Partly: you got the reference but did not confirm the pickup time back.
```

## Techniques Used

- **CM-01 (Explicit Context Framing):** the scenario and goal are fixed up front, and the beats are hidden.
- **ST-16 (Behavioral Trait Declarations):** the partner is declared polite, busy and constrained, and plays three scripted beats.
- **DS-01 (Framework Application):** the repair-strategy taxonomy structures the scoring.
- **QA-01 (Self-Verification):** a per-beat debrief with quoted repairs and a check for closing confirmation.

## Related Prompts

- `domain-conversation-practice/conversation_lang_sim_master_template.md`: slots, correction modes and commands.
- `domain-education-teaching/learner/language/learn_daily_conversation_drill.md`: the cooperative version of these scenes.
- `domain-conversation-practice/conversation_practice_simulator.md`: hard conversations in your own language.
