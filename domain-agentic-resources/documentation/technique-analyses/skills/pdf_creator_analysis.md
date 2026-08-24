# Technique Analysis: pdf-creator

**Resource Type:** Skill
**Path:** `claude-code-resources/skills/document-processing/pdf-creator/`
**Date Analyzed:** 2025-12-22
**Bundled Resources:** 340 lines (2 scripts: md_to_pdf.py, batch_convert.py)
**Complexity:** 4/5 (Production tool with i18n typography and batch processing)

## Overview

The `pdf-creator` skill provides professional PDF generation from markdown with proper Chinese font support. It demonstrates sophisticated internationalization (i18n) patterns, font fallback chains, and dual-mode operation (single file vs. batch processing).

**Key Innovation:** Typography-first approach with Chinese font fallback chains embedded in CSS, designed for formal legal/business documents with file size constraints.

## Identified Techniques

### Technique 1: Font Fallback Chain for i18n
- **Category:** DS (Domain-Specific - Typography/Internationalization)
- **Pattern:** Ordered list of fonts from most-preferred to universal fallback
- **Example from resource:**
```python
font-family: 'Songti SC', 'SimSun', 'STSong', 'Noto Serif CJK SC', serif;
# Primary (macOS) → Windows → Generic macOS → Open source → Universal
```
- **Maps to existing:** NEW - **DS-104 Font Fallback Chain for i18n**
- **Effectiveness:** Ensures Chinese characters render correctly across macOS, Windows, Linux

### Technique 2: Dual-Mode CLI (Single + Batch)
- **Category:** DS (Domain-Specific - CLI Design)
- **Pattern:** Two scripts with shared core: simple CLI for single files, argparse CLI for batch
- **Example from resource:**
```bash
# Single file mode
python md_to_pdf.py input.md output.pdf

# Batch mode
python batch_convert.py *.md --output-dir ./pdfs
```
- **Maps to existing:** Extends **IT-25 Multi-Mode Interactive CLI** → **DS-105 Dual-Mode CLI Pattern**
- **Effectiveness:** Users start simple, graduate to batch when needed; shared core prevents duplication

### Technique 3: Typography Specification Table
- **Category:** OT (Output Techniques)
- **Pattern:** Structured table defining font choices with semantic meaning
- **Example from resource:**
```markdown
| Font Type | Primary | Fallbacks |
|-----------|---------|-----------|
| Body text | Songti SC | SimSun, STSong, Noto Serif CJK SC |
| Headings | Heiti SC | SimHei, STHeiti, Noto Sans CJK SC |
```
- **Maps to existing:** NEW - **OT-15 Typography Specification Table**
- **Effectiveness:** Documents font decisions; users understand why each font is chosen

### Technique 4: Output Specifications Section
- **Category:** OT (Output Techniques)
- **Pattern:** Explicit list of output constraints and specifications
- **Example from resource:**
```markdown
- **Page size**: A4
- **Margins**: 2.5cm top/bottom, 2cm left/right
- **Body font**: 12pt, 1.8 line height
- **Max file size**: Designed to stay under 2MB for form submissions
```
- **Maps to existing:** Extends **OT-14 Output Artifacts Specification** → **OT-16 Output Constraints Specification**
- **Effectiveness:** Sets expectations; file size constraint drives typography choices (10pt tables, fixed layout)

### Technique 5: Environment Setup Prerequisites
- **Category:** DS (Domain-Specific - Environment Configuration)
- **Pattern:** Platform-specific environment variables required before execution
- **Example from resource:**
```markdown
## macOS Environment Setup

If encountering library errors, set these environment variables first:

```bash
export DYLD_LIBRARY_PATH="/opt/homebrew/lib:$DYLD_LIBRARY_PATH"
export PKG_CONFIG_PATH="/opt/homebrew/lib/pkgconfig:$PKG_CONFIG_PATH"
```
- **Maps to existing:** NEW - **DS-106 Environment Setup Prerequisites**
- **Effectiveness:** Prevents "library not found" errors; documents platform-specific requirements

### Technique 6: Semantic Typography Hierarchy
- **Category:** DS (Domain-Specific - Typography)
- **Pattern:** Different font families for different semantic elements (body text vs. headings)
- **Example from resource:**
```css
/* Serif for body text (traditional, readable) */
body { font-family: 'Songti SC', ..., serif; }

/* Sans-serif for headings (modern, clear) */
h1, h2, h3 { font-family: 'Heiti SC', ..., sans-serif; }
```
- **Maps to existing:** NEW - **DS-107 Semantic Typography Hierarchy**
- **Effectiveness:** Professional appearance; follows Chinese typography conventions

### Technique 7: Use Case-Driven Documentation
- **Category:** IT (Interaction Techniques)
- **Pattern:** Organize documentation by specific use cases rather than features
- **Example from resource:**
```markdown
## Common Use Cases

1. **Legal documents**: Trademark filings, contracts, evidence lists
2. **Reports**: Business reports, technical documentation
3. **Formal letters**: Official correspondence requiring print format
```
- **Maps to existing:** Extends **IT-11 Use Case Examples** → **IT-37 Use Case-Driven Documentation**
- **Effectiveness:** Users find their scenario, understand if tool fits their needs

### Technique 8: Module Import Reuse Pattern
- **Category:** DS (Domain-Specific - Python Architecture)
- **Pattern:** Batch script imports and reuses core conversion function from single-file script
- **Example from resource:**
```python
# batch_convert.py
from md_to_pdf import markdown_to_pdf

# Uses existing function instead of duplicating conversion logic
markdown_to_pdf(str(md_path), pdf_file)
```
- **Maps to existing:** **AG-19 Production App as Skill** (modular architecture)
- **Effectiveness:** DRY principle; single source of truth for conversion logic

### Technique 9: Success/Failure Counters in Batch Operations
- **Category:** QA (Quality Assurance)
- **Pattern:** Track success and failure counts, report summary, exit with appropriate code
- **Example from resource:**
```python
success = 0
failed = 0

for md_file in args.files:
    try:
        # ... conversion logic ...
        success += 1
    except Exception as e:
        print(f"[ERROR] Failed to convert {md_file}: {e}")
        failed += 1

print(f"\nCompleted: {success} succeeded, {failed} failed")
sys.exit(0 if failed == 0 else 1)
```
- **Maps to existing:** NEW - **QA-26 Success/Failure Counters in Batch Operations**
- **Effectiveness:** Users see progress; exit code enables CI/CD integration

### Technique 10: Markdown Extensions Configuration
- **Category:** DS (Domain-Specific - Markdown Processing)
- **Pattern:** Explicit list of markdown extensions for feature support
- **Example from resource:**
```python
html_content = markdown.markdown(
    md_content,
    extensions=['tables', 'fenced_code', 'codehilite', 'toc']
)
```
- **Maps to existing:** NEW - **DS-108 Markdown Extensions Configuration**
- **Effectiveness:** Documents which markdown features are supported (tables, code blocks, TOC)

## Novel Patterns (Not in MASTER_TECHNIQUE_INDEX)

### Pattern 1: Font Fallback Chain for i18n (DS-104)
- **Description:** Ordered list of fonts from platform-specific to universal, ensuring cross-platform rendering
- **Implementation:**
  - Primary: Platform-native font (best quality)
  - Secondary: Alternative platform font
  - Tertiary: Generic platform font
  - Quaternary: Open-source universal font
  - Fallback: Generic font family (serif, sans-serif)
- **Use case:** Any i18n application with typography requirements (PDFs, web apps, documents)
- **Example:** Arabic text rendering, Japanese typography, Cyrillic fonts
- **Proposed category:** DS (Domain-Specific - Typography/Internationalization)
- **Proposed code:** DS-104

### Pattern 2: Dual-Mode CLI Pattern (DS-105)
- **Description:** Two scripts with shared core: simple CLI for single operations, argparse CLI for batch
- **Implementation:**
  - `core_tool.py`: Main logic as importable function
  - Simple CLI: Positional args only, minimal interface
  - Batch CLI: Imports core function, adds --output-dir, glob patterns, error handling
- **Use case:** Any CLI tool that needs simple + advanced modes (image processing, file conversion, data transformation)
- **Example:** Image resizing (single image vs. batch), CSV conversion, code formatting
- **Proposed category:** DS (Domain-Specific - CLI Design)
- **Proposed code:** DS-105

### Pattern 3: Typography Specification Table (OT-15)
- **Description:** Structured table defining font choices with semantic meaning
- **Implementation:**
  - Column 1: Font type/semantic purpose
  - Column 2: Primary font choice
  - Column 3: Fallback fonts
- **Use case:** Design systems, typography documentation, PDF generation, printing workflows
- **Example:** Brand guidelines, web design systems, publishing platforms
- **Proposed category:** OT (Output Techniques)
- **Proposed code:** OT-15

### Pattern 4: Output Constraints Specification (OT-16)
- **Description:** Explicit list of output constraints (file size, dimensions, format)
- **Implementation:**
  - Physical constraints (page size, margins, DPI)
  - Typography constraints (font size, line height)
  - File constraints (max size, format version)
  - Rationale for each constraint
- **Use case:** Document generation, image processing, video encoding, data export
- **Example:** Email attachment limits, form submission size limits, printing specifications
- **Proposed category:** OT (Output Techniques)
- **Proposed code:** OT-16

### Pattern 5: Environment Setup Prerequisites (DS-106)
- **Description:** Platform-specific environment variables required before tool execution
- **Implementation:**
  - Section titled "Environment Setup" or "Prerequisites"
  - Platform identifier (macOS, Linux, Windows)
  - Export commands ready to copy-paste
  - Trigger conditions ("If encountering X error...")
- **Use case:** Any tool with native library dependencies (databases, image processing, ML frameworks)
- **Example:** PostgreSQL client setup, CUDA configuration, native module compilation
- **Proposed category:** DS (Domain-Specific - Environment Configuration)
- **Proposed code:** DS-106

### Pattern 6: Semantic Typography Hierarchy (DS-107)
- **Description:** Different font families for different semantic elements
- **Implementation:**
  - Body text: Serif fonts (traditional, readable)
  - Headings: Sans-serif fonts (modern, clear)
  - Code: Monospace fonts (technical, precise)
  - Apply consistently across all elements
- **Use case:** Typography design, document generation, web design, publishing
- **Example:** Legal documents, academic papers, technical manuals
- **Proposed category:** DS (Domain-Specific - Typography)
- **Proposed code:** DS-107

### Pattern 7: Use Case-Driven Documentation (IT-37)
- **Description:** Organize documentation by specific use cases rather than by features
- **Implementation:**
  - Section: "Common Use Cases"
  - Each use case: Name + description
  - Map use cases to features/commands
- **Use case:** Product documentation, API docs, framework guides
- **Example:** "Building a REST API", "Creating a dashboard", "Processing payments"
- **Proposed category:** IT (Interaction Techniques)
- **Proposed code:** IT-37

### Pattern 8: Success/Failure Counters in Batch Operations (QA-26)
- **Description:** Track and report success/failure counts in batch operations
- **Implementation:**
  - Initialize counters: `success = 0; failed = 0`
  - Increment in try/except blocks
  - Report summary: "Completed: X succeeded, Y failed"
  - Exit code based on failures: `sys.exit(0 if failed == 0 else 1)`
- **Use case:** Batch processing, data migrations, test runners, CI/CD pipelines
- **Example:** Batch file conversion, database migration, multi-repo operations
- **Proposed category:** QA (Quality Assurance)
- **Proposed code:** QA-26

### Pattern 9: Markdown Extensions Configuration (DS-108)
- **Description:** Explicit list of markdown extensions for feature support
- **Implementation:**
  - Use markdown library with extension support
  - List extensions explicitly in code
  - Document which features are enabled
- **Use case:** Markdown processing, static site generators, documentation tools
- **Example:** Table support, syntax highlighting, footnotes, TOC generation
- **Proposed category:** DS (Domain-Specific - Markdown Processing)
- **Proposed code:** DS-108

## Multi-Technique Combinations

The `pdf-creator` skill demonstrates sophisticated combination of techniques:

1. **Font Fallback + Typography Hierarchy:**
   - Font Fallback Chain ensures Chinese rendering
   - Semantic Typography Hierarchy applies different fonts to body/headings
   - Result: Professional Chinese typography across platforms

2. **Dual-Mode CLI + Success Counters:**
   - Dual-Mode pattern provides simple + batch interfaces
   - Success/Failure Counters enable batch monitoring
   - Result: Scalable from 1 file to 1000 files

3. **Output Constraints + Use Cases:**
   - Output Constraints Specification defines file size limit (2MB)
   - Use Case-Driven Documentation explains why (form submissions)
   - Result: Users understand design decisions

4. **Environment Prerequisites + Typography Spec:**
   - Environment Setup documents macOS library paths
   - Typography Table documents font requirements
   - Result: Complete setup guide for production use

5. **Module Reuse + Batch Processing:**
   - Module Import Reuse prevents duplication
   - Batch script wraps core function with counters
   - Result: Maintainable architecture (single conversion logic)

## Integration Notes

### For MASTER_TECHNIQUE_INDEX.md:
1. **Add 9 new techniques:**
   - DS-104: Font Fallback Chain for i18n
   - DS-105: Dual-Mode CLI Pattern
   - OT-15: Typography Specification Table
   - OT-16: Output Constraints Specification
   - DS-106: Environment Setup Prerequisites
   - DS-107: Semantic Typography Hierarchy
   - IT-37: Use Case-Driven Documentation
   - QA-26: Success/Failure Counters in Batch Operations
   - DS-108: Markdown Extensions Configuration

2. **Create new subcategories:**
   - "Typography" (DS-104, DS-107, OT-15)
   - "CLI Design" (DS-105)
   - "Markdown Processing" (DS-108)

3. **Cross-reference existing techniques:**
   - IT-25 (Multi-Mode Interactive CLI) → DS-105 extends to dual-script pattern
   - AG-19 (Production App as Skill) → Module reuse architecture

### For USE_CASE_LOOKUP.md:
- Add "Document Generation" use case
- Recommended techniques: DS-104, DS-105, OT-15, OT-16, DS-107, QA-26

### For AI_AGENT_QUICK_START.md:
- Add example in Section 5: "i18n typography with font fallback chains"
- Demonstrate Dual-Mode CLI pattern for scalability

## Summary

**Complexity Rating:** 4/5

The `pdf-creator` skill is a **production-ready document generation tool** with internationalization support (Chinese typography), designed for formal legal/business documents with file size constraints.

**Key Strengths:**
1. **i18n-first approach:** Font fallback chains ensure cross-platform Chinese rendering
2. **Scalable architecture:** Dual-mode CLI (single → batch) with shared core
3. **Production-ready:** File size constraints, error handling, success counters
4. **Typography excellence:** Semantic hierarchy (serif body, sans headings) following conventions

**Novel Contributions:**
- Font Fallback Chain for i18n (DS-104): Universal pattern for multi-platform typography
- Dual-Mode CLI Pattern (DS-105): Scalable CLI design for single → batch workflows
- Output Constraints Specification (OT-16): Document file size/format limits with rationale
- Success/Failure Counters (QA-26): Batch operation monitoring for CI/CD

**Recommended Integration Priority:** HIGH
- DS-104 (Font Fallback Chain): Critical for any i18n typography work
- DS-105 (Dual-Mode CLI): Excellent pattern for CLI tool scalability
- QA-26 (Success/Failure Counters): Standard for batch operations

**Lines of Bundled Knowledge:** 340 lines
- SKILL.md: 62 lines
- scripts/md_to_pdf.py: 199 lines (core converter with CSS)
- scripts/batch_convert.py: 79 lines (batch wrapper)

**Production Readiness:** 5/5 - Designed for legal document submissions (trademark filings), includes file size constraints, error handling, batch processing, and cross-platform support
