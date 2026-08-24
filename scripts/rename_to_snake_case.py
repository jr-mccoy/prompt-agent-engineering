#!/usr/bin/env python3
"""
Script to rename markdown files from kebab-case and PascalCase to snake_case.
Excludes: README.md, CLAUDE.md, CONTRIBUTING.md, LICENSE.md, CHANGELOG.md
"""

import os
import re
import subprocess
import sys

# Files to exclude from renaming
EXCLUDED_FILES = {
    'README.md', 'readme.md', 'CLAUDE.md', 'CONTRIBUTING.md',
    'LICENSE.md', 'CHANGELOG.md', 'LICENSE', 'CODEOWNERS'
}

# Directories to process
DIRECTORIES = ['prompts', 'domain-agentic-resources']


def to_snake_case(filename):
    """Convert filename to snake_case while preserving .md extension."""
    # Remove .md extension for processing
    name = filename
    if filename.endswith('.md'):
        name = filename[:-3]

    # Handle PascalCase: insert underscore before uppercase letters
    # e.g., "APIDesign" -> "api_design"
    name = re.sub(r'([A-Z]+)([A-Z][a-z])', r'\1_\2', name)
    name = re.sub(r'([a-z\d])([A-Z])', r'\1_\2', name)

    # Convert to lowercase
    name = name.lower()

    # Replace hyphens with underscores
    name = name.replace('-', '_')

    # Remove duplicate underscores
    name = re.sub(r'_+', '_', name)

    # Remove leading/trailing underscores
    name = name.strip('_')

    # Add back .md extension if it was there
    if filename.endswith('.md'):
        name += '.md'

    return name


def needs_rename(filename):
    """Check if file needs to be renamed (has hyphen or uppercase in name, excluding extension)."""
    if filename in EXCLUDED_FILES:
        return False

    # Get name without extension
    name = filename
    if filename.endswith('.md'):
        name = filename[:-3]

    # Check for hyphens or uppercase letters
    return '-' in name or any(c.isupper() for c in name)


def rename_files(base_dir, dry_run=False):
    """Rename all applicable files in the given directory."""
    count = 0
    errors = []

    for root, dirs, files in os.walk(base_dir):
        for filename in files:
            if not filename.endswith('.md'):
                continue

            if not needs_rename(filename):
                continue

            old_path = os.path.join(root, filename)
            new_filename = to_snake_case(filename)
            new_path = os.path.join(root, new_filename)

            if old_path == new_path:
                continue

            # Check if destination already exists
            if os.path.exists(new_path):
                errors.append(f"SKIP (exists): {old_path} -> {new_path}")
                continue

            if dry_run:
                print(f"WOULD RENAME: {filename} -> {new_filename}")
            else:
                try:
                    # Use git mv if in a git repo, otherwise regular mv
                    result = subprocess.run(
                        ['git', 'mv', old_path, new_path],
                        capture_output=True,
                        text=True
                    )
                    if result.returncode != 0:
                        # Fall back to regular rename
                        os.rename(old_path, new_path)
                    print(f"RENAMED: {filename} -> {new_filename}")
                    count += 1
                except Exception as e:
                    errors.append(f"ERROR: {old_path} - {str(e)}")

    return count, errors


def main():
    dry_run = '--dry-run' in sys.argv

    if dry_run:
        print("=== DRY RUN MODE ===")
        print("No files will be modified.\n")

    total_count = 0
    all_errors = []

    os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

    for directory in DIRECTORIES:
        if os.path.exists(directory):
            print(f"\n{'='*60}")
            print(f"Processing: {directory}")
            print('='*60)
            count, errors = rename_files(directory, dry_run)
            total_count += count
            all_errors.extend(errors)

    print(f"\n{'='*60}")
    print(f"SUMMARY")
    print('='*60)
    print(f"Total files renamed: {total_count}")

    if all_errors:
        print(f"\nErrors/Skipped ({len(all_errors)}):")
        for error in all_errors:
            print(f"  {error}")


if __name__ == '__main__':
    main()
