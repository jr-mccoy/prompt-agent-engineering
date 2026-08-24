# Technique Analysis: mermaid-tools

**Resource Type:** Skill
**Path:** `skills/document-processing/mermaid-tools/`
**Date Analyzed:** 2025-12-22
**Bundled Resources:** 3 scripts (orchestrator, extractor, config), 1 reference (setup guide)
**Total Lines Analyzed:** ~298 lines (164 SKILL.md + 134 extract_diagrams.py)

---

## Executive Summary

This is a **self-contained diagram generation tool** that extracts Mermaid diagrams from markdown and generates high-quality PNGs. It demonstrates context-aware naming, smart sizing based on diagram type, and a fully bundled script ecosystem requiring minimal external setup.

**Key Innovation:** Context-aware naming algorithm that analyzes surrounding markdown to generate meaningful diagram filenames (e.g., "01-caching-architecture" instead of "diagram-01").

**Complexity:** 4/5 (High - NLP-based naming, smart sizing, orchestration, bundled dependencies)

---

## Identified Techniques

### Technique 1: Context-Aware Naming Algorithm (NEW)
- **Category:** DS (Domain-Specific)
- **Pattern:** Analyze surrounding text context to generate intelligent names
- **Example from resource:**
  ```python
  # Look backwards for specific diagram descriptions
  for line in reversed(context_lines):
      line = line.strip().lower()
      if 'system architecture' in line:
          diagram_name = f"{i:02d}-system-architecture"
          break
      elif 'authentication flow' in line:
          diagram_name = f"{i:02d}-authentication-flow"
          break
  ```
- **Maps to existing:** NEW (DS-43)
- **Effectiveness:** Produces meaningful filenames automatically; improves organization

### Technique 2: Diagram-Type Smart Sizing (NEW)
- **Category:** DS (Domain-Specific)
- **Pattern:** Adjust output dimensions based on detected content type
- **Example from resource:**
  ```markdown
  The script automatically adjusts dimensions based on diagram type:
  - **Timeline/Gantt**: 2400×400 (wide and short)
  - **Architecture/System/Caching**: 2400×1600 (large and detailed)
  - **Monitoring/Workflow/Sequence/API**: 2400×800 (wide for process flows)
  - **Default**: 1200×800 (standard size)
  ```
- **Maps to existing:** NEW (DS-44)
- **Effectiveness:** Optimizes visual quality per diagram type; no manual sizing needed

### Technique 3: Self-Contained Script Package (NEW)
- **Category:** IT (Interaction)
- **Pattern:** Bundle all dependencies (scripts, configs) in single directory
- **Example from resource:**
  ```markdown
  ### scripts/
  - **extract-and-generate.sh** - Main orchestrator
  - **extract_diagrams.py** - Python extraction logic
  - **puppeteer-config.json** - Browser configuration

  All scripts must be run from the `scripts/` directory to properly locate dependencies.
  ```
- **Maps to existing:** NEW (IT-24)
- **Effectiveness:** Portability; single skill directory contains everything needed

### Technique 4: Priority-Based Context Detection (NEW)
- **Category:** DS (Domain-Specific)
- **Pattern:** Tiered heuristics for information extraction
- **Example from resource:**
  ```python
  # Priority 1: Look for specific diagram descriptions
  for line in reversed(context_lines):
      if 'system architecture' in line:
          diagram_name = f"{i:02d}-system-architecture"
          break

  # Priority 2: Look for section headers (## or ###)
  if diagram_name.startswith('diagram-'):
      for line in reversed(context_lines):
          if line.startswith('###') or line.startswith('##'):
              # Extract header text
  ```
- **Maps to existing:** NEW (DS-45)
- **Effectiveness:** Falls back gracefully; tries specific matches before generic

### Technique 5: Environment Variable Configuration
- **Category:** IT (Interaction - existing)
- **Pattern:** Allow runtime customization without editing code
- **Example from resource:**
  ```bash
  MERMAID_WIDTH=1600 MERMAID_HEIGHT=1200 ./extract-and-generate.sh "<markdown_file>"
  ```
- **Maps to existing:** IT-09 (Configuration Patterns) - enhanced with multiple variables
- **Effectiveness:** Override defaults per invocation; no config file editing

### Technique 6: Sequential Numbering for Ordering
- **Category:** DS (Domain-Specific)
- **Pattern:** Prefix outputs with sequence numbers to preserve document order
- **Example from resource:**
  ```markdown
  For each diagram, the script generates:
  - `01-diagram-name.mmd` - Extracted Mermaid code
  - `01-diagram-name.png` - High-resolution PNG image

  The numbering ensures diagrams maintain their order from the source document.
  ```
- **Maps to existing:** DS-04 (Ordering/Sequencing)
- **Effectiveness:** Maintains logical flow; prevents alphabetical scrambling

### Technique 7: Multi-Phase Orchestration Script
- **Category:** DS (Domain-Specific - existing)
- **Pattern:** Main script coordinates multiple sub-processes
- **Example from resource:**
  ```markdown
  ### What the Script Does
  1. **Extracts** all Mermaid code blocks from the markdown file
  2. **Numbers** them sequentially (01, 02, 03, etc.)
  3. **Generates** `.mmd` files for each diagram
  4. **Creates** high-resolution PNG images with smart sizing
  5. **Validates** all generated PNG files
  ```
- **Maps to existing:** DS-11 (Multi-Stage Workflows)
- **Effectiveness:** Each phase validates before next; clear failure points

### Technique 8: Scale Factor for Quality Control
- **Category:** DS (Domain-Specific)
- **Pattern:** Separate resolution from dimensions using scale multiplier
- **Example from resource:**
  ```bash
  # Base: 1200×800
  # MERMAID_SCALE=2: Output 2400×1600 (2x resolution, high DPI)
  # MERMAID_SCALE=5: Output 6000×4000 (print quality)
  ```
- **Maps to existing:** DS-09 (Performance/Quality Optimization)
- **Effectiveness:** Independent control of size vs. resolution; print-ready output

### Technique 9: Lookback Window for Context
- **Category:** DS (Domain-Specific - NEW)
- **Pattern:** Analyze N lines before target to extract context
- **Example from resource:**
  ```python
  # Look for context clues in the 20 lines before the diagram
  context_start = max(0, lines_before - 20)
  context_lines = lines[context_start:lines_before]
  ```
- **Maps to existing:** NEW (DS-46)
- **Effectiveness:** Limited search scope improves performance; captures relevant context

### Technique 10: Prerequisite Verification Guidance
- **Category:** IT (Interaction - existing)
- **Pattern:** Provide verification commands for dependencies
- **Example from resource:**
  ```markdown
  ## Prerequisites Verification
  1. **mermaid-cli**: `mmdc --version`
  2. **Google Chrome**: `google-chrome-stable --version`
  3. **Python 3**: `python3 --version`
  ```
- **Maps to existing:** DS-10 (Tool Integration Patterns)
- **Effectiveness:** Users can self-diagnose; clear requirement checklist

---

## Novel Patterns (Not in MASTER_TECHNIQUE_INDEX)

### Pattern 1: DS-43 - Context-Aware Naming Algorithm
- **Description:** Analyze surrounding text (markdown headers, keywords) to generate meaningful names for extracted artifacts
- **Implementation:** Lookback window + priority-based keyword matching + fallback to headers
- **Use case:** Diagram extraction, code snippet extraction, test generation, documentation generation
- **Example:** "Extract diagram → Look back 20 lines → Find 'authentication flow' → Name: 01-authentication-flow"
- **Proposed category:** DS (Domain-Specific)
- **Proposed code:** DS-43

### Pattern 2: DS-44 - Diagram-Type Smart Sizing
- **Description:** Automatically adjust output dimensions based on detected content type/purpose
- **Implementation:** Pattern matching on names/content → Dimension lookup table → Apply sizing
- **Use case:** Diagram generation, image processing, layout optimization, responsive design
- **Example:** "Timeline → 2400×400 (wide+short) | Architecture → 2400×1600 (large+detailed)"
- **Proposed category:** DS (Domain-Specific)
- **Proposed code:** DS-44

### Pattern 3: IT-24 - Self-Contained Script Package
- **Description:** Bundle all scripts and configurations in single directory; no external path dependencies
- **Implementation:** Co-locate all files, use relative paths, enforce execution from package directory
- **Use case:** Portable tools, skill packaging, plugin systems, deployable utilities
- **Example:** "scripts/ contains: orchestrator.sh + extractor.py + config.json (all relative paths)"
- **Proposed category:** IT (Interaction)
- **Proposed code:** IT-24

### Pattern 4: DS-45 - Priority-Based Context Detection
- **Description:** Tiered heuristics for extracting information from context (specific → general)
- **Implementation:** Try high-confidence matches first, fall back to broader patterns
- **Use case:** NLP extraction, intent detection, categorization, name generation
- **Example:** "Priority 1: Specific keywords | Priority 2: Section headers | Priority 3: Default"
- **Proposed category:** DS (Domain-Specific)
- **Proposed code:** DS-45

### Pattern 5: DS-46 - Lookback Window for Context
- **Description:** Analyze fixed number of lines/tokens before target to extract context
- **Implementation:** Define window size (e.g., 20 lines), extract before target, analyze backwards
- **Use case:** Documentation generation, code analysis, context extraction, semantic naming
- **Example:** "Extract diagram at line 100 → Analyze lines 80-100 → Find relevant context"
- **Proposed category:** DS (Domain-Specific)
- **Proposed code:** DS-46

---

## Multi-Technique Combinations

### Combination 1: Lookback Window + Priority Detection
Lookback window (DS-46) provides context, priority detection (DS-45) extracts best match.

**Effectiveness:** Limited search scope + smart matching = fast + accurate naming.

### Combination 2: Context-Aware Naming + Sequential Numbering
Context naming (DS-43) generates descriptive names, sequential numbering (DS-04) preserves order.

**Effectiveness:** Both meaningful names AND logical ordering.

### Combination 3: Smart Sizing + Environment Variables
Smart sizing (DS-44) provides intelligent defaults, env vars (IT-09) allow overrides.

**Effectiveness:** Automation with escape hatch for special cases.

### Combination 4: Self-Contained Package + Multi-Phase Orchestration
Self-contained package (IT-24) bundles dependencies, orchestration (DS-11) coordinates execution.

**Effectiveness:** Portability + reliability; everything needed in one place.

### Combination 5: Scale Factor + Smart Sizing
Smart sizing (DS-44) optimizes dimensions, scale factor multiplies for resolution.

**Effectiveness:** Independent control of layout vs. quality.

---

## Notes for Integration

### 1. Context-Aware Naming as Universal Pattern
DS-43 should be applied to other extraction tasks:
- **Code extraction**: Generate function names from comments
- **Test generation**: Name tests based on test case descriptions
- **Documentation**: Generate section titles from surrounding text
- **Screenshot automation**: Name images based on page title/context

### 2. Smart Sizing for Content Types
DS-44 generalizes to "Content-Type Optimization":
- **Videos**: Aspect ratio by platform (Instagram, YouTube, TikTok)
- **Images**: Dimensions by use case (thumbnail, hero, gallery)
- **Code blocks**: Line length by language (Python: 79, Java: 120)
- **Documents**: Page size by region (Letter vs. A4)

### 3. Self-Contained Package Best Practices
IT-24 pattern for skill packaging:
- **Co-locate dependencies**: All scripts + configs in skills/<name>/scripts/
- **Relative paths only**: No absolute paths to external resources
- **Execution from package dir**: Document "cd to scripts/ first"
- **Bundled configs**: Don't rely on system configs

### 4. Priority-Based Detection Framework
DS-45 template for tiered extraction:
```
Priority 1: High-confidence patterns (exact matches)
Priority 2: Medium-confidence patterns (headers, structure)
Priority 3: Low-confidence patterns (defaults, inference)
Priority 4: Fallback (generic names, error handling)
```

### 5. Lookback Window Sizing Guidelines
DS-46 guidelines for window size selection:
- **Code context**: 10-20 lines (captures function + docstring)
- **Documentation context**: 20-50 lines (captures section)
- **Conversational context**: 3-5 messages (captures topic)
- **Log context**: 50-100 lines (captures event sequence)

### 6. Environment Variable Configuration Pattern
Standard env var pattern for skills:
```bash
SKILL_WIDTH=value    # Dimension/size
SKILL_HEIGHT=value   # Dimension/size
SKILL_SCALE=value    # Multiplier/factor
SKILL_QUALITY=value  # Quality setting
SKILL_FORMAT=value   # Output format
```

---

## Real-World Usage

From mermaid-tools/SKILL.md:
- Lines 1-48: Core workflow and output structure
- Lines 49-77: Advanced usage with env var overrides
- Lines 79-88: Smart sizing feature documentation
- Lines 91-106: Critical usage principles

From scripts/extract_diagrams.py:
- Lines 10-48: Extraction logic with error handling
- Lines 49-99: Context-aware naming algorithm (Priority 1 + Priority 2)
- Lines 100-123: File creation with sequential numbering

---

## Summary

**mermaid-tools** is a self-contained diagram generation tool demonstrating intelligent content processing. It introduces **5 novel techniques** focused on:

1. **Context-aware naming** (DS-43: NLP-based filename generation)
2. **Smart sizing** (DS-44: Content-type dimension optimization)
3. **Self-contained packaging** (IT-24: Bundled dependencies)
4. **Priority-based detection** (DS-45: Tiered heuristics)
5. **Lookback window** (DS-46: Fixed-size context analysis)

**Key Insight:** Automation can be intelligent—don't just extract, analyze context and optimize. The combination of context-aware naming + smart sizing eliminates two manual steps users typically perform.

**Recommendation:** Apply context-aware naming (DS-43) to any extraction/generation task where meaningful names improve usability. The pattern is broadly applicable beyond diagram generation.

**Bundled Resources Value:** The 3 scripts form a complete ecosystem: orchestrator coordinates, extractor analyzes, config optimizes. This demonstrates how bundled scripts should work together as a cohesive tool.

**NLP-Lite Pattern:** Lines 56-99 show "NLP-lite" - simple keyword matching and pattern recognition that achieves 80% of NLP value with 5% of complexity. Good pattern for practical automation.
