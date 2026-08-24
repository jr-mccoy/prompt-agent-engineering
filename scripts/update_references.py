#!/usr/bin/env python3
"""
Script to update file references in documentation from kebab-case to snake_case.
"""

import os
import re
import sys

# Files to process for reference updates
DOC_FILES_TO_CHECK = [
    'CLAUDE.md',
    'README.md',
    'PROMPT_INDEX.md',
    'prompts/non-engineering/README.md',
    'domain-agentic-resources/README.md',
    'domain-agentic-resources/agents/README.md',
    'domain-agentic-resources/commands/README.md',
    'domain-agentic-resources/personas/README.md',
    'domain-agentic-resources/skills/README.md',
    'techniques/MASTER_TECHNIQUE_INDEX.md',
]

def to_snake_case_filename(filename):
    """Convert filename portion from kebab-case to snake_case."""
    # Handle .md extension
    if filename.endswith('.md'):
        name = filename[:-3]
        name = name.replace('-', '_').lower()
        # Handle PascalCase
        name = re.sub(r'([A-Z]+)([A-Z][a-z])', r'\1_\2', name)
        name = re.sub(r'([a-z\d])([A-Z])', r'\1_\2', name)
        name = name.lower()
        name = re.sub(r'_+', '_', name)
        return name.strip('_') + '.md'
    return filename


def update_file_references(filepath):
    """Update kebab-case file references in a file."""
    if not os.path.exists(filepath):
        print(f"SKIP (not found): {filepath}")
        return 0

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content

    # Pattern to match kebab-case .md file references
    # This matches patterns like `filename.md`, `path/to/filename.md`, `agents/backend/backend-security-coder.md`
    pattern = r'([`\[\("]?)([a-zA-Z0-9_/.-]*?)([a-zA-Z0-9]+(?:-[a-zA-Z0-9]+)+)(\.md)([`\]\)"]?)'

    def replace_match(match):
        prefix = match.group(1)
        path = match.group(2)  # Path before filename
        name = match.group(3)  # The kebab-case filename (without extension)
        ext = match.group(4)   # .md
        suffix = match.group(5)

        # Convert kebab to snake
        new_name = name.replace('-', '_')

        return f"{prefix}{path}{new_name}{ext}{suffix}"

    content = re.sub(pattern, replace_match, content)

    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        changes = len(re.findall(pattern, original))
        print(f"UPDATED: {filepath} ({changes} references)")
        return changes
    else:
        print(f"NO CHANGES: {filepath}")
        return 0


def find_all_docs():
    """Find all markdown files that might have references."""
    doc_files = []
    for root, dirs, files in os.walk('.'):
        # Skip _archive directory
        if '_archive' in root:
            continue
        for f in files:
            if f.endswith('.md') and f not in ['CLAUDE.md']:  # Skip files we'll handle specifically
                filepath = os.path.join(root, f)
                # Only include README files and known doc files
                if 'README' in f or filepath.lstrip('./') in DOC_FILES_TO_CHECK:
                    doc_files.append(filepath)
    return doc_files


def main():
    os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

    total_changes = 0

    # Process known doc files
    for filepath in DOC_FILES_TO_CHECK:
        changes = update_file_references(filepath)
        total_changes += changes

    # Also check all README files
    for root, dirs, files in os.walk('.'):
        if '_archive' in root:
            continue
        for f in files:
            if f == 'README.md':
                filepath = os.path.join(root, f).lstrip('./')
                if filepath not in DOC_FILES_TO_CHECK:
                    changes = update_file_references(filepath)
                    total_changes += changes

    print(f"\n{'='*60}")
    print(f"Total references updated: {total_changes}")


if __name__ == '__main__':
    main()
