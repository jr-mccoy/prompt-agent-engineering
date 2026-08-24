---
title: "Crisis Comms Draft and Drill"
category: decision-making
description: "Produce the actual artifacts a leader needs in the first 60 minutes of a crisis: an internal holding statement, an external holding statement, a single-page audience matrix, and a 10-minute spokesperson drill script keyed to the be-first / be-right / be-credible discipline. Optimized for use under time pressure, not as a framework reference."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - RP-02
  - CM-02
  - QA-04
  - DS-02
difficulty: intermediate
tags:
  - decision-making
  - crisis-communication
  - drill
  - holding-statement
  - spokesperson-prep
updated: "2026-04-26"
related_prompts:
  - domain-decision-making/decisioning_crisis_communication_playbook.md
  - domain-decision-making/decisioning_crisis_severity_triage.md
  - domain-decision-making/decisioning_rapid_stakeholder_alignment.md
  - domain-decision-making/decisioning_escalation_decision_tree.md
---

# Crisis Comms Draft and Drill

**Objective:** In a single pass, produce the actual artifacts a leader will use inside the first 60 minutes of a crisis: (1) an internal holding statement, (2) an external holding statement, (3) a one-page audience matrix scoped to the immediate window, and (4) a 10-minute spokesperson drill script with rehearsable Q&A. The output is the artifact the user takes into the room — not a framework to read later.

**When to Use:**
- The crisis just happened (minutes ago, not days). The user needs text to send and a script to rehearse, now.
- A spokesperson must speak publicly within the next two hours and has not yet practiced.
- The org has a full crisis communication framework but no current draft for *this* incident.
- Pre-drilling: rehearsing a likely scenario before it happens, to build muscle memory.

**When NOT to use:**
- The user has not yet triaged severity. Run `decisioning_crisis_severity_triage.md` first.
- The user wants the full multi-phase framework (holding → update → resolution → trust rebuilding). Use `decisioning_crisis_communication_playbook.md` instead.
- The crisis is over and the user is preparing a post-mortem. Use a post-mortem prompt.
- The user does not yet know who the affected audiences are. Run an audience scoping pass first.

**Audience:** Founders, CEOs, comms leads, chiefs of staff, incident commanders, anyone who has to put a statement out under time pressure and may have to deliver it themselves.

---

## Inputs / Context

1. **What happened.** Two to four sentences. Plain language. No spin. If facts are uncertain, mark each fact as `confirmed` or `unconfirmed`.
2. **What is currently known vs. unknown.** Two short lists. Be honest about the gap.
3. **Who is already affected.** Customers, employees, partners, regulators, public. List in priority order.
4. **The forcing function.** What event triggered the need for comms now (a journalist called, a customer tweeted, a regulator deadline, a status page outage, an internal leak).
5. **Who will deliver it.** Name and role. If unknown, the prompt will recommend a default based on severity.
6. **Time available before first delivery.** In minutes.
7. **Hard constraints.** Anything legal, regulatory, or contractual that limits what can be said (e.g., "cannot name vendor under NDA," "regulator notification due in 72h").

If "what happened" is empty or contains only speculation, **stop** — drafting a statement on speculation creates more crisis than it solves. Ask the user to fill in confirmed facts first.

---

## Constraints

### Must
- Produce four artifacts: internal holding, external holding, audience matrix (this hour only), 10-minute drill script.
- Apply the **be first / be right / be credible** discipline to every statement: be first means do not stay silent; be right means do not state unverified facts; be credible means take ownership and acknowledge uncertainty.
- Mark every factual claim in every draft as `[confirmed]` or `[unconfirmed]`. Unconfirmed facts must be removed or rephrased before publication; flag this back to the user.
- Every statement must include a specific next-update commitment with a clock time, not "soon."
- The drill script must include three hard questions the spokesperson is most likely to be asked, with a short scripted response and a one-line "what to do if pressed."
- The audience matrix is scoped to **the next 60 minutes only** — not the full lifecycle. Anything beyond that hour belongs in the playbook prompt.

### Must Not
- Speculate about cause. "We are investigating" is the only acceptable cause-language until investigation is complete.
- Use the phrase "no comment." It implies guilt.
- Use passive voice to deflect ownership ("mistakes were made"). Use first-person plural where the org is responsible.
- Promise an outcome ("we will resolve this by X") unless the user has explicitly confirmed it.
- Inflate scope ("this will not happen again") — credibility erodes faster from broken promises than from incomplete answers.
- Borrow legal boilerplate without adapting to the actual situation.
- Drift into the full multi-phase playbook. This prompt produces the first 60 minutes of artifacts only.

---

## Instructions

### Step 1 — Restate facts with confirmation tags
Restate "what happened" as a single paragraph with each clause tagged `[confirmed]` or `[unconfirmed]`. If any sentence is fully unconfirmed, rewrite as a question to the user before continuing. The drafts depend on this filter.

### Step 2 — Apply the discipline
For each of be-first / be-right / be-credible, write a one-line read on the current state:
- **Be first:** What is the latest moment we can issue something without losing narrative control? (Express as clock time.)
- **Be right:** What facts are we *not* willing to state in a public-facing channel until verified?
- **Be credible:** What ownership statement does the org need to make to maintain trust?

These three lines drive the tone of the drafts.

### Step 3 — Draft the internal holding statement
Audience: employees and the response team. Goal: align the org, prevent freelance public statements, name the lead, name the next update time.

Format:
- One sentence stating what the org is aware of (using only `[confirmed]` facts).
- One sentence naming the response lead and single point of contact.
- One sentence with a do-not-speculate-publicly instruction.
- One sentence with the next internal update time.

### Step 4 — Draft the external holding statement
Audience: customers, partners, public, media — whichever is most exposed in the next 60 minutes.

Format:
- One sentence acknowledging awareness.
- One sentence on what is and is not yet known (frame the unknown as actively being investigated).
- One sentence on what affected parties should do right now (or "no action required at this time" if true).
- One sentence with a specific next-update commitment.

If the external statement would force inclusion of an `[unconfirmed]` fact, route the fact back to the user and pause that draft.

### Step 5 — Audience matrix for the next 60 minutes
Build a small matrix limited to audiences who must hear from the org *before the next hour ends*. Defer the full lifecycle map to the playbook.

Columns: Audience | Channel | Message scope | Owner | Send by (clock time).

Rows: only audiences with first-hour exposure. Typical first-hour set: response team, exec leadership, any customer cohort already affected and observing impact, regulators with statutory short windows.

### Step 6 — Spokesperson 10-minute drill script
This is the core artifact for the person who will speak. Structure:

1. **The 30-second core message.** Three sentences the spokesperson will say verbatim if their mind goes blank: (a) what we know, (b) what we are doing, (c) when we will say more.
2. **Three hard questions and scripted answers.** Pick the three questions most likely to be asked given the inputs. For each: the question, a 2–3 sentence response, and a one-line "if pressed" follow-up.
3. **Three landmines.** Phrases the spokesperson must not use under stress (examples: "no comment," "we believe," "as far as we know," "I'm not sure," "off the record"). For each landmine, write the safe substitute.
4. **The bridge.** A one-line transition the spokesperson can use to redirect any unanswerable question back to the core message: "[Bridge phrase] — what I can confirm right now is..."
5. **The exit.** A scripted closing sentence that ends the conversation without leaving a vacuum: "We will have an update by [time]. Thank you."

### Step 7 — Pre-publication gate
Output a checklist the user must clear before sending any of the four artifacts:
- [ ] Every `[unconfirmed]` tag has been resolved to `[confirmed]` or removed.
- [ ] Legal review (if a regulated industry or material exposure) has signed off.
- [ ] Spokesperson has run the drill script aloud at least once.
- [ ] Next-update clock times are realistic and on someone's calendar.
- [ ] Internal holding goes out before external holding (do not invert).

---

## False-Positive Prevention

1. **Drafting on speculation.** If "what happened" contains unverified claims, the prompt produces credible-sounding text grounded in fiction. Tag and refuse.
2. **Borrowed boilerplate trap.** Generic statements ("we take this seriously") read as evasive when not paired with specific action. Every statement must include at least one specific commitment.
3. **Spokesperson over-rehearsal.** A spokesperson who memorizes only the 30-second core sounds robotic. The drill must include landmines and bridges, not just the safe script.
4. **Severity inflation.** A holding statement that overstates severity creates its own crisis. If severity is unclear, draft for the verified facts, not the worst plausible interpretation.
5. **Audience overshoot.** Notifying audiences who are not yet affected creates noise and reduces trust when real notifications come later. The 60-minute matrix must include only currently-exposed audiences.
6. **Legal-paralysis trap.** Waiting for full legal sign-off on every word can blow the be-first window. Pre-clear the holding-statement template with legal in calm times so first-hour drafts can move faster.
7. **Inverted ordering.** External statement before internal statement causes employees to learn from media. The output must enforce internal-first.
8. **Promise drift.** "We will fix this by tomorrow" sounds reassuring but creates a second crisis if missed. Promises must be replaced with commitments to next *updates*, not next *resolutions*.

---

## Output Format

```
# Crisis comms — draft + drill (first 60 minutes)

**Incident (one-paragraph factual restatement with [confirmed]/[unconfirmed] tags):**
[restated facts with tags]

**Discipline read:**
- Be first: [latest acceptable clock time]
- Be right: [facts we will not state publicly until verified]
- Be credible: [ownership statement the org must make]

---

## 1. Internal holding statement
**To:** [employees / response team]
**Channel:** [Slack all-hands / company-wide email]
**Send by:** [clock time]

> [draft text — 4 sentences max]

## 2. External holding statement
**To:** [primary external audience]
**Channel:** [status page / press / customer email]
**Send by:** [clock time]

> [draft text — 4 sentences max]

[If any [unconfirmed] facts blocked the external draft, list them here for the user to resolve before publication.]

## 3. First-60-minutes audience matrix

| Audience | Channel | Message scope | Owner | Send by |
|----------|---------|----------------|-------|---------|
| [...]    | [...]   | [...]          | [...] | [time]  |

## 4. Spokesperson 10-minute drill script

**30-second core message (verbatim):**
> [3 sentences]

**Hard Q&A (3 questions):**
1. **Q:** [question]
   **A:** [2–3 sentences]
   **If pressed:** [one line]
2. **Q:** [question]
   **A:** [2–3 sentences]
   **If pressed:** [one line]
3. **Q:** [question]
   **A:** [2–3 sentences]
   **If pressed:** [one line]

**Landmines (do not say → say instead):**
- "[banned phrase]" → "[safe substitute]"
- "[banned phrase]" → "[safe substitute]"
- "[banned phrase]" → "[safe substitute]"

**Bridge phrase:**
> "[transition sentence to redirect to core message]"

**Exit line:**
> "[closing sentence]"

---

## Pre-publication gate
- [ ] All [unconfirmed] tags resolved.
- [ ] Legal sign-off (if required).
- [ ] Spokesperson ran the drill script aloud.
- [ ] Next-update clock times on the calendar with owners.
- [ ] Internal statement goes out before external statement.
```

---

## Verification

- [ ] Every factual claim in both drafts is tagged `[confirmed]` or `[unconfirmed]`.
- [ ] Both holding statements include a next-update commitment with a clock time.
- [ ] No statement uses "no comment," passive deflection, or unverified cause language.
- [ ] The audience matrix is limited to first-60-minutes exposure only.
- [ ] The drill script contains the 30-second core, 3 Q&A pairs, 3 landmines with substitutes, a bridge phrase, and an exit line.
- [ ] The pre-publication gate is present and checkable.
- [ ] Internal-before-external ordering is enforced.
- [ ] If any unconfirmed fact blocked drafting, the user is told what to verify before publication.
