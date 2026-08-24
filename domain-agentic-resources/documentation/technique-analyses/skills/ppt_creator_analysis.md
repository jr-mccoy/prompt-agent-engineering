# Technique Analysis: ppt-creator

**Resource Type:** Skill (Content Generation with Quality Assurance)
**Path:** `claude-code-resources/skills/document-processing/ppt-creator/`
**Date Analyzed:** 2025-12-22
**Bundled Resources:** 1 script (chartkit.py) + 11 reference documents (4,622 lines)
**Complexity:** 4/5 (High - Multi-stage workflow with auto-quality assurance)

## Overview

The `ppt-creator` skill demonstrates how to build content generation workflows with built-in quality assurance, progressive refinement, and orchestration capabilities. It transforms a simple topic into presentation-ready slide decks through a 9-stage process, self-evaluating against a rubric and auto-iterating until quality threshold is met.

**Key Innovation:** Quality-gated content generation with safe defaults - the skill never blocks on missing information, instead using documented assumptions while maintaining high output quality through iterative refinement.

## Bundled Resources Summary

### Script (1 file, ~100 lines)
- `scripts/chartkit.py` - Minimal chart renderer using matplotlib/pandas

### References (11 markdown files, 4,622 lines)

**Core Workflow:**
1. **INTAKE.md** (225 lines) - 10-item minimal questionnaire with safe defaults
2. **WORKFLOW.md** (573 lines) - 9-stage step-by-step process
3. **TEMPLATES.md** (540 lines) - Slide template library (assertion-evidence style)

**Quality Assurance:**
4. **CHECKLIST.md** (357 lines) - Pre-flight quality checks
5. **RUBRIC.md** (414 lines) - 10-item scoring rubric (100 points, ≥75 to deliver)

**Design Standards:**
6. **STYLE-GUIDE.md** (460 lines) - Layout, fonts, spacing, colors, accessibility (WCAG AA)
7. **VIS-GUIDE.md** (446 lines) - Chart selection dictionary and labeling standards

**Orchestration:**
8. **ORCHESTRATION_OVERVIEW.md** (248 lines) - End-to-end automation overview
9. **ORCHESTRATION_DATA_CHARTS.md** (140 lines) - Data synthesis and chart generation
10. **ORCHESTRATION_PPTX.md** (659 lines) - Dual-path PPTX creation and chart insertion

**Examples:**
11. **EXAMPLES.md** (560 lines) - Two complete usage examples with iterations

### Total Bundled Knowledge
- **Script:** ~100 lines (chartkit.py)
- **References:** 4,622 lines (11 specialized documents)
- **SKILL.md:** 171 lines (entry point)
- **Total:** ~4,893 lines

---

## Identified Techniques

### Technique 1: Safe Defaults Pattern

- **Category:** IT (Interaction Techniques) - NEW
- **Pattern:** Every required input has a safe default; missing info triggers defaults instead of blocking progress
- **Example from resource:**
  ```markdown
  # From INTAKE.md

  ## Minimal Intake Questionnaire (10 Items)

  ### 1. Who is the audience?
  **Question**: Who will be viewing/listening to this presentation?
  **Default if missing**: General public (educated adults with no specialized background)
  **Impact**: Determines technical depth, jargon usage, and evidence types.

  ### 2. What is the core objective?
  **Question**: What do you want the audience to understand, believe, or feel?
  **Default if missing**: "Understand and accept" the main proposition
  **Impact**: Shapes the storyline and emphasis throughout the deck.

  ### 3. What is the desired action or decision?
  **Question**: What specific action should the audience take?
  **Default if missing**: Agree to move to the next step after the meeting
  **Impact**: Defines the call-to-action (CTA) on the closing slide.

  [7 more with defaults...]

  # From SKILL.md
  **Goal**: When key information is missing, use the minimal intake form to gather
  context or apply safe defaults. If the user doesn't respond after 2 prompts, use
  the **safe default** for each item and clearly note assumptions in speaker notes.
  ```
- **Maps to existing:** NEW - Systematic default values for missing inputs
- **Effectiveness:** Eliminates blocking on missing info while maintaining transparency

**Safe Defaults for All 10 Items:**
1. Audience → General public
2. Objective → "Understand and accept"
3. Desired action → Agree to next step
4. Duration → 15-20 min, 12-15 slides
5. Tone → Professional, clear, friendly
6. Topic scope → Given topic + 1 layer related
7. Must-include/taboos → None
8. Available data → None (generate placeholders)
9. Brand constraints → Built-in neutral theme
10. Format preference → slides.md + optional charts

### Technique 2: Quality Rubric with Auto-Iteration

- **Category:** QA (Quality Assurance) - NEW
- **Pattern:** Self-evaluate against rubric, auto-iterate up to N times if score below threshold
- **Example from resource:**
  ```markdown
  # From RUBRIC.md

  ## Scoring System
  - **Total Score**: 100 points (10 items × 10 points each)
  - **Passing Threshold**: ≥ 75 points
  - **Rating Scale** (per item):
    - 9-10: Excellent
    - 7-8: Good
    - 5-6: Acceptable
    - 3-4: Weak (significant improvements required)
    - 0-2: Poor (fundamental issues, must fix)

  ## Self-Evaluation Process

  1. Run CHECKLIST first (pre-flight quality checks)
  2. Score each of 10 items (see detailed criteria below)
  3. Calculate total score
  4. If total < 75:
     - Identify weakest 3 items
     - Document improvement actions
     - Apply improvements
     - Re-score (max 2 iterations)
  5. If total ≥ 75: Deliver

  ## 10 Scoring Items:
  1. Goal Clarity (audience, objective, CTA defined?)
  2. Story Structure (Pyramid Principle applied?)
  3. Slide Assertions (headings are testable claims?)
  4. Evidence Quality (claims backed by data/citations?)
  5. Chart Fit (correct selection, complete labeling?)
  6. Visual & Accessibility (contrast, fonts, white space, WCAG AA?)
  7. Coherence & Transitions (natural chapter flow?)
  8. Speakability (45-60 sec per slide, natural language?)
  9. Deliverables Complete (all required files present?)
  10. Robustness (gaps marked, fallback plan provided?)
  ```

  ```markdown
  # From SKILL.md
  6. **Self-Check & Score**: Use references/CHECKLIST.md for pre-flight check, then
     score with references/RUBRIC.md. If total score < 75, identify the weakest 3
     items and refine; repeat scoring (max 2 iterations).
  ```
- **Maps to existing:** QA-05 (Test Coverage Matrix) - Similar but for content quality
- **Effectiveness:** Systematic quality assurance with objective criteria and auto-improvement

**Auto-Iteration Logic:**
```
Generate content → Score (10 items × 10 points)
↓
Score ≥ 75? → YES → Deliver
↓
NO → Identify weakest 3 items → Refine → Re-score
↓
Iteration < 2? → YES → Repeat
↓
NO → Deliver with quality warnings
```

### Technique 3: Multi-Stage Workflow with Checkpoints

- **Category:** DS (Domain-Specific) - Extension of DS-27
- **Pattern:** 9-stage sequential process with clear checkpoints and deliverables
- **Example from resource:**
  ```markdown
  # From WORKFLOW.md

  ## 9-Stage Pipeline

  **Stage 0 - Archive Input**
  - Record user's original request
  - Document defaults used
  - Log assumptions made
  - Output: archive.txt

  **Stage 1 - Structure Goals**
  - Rewrite goal as "who takes what action when" (clear CTA)
  - Output: goals.txt

  **Stage 2 - Storyline**
  - Apply Pyramid Principle: one conclusion → 3-5 reasons → evidence
  - Output: storyline.txt

  **Stage 3 - Outline & Slide Titles**
  - Create 12-15 slide skeleton
  - Each slide has one assertion-style heading (complete sentence)
  - Output: outline.txt

  **Stage 4 - Evidence & Charts**
  - Use Chart Selection Dictionary from VIS-GUIDE
  - Generate charts if data provided (call chartkit.py)
  - Otherwise: Create placeholder + required field list
  - Output: slides_draft.md, chart_specs.txt

  **Stage 5 - Layout & Accessibility**
  - Apply STYLE-GUIDE (fonts, spacing, contrast ratios, color palettes)
  - Unify units and decimal places
  - Output: slides_styled.md

  **Stage 6 - Speaker Notes**
  - Generate 45-60 second notes per slide
  - Structure: opening → assertion → evidence → transition
  - Output: notes.md

  **Stage 7 - Self-Check & Scoring**
  - Run CHECKLIST (pre-flight)
  - Score with RUBRIC (10 items)
  - If score < 75: Refine weakest 3 items, re-score (max 2 iterations)
  - Output: rubric_score.txt, improvements.txt

  **Stage 8 - Package Deliverables**
  - Create /output/ directory
  - Generate slides.md, notes.md, refs.md, assets/*.png
  - If python-pptx available: Export PPTX
  - Output: Complete /output/ package

  **Stage 9 - Reuse Instructions**
  - Append "5-step guide to replace data/colors with your own"
  - Output: notes.md (updated with reuse guide)
  ```
- **Maps to existing:** DS-27 (Workflow-Encoded Process) + DS-24 (Validation Pipeline)
- **Effectiveness:** Clear progression with checkpoints ensures no steps skipped

### Technique 4: Orchestration Mode with Dual-Path Generation

- **Category:** AG (Agentic - Orchestration) - NEW
- **Pattern:** End-to-end automation that coordinates multiple tools/agents and generates multiple output formats for comparison
- **Example from resource:**
  ```markdown
  # From ORCHESTRATION_OVERVIEW.md

  ## When to Use Orchestration Mode

  ### Activation Triggers
  User request includes:
  - "Generate complete PPTX with real charts"
  - "Create final deliverable ready for presentation"
  - "Export to PowerPoint with all visualizations"

  ### Workflow (extends Stage 8)

  Stage 8: Package Deliverables (Extended)
    ├─ 8a: Package Markdown deliverables (baseline)
    │     └─ Output: /output/slides.md, notes.md, refs.md
    │
    ├─ 8b: Synthesize Data (if needed)
    │     ├─ Check: User provided data files?
    │     └─ If no: Generate synthetic CSV files matching specs
    │           → Output: /output/data/*.csv
    │
    ├─ 8c: Generate Charts
    │     ├─ Read: refs.md (chart specifications)
    │     ├─ Read: data/*.csv (generated or user-provided)
    │     ├─ Execute: Python/matplotlib chart generation
    │     └─ Output: /output/assets/*.png (180 DPI)
    │
    ├─ 8d: Dual-Path PPTX Creation (PARALLEL)
    │     ├─ Path A: Marp CLI export
    │     │   └─ Output: presentation_marp.pptx
    │     └─ Path B: document-skills:pptx
    │         └─ Output: presentation_pptx.pptx
    │
    └─ 8e: Dual-Path Chart Insertion (PARALLEL)
          ├─ Insert charts into presentation_marp.pptx
          │   └─ Output: presentation_marp_with_charts.pptx
          └─ Insert charts into presentation_pptx.pptx
              └─ Output: presentation_pptx_with_charts.pptx

  **Deliverables**: TWO complete PPTX files with different styling for comparison

  # From SKILL.md
  ## Orchestration Mode (End-to-End Automation)

  When the user requests a "complete" or "presentation-ready" deliverable,
  ppt-creator automatically orchestrates the full pipeline:

  content creation → data synthesis → chart generation → dual-path PPTX →
  chart insertion

  **Duration**: 4-6 minutes (parallel execution)
  **Output**: 2 complete PPTX files with real charts
  ```
- **Maps to existing:** AG-07 (Multi-Agent Orchestration) - Similar but for single-agent multi-tool coordination
- **Effectiveness:** One request triggers complete pipeline; dual outputs provide choice

**Orchestration Coordination:**
1. **Auto-activation:** Detect trigger phrases
2. **Data synthesis:** Generate synthetic data if missing
3. **Chart generation:** Execute Python/matplotlib scripts
4. **Parallel PPTX creation:** Two paths simultaneously
5. **Chart insertion:** Inject PNGs into both PPTX files
6. **User choice:** Deliver two styled versions

### Technique 5: Assertion-Evidence Content Structure

- **Category:** DS (Domain-Specific - Content) - NEW
- **Pattern:** Enforce specific content structure based on proven communication principles
- **Example from resource:**
  ```markdown
  # From SKILL.md

  ## Core Principles (Must Follow)

  **Information Organization**: Pyramid Principle
  - Conclusion first, then evidence
  - Each slide conveys ONLY 1 core idea
  - Headings must be **testable assertion sentences**, not topic labels

  **Examples**:
  - ✅ Assertion: "Finer grind size extracts flavors faster"
  - ❌ Topic label: "Grind Size"

  - ✅ Assertion: "Revenue grew 35% year-over-year"
  - ❌ Topic label: "Q3 Results"

  **Evidence-First**:
  - Use charts/tables/evidence blocks instead of paragraphs
  - Limit to 3-5 bullet points per slide
  - Body content provides evidence supporting the assertion

  # From RUBRIC.md

  ## 3. Slide Assertions (0-10 points)

  **Test**: Can you agree/disagree with the heading?
  - If YES → assertion (testable claim)
  - If NO → topic label (weak)

  **Scoring**:
  - 10: All slide headings are complete, testable assertion sentences
  - 6: Mix of assertions and topic labels (50/50)
  - 2: All headings are topic labels

  # From TEMPLATES.md

  ## Assertion-Evidence Template

  **Slide Heading** (Assertion): "[Complete sentence making a claim]"

  **Body** (Evidence):
  - Data point supporting the claim
  - Chart or table visualizing the evidence
  - Example or case study demonstrating the claim

  **Speaker Note**: Explain why this evidence supports the assertion
  ```
- **Maps to existing:** OT-02 (Template-Based Generation) - Similar but with strict structural rules
- **Effectiveness:** Forces clarity and testability in every slide

**Pyramid Principle Application:**
```
Cover Slide
└─ Main Conclusion: "Master three variables for great coffee"

Section 1: Grind Size
├─ Assertion: "Finer grind extracts flavors faster"
└─ Evidence: Chart showing extraction time vs grind size

Section 2: Water Temperature
├─ Assertion: "195-205°F range optimizes flavor compounds"
└─ Evidence: Table of flavor profiles by temperature

Section 3: Brew Time
├─ Assertion: "4-minute brew yields balanced extraction"
└─ Evidence: Graph of extraction percentage over time
```

### Technique 6: Chart Selection Dictionary

- **Category:** DS (Domain-Specific - Visualization) - NEW
- **Pattern:** Rule-based chart type selection mapping questions to visualization types
- **Example from resource:**
  ```markdown
  # From VIS-GUIDE.md

  ## Chart Selection Dictionary

  **Question Type** → **Chart Type**

  ### Comparison
  - "Which is larger?" → Bar chart (horizontal for readability)
  - "How do categories rank?" → Sorted bar chart
  - "A vs B head-to-head?" → Grouped bar chart or table

  ### Distribution
  - "What's the spread?" → Histogram
  - "Show me the range" → Box plot
  - "Density comparison?" → Violin plot

  ### Relationship
  - "Correlation between X and Y?" → Scatter plot
  - "Multiple variables?" → Scatter matrix or bubble chart

  ### Composition
  - "Parts of a whole?" → Pie chart (max 5 categories) or Treemap
  - "How does composition change?" → Stacked area chart
  - "Breakdown over time?" → Stacked bar chart

  ### Trend
  - "How does X change over time?" → Line chart
  - "Multiple trends?" → Multi-line chart with legend
  - "Cumulative growth?" → Area chart

  ### Flow
  - "Process stages?" → Sankey diagram or Funnel chart
  - "Network connections?" → Network graph

  ### Geographic
  - "Regional distribution?" → Choropleth map
  - "Point locations?" → Scatter map with markers

  ## Labeling Standards (Required)

  Every chart MUST include:
  1. **Title**: Assertion sentence (not "Chart 1")
  2. **Axes**: Clear labels with units (e.g., "Revenue ($M)", "Time (seconds)")
  3. **Legend**: If multiple series (max 7 series for readability)
  4. **Data source**: Footer citation (e.g., "Source: Q3 2024 Sales Data")
  5. **Annotations**: Highlight key data points or thresholds
  ```
- **Maps to existing:** DS-02 (Metric Specification) - Similar decision logic but for charts
- **Effectiveness:** Removes guesswork from visualization selection

### Technique 7: Accessibility Enforcement with Standards

- **Category:** DS (Domain-Specific - Accessibility)
- **Pattern:** Document and enforce specific accessibility standards (WCAG AA)
- **Example from resource:**
  ```markdown
  # From STYLE-GUIDE.md

  ## Accessibility Standards (WCAG 2.1 AA Compliance)

  ### Contrast Ratios (Required)
  - **Text vs Background**: ≥ 4.5:1 (normal text)
  - **Large text vs Background**: ≥ 3:1 (18pt+ or 14pt+ bold)
  - **UI elements vs Background**: ≥ 3:1 (buttons, icons, charts)

  ### Color Palette (AA Compliant)
  - **Dark Ink**: #1F2937 (vs white = 14.8:1) ✓
  - **Background**: #FFFFFF
  - **Accent**: #2563EB (vs white = 5.9:1) ✓
  - **Emphasis**: #DC2626 (vs white = 5.1:1) ✓

  ### Font Sizes (Minimum)
  - **Heading**: 34-40pt
  - **Subheading**: 24-28pt
  - **Body text**: 18-22pt (minimum 18pt)
  - **Footer**: 14-16pt

  ### Line Spacing
  - **Headings**: 1.1× (tight for impact)
  - **Body text**: 1.3× (readable)
  - **Bullet spacing**: ≥ 8px between items

  ### Images & Charts
  - **Alt descriptions**: Brief text description for screen readers
  - **Color independence**: Don't rely on color alone (use patterns/labels)
  - **Text in images**: Avoid if possible; if needed, ensure ≥ 18pt

  ### Page Density
  - **Maximum**: ≤ 70 words per slide (excluding captions)
  - **White space**: ≥ 48px safe margins
  ```
- **Maps to existing:** DS-11 (Accessibility Scanning) - But more comprehensive
- **Effectiveness:** Ensures presentations are accessible to all audiences

### Technique 8: Progressive Disclosure for Complex Workflows

- **Category:** IT (Interaction Techniques)
- **Pattern:** Entry point (SKILL.md) references specialized guides; read only as needed
- **Example from resource:**
  ```markdown
  # From SKILL.md (171 lines)

  ## Quick Start (7 steps, 30 lines)
  [Concise instructions for common case]

  ## Orchestration Mode (20 lines)
  For orchestration details, see:
  - `references/ORCHESTRATION_OVERVIEW.md` (start here)
  - Then navigate to specialized guides as needed

  ## Resources (40 lines)
  **References** (load as needed):
  - **Critical**: WORKFLOW.md, RUBRIC.md
  - **Getting started**: INTAKE.md, TEMPLATES.md
  - **Design**: STYLE-GUIDE.md, VIS-GUIDE.md
  - **Quality**: CHECKLIST.md
  - **Examples**: EXAMPLES.md
  - **Advanced**: ORCHESTRATION_*.md (3 files)
  ```

  **Loading Hierarchy:**
  ```
  SKILL.md (171 lines) - Always loaded
  ↓
  For quality checks: CHECKLIST.md (357 lines)
  ↓
  For scoring: RUBRIC.md (414 lines)
  ↓
  For detailed workflow: WORKFLOW.md (573 lines)
  ↓
  For orchestration: ORCHESTRATION_OVERVIEW.md (248 lines)
  ↓
  For specific orchestration stage: ORCHESTRATION_PPTX.md (659 lines)
  ```
- **Maps to existing:** IT-06 (Progressive Disclosure)
- **Effectiveness:** 4,622 lines of docs remain outside context until needed

### Technique 9: Template Library with Structural Guidance

- **Category:** OT (Output Techniques)
- **Pattern:** Comprehensive template library with "when to use" guidance
- **Example from resource:**
  ```markdown
  # From TEMPLATES.md

  ## Slide Template Library

  ### 1. Cover
  **Use when**: Opening slide
  **Structure**:
  - Title (assertion sentence stating main conclusion)
  - Subtitle (context or scope)
  - Presenter name/date/logo
  **Example**: "Master Three Variables for Great Coffee | Home Brewing Guide"

  ### 2. Problem Statement
  **Use when**: Establishing the need or pain point
  **Structure**:
  - Heading (assertion): "Current approach wastes 30% of brewing time"
  - Evidence: Data showing inefficiency
  - Impact: "Resulting in inconsistent quality and higher costs"
  **Example**: "Manual temperature control causes 15°F variance"

  ### 3. Opportunity/Goal
  **Use when**: Defining the solution space
  **Structure**:
  - Heading (assertion): "Automated temperature control reduces variance to 2°F"
  - Benefits: Bullet list (3-5 items)
  - Quantified impact: "$2.4M annual savings"

  [11 more templates with structures...]

  ## Micro-Templates

  ### Comparison (A vs B)
  | Aspect | Option A | Option B | Winner |
  |--------|----------|----------|--------|
  | Speed  | 10 min   | 5 min    | B ✓    |
  | Cost   | $50      | $75      | A ✓    |
  | Quality| 7/10     | 9/10     | B ✓    |

  ### Pyramid Summary
  Main Conclusion
  ├─ Reason 1 → Evidence 1.1, Evidence 1.2
  ├─ Reason 2 → Evidence 2.1, Evidence 2.2
  └─ Reason 3 → Evidence 3.1, Evidence 3.2

  [10 more micro-templates...]
  ```
- **Maps to existing:** OT-03 (Output Templates)
- **Effectiveness:** Reduces decision fatigue with proven structures

---

## Novel Patterns (Not in MASTER_TECHNIQUE_INDEX)

### Pattern 1: IT-18: Safe Defaults Pattern

- **Description:** Every required input has a documented safe default; missing info triggers defaults instead of blocking
- **Implementation:**
  - 10-item intake questionnaire
  - Each item has a safe default value
  - Defaults chosen to work for 80% of use cases
  - Assumptions documented clearly in output
  - User can override at any time
- **Use case:** Content generation where blocking on missing info would stall workflow
- **Example:**
  ```markdown
  ## Intake Questions with Safe Defaults

  1. Audience? → Default: General public
  2. Objective? → Default: "Understand and accept"
  3. Desired action? → Default: Agree to next step
  4. Duration? → Default: 15-20 min, 12-15 slides
  5. Tone? → Default: Professional, clear, friendly

  # In practice:
  User: "Create a presentation about coffee"
  [No other info provided]

  Assistant:
  - Uses all 10 defaults
  - Documents in speaker notes: "Assumed audience: general public"
  - Proceeds with content generation
  - Delivers complete, usable presentation
  ```
- **Proposed category:** IT (Interaction Techniques)
- **Proposed code:** IT-18
- **Priority:** HIGH - Eliminates blocking in workflows

### Pattern 2: QA-10: Quality Rubric with Auto-Iteration

- **Description:** Self-evaluate against objective rubric, auto-iterate up to N times if score below threshold
- **Implementation:**
  - Define rubric with specific scoring criteria (10 items × 10 points = 100)
  - Set passing threshold (≥75 points)
  - After generation, self-score each item
  - If total < threshold: Identify weakest items, refine, re-score
  - Limit iterations (max 2) to prevent infinite loops
  - Deliver when threshold met or iterations exhausted
- **Use case:** Ensuring content quality without manual review
- **Example:**
  ```
  Generate slides → Score (10 items)
  Total = 68 (< 75 threshold)
  ↓
  Weakest items: #3 (Slide Assertions=4), #5 (Chart Fit=5), #6 (Visual=4)
  ↓
  Iteration 1:
  - Fix slide headings (make assertions)
  - Improve chart selection
  - Adjust fonts/spacing
  ↓
  Re-score → Total = 78 (≥ 75) → Deliver
  ```
- **Proposed category:** QA (Quality Assurance)
- **Proposed code:** QA-10
- **Priority:** HIGH - Autonomous quality assurance

### Pattern 3: AG-22: Orchestration Mode with Dual-Path Generation

- **Description:** End-to-end automation that coordinates multiple tools and generates multiple output formats for comparison
- **Implementation:**
  - Activation triggers (user phrases indicating need for complete deliverable)
  - Sequential stages: data synthesis → chart generation → PPTX creation
  - Parallel execution where possible (two PPTX paths simultaneously)
  - Deliver multiple styled versions for user choice
  - Estimated time communicated upfront
- **Use case:** Complete deliverable generation requiring multiple specialized tools
- **Example:**
  ```
  User: "Create complete PPTX with real charts"
  ↓
  Orchestration mode activated
  ↓
  Stage 8b: Synthesize data (generate CSV if missing)
  Stage 8c: Generate charts (matplotlib)
  Stage 8d: PARALLEL
    ├─ Path A: Marp CLI → presentation_marp.pptx
    └─ Path B: document-skills:pptx → presentation_pptx.pptx
  Stage 8e: PARALLEL
    ├─ Insert charts → presentation_marp_with_charts.pptx
    └─ Insert charts → presentation_pptx_with_charts.pptx
  ↓
  Deliver 2 complete PPTX files (4-6 minutes total)
  ```
- **Proposed category:** AG (Agentic - Orchestration)
- **Proposed code:** AG-22
- **Priority:** HIGH - Multi-tool coordination

### Pattern 4: DS-33: Assertion-Evidence Content Structure

- **Description:** Enforce specific content structure based on proven communication principles (Pyramid Principle)
- **Implementation:**
  - Conclusion first, then supporting reasons, then evidence
  - Each slide = 1 core idea
  - Headings must be testable assertion sentences (not topic labels)
  - Body provides evidence (charts/tables/data, not paragraphs)
  - Limit to 3-5 bullet points per slide
- **Use case:** Creating persuasive, structured presentations
- **Example:**
  ```
  ❌ Weak (Topic Label):
  Heading: "Coffee Brewing"
  Body: Various facts about coffee

  ✅ Strong (Assertion-Evidence):
  Heading: "195-205°F water temperature optimizes flavor extraction"
  Body:
  - Chart showing extraction rates by temperature
  - Table of flavor compounds vs temperature
  - Case study: taste test results
  ```
- **Proposed category:** DS (Domain-Specific - Content)
- **Proposed code:** DS-33
- **Priority:** MEDIUM - Domain-specific but broadly applicable

### Pattern 5: DS-34: Chart Selection Dictionary

- **Description:** Rule-based visualization type selection mapping questions to chart types
- **Implementation:**
  - Map common question types to appropriate chart types
  - Include labeling standards for each chart type
  - Provide fallback logic (if data insufficient → placeholder)
  - Enforce accessibility standards (contrast, labels, sources)
- **Use case:** Automatic chart type selection for data visualization
- **Example:**
  ```python
  def select_chart_type(question: str, data: DataFrame) -> str:
      if "compare" in question or "which is larger" in question:
          return "bar_chart"
      elif "over time" in question or "trend" in question:
          return "line_chart"
      elif "parts of whole" in question or "percentage" in question:
          return "pie_chart" if len(data) <= 5 else "treemap"
      elif "correlation" in question or "relationship" in question:
          return "scatter_plot"
      elif "distribution" in question or "spread" in question:
          return "histogram"
      else:
          return "table"  # Safe fallback
  ```
- **Proposed category:** DS (Domain-Specific - Visualization)
- **Proposed code:** DS-34
- **Priority:** MEDIUM - Useful for data visualization workflows

---

## Multi-Technique Combinations

### Combination 1: Quality-Gated Content Generation
**Techniques:** IT-18 (Safe Defaults) + QA-10 (Rubric Auto-Iteration) + DS-33 (Assertion-Evidence)

Produces high-quality content without blocking:
1. **Safe defaults** (IT-18): Never blocks on missing info
2. **Structured content** (DS-33): Enforces proven communication patterns
3. **Auto-refinement** (QA-10): Iterates until quality threshold met

**Result:** Reliable, high-quality deliverables from minimal input

### Combination 2: End-to-End Orchestration
**Techniques:** AG-22 (Orchestration Mode) + DS-34 (Chart Selection) + IT-06 (Progressive Disclosure)

Automates complete pipeline:
1. **Orchestration** (AG-22): Coordinates data → charts → PPTX → insertion
2. **Chart selection** (DS-34): Auto-selects appropriate visualization types
3. **Progressive docs** (IT-06): Detailed guides loaded only when orchestrating

**Result:** Single request produces complete, presentation-ready PPTX files

### Combination 3: Multi-Stage Quality Assurance
**Techniques:** QA-10 (Rubric) + DS-28 (SOLID - from transcript-fixer) + IT-18 (Safe Defaults)

Systematic quality through pipeline:
1. **Safe defaults** (IT-18): Ensures all required inputs have values
2. **SOLID workflow** (DS-28): 9 clear stages, each with single responsibility
3. **Rubric scoring** (QA-10): Objective quality gate before delivery

**Result:** Consistent quality output regardless of input completeness

---

## Integration Notes

### For MASTER_TECHNIQUE_INDEX.md
Add these 5 novel techniques:
- **IT-18:** Safe Defaults Pattern (HIGH priority)
- **QA-10:** Quality Rubric with Auto-Iteration (HIGH priority)
- **AG-22:** Orchestration Mode with Dual-Path Generation (HIGH priority)
- **DS-33:** Assertion-Evidence Content Structure (MEDIUM priority)
- **DS-34:** Chart Selection Dictionary (MEDIUM priority)

### For AI_AGENT_QUICK_START.md
Add section on quality-gated content generation:
- Safe defaults eliminate blocking on missing info
- Self-evaluation rubrics enable autonomous quality assurance
- Multi-stage workflows with checkpoints ensure completeness
- Orchestration mode coordinates multiple tools/agents

### For USE_CASE_LOOKUP.md
Add patterns for:
- **Content generation:** Safe defaults, quality rubrics, structured content
- **Orchestration:** Multi-tool coordination, dual-path generation
- **Quality assurance:** Auto-iteration, checkpoint validation

### Key Insights

1. **Safe Defaults Enable Flow:** Never block on missing info - use documented defaults
2. **Quality Can Be Objective:** Rubrics with specific criteria enable self-evaluation
3. **Iteration Improves Output:** Auto-refine based on weakest scored items
4. **Structure Ensures Clarity:** Assertion-evidence style forces testable claims
5. **Orchestration Coordinates Complexity:** Single request can trigger multi-tool pipeline
6. **Progressive Disclosure Scales:** 4,622 lines of docs loaded only as needed

---

## Complexity Justification: 4/5

This skill earns high complexity rating because it:

1. **Multi-stage workflow:** 9 sequential stages with clear checkpoints
2. **Quality assurance:** 10-item rubric with auto-iteration (max 2 times)
3. **Safe defaults:** 10-item intake form, each with documented default
4. **Orchestration mode:** End-to-end automation coordinating multiple tools
5. **Dual-path generation:** Parallel PPTX creation in two styling paths
6. **Comprehensive references:** 11 specialized documents (4,622 lines)
7. **Accessibility standards:** WCAG AA compliance enforced
8. **Content structure:** Pyramid Principle, assertion-evidence style
9. **Chart selection:** Rule-based visualization type mapping
10. **Template library:** 14+ slide templates with structural guidance

**Total Novel Techniques:** 5 (IT-18, QA-10, AG-22, DS-33, DS-34)
**Bundled Knowledge:** 4,793 lines (SKILL.md + scripts + references)
**Use Case:** Demonstrates quality-gated content generation with safe defaults and auto-refinement

---

## Statistics

- **SKILL.md lines:** 171
- **Script lines:** ~100 (chartkit.py)
- **Reference lines:** 4,622 (11 documents)
- **Total lines:** ~4,893
- **Novel techniques:** 5
- **High-priority techniques:** 3
- **Workflow stages:** 9 (0-8)
- **Quality rubric items:** 10 (100 points total)
- **Passing threshold:** ≥75 points
- **Max iterations:** 2
- **Safe defaults:** 10 (one per intake item)
- **Template count:** 14+ (slide types + micro-templates)
- **Orchestration stages:** 5 (8a-8e)
- **Output formats:** 2 (Marp + document-skills:pptx)

**Pattern Density:** 1.02 novel techniques per 1,000 lines of bundled knowledge (5 / 4.893)
**Quality Focus:** 2 dedicated quality assurance documents (CHECKLIST + RUBRIC, 771 lines)
**Educational Impact:** Demonstrates quality-gated workflows that never block while maintaining high output standards
