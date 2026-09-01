#!/usr/bin/env python3
"""
Script to fix naming convention violations in the Prompt & Agent Engineering repository.

This script:
1. Renames files that violate naming conventions
2. Updates references in documentation files
3. Uses git mv for proper tracking

Usage:
    python fix_naming_violations.py --dry-run    # Preview changes
    python fix_naming_violations.py              # Apply changes
"""

import os
import re
import subprocess
import sys
from pathlib import Path
from collections import defaultdict

# Change to repo root
REPO_ROOT = Path(__file__).parent.parent
os.chdir(REPO_ROOT)

# Files that should NOT be renamed (uppercase index/meta files)
PROTECTED_FILES = {
    'README.md', 'CLAUDE.md', 'CONTRIBUTING.md', 'LICENSE.md', 'CHANGELOG.md',
    'SKILL.md', 'AGENT.md', 'COMMAND.md', 'INDEX.md',
    'IMAGE_GENERATION_GUIDE.md', 'QUICK_START.md',
    'MASTER_TECHNIQUE_INDEX.md', 'USE_CASE_LOOKUP.md',
    'SKILL_PATTERN_INDEX.md', 'SKILL_USE_CASE_LOOKUP.md',
    'SKILL_QUALITY_RUBRIC.md', 'AGENT_SKILL_QUICK_START.md',
    'GOLD_STANDARD_SKILL.md', 'PROMPT_QUALITY_STANDARDS.md',
    'AI_AGENT_QUICK_START.md', 'NON_CODING_QUICK_START.md',
    'AGENT_QUICK_START.md', 'COMMAND_QUICK_START.md',
    'AGENT_PATTERN_INDEX.md', 'AGENT_QUALITY_RUBRIC.md',
    'AGENT_USE_CASE_LOOKUP.md', 'COMMAND_PATTERN_INDEX.md',
    'COMMAND_QUALITY_RUBRIC.md', 'COMMAND_USE_CASE_LOOKUP.md',
    'GOLD_STANDARD_AGENT.md', 'GOLD_STANDARD_COMMAND.md',
    'ADVANCED_PROMPTING_TECHNIQUES.md', 'IMAGE_JSON_PROMPT_TRANSLATOR.md',
}

# Prefix standardization rules
PREFIX_RULES = {
    'codex_': 'workflow_codex_',
    'slop_evaluator_': 'quality_slop_',
    'context_engineering_': 'architecture_context_',
}

# Track all renames for reference updates
RENAME_MAP = {}


def is_protected(filename):
    """Check if file should not be renamed."""
    return filename in PROTECTED_FILES


def sanitize_special_chars(filename):
    """Remove special characters from filename."""
    name = filename[:-3] if filename.endswith('.md') else filename
    # Replace & with _and_ first
    name = name.replace('&', '_and_')
    # Keep only alphanumeric, underscore, and period
    # Remove anything that isn't a-z, A-Z, 0-9, or _
    name = re.sub(r'[^a-zA-Z0-9_]', '', name)
    # Clean up multiple underscores
    name = re.sub(r'_+', '_', name)
    name = name.strip('_')
    return name + '.md' if filename.endswith('.md') else name


def convert_to_snake_case(filename):
    """Convert hyphen-case to snake_case."""
    name = filename[:-3] if filename.endswith('.md') else filename
    name = name.replace('-', '_')
    name = re.sub(r'_+', '_', name)
    return name + '.md' if filename.endswith('.md') else name


def standardize_prefix(filename):
    """Standardize non-standard prefixes."""
    for old_prefix, new_prefix in PREFIX_RULES.items():
        if filename.lower().startswith(old_prefix):
            return new_prefix + filename[len(old_prefix):]
    return filename


def remove_numbered_sequence(filename):
    """Remove numbered sequences like _no1_, _no2_."""
    return re.sub(r'_no\d+_', '_', filename)


def apply_all_fixes(filename):
    """Apply all naming fixes to a filename."""
    if is_protected(filename):
        return filename

    new_name = filename

    # 1. Convert hyphen-case to snake_case FIRST (preserves word boundaries)
    new_name = convert_to_snake_case(new_name)

    # 2. Remove special characters (after hyphens are converted to underscores)
    new_name = sanitize_special_chars(new_name)

    # 3. Remove numbered sequences
    new_name = remove_numbered_sequence(new_name)

    # 4. Standardize prefixes
    new_name = standardize_prefix(new_name)

    # 5. Clean up any double underscores
    new_name = re.sub(r'_+', '_', new_name)
    if new_name.endswith('.md'):
        new_name = new_name[:-3].strip('_') + '.md'

    return new_name


def find_files_to_rename():
    """Find all files that need renaming."""
    to_rename = []

    directories = [
        'domain-agentic-resources',
        'domain-software-engineering',
        'domain-business-strategy',
        'domain-engineering-workflows',
        'domain-productivity',
        'domain-image-generation',
        'domain-presentations',
        'domain-prompt-engineering',
        'domain-decision-making',
        'domain-advertising',
        'domain-professional-writing',
        'domain-professional-communication',
        'domain-personal-development',
        'domain-healthcare-clinical',
        'domain-learning-coding',
        'domain-research-academic',
        'domain-conversation-practice',
        'domain-creative-writing',
        'domain-education-teaching',
        'domain-specialized-fields',
        'domain-frontend-development',
        'techniques',
        'authoring',
    ]

    for directory in directories:
        if not os.path.exists(directory):
            continue
        for root, _, files in os.walk(directory):
            for filename in files:
                if not filename.endswith('.md'):
                    continue
                if is_protected(filename):
                    continue

                new_name = apply_all_fixes(filename)
                if new_name != filename:
                    old_path = os.path.join(root, filename)
                    new_path = os.path.join(root, new_name)
                    to_rename.append((old_path, new_path, filename, new_name))

    return to_rename


def perform_rename(old_path, new_path, dry_run=False):
    """Rename a file using git mv if possible."""
    if dry_run:
        print(f"  Would rename: {os.path.basename(old_path)}")
        print(f"           to: {os.path.basename(new_path)}")
        return True

    # Check if destination exists
    if os.path.exists(new_path):
        print(f"  SKIP (exists): {new_path}")
        return False

    try:
        # Try git mv first
        result = subprocess.run(
            ['git', 'mv', old_path, new_path],
            capture_output=True,
            text=True
        )
        if result.returncode != 0:
            # Fall back to regular rename
            os.rename(old_path, new_path)

        # Track the rename for reference updates
        RENAME_MAP[old_path] = new_path
        print(f"  Renamed: {os.path.basename(old_path)} -> {os.path.basename(new_path)}")
        return True
    except Exception as e:
        print(f"  ERROR: {old_path} - {str(e)}")
        return False


def update_references():
    """Update file references in documentation files."""
    if not RENAME_MAP:
        return

    print("\nUpdating references...")

    # Files to check for references
    doc_files = []
    for pattern in ['*.md', '**/*.md']:
        doc_files.extend(Path('.').glob(pattern))

    # Filter to actual documentation files
    doc_files = [f for f in doc_files if f.is_file() and not str(f).startswith('_archive')]

    updated_count = 0
    for doc_file in doc_files:
        try:
            content = doc_file.read_text(encoding='utf-8')
            original = content

            for old_path, new_path in RENAME_MAP.items():
                old_name = os.path.basename(old_path)
                new_name = os.path.basename(new_path)

                # Update direct filename references
                content = content.replace(old_name, new_name)

                # Update relative path references
                old_rel = old_path.replace('./', '')
                new_rel = new_path.replace('./', '')
                content = content.replace(old_rel, new_rel)

            if content != original:
                doc_file.write_text(content, encoding='utf-8')
                updated_count += 1
                print(f"  Updated: {doc_file}")
        except Exception as e:
            print(f"  ERROR reading {doc_file}: {e}")

    print(f"\nUpdated {updated_count} documentation files")


def main():
    dry_run = '--dry-run' in sys.argv

    if dry_run:
        print("=" * 60)
        print("DRY RUN MODE - No files will be modified")
        print("=" * 60)

    print("\nFinding files to rename...")
    to_rename = find_files_to_rename()

    if not to_rename:
        print("No files need renaming!")
        return

    # Group by type of change for reporting
    by_directory = defaultdict(list)
    for old_path, new_path, old_name, new_name in to_rename:
        directory = os.path.dirname(old_path).split('/')[0]
        by_directory[directory].append((old_path, new_path, old_name, new_name))

    print(f"\nFound {len(to_rename)} files to rename across {len(by_directory)} directories")

    # Process each directory
    success_count = 0
    for directory, files in sorted(by_directory.items()):
        print(f"\n{directory}/ ({len(files)} files)")
        print("-" * 50)
        for old_path, new_path, old_name, new_name in files:
            if perform_rename(old_path, new_path, dry_run):
                success_count += 1

    print(f"\n{'=' * 60}")
    print(f"SUMMARY")
    print(f"{'=' * 60}")
    print(f"Files {'would be ' if dry_run else ''}renamed: {success_count}/{len(to_rename)}")

    if not dry_run and RENAME_MAP:
        update_references()

    if dry_run:
        print("\nRun without --dry-run to apply changes")


if __name__ == '__main__':
    main()
