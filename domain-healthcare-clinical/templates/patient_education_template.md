---
title: "Patient Education Material Template"
category: healthcare-clinical/templates
description: "Fill-in template for creating patient education content matched to the patient's health literacy, with prioritized key messages, concrete action steps, warning signs, and teach-back questions."
techniques:
  - ST-01
  - RP-02
  - CM-02
  - ST-03
  - QA-01
difficulty: intermediate
tags:
  - patient-education
  - health-literacy
  - patient-communication
  - teaching
updated: "2026-10-06"
---

# Patient Education Material Template

> **Medical disclaimer — read before use.** This prompt is a decision-support and
> teaching aid for **licensed clinicians**. It is **not medical advice** and is not for
> patients to diagnose or treat themselves. Drug doses, thresholds and guideline
> references in it and in its worked example may be incomplete, outdated or wrong:
> verify each one against the current guideline, the product label and your local
> formulary, and follow your institution's protocols. It does not replace examination
> or clinical judgment. **Medical emergency: call your local emergency number (911 in
> the US).**
>
> **Review status:** AI-assisted content, reviewed by AI only (2026-10-06);
> **not yet reviewed by a licensed clinician.**

> Copy this template when creating patient education content.
> Customize placeholders marked with [BRACKETS].

---

```markdown
# Patient Education: [Topic]

**Objective:** Create patient-friendly education materials about [condition/treatment/procedure]

## Target Audience

**Patient Profile:**
- Age range: [e.g., adults 40-70, pediatric parents, elderly]
- Health literacy: [Limited / Adequate / Proficient] (health literacy is the ability to find, understand and use health information — not the same as reading grade; set the writing target separately below)
  - Limited = write at a 6th-grade reading level target, avoid medical jargon
  - Adequate = write at an 8th-9th grade target, can understand with explanation
  - Proficient = Can handle standard medical information

**Language Considerations:**
- Primary language: [English/Spanish/Other]
- Reading level target: [Flesch-Kincaid grade level]
- Cultural considerations: [If relevant]

**Learning Context:**
- Timing: [New diagnosis / Pre-procedure / Discharge / Ongoing management]
- Prior knowledge: [What they already know]
- Emotional state: [Anxious / Overwhelmed / Receptive / In denial]

## Clinical Topic

**Condition/Treatment:** [Specific medical topic]

**Clinical Accuracy Source:** [Ensure medically accurate base information]

## Key Messages (Maximum 3-5)

Priority order - most critical first:
1. [MOST IMPORTANT - if they remember nothing else, this]
2. [Second priority]
3. [Third priority]
4. [Optional fourth]
5. [Optional fifth]

## Content Requirements

**Must Include:**
- What [condition/treatment] IS in simple terms
- What the patient SHOULD DO (concrete actions)
- When to SEEK HELP (specific warning signs)
- How to GET ANSWERS (who to call, when)

**Must Avoid:**
- Medical jargon without explanation
- Information overload (>5 key points)
- Scary statistics without context
- Assumptions about prior knowledge
- Condescending tone
- Long paragraphs (use bullets and short sentences)

## Output Structure

Generate patient education material with this structure:

### 1. Opening Hook (1-2 sentences)
- Why this matters to THEM
- Connect to their daily life

### 2. Simple Explanation
- Use an analogy from everyday life
- Example: "Think of your heart like a pump..." or "It's similar to when your car..."
- Avoid "simple" becoming "inaccurate"

### 3. What You Should Do (Numbered Steps)
- Specific, actionable items
- One action per step
- Include frequency and timing
- Make it easy to remember

### 4. Warning Signs - When to Get Help
- Specific symptoms to watch for
- "Call your doctor if..."
- "Go to the ER immediately if..."
- Include phone numbers to call

### 5. Common Questions
- Questions patients frequently ask
- Brief, clear answers
- "It's normal to wonder about..."

### 6. Summary (2-3 sentences)
- Repeat the most important message
- Encouraging, empowering tone
- Next step

## Verification Elements

**Teach-Back Questions:**
Include questions to verify understanding:
- "In your own words, what is the main thing you need to do?"
- "How will you know if you need to call the doctor?"
- "What is the most important thing to remember?"

**Comprehension Check:**
- Is every medical term explained?
- Are sentences under 15 words on average?
- Can a 6th grader understand this? (for limited literacy)
- Are action steps numbered and specific?
```

---

## Example Application

**Scenario:** Discharge instructions for new diabetes diagnosis

```markdown
# Patient Education: Your New Diabetes Diagnosis

**Patient Profile:**
- Age: Adults 45-65
- Health literacy: Limited (writing target: 6th-grade reading level)
- Timing: New diagnosis, overwhelmed
- Language: English

**Key Messages:**
1. Diabetes can be managed - you can live a full life
2. Check your blood sugar as directed
3. Take your medication every day
4. Know when to call for help

---

## Expected Output:

### Why This Matters to You
You just learned you have diabetes. This might feel scary, but here's the good news: diabetes can be managed. Many people with diabetes live long, healthy lives. This guide will help you get started.

### What Is Diabetes? (The Simple Version)
Think of sugar like fuel for your body. Normally, your body moves sugar from your blood into your cells where it's used for energy. With diabetes, this process doesn't work as well, so sugar builds up in your blood.

Your medicine helps your body use sugar better.

### What You Should Do Every Day

1. **Take your medicine** at the same time each day
2. **Check your blood sugar** when your doctor tells you to
3. **Eat regular meals** - don't skip meals
4. **Move your body** - even a 10-minute walk helps

### Warning Signs - When to Call

**Call your doctor if:**
- Blood sugar over [number] or under [number]
- You have signs of low blood sugar - shaky, sweaty, fast heartbeat, very hungry, or confused [VERIFY: low-blood-sugar steps from this patient's care plan - depends on their medicine]
- You feel sick for more than 2 days
- You have questions about your medicine

**Go to the ER if:**
- You can't keep food or water down
- Blood sugar won't come down
- You feel confused or very sleepy

**Your doctor's number:** _______________

### Questions You Might Have

**"Can I still eat things I enjoy?"**
Yes! You don't have to give up all your favorite foods. You'll learn to eat smaller portions and balance your meals.

**"Is this my fault?"**
No. Many things cause diabetes - family history, age, and other factors you can't control.

### Remember
Diabetes can be managed. Take your medicine, check your blood sugar, and call your doctor if you have questions. You've got this.

---

**Teach-back:** "Before you go home, can you tell me: What will you do if your blood sugar is too high?"
```

---

## False-Positive Prevention

When filling this template:

❌ **DON'T:**
- Replace a warning-sign placeholder such as "Blood sugar over [number] or under [number]" with typical values; call-back thresholds are this patient's prescriber targets and come from the order or care plan.
- Put a guideline name you have not opened into "Clinical Accuracy Source", or leave that slot as placeholder text and still tick "Medically accurate (verified by source)".
- Write timed action steps (dose times, glucose-check schedule, dressing-change frequency) that are not on the patient's actual discharge orders or medication list.
- Tick "Reading level appropriate" by impression; one undefined word such as "hyperglycemia" or "titrate" breaks a 6th-grade target even when sentences are short.
- Simplify the everyday analogy until it says something false about how the condition or medicine works.

✅ **DO:**
- Run a readability score (Flesch-Kincaid or equivalent) on the finished text and record the grade beside "Reading level target"; count the key messages (5 or fewer) and confirm each numbered step holds one action.
- Trace every medication name, dose, frequency and phone number in the handout to the discharge medication list or the clinic's own contact sheet; leave a `[VERIFY: ...]` blank rather than inventing one.
- Check the "Call your doctor" and "Go to the ER" lists against the named source for this condition, covering both directions where the condition has them (for diabetes, low as well as high blood sugar).
- Make sure the teach-back questions test key message #1 and the warning signs, not a minor point.

---

## Quality Checklist

- [ ] Reading level appropriate for audience
- [ ] Medical terms explained in plain language
- [ ] Maximum 5 key messages
- [ ] Specific action steps (not vague advice)
- [ ] Clear warning signs with specific actions
- [ ] Phone numbers/contacts included
- [ ] Teach-back questions included
- [ ] Encouraging, non-judgmental tone
- [ ] Culturally appropriate
- [ ] Medically accurate (verified by source)
