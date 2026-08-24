# Technique Analysis: llm-icon-finder

**Resource Type:** Skill
**Path:** `skills/llm-application-dev/llm-icon-finder/`
**Date Analyzed:** 2025-12-22
**Category:** LLM Application Development - Asset Discovery
**Bundled Resources:** 2 references (icons-list.md: 88 lines, developer-info.md: 48 lines)
**Total Knowledge:** ~179 lines
**Complexity:** 3/5 (Knowledge base with API integration patterns)

---

## Resource Summary

**Purpose:** Enable Claude to find and access AI/LLM model brand icons from the lobe-icons library. Supports 100+ icons for models (Claude, GPT, Gemini), providers (OpenAI, Anthropic, Google), and applications, with multi-language support (English/Chinese).

**Key Innovation:** URL pattern templates + cross-language entity mapping + fallback strategies

**Architecture:**
- **SKILL.md (91 lines):** Core workflow, URL patterns, troubleshooting
- **references/icons-list.md (88 lines):** Comprehensive icon catalog organized by category
- **references/developer-info.md (48 lines):** npm installation and React usage examples

**Use Case:** When users request AI/LLM brand icons, need icon URLs, want to download logos, or query in Chinese for Chinese AI providers.

---

## Identified Techniques

### Technique 1: URL Pattern Templates
- **Category:** DS (Domain-Specific) - NEW
- **Pattern:** Provide URL construction templates with placeholders for dynamic generation
- **Example from resource:**
```markdown
# SVG
https://raw.githubusercontent.com/lobehub/lobe-icons/refs/heads/master/packages/static-svg/{light|dark}/{icon-name}.svg

# PNG
https://raw.githubusercontent.com/lobehub/lobe-icons/refs/heads/master/packages/static-png/{light|dark}/{icon-name}.png
```
- **Maps to existing:** NEW - **DS-50: URL Pattern Templates**
- **Effectiveness:** Enables Claude to construct valid CDN URLs dynamically without hardcoding every possibility. Uses placeholder syntax {light|dark} to show variants.

### Technique 2: Multi-Language Entity Mapping
- **Category:** IT (Interaction Techniques) - NEW
- **Pattern:** Map cross-language queries to canonical identifiers
- **Example from resource:**
```markdown
**Chinese AI models**: Support Chinese queries (e.g., "智谱" → `chatglm`, "月之暗面" → `moonshot`)

| Icon Name | Chinese Name | Description |
|-----------|--------------|-------------|
| `chatglm` | 智谱清言 | ChatGLM |
| `moonshot` | 月之暗面 | Moonshot (Kimi) |
| `baichuan` | 百川 | Baichuan |
```
- **Maps to existing:** NEW - **IT-28: Multi-Language Entity Mapping**
- **Effectiveness:** Enables Claude to understand Chinese queries and map them to English icon identifiers. Critical for Chinese AI ecosystem (Moonshot, Zhipu, Baichuan, etc.).

### Technique 3: Fallback Strategy Pattern
- **Category:** DS (Domain-Specific) - NEW
- **Pattern:** Provide progressive fallback strategies with increasing generality
- **Example from resource:**
```markdown
## Troubleshooting

If URL returns 404:
1. Try `-color` suffix variant
2. Check alternate naming (e.g., `chatgpt` vs `gpt`, `google` vs `gemini`)
3. Direct user to https://lobehub.com/icons to browse
4. Search repository: https://github.com/lobehub/lobe-icons
```
- **Maps to existing:** NEW - **DS-51: Fallback Strategy Pattern**
- **Effectiveness:** Handles uncertainty gracefully. Each fallback level increases scope: variant suffix → alternate names → web browse → full search.

### Technique 4: Reference Catalog Pattern
- **Category:** IT (Interaction Techniques) - NEW
- **Pattern:** Extensive catalog in bundled reference for quick lookup, organized by category
- **Example from resource:**
```markdown
# Common AI/LLM Icons Reference

## Models
| Icon Name | Description |
|-----------|-------------|
| `claude` | Anthropic Claude |
| `chatgpt` | ChatGPT |
| `gemini` | Google Gemini |
...

## Providers
| Icon Name | Description |
|-----------|-------------|
| `openai` | OpenAI |
| `anthropic` | Anthropic |
...

## Applications
| Icon Name | Description |
|-----------|-------------|
| `lobechat` | LobeChat |
| `comfyui` | ComfyUI |
...
```
- **Maps to existing:** NEW - **IT-29: Reference Catalog Pattern**
- **Effectiveness:** Reduces need for external searches. Categorized organization (Models/Providers/Applications) matches user mental models. 100+ icons indexed.

### Technique 5: Convention Documentation
- **Category:** DS (Domain-Specific) - NEW
- **Pattern:** Document naming conventions and variant patterns to enable inference
- **Example from resource:**
```markdown
**Icon naming convention**: Lowercase, hyphenated (e.g., `claude`, `chatglm`, `openai`, `huggingface`)

## Tips for Finding Icons

1. **Icon naming**: Usually lowercase, hyphenated (e.g., `anthropic`, `chatglm`)
2. **Company vs Product**: Some have both (e.g., `alibaba` and `alibabacloud`, `zhipu` and `chatglm`)
3. **Color variants**: Many icons have `-color` suffix for colored versions
```
- **Maps to existing:** NEW - **DS-52: Convention Documentation**
- **Effectiveness:** Enables Claude to infer likely icon names even when not in catalog. Example: If asked for "Stability AI", can infer `stability` following lowercase convention.

### Technique 6: Example-Driven Workflow
- **Category:** IT (Interaction Techniques) - EXISTING
- **Pattern:** Show concrete examples for each use case with expected inputs and outputs
- **Example from resource:**
```markdown
## Examples

**Single icon request**:
User: "Claude icon"
→ Provide: https://raw.githubusercontent.com/lobehub/lobe-icons/refs/heads/master/packages/static-png/dark/claude.png
→ Also mention color variant and web viewer link

**Multiple icons download**:
curl -o openai.svg "https://raw.githubusercontent.com/lobehub/lobe-icons/.../dark/openai.svg"
curl -o anthropic.svg "https://raw.githubusercontent.com/lobehub/lobe-icons/.../dark/anthropic.svg"

**Chinese query**:
User: "找一下智谱的图标"
→ Identify: 智谱 = ChatGLM → icon name: chatglm
→ Provide URLs and mention related icons (zhipu, codegeex)
```
- **Maps to existing:** ST-04 (Few-Shot Examples) or IT-06 (Workflow Examples)
- **Effectiveness:** Shows expected format and behavior for single/multiple/Chinese queries. Demonstrates the thought process (Identify → Construct URL → Provide extras).

### Technique 7: Three-Tier Progressive Loading
- **Category:** IT (Interaction Techniques) - EXISTING
- **Pattern:** Metadata → Core → References
- **Example from resource:**
- Tier 1: `description` (when to use this skill)
- Tier 2: SKILL.md (URL patterns, workflow, troubleshooting)
- Tier 3: references/ (comprehensive icon catalog, developer info)
- **Maps to existing:** IT-19 (from previous analysis)
- **Effectiveness:** Skill description is tiny (1 line), core is focused (91 lines), detailed catalog loaded only when needed (136 lines in references).

### Technique 8: Multi-Format Support Documentation
- **Category:** DS (Domain-Specific) - EXISTING
- **Pattern:** Document all supported formats with format-specific guidance
- **Example from resource:**
```markdown
## Icon Formats and Variants

**Available formats**: SVG (scalable), PNG (raster), WEBP (compressed)
**Theme variants**: light, dark, and color (some icons)
```
- **Maps to existing:** DS-07 (Output Format Specification) - variation for inputs
- **Effectiveness:** Clear enumeration of formats (SVG/PNG/WEBP) and variants (light/dark/color). Guides format selection based on use case.

---

## Novel Patterns (Not in MASTER_TECHNIQUE_INDEX)

### Pattern 1: URL Pattern Templates (DS-50)

**Description:** Provide URL construction templates with placeholders ({var}) that enable dynamic URL generation without hardcoding.

**Implementation:**
```markdown
# Pattern template
https://base.url/{option1|option2}/{parameter}.{extension}

# Concrete example
https://raw.githubusercontent.com/.../packages/static-{format}/{light|dark}/{icon-name}.{svg|png|webp}
```

**Use case:**
- API endpoint construction
- CDN URL generation
- File path templates
- Query string patterns

**Why it's novel:** Combines URL patterns with inline option notation ({light|dark}). More compact than listing all variations. Teaches Claude the construction logic, not just the results.

**Proposed category:** DS (Domain-Specific - API Integration)
**Proposed code:** DS-50

---

### Pattern 2: Multi-Language Entity Mapping (IT-28)

**Description:** Map cross-language queries (especially Chinese ↔ English) to canonical identifiers to support multilingual discovery.

**Implementation:**
```markdown
| Icon Name | Chinese Name | English Name |
|-----------|--------------|--------------|
| `chatglm` | 智谱清言 | ChatGLM |
| `moonshot` | 月之暗面 | Moonshot (Kimi) |
| `baichuan` | 百川 | Baichuan |

**Usage:** Chinese queries (e.g., "智谱") → lookup table → canonical ID (`chatglm`)
```

**Use case:**
- Chinese AI ecosystem navigation
- Cross-language product/company lookup
- Localized brand name resolution
- Multilingual knowledge bases

**Why it's novel:** Not just translation - maps colloquial Chinese names to English technical IDs. Example: "月之暗面" (Dark Side of the Moon, literal) → `moonshot` (Kimi brand) shows understanding of brand context.

**Proposed category:** IT (Interaction Techniques - Multilingual Support)
**Proposed code:** IT-28

---

### Pattern 3: Fallback Strategy Pattern (DS-51)

**Description:** Provide progressive fallback strategies with increasing generality when primary approach fails.

**Implementation:**
```markdown
If [primary approach] fails:
1. Try [specific variant] (narrow scope)
2. Try [alternate naming] (medium scope)
3. Browse [web interface] (wide scope)
4. Search [full repository] (widest scope)
```

**Use case:**
- API 404 handling
- File not found recovery
- Fuzzy matching strategies
- Discovery workflows

**Why it's novel:** Structured escalation from specific to general. Each level increases cost (cognitive or computational) but also increases likelihood of success. Prevents premature escalation to expensive fallbacks.

**Proposed category:** DS (Domain-Specific - Error Recovery)
**Proposed code:** DS-51

---

### Pattern 4: Reference Catalog Pattern (IT-29)

**Description:** Extensive catalog in bundled reference file, organized by category, for quick lookup without external API calls.

**Implementation:**
```markdown
# Reference file structure
## Category 1
| Identifier | Description | Metadata |
|------------|-------------|----------|
| entry1 | ... | ... |
| entry2 | ... | ... |

## Category 2
| Identifier | Description | Metadata |
...

Usage: When user requests entity, lookup in catalog → return details
```

**Use case:**
- Icon libraries (100+ icons)
- API endpoint catalogs
- Error code references
- Configuration option documentation

**Why it's novel:** Brings the "database" into the skill as a bundled reference. Eliminates need for API calls or web searches for common queries. Categorization matches user mental models (Models/Providers/Applications).

**Proposed category:** IT (Interaction Techniques - Knowledge Packaging)
**Proposed code:** IT-29

---

### Pattern 5: Convention Documentation (DS-52)

**Description:** Document naming conventions, variant patterns, and structural rules to enable inference for entities not in catalog.

**Implementation:**
```markdown
**Naming convention**: [pattern description] (e.g., lowercase, hyphenated)

**Variants**:
- Pattern 1: [description] (e.g., `-color` suffix for colored versions)
- Pattern 2: Company vs Product (e.g., `alibaba` vs `alibabacloud`)

**Tips**:
1. [Rule 1 with examples]
2. [Rule 2 with examples]
```

**Use case:**
- Incomplete catalogs (can infer unlisted items)
- Evolving systems (new items follow conventions)
- Fuzzy matching (apply rules to guess)
- API endpoint discovery

**Why it's novel:** Teaches the *system* (conventions) rather than just the *data* (catalog entries). Enables generalization beyond explicit training. Example: Even without "huggingface" in catalog, can infer lowercase, hyphenated form.

**Proposed category:** DS (Domain-Specific - API Conventions)
**Proposed code:** DS-52

---

## Multi-Technique Combinations

### Combination 1: Discovery + Fallback (IT-29 + DS-51)

**Pattern:** Reference Catalog for quick lookup → Fallback Strategy if not found

**Example:**
1. User asks for "Anthropic icon"
2. Check catalog (IT-29) → found: `anthropic`
3. Construct URL using pattern
4. If 404, apply fallback (DS-51): try `-color`, try `claude`, browse web, search repo

**Why effective:** Optimizes for common case (catalog hit) while gracefully handling edge cases (fallback). 80/20 rule: catalog covers 80% of queries, fallback handles remaining 20%.

---

### Combination 2: Pattern Templates + Conventions (DS-50 + DS-52)

**Pattern:** URL Pattern Templates provide structure → Convention Documentation fills in specifics

**Example:**
1. Template: `https://.../packages/static-png/{theme}/{icon-name}.png`
2. Conventions: icon-name is lowercase, hyphenated
3. Query: "Hugging Face logo"
4. Apply convention: "Hugging Face" → `hugging-face` (lowercase, hyphenated)
5. Construct URL: `https://.../dark/hugging-face.png`

**Why effective:** Template provides structure (where to put what), conventions provide transformation rules (how to format). Together enable generative URL construction.

---

### Combination 3: Multi-Language Mapping + Catalog (IT-28 + IT-29)

**Pattern:** Multi-Language Entity Mapping for Chinese queries → Reference Catalog for details

**Example:**
1. User: "找一下智谱的图标" (Find Zhipu icon)
2. Entity mapping (IT-28): "智谱" → `chatglm` or `zhipu`
3. Catalog lookup (IT-29): Both exist, provide both plus related icons (`codegeex`)
4. Return URLs for all variants

**Why effective:** Bridges language gap (Chinese → English ID) then leverages catalog for comprehensive results. Enables multilingual discovery.

---

## Integration Notes

### For MASTER_TECHNIQUE_INDEX.md

**5 new techniques to add:**

1. **DS-50: URL Pattern Templates** - URL construction templates with placeholders for dynamic generation
2. **IT-28: Multi-Language Entity Mapping** - Cross-language query mapping to canonical identifiers
3. **DS-51: Fallback Strategy Pattern** - Progressive fallback with increasing generality
4. **IT-29: Reference Catalog Pattern** - Bundled catalog for quick lookup without external calls
5. **DS-52: Convention Documentation** - Document conventions to enable inference beyond catalog

### For USE_CASE_LOOKUP.md

**Add to existing sections:**

**"API Integration & Tool Usage":**
- DS-50: URL Pattern Templates (construct API URLs dynamically)
- DS-51: Fallback Strategy Pattern (handle API errors gracefully)
- DS-52: Convention Documentation (discover undocumented endpoints)

**"Knowledge Management":**
- IT-29: Reference Catalog Pattern (bundle comprehensive lookup tables)
- IT-19: Three-Tier Progressive Loading (optimize context usage)

**"Multilingual Support":**
- IT-28: Multi-Language Entity Mapping (support Chinese/English queries)

### For AI_AGENT_QUICK_START.md

**Example: Building a Brand Asset Discovery Skill**

```markdown
## Use Case: Icon/Logo Discovery

**Goal:** Help users find brand assets (icons, logos) from libraries

**Techniques:**
1. DS-50: URL Pattern Templates - Teach URL construction logic
2. IT-29: Reference Catalog - Bundle common icons for quick lookup
3. DS-51: Fallback Strategy - Handle missing/misnamed icons
4. DS-52: Convention Documentation - Enable inference for unlisted items
5. IT-28: Multi-Language Mapping (if supporting non-English queries)

**Structure:**
- SKILL.md: URL patterns, workflow, troubleshooting
- references/catalog.md: Comprehensive icon list by category
- references/developer-info.md: Integration instructions
```

### Key Insight: Self-Contained Discovery Systems

**Observation:** This skill creates a self-contained discovery system that minimizes external dependencies:

1. **URL patterns** (not hardcoded URLs) → generates infinite URLs
2. **Catalog** (not API calls) → instant lookup for common cases
3. **Conventions** (not exhaustive enumeration) → infers unlisted items
4. **Fallbacks** (not failures) → gracefully escalates when needed

**Design principle:** Teach the system, not just the data. A good skill provides:
- **Data** (catalog of 100 icons)
- **Logic** (URL construction patterns)
- **Rules** (naming conventions)
- **Recovery** (fallback strategies)

This is more valuable than just listing 100 icon URLs because:
- **Compact:** Patterns are shorter than all URLs
- **Extensible:** Works for new icons following conventions
- **Robust:** Fallbacks handle edge cases
- **Multilingual:** Entity mapping supports Chinese queries

### Application to Other Domains

**This pattern applies to:**
- API documentation (patterns + catalog + conventions)
- Font libraries (naming conventions + CDN patterns)
- Package managers (naming rules + registry lookup + fallbacks)
- Color palettes (naming conventions + hex code patterns)
- Dataset repositories (URL patterns + metadata catalogs)

**Anti-pattern:** Listing every possible URL individually. Instead, teach the construction logic + provide catalog for common cases + document conventions for inference.

---

## Summary

**llm-icon-finder** demonstrates **self-contained discovery system** design using:
- URL pattern templates (generative, not enumerative)
- Reference catalogs (quick lookup for 80% case)
- Convention documentation (inference for edge cases)
- Fallback strategies (graceful degradation)
- Multi-language entity mapping (Chinese/English support)

**Novel contribution:** Shows how to make Claude a **generative discovery agent** rather than a static lookup table. Teaches construction logic, not just memorized answers.

**Key metrics:**
- **Catalog:** 100+ icons organized by category
- **Patterns:** 4 URL patterns (SVG/PNG/WEBP, light/dark, color variants)
- **Languages:** English + Chinese entity mapping
- **Fallback depth:** 4 levels (variant → alternate → browse → search)
- **Total knowledge:** ~179 lines (compact for 100+ icons)

**Recommended applications:**
- Icon/logo libraries
- API endpoint discovery
- Package/dataset registries
- Font libraries
- Color palette systems
- Any domain with systematic naming conventions + large catalogs

---

## Analysis Metadata

- **Analyzer:** Claude (Task 2.2 Priority 2)
- **Review Status:** Complete
- **Priority:** High (LLM application development, asset management)
- **Recommended for MASTER_TECHNIQUE_INDEX:** Yes (5 novel techniques)
- **Integration Complexity:** Low (clear, well-documented patterns)
