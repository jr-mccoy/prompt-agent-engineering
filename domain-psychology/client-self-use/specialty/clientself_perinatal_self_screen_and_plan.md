---
title: "Perinatal Mood & Anxiety Self-Screen — With Escalation Thresholds"
category: psychology/client-self-use/specialty
description: "Help someone who is pregnant or within 12 months after birth or loss make sense of their own mood and anxiety — including an EPDS or PHQ-9/GAD-7 score from their provider, if they have one — against clear, pre-stated escalation thresholds: 911/ED now for psychosis signs or intent, 988 and a clinician today for any self-harm thought, clinician this week for high scores, next appointment for mild ones. Screens, never diagnoses, and ends with a plan and the words to say to the OB, midwife, or GP."
techniques:
  - QA-08
  - ST-04
  - QA-04
  - CM-02
  - NE-07
difficulty: advanced
tags:
  - client-self-use
  - specialty
  - perinatal
  - postpartum
  - pmad
  - self-screen
  - escalation
  - baby-blues
  - pregnancy-anxiety
  - scary-baby-thoughts
  - not-bonding
intended_use: model-testing
updated: "2026-09-24"
related_prompts:
  - domain-psychology/populations/perinatal/psychology_perinatal_mood_anxiety_screen_interpretation.md
  - domain-psychology/client-self-use/specialty/clientself_postpartum_partner_support_guide.md
  - domain-psychology/populations/perinatal/psychology_postpartum_psychosis_referral.md
---

# Perinatal Mood & Anxiety Self-Screen — With Escalation Thresholds

> **IF YOU ARE SEEING OR HEARING THINGS OTHERS DON'T, FEEL CONFUSED OR EXTREMELY SUSPICIOUS, HAVEN'T SLEPT FOR DAYS EVEN WHEN YOU COULD, OR FEEL YOU MIGHT HARM YOURSELF OR YOUR BABY: call 911 or go to the nearest emergency department (ED) now, and make sure you and your baby are not alone.** For thoughts of suicide or self-harm, call or text **988** (Suicide & Crisis Lifeline, US). For support any time: **National Maternal Mental Health Hotline 1-833-TLC-MAMA (1-833-852-6262)**; Postpartum Support International HelpLine 1-800-944-4773. Outside the US, use your local emergency number or find a local crisis line at findahelpline.com. This is a self-screen aid — it is **not** a diagnosis, and it does not replace your OB, midwife, GP, or therapist.

## Objective

Help you check in with your own mood and anxiety during pregnancy or the first year after birth (or loss), place what you're experiencing against **thresholds decided in advance** — so you don't have to judge in the moment whether it's "bad enough" — and leave with a concrete next step and the exact words to use with your care team. Perinatal mood and anxiety conditions are common and treatable; saying something is the protective move.

## When to Use

- You're pregnant or up to 12 months after birth, miscarriage, stillbirth, or adoption, and something feels off beyond tiredness.
- Your provider gave you an EPDS (or PHQ-9/GAD-7) score and you want to understand what it means for next steps.
- You're having scary intrusive thoughts, can't stop worrying, feel flat, or feel detached from the baby.

**Distinct from:**
- `populations/perinatal/psychology_perinatal_mood_anxiety_screen_interpretation.md` — the clinician-side interpretation and disposition; this is the client-held version with the same thresholds in plain language.
- `domain-parenting/caregiver-facing/ages-0-3/parenting_postpartum_parent_capacity_check.md` — capacity to parent in the postpartum year, framed around care load; this prompt covers **pregnancy through 12 months**, anchors to screen scores and escalation tiers, and hands off to the perinatal care team.
- `specialty/clientself_postpartum_partner_support_guide.md` — for the partner watching from outside.

## Inputs / Context

- Weeks pregnant or weeks/months since birth or loss.
- What you've noticed over the past two weeks: mood, interest, anxiety, sleep (when the baby lets you), appetite, irritability, intrusive thoughts, bonding.
- An EPDS, PHQ-9, or GAD-7 score from your provider, if you have one (don't reproduce the questionnaire here — just the score and whether the self-harm item was positive).
- Any thoughts of self-harm or suicide; any unusual experiences (hearing/seeing things, beliefs others find strange, not needing sleep).
- History: prior depression, anxiety, bipolar disorder, or postpartum episodes.
- Who is on your care team and when you next see them.

## Constraints

### Must

- **Gate 1 — emergency (QA-08):** psychosis signs, intent to harm self or baby, or several nights without sleep despite opportunity → 911/ED now; not left alone with the baby; stop.
- **Gate 2 — same day:** any thought of self-harm or suicide, or a positive self-harm item (EPDS item 10 or PHQ-9 item 9) regardless of total → 988 and a clinician **today**.
- **Tier 3 — this week:** EPDS 13 or more, PHQ-9 10 or more, GAD-7 10 or more, or symptoms most days for 2+ weeks affecting functioning → contact OB/midwife/GP/therapist within the week.
- **Tier 4 — next appointment:** EPDS 10–12, PHQ-9 or GAD-7 in the mild range (5–9), or symptoms that come and go → raise it at the next scheduled visit and re-check in two weeks.
- State that cut-offs vary by guideline and population (QA-04) and that the score starts the conversation; the clinician decides.
- Flag **bipolar history** as higher risk postpartum → tell the care team now even if mood seems fine.
- Distinguish in plain language: unwanted, horrifying intrusive thoughts about harm to the baby (common, often perinatal OCD, still worth telling a clinician) vs. thoughts that feel right or true, or intent (Gate 1).
- Validate (NE-07) without minimising; close with the words to say to the provider.

### Must Not

- Do not diagnose PPD, PPA, perinatal OCD, bipolar disorder, or psychosis.
- Do not reproduce EPDS, PHQ-9, or GAD-7 items or score them from free text.
- Do not reassure away intrusive thoughts or advise keeping them secret for fear of child removal; say clinicians hear these often and treat them.
- Do not advise on starting, stopping, or changing medication in pregnancy or breastfeeding — that's a prescriber conversation.
- Do not attribute everything to sleep deprivation.

## Instructions

1. Run Gate 1, then Gate 2; stop and route if either is met.
2. Validate what the person is carrying.
3. Place symptoms and any score against Tier 3 and Tier 4.
4. Flag bipolar/prior-episode history.
5. Write the next step, re-check date, and the words to use.
6. List support lines and one practical ask.

## Output Format

```
=== PERINATAL SELF-SCREEN & PLAN ===

>>> EMERGENCY CHECK <<<
Hearing/seeing things, confused, very suspicious, no sleep for days despite chances, or might harm myself/baby?
  → 911 or ED NOW. Don't stay alone with the baby.
Any thought of self-harm or suicide (or a positive self-harm item on my screen)?
  → 988 (call/text) AND my clinician TODAY.

Where I am: [weeks pregnant / weeks postpartum]
What I've noticed (2 weeks): [...]
Screen score (if I have one): [EPDS __ / PHQ-9 __ / GAD-7 __]; self-harm item: [yes/no]

My tier: [This week / Next appointment]   (cut-offs vary — my clinician decides)
History flag: [bipolar / prior postpartum episode → tell care team now]

Next step: contact [OB / midwife / GP / therapist] by [date].
Words to use: "I'm [N] weeks [pregnant/postpartum]. For two weeks I've felt [...]. My EPDS was [__]. I'd like to talk about treatment options."

Re-check: [date, two weeks out]
Support lines: 1-833-TLC-MAMA · PSI 1-800-944-4773 · 988
One practical ask: [person] → [protected sleep block / feed / meal]
```

## Verification

- [ ] Emergency and same-day gates run first, with 911/ED, 988, and not-alone-with-baby.
- [ ] Positive self-harm item routes same day regardless of total score.
- [ ] Tier thresholds stated, with the "cut-offs vary" caveat.
- [ ] Bipolar/prior-episode flag present.
- [ ] Intrusive-thought vs intent distinction made without reassurance or secrecy.
- [ ] No diagnosis, no questionnaire items reproduced, no medication advice.
- [ ] Next step, words to use, re-check date, and support lines present.

## False-Positive Prevention

- Baby blues (tearfulness and mood swings in the first ~2 weeks that ease on their own) are common and not a disorder — but anything lasting past two weeks, or any Gate 1/2 sign at any time, is not "just blues." Do not use the blues label to delay escalation.
- Horrifying intrusive thoughts of harm the person does not want are not, on their own, a psychosis or intent signal; route them to a clinician (Tier 3), not to 911 — unless the person describes wanting to act or believing the thought is right.
- A low EPDS total does not clear a positive self-harm item; the item routes on its own.

## Example

**Input:** "I'm 7 weeks postpartum. My EPDS at the pediatrician was 14, self-harm question was 'never.' I keep picturing dropping the baby down the stairs and it horrifies me, so I avoid carrying her on the stairs. No history."

**Output (abbreviated):** Gates clear (no psychosis signs, no self-harm thoughts, no intent — the images are unwanted and horrifying). Validation. Tier: this week (EPDS 14). Note that unwanted intrusive images plus avoidance are common postpartum and very treatable — worth telling a clinician, not a sign of danger. Next step: call OB by Friday. Script included. Re-check in two weeks. Support lines listed. Practical ask: partner covers the 2 a.m. feed.
