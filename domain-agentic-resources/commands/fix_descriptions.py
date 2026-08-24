#!/usr/bin/env python3
"""
Fix description fields in command frontmatter.
Updates descriptions to be more meaningful.
"""

import os
import re
from pathlib import Path


def extract_better_description(content: str, max_length: int = 100) -> str:
    """Extract a better description from content."""
    # Remove existing frontmatter
    if content.strip().startswith('---'):
        parts = content.split('---', 2)
        if len(parts) >= 3:
            content = parts[2]

    lines = content.split('\n')
    description_lines = []
    found_title = False
    title_text = ""

    for line in lines:
        stripped = line.strip()

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
            # Skip Output/Context lines
            if stripped.startswith('- Output:') or stripped.startswith('- Context:'):
                continue
            if stripped.startswith('- Expected output:'):
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


def fix_description_in_file(file_path: Path, dry_run: bool = False) -> tuple[bool, str]:
    """Fix the description in a file's frontmatter."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    if not content.strip().startswith('---'):
        return False, f"No frontmatter: {file_path.name}"

    # Parse frontmatter
    parts = content.split('---', 2)
    if len(parts) < 3:
        return False, f"Invalid frontmatter: {file_path.name}"

    frontmatter = parts[1]
    body = parts[2]

    # Get better description
    new_desc = extract_better_description(content)

    # Check current description
    desc_match = re.search(r'^description:\s*(.+)$', frontmatter, re.MULTILINE)
    if desc_match:
        old_desc = desc_match.group(1).strip()

        # Check if description needs fixing (starts with technical content)
        needs_fix = (
            old_desc.startswith('- ') or
            old_desc.startswith('Prompt:') or
            'Minimum' in old_desc or
            'coverage' in old_desc.lower() or
            len(old_desc) < 30
        )

        if not needs_fix:
            return False, f"Description OK: {file_path.name}"

        # Replace description
        new_frontmatter = re.sub(
            r'^description:\s*.+$',
            f'description: {new_desc}',
            frontmatter,
            flags=re.MULTILINE
        )
    else:
        return False, f"No description field: {file_path.name}"

    new_content = f'---{new_frontmatter}---{body}'

    if not dry_run:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True, f"Fixed description: {file_path.name}"
    else:
        return True, f"Would fix: {file_path.name} -> {new_desc[:50]}..."


def main():
    import argparse

    parser = argparse.ArgumentParser(description='Fix descriptions in command frontmatter')
    parser.add_argument('--dry-run', action='store_true', help='Show changes without applying')

    args = parser.parse_args()

    commands_dir = Path(__file__).parent

    fixed = 0
    skipped = 0

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

            was_fixed, message = fix_description_in_file(md_file, args.dry_run)
            print(message)

            if was_fixed:
                fixed += 1
            else:
                skipped += 1

    print(f"\nFixed: {fixed}, Skipped: {skipped}")


if __name__ == '__main__':
    main()
