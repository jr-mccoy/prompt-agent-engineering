# Technique Analysis: skills-search

**Resource Type:** Skill
**Path:** `claude-code-resources/skills/developer-tools/skills-search/`
**Date Analyzed:** 2025-12-22
**Bundled Resources:** 177 lines (SKILL.md only, no scripts/references/assets)
**Complexity:** 3/5 (CLI wrapper with workflow guidance and popular skills directory)

## Overview

The `skills-search` skill provides command reference and workflow guidance for discovering and managing Claude Code skills using the CCPM (Claude Code Plugin Manager) CLI. It demonstrates CLI command documentation patterns, workflow orchestration for tool discovery, and popular options highlighting.

**Key Innovation:** Meta-skill pattern - a skill that helps discover and install other skills, creating a self-bootstrapping ecosystem.

## Identified Techniques

### Technique 1: CLI Command Reference Table
- **Category:** OT (Output Techniques)
- **Pattern:** Structured command documentation with syntax, options, and examples
- **Example from resource:**
```markdown
### Search Skills
```bash
ccpm search <query> [options]

Options:
  --limit <n>    Maximum results (default: 10)
  --json         Output as JSON
```

**Examples:**
```bash
ccpm search pdf              # Find PDF-related skills
ccpm search "code review"    # Find code review skills
```
- **Maps to existing:** Extends **OT-02 Format Specification** → **OT-18 CLI Command Reference Table**
- **Effectiveness:** Clear command syntax + inline comments explain purpose

### Technique 2: Numbered Workflow for Tool Discovery
- **Category:** DS (Domain-Specific - Tool Discovery)
- **Pattern:** 5-step workflow for finding, evaluating, and installing tools
- **Example from resource:**
```markdown
## Workflow: Finding and Installing Skills

1. **Search** for relevant skills: ccpm search <keywords>
2. **Review** search results - check download counts and descriptions
3. **Get details** on promising skills: ccpm info <skill-name>
4. **Install** chosen skill: ccpm install <skill-name>
5. **Inform user** to restart Claude Code
```
- **Maps to existing:** NEW - **DS-119 Numbered Workflow for Tool Discovery**
- **Effectiveness:** Structured approach to exploring unfamiliar tools; reduces trial-and-error

### Technique 3: Popular Options Directory
- **Category:** IT (Interaction Techniques)
- **Pattern:** Curated table of commonly-used options with use cases
- **Example from resource:**
```markdown
## Popular Skills

| Skill | Purpose |
|-------|---------|
| `skill-creator` | Create new Claude Code skills |
| `pdf-processor` | PDF manipulation and analysis |
| `cloudflare-troubleshooting` | Debug Cloudflare issues |
```
- **Maps to existing:** NEW - **IT-45 Popular Options Directory**
- **Effectiveness:** Fast-track common needs; users start with battle-tested options

### Technique 4: Restart Requirement Warning
- **Category:** IT (Interaction Techniques)
- **Pattern:** Explicit warning about post-installation action required for changes to take effect
- **Example from resource:**
```markdown
**Important:** After installing a skill, Claude Code must be restarted for the skill to become available.
```
- **Maps to existing:** NEW - **IT-46 Restart Requirement Warning**
- **Effectiveness:** Prevents user confusion ("I installed it but it's not working"); sets clear expectations

### Technique 5: Inline Command Comments
- **Category:** OT (Output Techniques)
- **Pattern:** Add explanatory comments after bash commands using `#`
- **Example from resource:**
```bash
ccpm search pdf              # Find PDF-related skills
ccpm search "code review"    # Find code review skills
ccpm install cloudflare-troubleshooting       # Install troubleshooting skill
```
- **Maps to existing:** NEW - **OT-19 Inline Command Comments**
- **Effectiveness:** Self-documenting examples; users understand command purpose without separate description

### Technique 6: Meta-Skill Pattern
- **Category:** AG (Agentic - Skill Architecture)
- **Pattern:** A skill that facilitates discovery and installation of other skills
- **Example from resource:**
```markdown
name: skills-search
description: Search, discover, and manage Claude Code skills from CCPM registry
```
- **Maps to existing:** NEW - **AG-24 Meta-Skill Pattern**
- **Effectiveness:** Bootstrap ecosystem growth; users can find capabilities without external documentation

## Novel Patterns (Not in MASTER_TECHNIQUE_INDEX)

### Pattern 1: CLI Command Reference Table (OT-18)
- **Description:** Structured command documentation with syntax, options, and examples
- **Implementation:**
  - Section per command
  - Syntax block: `command <required> [optional]`
  - Options table with defaults
  - 2-3 examples with inline comments
- **Use case:** CLI tool documentation, command wrappers, tool skills
- **Example:** Docker commands, Git workflows, npm scripts
- **Proposed category:** OT (Output Techniques)
- **Proposed code:** OT-18

### Pattern 2: Numbered Workflow for Tool Discovery (DS-119)
- **Description:** Structured 5-step workflow for finding, evaluating, and installing tools
- **Implementation:**
  - Step 1: Search (with keywords)
  - Step 2: Review results (evaluation criteria)
  - Step 3: Get details (deep dive)
  - Step 4: Install (action)
  - Step 5: Post-install instructions
- **Use case:** Package managers, plugin ecosystems, tool marketplaces
- **Example:** VSCode extensions, npm packages, WordPress plugins
- **Proposed category:** DS (Domain-Specific - Tool Discovery)
- **Proposed code:** DS-119

### Pattern 3: Popular Options Directory (IT-45)
- **Description:** Curated table of commonly-used options with use cases
- **Implementation:**
  - Section: "Popular [Items]"
  - Table: Name | Purpose
  - 5-10 battle-tested options
  - Focus on high-download or high-value items
- **Use case:** Any ecosystem with many options (tools, libraries, templates)
- **Example:** Popular npm packages, Common design patterns, Frequently-used APIs
- **Proposed category:** IT (Interaction Techniques)
- **Proposed code:** IT-45

### Pattern 4: Restart Requirement Warning (IT-46)
- **Description:** Explicit warning about post-installation action required
- **Implementation:**
  - Place immediately after install instructions
  - Format: "**Important:** After [action], [system] must be [action] for changes to take effect"
  - Use bold or callout formatting
- **Use case:** Tools with hot-reload limitations, system configuration changes
- **Example:** Editor plugins, environment variables, daemon configuration
- **Proposed category:** IT (Interaction Techniques)
- **Proposed code:** IT-46

### Pattern 5: Inline Command Comments (OT-19)
- **Description:** Explanatory comments after bash commands using `#`
- **Implementation:**
  - Command followed by whitespace, then `# Comment`
  - Comments explain what command does or when to use it
  - Keeps examples self-documenting
- **Use case:** Code examples, command tutorials, shell script documentation
- **Example:** Installation guides, CLI tutorials, automation scripts
- **Proposed category:** OT (Output Techniques)
- **Proposed code:** OT-19

### Pattern 6: Meta-Skill Pattern (AG-24)
- **Description:** A skill that facilitates discovery and installation of other skills
- **Implementation:**
  - Wraps package manager or registry CLI
  - Provides search/install/list workflows
  - Includes popular items directory
  - Guides users through discovery process
- **Use case:** Plugin ecosystems, package management, tool discovery
- **Example:** VSCode extension marketplace, npm registry, Homebrew formulae
- **Proposed category:** AG (Agentic - Skill Architecture)
- **Proposed code:** AG-24

## Multi-Technique Combinations

The `skills-search` skill demonstrates effective combination of techniques:

1. **CLI Command Reference + Inline Comments:**
   - CLI Command Reference provides structure
   - Inline Command Comments make examples self-explanatory
   - Result: No separate description needed for examples

2. **Numbered Workflow + Popular Directory:**
   - Numbered Workflow guides discovery process
   - Popular Options Directory fast-tracks common needs
   - Result: Efficient exploration for both novice and experienced users

3. **Meta-Skill + Restart Warning:**
   - Meta-Skill enables skill discovery
   - Restart Requirement Warning prevents post-install confusion
   - Result: Smooth user experience for ecosystem growth

## Integration Notes

### For MASTER_TECHNIQUE_INDEX.md:
1. **Add 6 new techniques:**
   - OT-18: CLI Command Reference Table
   - DS-119: Numbered Workflow for Tool Discovery
   - IT-45: Popular Options Directory
   - IT-46: Restart Requirement Warning
   - OT-19: Inline Command Comments
   - AG-24: Meta-Skill Pattern

2. **Create new subcategories:**
   - "Tool Discovery" (DS-119)
   - "Skill Architecture" (AG-24)

3. **Cross-reference existing techniques:**
   - OT-02 (Format Specification) → OT-18 extends to CLI commands
   - OT-19 complements existing code example techniques

### For USE_CASE_LOOKUP.md:
- Add "Tool/Plugin Discovery" use case
- Recommended techniques: DS-119, IT-45, OT-18, OT-19, IT-46

### For AI_AGENT_QUICK_START.md:
- Add example in Section 5: "CLI wrapper skills with command reference"
- Demonstrate Meta-Skill Pattern for ecosystem bootstrapping

## Summary

**Complexity Rating:** 3/5

The `skills-search` skill is a **meta-skill for Claude Code ecosystem discovery** that wraps the CCPM CLI with workflow guidance and popular options curation.

**Key Strengths:**
1. **Self-documenting examples:** Inline comments make examples clear without separate descriptions
2. **Structured discovery:** 5-step workflow reduces trial-and-error
3. **Fast-track common needs:** Popular skills directory accelerates onboarding
4. **Meta pattern:** Skill that helps discover other skills, bootstrapping ecosystem growth

**Novel Contributions:**
- Meta-Skill Pattern (AG-24): Universal pattern for tool/plugin discovery systems
- Numbered Workflow for Tool Discovery (DS-119): Structured approach to exploring unfamiliar tools
- Popular Options Directory (IT-45): Curated fast-track for common use cases
- Inline Command Comments (OT-19): Self-documenting code examples

**Recommended Integration Priority:** MEDIUM
- AG-24 (Meta-Skill Pattern): Important for plugin ecosystems
- DS-119 (Numbered Workflow for Tool Discovery): Standard for package management
- OT-19 (Inline Command Comments): Universal pattern for code examples

**Lines of Bundled Knowledge:** 177 lines
- SKILL.md: 177 lines (command reference + workflow + popular skills)

**Production Readiness:** 4/5 - Comprehensive CLI documentation, clear workflow, troubleshooting section, and restart warning. Missing: version compatibility matrix, rollback instructions.

**Architecture Note:** This is a **meta-skill** - a skill about skills. It demonstrates the Claude Code ecosystem's self-bootstrapping capability where skills can help users discover and install other skills.
