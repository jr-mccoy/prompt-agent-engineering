# Technique Analysis: teams-channel-post-writer

**Resource Type:** Skill
**Category:** Content Creation
**Path:** `skills/content-creation/teams-channel-post-writer/`
**Date Analyzed:** 2025-12-22
**Bundled Resources:** 1 reference (writing-guidelines.md), 1 asset (post-template.md)
**Total Lines:** ~189 lines

## Overview

This skill creates educational Teams channel posts for internal knowledge sharing about Claude Code features, tools, and best practices. It provides templates, writing guidelines, and a structured workflow for producing consistent, actionable technical content.

**Core Purpose:** Transform technical information into educational content that teaches colleagues effective Claude Code usage patterns while connecting to broader engineering principles.

**Complexity Score:** 4/5 (High complexity in content structuring, quality assurance, and pedagogical patterns)

---

## Identified Techniques

### Technique 1: Template-Driven Content Generation
- **Category:** OT (Output Techniques)
- **Maps to existing:** OT-01 (Format Specification with Templates)
- **Pattern:** Provides ready-to-use markdown template with placeholder structure that users fill in while maintaining proven content architecture
- **Example from resource:**
```markdown
## 🎯 [Title]: [Feature/Tool Name]

**New in [Tool Name] ([Date]):** Brief introduction

**What is it?**
[1-2 sentence explanation]

**How to use it - BE EXPLICIT:**
📝 **Normal:** "[Example of typical approach]"
⭐ **Better:** "[Example of improved approach]"
```
- **Effectiveness:** Templates ensure consistency while allowing customization. The 9-section structure (Title → Introduction → What/How/Why → Examples → Options → CTA → Resources) creates scannable, actionable content.

### Technique 2: Comparative Example Pattern (Normal vs Better)
- **Category:** DS (Domain-Specific - Technical Writing)
- **Maps to existing:** NEW - **DS-74: Non-Judgmental Comparison Pattern**
- **Pattern:** Uses "Normal vs Better" instead of "Wrong vs Correct" to show improvements without making readers feel criticized
- **Example from resource:**
```markdown
📝 **Normal:** "[Example of typical approach]"
⭐ **Better:** "[Example of improved approach with explicit instructions]"
```
- **Effectiveness:** Psychologically safe learning environment. Shows evolution rather than failure, encourages adoption without defensiveness.
- **Novel aspect:** Explicit emoji-based labeling (📝 vs ⭐) provides visual distinction while maintaining positive framing.

### Technique 3: Multi-Stage Quality Assurance
- **Category:** QA (Quality Assurance)
- **Maps to existing:** QA-01 (Self-Verification), QA-03 (Checklist Validation)
- **Pattern:** Combines research checklist (pre-writing), quality checklist (post-writing), and workflow checkpoints
- **Example from resource:**
```markdown
**Research checklist:**
- [ ] Found official release date/version number
- [ ] Verified feature behavior through testing or documentation
- [ ] Identified authoritative sources to link to
- [ ] Understood the underlying principle or best practice

**Quality Checklist:**
- [ ] Includes specific release date or timing
- [ ] Explains the "why" with principles or best practices
- [ ] Provides 3+ concrete, realistic examples
- [ ] Uses "Normal/Better" pattern (not "Wrong/Correct")
- [ ] Includes clear call-to-action
- [ ] Links to additional learning resources
```
- **Effectiveness:** Catches errors at multiple stages: before writing (research), during writing (guidelines), after writing (quality check). Prevents common mistakes like missing dates, insufficient examples, or judgmental tone.

### Technique 4: Principle-Connection Scaffolding
- **Category:** DS (Domain-Specific - Educational Content)
- **Maps to existing:** NEW - **DS-75: Feature-to-Principle Bridging**
- **Pattern:** Explicitly requires connecting features to broader best practices and underlying principles
- **Example from resource:**
```markdown
### Connect to Principles
Don't just describe features—explain the underlying best practices.
For example, connect the Explore agent to "context offloading"
principles in context engineering.

**Why use it? ([Key Principle/Best Practice])**
[Explanation of the underlying principle or best practice]
```
- **Effectiveness:** Transforms surface-level feature descriptions into deeper learning. Users understand not just "what" but "why" and "when," enabling better decision-making.
- **Novel aspect:** Mandates principle identification as a planning step, not an optional enhancement.

### Technique 5: Workflow-Driven Content Creation
- **Category:** DS (Domain-Specific - Content Production)
- **Maps to existing:** DS-04 (Workflow Specification)
- **Pattern:** 5-stage workflow: Understand → Plan → Draft → Review → Share, each with specific deliverables and checklists
- **Example from resource:**
```markdown
## Workflow

### 1. Understand the Topic
[Research checklist with 4 items]

### 2. Plan the Content
[4 planning questions: Hook, Core principle, Examples, Call-to-action]

### 3. Draft Using the Template
[9-section template structure]

### 4. Apply Writing Guidelines
[Quality checklist review]

### 5. Save and Share
[Distribution instructions]
```
- **Effectiveness:** Prevents "blank page syndrome" by breaking large task into manageable steps. Each stage has clear entry/exit criteria.

### Technique 6: Tone and Style Codification
- **Category:** ST (Structural Techniques)
- **Maps to existing:** ST-02 (Persona Assignment) - but more nuanced
- **Pattern:** Explicit tone guidelines with specific do/don't patterns beyond simple persona
- **Example from resource:**
```markdown
## Tone and Style

- **Educational and helpful**: Focus on teaching concepts, not just announcing features
- **Professional but approachable**: Conversational without being too casual
- **Action-oriented**: Include concrete examples and calls-to-action
- **Concise**: Keep posts scannable - use short paragraphs and bullet points

Uses "Normal/Better" pattern (not "Wrong/Correct")
```
- **Effectiveness:** Provides nuanced guidance beyond "act professional" - specifies balance points (professional but approachable, educational not promotional) and forbidden patterns (judgmental language).

### Technique 7: Concrete Example Quota
- **Category:** DS (Domain-Specific - Technical Writing)
- **Maps to existing:** NEW - **DS-76: Example Quantity Specification**
- **Pattern:** Mandates minimum number of concrete, realistic examples (3+) that users can adapt
- **Example from resource:**
```markdown
**Example prompts:**

"[Example 1]"
"[Example 2]"
"[Example 3]"

Quality checklist:
- [ ] Provides 3+ concrete, realistic examples
```
- **Effectiveness:** Prevents vague explanations. Forces author to think through multiple use cases, which often reveals gaps in understanding. Gives readers variety to find relevant patterns.
- **Novel aspect:** Specifies both quantity (3+) AND quality (concrete, realistic, adaptable).

### Technique 8: Call-to-Action Mandatory Close
- **Category:** IT (Interaction Techniques)
- **Maps to existing:** IT-06 (Guided Discovery)
- **Pattern:** Every post must end with actionable next step
- **Example from resource:**
```markdown
Try it next time you [call to action]!

Quality checklist:
- [ ] Includes clear call-to-action
```
- **Effectiveness:** Converts passive reading into active learning. Users leave with concrete task, increasing engagement and retention.

### Technique 9: Verification-First Research
- **Category:** QA (Quality Assurance)
- **Maps to existing:** NEW - **QA-17: Authoritative Source Verification**
- **Pattern:** Requires finding and linking to authoritative sources before drafting
- **Example from resource:**
```markdown
## Research Requirements

Before writing any post:
1. **Verify release dates**: Use official documentation or changelog
2. **Test the feature**: Ensure examples work as described
3. **Find authoritative sources**: Link to official docs or reputable technical blogs
4. **Check for updates**: Ensure information is current
```
- **Effectiveness:** Prevents misinformation at source. Builds trust through cited, tested information.
- **Novel aspect:** Makes research a prerequisite, not a post-writing task.

### Technique 10: Format Convention Codification
- **Category:** OT (Output Techniques)
- **Maps to existing:** OT-01 (Format Specification)
- **Pattern:** Explicit formatting standards for emojis, bold text, code blocks, lists, comparisons
- **Example from resource:**
```markdown
## Formatting Standards

- **Emojis**: Use sparingly and only in titles (🔍 🎯 💡 ⚡)
- **Bold**: Use for emphasis on key terms and section headers
- **Code blocks**: Use for example prompts (triple backticks or quotes)
- **Lists**: Use bullets for benefits/features, numbers for sequential steps
- **Comparisons**: Use 📝 for "Normal" and ⭐ for "Better"
```
- **Effectiveness:** Ensures visual consistency across authors. Readers develop pattern recognition for content types (bullets = benefits, numbers = steps).

---

## Novel Patterns (Not in MASTER_TECHNIQUE_INDEX)

### Pattern 1: Non-Judgmental Comparison Pattern (DS-74)
- **Description:** Show improvements using "Normal vs Better" instead of "Wrong vs Correct" with visual emoji distinction
- **Implementation:**
  - Label baseline approach as "Normal" (📝)
  - Label improved approach as "Better" (⭐)
  - Avoid judgmental language like "incorrect," "bad," "wrong"
  - Frame as evolution/improvement, not correction/failure
- **Use case:** Technical documentation, educational content, code reviews, best practice guides
- **Example:**
```markdown
📝 **Normal:** "Search for the function definition"
⭐ **Better:** "Use Glob to find *.py files with 'def calculate_' pattern"
```
- **Proposed category:** DS (Domain-Specific - Technical Writing)
- **Proposed code:** DS-74

**Why this is novel:** While existing techniques cover positive framing and examples, none explicitly codify the psychological safety aspect of comparative examples. This pattern recognizes that HOW you present alternatives affects adoption rates.

### Pattern 2: Feature-to-Principle Bridging (DS-75)
- **Description:** Explicitly require connecting specific features to broader engineering principles or best practices
- **Implementation:**
  - Planning phase includes "Core principle" question
  - Template mandates "Why use it? ([Key Principle/Best Practice])" section
  - Guidelines state "Don't just describe features—explain the underlying best practices"
- **Use case:** Feature documentation, educational content, technical onboarding, architectural decision records
- **Example:**
```markdown
**Why use it? (Context Engineering)**

The Explore agent implements "context offloading" - reducing cognitive load by
delegating codebase navigation to a specialized agent. This allows you to focus
on high-level reasoning while the agent handles mechanical search tasks.

- **Reduces context switching**: Stay in design mode while agent searches
- **Leverages specialization**: Agent optimized for rapid exploration
- **Improves token efficiency**: Explore agent uses cheaper models for search
- **Creates reusable knowledge**: Agent findings inform future queries
```
- **Proposed category:** DS (Domain-Specific - Educational Content)
- **Proposed code:** DS-75

**Why this is novel:** Existing techniques don't mandate principle identification as a structural requirement. This elevates feature documentation to conceptual learning.

### Pattern 3: Example Quantity Specification (DS-76)
- **Description:** Mandate minimum number of concrete, realistic, adaptable examples (3+) rather than leaving quantity open-ended
- **Implementation:**
  - Template includes 3 example slots
  - Quality checklist verifies "3+ concrete, realistic examples"
  - Guidelines specify "realistic use cases from actual development workflows"
- **Use case:** API documentation, prompt engineering guides, code tutorials, recipe documentation
- **Example:**
```markdown
**Example prompts:**

1. "Find all React components that handle user authentication"
2. "Show me database migration files from the last sprint"
3. "List API endpoints that aren't covered by integration tests"

Quality checklist:
✓ 3+ examples provided
✓ Each example is concrete (specific, not abstract)
✓ Examples cover different use cases
✓ Users can adapt examples to their context
```
- **Proposed category:** DS (Domain-Specific - Technical Writing)
- **Proposed code:** DS-76

**Why this is novel:** While many techniques recommend examples, quantifying the minimum (3+) and specifying quality criteria (concrete, realistic, adaptable) creates measurable standard.

### Pattern 4: Authoritative Source Verification (QA-17)
- **Description:** Require finding and citing authoritative sources BEFORE drafting content, not as post-writing enhancement
- **Implementation:**
  - Research phase checklist includes "Identified authoritative sources to link to"
  - "Research Requirements" section mandates verification before writing
  - Quality checklist verifies "Links to additional learning resources"
  - All facts must be "verified against official sources"
- **Use case:** Technical documentation, educational content, API references, security advisories
- **Example:**
```markdown
## Research Requirements

Before writing any post:
1. **Verify release dates**: Use official documentation or changelog
   ✓ Found: Claude Code 2.1 changelog (Dec 15, 2024)
   Link: https://docs.anthropic.com/claude-code/changelog

2. **Test the feature**: Ensure examples work as described
   ✓ Tested: Explore agent with "quick", "medium", "thorough" levels
   ✓ Confirmed: thorough level searches multiple naming conventions

3. **Find authoritative sources**: Link to official docs
   ✓ Found: Explore agent documentation
   Link: https://docs.anthropic.com/claude-code/agents/explore

4. **Check for updates**: Ensure information is current
   ✓ Verified: No updates since Dec 15 release
```
- **Proposed category:** QA (Quality Assurance)
- **Proposed code:** QA-17

**Why this is novel:** Existing QA techniques focus on post-generation verification. This makes source verification a prerequisite, preventing misinformation at the source rather than catching it later.

---

## Multi-Technique Combinations

### Content Creation Pipeline
This skill combines multiple techniques into a complete content production workflow:

1. **Planning Phase:**
   - DS-75 (Feature-to-Principle Bridging): Identify core principle
   - QA-17 (Authoritative Source Verification): Research and verify sources
   - DS-04 (Workflow Specification): Follow structured planning

2. **Drafting Phase:**
   - OT-01 (Template-Driven Output): Use post template
   - DS-76 (Example Quantity Specification): Create 3+ examples
   - DS-74 (Non-Judgmental Comparisons): Show Normal vs Better

3. **Review Phase:**
   - QA-01 (Self-Verification): Apply quality checklist
   - ST-02 (Tone Guidance): Verify tone consistency
   - OT-01 (Format Verification): Check formatting standards

4. **Distribution Phase:**
   - IT-06 (Call-to-Action): End with actionable next step
   - QA-17 (Source Linking): Provide learning resources

**Effectiveness:** The combination creates a systematic approach to educational content creation that ensures quality, consistency, and actionability. Each phase builds on previous work, preventing rework.

---

## Integration Notes

### For MASTER_TECHNIQUE_INDEX.md
Recommend adding 4 new techniques:
1. **DS-74: Non-Judgmental Comparison Pattern** - High priority for any comparative documentation
2. **DS-75: Feature-to-Principle Bridging** - Medium priority for educational content
3. **DS-76: Example Quantity Specification** - High priority for API docs and tutorials
4. **QA-17: Authoritative Source Verification** - High priority for accuracy-critical content

### For USE_CASE_LOOKUP.md
Add to "Documentation & Writing" use case:
- DS-74: When showing code improvements or alternatives
- DS-75: When documenting features or architectural decisions
- DS-76: When creating tutorials, guides, or API documentation
- QA-17: When creating any technical documentation requiring accuracy

### For AI_AGENT_QUICK_START.md
Reference this skill as example of:
- Template-driven content generation (progressive disclosure)
- Multi-stage quality assurance in content workflows
- Psychological safety in technical writing (Normal vs Better)

### Cross-References
- **Similar to:** ppt-creator (multi-stage quality gates), api-design-principles (checklist-driven design)
- **Complements:** prompt-engineering-patterns (can use this skill to document prompt patterns)
- **Extends:** Standard technical writing practices with quantified quality standards

---

## Statistical Summary

- **Novel Techniques Identified:** 4
- **Existing Techniques Referenced:** 6
- **Quality Checkpoints:** 2 (research checklist + quality checklist)
- **Workflow Stages:** 5 (Understand → Plan → Draft → Review → Share)
- **Template Sections:** 9 (Title → What → How → Why → Examples → Options → CTA → Learn More)
- **Minimum Example Count:** 3+
- **Bundled Knowledge:** 189 lines (SKILL.md + guidelines + template)

---

## Key Insights

1. **Psychological Safety in Documentation:** The "Normal vs Better" pattern acknowledges that how you present information affects adoption. Technical accuracy matters less than perceived criticism.

2. **Principle-First Teaching:** Connecting features to principles transforms documentation from reference material to learning resource. Users develop mental models, not just memorize commands.

3. **Quantified Quality Standards:** Specifying "3+ examples" is more actionable than "provide examples." Measurable standards enable consistency across authors.

4. **Research as Prerequisite:** Making source verification a pre-writing requirement prevents misinformation at creation rather than catching it during review.

5. **Template + Checklist Pattern:** Templates provide structure, checklists ensure completeness. Together, they create consistent quality without rigid constraints.
