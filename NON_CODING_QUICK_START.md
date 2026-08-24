# Non-Coding Quick Start: Building Prompts for Everything Else

> **Root-level access for AI agents.** This guide provides fast reference for constructing effective prompts for non-coding domains: education, writing, healthcare, research, personal development, business communication, and specialized professional fields.
>
> **For coding/technical prompts:** See [AI_AGENT_QUICK_START.md](AI_AGENT_QUICK_START.md)
>
> **For image generation prompts:** See [domain-image-generation/IMAGE_GENERATION_GUIDE.md](domain-image-generation/IMAGE_GENERATION_GUIDE.md) - Image generation prompts require fundamentally different techniques (grid forcing, constraint redundancy, terminology steering) that are not covered here.
>
> **Creating a new resource?** Use the [Authoring Toolkit](authoring/NEW_PROMPT_TEMPLATE.md): template, technique picker, and checklist.
>
> **Saving the prompt into this repository?** Include the YAML frontmatter block (`title`, `category`, `description`, `techniques`, `difficulty`, `tags`, `updated`, `related_prompts`) — it powers `PROMPT_INDEX.json` discovery. See [PROMPT_QUALITY_STANDARDS.md](PROMPT_QUALITY_STANDARDS.md) for the spec.

---

## Why Non-Coding Prompts Are Different

| Dimension | Coding Prompts | Non-Coding Prompts |
|-----------|----------------|-------------------|
| **Verification** | Tests pass, code compiles | Subjective quality, "feels right" |
| **Output Format** | Code blocks, specific syntax | Prose, visuals, frameworks, tables |
| **Context Needs** | Tech stack, error messages | Audience, tone, purpose, constraints |
| **Success Criteria** | Works/doesn't work | Persuasive, clear, actionable, appropriate |
| **Iteration Style** | Debug, fix, test | Refine tone, expand scope, adjust audience |
| **False Positives** | Wrong code is obvious | Wrong advice can seem plausible |

This guide teaches you to handle these differences systematically.

---

## 1. Quick Classification (5 seconds)

**Ask yourself: What is the user fundamentally trying to do?**

### Task Types

| Type | User Intent | Example Requests |
|------|-------------|------------------|
| **CREATE** | Generate something new | "Write a lesson plan," "Draft a proposal," "Create a character" |
| **LEARN** | Understand something | "Explain this concept," "Help me understand," "What does this mean?" |
| **DECIDE** | Make a choice | "Should I...," "What's the best option for," "Help me choose" |
| **COMMUNICATE** | Convey information | "Draft an email," "Present this to," "Explain to my boss" |
| **IMPROVE** | Refine existing content | "Make this better," "Edit my draft," "Strengthen this argument" |
| **SIMULATE** | Practice or roleplay | "Act as," "Let me practice," "Interview me as if" |

### Domain Detection

| If request mentions... | Route to Domain |
|-----------------------|-----------------|
| Students, lessons, curriculum, grades, teaching | **Education/Teaching** |
| Story, characters, plot, narrative, creative writing | **Creative Writing** |
| Patient, clinical, diagnosis, treatment, symptoms | **Healthcare/Clinical** |
| Research, methodology, literature, hypothesis, study | **Research/Academic** |
| Goals, habits, career, self-improvement, mindset | **Personal Development** |
| Stakeholders, presentation, PRD, proposal, business | **Professional Communication** |
| Legal, contracts, finance, real estate, trades | **Specialized Fields** |

*Once classified, use the appropriate Task Type Pattern below.*

---

## 2. Universal Principles: The 5 Elements

Every good non-coding prompt addresses these five elements:

### Element 1: Intent Clarity

**Bad:** "Help me write something for my class"
**Good:** "Create a 10-question quiz on the American Revolution for 8th graders, focusing on causes and key battles"

**Pattern:**
```
I need to [specific action] for [specific purpose/audience] that [measurable outcome]
```

### Element 2: Audience Specification

Non-coding output always has an audience. Specify:

- **Who:** Age, role, expertise level, relationship to creator
- **What they know:** Prior knowledge, context they have
- **What they need:** What action or understanding should result
- **Constraints:** Reading level, time available, cultural considerations

**Example:**
```
Audience:
- 5th grade students (ages 10-11)
- Have studied basic fractions
- Need to understand fraction multiplication conceptually before learning the algorithm
- Reading level: Flesch-Kincaid Grade 5
```

### Element 3: Context That Matters

Different domains require different context:

| Domain | Critical Context |
|--------|-----------------|
| **Education** | Grade level, learning objectives, prior knowledge, time available, accessibility needs |
| **Creative Writing** | Genre, tone, word count, target publication, existing style guide |
| **Healthcare** | Patient demographics, clinical setting, evidence requirements, communication goals |
| **Research** | Field, methodology constraints, publication target, existing literature |
| **Personal Development** | Current situation, constraints, values, past attempts, timeline |
| **Professional Communication** | Stakeholder expectations, organizational culture, decision needed, political considerations |
| **Specialized Fields** | Regulatory requirements, professional standards, jurisdictional rules |

**Capture the purpose, not just the task.** The *task* is what to do ("summarize this meeting"). The *purpose* is what the output is for — what decision it informs, who reads it next, where it goes. The same task aimed at different purposes should produce different outputs: "summarize this meeting" *as a reminder to attendees* is not the same as "...*so a director who wasn't there can decide whether to greenlight the project.*" Always state the downstream purpose.

**The colleague test.** Read your prompt as if you were a capable person seeing it cold, with no knowledge of the situation. Could you do the task well, or would you need to ask clarifying questions first? Those questions are exactly the context gaps that make a model guess.

**Delimit pasted source material.** When the prompt includes a chunk of content for the model to work on — a draft to improve, a transcript to summarize, research notes to synthesize — wrap it in a named XML-style tag (`<student_draft>`, `<meeting_transcript>`) and refer to it by name in the instructions. This keeps the model from mistaking the source material for instructions. See [authoring/PROMPT_STRUCTURE_GUIDE.md](authoring/PROMPT_STRUCTURE_GUIDE.md) for conventions and examples.

### Element 4: Output Specification

Be explicit about format, length, tone, and structure:

```markdown
**Output Requirements:**
- Format: [Narrative/List/Table/Outline/Script/Template]
- Length: [Word count/Page count/Time to read]
- Tone: [Formal/Conversational/Encouraging/Authoritative]
- Structure: [Sections required, headings to use]
- Must include: [Required elements]
- Must avoid: [Prohibited elements]
```

### Element 5: Quality Indicators

**Critical:** Define what "good" looks like for subjective output.

```markdown
**Quality Criteria:**
- The output is successful if: [specific observable outcomes]
- Verify by: [how to check quality]
- Red flags: [indicators of poor output]
```

---

## 3. Task Type Patterns

### CREATE Pattern

Use when user wants to generate something new.

```markdown
**Objective:** Create [specific artifact] for [audience] that [achieves outcome]

**Context:**
- Purpose: [Why this is being created]
- Audience: [Who will receive/use it]
- Constraints: [Length, format, tone, style requirements]
- Must include: [Required elements]
- Must avoid: [Prohibited elements]

**Quality Criteria:**
- Success looks like: [Observable outcome]
- The [audience] should feel/do: [Intended effect]
- Verify by: [How to check it worked]

**Create the [artifact] now.**
```

**Example Application:**
```markdown
**Objective:** Create a 45-minute lesson plan on photosynthesis for 7th graders that builds conceptual understanding before introducing the chemical equation.

**Context:**
- Purpose: First introduction to photosynthesis in biology unit
- Audience: 7th grade science class, mixed abilities, 28 students
- Constraints: 45-minute period, must include hands-on activity, aligns to NGSS MS-LS1-6
- Must include: Learning objectives, materials list, assessment check
- Must avoid: Lecturing more than 10 minutes continuously

**Quality Criteria:**
- Success: Students can explain why plants need sunlight in their own words
- Students should feel: Curious about plant biology, successful in understanding
- Verify by: Exit ticket asking "How do plants make their food?"

**Create the lesson plan now.**
```

---

### LEARN Pattern

Use when user wants to understand something.

```markdown
**Objective:** Explain [concept] to someone who [current knowledge level] so they can [what they'll do with knowledge]

**Learner Profile:**
- Current knowledge: [What they already know]
- Knowledge gaps: [What's missing]
- Learning goal: [What they need to accomplish]
- Preferred style: [Visual/verbal/hands-on/examples]

**Instructions:**
1. Start with a simple analogy from [familiar domain]
2. Explain the core concept in [3-5] key points
3. Provide [concrete example] showing the concept in action
4. Address the most common misconception: [specific misconception]
5. Give them a way to test their understanding

**Output Format:**
## The Simple Version
[Analogy and core concept in 2-3 sentences]

## How It Actually Works
[Step-by-step explanation]

## Real Example
[Concrete illustration]

## Common Mistake to Avoid
[Misconception and correction]

## Check Your Understanding
[Self-test question or exercise]
```

---

### DECIDE Pattern

Use when user needs to make a choice between options.

```markdown
**Decision:** [What needs to be decided]

**Context:**
- Current situation: [Where things stand now]
- Constraints: [Budget, time, resources, requirements]
- Stakeholders: [Who is affected and their priorities]
- Success criteria: [What makes this decision "right"]

**Instructions:**
1. Identify 3 viable options (including "do nothing" if applicable)

2. For each option, analyze:
   - What it involves
   - Pros (specific advantages)
   - Cons (specific disadvantages)
   - Best-fit scenario (when this is the right choice)
   - Hidden risks or assumptions

3. Compare options against the success criteria

4. Provide recommendation with:
   - Which option is best for this context
   - Key factors driving the recommendation
   - What could change this recommendation
   - Immediate next steps if chosen

**Expected Output:**

## Option 1: [Name]
[Full analysis]

## Option 2: [Name]
[Full analysis]

## Option 3: [Name]
[Full analysis]

## Comparison Matrix
| Criterion | Option 1 | Option 2 | Option 3 |
|-----------|----------|----------|----------|

## Recommendation
[Clear recommendation with reasoning]

## If You Choose This
[Concrete next steps]
```

---

### COMMUNICATE Pattern

Use when user wants to convey information to others.

```markdown
**Objective:** Draft [communication type] to [recipient] that [achieves outcome]

**Communication Context:**
- Recipient: [Who, their role, relationship to sender]
- Recipient's current state: [What they know, believe, feel]
- Desired end state: [What you want them to know, believe, feel, do]
- Channel: [Email, presentation, document, conversation]
- Tone required: [Formal/informal, urgent/routine, positive/neutral]

**Constraints:**
- Length: [Appropriate for channel and recipient]
- Must address: [Key points to cover]
- Must avoid: [Sensitive topics, problematic framing]
- Political considerations: [Organizational dynamics]

**Quality Criteria:**
- Successful if recipient: [Takes action, understands point, feels X]
- Red flags: [What would make this fail]

**Draft the [communication] now.**
```

**Example:**
```markdown
**Objective:** Draft an email to my manager requesting flexible work hours that gets approved

**Communication Context:**
- Recipient: Direct manager, 2 years working relationship, generally supportive
- Current state: Assumes I'm available 9-5, doesn't know about my childcare situation
- Desired end state: Approves 7-3 schedule, sees me as committed employee
- Channel: Email (formal request for documentation)
- Tone: Professional, solution-oriented, not apologetic

**Constraints:**
- Length: Under 200 words
- Must address: Proposed schedule, how I'll maintain availability, trial period offer
- Must avoid: Over-explaining personal circumstances, seeming entitled
- Political: Other team members have been denied similar requests

**Quality Criteria:**
- Successful if: Manager responds positively or asks clarifying questions (not flat rejection)
- Red flags: Defensive tone, too many justifications, unclear ask

**Draft the email now.**
```

---

### IMPROVE Pattern

Use when user wants to refine existing content.

```markdown
**Objective:** Improve [content type] to [specific improvement goal]

**Current Content:**
[Paste or describe the existing content]

**Improvement Focus:**
- Primary goal: [What most needs to improve - clarity, persuasiveness, tone, structure]
- Secondary goals: [Other improvements if possible]
- Preserve: [What's working and should not change]

**Target State:**
- Audience: [Who this is for]
- Purpose: [What it should accomplish]
- Quality bar: [What "good enough" looks like]

**Constraints:**
- Length: [Can expand/must shorten/keep same]
- Tone: [Adjust to X/maintain current]
- Format: [Keep/change structure]

**Instructions:**
1. Identify what's working in the current version
2. Identify specific weaknesses
3. Provide improved version
4. Explain key changes and why they help

**Expected Output:**

## What's Working
[Strengths to preserve]

## Areas for Improvement
[Specific weaknesses with examples]

## Improved Version
[Full revised content]

## Key Changes Made
[Explanation of major edits and their purpose]
```

---

### SIMULATE Pattern

Use when user wants to practice or roleplay.

```markdown
**Simulation:** [What scenario to simulate]

**Your Role:**
- You are: [Character/persona to adopt]
- Your perspective: [What you believe, value, prioritize]
- Your knowledge: [What you know and don't know]
- Your communication style: [How you talk, respond]

**User's Role:**
- They are practicing: [What skill they're developing]
- They should experience: [Realistic challenge or scenario]
- Success for them looks like: [Observable skill demonstration]

**Simulation Rules:**
- Stay in character as [role] throughout
- Respond realistically, including [realistic challenges]
- If they [common mistake], respond as [realistic consequence]
- If they [good technique], respond as [realistic positive reaction]
- Don't break character to give tips unless they explicitly ask

**Begin the simulation when the user starts.**
```

**Example:**
```markdown
**Simulation:** Job interview for senior product manager position

**Your Role:**
- You are: Hiring manager, VP of Product at a B2B SaaS company
- Your perspective: Value data-driven decisions, skeptical of candidates who can't give specific examples
- Your knowledge: Have seen 5 other candidates, 2 were strong
- Your communication style: Friendly but probing, ask follow-up questions

**User's Role:**
- They are practicing: Behavioral interview responses using STAR method
- They should experience: Follow-up questions that probe for specifics
- Success: Gives concrete examples with measurable outcomes

**Simulation Rules:**
- Stay in character as VP of Product
- If they give vague answers, ask "Can you give me a specific example?"
- If they give good STAR responses, nod and ask natural follow-up
- Don't break character to coach unless they say "pause" or "feedback please"

**Begin with:** "Thanks for coming in today. I've reviewed your resume and I'm excited to learn more about your experience. Let's start with a question about stakeholder management..."
```

---

## 4. Quality Without Tests: Verification Techniques

### How to Verify Non-Coding Output

Unlike code, you can't run tests. Use these verification approaches:

#### 1. Audience Simulation Check
```markdown
After generating:
Imagine you are [the target audience]. Read this output.
- Would you understand it? (Comprehension check)
- Would you trust it? (Credibility check)
- Would you act on it? (Actionability check)
- What questions would you still have? (Completeness check)
```

#### 2. Purpose Alignment Check
```markdown
After generating:
Review the output against the stated objective:
- Does it accomplish [specific goal]?
- Does it avoid [stated constraints]?
- Would [stakeholder] approve this?
```

#### 3. Red Flag Scan
```markdown
Before finalizing, check for:
- [ ] Unsupported claims presented as facts
- [ ] Tone mismatches (too formal/informal for audience)
- [ ] Missing critical information the audience needs
- [ ] Assumptions that may not apply to this context
- [ ] Cultural or sensitivity issues
```

### Handling Uncertainty

Non-coding domains often involve opinions, incomplete information, or contested claims. Handle uncertainty explicitly:

```markdown
**Uncertainty Acknowledgment Template:**

What we know with confidence:
- [Well-supported claims with evidence]

What we're less certain about:
- [Claim]: [Why uncertain - limited data, contested, context-dependent]

What we don't know:
- [Important unknowns that could change recommendations]

Given this uncertainty:
- [How to proceed, what to validate, when to revisit]
```

### Confidence Calibration

Assign confidence levels to claims and recommendations:

| Confidence | Meaning | Use When |
|------------|---------|----------|
| **High** | Strong evidence, widely accepted, verified | Multiple sources agree, expert consensus, empirical data |
| **Medium** | Reasonable inference, some evidence | Single source, logical extrapolation, common practice |
| **Low** | Best guess, limited evidence | Novel situation, conflicting information, hypothesis |

**Example:**
```markdown
## Recommendations

1. **Use active recall for studying** (High confidence)
   - Extensive research supports this technique
   - Meta-analyses show consistent effect sizes

2. **Schedule study sessions in morning** (Medium confidence)
   - Some research supports morning retention
   - Individual variation is significant

3. **This specific schedule will work for you** (Low confidence)
   - Based on general principles
   - Your personal constraints and preferences may differ
   - Recommend testing and adjusting
```

### False-Positive Prevention for Non-Coding

**The most common quality problem in non-coding prompts: plausible-sounding advice that's wrong for the context.**

#### Universal False-Positive Prevention

**DON'T:**
- Present best practices as universal rules (they depend on context)
- Give advice without knowing constraints
- Assume your audience matches the "typical" user
- State opinions as facts
- Recommend without acknowledging trade-offs
- Over-generalize from limited examples

**DO:**
- State assumptions explicitly
- Qualify recommendations with "if [condition]"
- Distinguish between evidence-based and experience-based claims
- Acknowledge when you're extrapolating
- Provide criteria for when advice doesn't apply
- Include "this might not work if..." caveats

#### Domain-Specific False-Positive Patterns

**Education:**
- DON'T assume grade level equals ability level
- DO ask about accommodations, IEPs, diverse learners

**Healthcare Communication:**
- DON'T provide medical advice (provide communication frameworks)
- DO emphasize this supports, not replaces, professional judgment

**Business Communication:**
- DON'T assume standard org culture
- DO ask about political dynamics and stakeholder relationships

**Creative Writing:**
- DON'T impose genre conventions as rules
- DO clarify author's intent before suggesting changes

---

## 5. Domain Quick Reference

| Domain | Guide | Key Prompts | Key Considerations |
|--------|-------|-------------|-------------------|
| **Education/Teaching** | [domain-education-teaching/](domain-education-teaching/) | Worksheet generators, lesson plans, assessments | Grade level, learning objectives, accessibility |
| **Creative Writing** | [domain-creative-writing/](domain-creative-writing/) | Story builders, character development, narrative arcs | Genre, tone, audience, length |
| **Healthcare/Clinical** | [domain-healthcare-clinical/](domain-healthcare-clinical/) | Clinical decision support, patient education | Safety, evidence, uncertainty, shared decision-making |
| **Research/Academic** | [domain-research-academic/](domain-research-academic/) | Literature review, methodology, analysis | Sources, rigor, bias awareness |
| **Personal Development** | [domain-personal-development/](domain-personal-development/) | Goal setting, habit building, career planning | Individual constraints, emotional sensitivity |
| **Professional Communication** | [domain-professional-communication/](domain-professional-communication/) | PRDs, presentations, proposals, stakeholder communication | Formality, politics, action orientation |
| **Specialized Fields** | [domain-specialized-fields/](domain-specialized-fields/) | Legal, trades, real estate, marketing | Field-specific norms, regulations, terminology |
| **Finance** | [domain-finance/](domain-finance/) | Finance & economics field guide | Not investment advice, disclosures, individual circumstances |
| **Psychology** | [domain-psychology/](domain-psychology/) | Psychology, therapy & behavioral health | Clinical fidelity (model-testing), ethical boundaries |

---

## 6. Universal Templates

### Template 1: General Creation

```markdown
# [Artifact Type] Creation

**Objective:** Create [specific artifact] for [audience] to achieve [outcome]

**Context:**
- Purpose: [Why needed]
- Audience: [Who, their characteristics]
- Use case: [How it will be used]

**Requirements:**
- Format: [Structure, sections]
- Length: [Constraints]
- Tone: [Voice, formality]
- Must include: [Required elements]
- Must avoid: [Prohibited elements]

**Quality Criteria:**
- Success: [What good looks like]
- Verify by: [How to check]

**Create the [artifact].**
```

### Template 2: Explanation/Teaching

```markdown
# Explain [Topic]

**Objective:** Help [audience] understand [topic] well enough to [application]

**Audience:**
- Knowledge level: [What they know]
- Goal: [What they need to do with this]
- Constraints: [Time, attention, reading level]

**Instructions:**
1. Open with why this matters to them
2. Use analogy from [familiar domain]
3. Explain in [number] key points
4. Provide concrete example
5. Address misconception: [common mistake]
6. Give them a way to verify understanding

**Format:**
- Length: [Constraint]
- Style: [Conversational/formal/etc.]
- Include: [Visuals, examples, exercises as appropriate]
```

### Template 3: Decision Analysis

```markdown
# Decision: [What to decide]

**Context:**
- Current situation: [Status quo]
- Trigger: [Why deciding now]
- Stakeholders: [Who cares and why]
- Constraints: [Budget, time, requirements]
- Success criteria: [What makes decision "right"]

**Analyze:**
1. Generate 3+ viable options
2. For each: description, pros, cons, risks, best-fit scenario
3. Compare against success criteria
4. Recommend with clear reasoning

**Output:**
- Options with full analysis
- Comparison matrix
- Clear recommendation
- Implementation next steps
```

### Template 4: Document Drafting

```markdown
# Draft: [Document Type]

**Purpose:** [What this document accomplishes]

**Audience:**
- Primary reader: [Who]
- Their goal: [What they want from this]
- Their context: [What they know]

**Requirements:**
- Tone: [Formal/informal]
- Length: [Target]
- Format: [Structure required]
- Key messages: [Must convey]
- Call to action: [What reader should do]

**Constraints:**
- Avoid: [Topics, tones, formats to skip]
- Sensitive areas: [Handle carefully]

**Draft the document.**
```

### Template 5: Research Synthesis

```markdown
# Synthesize: [Topic]

**Objective:** Synthesize information on [topic] for [audience/purpose]

**Scope:**
- Focus: [Specific aspects]
- Depth: [Overview/detailed]
- Sources: [What to draw from]

**Instructions:**
1. Identify key themes/findings
2. Note areas of consensus
3. Highlight disagreements or gaps
4. Assess quality/reliability of information
5. Synthesize into coherent summary
6. Note limitations and what's still unknown

**Output:**
## Key Findings
[Main takeaways]

## Areas of Agreement
[What sources agree on]

## Contested or Unclear
[Where sources disagree or evidence is weak]

## Synthesis
[Integrated understanding]

## Limitations
[What we don't know, caveats]
```

### Template 6: Feedback/Critique

```markdown
# Provide Feedback on [Content]

**Content to Review:**
[The material being critiqued]

**Context:**
- Creator's goal: [What they're trying to achieve]
- Audience: [Who this is for]
- Constraints: [What they're working with]
- Feedback purpose: [Improve quality/validate direction/catch errors]

**Instructions:**
1. Start with what's working (be specific, not just "nice")
2. Identify areas for improvement (specific, actionable)
3. Prioritize feedback (what matters most)
4. Provide concrete suggestions
5. End with overall assessment and encouragement

**Output Format:**
## Strengths
- [Specific thing that works]: [Why it works]

## Opportunities for Improvement
1. [Issue]: [Specific suggestion] - Priority: [High/Medium/Low]
2. [Issue]: [Specific suggestion] - Priority: [High/Medium/Low]

## Overall Assessment
[Summary judgment and next steps]
```

---

## 7. Worked Examples

### Example 1: Teacher Creating a History Worksheet

**User says:** "I need a worksheet on the causes of World War I for my 10th grade class"

**Step 1: Classification**
- Task Type: CREATE
- Domain: Education/Teaching

**Step 2: Context Gathering**
- Grade level: 10th grade (ages 15-16)
- Subject: World history
- Topic: Causes of WWI
- Missing info: Learning objectives, time for completion, question types desired

**Step 3: Apply CREATE Pattern**

```markdown
**Objective:** Create a worksheet on causes of World War I for 10th graders that assesses understanding of the main contributing factors

**Context:**
- Purpose: Formative assessment after lecture on WWI causes
- Audience: 10th grade world history students, have covered imperialism, nationalism, and the alliance system
- Constraints: 20-25 minutes completion time, mix of question types

**Requirements:**
- 10-12 questions total
- Mix: multiple choice (4), short answer (4), one extended response
- Cover: militarism, alliances, imperialism, nationalism, assassination trigger
- Include primary source excerpt for analysis
- Aligned to state standards for historical causation

**Quality Criteria:**
- Success: Students can identify MAIN causes and explain how they connected
- Questions at various Bloom's levels (recall through analysis)
- Clear instructions, readable formatting

**Create the worksheet.**
```

**Step 4: Quality Check**

After generating, verify:
- [ ] Covers all major causes (MAIN + trigger)
- [ ] Age-appropriate vocabulary and complexity
- [ ] Clear instructions for each section
- [ ] Point values add up correctly
- [ ] Answer key is accurate

---

### Example 2: Writer Developing a Character

**User says:** "Help me create a villain for my fantasy novel"

**Step 1: Classification**
- Task Type: CREATE (with LEARN elements about character development)
- Domain: Creative Writing

**Step 2: Context Gathering**

Need to know:
- Genre specifics (epic fantasy, urban fantasy, etc.)
- Protagonist's nature (to create meaningful opposition)
- Theme of the story (villain should embody or challenge it)
- Tone (dark, humorous, morally gray)
- Role (main antagonist, secondary villain, redeemable)

**Step 3: Apply CREATE Pattern with Character-Specific Elements**

```markdown
**Objective:** Create a compelling villain character for [epic fantasy novel] who serves as meaningful opposition to [protagonist traits] while embodying the theme of [theme]

**Story Context:**
- Genre: Epic fantasy with political intrigue
- Protagonist: Young heir learning to rule, values justice and transparency
- Theme: The corrupting nature of power
- Tone: Serious with moments of dark humor
- Villain role: Primary antagonist, currently in power

**Character Development Requirements:**
1. **Motivation:** What do they want? Why do they want it? What's the emotional wound driving them?
2. **Methods:** How do they pursue their goals? What lines will/won't they cross?
3. **Relationship to protagonist:** Why are they opposed? What do they see in each other?
4. **Complexity:** What makes them more than "pure evil"? What would they say justifies their actions?
5. **Arc:** How will they change through the story? What's their fatal flaw?

**Output Format:**
## Character Profile
[Name, title, appearance, public persona vs. private reality]

## Psychological Profile
[Motivation, fears, values, worldview]

## Backstory
[Key events that shaped them - show, don't tell in the novel]

## Opposition to Protagonist
[Why they conflict, what each represents]

## Complexity/Humanity
[What makes them sympathetic or understandable]

## Story Function
[What they reveal about the theme, how they challenge protagonist to grow]
```

---

### Example 3: Professional Drafting a Proposal

**User says:** "I need to convince my leadership to invest in a new customer analytics platform"

**Step 1: Classification**
- Task Type: COMMUNICATE (with DECIDE elements for leadership)
- Domain: Professional Communication

**Step 2: Context Gathering**

Need to know:
- Current state (what exists today, pain points)
- Proposed solution specifics
- Cost and resource requirements
- Expected benefits (quantified if possible)
- Audience (who decides, what they care about)
- Organizational context (budget climate, competing priorities)

**Step 3: Apply COMMUNICATE Pattern with Proposal Structure**

```markdown
**Objective:** Draft a business proposal to leadership for investing $150K in a customer analytics platform that will increase retention by 8%

**Communication Context:**
- Recipients: VP of Operations, CFO (final approver)
- Their current state: Frustrated with customer churn (12%), making decisions on gut feel
- Desired end state: Approve Q2 budget allocation, see this as strategic priority
- Channel: Written proposal (3-5 pages) + 15-min presentation
- Tone: Data-driven, confident but not overselling, acknowledges risks

**Key Messages:**
1. Current churn costs us $2M annually
2. Platform enables data-driven retention (specific capabilities)
3. Expected ROI: 8% churn reduction = $400K annually
4. Proven vendor with references in our industry
5. Implementation risk is manageable (6-month rollout, dedicated support)

**Objections to Address:**
- "We tried analytics before" - Different scope, better vendor
- "Budget is tight" - ROI pays back in 4 months
- "IT bandwidth" - Vendor handles implementation

**Constraints:**
- Keep proposal under 5 pages (executives won't read more)
- Lead with business problem, not technology features
- Include executive summary they can forward up

**Quality Criteria:**
- Successful if: CFO asks clarifying questions (engaged), VP champions internally
- Red flags: Too much jargon, buried ask, defensive tone

**Draft the proposal.**
```

**Step 4: Quality Check**

After generating, verify:
- [ ] Executive summary stands alone (could forward to CEO)
- [ ] Problem clearly articulated with numbers
- [ ] Benefits are specific and credible (not hyperbole)
- [ ] Cost and timeline are explicit
- [ ] Objections are anticipated and addressed
- [ ] Clear ask with specific next step

---

## 8. Anti-Patterns: Common Mistakes

### Mistake 1: Vague Audience

**Problem:** Output doesn't connect because audience wasn't specified.

**Bad Prompt:**
```
Write an explanation of compound interest.
```

**Good Prompt:**
```
Explain compound interest to a 16-year-old who just got their first job and opened a savings account. They understand basic math but have never thought about money growing over time. Use an example with $100 and 5 years.
```

**Why it matters:** The same concept needs completely different explanations for a teenager vs. a finance professional vs. a retiree.

---

### Mistake 2: Missing Tone Specification

**Problem:** Output is technically correct but wrong tone for context.

**Bad Prompt:**
```
Write an email to my team about the project deadline extension.
```

**Good Prompt:**
```
Write an email to my team (5 engineers who've been working overtime) announcing that the deadline is extended by 2 weeks. Tone: Celebratory relief, not "we failed." They should feel appreciated for their hard work and energized by the extra time, not deflated.
```

**Why it matters:** Same information, completely different reactions based on how it's framed.

---

### Mistake 3: No Success Criteria

**Problem:** No way to evaluate if output is good.

**Bad Prompt:**
```
Create a presentation about our product.
```

**Good Prompt:**
```
Create a 10-slide sales presentation for our CRM product targeting small business owners. Success criteria:
- After viewing, prospect should understand top 3 differentiators
- Should be able to self-identify if they're a fit
- Clear next step (book demo) with low friction
- Total presentation time: 12-15 minutes
```

**Why it matters:** Without success criteria, there's no way to improve the output or know when you're done.

---

### Mistake 4: Asking for Opinions Without Context

**Problem:** Getting generic advice that doesn't apply.

**Bad Prompt:**
```
Should I go back to school for an MBA?
```

**Good Prompt:**
```
I'm a 32-year-old product manager with 8 years experience, making $140K in a stable job. I'm considering an MBA because I want to transition to general management. Help me think through this decision:
- My constraints: $150K max debt, need to keep working or finish in <2 years
- My alternatives: Executive MBA, online programs, management training at current company
- What I value: Learning with peers, career acceleration, not just credentials
- What I'm worried about: Opportunity cost, whether it actually helps PMs become GMs
```

**Why it matters:** Good advice depends entirely on individual circumstances. Generic advice is often wrong advice.

---

### Mistake 5: Over-Scoping

**Problem:** Asking for too much in one prompt, getting shallow everything.

**Bad Prompt:**
```
Write a complete business plan for a coffee shop including market analysis, financial projections, marketing strategy, operations plan, and funding requirements.
```

**Good Prompt:**
```
I'm writing a business plan for a specialty coffee shop in Austin. Right now, I need help with the competitive analysis section specifically. There are 3 main competitors within 1 mile. Help me:
1. Create a framework for comparing them
2. Identify what dimensions matter for coffee shop competition
3. Find the underserved position I could occupy

I'll tackle financial projections separately after positioning is clear.
```

**Why it matters:** Deep analysis on one section beats shallow coverage of everything. Sequence your prompts.

---

## 9. Technique Quick Reference

**When you need:**

→ **Clear creation requirements** = Use detailed context + constraints (Element 3 + 4)
→ **Audience-appropriate output** = Specify audience fully (Element 2)
→ **Evaluation criteria** = Define quality indicators (Element 5)
→ **Multiple options** = Use DECIDE pattern with 3+ alternatives
→ **Realistic practice** = Use SIMULATE pattern with clear persona rules
→ **Improved drafts** = Use IMPROVE pattern with specific focus areas
→ **Verified quality** = Add Audience Simulation Check
→ **Honest assessment** = Add Uncertainty Acknowledgment
→ **Protection from bad advice** = Apply False-Positive Prevention patterns

**Mapping to Coding Technique Equivalents:**

| Non-Coding Need | Coding Equivalent | Technique Code |
|-----------------|-------------------|----------------|
| Audience specification | Context framing | CM-01 |
| Output format | Output templates | OC-01 |
| Quality criteria | Success criteria | ST-01 |
| Multiple approaches | Tree of thoughts | RT-03 |
| Self-verification | Chain of verification | QA-01 |
| Uncertainty | Uncertainty acknowledgment | QA-04 |
| Structured steps | Sequential instructions | ST-02 |
| Evidence-based claims | Evidence-based reasoning | RT-05 |

---

## 10. When You're Stuck

**Problem:** Not sure what domain this request belongs to
**Solution:** Focus on the task type first (CREATE/LEARN/DECIDE/etc.), then apply that pattern with general elements

**Problem:** User's request is too vague
**Solution:** Use the 5 Elements checklist to identify what's missing, then ask clarifying questions

**Problem:** Output is technically correct but "doesn't feel right"
**Solution:** Check tone and audience match. Often the content is fine but the framing is wrong

**Problem:** User wants something in a field you're uncertain about
**Solution:** Use high uncertainty acknowledgment, be explicit about limitations, suggest validation with domain expert

**Problem:** Output is generic/could apply to anyone
**Solution:** Add more specific context about the user's actual situation, constraints, and goals

**Problem:** Hard to tell if output is good
**Solution:** Add explicit quality criteria before generating, then evaluate against them

---

## Quick Start Checklist

Before executing any non-coding prompt:

- [ ] **Task type identified?** (CREATE/LEARN/DECIDE/COMMUNICATE/IMPROVE/SIMULATE)
- [ ] **Audience specified?** (Who, what they know, what they need)
- [ ] **Context provided?** (Purpose, constraints, domain requirements)
- [ ] **Output defined?** (Format, length, tone, structure)
- [ ] **Quality criteria set?** (How to know it's good)
- [ ] **Uncertainty acknowledged?** (What we're confident about vs. not)
- [ ] **False-positive prevention?** (Assumptions stated, caveats included)

**If all checked, execute the prompt.**

---

## Related Resources

| Resource | Purpose |
|----------|---------|
| [AI_AGENT_QUICK_START.md](AI_AGENT_QUICK_START.md) | Coding/technical prompt building |
| [domain-image-generation/IMAGE_GENERATION_GUIDE.md](domain-image-generation/IMAGE_GENERATION_GUIDE.md) | Image generation prompt building (badge buddies, infographics, diagrams) |
| [techniques/MASTER_TECHNIQUE_INDEX.md](techniques/MASTER_TECHNIQUE_INDEX.md) | Complete technique catalog |
| [techniques/USE_CASE_LOOKUP.md](techniques/USE_CASE_LOOKUP.md) | Find techniques by use case |
| [authoring/PROMPT_STRUCTURE_GUIDE.md](authoring/PROMPT_STRUCTURE_GUIDE.md) | Structuring prompts, delimiting injected content, and diagnosing prompts that don't work |
| [PROMPT_QUALITY_STANDARDS.md](PROMPT_QUALITY_STANDARDS.md) | Quality tiers and standards |
| [domain-image-generation/](domain-image-generation/) | 110 image generation prompts |
| [domain-education-teaching/](domain-education-teaching/) | Education-focused prompts |
| [domain-creative-writing/](domain-creative-writing/) | Creative writing prompts |
| [domain-healthcare-clinical/](domain-healthcare-clinical/) | Healthcare/clinical prompts |
| [domain-personal-development/](domain-personal-development/) | Personal development prompts |
| [domain-professional-communication/](domain-professional-communication/) | Professional communication prompts |

---

**Remember:** Non-coding prompts succeed when they match the audience, specify quality criteria, and acknowledge uncertainty. When in doubt:

1. Specify who the audience is
2. Define what success looks like
3. State your assumptions explicitly
4. Ask "would the intended reader find this useful?"

**You're ready! Start building effective non-coding prompts now.**

---

*Document Version: 1.0*
*Created: 2026-01-26*
*Last Updated: 2026-01-26*
