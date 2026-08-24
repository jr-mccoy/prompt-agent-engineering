---
title: "Prebunking Design — Warning People Before the Claim Arrives"
category: psy-ops/counter-messaging
description: "Design advance inoculation against an expected false claim: a forewarning, a weakened exposure to the technique, and a refutation the audience can carry themselves. Targets the manipulation technique rather than the specific claim, so the protection generalizes. Includes the honesty constraint that prebunking a claim which turns out to be true is a serious failure, and the timing constraint that prebunking after arrival is just debunking."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - CM-02
  - QA-01
difficulty: advanced
tags:
  - psy-ops
  - prebunking
  - inoculation
  - communications
  - counter-messaging
updated: "2026-07-28"
reasoning:
  styles: [design, analytic, protective]
  stakes: high
  horizon: weeks
  uncertainty: ambiguity
  evidence_quality: moderate
  domain_complexity: cross_domain
  collaboration: team
  output_format: inoculation_design
  user_role: [communications, policy, educator, trust_and_safety]
  mode: [design, decide, act]
related_prompts:
  - domain-psy-ops/counter-messaging/psyops_debunk_and_correction_design.md
  - domain-psy-ops/counter-messaging/psyops_rumor_response_triage.md
  - domain-psy-ops/organizational-red-team/psyops_narrative_vulnerability_assessment.md
---

# Prebunking / Inoculation Design

**Objective:** Design advance protection against a false claim you expect an audience to encounter, on the inoculation model: a **forewarning** that an attempt is coming, a **weakened exposure** to the manipulation technique, and a **refutation the audience can reconstruct themselves** when they meet the real thing. The mechanism is closer to a vaccine than to an argument — the audience is not being told what to think but shown how a specific move works, so they recognize it unaided.

The strongest design choice available is to **target the technique rather than the claim**. Inoculating against "the specific false statistic that will circulate next week" protects against one claim. Inoculating against "numbers presented without their base rate, which makes any risk look alarming" protects against every instance of that move, including ones you did not anticipate and ones that come from your own side.

Two constraints do most of the work in keeping this honest. First, **timing**: prebunking must precede exposure. After the claim has landed, this is debunking, which is a different and harder problem with a different design. Second, and more seriously: **prebunking a claim that turns out to be true is a grave failure**. It uses a protective technique to pre-emptively discredit accurate information, and an organization that does it has manufactured immunity against the truth. The truth check on the target claim is therefore not a formality.

**When to use:**
- You can predict, with reason, a specific false claim or technique your audience will meet.
- A recurring seasonal or event-driven claim is due again — an election, a public health cycle, a product launch.
- You are building durable media literacy rather than responding to an incident.
- A vulnerability assessment has identified a false narrative likely to be deployed against you.

**When NOT to use:**
- The claim has already spread — use `psyops_debunk_and_correction_design.md`.
- You are unsure whether to respond at all — use `psyops_rumor_response_triage.md`.
- You cannot establish that the anticipated claim is false. Then you must not prebunk it.
- The claim is about you and is partly true — that is a remediation problem; see `../organizational-red-team/psyops_narrative_vulnerability_assessment.md`.

**Audience:** Communications and policy teams, public health and election officials, educators, and trust-and-safety staff.

---

## Inputs / Context

1. **The anticipated claim or technique.** As specifically as you can state it.
2. **Your basis for anticipating it.** Prior occurrence, seasonality, an observed early signal, or a vulnerability assessment. Speculation is a weak basis and should be labeled as such.
3. **The truth status of the anticipated claim.** How you know it is false, and how confident you are. This gates the entire exercise.
4. **The audience.** Who you are protecting, what they currently believe, and how much they trust you.
5. **The channel and timing.** How you reach them before exposure, and how much time you have.
6. **Your standing.** Whether you are a credible messenger to this audience, or whether someone else should carry it.

---

## Constraints

### Must
- **Verify the anticipated claim is false** before designing anything, and state the basis and confidence. If it might be true, stop.
- Prefer **technique-level inoculation** over claim-level, and state which you are doing.
- Include all three components: **forewarning, weakened exposure, refutation** — a warning alone does not inoculate.
- Keep the weakened exposure **weak**: enough to demonstrate the move, never a fluent rendition of the persuasive content.
- Ensure the refutation is **reconstructable by the audience** without you present.
- Verify **timing precedes exposure**, and say what happens to the design if it does not.
- Assess **messenger credibility** with this audience, and consider whether a different messenger should deliver it.
- Include a **falsifiability commitment**: what you will say publicly if the anticipated claim turns out to have merit.

### Must Not
- Prebunk a claim you have not established is false, or a claim that is contested, or one that is inconvenient rather than untrue. This is the failure that turns inoculation into propaganda.
- Prebunk criticism of yourself. Inoculating an audience against your own critics is a self-serving use of the technique and is transparent to everyone outside the organization.
- Produce a compelling version of the false claim. The weakened exposure must be visibly weak; a persuasive rendition spreads on its own.
- Use inoculation to build generalized distrust of a category of source. Protecting people against a technique is legitimate; teaching them to reject an outlet or institution wholesale is not.
- Fabricate examples, statistics, or research findings about inoculation effectiveness.
- Deploy without a plan for the case where the claim never arrives — an unnecessary warning has its own credibility cost.
- Assume prebunking works on an audience that does not trust the messenger. It can entrench the opposite.

---

## Instructions

### Step 1 — Verify the claim is false, and state your confidence
Document how you know. If the answer is that it is contested, unflattering, or merely inconvenient, stop — this technique is not available for it.

### Step 2 — State your basis for anticipating it
Prior occurrence, seasonality, an early signal, or an assessment. Speculative anticipation produces warnings for claims that never come, and those cost credibility.

### Step 3 — Choose the level: technique or claim
Identify the underlying move — decontextualized statistics, fake expert credentials, emotionally selected anecdotes, manufactured urgency, false balance. Technique level is stronger and generalizes; choose it unless the claim is highly specific and non-recurring.

### Step 4 — Write the forewarning
Short, specific, non-alarming: people will encounter attempts to persuade them using a particular move, and here is what it looks like. Avoid framing that makes the audience feel warned-about rather than equipped.

### Step 5 — Build the weakened exposure
A small, obviously constructed example of the technique — ideally on a neutral or unrelated topic, which demonstrates the move without carrying the contested content at all. Keep it visibly weak.

### Step 6 — Build the reconstructable refutation
Give the audience the question that defeats the move: "what is the base rate?", "who is this expert and in what field?", "what happened before the clock started?" A question they can carry beats a fact they must recall.

### Step 7 — Check messenger and timing
Do they trust you on this? If not, identify who they do trust. Then confirm delivery precedes exposure, and state what changes if it does not.

### Step 8 — Write the falsifiability commitment and run the adversarial check
Write, in advance, what you will say publicly if the claim turns out to have merit. Then argue that this prebunk is really an attempt to protect your own position, and revise until it is not.

---

## False-Positive Prevention

1. **Prebunking a true claim.** The gravest failure. It weaponizes a protective technique against accurate information, and it is usually discovered.
2. **Prebunking legitimate criticism.** Inoculating an audience against your own critics. Transparent from outside and corrosive to trust.
3. **Weakened exposure too strong.** Producing a persuasive version of the false claim, which then circulates on its own with your branding attached.
4. **Warning without refutation.** Telling people something is coming without equipping them, which raises anxiety and provides no protection.
5. **Timing failure.** Deploying after exposure and calling it prebunking. It is debunking, and it needs the other design.
6. **Messenger mismatch.** Delivering to an audience that distrusts you, where inoculation can entrench the belief it targets.
7. **Generalized distrust.** Teaching people to reject a source category wholesale rather than to recognize a move. That is not inoculation; it is what inoculation defends against.
8. **No plan for a no-show.** Warning about a claim that never arrives, repeatedly, until the warnings themselves are discounted.

---

## Output Format

```
# Prebunk design — [anticipated claim or technique]

## Truth verification (gate)
- The anticipated claim is false because: [basis]
- Confidence: [low / moderate / high]
- **If not high, or if the claim is contested or merely inconvenient: stop. Do not prebunk.**

## Basis for anticipating it
[Prior occurrence / seasonality / observed early signal / assessment — or "speculative", labeled]

## Level
[Technique-level (preferred) or claim-level] — the underlying move: [...]

## The three components

**1. Forewarning**
"[Short, specific, non-alarming — equips rather than alarms]"

**2. Weakened exposure**
[Small, obviously constructed demonstration of the move — ideally on a neutral topic.
Deliberately weak. Not a fluent version of the false claim.]

**3. Reconstructable refutation**
The question the audience carries: "[question that defeats this move unaided]"

## Messenger
[Do they trust us on this? If not — who should carry it instead?]

## Timing
[Delivery precedes exposure: yes/no. If no — this is debunking; switch designs.]

## Falsifiability commitment
[Written in advance: what we will say publicly if the claim turns out to have merit]

## If the claim never arrives
[What we do, and the credibility cost of an unnecessary warning]

## Adversarial check
[The case that this prebunk is really protecting our position — and what was revised]
```

---

## Verification

- [ ] The anticipated claim was verified false with a stated basis and confidence, and the design stops if confidence is not high.
- [ ] The prebunk does not target criticism of the sponsoring organization.
- [ ] All three components are present: forewarning, weakened exposure, reconstructable refutation.
- [ ] The weakened exposure is visibly weak and does not constitute a persuasive version of the false claim.
- [ ] The refutation is a question or test the audience can apply without the messenger present.
- [ ] Technique-level inoculation was chosen unless a specific reason for claim-level is stated.
- [ ] Messenger credibility with this audience is assessed.
- [ ] Timing precedes exposure, or the design is switched to debunking.
- [ ] A falsifiability commitment is written in advance.
- [ ] Nothing teaches generalized distrust of a source category, and no effectiveness research was fabricated.
