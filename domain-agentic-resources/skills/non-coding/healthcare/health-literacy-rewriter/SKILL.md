---
name: health-literacy-rewriter
description: Rewrite complex health content into plain-language, health-literate versions for broad audiences.
tags:
  - healthcare
  - health-literacy
  - plain-language
  - patient-education
  - readability
updated: "2026-04-11"
---

# Health Literacy Rewriter

Rewrite complex health and medical content into plain-language versions that are accessible, accurate, and actionable for diverse audiences.

## When to Use This Skill

- Translating clinical documentation into patient-facing materials
- Simplifying medication instructions, discharge summaries, or consent forms
- Creating health education content for low-literacy populations
- Adapting public health communications for diverse audiences
- Reviewing existing patient materials for readability and clarity

## Core Concepts

### Health Literacy Levels

Over 36% of US adults have basic or below-basic health literacy (NAAL). Materials should target a **5th-8th grade reading level** for general public use.

| Level | Reading Grade | Characteristics |
|-------|-------------|-----------------|
| Proficient | 12+ | Can interpret complex health info, compare plans |
| Intermediate | 9-11 | Can follow moderately complex instructions |
| Basic | 5-8 | Can follow simple instructions with familiar terms |
| Below Basic | <5 | Can identify basic health info on simple forms |

### Plain Language Principles

1. **Use common words**: "high blood pressure" not "hypertension"
2. **Short sentences**: Average 15 words or fewer per sentence
3. **Active voice**: "Take the medicine" not "The medicine should be taken"
4. **One idea per sentence**: Don't stack multiple instructions
5. **Define necessary medical terms**: If a term must be used, define it immediately
6. **Use "you" and "your"**: Direct address increases engagement

### Readability Scoring

| Metric | Target | What It Measures |
|--------|--------|-----------------|
| Flesch-Kincaid Grade | 5-8 | Sentence length + syllable count → grade level |
| Flesch Reading Ease | 60-70+ | Higher = easier (100 = very easy) |
| SMOG Index | 5-8 | Polysyllabic word density → grade level |
| Gunning Fog | 5-8 | Sentence length + complex words → grade level |

## Workflow

### Phase 1: Analyze Source Material

1. Identify the source document type (clinical, regulatory, educational)
2. Run readability score on the original (Flesch-Kincaid, SMOG)
3. Highlight medical jargon, acronyms, and complex sentences
4. Identify the core message: What does the reader NEED to do?
5. Note any legally required language that cannot be simplified

### Phase 2: Simplify Structure

1. Lead with the most important information (inverted pyramid)
2. Use headings as questions the reader would ask: "What should I do?" not "Treatment Protocol"
3. Break long sections into bulleted lists
4. Use numbered steps for sequential instructions
5. Limit paragraphs to 3-4 sentences maximum

### Phase 3: Rewrite for Plain Language

Apply these substitution patterns:

| Medical/Complex | Plain Language |
|----------------|---------------|
| Hypertension | High blood pressure |
| Administer | Give |
| Contraindicated | Should not be used |
| Asymptomatic | No symptoms |
| Etiology | Cause |
| Prognosis | What to expect |
| Benign | Not cancer / not harmful |
| Chronic | Long-lasting |
| Acute | Sudden / short-term |
| Bilateral | On both sides |
| NPO | Do not eat or drink |
| PRN | As needed |
| Subcutaneous | Under the skin |
| Oral administration | By mouth |
| Discontinue | Stop |

### Phase 4: Add Actionability

For every piece of information, answer: **"What should the reader DO with this?"**

Transform passive information into action steps:
- Before: "Elevated blood glucose levels may indicate the need for dietary modification."
- After: "If your blood sugar is high, you may need to change what you eat. Talk to your doctor about a meal plan."

### Phase 5: Cultural Sensitivity Review

1. Avoid idioms and culturally specific references
2. Use inclusive imagery and examples
3. Consider health beliefs of target population
4. Check for assumptions about family structure, diet, or daily routine
5. Ensure translated materials are culturally adapted, not just linguistically translated

### Phase 6: Validate and Test

1. Run readability scores on rewritten version (target: grade 5-8)
2. Apply the **Teach-Back Method**: Ask a non-expert to read it and explain it back
3. Check with clinical reviewer for medical accuracy
4. Verify no critical safety information was lost in simplification
5. Test with representative users from the target audience

## Templates

### Patient Instruction Rewrite Template

```markdown
## [What This Is About — as a question]

### What You Need to Know
[1-2 sentences: the most important fact]

### What to Do
1. [Step 1 — one action per step]
2. [Step 2]
3. [Step 3]

### When to Call Your Doctor
Call your doctor if:
- [Warning sign 1]
- [Warning sign 2]
- [Warning sign 3]

**If you have [emergency symptom], call 911 right away.**

### Words to Know
- **[Medical term]**: [Plain definition]
```

## Best Practices

- **Lead with action**: Put what the reader should DO first, background information second.
- **Use the "So what?" test**: For every sentence, ask if the reader needs this to take action.
- **Chunk information**: Group related items under clear headings. No wall-of-text.
- **Include safety netting**: Always tell patients when to seek help and what warning signs to watch for.
- **Verify medical accuracy after simplifying**: Simplification must never distort clinical meaning.
- **Use visuals**: Icons, diagrams, and labeled images improve comprehension for low-literacy readers.
- **Test with real users**: Readability scores are a proxy; the real test is human comprehension.

## Common Pitfalls

| Pitfall | Why It Happens | How to Avoid |
|---------|----------------|--------------|
| Oversimplification that distorts meaning | Removing nuance removes accuracy | Clinical review after every rewrite |
| Condescending tone | Overcompensating for simplicity | Write clearly, not childishly |
| Jargon blind spots | Writer is too close to the domain | Have a non-medical person flag jargon |
| Missing safety information | Focused on simplification, not completeness | Use a safety checklist for every document |
| One-size-fits-all | Same materials for all populations | Adapt for audience-specific needs |
| Translation without adaptation | Literal translation misses cultural context | Use cultural adaptation, not just translation |

## Quality Checklist

- [ ] Readability score at grade 5-8 level (Flesch-Kincaid or SMOG)
- [ ] All medical jargon replaced or defined
- [ ] Sentences average 15 words or fewer
- [ ] Active voice used throughout
- [ ] Most important information comes first
- [ ] Action steps are numbered and specific
- [ ] Safety netting included (when to call doctor, warning signs)
- [ ] Teach-Back test completed with a non-expert
- [ ] Clinical accuracy verified by healthcare professional
- [ ] Culturally appropriate for target audience

## Examples

### Example: Medication Instructions Rewrite

**Before (Grade 12+):**
> "Administer metformin 500mg orally twice daily with meals. Contraindicated in patients with renal insufficiency (eGFR <30). Monitor hepatic function periodically. Discontinue if lactic acidosis is suspected."

**After (Grade 6):**
> **How to Take Your Metformin**
> - Take 1 pill (500mg) **2 times a day** — with breakfast and dinner.
> - Always take it with food to avoid an upset stomach.
>
> **When to Call Your Doctor**
> Call your doctor if you have:
> - Very fast breathing
> - Muscle pain that won't go away
> - Feeling very weak or tired
> - Stomach pain, nausea, or vomiting
>
> **Important:** Your doctor needs to check your kidneys and liver with blood tests. Keep all your lab appointments.
