#!/bin/bash
# Script to rename files from kebab-case and PascalCase to snake_case
# Excludes: README.md, CLAUDE.md, and already snake_case files

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Counter for renamed files
count=0

# Function to convert to snake_case
to_snake_case() {
    local filename="$1"
    # First, handle PascalCase by adding underscore before uppercase letters
    # Then convert all to lowercase and replace hyphens with underscores
    echo "$filename" | \
        sed 's/\([A-Z]\)/_\L\1/g' | \
        sed 's/^_//' | \
        tr '[:upper:]' '[:lower:]' | \
        tr '-' '_' | \
        sed 's/__*/_/g' | \
        sed 's/^_//'
}

# Function to check if file should be excluded
should_exclude() {
    local basename="$1"
    case "$basename" in
        README.md|readme.md|CLAUDE.md|CONTRIBUTING.md|LICENSE.md|CHANGELOG.md)
            return 0
            ;;
        *)
            return 1
            ;;
    esac
}

# Function to check if already snake_case
is_snake_case() {
    local basename="$1"
    # Remove .md extension
    local name="${basename%.md}"
    # Check if contains uppercase or hyphens
    if [[ "$name" =~ [A-Z] ]] || [[ "$name" =~ - ]]; then
        return 1
    fi
    return 0
}

# Process files in specified directories
process_directory() {
    local dir="$1"
    echo -e "${YELLOW}Processing directory: $dir${NC}"

    find "$dir" -type f -name "*.md" | while read -r filepath; do
        local dirname=$(dirname "$filepath")
        local basename=$(basename "$filepath")

        # Skip excluded files
        if should_exclude "$basename"; then
            continue
        fi

        # Skip if already snake_case
        if is_snake_case "$basename"; then
            continue
        fi

        # Convert to snake_case
        local new_basename=$(to_snake_case "$basename")

        # Ensure .md extension
        if [[ ! "$new_basename" =~ \.md$ ]]; then
            new_basename="${new_basename}.md"
        fi

        local new_filepath="$dirname/$new_basename"

        # Skip if source and destination are the same
        if [ "$filepath" = "$new_filepath" ]; then
            continue
        fi

        # Perform rename using git mv for tracking
        if [ -f "$filepath" ]; then
            echo -e "${GREEN}Renaming:${NC} $basename -> $new_basename"
            git mv "$filepath" "$new_filepath" 2>/dev/null || mv "$filepath" "$new_filepath"
            count=$((count + 1)) || true
        fi
    done
}

# Main execution
cd "$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

echo "Starting file rename to snake_case convention..."
echo "================================================"

# Process prompts directory
process_directory "prompts"

# Process domain-agentic-resources directory
process_directory "domain-agentic-resources"

echo "================================================"
echo -e "${GREEN}Rename complete!${NC}"
