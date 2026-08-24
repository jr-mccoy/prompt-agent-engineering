#!/bin/bash

# find-prompt.sh - Search and filter prompts in the Prompting-Guides repository
# Usage: ./scripts/find-prompt.sh [OPTIONS] [SEARCH_TERM]
#
# Options:
#   -c, --category CATEGORY   Filter by category (e.g., testing, devops, security)
#   -t, --technique CODE      Filter by technique code (e.g., ST-01, RT-02)
#   -l, --list-categories     List all available categories
#   -s, --show PATH           Show full content of a prompt
#   -h, --help                Show this help message
#
# Examples:
#   ./scripts/find-prompt.sh security           # Search for prompts containing "security"
#   ./scripts/find-prompt.sh -c testing         # List all testing prompts
#   ./scripts/find-prompt.sh -t ST-01           # Find prompts using technique ST-01
#   ./scripts/find-prompt.sh -l                 # List all categories
#   ./scripts/find-prompt.sh -s testing/testing_unit_test_generation.md

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

# Directories to search (prompt directories)
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

# Function to show help
show_help() {
    echo -e "${BOLD}find-prompt.sh${NC} - Search and filter prompts in the Prompting-Guides repository"
    echo ""
    echo -e "${BOLD}USAGE:${NC}"
    echo "    ./scripts/find-prompt.sh [OPTIONS] [SEARCH_TERM]"
    echo ""
    echo -e "${BOLD}OPTIONS:${NC}"
    echo "    -c, --category CATEGORY   Filter by category (e.g., testing, devops, security)"
    echo "    -t, --technique CODE      Filter by technique code (e.g., ST-01, RT-02)"
    echo "    -l, --list-categories     List all available categories"
    echo "    -s, --show PATH           Show full content of a prompt"
    echo "    -a, --all                 List all prompts"
    echo "    -n, --count               Show count only"
    echo "    -h, --help                Show this help message"
    echo ""
    echo -e "${BOLD}EXAMPLES:${NC}"
    echo "    ./scripts/find-prompt.sh security"
    echo "        # Search for prompts containing 'security'"
    echo ""
    echo "    ./scripts/find-prompt.sh -c testing"
    echo "        # List all prompts in the testing category"
    echo ""
    echo "    ./scripts/find-prompt.sh -t ST-01"
    echo "        # Find prompts using technique ST-01"
    echo ""
    echo "    ./scripts/find-prompt.sh -l"
    echo "        # List all available categories"
    echo ""
    echo "    ./scripts/find-prompt.sh -s testing/testing_unit_test_generation.md"
    echo "        # Show content of a specific prompt"
    echo ""
    echo "    ./scripts/find-prompt.sh -a -n"
    echo "        # Count all prompts"
}

# Function to list categories
list_categories() {
    echo -e "${BOLD}Available Categories:${NC}"
    echo ""

    for dir in "${PROMPT_DIRS[@]}"; do
        if [ -d "$REPO_ROOT/$dir" ]; then
            count=$(find "$REPO_ROOT/$dir" -name "*.md" -type f ! -name "README.md" ! -name "*GUIDE*" ! -name "*WORKFLOW*" 2>/dev/null | wc -l)
            echo -e "  ${CYAN}$dir${NC} ($count prompts)"

            # List subdirectories if they exist
            if [ -d "$REPO_ROOT/$dir" ]; then
                for subdir in "$REPO_ROOT/$dir"/*/; do
                    if [ -d "$subdir" ]; then
                        subname=$(basename "$subdir")
                        subcount=$(find "$subdir" -name "*.md" -type f ! -name "README.md" 2>/dev/null | wc -l)
                        if [ "$subcount" -gt 0 ]; then
                            echo -e "    └── ${BLUE}$subname${NC} ($subcount prompts)"
                        fi
                    fi
                done
            fi
        fi
    done
}

# Function to search by keyword
search_keyword() {
    local keyword="$1"
    local count_only="$2"

    echo -e "${BOLD}Searching for:${NC} ${YELLOW}$keyword${NC}"
    echo ""

    local results=()
    local total=0

    for dir in "${PROMPT_DIRS[@]}"; do
        if [ -d "$REPO_ROOT/$dir" ]; then
            while IFS= read -r file; do
                if [ -n "$file" ]; then
                    results+=("$file")
                    total=$((total + 1))
                fi
            done < <(grep -ril "$keyword" "$REPO_ROOT/$dir" --include="*.md" 2>/dev/null || true)
        fi
    done

    if [ "$count_only" = "true" ]; then
        echo -e "${GREEN}Found $total prompts matching '$keyword'${NC}"
    else
        if [ ${#results[@]} -eq 0 ]; then
            echo -e "${RED}No prompts found matching '$keyword'${NC}"
        else
            echo -e "${GREEN}Found $total prompts:${NC}"
            echo ""
            for file in "${results[@]}"; do
                relative_path="${file#$REPO_ROOT/}"
                # Get first line (title) from file
                title=$(head -1 "$file" | sed 's/^#\s*//')
                echo -e "  ${CYAN}$relative_path${NC}"
                echo -e "    ${BLUE}$title${NC}"
            done
        fi
    fi
}

# Function to filter by category
filter_category() {
    local category="$1"
    local count_only="$2"

    echo -e "${BOLD}Category:${NC} ${YELLOW}$category${NC}"
    echo ""

    local total=0
    local found_dir=""

    # Find the matching directory
    for dir in "${PROMPT_DIRS[@]}"; do
        if [[ "$dir" == *"$category"* ]]; then
            found_dir="$dir"
            break
        fi
    done

    # Also check subdirectories
    if [ -z "$found_dir" ]; then
        for dir in "${PROMPT_DIRS[@]}"; do
            if [ -d "$REPO_ROOT/$dir/$category" ]; then
                found_dir="$dir/$category"
                break
            fi
        done
    fi

    if [ -z "$found_dir" ] || [ ! -d "$REPO_ROOT/$found_dir" ]; then
        echo -e "${RED}Category '$category' not found${NC}"
        echo ""
        echo "Use -l to list available categories"
        exit 1
    fi

    if [ "$count_only" = "true" ]; then
        total=$(find "$REPO_ROOT/$found_dir" -name "*.md" -type f ! -name "README.md" ! -name "*GUIDE*" ! -name "*WORKFLOW*" 2>/dev/null | wc -l)
        echo -e "${GREEN}Found $total prompts in '$category'${NC}"
    else
        echo -e "${GREEN}Prompts in $found_dir:${NC}"
        echo ""

        while IFS= read -r file; do
            if [ -n "$file" ]; then
                relative_path="${file#$REPO_ROOT/}"
                title=$(head -1 "$file" | sed 's/^#\s*//')
                echo -e "  ${CYAN}$relative_path${NC}"
                echo -e "    ${BLUE}$title${NC}"
                total=$((total + 1))
            fi
        done < <(find "$REPO_ROOT/$found_dir" -name "*.md" -type f ! -name "README.md" ! -name "*GUIDE*" ! -name "*WORKFLOW*" 2>/dev/null | sort)

        echo ""
        echo -e "${GREEN}Total: $total prompts${NC}"
    fi
}

# Function to search by technique
search_technique() {
    local technique="$1"
    local count_only="$2"

    echo -e "${BOLD}Searching for technique:${NC} ${YELLOW}$technique${NC}"
    echo ""

    local results=()
    local total=0

    for dir in "${PROMPT_DIRS[@]}"; do
        if [ -d "$REPO_ROOT/$dir" ]; then
            while IFS= read -r file; do
                if [ -n "$file" ]; then
                    results+=("$file")
                    total=$((total + 1))
                fi
            done < <(grep -ril "$technique" "$REPO_ROOT/$dir" --include="*.md" 2>/dev/null || true)
        fi
    done

    if [ "$count_only" = "true" ]; then
        echo -e "${GREEN}Found $total prompts using technique '$technique'${NC}"
    else
        if [ ${#results[@]} -eq 0 ]; then
            echo -e "${RED}No prompts found using technique '$technique'${NC}"
        else
            echo -e "${GREEN}Found $total prompts:${NC}"
            echo ""
            for file in "${results[@]}"; do
                relative_path="${file#$REPO_ROOT/}"
                title=$(head -1 "$file" | sed 's/^#\s*//')
                echo -e "  ${CYAN}$relative_path${NC}"
                echo -e "    ${BLUE}$title${NC}"
            done
        fi
    fi
}

# Function to show prompt content
show_prompt() {
    local path="$1"
    local full_path="$REPO_ROOT/$path"

    if [ ! -f "$full_path" ]; then
        # Try to find the file
        found=$(find "$REPO_ROOT" -name "$(basename "$path")" -type f 2>/dev/null | head -1)
        if [ -n "$found" ]; then
            full_path="$found"
        else
            echo -e "${RED}Prompt not found: $path${NC}"
            exit 1
        fi
    fi

    echo -e "${BOLD}Prompt:${NC} ${CYAN}${full_path#$REPO_ROOT/}${NC}"
    echo ""
    echo "---"
    cat "$full_path"
}

# Function to list all prompts
list_all() {
    local count_only="$1"
    local total=0

    echo -e "${BOLD}All Prompts${NC}"
    echo ""

    for dir in "${PROMPT_DIRS[@]}"; do
        if [ -d "$REPO_ROOT/$dir" ]; then
            while IFS= read -r file; do
                if [ -n "$file" ]; then
                    if [ "$count_only" != "true" ]; then
                        relative_path="${file#$REPO_ROOT/}"
                        title=$(head -1 "$file" | sed 's/^#\s*//')
                        echo -e "  ${CYAN}$relative_path${NC}"
                    fi
                    total=$((total + 1))
                fi
            done < <(find "$REPO_ROOT/$dir" -name "*.md" -type f ! -name "README.md" ! -name "*GUIDE*" ! -name "*WORKFLOW*" ! -name "CONTRIBUTING*" 2>/dev/null | sort)
        fi
    done

    echo ""
    echo -e "${GREEN}Total: $total prompts${NC}"
}

# Parse arguments
CATEGORY=""
TECHNIQUE=""
SEARCH_TERM=""
SHOW_PATH=""
LIST_CATS=false
LIST_ALL=false
COUNT_ONLY=false

while [[ $# -gt 0 ]]; do
    case $1 in
        -c|--category)
            CATEGORY="$2"
            shift 2
            ;;
        -t|--technique)
            TECHNIQUE="$2"
            shift 2
            ;;
        -l|--list-categories)
            LIST_CATS=true
            shift
            ;;
        -s|--show)
            SHOW_PATH="$2"
            shift 2
            ;;
        -a|--all)
            LIST_ALL=true
            shift
            ;;
        -n|--count)
            COUNT_ONLY=true
            shift
            ;;
        -h|--help)
            show_help
            exit 0
            ;;
        -*)
            echo -e "${RED}Unknown option: $1${NC}"
            echo "Use -h for help"
            exit 1
            ;;
        *)
            SEARCH_TERM="$1"
            shift
            ;;
    esac
done

# Execute based on options
if [ "$LIST_CATS" = true ]; then
    list_categories
elif [ -n "$SHOW_PATH" ]; then
    show_prompt "$SHOW_PATH"
elif [ -n "$CATEGORY" ]; then
    filter_category "$CATEGORY" "$COUNT_ONLY"
elif [ -n "$TECHNIQUE" ]; then
    search_technique "$TECHNIQUE" "$COUNT_ONLY"
elif [ "$LIST_ALL" = true ]; then
    list_all "$COUNT_ONLY"
elif [ -n "$SEARCH_TERM" ]; then
    search_keyword "$SEARCH_TERM" "$COUNT_ONLY"
else
    show_help
fi
