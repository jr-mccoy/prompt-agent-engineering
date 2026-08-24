---
title: "Voice Clone Profile Builder"
category: professional-writing/voice
description: "Analyze writing samples to build a comprehensive, reusable voice profile that enables AI to generate content authentically matching a person's writing style, tone, and rhetorical patterns"
techniques:
  - ST-01
  - ST-02
  - RT-02
  - ED-05
  - ST-16
  - AG-01
  - AG-10
  - NE-04
  - ED-06
  - QA-02
difficulty: advanced
tags:
  - voice-cloning
  - style-transfer
  - voice-profile
  - writing-style
  - tone-matching
  - ghostwriting
  - brand-voice
  - style-guide
updated: "2026-04-08"
related_prompts:
  - domain-creative-writing/writing_voice_development.md
  - domain-business-strategy/startup/copy/startup_tone_of_voice.md
---

# Voice Clone Profile Builder

**Objective:** Analyze one or more writing samples from a specific person to produce a comprehensive, reusable Voice Profile — a style guide that enables AI to generate new content that authentically sounds like that person.

**When to use:**
- You need AI-generated content that matches a specific person's writing voice
- You're ghostwriting and need to internalize someone's style
- You want to maintain voice consistency across AI-assisted drafts
- You're building a persistent style guide for ongoing AI collaboration
- A team needs to write in a founder's, executive's, or thought leader's voice

**What makes this different from the Voice Print Extractor:**
The Voice Print Extractor produces a lightweight 150-word snapshot. This prompt performs deep linguistic analysis across multiple dimensions, produces a multi-section reusable style guide, includes calibration tests, and handles voice variation across contexts. It's designed to be saved and reused as a system prompt or reference document for ongoing AI writing.

---

## Your Input

### Writing Samples

Provide **2-5 writing samples** (the more variety, the better the profile). Ideal samples:
- Are **300-1,000 words each** (longer is better)
- Represent **different contexts** (e.g., blog post, email, presentation, social media, internal memo)
- Were **written by the person themselves** (not heavily edited by others)
- Are **recent** (voice evolves — use samples from the last 1-2 years)

```
SAMPLE 1 — [Context: e.g., "Blog post about product launch"]
[Paste writing here]
```

```
SAMPLE 2 — [Context: e.g., "Email to team about Q3 priorities"]
[Paste writing here]
```

```
SAMPLE 3 — [Context: e.g., "LinkedIn post about industry trend"]
[Paste writing here]
```

*(Add more samples as available. Minimum: 1 sample of 500+ words. Recommended: 3-5 samples across different formats.)*

### Optional Context
- **Who is this person?** [Role, industry, audience they typically write for]
- **What will the voice profile be used for?** [Blog posts, emails, social media, speeches, all of the above]
- **Are there any known style preferences?** [e.g., "They hate jargon" or "They always use Oxford commas"]

---

## Instructions

### Phase 1: Forensic Voice Analysis

Analyze all provided samples across these dimensions. Do not guess or fill in dimensions you can't observe — mark them as "Insufficient data" if the samples don't reveal that trait.

#### 1.1 Sentence Architecture

| Dimension | What to Measure | Finding |
|-----------|----------------|---------|
| **Average length** | Short (≤12 words), Medium (13-25), Long (26+) | [Measured from samples] |
| **Length variation** | Consistent or mixed? Intentional rhythm? | [Pattern observed] |
| **Complexity** | Simple, compound, complex, compound-complex — what's the default? | [Dominant type] |
| **Opening patterns** | How do sentences typically start? (Subject-verb? Dependent clause? Transitional phrase? Question?) | [Top 3 patterns] |
| **Paragraph length** | Short (1-3 sentences), Medium (4-6), Long (7+) | [Pattern observed] |
| **Paragraph architecture** | Lead with the point? Build to it? Meander? | [Structure pattern] |

#### 1.2 Word Choice & Vocabulary

| Dimension | What to Measure | Finding |
|-----------|----------------|---------|
| **Register** | Formal ←→ Casual (scale 1-5) | [Position + evidence] |
| **Vocabulary level** | Common words or specialized/unusual ones? | [Pattern + examples] |
| **Jargon usage** | Avoids? Embraces? Uses then explains? | [Pattern + examples] |
| **Concrete vs abstract** | Sensory/specific or conceptual/theoretical? | [Ratio + examples] |
| **Verb energy** | Passive vs active voice ratio; strong verbs vs weak verbs | [Pattern + examples] |
| **Signature words** | Words or phrases that recur across samples | [List with frequency] |
| **Words they avoid** | Notably absent words common in their field | [List if detectable] |
| **Contractions** | Always, sometimes, never? | [Pattern] |

#### 1.3 Rhetorical Fingerprint

| Dimension | What to Measure | Finding |
|-----------|----------------|---------|
| **Argument structure** | How do they build a case? (Evidence first? Assertion then support? Story then lesson?) | [Pattern] |
| **Persuasion mode** | Logic-driven, emotion-driven, credibility-driven, or blend? | [Dominant mode] |
| **Transitions** | How do they connect ideas? (Explicit connectors? Juxtaposition? White space?) | [Style + examples] |
| **Use of questions** | Rhetorical? Socratic? Rare? Frequent? | [Pattern + examples] |
| **Use of lists/structure** | Bullet-heavy? Prose-only? Numbered steps? | [Preference] |
| **Metaphor & analogy** | Frequent? Rare? What domains do they draw from? | [Pattern + examples] |
| **Humor & wit** | Dry? Self-deprecating? Absent? Sarcastic? Playful? | [Style + examples] |
| **Cultural references** | Pop culture? Academic? Industry? Historical? Sports? | [Domain pattern] |

#### 1.4 Emotional & Tonal DNA

| Dimension | What to Measure | Finding |
|-----------|----------------|---------|
| **Default emotional register** | Optimistic, measured, urgent, contemplative, energetic, skeptical? | [Primary + secondary] |
| **Warmth level** | Distant/professional ←→ Warm/personal (scale 1-5) | [Position + evidence] |
| **Confidence expression** | Hedged ("I think maybe...") vs direct ("Here's what works") vs authoritative ("The data shows...") | [Pattern] |
| **Vulnerability** | Do they share doubts, mistakes, personal stories? How much? | [Level + examples] |
| **How they handle disagreement** | Diplomatic? Direct? Avoidant? Reframing? | [Style if visible] |
| **Energy level** | Calm and measured vs high-energy and intense | [Pattern] |

#### 1.5 Structural Habits

| Dimension | What to Measure | Finding |
|-----------|----------------|---------|
| **Opening style** | How do they begin pieces? (Hook? Context? Bold claim? Anecdote? Question?) | [Pattern across samples] |
| **Closing style** | How do they end? (Call to action? Summary? Open question? Callback? Forward look?) | [Pattern across samples] |
| **Section structure** | How do they organize longer pieces? | [Pattern] |
| **Use of examples** | Frequent? Always real-world? Hypothetical? Personal anecdotes? | [Style] |
| **Formatting patterns** | Headers, bold, italics, em-dashes, parentheticals, ellipses | [Distinctive usage] |
| **Punctuation personality** | Em-dash lover? Semicolon user? Exclamation mark policy? Parenthetical asides? | [Signature patterns] |

### Phase 2: Cross-Sample Consistency Check

Compare findings across all samples:

1. **Consistent traits** — What stays the same regardless of context? These are the core voice.
2. **Context-dependent traits** — What shifts based on audience or format? These are tone adaptations.
3. **Contradictions** — Any traits that conflict between samples? Flag these for the Contextual Tone Map.

**Confidence assessment for each dimension:**
- **High** — Trait is consistent across 3+ samples with clear evidence
- **Medium** — Trait appears in 2 samples or is somewhat consistent
- **Low** — Observed in 1 sample only, or ambiguous

### Phase 3: Build the Voice Profile

Produce the following reusable style guide document:

---

## VOICE PROFILE: [Person's Name or Identifier]

*Generated from [N] writing samples across [list contexts]. Use this profile as a system prompt or reference when generating content in this person's voice.*

### Voice Summary (The Quick Version)
*[3-5 sentences capturing the essence of this person's writing voice. This should be vivid and specific enough that someone could immediately adjust their writing after reading only this section.]*

### Core Voice Traits
*[5-7 defining characteristics, ranked by confidence. Format:]*

| Trait | Description | Confidence | Evidence |
|-------|------------|------------|----------|
| [Trait name] | [Specific description] | High/Med/Low | [Brief quote or pattern reference] |

### The Voice Spectrum: What They Sound Like vs. Don't

**This voice IS:**
- [Trait] — *"[example phrase or sentence from samples]"*
- [Trait] — *"[example phrase or sentence from samples]"*
- [Trait] — *"[example phrase or sentence from samples]"*

**This voice is NEVER:**
- [Anti-trait] — *"[example of what they would NOT write, and why]"*
- [Anti-trait] — *"[example of what they would NOT write, and why]"*
- [Anti-trait] — *"[example of what they would NOT write, and why]"*

### Sentence-Level Style Guide

**Sentence construction rules:**
- [Rule 1 with example from samples]
- [Rule 2 with example from samples]
- [Rule 3 with example from samples]

**Word choice rules:**
- **Prefer:** [words/types this person gravitates toward]
- **Avoid:** [words/types this person never uses]
- **Signature phrases:** [recurring expressions to incorporate naturally]

**Punctuation & formatting rules:**
- [Rule with example]
- [Rule with example]

### Contextual Tone Map

*How the voice adapts across different contexts while maintaining core identity:*

| Context | What Changes | What Stays | Example Adjustment |
|---------|-------------|------------|-------------------|
| [Context 1: e.g., Blog post] | [Adaptations] | [Constants] | [Sample sentence] |
| [Context 2: e.g., Email to team] | [Adaptations] | [Constants] | [Sample sentence] |
| [Context 3: e.g., Social media] | [Adaptations] | [Constants] | [Sample sentence] |
| [Context 4: e.g., Formal presentation] | [Adaptations] | [Constants] | [Sample sentence] |

### Rhetorical Playbook

**How this person builds arguments:**
1. [Step 1 of their typical argument pattern]
2. [Step 2]
3. [Step 3]

**Persuasion tools they reach for:**
- [Tool 1 with example]
- [Tool 2 with example]

**Transitions they use:**
- [List of characteristic transition patterns with examples]

### Quick-Reference Card (For AI System Prompts)

```
VOICE INSTRUCTIONS:
- Tone: [2-3 word description]
- Register: [formal/casual/conversational scale position]
- Sentences: [length and complexity pattern]
- Vocabulary: [level and preferences]
- Personality on page: [key personality traits that show through]
- Structure: [paragraph and section habits]
- ALWAYS: [3 things to always do]
- NEVER: [3 things to never do]
- When in doubt, default to: [single guiding principle]
```

---

### Phase 4: Calibration Tests

Generate **3 short test passages** (75-150 words each) to validate the voice profile:

**Test 1 — [Context matching one of the provided samples]**
*Write a passage on a DIFFERENT topic but in the same context as one of the samples. The reader should feel like the same person wrote it.*

**Test 2 — [New context not in the samples]**
*Write a passage in a context NOT represented in the samples (e.g., if all samples were blog posts, write a short email or social post). The voice should still be recognizable.*

**Test 3 — [Challenging topic]**
*Write about something emotionally or intellectually different from the samples (e.g., if samples are upbeat product posts, write something more reflective or critical). The voice should adapt but remain identifiable.*

**For each test, include a self-audit:**
- Which Voice Profile traits are demonstrated?
- Which traits were hardest to maintain?
- What would the real author likely change?

---

## Verification & Quality Gates

### Before delivering the Voice Profile, verify:

- [ ] **Every trait has evidence** — No trait is asserted without a quote or pattern reference from the samples
- [ ] **Confidence levels are honest** — Single-sample observations are marked Low, not inflated
- [ ] **"IS/NEVER" section has contrast** — The anti-traits are specific, not just inversions of positive traits
- [ ] **Contextual Tone Map is grounded** — If only one context was provided, say so; don't fabricate adaptations
- [ ] **Calibration tests feel right** — Read them aloud; do they sound like one person?
- [ ] **Quick-Reference Card is actionable** — Could someone paste it as a system prompt and get recognizable output?

### False-Positive Prevention (MUST follow)

**DON'T:**
- Invent voice traits not evidenced in the samples (don't assume "warm" because the person writes about people)
- Confuse topic preferences with voice traits (writing about technology doesn't mean the voice is "technical")
- Over-index on a single sample when it may be an outlier
- Describe generic "good writing" traits as if they're distinctive to this person
- Flatten genuine complexity — if the voice is contradictory across contexts, say so
- Project stereotypes based on the person's role, industry, or demographics

**DO:**
- Ground every assertion in specific textual evidence
- Distinguish between core voice (consistent) and contextual tone (variable)
- Flag low-confidence observations explicitly
- Note when samples are insufficient to assess a dimension
- Acknowledge that voice profiles are approximations, not perfect captures
- Include the person's quirks and imperfections — those are often the most distinctive elements

---

## Example Output (Abbreviated)

### VOICE PROFILE: Alex Chen (VP Engineering)

**Voice Summary:**
Alex writes like someone explaining a whiteboard diagram over coffee — structured but conversational, using concrete metaphors from building and engineering to make abstract concepts tangible. Sentences are medium-length and punchy, rarely compound-complex. There's a quiet confidence: assertions are direct but not aggressive, often softened with "Here's the thing" or "What I've learned is." Humor is dry and infrequent, deployed for emphasis rather than entertainment.

**Core Voice Traits:**

| Trait | Description | Confidence | Evidence |
|-------|------------|------------|----------|
| Builder metaphors | Consistently uses construction/architecture metaphors for abstract ideas | High | "We're laying foundation before framing walls" (S1), "The scaffolding isn't the building" (S3) |
| Direct assertion + earned softener | States positions directly, then adds experiential qualifier | High | "This approach fails. I've seen it fail three times." (S1, S2) |
| Short paragraphs | Rarely exceeds 3 sentences per paragraph | High | Avg 2.4 sentences across all samples |
| Conversational register | Writes at a 4/5 casual despite technical topics | Medium | Contractions always, "look" and "here's the thing" as openers |
| Minimal hedging | Almost never uses "I think" or "perhaps" or "it seems" | Medium | 0 hedges found across 2,400 words |

**This voice IS:**
- Direct without being blunt — *"We shipped it. It broke. Here's what we learned."*
- Concrete and visual — *"Think of your API like a restaurant menu, not a buffet."*
- Experiential — *"I've watched this pattern play out at three different companies."*

**This voice is NEVER:**
- Academic or abstract — would never write *"The paradigmatic implications of this architectural decision warrant further deliberation"*
- Performatively humble — would never write *"I'm just thinking out loud here, but maybe possibly..."*
- Buzzword-driven — would never write *"We need to leverage synergies to drive holistic transformation"*

**Quick-Reference Card:**
```
VOICE INSTRUCTIONS:
- Tone: Confident, grounded, pragmatic
- Register: Conversational (4/5 casual)
- Sentences: Medium-short, simple/compound, rarely complex
- Vocabulary: Plain language, construction/building metaphors, no jargon
- Personality on page: Experienced practitioner, dry wit, pattern-matcher
- Structure: Short paragraphs (2-3 sentences), opens with assertion, closes with lesson
- ALWAYS: Use concrete metaphors, state position directly, reference real experience
- NEVER: Hedge with "I think/perhaps", use buzzwords, write paragraphs over 4 sentences
- When in doubt, default to: Shorter, more direct, more concrete
```

---

## Techniques Used

- **ST-01** (Clear Objective Statement) — Unambiguous goal: build a reusable voice profile
- **ST-02** (Structured Sequential Instructions) — 4-phase process: analyze, cross-check, build, calibrate
- **RT-02** (Multi-Dimensional Analysis) — 5 analysis dimensions with specific measurement criteria
- **ED-05** (Reference Class Priming) — Uses the person's own writing as the quality benchmark
- **ST-16** (Behavioral Trait Declarations) — Captures communication style, stance, and interaction patterns
- **AG-01** (Personality-First Role Definition) — Builds persona from personality traits, not just expertise
- **AG-10** (Emotional Context Spectrum) — Maps voice adaptation across different contexts
- **NE-04** (Good vs Bad Example Calibration) — IS/NEVER contrast pairs define voice boundaries
- **ED-06** (Example Quantity Specification) — Requires multiple samples for robust profiling
- **QA-02** (Adversarial Thinking) — Calibration tests stress-test the profile in unfamiliar territory
