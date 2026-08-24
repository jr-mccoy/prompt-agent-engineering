# Technique Analysis: ui-designer

**Resource Type:** Skill
**Path:** `claude-code-resources/skills/web-development/ui-designer/`
**Date Analyzed:** 2025-12-22
**Bundled Resources:** 477 lines (3 assets: design-system.md, app-overview-generator.md, vibe-design-template.md)
**Complexity:** 5/5 (Multi-stage workflow with template composition and subagent orchestration)

## Overview

The `ui-designer` skill provides a systematic workflow for extracting design systems from reference UI images and generating implementation-ready UI design prompts. It demonstrates sophisticated template composition, multi-stage orchestration with subagents, and structured intermediate output preservation.

**Key Innovation:** Multi-stage design system extraction workflow using template substitution (`{项目设计指南}` + `{项目MVP PRD}`) to compose final implementation prompts from intermediate artifacts.

## Identified Techniques

### Technique 1: Multi-Stage Workflow with Intermediate Outputs
- **Category:** DS (Domain-Specific - Design Workflows)
- **Pattern:** Sequential stages producing reusable intermediate artifacts
- **Example from resource:**
```markdown
Step 1: Gather Inputs (images + project idea)
Step 2: Extract Design System → save to documents/designs/
Step 3: Generate MVP PRD → save as variable
Step 4: Compose Final Prompt (design system + PRD) → save to documents/ux-design/
Step 5: Verify Environment
Step 6: Implement UI
```
- **Maps to existing:** NEW - **DS-115 Multi-Stage Workflow with Intermediate Outputs**
- **Effectiveness:** Reusable artifacts enable iteration; users can modify design system without regenerating PRD

### Technique 2: Template Substitution Composition
- **Category:** OT (Output Techniques)
- **Pattern:** Final output template with placeholder variables filled from intermediate artifacts
- **Example from resource:**
```markdown
Use assets/vibe-design-template.md:
- {项目设计指南} → Design system from Step 2
- {项目MVP PRD} → PRD from Step 3
Result: Complete implementation-ready prompt
```
- **Maps to existing:** NEW - **OT-17 Template Substitution Composition**
- **Effectiveness:** Separates structure (template) from content (artifacts); enables mix-and-match of design systems and PRDs

### Technique 3: Subagent Orchestration with Task Tool
- **Category:** AG (Agentic)
- **Pattern:** Main skill delegates to general-purpose subagents with structured prompts
- **Example from resource:**
```markdown
### Step 2: Extract Design System from Images
**Use Task tool with general-purpose subagent**, providing:
- Prompt template from assets/design-system.md
- Attach reference images to context
**Output**: Design system markdown
```
- **Maps to existing:** **AG-07 Multi-Agent Orchestration** + **AG-21 Agent Handoff**
- **Effectiveness:** Leverages general-purpose agent capabilities; main skill focuses on workflow coordination

### Technique 4: Image Analysis Prompt Template
- **Category:** DS (Domain-Specific - UI/UX Design)
- **Pattern:** Structured prompt template for extracting design patterns from images
- **Example from resource:**
```markdown
Template sections (assets/design-system.md):
- Color palette (primary, secondary, accent, functional, backgrounds)
- Typography (font families, weights, text styles)
- Component styles (buttons, cards, inputs, icons)
- Spacing system (4dp-48dp scale)
- Animations (durations, easing curves)
- Dark mode variants
```
- **Maps to existing:** NEW - **DS-116 Image Analysis Prompt Template**
- **Effectiveness:** Ensures comprehensive design system coverage; systematic extraction prevents missing critical patterns

### Technique 5: Interactive PRD Refinement Pattern
- **Category:** IT (Interaction Techniques)
- **Pattern:** Generate initial PRD from template, then refine through user interaction
- **Example from resource:**
```markdown
### Step 3: Generate MVP PRD
- Replace {项目背景} with project idea content
- **Interact with user** to refine and clarify
- Save refined PRD for Step 4
```
- **Maps to existing:** NEW - **IT-41 Interactive PRD Refinement Pattern**
- **Effectiveness:** Balances automation (template) with human judgment (refinement); clarifies ambiguities before implementation

### Technique 6: Timestamped Output Versioning
- **Category:** DS (Domain-Specific - File Management)
- **Pattern:** Append timestamp to final outputs for version tracking
- **Example from resource:**
```markdown
**Save to**: documents/ux-design/{idea_file_name}_design_prompt_{timestamp}.md
Example: project-management-app_design_prompt_20251025_153000.md
```
- **Maps to existing:** Extends **DS-103 Metadata Preservation** → **DS-117 Timestamped Output Versioning**
- **Effectiveness:** Preserves iteration history; enables comparison of design evolution

### Technique 7: Environment Verification Checkpoint
- **Category:** QA (Quality Assurance)
- **Pattern:** Check for required tooling before implementation, provide setup instructions if missing
- **Example from resource:**
```markdown
### Step 5: Verify React Environment
Check for existing React project:
```bash
find . -name "package.json" -exec grep -l "react" {} \;
```

If none found, inform user:
```bash
npx create-react-app my-app
npm install -D tailwindcss postcss autoprefixer
```
- **Maps to existing:** NEW - **QA-28 Environment Verification Checkpoint**
- **Effectiveness:** Prevents implementation failures; guides users through setup before work begins

### Technique 8: Best Practices by Workflow Stage
- **Category:** IT (Interaction Techniques)
- **Pattern:** Organize best practices by workflow stage rather than by topic
- **Example from resource:**
```markdown
## Best Practices

### Image Analysis
- Read all images before starting analysis
- Look for patterns across multiple screens

### Design System Extraction
- Use specific values (hex codes, px sizes)
- Document the "why" for design choices

### PRD Generation
- Engage user interactively to clarify ambiguities
- Ensure MVP scope is realistic

### Output Organization
- Save with descriptive filename
- Keep all outputs in documents/ directory
```
- **Maps to existing:** Extends **IT-36 Best Practices by Category** → **IT-42 Best Practices by Workflow Stage**
- **Effectiveness:** Contextual guidance when needed; users find relevant practices for current stage

### Technique 9: Complete Usage Example Section
- **Category:** IT (Interaction Techniques)
- **Pattern:** End-to-end example showing inputs, workflow execution, and outputs
- **Example from resource:**
```markdown
## Example Usage

**User provides:**
- reference-images/saas-dashboard/ (5 screenshots)
- ideas/project-management-app.md (project concept)

**Execute workflow:**
1. Read 5 images from reference-images/saas-dashboard/
2. Use Task tool → design-system.md template → analyze images
3. Save to documents/designs/saas-dashboard_design_system.md
4. [... full 9-step workflow ...]
```
- **Maps to existing:** Extends **IT-40 Real-World Example** → **IT-43 Complete Usage Example Section**
- **Effectiveness:** Shows concrete inputs/outputs for each step; reduces ambiguity about workflow execution

### Technique 10: High Freedom Workflow Disclosure
- **Category:** IT (Interaction Techniques)
- **Pattern:** Explicitly state workflow adaptability and encourage thoughtful customization
- **Example from resource:**
```markdown
## Notes

- This is a **high freedom** workflow—adapt steps based on context
- Templates provide structure but encourage thoughtful analysis over rote filling
- User interaction during PRD generation is critical for quality
```
- **Maps to existing:** NEW - **IT-44 High Freedom Workflow Disclosure**
- **Effectiveness:** Empowers agents to adapt workflow; prevents rigid template-filling without thinking

### Technique 11: Structured Asset Library
- **Category:** DS (Domain-Specific - Template Management)
- **Pattern:** Bundle multiple prompt templates as reusable assets with descriptions
- **Example from resource:**
```markdown
## Template Assets

### assets/design-system.md
Template for extracting visual design patterns. Includes sections for:
- Color palette, Typography, Component styles, Spacing, Animations

### assets/app-overview-generator.md
Template for collaborative PRD generation. Guides through:
- Elevator pitch, Problem statement, Feature list

### assets/vibe-design-template.md
Final implementation prompt template combining design system and PRD.
```
- **Maps to existing:** NEW - **DS-118 Structured Asset Library**
- **Effectiveness:** Organized prompt templates; clear documentation of each asset's purpose

## Novel Patterns (Not in MASTER_TECHNIQUE_INDEX)

### Pattern 1: Multi-Stage Workflow with Intermediate Outputs (DS-115)
- **Description:** Sequential stages producing reusable intermediate artifacts
- **Implementation:**
  - Stage 1: Extract raw data → save artifact
  - Stage 2: Transform data → save artifact
  - Stage 3: Compose final output from artifacts
  - All intermediate outputs preserved for iteration
- **Use case:** Complex workflows requiring multiple transformations, design processes, data pipelines
- **Example:** Code generation (AST → IR → target code), Report generation (data → analysis → visualization)
- **Proposed category:** DS (Domain-Specific - Design Workflows)
- **Proposed code:** DS-115

### Pattern 2: Template Substitution Composition (OT-17)
- **Description:** Final output template with placeholder variables filled from intermediate artifacts
- **Implementation:**
  - Create template with placeholders: `{artifact_name}`
  - Generate intermediate artifacts separately
  - Substitute placeholders with artifact content
  - Produce final composed output
- **Use case:** Report generation, code scaffolding, document assembly
- **Example:** Email templates, contract generation, configuration file assembly
- **Proposed category:** OT (Output Techniques)
- **Proposed code:** OT-17

### Pattern 3: Image Analysis Prompt Template (DS-116)
- **Description:** Structured prompt template for extracting design patterns from images
- **Implementation:**
  - Define comprehensive extraction checklist
  - Color palette (primary, secondary, accent, functional)
  - Typography (families, weights, sizes, styles)
  - Component styles (buttons, cards, inputs)
  - Spacing system, Animations, Dark mode
- **Use case:** Design system extraction, UI analysis, style guide creation
- **Example:** Converting Figma screenshots to design tokens, Analyzing competitor UIs
- **Proposed category:** DS (Domain-Specific - UI/UX Design)
- **Proposed code:** DS-116

### Pattern 4: Interactive PRD Refinement Pattern (IT-41)
- **Description:** Generate initial PRD from template, then refine through user interaction
- **Implementation:**
  - Generate initial draft from template + user input
  - Present draft to user
  - Iteratively refine through clarifying questions
  - Save refined version for next stage
- **Use case:** Requirements gathering, specifications, design documents
- **Example:** API specification, Architecture decision records, Test plans
- **Proposed category:** IT (Interaction Techniques)
- **Proposed code:** IT-41

### Pattern 5: Timestamped Output Versioning (DS-117)
- **Description:** Append timestamp to final outputs for automatic version tracking
- **Implementation:**
  - File naming pattern: `{base_name}_{descriptor}_{timestamp}.ext`
  - Example: `project_design_prompt_20251025_153000.md`
  - Enables chronological sorting and comparison
- **Use case:** Design iteration, configuration management, report generation
- **Example:** Architecture diagrams, Test reports, Generated code
- **Proposed category:** DS (Domain-Specific - File Management)
- **Proposed code:** DS-117

### Pattern 6: Environment Verification Checkpoint (QA-28)
- **Description:** Check for required tooling before implementation, provide setup if missing
- **Implementation:**
  - Define verification check (find command, package query)
  - If found: Proceed to implementation
  - If missing: Display setup instructions
  - User can choose to set up or skip
- **Use case:** Code generation, deployment workflows, tooling integration
- **Example:** Docker availability, Database connectivity, API credentials
- **Proposed category:** QA (Quality Assurance)
- **Proposed code:** QA-28

### Pattern 7: Best Practices by Workflow Stage (IT-42)
- **Description:** Organize best practices by workflow stage rather than by topic
- **Implementation:**
  - Identify workflow stages (Analysis, Design, Implementation, Testing)
  - List 3-5 best practices per stage
  - Place practices near relevant workflow steps
- **Use case:** Multi-stage workflows, process documentation, onboarding guides
- **Example:** Software development (design → code → test → deploy), Data pipelines (ingest → transform → validate → publish)
- **Proposed category:** IT (Interaction Techniques)
- **Proposed code:** IT-42

### Pattern 8: Complete Usage Example Section (IT-43)
- **Description:** End-to-end example showing inputs, workflow execution, outputs for every step
- **Implementation:**
  - Section: "Example Usage"
  - User provides: [Concrete inputs with paths/names]
  - Execute workflow: [Step-by-step with commands/actions]
  - Show outputs at each stage
- **Use case:** Complex workflow documentation, API tutorials, tool guides
- **Example:** ML training pipeline, CI/CD workflow, Data migration
- **Proposed category:** IT (Interaction Techniques)
- **Proposed code:** IT-43

### Pattern 9: High Freedom Workflow Disclosure (IT-44)
- **Description:** Explicitly state workflow adaptability and encourage thoughtful customization
- **Implementation:**
  - Add "Notes" section at end
  - State: "This is a high freedom workflow—adapt based on context"
  - Emphasize: "Templates provide structure but encourage thoughtful analysis"
- **Use case:** Flexible workflows, creative processes, contextual adaptation
- **Example:** Design processes, Research workflows, Troubleshooting guides
- **Proposed category:** IT (Interaction Techniques)
- **Proposed code:** IT-44

### Pattern 10: Structured Asset Library (DS-118)
- **Description:** Bundle multiple prompt templates as reusable assets with descriptions
- **Implementation:**
  - Create `assets/` directory
  - One template per file
  - Document each asset's purpose in main skill
  - Section: "Template Assets" with subsection per template
- **Use case:** Prompt engineering, code generation, document assembly
- **Example:** Email template library, Code scaffold templates, Report templates
- **Proposed category:** DS (Domain-Specific - Template Management)
- **Proposed code:** DS-118

## Multi-Technique Combinations

The `ui-designer` skill demonstrates sophisticated combination of techniques:

1. **Multi-Stage Workflow + Intermediate Outputs:**
   - Multi-Stage Workflow defines 6 sequential steps
   - Each stage produces saved intermediate artifacts
   - Result: Reusable design systems, iterable PRDs

2. **Template Substitution + Structured Asset Library:**
   - Structured Asset Library provides 3 templates
   - Template Substitution composes final output
   - Result: Mix-and-match design systems with different PRDs

3. **Subagent Orchestration + Image Analysis Template:**
   - Subagent receives Image Analysis Prompt Template
   - Analyzes images, fills template systematically
   - Result: Comprehensive design system extraction

4. **Interactive Refinement + Best Practices:**
   - Interactive PRD Refinement engages user
   - Best Practices by Stage guide clarification
   - Result: High-quality, validated requirements

5. **Environment Verification + Timestamped Versioning:**
   - Environment Verification ensures tooling ready
   - Timestamped Versioning tracks design iterations
   - Result: Production-ready workflow with audit trail

## Integration Notes

### For MASTER_TECHNIQUE_INDEX.md:
1. **Add 10 new techniques:**
   - DS-115: Multi-Stage Workflow with Intermediate Outputs
   - OT-17: Template Substitution Composition
   - DS-116: Image Analysis Prompt Template
   - IT-41: Interactive PRD Refinement Pattern
   - DS-117: Timestamped Output Versioning
   - QA-28: Environment Verification Checkpoint
   - IT-42: Best Practices by Workflow Stage
   - IT-43: Complete Usage Example Section
   - IT-44: High Freedom Workflow Disclosure
   - DS-118: Structured Asset Library

2. **Create new subcategories:**
   - "Design Workflows" (DS-115)
   - "UI/UX Design" (DS-116)
   - "Template Management" (DS-118)

3. **Cross-reference existing techniques:**
   - AG-07 (Multi-Agent Orchestration) + AG-21 (Agent Handoff) - subagent pattern
   - IT-36 (Best Practices by Category) → IT-42 extends to workflow stages
   - IT-40 (Real-World Example) → IT-43 extends to complete usage example

### For USE_CASE_LOOKUP.md:
- Add "UI Design System Extraction" use case
- Recommended techniques: DS-115, OT-17, DS-116, IT-41, DS-117, QA-28, DS-118

### For AI_AGENT_QUICK_START.md:
- Add example in Section 5: "Multi-stage design workflow with template composition"
- Demonstrate Template Substitution Composition pattern

## Summary

**Complexity Rating:** 5/5

The `ui-designer` skill is a **multi-stage design system extraction and composition workflow** that orchestrates subagents, processes images, generates intermediate artifacts, and composes final implementation prompts through template substitution.

**Key Strengths:**
1. **Systematic extraction:** Image Analysis Prompt Template ensures comprehensive coverage
2. **Reusable artifacts:** Intermediate outputs (design system, PRD) can be mixed and matched
3. **Interactive refinement:** User collaboration during PRD generation improves quality
4. **Production-ready:** Environment verification, timestamped versioning, complete examples

**Novel Contributions:**
- Multi-Stage Workflow with Intermediate Outputs (DS-115): Universal pattern for complex transformations
- Template Substitution Composition (OT-17): Modular output assembly from artifacts
- Image Analysis Prompt Template (DS-116): Systematic design system extraction from images
- High Freedom Workflow Disclosure (IT-44): Empowers adaptive execution

**Recommended Integration Priority:** HIGH
- DS-115 (Multi-Stage Workflow): Applicable to any complex transformation process
- OT-17 (Template Substitution): Standard for modular output composition
- IT-44 (High Freedom Workflow): Important for flexible, context-aware workflows

**Lines of Bundled Knowledge:** 477 lines
- SKILL.md: 192 lines (workflow documentation)
- assets/design-system.md: 155 lines (extraction template in Chinese)
- assets/app-overview-generator.md: 73 lines (PRD template in Chinese)
- assets/vibe-design-template.md: 57 lines (final composition template)

**Production Readiness:** 5/5 - Multi-stage workflow with intermediate artifact preservation, environment verification, timestamped versioning, interactive refinement, and complete working example

**Workflow Stages:**
1. Gather Inputs (images + project idea)
2. Extract Design System (subagent + template) → save artifact
3. Generate MVP PRD (subagent + template + user refinement) → save artifact
4. Compose Final Prompt (template substitution) → save timestamped output
5. Verify React Environment (setup instructions if needed)
6. Implement UI (React components)
