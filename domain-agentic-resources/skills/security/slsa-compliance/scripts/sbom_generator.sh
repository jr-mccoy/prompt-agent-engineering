#!/bin/bash
#
# SBOM Generator Script
# Generates Software Bill of Materials (SBOM) for a project
#
# Usage: ./sbom_generator.sh [OPTIONS]
#
# Options:
#   -d, --directory PATH    Directory to scan (default: current directory)
#   -f, --format FORMAT     Output format: spdx-json, cyclonedx-json, cyclonedx-xml (default: spdx-json)
#   -o, --output FILE       Output file path (default: sbom.<format-extension>)
#   -t, --tool TOOL         Tool to use: syft, cdxgen, trivy, auto (default: auto)
#   -h, --help              Show this help message
#
# Requirements:
#   - One of: syft, cdxgen, trivy
#   - jq (optional, for JSON validation)

set -euo pipefail

# Default values
SCAN_DIR="."
FORMAT="spdx-json"
OUTPUT=""
TOOL="auto"
VERBOSE=0

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

log_info() {
    echo -e "${BLUE}[INFO]${NC} $1"
}

log_success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1"
}

log_warn() {
    echo -e "${YELLOW}[WARN]${NC} $1"
}

log_error() {
    echo -e "${RED}[ERROR]${NC} $1" >&2
}

show_help() {
    cat << EOF
SBOM Generator - Generate Software Bill of Materials

Usage: $0 [OPTIONS]

Options:
  -d, --directory PATH    Directory to scan (default: current directory)
  -f, --format FORMAT     Output format (default: spdx-json)
                          Supported: spdx-json, spdx-tag-value, cyclonedx-json, cyclonedx-xml
  -o, --output FILE       Output file path (auto-generated if not specified)
  -t, --tool TOOL         Tool to use (default: auto)
                          Supported: syft, cdxgen, trivy, auto
  -v, --verbose           Enable verbose output
  -h, --help              Show this help message

Examples:
  $0                                    # Scan current directory, auto-detect tool
  $0 -d ./myproject -f cyclonedx-json   # Scan myproject with CycloneDX format
  $0 -t syft -o release-sbom.json       # Use Syft specifically

Supported ecosystems:
  - Node.js (package.json, package-lock.json, yarn.lock)
  - Python (requirements.txt, Pipfile, pyproject.toml)
  - Go (go.mod, go.sum)
  - Java (pom.xml, build.gradle)
  - Ruby (Gemfile, Gemfile.lock)
  - Rust (Cargo.toml, Cargo.lock)
  - .NET (*.csproj, packages.config)
  - PHP (composer.json, composer.lock)
  - And many more...
EOF
}

check_tool() {
    local tool=$1
    if command -v "$tool" &> /dev/null; then
        return 0
    fi
    return 1
}

detect_tool() {
    local tools=("syft" "cdxgen" "trivy")
    for tool in "${tools[@]}"; do
        if check_tool "$tool"; then
            echo "$tool"
            return 0
        fi
    done
    return 1
}

get_file_extension() {
    local format=$1
    case "$format" in
        spdx-json|cyclonedx-json)
            echo "json"
            ;;
        spdx-tag-value)
            echo "spdx"
            ;;
        cyclonedx-xml)
            echo "xml"
            ;;
        *)
            echo "json"
            ;;
    esac
}

generate_with_syft() {
    local dir=$1
    local format=$2
    local output=$3

    local syft_format
    case "$format" in
        spdx-json)
            syft_format="spdx-json"
            ;;
        spdx-tag-value)
            syft_format="spdx-tag-value"
            ;;
        cyclonedx-json)
            syft_format="cyclonedx-json"
            ;;
        cyclonedx-xml)
            syft_format="cyclonedx-xml"
            ;;
        *)
            log_error "Unsupported format for Syft: $format"
            return 1
            ;;
    esac

    log_info "Running Syft scan on $dir..."
    syft scan "dir:$dir" -o "$syft_format" --file "$output"
}

generate_with_cdxgen() {
    local dir=$1
    local format=$2
    local output=$3

    if [[ "$format" != "cyclonedx-json" && "$format" != "cyclonedx-xml" ]]; then
        log_warn "cdxgen only supports CycloneDX format. Converting request to cyclonedx-json."
        format="cyclonedx-json"
    fi

    local spec_version="1.5"
    local output_format="json"
    if [[ "$format" == "cyclonedx-xml" ]]; then
        output_format="xml"
    fi

    log_info "Running cdxgen scan on $dir..."
    cdxgen -o "$output" --spec-version "$spec_version" --format "$output_format" "$dir"
}

generate_with_trivy() {
    local dir=$1
    local format=$2
    local output=$3

    local trivy_format
    case "$format" in
        spdx-json)
            trivy_format="spdx-json"
            ;;
        cyclonedx-json)
            trivy_format="cyclonedx"
            ;;
        *)
            log_warn "Trivy supports spdx-json and cyclonedx. Defaulting to spdx-json."
            trivy_format="spdx-json"
            ;;
    esac

    log_info "Running Trivy scan on $dir..."
    trivy fs --format "$trivy_format" --output "$output" "$dir"
}

validate_sbom() {
    local file=$1
    local format=$2

    if ! check_tool "jq"; then
        log_warn "jq not installed, skipping SBOM validation"
        return 0
    fi

    if [[ "$format" == *"json"* ]]; then
        if jq empty "$file" 2>/dev/null; then
            log_success "SBOM is valid JSON"

            # Check for key fields based on format
            if [[ "$format" == "spdx"* ]]; then
                if jq -e '.spdxVersion' "$file" > /dev/null 2>&1; then
                    local version
                    version=$(jq -r '.spdxVersion' "$file")
                    log_info "SPDX Version: $version"

                    local pkg_count
                    pkg_count=$(jq '.packages | length' "$file")
                    log_info "Packages found: $pkg_count"
                fi
            elif [[ "$format" == "cyclonedx"* ]]; then
                if jq -e '.bomFormat' "$file" > /dev/null 2>&1; then
                    local version
                    version=$(jq -r '.specVersion' "$file")
                    log_info "CycloneDX Version: $version"

                    local comp_count
                    comp_count=$(jq '.components | length' "$file")
                    log_info "Components found: $comp_count"
                fi
            fi
            return 0
        else
            log_error "Generated SBOM is not valid JSON"
            return 1
        fi
    fi
    return 0
}

# Parse arguments
while [[ $# -gt 0 ]]; do
    case $1 in
        -d|--directory)
            SCAN_DIR="$2"
            shift 2
            ;;
        -f|--format)
            FORMAT="$2"
            shift 2
            ;;
        -o|--output)
            OUTPUT="$2"
            shift 2
            ;;
        -t|--tool)
            TOOL="$2"
            shift 2
            ;;
        -v|--verbose)
            VERBOSE=1
            shift
            ;;
        -h|--help)
            show_help
            exit 0
            ;;
        *)
            log_error "Unknown option: $1"
            show_help
            exit 1
            ;;
    esac
done

# Validate scan directory
if [[ ! -d "$SCAN_DIR" ]]; then
    log_error "Directory not found: $SCAN_DIR"
    exit 1
fi

SCAN_DIR=$(realpath "$SCAN_DIR")
log_info "Scanning directory: $SCAN_DIR"

# Detect or validate tool
if [[ "$TOOL" == "auto" ]]; then
    TOOL=$(detect_tool) || {
        log_error "No SBOM tool found. Please install one of: syft, cdxgen, trivy"
        echo ""
        echo "Installation options:"
        echo "  Syft:   curl -sSfL https://raw.githubusercontent.com/anchore/syft/main/install.sh | sh -s -- -b /usr/local/bin"
        echo "  cdxgen: npm install -g @cyclonedx/cdxgen"
        echo "  Trivy:  https://aquasecurity.github.io/trivy/latest/getting-started/installation/"
        exit 1
    }
    log_info "Auto-detected tool: $TOOL"
else
    if ! check_tool "$TOOL"; then
        log_error "Tool not found: $TOOL"
        exit 1
    fi
fi

# Set default output filename if not specified
if [[ -z "$OUTPUT" ]]; then
    ext=$(get_file_extension "$FORMAT")
    OUTPUT="sbom.${ext}"
fi

log_info "Output format: $FORMAT"
log_info "Output file: $OUTPUT"

# Generate SBOM
case "$TOOL" in
    syft)
        generate_with_syft "$SCAN_DIR" "$FORMAT" "$OUTPUT"
        ;;
    cdxgen)
        generate_with_cdxgen "$SCAN_DIR" "$FORMAT" "$OUTPUT"
        ;;
    trivy)
        generate_with_trivy "$SCAN_DIR" "$FORMAT" "$OUTPUT"
        ;;
    *)
        log_error "Unknown tool: $TOOL"
        exit 1
        ;;
esac

# Validate output
if [[ -f "$OUTPUT" ]]; then
    validate_sbom "$OUTPUT" "$FORMAT"
    log_success "SBOM generated successfully: $OUTPUT"

    # Show file size
    local size
    size=$(du -h "$OUTPUT" | cut -f1)
    log_info "File size: $size"
else
    log_error "Failed to generate SBOM"
    exit 1
fi
