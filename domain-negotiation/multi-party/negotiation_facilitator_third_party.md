---
title: "Facilitating a Negotiation You Are Not a Party To — The Neutral Role"
category: negotiation/multi-party
description: "Run a negotiation between other people without becoming a party to it. Establishes the mandate and its limits, sets the process the parties agree to before substance begins, separates the facilitator's control of process from the parties' control of outcome, and supplies the moves that unlock a stalled exchange — caucusing, reframing, reality-testing each side privately, and the single-text procedure. Includes the neutrality-loss warning signs and what to do when you are not actually neutral. Counters the failure that ends a facilitation: drifting from running the process to advocating an outcome."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - DS-01
  - CM-02
  - QA-01
difficulty: advanced
tags:
  - negotiation
  - facilitation
  - neutral
  - process
  - multi-party
updated: "2026-07-26"
reasoning:
  styles: [strategic, empathic, systems, analytic]
  stakes: high
  horizon: variable
  uncertainty: ambiguity
  evidence_quality: moderate
  domain_complexity: cross_domain
  collaboration: small_team
  output_format: structured
  user_role: [executive, manager, pm, hr, lawyer]
  mode: [plan, facilitate, diagnose]
related_prompts:
  - domain-negotiation/multi-party/negotiation_multi_party_alignment.md
  - domain-negotiation/at-the-table/negotiation_impasse_breaker.md
  - domain-negotiation/preparation/negotiation_interest_mapping.md
---

# Facilitating a Negotiation You Are Not a Party To — The Neutral Role

**Objective:** Managers, project leads, HR partners, and in-house counsel are regularly asked to run a negotiation between two other parties — two teams disputing scope, a vendor and an internal customer, two colleagues over resources, a departing employee and their manager. The role is genuinely different from negotiating, and its central discipline is the separation of **process** from **outcome**: the facilitator controls how the conversation runs, and the parties control what they agree to. Every facilitation failure is a version of that boundary breaking down — the facilitator who has a preferred outcome and steers toward it, the one who imposes a settlement, the one whose supposed neutrality is not credible to one side. This prompt sets the mandate, designs the process, supplies the unlocking moves (caucus, reframe, private reality-testing, single-text), and names the warning signs of neutrality loss — including the case where you are not neutral and should say so.

Every other mediation-adjacent prompt in the repo is **party-side** preparation — `domain-legal/divorce/`, `domain-legal/custody/`, and `domain-legal/family-self-advocacy/` all prepare a participant. This is the only one written for the neutral, and it is not legal mediation practice.

**When to use:**
- You have been asked to run a negotiation or dispute between two parties who both report to or work with you.
- Two teams are deadlocked and someone must run the process.
- You are chairing a multi-party session where you have no stake in the terms.
- A facilitation you are running has stalled or your neutrality has been questioned.

**When NOT to use:**
- You are a party with interests in the outcome — you cannot facilitate your own negotiation, and attempting it is the most common failure here.
- The dispute requires formal mediation, legal process, or an investigation — route accordingly; this is not a substitute for either.
- You are preparing one side — use the relevant `preparation/` prompts.

**Audience:** Managers, project leads, HR partners, in-house counsel, and executives asked to run a negotiation between others.

---

## Inputs / Context

1. **The dispute.** What the parties disagree about, as each describes it.
2. **The parties.** Who they are, their relationship, and its history.
3. **Your mandate.** What you have been asked to do, by whom, and what happens if no agreement is reached.
4. **Your actual position.** Whether you have a stake, a preference, or a prior relationship with either party.
5. **Constraints.** Anything neither party can agree to — budget, policy, legal, or a decision already made elsewhere.
6. **Timeline.** What forces resolution, and who imposed it.

---

## Constraints

### Must
- Establish and state the **mandate** explicitly to both parties: what you are doing, what you can and cannot decide, and what happens if they do not agree.
- Separate **process authority from outcome authority**, and say so out loud. You run the conversation; they own the agreement.
- Get **agreement to the process before substance** — how the session runs, who speaks when, confidentiality of caucuses, and how agreement is recorded.
- Disclose any **interest, prior relationship, or preference** at the start. Undisclosed non-neutrality discovered later invalidates the entire process retroactively.
- Use **caucusing** deliberately, with an explicit rule about what carries between rooms and what does not.
- **Reality-test each side privately** rather than arguing with either publicly — this is the facilitator's highest-value move and only works in caucus.
- State what happens on **no agreement**, since parties negotiate differently when the default is known.

### Must Not
- Advocate an outcome, including the one you privately believe is correct. The moment you have a preferred settlement and steer toward it, you are a party with a process role.
- Impose a settlement while calling it facilitation. If you are deciding, say you are deciding — parties can accept a decision, but not a decision presented as their own agreement.
- Carry information between caucuses without explicit permission. One breach ends the usefulness of private sessions permanently.
- Take a position on the merits, even when one side is clearly right. Reality-test both sides privately instead.
- Facilitate where you have an undisclosed stake. Disclose, or decline.
- Let the more forceful party set the process. Process control is the facilitator's only real authority, and conceding it early forfeits the role.

---

## Instructions

### Step 1 — Test your own neutrality and disclose
Before anything: do you have a stake in the outcome, a prior relationship with either party, or a view about who is right? A **preference** is manageable if disclosed and held; a **stake** is disqualifying. Write what you will disclose and how. If you cannot be neutral and cannot be replaced, say so explicitly and reframe the role — "I'm not neutral here, so I'm going to run this as a decision process rather than a facilitation" is a legitimate move; pretending is not.

### Step 2 — Define and communicate the mandate
State to both parties, in the same words to each: what you have been asked to do, what you can decide and what you cannot, whether the outcome is binding, who else will know what, and what happens if they do not reach agreement. Ambiguity about the no-agreement default is the most common source of later grievance, because each party assumes the default favours them.

### Step 3 — Get process agreement before substance
Propose and secure agreement on: session structure and length, who speaks in what order, whether caucuses will be used and what carries out of them, how agreements are recorded, and the ground rules — no interrupting, no relitigating settled points, no personal characterization. Getting explicit assent to the process is what gives you standing to enforce it later, and enforcement without prior agreement reads as bias.

### Step 4 — Open by having each side heard
Each party states their position and — more importantly — what matters to them and why, without interruption. Do not permit rebuttal in this phase. Much apparent deadlock is a party who does not believe they have been heard, and being heard is both free and frequently sufficient to unlock movement. Summarize each side's position back to them in your own words and confirm you have it right; this demonstrates neutrality by doing it symmetrically.

### Step 5 — Reframe from positions to interests
Do publicly what `preparation/negotiation_interest_mapping.md` does privately: ask each side why their position matters, and surface the interests underneath. Then restate the dispute in interest terms for both. A dispute over who gets a resource frequently restates as two different needs that a differently-shaped arrangement satisfies simultaneously.

### Step 6 — Caucus and reality-test privately
Meet each side separately. The rules: state explicitly what will and will not be carried to the other room, and honour it exactly. In caucus, do what you cannot do publicly — reality-test. "If they don't agree, what happens for you?" "What's your alternative here, concretely?" "How would that argument sound to someone who didn't already agree with you?" Reality-testing in the open is heard as taking sides; in caucus it is heard as help, and it is the single most effective thing a facilitator does.

### Step 7 — Use the single-text procedure when positions harden
When both sides are entrenched in competing proposals, stop trading proposals. Draft a single text yourself, circulate it to both, and invite criticism rather than counter-proposals. Revise and recirculate. This works because criticizing a neutral's draft is cognitively and socially easier than conceding to an opponent's proposal, and because it removes the ownership that makes proposals hard to abandon. Make explicit that the text is nobody's position, including yours, until they adopt it.

### Step 8 — Record agreement precisely, and name what is open
Write down what is agreed, in specific terms, and read it back to both parties before anyone leaves. Name the open items explicitly rather than letting them pass. Distinguish clearly between agreements and understandings. Then state the next step with a date and an owner. Vague facilitated agreements reliably reappear as the next dispute, with each party's recollection favouring themselves.

### Step 9 — Adversarial check
- Do you have a preferred outcome, and has any move you made advanced it?
- Would each party independently describe you as neutral — and if not, which one, and why?
- Are you facilitating an agreement, or brokering one you have already decided on?

---

## False-Positive Prevention

1. **Outcome advocacy.** Steering toward the settlement you believe is correct. It is the defining failure of the role, it is usually visible to at least one party, and it converts you from a neutral into a party with process authority.
2. **Imposition disguised as facilitation.** Deciding the outcome while presenting it as the parties' agreement. Parties can accept a decision openly made; what they do not accept, and later resent, is a decision presented as their own.
3. **Caucus leakage.** Carrying information between private sessions without permission — including inadvertently, by referencing something only one side said. One breach ends the usefulness of caucusing for the remainder of the process.
4. **Public reality-testing.** Challenging a party's position in front of the other. However accurate, it is heard as taking sides and costs the neutrality that makes the whole role work. Test in caucus.
5. **Undisclosed interest.** Facilitating with a stake or prior relationship that has not been named. When discovered — and it usually is — it retroactively invalidates the entire process and any agreement reached in it.
6. **Process capture.** Letting the more forceful party determine how the session runs. Process control is the facilitator's only genuine authority; conceding it early means spending the rest of the session as a spectator.
7. **Vague recording.** Ending with an agreement in principle and no specific written terms. Facilitated agreements are more prone to divergent recollection than negotiated ones, because neither party drafted it.
8. **Undefined no-agreement default.** Failing to state what happens if they do not agree. Each party assumes the default favours them, both negotiate accordingly, and the discovery at the end produces a grievance aimed at you.

---

## Output Format

```
# Facilitation Plan — [dispute]

## Neutrality check
Stake in the outcome: [none / describe]
Prior relationship: [...]
Preference about who is right: [...]
Verdict: can facilitate / preference disclosed / not neutral — reframing as [decision process]
Disclosure to be made: "[...]"

## Mandate (same words to both parties)
What I've been asked to do: [...]
I can decide: [...] · I cannot decide: [...]
Binding? [...] · Who else will know what: [...]
If no agreement is reached: [...]

## Process agreement (secured before substance)
Structure and length: [...]
Speaking order: [...]
Caucuses used? [y/n] — what carries out: [...]
Recording method: [...]
Ground rules: [...]
Explicit assent obtained from both: [y/n]

## Opening — being heard
Each side states position + what matters and why, no rebuttal.
Summary read back to [party A]: "[...]"
Summary read back to [party B]: "[...]"

## Interest reframe
| Party | Position | Underlying interest |
|---|---|---|
| A | [...] | [...] |
| B | [...] | [...] |
Dispute restated in interest terms: [...]

## Caucus plan
| Party | Reality-test questions | What may be carried out |
|---|---|---|
| A | "[...]" | [...] |
| B | "[...]" | [...] |

## Single-text (if positions harden)
Trigger: [both entrenched in competing proposals]
Draft circulated as: "nobody's position, including mine, until adopted"
Invite: criticism, not counter-proposals

## Agreement record
Agreed (specific): [...]
Open items (named explicitly): [...]
Agreements vs. understandings: [...]
Next step / owner / date: [...]
Read back before anyone left: [y/n]

## Adversarial check
- Do I have a preferred outcome, and has any move advanced it? [...]
- Would both parties independently call me neutral? [...]
- Am I facilitating or brokering a decision I've already made? [...]
```

---

## Verification

- [ ] Neutrality tested before anything else; stake vs. preference distinguished.
- [ ] Any interest, preference, or prior relationship disclosed at the start.
- [ ] Non-neutral cases reframed openly as a decision process rather than concealed.
- [ ] Mandate stated in the same words to both parties, including the no-agreement default.
- [ ] Process agreement secured with explicit assent before substance begins.
- [ ] Each side heard without rebuttal, with symmetrical read-backs.
- [ ] Dispute reframed from positions to interests for both sides.
- [ ] Caucus rules state exactly what carries between rooms.
- [ ] Reality-testing confined to caucus, never conducted publicly.
- [ ] Single-text procedure available and framed as nobody's position.
- [ ] Agreement recorded specifically and read back before anyone leaves; open items named.
- [ ] Adversarial check tests for outcome advocacy and asks whether both parties would call you neutral.
- [ ] No position taken on the merits at any point.
- [ ] No settlement imposed while described as facilitation.
