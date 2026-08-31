# Prompt Index Guide

**Last Updated:** 2026-04-20
**Index Version:** 1.1

---

## Overview

The Prompting-Guides repository includes **machine-readable prompt indexes** that map all ~1,800 prompts in the repository with comprehensive metadata. These indexes replace the deprecated `PROMPT_INDEX.md` and provide programmatic access to the entire prompt collection.

### Available Index Files

| File | Format | Use Case |
|------|--------|----------|
| `PROMPT_INDEX.json` | JSON | Programmatic access, scripting, tools |
| `PROMPT_INDEX.md` | Markdown | Human-readable browsing, GitHub viewing |

---

## Index Statistics

Do not quote statistics from this guide. Counts change with every regeneration,
and the raw index total is a **mixed artifact** total, not a prompt count.

- **Current classified counts:** [`meta/REPOSITORY_FACTS.json`](meta/REPOSITORY_FACTS.json) — each category with its membership rule, generated and verified in CI.
- **Current raw total:** `metadata.total_indexed_artifacts` in [`PROMPT_INDEX.json`](PROMPT_INDEX.json).
- **Largest domains and technique distribution:** printed by `python3 scripts/generate_prompt_index.py`.

---

## Using the JSON Index

### Structure

> **What this index actually contains.** Despite the filename, the index is a
> **mixed artifact population**: domain prompt artifacts, agentic resources
> (skills, agents, commands, personas), and bundled component files belonging to
> a parent resource. Its raw total is *not* a prompt count. Read
> [`meta/REPOSITORY_FACTS.json`](meta/REPOSITORY_FACTS.json) for classified
> counts with stated membership rules. Normalized resource kinds are planned for
> the PAE Registry and do not exist yet — see [`ROADMAP.md`](ROADMAP.md).
>
> Prefer the canonical metadata fields (`total_indexed_artifacts`,
> `index_semantics`, `schema_version`). The prompt-named fields below
> (`total_prompts`, `prompts_with_frontmatter`, `prompts_without_frontmatter`,
> and the top-level `prompts` array) are **deprecated aliases** retained so
> existing consumers keep working; they are enumerated in
> `metadata.deprecated_aliases`. Values shown here are illustrative — read the
> live file for current numbers.

```json
{
  "metadata": {
    "generated": "2026-08-31",
    "schema_version": 1,
    "index_semantics": "mixed_artifacts",
    "total_indexed_artifacts": 5597,
    "artifacts_with_frontmatter": 4661,
    "artifacts_without_frontmatter": 936,
    "domains": 44,
    "canonical_facts": "meta/REPOSITORY_FACTS.json",

    "deprecated_aliases": {
      "total_prompts": "total_indexed_artifacts",
      "prompts_with_frontmatter": "artifacts_with_frontmatter",
      "prompts_without_frontmatter": "artifacts_without_frontmatter",
      "prompts": "top-level array of indexed artifacts (mixed kinds)"
    },
    "total_prompts": 5597,
    "prompts_with_frontmatter": 4661,
    "prompts_without_frontmatter": 936
  },
  "prompts": [
    {
      "path": "domain-software-engineering/analysis/security/security_vulnerability_analysis.md",
      "filename": "security_vulnerability_analysis.md",
      "title": "Security Vulnerability Analysis",
      "domain": "software-engineering",
      "category": "software-engineering/analysis/security",
      "description": "Identify common security weaknesses...",
      "techniques": ["ST-01", "ST-02", "RT-02", "DS-06", "QA-02"],
      "keywords": ["security", "vulnerability", "xss", "sql-injection"],
      "difficulty": "intermediate",
      "updated": "2025-12-15",
      "related_prompts": [...],
      "has_frontmatter": true
    }
  ]
}
```

### Python Example

```python
import json

# Load the index
with open('PROMPT_INDEX.json', 'r') as f:
    index = json.load(f)

# Find all security-related prompts
security_prompts = [
    p for p in index['prompts']
    if 'security' in p['keywords'] or 'security' in p['category']
]

print(f"Found {len(security_prompts)} security prompts")

# Find prompts using specific technique
st_02_prompts = [
    p for p in index['prompts']
    if 'ST-02' in p['techniques']
]

print(f"Found {len(st_02_prompts)} prompts using ST-02")

# Find intermediate-level prompts
intermediate_prompts = [
    p for p in index['prompts']
    if p['difficulty'] == 'intermediate'
]

print(f"Found {len(intermediate_prompts)} intermediate prompts")
```

### JavaScript Example

```javascript
// Load the index
const index = require('./PROMPT_INDEX.json');

// Find all React-related prompts
const reactPrompts = index.prompts.filter(p =>
  p.keywords.some(k => k.toLowerCase().includes('react')) ||
  p.category.includes('react')
);

console.log(`Found ${reactPrompts.length} React prompts`);

// Group by domain
const byDomain = index.prompts.reduce((acc, prompt) => {
  if (!acc[prompt.domain]) acc[prompt.domain] = [];
  acc[prompt.domain].push(prompt);
  return acc;
}, {});

console.log('Prompts by domain:', Object.keys(byDomain).map(d =>
  `${d}: ${byDomain[d].length}`
));
```

---

## Using the Markdown Index

### Structure

The markdown index is organized by domain with tables containing:

- **Title** - Linked to the actual prompt file
- **Category** - Domain/subdomain classification
- **Techniques** - Technique codes used (from MASTER_TECHNIQUE_INDEX.md)
- **Keywords** - Searchable tags
- **Description** - Brief explanation

### Example Entry

```markdown
| Title | Category | Techniques | Keywords | Description |
|-------|----------|------------|----------|-------------|
| [Security Vulnerability Analysis](domain-software-engineering/analysis/security/security_vulnerability_analysis.md) | software-engineering/analysis/security | ST-01, ST-02, RT-02, DS-06, QA-02 | security, vulnerability, xss, sql-injection | Identify common security weaknesses... |
```

### Searching

1. **GitHub Search:** Use GitHub's built-in search on the markdown file
2. **Browser Search:** Open `PROMPT_INDEX.md` and use Ctrl+F / Cmd+F
3. **CLI Tools:** Use `grep`, `ripgrep`, or text editors

**Examples:**

```bash
# Find all prompts related to "security"
grep -i "security" PROMPT_INDEX.md

# Find prompts using technique ST-02
grep "ST-02" PROMPT_INDEX.md

# Find all React prompts
grep -i "react" PROMPT_INDEX.md | grep -v "^#"
```

---

## Search Strategies

### By Domain

**JSON:**
```python
domain_prompts = [p for p in index['prompts'] if p['domain'] == 'software-engineering']
```

**Markdown:**
```bash
# Navigate to the "Software Engineering" section
```

### By Technique

**JSON:**
```python
# Find all prompts using Multi-Dimensional Analysis (RT-02)
rt_02_prompts = [p for p in index['prompts'] if 'RT-02' in p['techniques']]
```

**Markdown:**
```bash
grep "RT-02" PROMPT_INDEX.md
```

### By Keyword

**JSON:**
```python
# Find all prompts tagged with "testing"
testing_prompts = [p for p in index['prompts'] if 'testing' in p['keywords']]
```

**Markdown:**
```bash
grep -i "testing" PROMPT_INDEX.md
```

### By Difficulty

**JSON:**
```python
# Find beginner-friendly prompts
beginner_prompts = [p for p in index['prompts'] if p['difficulty'] == 'beginner']
```

**Markdown:**
- Note: Difficulty is not shown in the table but can be found in the JSON index

### Cross-References

**JSON:**
```python
# Find prompts with related prompts
related_prompts = [p for p in index['prompts'] if p['related_prompts']]
```

### Prompts Without Frontmatter

The markdown index includes a section listing all prompts without frontmatter metadata. These are candidates for improvement.

**JSON:**
```python
no_frontmatter = [p for p in index['prompts'] if not p['has_frontmatter']]
print(f"{len(no_frontmatter)} prompts need frontmatter")
```

---

## Regenerating the Index

The index is generated by the `scripts/generate_prompt_index.py` script.

### Running the Script

```bash
cd /path/to/Prompting-guides
python3 scripts/generate_prompt_index.py
```

### When to Regenerate

- After adding new prompts
- After updating prompt frontmatter
- After reorganizing directory structure
- Monthly maintenance (recommended)

### Automated Regeneration

You can add this to CI/CD or git hooks:

```bash
# .git/hooks/pre-commit
#!/bin/bash
python3 scripts/generate_prompt_index.py
git add PROMPT_INDEX.json PROMPT_INDEX.md
```

---

## Metadata Fields

### Core Fields (Always Present)

| Field | Type | Description | Example |
|-------|------|-------------|---------|
| `path` | string | Relative path from repo root | `"domain-software-engineering/analysis/security/security_vulnerability_analysis.md"` |
| `filename` | string | File name | `"security_vulnerability_analysis.md"` |
| `title` | string | Prompt title | `"Security Vulnerability Analysis"` |
| `domain` | string | Top-level domain | `"software-engineering"` |
| `category` | string | Domain/subdomain classification | `"software-engineering/analysis/security"` |
| `description` | string | Brief explanation | `"Identify common security weaknesses..."` |
| `has_frontmatter` | boolean | Whether prompt has YAML frontmatter | `true` |

### Optional Fields (From Frontmatter)

| Field | Type | Description | Example |
|-------|------|-------------|---------|
| `techniques` | array | Technique codes used | `["ST-01", "ST-02", "RT-02"]` |
| `keywords` | array | Searchable tags | `["security", "vulnerability", "xss"]` |
| `difficulty` | string | Skill level required | `"intermediate"` |
| `updated` | string | Last update date | `"2025-12-15"` |
| `related_prompts` | array | Cross-references | `["domain-business-strategy/..."]` |

---

## Frontmatter Standards

Prompts with proper frontmatter follow this format:

```yaml
---
title: "Clear Descriptive Title"
category: domain-name/subcategory
description: "Brief description of what this prompt does"
techniques:
  - ST-01  # Clear Objective Statement
  - ST-02  # Structured Sequential Instructions
  - RT-02  # Multi-Dimensional Analysis Framework
difficulty: intermediate  # beginner | intermediate | advanced
tags:
  - keyword1
  - keyword2
  - keyword3
updated: "2025-12-15"
related_prompts:
  - path/to/related/prompt.md
---
```

### Adding Frontmatter to Existing Prompts

If a prompt lacks frontmatter, you can add it following the standard above. The index will automatically pick it up on the next regeneration.

**Example:**

Before:
```markdown
# Security Vulnerability Analysis

This prompt helps identify security vulnerabilities...
```

After:
```markdown
---
title: "Security Vulnerability Analysis"
category: software-engineering/analysis/security
description: "Identify common security weaknesses in code"
techniques:
  - ST-01
  - ST-02
  - RT-02
difficulty: intermediate
tags:
  - security
  - vulnerability
  - code-analysis
updated: "2026-02-07"
---

# Security Vulnerability Analysis

This prompt helps identify security vulnerabilities...
```

---

## Technique Codes Reference

The `techniques` field references codes from `techniques/MASTER_TECHNIQUE_INDEX.md`.

### Top 10 Most Used Techniques

| Code | Name | Usage Count |
|------|------|-------------|
| **ST-02** | Structured Sequential Instructions | 100 prompts |
| **ST-01** | Clear Objective Statement | 96 prompts |
| **RT-02** | Multi-Dimensional Analysis Framework | 81 prompts |
| **OC-01** | Output Format Templates | 36 prompts |
| **QA-02** | Adversarial Thinking / Stress-Test | 34 prompts |
| **DS-06** | Prioritization Guidance | 32 prompts |
| **RT-05** | Evidence-Based Reasoning | 29 prompts |
| **DS-01** | Framework Application | 26 prompts |
| **NE-01** | Direct Input Injection | 18 prompts |
| **DS-03** | Comparative Analysis | 15 prompts |

For the complete technique catalog, see `techniques/MASTER_TECHNIQUE_INDEX.md`.

---

## Integration Examples

### Building a Prompt Search Tool

```python
import json
from typing import List, Dict

class PromptSearch:
    def __init__(self, index_path: str):
        with open(index_path, 'r') as f:
            self.index = json.load(f)
        self.prompts = self.index['prompts']

    def search_by_keyword(self, keyword: str) -> List[Dict]:
        """Find prompts containing keyword in any field"""
        keyword = keyword.lower()
        return [
            p for p in self.prompts
            if keyword in p['title'].lower()
            or keyword in p['description'].lower()
            or any(keyword in k.lower() for k in p['keywords'])
        ]

    def search_by_technique(self, technique: str) -> List[Dict]:
        """Find prompts using specific technique"""
        return [p for p in self.prompts if technique in p['techniques']]

    def search_by_domain(self, domain: str) -> List[Dict]:
        """Find prompts in specific domain"""
        return [p for p in self.prompts if p['domain'] == domain]

    def get_stats(self) -> Dict:
        """Get index statistics"""
        return self.index['metadata']

# Usage
searcher = PromptSearch('PROMPT_INDEX.json')

# Find security prompts
security = searcher.search_by_keyword('security')
print(f"Found {len(security)} security prompts")

# Find prompts using ST-02
structured = searcher.search_by_technique('ST-02')
print(f"Found {len(structured)} prompts using ST-02")

# Get stats
stats = searcher.get_stats()
print(f"Total indexed artifacts: {stats['total_indexed_artifacts']}")
```

### Building a Prompt Recommender

```python
def recommend_prompts(query: str, searcher: PromptSearch, limit: int = 5) -> List[Dict]:
    """Recommend prompts based on query"""
    results = searcher.search_by_keyword(query)

    # Sort by relevance (simple scoring)
    def score(prompt):
        score = 0
        query_lower = query.lower()

        # Title match (highest weight)
        if query_lower in prompt['title'].lower():
            score += 10

        # Keyword match
        for keyword in prompt['keywords']:
            if query_lower in keyword.lower():
                score += 5

        # Description match
        if query_lower in prompt['description'].lower():
            score += 2

        # Has frontmatter (quality signal)
        if prompt['has_frontmatter']:
            score += 1

        return score

    results.sort(key=score, reverse=True)
    return results[:limit]

# Usage
recommendations = recommend_prompts('react testing', searcher, limit=5)
for prompt in recommendations:
    print(f"- {prompt['title']} ({prompt['path']})")
```

---

## Contributing

### Adding New Prompts

When adding new prompts:

1. **Follow naming conventions:** `{domain_prefix}_{specific_function}.md`
2. **Add proper frontmatter** (see Frontmatter Standards above)
3. **Regenerate the index:** `python3 scripts/generate_prompt_index.py`
4. **Commit both the prompt and updated index files**

### Improving Existing Prompts

When improving prompts without frontmatter:

1. **Add frontmatter** following the standard format
2. **Fill in all relevant fields** (techniques, keywords, difficulty, etc.)
3. **Regenerate the index**
4. **Commit changes**

The markdown index includes a "Prompts Without Frontmatter" section to identify candidates for improvement.

---

## Troubleshooting

### Index Generation Fails

**Problem:** Script errors during generation

**Solutions:**
- Ensure Python 3.8+ is installed
- Check that all markdown files are valid UTF-8
- Look for malformed YAML frontmatter

### Missing Prompts in Index

**Problem:** Some prompts don't appear in the index

**Solutions:**
- Check that files end with `.md`
- Verify files are in `domain-*` directories
- Ensure files are not in `EXCLUDE_FILES` list (README.md, INDEX.md, etc.)

### Incorrect Metadata

**Problem:** Metadata doesn't match the prompt file

**Solutions:**
- Check frontmatter YAML syntax
- Ensure YAML delimiters (`---`) are on their own lines
- Regenerate the index after fixing frontmatter

### Technique Codes Unknown

**Problem:** Don't know which technique codes to use

**Solutions:**
- Consult `techniques/MASTER_TECHNIQUE_INDEX.md`
- Review `techniques/USE_CASE_LOOKUP.md` for patterns
- Look at similar prompts in the index for examples

---

## FAQ

**Q: How often should I regenerate the index?**
A: After adding/modifying prompts, or monthly for maintenance.

**Q: Can I edit the index files directly?**
A: No, they're auto-generated. Edit the source prompts and regenerate.

**Q: What if my prompt doesn't have frontmatter?**
A: The script will infer basic metadata, but adding frontmatter is recommended.

**Q: How do I search for prompts across multiple criteria?**
A: Use the JSON index with Python/JavaScript for complex queries.

**Q: Are the indexes versioned?**
A: Yes, they're in git. Check git history to see changes over time.

**Q: What's the difference between `category` and `domain`?**
A: `domain` is the top-level directory (e.g., "software-engineering"), `category` includes subdirectories (e.g., "software-engineering/analysis/security").

---

## Resources

- **Main README:** `README.md`
- **Technique Index:** `techniques/MASTER_TECHNIQUE_INDEX.md`
- **Use Case Lookup:** `techniques/USE_CASE_LOOKUP.md`
- **AI Agent Quick Start:** `AI_AGENT_QUICK_START.md`
- **Non-Coding Quick Start:** `NON_CODING_QUICK_START.md`
- **Image Generation Guide:** `domain-image-generation/IMAGE_GENERATION_GUIDE.md`
- **Skill Authoring:** `authoring/skill-patterns/README.md`
- **Claude Agent Guide:** `CLAUDE.md`

---

**Version:** 1.1
**Last Updated:** 2026-04-20
**Maintainer:** Prompting-Guides Repository
**License:** MIT
