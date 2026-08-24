---
title: "Developmental Expectations Index (Router Across Age Bands)"
category: parenting/cross-age
description: "Router prompt that links to all four age-band developmental-expectations prompts (0-3, 4-8, 9-12, 13-18), identifies which is needed for a given concern, and provides cross-cutting context for when a behavior is 'off-tier' or when looking across age bands is necessary."
techniques:
  - DS-01
  - ST-02
  - CM-01
  - QA-02
difficulty: beginner
intended_use: model-testing
tags:
  - parenting
  - cross-age
  - developmental-expectations
  - router
  - milestones
updated: "2026-05-11"
related_prompts:
  - domain-parenting/caregiver-facing/ages-0-3/parenting_developmental_red_flags_0_3.md
  - domain-parenting/caregiver-facing/ages-4-8/parenting_developmental_expectations_4_to_8.md
  - domain-parenting/caregiver-facing/ages-9-12/parenting_developmental_expectations_9_12.md
  - domain-parenting/caregiver-facing/ages-13-18/parenting_developmental_expectations_13_18.md
  - domain-parenting/caregiver-facing/cross-age/parenting_when_to_seek_professional_help_all_ages.md
---

**Purpose:** Help a caregiver pick the right developmental-expectations prompt for a given question, identify when a behavior is "off-tier" (more typical of an earlier or later age band), and surface cross-cutting context when a single age-band view isn't sufficient.

**When to use:** Caregiver isn't sure which age-band prompt fits; behavior seems off-age (regression, advanced beyond age, mismatch); cross-sibling comparison; transitional age (3, 8, 12, 18); ND profile that complicates age-banding; reviewing a child's developmental profile broadly.

**When NOT to use:** Acute concern with clear signal in a specific age band → go directly to that age band's prompt. Specific clinical concern → use the dedicated symptom prompt.

---

## Core Principles

1. **Age-band prompts are organized by typical chronological developmental window.** They cover cognitive, emotional, social, physical, identity, and family domains within that window.
2. **Many kids are off-tier in some domains.** A 6-year-old may be at 4-year-old level emotionally and 10-year-old level cognitively. ND, trauma, and individual variation drive this.
3. **Looking across age bands is sometimes necessary.** Especially for ND kids, regression, gifted kids, or kids whose development is asynchronous.
4. **Developmental milestones are statistical.** Most kids cross most milestones in roughly the typical window. Variation within is normal; variation outside the window may warrant evaluation.
5. **The router doesn't replace the age-band prompts.** It points to them.

---

## Your Input

- **Kid age:**
- **Specific question or concern:**
- **Domain(s) of concern:** [Cognitive / language / motor / emotional / social / physical / identity / family]
- **Apparent developmental level (your sense):** [On-age / younger / older / mixed / regressing]
- **ND profile:**
- **Why you're asking now:**

---

## Constraints

**Must:**
- Identify the primary age-band prompt to use.
- Identify secondary prompts to consult if relevant.
- Address off-tier patterns explicitly.
- Address regression as distinct.
- Be brief — this is a router, not a full-content prompt.

**Must Not:**
- Substitute for the age-band prompts.
- Diagnose.
- Make caregivers feel that asynchronous development is wrong.

---

## Instructions

### Stage 1 — Age-Band Quick Map

**Ages 0–3 (Infant + Toddler):**
- Primary prompt: `parenting_developmental_red_flags_0_3.md` (domain-by-domain audit + routing).
- Covers: motor, language, social, cognitive, emotional, sensory, attachment.
- Key transitions: rolling, sitting, crawling, walking; first words, two-word phrases; pointing; pretend play; toilet readiness.
- Many milestones missed by 0–3 warrant Early Intervention referral.

**Ages 4–8 (Early Childhood / Early Elementary):**
- Primary prompt: `parenting_developmental_expectations_4_to_8.md`.
- Covers: cognitive, emotional, social, physical, family relationship.
- Key transitions: kindergarten readiness, reading emergence, friendship formation, internal moral framework, first regulated emotional repertoire.
- This window is where many ND profiles become visible.

**Ages 9–12 (Tween):**
- Primary prompt: `parenting_developmental_expectations_9_12.md`.
- Covers: cognitive, emotional, social, physical / pubertal, identity, family.
- Key transitions: puberty onset (variable timing), peer-primacy intensifying, abstract reasoning emerging, identity formation starting.

**Ages 13–18 (Adolescence):**
- Primary prompt: `parenting_developmental_expectations_13_18.md`.
- Covers: cognitive, emotional, social, physical, identity, family relationship + manager-to-consultant shift.
- Key transitions: identity formation as central task, autonomy renegotiation, sleep-phase delay, peer-primacy peaks then integrates.

### Stage 2 — Routing Logic

**If kid age is within a band and concern is on-age:** use that band's prompt.

**If kid is at a transition age (3, 8, 12, 18):** use both adjacent-band prompts; the developmental work overlaps.

**If kid is off-tier (younger or older than chronological age in the concern domain):**
- Read the age-band that matches the developmental level.
- Read the chronological-age band for the family/social context.
- Hold both in mind.

**If kid has regressed:**
- Note when the regression started.
- Loss of previously consolidated skills is a signal — consult `parenting_when_to_seek_professional_help_all_ages.md` and the appropriate age-band prompt.
- Common regression triggers: illness, family stress (move, divorce, new sibling, loss), trauma, sensory or environmental change. Some regression resolves in days to weeks.
- Sustained regression (>4 weeks) warrants evaluation.

**If kid is asynchronous (advanced in some domains, behind in others):**
- 2e (gifted + ND) is a common pattern.
- Read the age band that matches each domain.
- Specialist evaluation if pattern is consistent — neuropsych, developmental-behavioral pediatrician.

**If kid has known ND profile:**
- ND-affirming framing across bands.
- Some milestones don't apply; some apply differently.
- Specialist resources matter more than age-typical resources.

### Stage 3 — Cross-Cutting Context

Some questions require looking across bands:

**Sleep:**
- Newborn → toddler → preschool → school-age → tween → adolescent.
- Each stage has distinct sleep biology.
- A "sleep problem" at one age may be normal at the next.

**Aggression:**
- Toddler biting → 4–8 hitting → 9–12 verbal aggression → teen aggression.
- Same word, different developmental drivers.

**Anxiety:**
- Stranger and separation anxiety in infants → school refusal in 4–12 → social anxiety in tweens-and-teens → generalized in adolescence.

**Social difficulty:**
- Parallel play in toddlers → friendship formation in 4–8 → peer-primacy in 9–18.
- Difficulty at one stage doesn't predict the next.

**Identity:**
- Concrete identity in 4–8 → group identity in 9–12 → values identity in 13–18.

**Body / puberty:**
- Pre-pubertal in 4–8 → early puberty often in 9–12 → mid-late puberty in 13–18.

When a concern crosses these arcs (e.g., a 13-year-old with social difficulties since toddlerhood), look at multiple bands.

### Stage 4 — When Behavior Is "Off-Tier"

**Younger-than-tier:**
- Regression after stress (often resolves).
- Skill not yet consolidated (ordinary variance).
- Developmental delay.
- Trauma response.
- ND profile (autistic emotional age vs. cognitive age, e.g.).

**Older-than-tier:**
- Gifted (cognitive ahead).
- Parentification (responsibility ahead).
- Trauma exposure ahead of developmental capacity to process.
- Older sibling exposure.
- ND profile (autistic kids sometimes show adult-like preferences in narrow domains).

In both cases: don't force chronological-age expectations on developmental level.

### Stage 5 — Cross-Sibling Comparison

When comparing siblings:

- Same age can land differently for different kids.
- Birth order matters (older kids often more responsible-presenting; younger kids often more flexible-presenting).
- Caregiver capacity at each kid's stage may have differed.
- Comparison is informative but not predictive.
- Each sibling has their own arc.

### Stage 6 — When the Age-Band Prompt Isn't Enough

The age-band prompts are oriented to typical development. They flag concerns and route, but don't substitute for:

- Specific symptom prompts (anxiety, depression, eating disorder, substance, etc.).
- Clinical evaluation.
- Specialist guidance.

If the concern is: typical development → age-band prompt is the answer.
If the concern is: diagnosis or treatment → age-band prompt is one piece; specific symptom and evaluation prompts are needed.

### Stage 7 — Adaptations Across Profiles

- **Autistic kids:** developmental milestones often show different trajectories; ND-affirming developmental framing.
- **ADHD:** executive function lag is the throughline; varies in visibility by age.
- **Anxious kids:** anxiety presents differently at each age; cross-band view helpful.
- **2e / gifted:** asynchronous development; multiple age bands relevant.
- **Trauma history:** developmental tasks may be delayed; therapeutic anchoring of developmental expectations.
- **Chronic illness / disability:** developmental-pediatrics specialist; expectations adjusted.
- **Foster / kinship / adopted:** developmental impact of early experience; trauma-informed framing.
- **Multilingual / multicultural:** language development on different timeline.
- **Twin / multiple:** developmental comparison can mislead; each kid has own arc.

---

## Output Format

```markdown
## Developmental Expectations Routing — [Kid, concern]

### Primary Age-Band Prompt to Use
- [File path + reason]

### Secondary Prompt(s) to Consult
- [File path + reason]

### Off-Tier Read (if applicable)
- Apparent developmental level vs. chronological:
- Specific domain pattern:
- Adjacent-band prompt to also read:

### Regression Read (if applicable)
- Onset:
- Recent triggers:
- Severity / duration:
- Routing:

### Cross-Cutting Themes (if relevant to concern)
- [Specific arc across ages]

### Adaptation for [profile]
- [Specific framing]

### Beyond Developmental Expectations
- If concern is not just developmental: [specific other prompts to consult]
```

---

## Verification

- [ ] Primary age-band identified?
- [ ] Off-tier addressed if relevant?
- [ ] Regression addressed if relevant?
- [ ] Cross-cutting context surfaced if relevant?
- [ ] Adaptation for stated profile?
- [ ] Pointed to specific prompts (not generic advice)?

---

## False-Positive Prevention

| ❌ Don't | ✅ Do |
|---|---|
| Substitute this for the age-band prompt | Router only; full content lives in the age-band file |
| Diagnose | Pattern-orient; route |
| Force chronological-age expectations on off-tier kid | Match developmental level too |
| Treat asynchronous development as wrong | Common pattern, especially in 2e / ND |
| Skip the regression check | Loss of skills is a signal |
| Ignore ND-affirming framing | Standard milestones may not apply |
| Treat sibling comparison as predictive | Each kid has own arc |
| Use age-band prompt instead of symptom prompt for clinical concern | Different prompts |
| Skip transitional-age dual reading | At 3 / 8 / 12 / 18, both sides matter |
| Promise that off-tier resolves on its own | Sometimes; sometimes specialist evaluation needed |
| Treat cultural / multilingual variation as delay | Different trajectory |
| Conflate gifted with on-track | 2e specifically often missed |
