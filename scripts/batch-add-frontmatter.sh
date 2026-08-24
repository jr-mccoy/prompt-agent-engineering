#!/bin/bash

# batch-add-frontmatter.sh - Add YAML frontmatter to all prompts missing it
# Usage: ./scripts/batch-add-frontmatter.sh [OPTIONS]
#
# Options:
#   --dry-run             Show what would be done without modifying files
#   --limit N             Process only first N files
#   -v, --verbose         Show detailed progress
#   -h, --help            Show this help message
#
# Examples:
#   ./scripts/batch-add-frontmatter.sh --dry-run
#   ./scripts/batch-add-frontmatter.sh --limit 10
#   ./scripts/batch-add-frontmatter.sh

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color
BOLD='\033[1m'

# Get script directory and repo root
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"

# Default values
DRY_RUN=false
LIMIT=0
VERBOSE=false

# All prompt directories
# Prompt-bearing directories, discovered from the current repository layout
# (domain-* trees plus the self-contained toolkits). Discovered dynamically so
# this list cannot drift behind the repository structure the way a hardcoded
# array did before the domain-* migration.
PROMPT_DIRS=()
while IFS= read -r _d; do
    PROMPT_DIRS+=("$_d")
done < <(cd "$REPO_ROOT" && find . -maxdepth 1 -type d \
    \( -name 'domain-*' -o -name '*-toolkit' -o -name '*-studio' -o -name '*-kit' \
       -o -name 'techniques' -o -name 'authoring' -o -name '*-library' -o -name '*-system' \) \
    -printf '%f\n' | sort)

# Skip patterns
SKIP_PATTERNS=(
    "README.md"
    "GUIDE"
    "WORKFLOW"
    "INDEX"
    "SCHEMA"
    "TEMPLATE"
    "CONTRIBUTING"
    "CHANGELOG"
)

# Counters
PROCESSED=0
ADDED=0
SKIPPED=0
ERRORS=0

# Function to show help
show_help() {
    echo -e "${BOLD}batch-add-frontmatter.sh${NC} - Add YAML frontmatter to all prompts missing it"
    echo ""
    echo -e "${BOLD}USAGE:${NC}"
    echo "    ./scripts/batch-add-frontmatter.sh [OPTIONS]"
    echo ""
    echo -e "${BOLD}OPTIONS:${NC}"
    echo "    --dry-run             Show what would be done without modifying files"
    echo "    --limit N             Process only first N files"
    echo "    -v, --verbose         Show detailed progress"
    echo "    -h, --help            Show this help message"
    echo ""
    echo -e "${BOLD}EXAMPLES:${NC}"
    echo "    ./scripts/batch-add-frontmatter.sh --dry-run"
    echo "    ./scripts/batch-add-frontmatter.sh --limit 10"
    echo "    ./scripts/batch-add-frontmatter.sh"
}

# Function to check if file has frontmatter
has_frontmatter() {
    local file="$1"
    head -n 1 "$file" 2>/dev/null | grep -q "^---$"
}

# Function to check if file should be skipped
should_skip() {
    local file="$1"
    local filename=$(basename "$file")

    for pattern in "${SKIP_PATTERNS[@]}"; do
        if [[ "$filename" == *"$pattern"* ]]; then
            return 0
        fi
    done

    return 1
}

# Function to extract title from H1 or filename
extract_title() {
    local file="$1"
    local title=""

    # Try to find H1 heading
    title=$(grep -m 1 "^# " "$file" 2>/dev/null | sed 's/^# //')

    if [ -z "$title" ]; then
        # Use filename, convert underscores/hyphens to spaces, title case
        local filename=$(basename "$file" .md)
        title=$(echo "$filename" | sed 's/[_-]/ /g' | sed 's/\b\(.\)/\u\1/g')
    fi

    echo "$title"
}

# Function to extract description
extract_description() {
    local file="$1"
    local desc=""

    # Try Objective section
    desc=$(grep -A 1 "^\*\*Objective:\*\*" "$file" 2>/dev/null | tail -n 1 | head -c 180)

    if [ -z "$desc" ]; then
        # Try first paragraph after H1
        desc=$(sed -n '/^# /,/^$/p' "$file" 2>/dev/null | grep -v "^#" | grep -v "^$" | head -n 1 | head -c 180)
    fi

    if [ -z "$desc" ]; then
        # Use the title as description
        desc="$(extract_title "$file")"
    fi

    # Clean up markdown formatting
    desc=$(echo "$desc" | sed 's/\*\*//g' | sed 's/\*//g' | sed 's/`//g')

    echo "$desc"
}

# Function to infer category from file path
infer_category() {
    local file="$1"
    local rel_path="${file#$REPO_ROOT/}"
    local dir=$(dirname "$rel_path")

    # Handle root level
    if [ "$dir" == "." ]; then
        echo "uncategorized"
        return
    fi

    # Return first directory component
    echo "$dir" | cut -d'/' -f1
}

# Function to infer tags from content and path
infer_tags() {
    local file="$1"
    local category=$(infer_category "$file")
    local filename=$(basename "$file" .md)
    local tags=()

    # Add category as first tag
    tags+=("$category")

    # Add subdirectory as tag if exists
    local subdir=$(dirname "${file#$REPO_ROOT/}" | cut -d'/' -f2)
    if [ -n "$subdir" ] && [ "$subdir" != "." ] && [ "$subdir" != "$category" ]; then
        tags+=("$subdir")
    fi

    # Infer from filename
    if [[ "$filename" == *"security"* ]]; then tags+=("security"); fi
    if [[ "$filename" == *"test"* ]]; then tags+=("testing"); fi
    if [[ "$filename" == *"performance"* ]]; then tags+=("performance"); fi
    if [[ "$filename" == *"review"* ]]; then tags+=("review"); fi
    if [[ "$filename" == *"analysis"* ]]; then tags+=("analysis"); fi
    if [[ "$filename" == *"optimization"* ]]; then tags+=("optimization"); fi
    if [[ "$filename" == *"debug"* ]]; then tags+=("debugging"); fi

    # Remove duplicates and format
    printf '%s\n' "${tags[@]}" | sort -u | head -n 5 | while read tag; do
        echo "  - $tag"
    done
}

# Function to generate and add frontmatter
add_frontmatter() {
    local file="$1"
    local rel_path="${file#$REPO_ROOT/}"

    local title=$(extract_title "$file")
    local category=$(infer_category "$file")
    local description=$(extract_description "$file")
    local tags=$(infer_tags "$file")
    local date=$(date +%Y-%m-%d)

    # Build frontmatter
    local frontmatter="---
title: \"$title\"
category: $category
description: \"$description\"
tags:
$tags
updated: \"$date\"
---"

    if [ "$DRY_RUN" = true ]; then
        if [ "$VERBOSE" = true ]; then
            echo -e "${CYAN}Would add to $rel_path:${NC}"
            echo "$frontmatter"
            echo ""
        else
            echo -e "${CYAN}Would add frontmatter to:${NC} $rel_path"
        fi
        return 0
    fi

    # Create temp file with frontmatter + original content
    local temp_file=$(mktemp)
    echo "$frontmatter" > "$temp_file"
    echo "" >> "$temp_file"
    cat "$file" >> "$temp_file"

    # Replace original file
    mv "$temp_file" "$file"

    if [ "$VERBOSE" = true ]; then
        echo -e "${GREEN}Added frontmatter to:${NC} $rel_path"
    fi

    return 0
}

# Parse arguments
while [[ $# -gt 0 ]]; do
    case $1 in
        --dry-run)
            DRY_RUN=true
            shift
            ;;
        --limit)
            LIMIT="$2"
            shift 2
            ;;
        -v|--verbose)
            VERBOSE=true
            shift
            ;;
        -h|--help)
            show_help
            exit 0
            ;;
        *)
            echo -e "${RED}Unknown option: $1${NC}"
            show_help
            exit 1
            ;;
    esac
done

# Main execution
echo -e "${BOLD}Batch Adding Frontmatter${NC}"
if [ "$DRY_RUN" = true ]; then
    echo -e "${YELLOW}(Dry run - no files will be modified)${NC}"
fi
echo ""

for dir in "${PROMPT_DIRS[@]}"; do
    if [ -d "$REPO_ROOT/$dir" ]; then
        while IFS= read -r -d '' file; do
            # Check limit
            if [ "$LIMIT" -gt 0 ] && [ "$PROCESSED" -ge "$LIMIT" ]; then
                break 2
            fi

            # Check if should skip
            if should_skip "$file"; then
                if [ "$VERBOSE" = true ]; then
                    echo -e "${YELLOW}SKIP${NC} $(basename "$file") (excluded pattern)"
                fi
                SKIPPED=$((SKIPPED + 1))
                continue
            fi

            PROCESSED=$((PROCESSED + 1))

            # Check if already has frontmatter
            if has_frontmatter "$file"; then
                if [ "$VERBOSE" = true ]; then
                    rel_path="${file#$REPO_ROOT/}"
                    echo -e "${YELLOW}SKIP${NC} $rel_path (already has frontmatter)"
                fi
                SKIPPED=$((SKIPPED + 1))
                continue
            fi

            # Add frontmatter
            if add_frontmatter "$file"; then
                ADDED=$((ADDED + 1))
            else
                ERRORS=$((ERRORS + 1))
            fi

        done < <(find "$REPO_ROOT/$dir" -name "*.md" -type f -print0 2>/dev/null)
    fi
done

# Summary
echo ""
echo -e "${BOLD}Summary${NC}"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo -e "  Files processed:  $PROCESSED"
echo -e "  ${GREEN}Frontmatter added:${NC} $ADDED"
echo -e "  ${YELLOW}Skipped:${NC}           $SKIPPED"
echo -e "  ${RED}Errors:${NC}            $ERRORS"
echo ""

if [ "$DRY_RUN" = true ]; then
    echo -e "${YELLOW}This was a dry run. Run without --dry-run to apply changes.${NC}"
fi

exit 0
