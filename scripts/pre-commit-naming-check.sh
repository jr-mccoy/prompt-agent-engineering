#!/bin/bash
#
# Pre-commit hook to validate naming conventions for markdown files
#
# Installation:
#   cp scripts/pre-commit-naming-check.sh .git/hooks/pre-commit
#   chmod +x .git/hooks/pre-commit
#
# Or if using pre-commit framework, add to .pre-commit-config.yaml:
#   repos:
#     - repo: local
#       hooks:
#         - id: naming-conventions
#           name: Check naming conventions
#           entry: python scripts/validate_naming_conventions.py --ci
#           language: python
#           types: [markdown]
#

set -e

# Get the list of staged .md files
STAGED_FILES=$(git diff --cached --name-only --diff-filter=ACMR | grep '\.md$' || true)

if [ -z "$STAGED_FILES" ]; then
    exit 0
fi

# Check if python is available
if ! command -v python3 &> /dev/null; then
    echo "Warning: python3 not found, skipping naming convention check"
    exit 0
fi

# Check if the validator script exists
SCRIPT_PATH="scripts/validate_naming_conventions.py"
if [ ! -f "$SCRIPT_PATH" ]; then
    echo "Warning: $SCRIPT_PATH not found, skipping naming convention check"
    exit 0
fi

echo "Checking naming conventions for staged files..."

# Create temp file for staged files
TEMP_FILE=$(mktemp)
echo "$STAGED_FILES" > "$TEMP_FILE"

# Track any violations
VIOLATIONS=0

# Characters that must never appear in a prompt filename. Defined as a
# single-quoted variable (with an escaped literal apostrophe) so the shell
# does not mis-parse the class; matching an unquoted variable after =~
# keeps it a regex rather than a literal string.
SPECIAL_CHARS_RE='[]()"'"'"'[{}!@#$%^*=+|\:;<>?,]'

while IFS= read -r file; do
    # Skip special files
    filename=$(basename "$file")
    if [[ "$filename" =~ ^(README|CLAUDE|CONTRIBUTING|LICENSE|CHANGELOG|SKILL|AGENT|COMMAND|INDEX)\.md$ ]]; then
        continue
    fi
    if [[ "$filename" =~ ^[A-Z_]+\.md$ ]]; then
        # All-caps file (likely an index file)
        continue
    fi

    # Check for hyphen-case
    if [[ "$filename" =~ - ]]; then
        echo "  ERROR: $file uses hyphen-case (should be snake_case)"
        VIOLATIONS=$((VIOLATIONS + 1))
    fi

    # Check for special characters
    if [[ "$filename" =~ $SPECIAL_CHARS_RE ]]; then
        echo "  ERROR: $file contains special characters"
        VIOLATIONS=$((VIOLATIONS + 1))
    fi

    # Check filename length (without .md extension)
    name="${filename%.md}"
    if [ ${#name} -gt 55 ]; then
        echo "  WARNING: $file has filename longer than 55 characters (${#name})"
    fi
done < "$TEMP_FILE"

rm "$TEMP_FILE"

if [ $VIOLATIONS -gt 0 ]; then
    echo ""
    echo "Found $VIOLATIONS naming convention violations."
    echo "Please rename files to use snake_case and remove special characters."
    echo ""
    echo "To fix, run: python scripts/fix_naming_violations.py --dry-run"
    echo "Then: python scripts/fix_naming_violations.py"
    exit 1
fi

echo "All files pass naming convention checks."
exit 0
