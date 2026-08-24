#!/usr/bin/env python3
"""
Add standardized YAML frontmatter to command files that are missing it.

This script implements Initiative 1 from the Repository Review Report (2026-01-28):
Command Metadata Standardization

Schema:
---
name: command-name
description: Brief description of the command
version: "1.0.0"
category: category-from-directory
tags: [keyword1, keyword2, ...]
agents_used: [agent1, agent2, ...]
---
"""

import os
import re
from pathlib import Path
from typing import Optional


def has_frontmatter(content: str) -> bool:
    """Check if content already has YAML frontmatter."""
    return content.strip().startswith('---')


def extract_description(content: str, max_length: int = 100) -> str:
    """Extract description from the first meaningful paragraph after title."""
    lines = content.split('\n')
    description_lines = []
    found_title = False
    title_text = ""

    for line in lines:
        stripped = line.strip()

        # Skip frontmatter if present
        if stripped == '---':
            continue

        # Found a title - capture it as fallback
        if stripped.startswith('# '):
            found_title = True
            title_text = stripped[2:].strip()
            continue

        # After title, look for description text
        if found_title and stripped:
            # Skip code blocks
            if stripped.startswith('```'):
                break
            # Skip extended thinking blocks
            if stripped.startswith('[Extended thinking:'):
                continue
            # Skip Task tool invocations
            if stripped.startswith('- Use Task tool'):
                continue
            if stripped.startswith('- Prompt:'):
                continue
            # Skip section headers
            if stripped.startswith('##'):
                break
            # Skip bullet points that look like config/technical
            if stripped.startswith('- ') and any(char in stripped for char in [':', '>', '<', '=']):
                continue
            # Skip lines that are just labels
            if stripped.endswith(':'):
                continue

            # Clean up the line
            clean_line = stripped
            # Remove leading bullet
            if clean_line.startswith('- '):
                clean_line = clean_line[2:]
            # Remove markdown formatting
            clean_line = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', clean_line)
            clean_line = re.sub(r'[*_`]', '', clean_line)

            if clean_line and len(clean_line) > 10:
                description_lines.append(clean_line)
                current_desc = ' '.join(description_lines)
                if len(current_desc) >= max_length:
                    break

    description = ' '.join(description_lines)
    if len(description) > max_length + 20:
        description = description[:max_length].rsplit(' ', 1)[0] + '...'

    # If no good description found, derive from title
    if not description or len(description) < 20:
        if title_text:
            description = f"Multi-agent workflow for {title_text.lower()}"
        else:
            description = "Multi-agent orchestration command"

    return description


def extract_agents_from_content(content: str) -> list[str]:
    """Extract agent names from Task tool invocations in content."""
    agents = set()

    # Pattern: subagent_type="agent-name" or subagent_type='agent-name'
    pattern1 = r'subagent_type\s*=\s*["\']([^"\']+)["\']'
    matches = re.findall(pattern1, content)
    for match in matches:
        # Handle composite paths like "category::agent"
        if '::' in match:
            agents.add(match.split('::')[-1])
        else:
            agents.add(match)

    # Pattern: Looking for explicit agent references
    pattern2 = r'(?:Use|with|spawn|invoke)\s+(?:the\s+)?`?([a-z][a-z0-9-]+(?:-[a-z0-9]+)*)`?\s+(?:agent|specialist)'
    matches = re.findall(pattern2, content, re.IGNORECASE)
    agents.update(matches)

    # Clean up common false positives
    exclude = {'task', 'use', 'tool', 'the', 'with', 'bash', 'read', 'write', 'edit', 'glob', 'grep'}
    agents = {a for a in agents if a.lower() not in exclude and len(a) > 2}

    return sorted(list(agents))


def generate_tags(name: str, category: str, content: str) -> list[str]:
    """Generate relevant tags based on command name, category, and content."""
    tags = set()

    # Add category as tag
    tags.add(category.replace('-', ' '))

    # Extract keywords from name
    name_parts = name.replace('_', '-').split('-')
    for part in name_parts:
        if len(part) > 2 and part not in {'the', 'and', 'for', 'with'}:
            tags.add(part)

    # Look for technology keywords in content
    tech_keywords = [
        'python', 'javascript', 'typescript', 'react', 'vue', 'angular',
        'node', 'rust', 'go', 'java', 'kotlin', 'swift',
        'docker', 'kubernetes', 'k8s', 'terraform', 'aws', 'gcp', 'azure',
        'postgresql', 'mysql', 'mongodb', 'redis', 'kafka',
        'ci/cd', 'cicd', 'github', 'gitlab', 'jenkins',
        'security', 'testing', 'tdd', 'bdd', 'performance', 'monitoring',
        'api', 'rest', 'graphql', 'grpc', 'microservices',
        'ml', 'ai', 'machine learning', 'deep learning',
        'frontend', 'backend', 'fullstack', 'full-stack',
        'debug', 'debugging', 'troubleshooting', 'incident',
        'refactor', 'migration', 'upgrade', 'modernize',
        'documentation', 'docs', 'review', 'audit',
        'accessibility', 'a11y', 'wcag'
    ]

    content_lower = content.lower()
    for keyword in tech_keywords:
        if keyword in content_lower:
            tags.add(keyword.replace(' ', '-'))

    # Limit to most relevant tags
    tags_list = sorted(list(tags))
    return tags_list[:8]  # Keep top 8 tags


def generate_frontmatter(name: str, category: str, content: str) -> str:
    """Generate YAML frontmatter for a command."""
    description = extract_description(content)
    agents = extract_agents_from_content(content)
    tags = generate_tags(name, category, content)

    # Format tags as YAML array
    if tags:
        tags_str = '[' + ', '.join(tags) + ']'
    else:
        tags_str = '[]'

    # Format agents as YAML array
    if agents:
        agents_str = '[' + ', '.join(agents) + ']'
    else:
        agents_str = '[]'

    frontmatter = f'''---
name: {name}
description: {description}
version: "1.0.0"
category: {category}
tags: {tags_str}
agents_used: {agents_str}
---

'''

    return frontmatter


def add_frontmatter_to_file(file_path: Path, dry_run: bool = False) -> tuple[bool, str]:
    """
    Add frontmatter to a command file if it doesn't have one.

    Returns:
        tuple: (was_modified, message)
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    if has_frontmatter(content):
        return False, f"Already has frontmatter: {file_path.name}"

    # Get metadata from path
    category = file_path.parent.name
    name = file_path.stem

    # Generate frontmatter
    frontmatter = generate_frontmatter(name, category, content)

    # Combine with original content
    new_content = frontmatter + content

    if not dry_run:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True, f"Added frontmatter: {file_path.name}"
    else:
        return True, f"Would add frontmatter: {file_path.name}"


def process_commands(commands_dir: Path, dry_run: bool = False) -> dict:
    """Process all command files and add frontmatter where missing."""
    stats = {
        'total': 0,
        'already_has': 0,
        'added': 0,
        'skipped': 0,
        'errors': []
    }

    # Walk through all command subdirectories
    for category_dir in sorted(commands_dir.iterdir()):
        if not category_dir.is_dir():
            continue
        if category_dir.name.startswith('.') or category_dir.name.startswith('_'):
            continue
        if category_dir.name == '__pycache__':
            continue

        for md_file in sorted(category_dir.glob('*.md')):
            if md_file.name == 'README.md':
                continue

            stats['total'] += 1

            try:
                was_modified, message = add_frontmatter_to_file(md_file, dry_run)
                print(message)

                if was_modified:
                    stats['added'] += 1
                else:
                    stats['already_has'] += 1

            except Exception as e:
                stats['errors'].append(f"{md_file}: {str(e)}")
                print(f"ERROR: {md_file.name}: {str(e)}")

    return stats


def main():
    """Main entry point."""
    import argparse

    parser = argparse.ArgumentParser(
        description='Add standardized YAML frontmatter to command files'
    )
    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='Show what would be done without making changes'
    )
    parser.add_argument(
        '--single',
        type=str,
        help='Process only a single file (path relative to commands dir)'
    )

    args = parser.parse_args()

    commands_dir = Path(__file__).parent

    print("=" * 60)
    print("Command Metadata Standardization")
    print("Initiative 1 from Repository Review Report (2026-01-28)")
    print("=" * 60)
    print()

    if args.dry_run:
        print("DRY RUN MODE - No changes will be made")
        print()

    if args.single:
        # Process single file
        file_path = commands_dir / args.single
        if not file_path.exists():
            print(f"File not found: {file_path}")
            return 1

        was_modified, message = add_frontmatter_to_file(file_path, args.dry_run)
        print(message)
        return 0

    # Process all commands
    stats = process_commands(commands_dir, args.dry_run)

    print()
    print("=" * 60)
    print("Summary")
    print("=" * 60)
    print(f"Total command files processed: {stats['total']}")
    print(f"Already had frontmatter:       {stats['already_has']}")
    print(f"Frontmatter added:             {stats['added']}")

    if stats['errors']:
        print(f"Errors:                        {len(stats['errors'])}")
        for error in stats['errors']:
            print(f"  - {error}")

    if args.dry_run and stats['added'] > 0:
        print()
        print(f"Run without --dry-run to add frontmatter to {stats['added']} files")

    return 0


if __name__ == '__main__':
    exit(main())
