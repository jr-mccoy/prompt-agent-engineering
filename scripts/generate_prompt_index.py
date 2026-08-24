#!/usr/bin/env python3
"""
Generate a comprehensive machine-readable prompt index.
Extracts metadata from frontmatter and generates JSON + Markdown outputs.
"""

import os
import re
import json
import hashlib
import yaml
from datetime import date
from pathlib import Path
from typing import Dict, List, Optional, Any
from collections import defaultdict

# Track YAML parsing failures for reporting
_yaml_errors: List[str] = []

# Repository root
REPO_ROOT = Path(__file__).parent.parent
DOMAIN_DIRS = [
    "domain-software-engineering",
    "domain-AI-ML",
    "domain-frontend-development",
    "domain-agentic-resources",
    "domain-business-strategy",
    "domain-engineering-workflows",
    "domain-productivity",
    "domain-image-generation",
    "domain-presentations",
    "domain-prompt-engineering",
    "domain-decision-making",
    "domain-advertising",
    "domain-professional-writing",
    "domain-professional-communication",
    "domain-personal-development",
    "domain-healthcare-clinical",
    "domain-learning-coding",
    "domain-research-academic",
    "domain-science",
    "domain-conversation-practice",
    "domain-creative-writing",
    "domain-education-teaching",
    "domain-specialized-fields",
    "domain-finance",
    "domain-psychology",
    "domain-parenting",
    "domain-game-development",
    "domain-deep-analysis",
    "domain-hr-management",
    "domain-legal",
    "domain-biblical-studies",
    "domain-discipleship",
    "domain-childrens-writing",
    "domain-reasoning-craft",
    "domain-ideation",
    "domain-policy",
    "domain-negotiation",
    "domain-risk",
    "domain-learning",
    "domain-idea-to-product",
    "domain-psy-ops",
    "domain-written-advocacy",
    "domain-medical-education",
    "domain-voice-conversational-ui",
]

# Self-contained pipeline domains that intentionally re-copy upstream prompts
# so the directory works standalone. Their byte-identical copies are skipped
# during indexing to avoid double-counting prompts already indexed under their
# canonical homes; only prompts unique to the pipeline (e.g. the net-new
# gap-fill prompts and orchestrator) are indexed.
SELF_CONTAINED_DEDUP_DOMAINS = {
    "domain-idea-to-product",
}

# Files to exclude
EXCLUDE_FILES = {
    "README.md",
    "INDEX.md",
    "GUIDE.md",
    # Domain meta-docs, not prompts. Without these, 18 roadmap/field-guide files
    # across 12 domains were indexed as if they were prompts.
    "EXPANSION_ROADMAP.md",
    "field_guide.md",
    "MASTER_TECHNIQUE_INDEX.md",
    "USE_CASE_LOOKUP.md",
    "SKILL_PATTERN_INDEX.md",
    "SKILL_USE_CASE_LOOKUP.md",
    "SKILL_QUALITY_RUBRIC.md",
}


def extract_frontmatter(content: str, filepath: str = "") -> Optional[Dict[str, Any]]:
    """Extract YAML frontmatter from markdown content."""
    # Match YAML frontmatter between --- delimiters
    pattern = r'^---\s*\n(.*?)\n---\s*\n'
    match = re.match(pattern, content, re.DOTALL)

    if match:
        raw_yaml = match.group(1)
        try:
            frontmatter = yaml.safe_load(raw_yaml)
            if isinstance(frontmatter, dict):
                # Convert date objects to strings for JSON serialization
                for key, value in frontmatter.items():
                    if hasattr(value, 'isoformat'):
                        frontmatter[key] = value.isoformat()
                return frontmatter
            return {}
        except yaml.YAMLError as e:
            _yaml_errors.append(f"  YAML error in {filepath}: {e}")
            # Fallback: try to extract key fields from raw YAML text
            return _fallback_extract(raw_yaml)
    return {}


def _fallback_extract(raw_yaml: str) -> Dict[str, Any]:
    """Best-effort extraction of frontmatter fields when YAML parsing fails.

    Handles common issues like unquoted colons, invalid escape sequences,
    and nested quotes that cause yaml.safe_load to fail.
    """
    result = {}

    # Extract title (handles quoted values)
    title_match = re.search(r'^title:\s*"?([^"\n]+)"?\s*$', raw_yaml, re.MULTILINE)
    if title_match:
        result['title'] = title_match.group(1).strip().strip('"')

    # Extract category
    cat_match = re.search(r'^category:\s*(\S+)', raw_yaml, re.MULTILINE)
    if cat_match:
        result['category'] = cat_match.group(1).strip()

    # Extract techniques (YAML list format: "  - XX-NN")
    techniques = re.findall(r'^\s+-\s+([A-Z]{2}-\d{2})\s*$', raw_yaml, re.MULTILINE)
    if techniques:
        result['techniques'] = techniques

    # Extract tags (YAML list format or inline array)
    tags_inline = re.search(r'^tags:\s*\[([^\]]+)\]', raw_yaml, re.MULTILINE)
    if tags_inline:
        result['tags'] = [t.strip().strip('"\'') for t in tags_inline.group(1).split(',')]
    else:
        tags = re.findall(r'^  -\s+(\S+)', raw_yaml[raw_yaml.find('tags:'):] if 'tags:' in raw_yaml else '', re.MULTILINE)
        if tags:
            result['tags'] = tags

    # Extract difficulty
    diff_match = re.search(r'^difficulty:\s*(\S+)', raw_yaml, re.MULTILINE)
    if diff_match:
        result['difficulty'] = diff_match.group(1).strip()

    # Extract updated date
    date_match = re.search(r'^updated:\s*"?(\d{4}-\d{2}-\d{2})"?', raw_yaml, re.MULTILINE)
    if date_match:
        result['updated'] = date_match.group(1)

    return result


def extract_title_from_content(content: str) -> Optional[str]:
    """Extract title from first H1 header if frontmatter is missing."""
    lines = content.split('\n')
    for line in lines[:20]:  # Check first 20 lines
        if line.startswith('# '):
            return line[2:].strip()
    return None


def infer_category_from_path(filepath: Path) -> str:
    """Infer category from file path structure."""
    parts = filepath.parts

    # Find domain directory
    domain = None
    for part in parts:
        if part.startswith('domain-'):
            domain = part.replace('domain-', '')
            break

    # Get subdirectory path after domain
    if domain:
        try:
            domain_idx = parts.index(f'domain-{domain}')
            subdirs = parts[domain_idx + 1:-1]  # Exclude filename
            if subdirs:
                return f"{domain}/{'/'.join(subdirs)}"
            return domain
        except (ValueError, IndexError):
            pass

    return "uncategorized"


def extract_keywords_from_content(content: str, filename: str) -> List[str]:
    """Extract potential keywords from filename and content."""
    keywords = set()

    # From filename (remove extension and split on underscores)
    name_parts = Path(filename).stem.split('_')
    keywords.update([p for p in name_parts if len(p) > 2])

    # Extract from content headers (H2, H3)
    headers = re.findall(r'^#{2,3}\s+(.+)$', content, re.MULTILINE)
    for header in headers[:5]:  # Limit to first 5 headers
        words = re.findall(r'\b[a-zA-Z]{4,}\b', header)
        keywords.update([w.lower() for w in words[:3]])

    return sorted(list(keywords))[:10]  # Limit to 10 keywords


def extract_description_from_content(content: str) -> Optional[str]:
    """Extract description from content (first paragraph after title)."""
    # Remove frontmatter
    content = re.sub(r'^---\s*\n.*?\n---\s*\n', '', content, flags=re.DOTALL)

    # Find first paragraph after title
    lines = content.split('\n')
    in_paragraph = False
    paragraph_lines = []

    for line in lines:
        line = line.strip()

        # Skip empty lines and markdown headers
        if not line or line.startswith('#'):
            if paragraph_lines:
                break
            continue

        # Skip markdown formatting
        if line.startswith('**') or line.startswith('##'):
            continue

        # Collect paragraph lines
        paragraph_lines.append(line)

        # Stop at first full sentence or after 200 chars
        if line.endswith('.') or len(' '.join(paragraph_lines)) > 200:
            break

    if paragraph_lines:
        desc = ' '.join(paragraph_lines)
        # Clean up markdown formatting
        desc = re.sub(r'\*\*(.+?)\*\*', r'\1', desc)  # Bold
        desc = re.sub(r'\*(.+?)\*', r'\1', desc)      # Italic
        desc = re.sub(r'\[(.+?)\]\(.+?\)', r'\1', desc)  # Links
        return desc[:300]  # Limit to 300 chars

    return None


def process_prompt_file(filepath: Path) -> Optional[Dict[str, Any]]:
    """Process a single prompt file and extract metadata."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"Error reading {filepath}: {e}")
        return None

    # Extract frontmatter
    frontmatter = extract_frontmatter(content, str(filepath))

    # Detect frontmatter presence from delimiters (independent of YAML parse success)
    has_fm_delimiters = bool(re.match(r'^---\s*\n.*?\n---\s*\n', content, re.DOTALL))

    # Build metadata
    relative_path = filepath.relative_to(REPO_ROOT)

    metadata = {
        'path': str(relative_path),
        'filename': filepath.name,
        'title': frontmatter.get('title') or extract_title_from_content(content) or filepath.stem.replace('_', ' ').title(),
        'domain': relative_path.parts[0].replace('domain-', '') if relative_path.parts[0].startswith('domain-') else 'unknown',
        'category': frontmatter.get('category') or infer_category_from_path(filepath),
        'description': frontmatter.get('description') or extract_description_from_content(content) or '',
        'techniques': frontmatter.get('techniques', []),
        'keywords': frontmatter.get('tags', []) or extract_keywords_from_content(content, filepath.name),
        'difficulty': frontmatter.get('difficulty', ''),
        'updated': frontmatter.get('updated', ''),
        'related_prompts': frontmatter.get('related_prompts', []),
        'has_frontmatter': has_fm_delimiters,
    }

    # Machine-readable reasoning taxonomy block (domain-reasoning-craft convention);
    # included only when present so legacy entries stay unchanged.
    if isinstance(frontmatter.get('reasoning'), dict):
        metadata['reasoning'] = frontmatter['reasoning']

    return metadata


def _content_hash(filepath: Path) -> Optional[str]:
    """Return an MD5 hash of a file's bytes, or None if unreadable."""
    try:
        return hashlib.md5(filepath.read_bytes()).hexdigest()
    except OSError:
        return None


def build_canonical_hashes() -> set:
    """Hash every prompt file outside the self-contained dedup domains.

    Used to skip byte-identical copies in self-contained pipeline domains so
    they are not double-counted in the index.
    """
    hashes = set()
    for domain_dir in DOMAIN_DIRS:
        if domain_dir in SELF_CONTAINED_DEDUP_DOMAINS:
            continue
        domain_path = REPO_ROOT / domain_dir
        if not domain_path.exists():
            continue
        for root, dirs, files in os.walk(domain_path):
            # Sort in place so traversal order does not depend on the
            # filesystem; the index must be byte-identical across machines
            # for the CI freshness check to be meaningful.
            dirs.sort()
            files.sort()
            for filename in files:
                if not filename.endswith('.md') or filename in EXCLUDE_FILES:
                    continue
                h = _content_hash(Path(root) / filename)
                if h:
                    hashes.add(h)
    return hashes


def scan_domain_directories() -> List[Dict[str, Any]]:
    """Scan all domain directories and extract prompt metadata."""
    all_prompts = []
    canonical_hashes = build_canonical_hashes()

    for domain_dir in DOMAIN_DIRS:
        domain_path = REPO_ROOT / domain_dir

        if not domain_path.exists():
            print(f"Warning: {domain_dir} not found")
            continue

        is_dedup_domain = domain_dir in SELF_CONTAINED_DEDUP_DOMAINS
        skipped_dups = 0

        # Walk through directory
        for root, dirs, files in os.walk(domain_path):
            dirs.sort()
            files.sort()
            for filename in files:
                # Skip non-markdown files and excluded files.
                # Leading-underscore files are planning/notes docs, not prompts.
                if (not filename.endswith('.md')
                        or filename in EXCLUDE_FILES
                        or filename.startswith('_')):
                    continue

                filepath = Path(root) / filename

                # In self-contained pipeline domains, skip prompts that are
                # byte-identical copies of canonical prompts indexed elsewhere.
                if is_dedup_domain and _content_hash(filepath) in canonical_hashes:
                    skipped_dups += 1
                    continue

                metadata = process_prompt_file(filepath)

                if metadata:
                    all_prompts.append(metadata)

        if is_dedup_domain:
            print(f"Scanning {domain_dir}... (skipped {skipped_dups} "
                  f"duplicate copies of canonical prompts)")
        else:
            print(f"Scanning {domain_dir}...")

    return all_prompts


def generate_json_index(prompts: List[Dict[str, Any]], output_path: Path):
    """Generate JSON index file."""
    # Group by domain for better organization
    today = date.today().isoformat()
    index = {
        'metadata': {
            'generated': today,
            'total_prompts': len(prompts),
            'domains': len(set(p['domain'] for p in prompts)),
            'prompts_with_frontmatter': sum(1 for p in prompts if p['has_frontmatter']),
            'prompts_without_frontmatter': sum(1 for p in prompts if not p['has_frontmatter']),
        },
        'prompts': sorted(prompts, key=lambda x: (x['domain'], x['category'], x['title'], x['path']))
    }

    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(index, f, indent=2, ensure_ascii=False)

    print(f"\n✓ Generated JSON index: {output_path}")
    print(f"  Total prompts: {len(prompts)}")


def generate_markdown_index(prompts: List[Dict[str, Any]], output_path: Path):
    """Generate Markdown table index."""
    with open(output_path, 'w', encoding='utf-8') as f:
        today = date.today().isoformat()
        f.write("# Comprehensive Prompt Index\n\n")
        f.write(f"**Generated:** {today}\n\n")
        f.write(f"**Total Prompts:** {len(prompts)}\n\n")
        f.write(f"**Prompts with Frontmatter:** {sum(1 for p in prompts if p['has_frontmatter'])}\n\n")
        f.write(f"**Prompts without Frontmatter:** {sum(1 for p in prompts if not p['has_frontmatter'])}\n\n")

        f.write("---\n\n")

        # Group by domain
        prompts_by_domain = defaultdict(list)
        for prompt in prompts:
            prompts_by_domain[prompt['domain']].append(prompt)

        for domain in sorted(prompts_by_domain.keys()):
            domain_prompts = sorted(prompts_by_domain[domain], key=lambda x: (x['category'], x['title'], x['path']))

            f.write(f"## {domain.replace('-', ' ').title()}\n\n")
            f.write(f"**Total:** {len(domain_prompts)} prompts\n\n")

            # Table header
            f.write("| Title | Category | Techniques | Keywords | Description |\n")
            f.write("|-------|----------|------------|----------|-------------|\n")

            for prompt in domain_prompts:
                title = prompt['title'][:50]
                category = prompt['category'][:30]
                techniques = ', '.join(str(t) for t in prompt['techniques'][:5]) if prompt['techniques'] else '—'
                keywords = ', '.join(str(k) for k in prompt['keywords'][:5]) if prompt['keywords'] else '—'
                description = (prompt['description'][:100] + '...') if len(prompt['description']) > 100 else prompt['description']

                # Escape pipe characters in content
                description = description.replace('|', '\\|')
                title = title.replace('|', '\\|')

                f.write(f"| [{title}]({prompt['path']}) | {category} | {techniques} | {keywords} | {description} |\n")

            f.write("\n")

        # Add prompts without frontmatter section
        no_frontmatter = [p for p in prompts if not p['has_frontmatter']]
        if no_frontmatter:
            f.write("---\n\n")
            f.write(f"## Prompts Without Frontmatter ({len(no_frontmatter)})\n\n")
            f.write("These prompts need frontmatter metadata added:\n\n")

            for prompt in sorted(no_frontmatter, key=lambda x: x['path']):
                f.write(f"- `{prompt['path']}` - {prompt['title']}\n")

    print(f"\n✓ Generated Markdown index: {output_path}")


def generate_statistics(prompts: List[Dict[str, Any]]):
    """Generate and print statistics about the prompt collection."""
    print("\n" + "="*60)
    print("PROMPT INDEX STATISTICS")
    print("="*60)

    print(f"\nTotal Prompts: {len(prompts)}")
    print(f"Prompts with Frontmatter: {sum(1 for p in prompts if p['has_frontmatter'])}")
    print(f"Prompts without Frontmatter: {sum(1 for p in prompts if not p['has_frontmatter'])}")

    # By domain
    by_domain = defaultdict(int)
    for p in prompts:
        by_domain[p['domain']] += 1

    print("\nPrompts by Domain:")
    for domain in sorted(by_domain.keys(), key=lambda x: by_domain[x], reverse=True):
        print(f"  {domain}: {by_domain[domain]}")

    # Technique usage
    technique_counts = defaultdict(int)
    for p in prompts:
        for tech in p['techniques']:
            technique_counts[tech] += 1

    if technique_counts:
        print("\nTop 10 Most Used Techniques:")
        for tech, count in sorted(technique_counts.items(), key=lambda x: x[1], reverse=True)[:10]:
            print(f"  {tech}: {count} prompts")

    # Difficulty distribution
    difficulty_counts = defaultdict(int)
    for p in prompts:
        diff = p['difficulty'] or 'unspecified'
        difficulty_counts[diff] += 1

    print("\nDifficulty Distribution:")
    for diff, count in sorted(difficulty_counts.items()):
        print(f"  {diff}: {count}")

    # Report YAML parsing errors
    if _yaml_errors:
        print(f"\nYAML Parsing Errors ({len(_yaml_errors)} files — used fallback extraction):")
        for err in _yaml_errors:
            print(err)

    print("\n" + "="*60)


def main():
    """Main execution function."""
    print("="*60)
    print("PROMPT INDEX GENERATOR")
    print("="*60)

    # Scan all prompts
    print("\nScanning domain directories...\n")
    prompts = scan_domain_directories()

    if not prompts:
        print("No prompts found!")
        return

    # Generate outputs
    json_output = REPO_ROOT / 'PROMPT_INDEX.json'
    markdown_output = REPO_ROOT / 'PROMPT_INDEX.md'

    generate_json_index(prompts, json_output)
    generate_markdown_index(prompts, markdown_output)
    generate_statistics(prompts)

    print("\n✓ Index generation complete!")
    print(f"\nOutputs:")
    print(f"  - {json_output}")
    print(f"  - {markdown_output}")


if __name__ == '__main__':
    main()
