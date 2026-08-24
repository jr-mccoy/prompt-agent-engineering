---
name: teams-channel-post-writer
description: Creates educational Teams channel posts for internal knowledge sharing about Claude Code features, tools, and best practices. Applies when writing posts, announcements, or documentation to teach colleagues effective Claude Code usage, announce new features, share productivity tips, or document lessons learned. Provides templates, writing guidelines, and structured approaches emphasizing concrete examples, underlying principles, and connections to best practices like context engineering. Activates for content involving Teams posts, channel announcements, feature documentation, or tip sharing.
metadata:
  tags:
    - teams-posts
    - internal-communication
    - knowledge-sharing
    - technical-writing
    - claude-code
  updated: "2026-04-11"
---
# Teams Channel Post Writer

## Overview

Create well-structured, educational Teams channel posts for internal knowledge sharing about Claude Code features and best practices. This skill provides templates, writing guidelines, and a structured workflow to produce consistent, actionable content that helps colleagues learn effective Claude Code usage.

## When to Use This Skill

This skill activates when creating Teams channel posts to:
- Announce and explain new Claude Code features
- Share Claude Code tips and best practices
- Teach effective prompting patterns and workflows
- Connect features to broader engineering principles (e.g., context engineering)
- Document lessons learned from using Claude Code

## Workflow

### 1. Understand the Topic

Gather information about what to write about:
- Research the feature/topic thoroughly using official documentation
- Verify release dates and version numbers from changelogs
- Identify the core benefit or principle the post should teach
- Collect concrete examples from real usage

**Research checklist:**
- [ ] Found official release date/version number
- [ ] Verified feature behavior through testing or documentation
- [ ] Identified authoritative sources to link to
- [ ] Understood the underlying principle or best practice

### 2. Plan the Content

Based on the writing guidelines in `references/writing-guidelines.md`, plan:
- **Hook**: What's new or important about this topic?
- **Core principle**: What best practice does this illustrate?
- **Examples**: What concrete prompts or workflows demonstrate this?
- **Call-to-action**: What should readers try next?

### 3. Draft Using the Template

Start with the template in `assets/post-template.md` and fill in:

1. **Title**: Use an emoji and clear description
2. **Introduction**: Include release date and brief context
3. **What it is**: 1-2 sentence explanation
4. **How to use it**: Show "Normal vs Better" pattern with explicit instructions
5. **Why use it**: Explain the underlying principle with 4 key benefits
6. **Examples**: Provide 3+ realistic, concrete prompts
7. **Options/Settings**: List key configurations or parameters
8. **Call-to-action**: End with actionable next step
9. **Learn more**: Link to authoritative resources

### 4. Apply Writing Guidelines

Review the draft against the quality checklist in `references/writing-guidelines.md`:
- Educational and helpful tone
- "Normal/Better" pattern (not "Wrong/Correct")
- Concrete, realistic examples
- Explains the "why" with principles
- Clear structure with bullets and formatting
- Verified facts and dates

### 5. Save and Share

Save the final post to your team's documentation location with a descriptive filename like "Claude Code Tips.md" or "[Topic Name].md"

## Key Principles

### Show, Don't Just Tell
Always include concrete examples users can adapt. Use "Normal vs Better" comparisons to demonstrate improvements without making readers feel criticized.

### Connect to Principles
Don't just describe features—explain the underlying best practices. For example, connect the Explore agent to "context offloading" principles in context engineering.

### Make it Actionable
Be explicit about invocation patterns. Users should be able to copy/paste examples and immediately use them.

### Verify Everything
Always research release dates, verify feature behavior, and link to authoritative sources. Accuracy builds trust.

## Resources

### references/writing-guidelines.md
Comprehensive writing guidelines including:
- Tone and style standards
- Structure patterns for different post types
- Formatting conventions
- Research requirements
- Quality checklist

Reference this file for detailed guidance on tone, structure, and quality standards.

### assets/post-template.md
Ready-to-use markdown template with placeholder structure for:
- Title and introduction
- Feature explanation
- Usage examples
- Benefits and principles
- Options and settings
- Call-to-action and resources

Copy this template as a starting point for new posts, then customize the content while maintaining the proven structure.

---

## Core Concepts

### Internal Developer Advocacy

Teams channel posts serve as internal developer advocacy -- the practice of championing tools, techniques, and best practices within your organization. Unlike external developer relations, internal advocacy focuses on:

- **Reducing friction** - Help colleagues adopt tools they already have access to
- **Building shared vocabulary** - Establish common terminology around AI-assisted development
- **Creating pull (not push)** - Make content so useful that people seek it out
- **Compounding knowledge** - Each post builds on previous ones, creating a knowledge base

### Knowledge Democratization

The goal is not just sharing information but making expertise accessible to everyone regardless of experience level. A junior developer reading your post about Claude Code's Explore agent should gain the same confidence as someone who discovered the feature through experimentation.

Principles of effective knowledge democratization:
1. **No assumed context** - Define terms, link to prerequisites
2. **Multiple entry points** - Some readers want the quick tip, others want the deep dive
3. **Concrete over abstract** - Always lead with a real example, then explain the principle
4. **Invitation, not instruction** - "Try this" works better than "You should do this"

---

## Post Type Taxonomy

### Feature Announcement

**When:** A new Claude Code feature ships or an existing one gets a significant update.

**Structure:**
```
[Emoji] New: [Feature Name] in Claude Code [version]
|
+-- What changed (1-2 sentences)
+-- Why it matters (connect to daily workflow)
+-- How to use it (Normal vs Better example)
+-- Try it now (specific prompt to copy/paste)
+-- Learn more (link to official docs)
```

**Length:** 150-250 words. Concise -- people scan announcements.

### Tip of the Week

**When:** You discover a workflow improvement, shortcut, or non-obvious capability.

**Structure:**
```
[Emoji] Tip: [Concise benefit statement]
|
+-- The scenario (relatable problem)
+-- The tip (concrete solution with example)
+-- Why it works (underlying principle)
+-- Bonus variation (alternative use case)
```

**Length:** 100-200 words. The tightest format -- one idea, well delivered.

### Deep Dive

**When:** A topic deserves thorough explanation with multiple examples and nuance.

**Structure:**
```
[Emoji] Deep Dive: [Topic]
|
+-- Introduction (why this matters)
+-- Background/Context (what you need to know first)
+-- Core technique (detailed walkthrough with examples)
+-- Advanced variations (2-3 additional patterns)
+-- Common mistakes (what to avoid)
+-- Resources (links for further exploration)
```

**Length:** 400-800 words. Use formatting heavily -- this is a reference people will revisit.

### FAQ / Myth Busting

**When:** You notice recurring questions or misconceptions in the team.

**Structure:**
```
[Emoji] FAQ: [Topic] - What You Might Be Getting Wrong
|
+-- The common belief (what people assume)
+-- The reality (what actually happens, with evidence)
+-- The better approach (corrected workflow)
+-- Quick reference (summary table or checklist)
```

**Length:** 200-400 words. Direct and factual -- this corrects misunderstandings.

---

## Engagement Optimization

### Formatting for Teams

Microsoft Teams has specific rendering behaviors that affect readability:

| Element | Teams Behavior | Best Practice |
|---------|---------------|---------------|
| Code blocks | Monospace, gray background | Use for commands, prompts, and output |
| Bold text | Renders well, stands out | Use for key terms and section headers |
| Bullet lists | Renders well | Preferred over numbered lists for scanability |
| Numbered lists | Renders well | Use for sequential steps only |
| Tables | Basic rendering, no sorting | Keep to 3-5 columns maximum |
| Links | Blue, clickable | Use descriptive text, not raw URLs |
| Emojis | Full support | Use one emoji per post title, sparingly in body |
| Images | Inline rendering | Use sparingly -- most content should be text |
| Line breaks | Double-enter for paragraph | Use generously to avoid walls of text |

### Threading Strategies

- **Main post**: Self-contained, complete message. Readers should not need to read replies.
- **First reply (self-thread)**: Add supplementary context, links, or "for the curious" deep dives
- **Encourage replies**: End with a question -- "What's your favorite use case for X?"
- **Pin important posts**: Ask channel admins to pin reference posts (deep dives, FAQs)

### Timing and Frequency

| Cadence | Post Type | Rationale |
|---------|-----------|-----------|
| Weekly | Tip of the Week | Predictable cadence builds habit |
| As-needed | Feature Announcement | Timeliness matters more than schedule |
| Biweekly | Deep Dive | Gives time for research and quality |
| Monthly | FAQ / Myth Busting | Collects enough questions to address |

Best posting times for engagement:
- **Tuesday-Thursday, 9-10 AM** local time for the majority of your team
- Avoid Monday mornings (inbox overload) and Friday afternoons (checked out)

---

## Metrics and Feedback Loops

### Measuring Post Effectiveness

Track these signals to understand what resonates:

| Signal | How to Measure | What It Means |
|--------|---------------|---------------|
| Reactions (likes, hearts) | Teams reaction count | Surface-level engagement |
| Thread replies | Reply count and quality | Deeper engagement and discussion |
| Questions in replies | Monitor for "how do I..." responses | Content gaps to address in follow-ups |
| Direct messages | People reaching out privately | Strong interest, possibly sensitive questions |
| Adoption metrics | Tool usage dashboards (if available) | Actual behavior change |
| Repeat references | People linking to your post in other threads | Post became a reference resource |

### Feedback Loop Process

```
Write Post -> Publish -> Observe Reactions -> Collect Questions
     ^                                           |
     |                                           v
     +---- Refine Approach <-- Analyze Patterns --+
```

1. **After each post**: Note reaction count and any questions raised
2. **Weekly**: Review which post types get the most engagement
3. **Monthly**: Adjust content calendar based on patterns
4. **Quarterly**: Survey the team -- "What topics would you like covered?"

### Signs Your Posts Are Working

- Colleagues reference your posts in code reviews ("as mentioned in the Claude Code tips channel...")
- People tag you when they discover something related
- New team members are pointed to your posts during onboarding
- You get requests for specific topics

---

## Common Pitfalls

| Pitfall | Symptom | Solution |
|---------|---------|----------|
| Too much jargon | Low engagement, no questions asked | Define terms inline; write for the newest team member |
| Wall of text | People react but clearly did not read | Use headers, bullets, bold, and whitespace aggressively |
| No concrete examples | Replies asking "can you show an example?" | Always include at least one copy-pasteable prompt or command |
| Wrong/Better framing | Readers feel criticized for current approach | Use "Normal vs Better" not "Wrong vs Right" |
| Unverified information | Someone corrects you in replies | Research dates, versions, and behavior before posting |
| Posting too frequently | Engagement drops, people mute the channel | Quality over quantity; 1-2 posts per week maximum |
| No call to action | Post gets reactions but no behavior change | End every post with a specific thing to try |
| Ignoring replies | Thread dies, future engagement drops | Respond to every reply within 24 hours |

---

## Advanced: Series Planning and Content Calendars

### Planning a Post Series

A series of related posts builds expertise progressively and creates anticipation:

```markdown
## Series: "Claude Code Power Patterns" (6-week series)

Week 1: Context Engineering Fundamentals
  -> What is context engineering? Why does it matter?
  -> Example: CLAUDE.md as persistent context

Week 2: The Explore Agent
  -> Using /explore for codebase discovery
  -> Normal vs Better: research before implementation

Week 3: Multi-File Editing Patterns
  -> Techniques for coherent cross-file changes
  -> Example: Refactoring an API endpoint end-to-end

Week 4: Custom Slash Commands
  -> Building project-specific workflows
  -> Example: /review-pr command for your team

Week 5: Skills and Progressive Disclosure
  -> Loading domain knowledge on demand
  -> Example: Building a skill for your team's stack

Week 6: Putting It All Together
  -> Combining patterns for complex tasks
  -> Recap and reader Q&A
```

### Content Calendar Template

```markdown
## Q2 2026 Content Calendar

| Week | Date | Type | Topic | Status |
|------|------|------|-------|--------|
| 14 | Apr 7 | Tip | Using /compact effectively | Published |
| 14 | Apr 10 | Announcement | Claude Code v2.3 features | Published |
| 15 | Apr 14 | Tip | Markdown formatting in prompts | Draft |
| 15 | Apr 17 | Deep Dive | Context engineering series pt. 1 | Planned |
| 16 | Apr 21 | Tip | Git workflow with Claude Code | Planned |
| 16 | Apr 24 | FAQ | "Does Claude Code read my files?" | Planned |
```

### Cross-Referencing Between Posts

Build a knowledge network by linking related posts:

- **Forward references**: "Next week, we will dive deeper into X"
- **Back references**: "As we covered in [previous post link], the key principle is..."
- **See also**: "Related: [link to complementary post]"
- **Index post**: Periodically publish a "table of contents" post linking all previous tips
