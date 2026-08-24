---
title: PACU Local Anesthetic Systemic Toxicity (LAST) — Recognition & Response
category: pacu/complications
task_type: LEARN
audience: PACU orientee (mid/late) or preceptor for huddle; any unit recovering regional/neuraxial patients
updated: "2026-07-06"
tags:
  - pacu
  - LAST
  - local-anesthetic-toxicity
  - regional-anesthesia
  - emergency
techniques:
  - ST-01
  - ST-02
  - RT-02
  - QA-02
  - ED-02
  - DS-06
difficulty: advanced
related_prompts:
  - pacu_complication_deep_dive.md
  - pacu_dysrhythmia_recognition.md
  - pacu_emergency_drill_designer.md
  - pacu_red_flag_card.md
references:
  - Drain's PeriAnesthesia Nursing Practice (7th ed.) — regional anesthesia chapters
  - ASPAN Standards of Perianesthesia Nursing Practice
  - ASRA (American Society of Regional Anesthesia) — Checklist for Treatment of LAST
  - ASPAN Core Curriculum for PeriAnesthesia Nursing Practice
---

# Local Anesthetic Systemic Toxicity (LAST) — PACU Deep Dive

> Safety reminder: LAST is a rare, time-critical emergency. The nurse's job is early recognition, calling for help, and retrieving the lipid-rescue resources — **not** independent drug administration. Lipid emulsion dose and all pharmacology are per the ASRA checklist and provider order. This prompt states no doses. See `../SAFETY_PREAMBLE.md`.

## Objective

Produce a structured deep dive on LAST for any orientee whose unit recovers patients with a regional block, neuraxial catheter, wound-infiltration catheter, or recent large-volume local infiltration. Covers why it matters → mechanism → early prodrome → progression → differential → immediate response (ASRA-aligned) → escalation → after-event.

## Inputs

- **Regional context in your unit:** {{single-shot blocks | continuous peripheral catheters | neuraxial | wound-infiltration catheters | liposomal bupivacaine}}
- **Where the lipid-rescue kit lives on your unit:** {{per facility — the orientee should be able to state this}}
- **Source chapters:** {{Drain's regional chapters, ASRA LAST checklist}}

## Audience

- Orientee in weeks 4–10 who recovers regional/neuraxial patients.
- Preceptor preparing a high-consequence, low-frequency huddle.

## Output requirements

```markdown
# Local Anesthetic Systemic Toxicity (LAST) — PACU Deep Dive

> Safety reminder: Time-critical. Recognize, call for help, retrieve lipid-rescue kit, assist provider. All pharmacology per ASRA checklist / provider order.

## Why it matters
[One paragraph — rare but potentially fatal; can present late (delayed absorption, catheter dosing); the PACU nurse is often the first to see the prodrome.]

## Pathophysiology
[2–4 sentences: systemic local-anesthetic levels block cardiac and CNS sodium channels; CNS excitation then depression; cardiac conduction and contractility impairment. Higher risk with bupivacaine.]

## Risk / setup (who and when)
- Recent block, catheter bolus/infusion, large-volume infiltration, inadvertent intravascular uptake.
- Delayed onset possible — LAST is not only an "at-injection" event; catheter patients can present in PACU.

## Early cues (prodrome — before collapse)
- Perioral numbness or tingling.
- Tinnitus, metallic taste.
- Lightheadedness, visual disturbance.
- New agitation, confusion, "sense of doom," dysarthria, muscle twitching.
- **A patient reporting these after a block is a red flag until proven otherwise.**

## Progression (if unrecognized)
- CNS excitation → seizures.
- CNS depression → decreased consciousness, respiratory depression.
- Cardiac → bradycardia, conduction block, ventricular dysrhythmia, hypotension, arrest.

## Differential — what else looks like this?
| Mimic | How to tell them apart |
|---|---|
| Emergence agitation | No perioral numbness/tinnitus/metallic taste; not temporally linked to local dosing |
| Vasovagal / hypotension | Prodrome differs; LAST has neuro-sensory prodrome + progression |
| Primary seizure disorder | History; LAST seizure follows local-anesthetic exposure |
| High/total spinal | Ascending motor/sensory block + hypotension/bradypnea pattern |

## Immediate response (ASRA-aligned — recognize & assist)
1. Stop any local-anesthetic injection/infusion (pause catheter) → notify provider immediately.
2. Call for help; get the code cart AND the lipid-rescue kit to the bedside → reassess continuously.
3. Airway/oxygenation: 100% O₂ per order, support ventilation → reassess in 1 min.
4. Seizure management, lipid emulsion, and all drugs are **per ASRA checklist / provider order** — retrieve, prepare, and assist; do not self-initiate.
5. Anticipate prolonged resuscitation; LAST arrest can require extended effort.

## Escalation
- Call {anesthesia provider by role} immediately at the prodrome — do not wait for seizure.
- Activate rapid response / code per facility for seizure, arrhythmia, or arrest.
- Ensure the ASRA LAST checklist is physically at the bedside for the team.

## Pharm / equipment likely used
- Lipid emulsion (per ASRA checklist / order — no dose stated here).
- Airway/resuscitation equipment; code cart.
- Note: some standard resuscitation drugs are modified in LAST arrest — team follows the ASRA checklist.

## After it resolves
- Extended monitoring (recurrence possible as tissue redistributes) → interval per facility/provider.
- Charting: prodrome, timeline, local-anesthetic source, interventions, response, escalation.
- Handoff: flag LAST event + monitoring window for receiving unit.

## Teaching pearls
- The prodrome is sensory and subtle — perioral numbness/tinnitus/metallic taste after a block is LAST until proven otherwise.
- Know where the lipid-rescue kit and the ASRA checklist live *before* you need them.

## Common orientee mistakes
- Attributing prodrome to "anxiety" and waiting.
- Not knowing the location of the lipid-rescue kit.

## Sources
- ...
```

## Must / Must not

**Must:**
- Early sensory prodrome section **before** seizure/collapse.
- Frame response as ASRA-checklist-driven; nurse recognizes, retrieves kit, assists.
- Differentiate from emergence agitation, vasovagal, high/total spinal.
- Emphasize the orientee knowing the lipid-kit and checklist location in advance.

**Must not:**
- No lipid-emulsion dose or any specific drug dose — "per ASRA checklist / order."
- No invented incidence statistics.
- No scope creep — no nurse-initiated lipid or resuscitation drug decisions.
- No facility-specific kit contents/pager paths invented.

## Quality signals

- Orientee names 3 prodrome cues they'd have dismissed before.
- Orientee can say where the lipid-rescue kit and ASRA checklist are.
- Response is recognize-call-retrieve-assist, not self-treat.

## Verification

- [ ] Sensory prodrome precedes seizure/collapse.
- [ ] Response is ASRA-aligned; nurse role is recognize/retrieve/assist.
- [ ] Differential has ≥ 2 mimics with distinguishing features.
- [ ] Every response step names a reassess interval or "continuously."
- [ ] Escalation names a role and says "at prodrome, don't wait."
- [ ] Lipid emulsion and drugs are "per checklist/order" — no dose.

## False-Positive Prevention

Do **not** fabricate or invent:

- **No lipid-emulsion or drug doses / rates / concentrations.** Per ASRA checklist / provider order only.
- **No invented incidence or mortality statistics.** Describe qualitatively ("rare but potentially fatal").
- **No invented facility kit contents, locations, or pager paths** — the location is `{{per facility}}` for the orientee to fill.
- **No fabricated ASRA checklist steps** — reference the checklist; do not paraphrase specific numeric parameters from memory.
- **No fabricated chapter citations.** Mark `{{confirm}}` when unknown.
- **No scope creep** — provider-scope resuscitation/pharmacology stays with the provider/team.

## Worked Example

<details>
<summary>Example: "Early cues (prodrome)" for a continuous-catheter patient (click to expand)</summary>

```markdown
## Early cues (prodrome — before collapse)

A patient with a continuous interscalene catheter running in PACU calls you over: "My lips feel numb and my ears are ringing." She seems more anxious than 10 minutes ago and her speech is slightly slurred.

- Perioral numbness + tinnitus + new agitation after ongoing local-anesthetic delivery = treat as LAST prodrome.
- Pause the catheter infusion, call the anesthesia provider by role immediately, bring the code cart and lipid-rescue kit to the bedside, apply O₂ per order, and stay with the patient reassessing continuously.
- Do not wait to see if it "settles" — the next step in unrecognized LAST is a seizure.
```

Notes: prodrome recognized and acted on before collapse; infusion paused; kit retrieved; escalation at prodrome; no doses invented; nurse role is recognize/retrieve/assist.
</details>

## Self-check

- [ ] Prodrome before collapse.
- [ ] ASRA-aligned recognize/retrieve/assist framing.
- [ ] Differential ≥ 2 mimics.
- [ ] Reassess intervals present.
- [ ] Escalation at prodrome, by role.
- [ ] No lipid/drug doses invented; kit location is a facility placeholder.
- [ ] Safety reminder at top.
- [ ] Verification + False-Positive Prevention passed.
