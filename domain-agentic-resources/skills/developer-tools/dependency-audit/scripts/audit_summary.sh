#!/usr/bin/env bash
# audit_summary.sh — Quick dependency audit summary for detected ecosystems
# Usage: bash audit_summary.sh [project_directory]
#
# Detects package ecosystems in the project and runs available audit tools.
# Outputs a unified summary of vulnerabilities found.

set -euo pipefail

PROJECT_DIR="${1:-.}"
FOUND_ECOSYSTEMS=0
TOTAL_VULNS=0

echo "======================================"
echo "  Dependency Audit Summary"
echo "  Directory: ${PROJECT_DIR}"
echo "  Date: $(date -u +%Y-%m-%dT%H:%M:%SZ)"
echo "======================================"
echo ""

# Node.js
if [ -f "${PROJECT_DIR}/package.json" ]; then
    FOUND_ECOSYSTEMS=$((FOUND_ECOSYSTEMS + 1))
    echo "## Node.js (npm)"
    echo "---"
    if command -v npm &> /dev/null; then
        AUDIT_OUTPUT=$(cd "${PROJECT_DIR}" && npm audit --json 2>/dev/null || true)
        VULN_COUNT=$(echo "${AUDIT_OUTPUT}" | python3 -c "
import sys, json
try:
    data = json.load(sys.stdin)
    total = data.get('metadata', {}).get('vulnerabilities', {})
    count = sum(total.values()) if isinstance(total, dict) else 0
    print(count)
except: print(0)
" 2>/dev/null || echo "0")
        TOTAL_VULNS=$((TOTAL_VULNS + VULN_COUNT))
        echo "Vulnerabilities found: ${VULN_COUNT}"

        OUTDATED=$(cd "${PROJECT_DIR}" && npm outdated --json 2>/dev/null | python3 -c "
import sys, json
try:
    data = json.load(sys.stdin)
    print(len(data))
except: print(0)
" 2>/dev/null || echo "0")
        echo "Outdated packages: ${OUTDATED}"
    else
        echo "npm not found — skipping"
    fi
    echo ""
fi

# Python
if [ -f "${PROJECT_DIR}/requirements.txt" ] || [ -f "${PROJECT_DIR}/pyproject.toml" ]; then
    FOUND_ECOSYSTEMS=$((FOUND_ECOSYSTEMS + 1))
    echo "## Python"
    echo "---"
    if command -v pip-audit &> /dev/null; then
        VULN_COUNT=$(cd "${PROJECT_DIR}" && pip-audit --format json 2>/dev/null | python3 -c "
import sys, json
try:
    data = json.load(sys.stdin)
    print(len([v for v in data if v.get('vulns')]))
except: print(0)
" 2>/dev/null || echo "0")
        TOTAL_VULNS=$((TOTAL_VULNS + VULN_COUNT))
        echo "Vulnerable packages: ${VULN_COUNT}"
    elif command -v safety &> /dev/null; then
        VULN_COUNT=$(cd "${PROJECT_DIR}" && safety check --json 2>/dev/null | python3 -c "
import sys, json
try: print(len(json.load(sys.stdin)))
except: print(0)
" 2>/dev/null || echo "0")
        TOTAL_VULNS=$((TOTAL_VULNS + VULN_COUNT))
        echo "Vulnerable packages: ${VULN_COUNT}"
    else
        echo "pip-audit/safety not found — skipping vulnerability scan"
    fi
    echo ""
fi

# Go
if [ -f "${PROJECT_DIR}/go.mod" ]; then
    FOUND_ECOSYSTEMS=$((FOUND_ECOSYSTEMS + 1))
    echo "## Go"
    echo "---"
    if command -v govulncheck &> /dev/null; then
        VULN_COUNT=$(cd "${PROJECT_DIR}" && govulncheck -json ./... 2>/dev/null | python3 -c "
import sys, json
count = 0
for line in sys.stdin:
    try:
        obj = json.loads(line)
        if 'osv' in obj: count += 1
    except: pass
print(count)
" 2>/dev/null || echo "0")
        TOTAL_VULNS=$((TOTAL_VULNS + VULN_COUNT))
        echo "Vulnerabilities found: ${VULN_COUNT}"
    else
        echo "govulncheck not found — skipping"
    fi
    echo ""
fi

# Rust
if [ -f "${PROJECT_DIR}/Cargo.toml" ]; then
    FOUND_ECOSYSTEMS=$((FOUND_ECOSYSTEMS + 1))
    echo "## Rust"
    echo "---"
    if command -v cargo-audit &> /dev/null; then
        VULN_COUNT=$(cd "${PROJECT_DIR}" && cargo audit --json 2>/dev/null | python3 -c "
import sys, json
try:
    data = json.load(sys.stdin)
    print(len(data.get('vulnerabilities', {}).get('list', [])))
except: print(0)
" 2>/dev/null || echo "0")
        TOTAL_VULNS=$((TOTAL_VULNS + VULN_COUNT))
        echo "Vulnerabilities found: ${VULN_COUNT}"
    else
        echo "cargo-audit not found — skipping"
    fi
    echo ""
fi

# Ruby
if [ -f "${PROJECT_DIR}/Gemfile" ]; then
    FOUND_ECOSYSTEMS=$((FOUND_ECOSYSTEMS + 1))
    echo "## Ruby"
    echo "---"
    if command -v bundle-audit &> /dev/null; then
        VULN_COUNT=$(cd "${PROJECT_DIR}" && bundle-audit check 2>/dev/null | grep -c "^Name:" || echo "0")
        TOTAL_VULNS=$((TOTAL_VULNS + VULN_COUNT))
        echo "Vulnerabilities found: ${VULN_COUNT}"
    else
        echo "bundle-audit not found — skipping"
    fi
    echo ""
fi

# Summary
echo "======================================"
echo "  SUMMARY"
echo "======================================"
echo "Ecosystems detected: ${FOUND_ECOSYSTEMS}"
echo "Total vulnerabilities: ${TOTAL_VULNS}"

if [ "${TOTAL_VULNS}" -gt 0 ]; then
    echo "Status: ACTION REQUIRED"
    exit 1
else
    echo "Status: CLEAN"
    exit 0
fi
