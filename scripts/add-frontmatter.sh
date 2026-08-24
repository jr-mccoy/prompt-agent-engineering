#!/bin/bash

# add-frontmatter.sh - Add YAML frontmatter template to prompt files
# Usage: ./scripts/add-frontmatter.sh [OPTIONS] FILE
#
# Options:
#   -t, --title TITLE           Set the title
#   -c, --category CATEGORY     Set the category
#   -d, --description DESC      Set the description
#   -D, --difficulty LEVEL      Set difficulty (beginner, intermediate, advanced)
#   --dry-run                   Show what would be added without modifying
#   -h, --help                  Show this help message
#
# Examples:
#   ./scripts/add-frontmatter.sh testing/testing_unit_test_generation.md
#   ./scripts/add-frontmatter.sh -t "Unit Test Generation" -c testing testing/test.md
#   ./scripts/add-frontmatter.sh --dry-run code-analysis/quality/quality_complexity.md

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
TITLE=""
CATEGORY=""
DESCRIPTION=""
DIFFICULTY=""
DRY_RUN=false

# Function to show help
show_help() {
    echo -e "${BOLD}add-frontmatter.sh${NC} - Add YAML frontmatter template to prompt files"
    echo ""
    echo -e "${BOLD}USAGE:${NC}"
    echo "    ./scripts/add-frontmatter.sh [OPTIONS] FILE"
    echo ""
    echo -e "${BOLD}OPTIONS:${NC}"
    echo "    -t, --title TITLE           Set the title"
    echo "    -c, --category CATEGORY     Set the category"
    echo "    -d, --description DESC      Set the description"
    echo "    -D, --difficulty LEVEL      Set difficulty (beginner, intermediate, advanced)"
    echo "    --dry-run                   Show what would be added without modifying"
    echo "    -h, --help                  Show this help message"
    echo ""
    echo -e "${BOLD}EXAMPLES:${NC}"
    echo "    ./scripts/add-frontmatter.sh testing/testing_unit_test_generation.md"
    echo "    ./scripts/add-frontmatter.sh -t \"Unit Test Generation\" -c testing testing/test.md"
    echo "    ./scripts/add-frontmatter.sh --dry-run code-analysis/quality/quality_complexity.md"
    echo ""
    echo -e "${BOLD}NOTES:${NC}"
    echo "    - If title is not provided, it will be extracted from the first H1 header"
    echo "    - If category is not provided, it will be inferred from the file path"
    echo "    - If description is not provided, it will be extracted from the Objective section"
    echo "    - Files that already have frontmatter will be skipped"
}

# Function to check if file has frontmatter
has_frontmatter() {
    local file="$1"
    head -n 1 "$file" | grep -q "^---$"
}

# Function to extract title from H1
extract_title() {
    local file="$1"
    grep -m 1 "^# " "$file" | sed 's/^# //' | head -n 1
}

# Function to extract description from Objective
extract_description() {
    local file="$1"
    # Try to find Objective section
    local desc=$(grep -A 1 "^\*\*Objective:\*\*" "$file" 2>/dev/null | tail -n 1 | head -c 200)
    if [ -z "$desc" ]; then
        # Try to find first paragraph after H1
        desc=$(sed -n '/^# /,/^$/p' "$file" | tail -n +2 | head -n 1 | head -c 200)
    fi
    echo "$desc"
}

# Function to infer category from file path
infer_category() {
    local file="$1"
    local rel_path="${file#$REPO_ROOT/}"

    # Get the directory part
    local dir=$(dirname "$rel_path")

    # Handle special cases
    case "$dir" in
        "code-analysis/quality"|"code-analysis/security"|"code-analysis/architecture"|"code-analysis/performance"|"code-analysis/evolution"|"code-analysis/database")
            echo "$dir"
            ;;
        "code-analysis")
            # Try to determine subcategory from filename
            local filename=$(basename "$file" .md)
            if [[ "$filename" == *"security"* ]]; then
                echo "code-analysis/security"
            elif [[ "$filename" == *"quality"* ]] || [[ "$filename" == *"complexity"* ]] || [[ "$filename" == *"duplication"* ]]; then
                echo "code-analysis/quality"
            elif [[ "$filename" == *"performance"* ]] || [[ "$filename" == *"bottleneck"* ]]; then
                echo "code-analysis/performance"
            elif [[ "$filename" == *"architecture"* ]] || [[ "$filename" == *"design"* ]]; then
                echo "code-analysis/architecture"
            else
                echo "code-analysis"
            fi
            ;;
        "agency-agents/"*)
            echo "$dir"
            ;;
        *)
            echo "$dir"
            ;;
    esac
}

# Function to extract techniques from file
extract_techniques() {
    local file="$1"
    # Look for Techniques Used section
    grep -E "^- [A-Z]{2}-[0-9]{2}" "$file" 2>/dev/null | sed 's/^- /  - /' | head -n 10
}

# Function to generate frontmatter
generate_frontmatter() {
    local file="$1"
    local title="$2"
    local category="$3"
    local description="$4"
    local difficulty="$5"

    # Extract title if not provided
    if [ -z "$title" ]; then
        title=$(extract_title "$file")
    fi

    # Infer category if not provided
    if [ -z "$category" ]; then
        category=$(infer_category "$file")
    fi

    # Extract description if not provided
    if [ -z "$description" ]; then
        description=$(extract_description "$file")
        # Clean up description - remove markdown formatting
        description=$(echo "$description" | sed 's/\*\*//g' | sed 's/\*//g' | head -c 200)
    fi

    # Extract techniques
    local techniques=$(extract_techniques "$file")

    # Build frontmatter
    echo "---"
    echo "title: \"$title\""
    echo "category: $category"
    echo "description: \"$description\""

    if [ -n "$techniques" ]; then
        echo "techniques:"
        echo "$techniques"
    fi

    if [ -n "$difficulty" ]; then
        echo "difficulty: $difficulty"
    fi

    echo "updated: \"$(date +%Y-%m-%d)\""
    echo "---"
}

# Parse arguments
while [[ $# -gt 0 ]]; do
    case $1 in
        -t|--title)
            TITLE="$2"
            shift 2
            ;;
        -c|--category)
            CATEGORY="$2"
            shift 2
            ;;
        -d|--description)
            DESCRIPTION="$2"
            shift 2
            ;;
        -D|--difficulty)
            DIFFICULTY="$2"
            shift 2
            ;;
        --dry-run)
            DRY_RUN=true
            shift
            ;;
        -h|--help)
            show_help
            exit 0
            ;;
        *)
            FILE="$1"
            shift
            ;;
    esac
done

# Check if file is provided
if [ -z "$FILE" ]; then
    echo -e "${RED}Error: No file specified${NC}"
    echo ""
    show_help
    exit 1
fi

# Resolve file path
if [[ "$FILE" != /* ]]; then
    FILE="$REPO_ROOT/$FILE"
fi

# Check if file exists
if [ ! -f "$FILE" ]; then
    echo -e "${RED}Error: File not found: $FILE${NC}"
    exit 1
fi

# Check if file already has frontmatter
if has_frontmatter "$FILE"; then
    echo -e "${YELLOW}Warning: File already has frontmatter: $FILE${NC}"
    echo "Skipping..."
    exit 0
fi

# Generate frontmatter
FRONTMATTER=$(generate_frontmatter "$FILE" "$TITLE" "$CATEGORY" "$DESCRIPTION" "$DIFFICULTY")

if [ "$DRY_RUN" = true ]; then
    echo -e "${BOLD}Dry run - would add to $FILE:${NC}"
    echo ""
    echo -e "${CYAN}$FRONTMATTER${NC}"
    echo ""
else
    # Create temp file with frontmatter + original content
    TEMP_FILE=$(mktemp)
    echo "$FRONTMATTER" > "$TEMP_FILE"
    echo "" >> "$TEMP_FILE"
    cat "$FILE" >> "$TEMP_FILE"

    # Replace original file
    mv "$TEMP_FILE" "$FILE"

    echo -e "${GREEN}Added frontmatter to: $FILE${NC}"
fi
