#!/bin/bash
# OpenTelemetry Setup Validation Script
# Validates that OpenTelemetry is properly configured

set -e

echo "=== OpenTelemetry Setup Validation ==="
echo ""

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

ERRORS=0
WARNINGS=0

# Check environment variables
echo "Checking environment variables..."

if [ -z "$OTEL_SERVICE_NAME" ]; then
    echo -e "${YELLOW}WARNING: OTEL_SERVICE_NAME not set${NC}"
    WARNINGS=$((WARNINGS + 1))
else
    echo -e "${GREEN}✓ OTEL_SERVICE_NAME: $OTEL_SERVICE_NAME${NC}"
fi

if [ -z "$OTEL_EXPORTER_OTLP_ENDPOINT" ]; then
    echo -e "${YELLOW}WARNING: OTEL_EXPORTER_OTLP_ENDPOINT not set (using default)${NC}"
    OTEL_ENDPOINT="http://localhost:4318"
    WARNINGS=$((WARNINGS + 1))
else
    OTEL_ENDPOINT="$OTEL_EXPORTER_OTLP_ENDPOINT"
    echo -e "${GREEN}✓ OTEL_EXPORTER_OTLP_ENDPOINT: $OTEL_ENDPOINT${NC}"
fi

echo ""

# Check OTLP endpoint connectivity
echo "Checking OTLP endpoint connectivity..."

TRACES_URL="${OTEL_ENDPOINT}/v1/traces"
METRICS_URL="${OTEL_ENDPOINT}/v1/metrics"

# Check traces endpoint
if curl -s -o /dev/null -w "%{http_code}" -X POST "$TRACES_URL" \
    -H "Content-Type: application/json" -d '{}' | grep -q "200\|400\|405"; then
    echo -e "${GREEN}✓ Traces endpoint reachable: $TRACES_URL${NC}"
else
    echo -e "${RED}✗ Cannot reach traces endpoint: $TRACES_URL${NC}"
    ERRORS=$((ERRORS + 1))
fi

# Check metrics endpoint
if curl -s -o /dev/null -w "%{http_code}" -X POST "$METRICS_URL" \
    -H "Content-Type: application/json" -d '{}' | grep -q "200\|400\|405"; then
    echo -e "${GREEN}✓ Metrics endpoint reachable: $METRICS_URL${NC}"
else
    echo -e "${RED}✗ Cannot reach metrics endpoint: $METRICS_URL${NC}"
    ERRORS=$((ERRORS + 1))
fi

echo ""

# Check for required packages (Node.js)
echo "Checking Node.js dependencies..."

if [ -f "package.json" ]; then
    REQUIRED_PACKAGES=(
        "@opentelemetry/sdk-node"
        "@opentelemetry/auto-instrumentations-node"
        "@opentelemetry/exporter-trace-otlp-http"
    )

    for pkg in "${REQUIRED_PACKAGES[@]}"; do
        if grep -q "\"$pkg\"" package.json; then
            echo -e "${GREEN}✓ $pkg found${NC}"
        else
            echo -e "${RED}✗ $pkg not found in package.json${NC}"
            ERRORS=$((ERRORS + 1))
        fi
    done
else
    echo -e "${YELLOW}WARNING: No package.json found${NC}"
    WARNINGS=$((WARNINGS + 1))
fi

echo ""

# Check for instrumentation file
echo "Checking instrumentation setup..."

INSTRUMENTATION_FILES=(
    "src/instrumentation.ts"
    "instrumentation.ts"
    "src/tracing.ts"
    "tracing.ts"
)

FOUND_INSTRUMENTATION=false
for file in "${INSTRUMENTATION_FILES[@]}"; do
    if [ -f "$file" ]; then
        echo -e "${GREEN}✓ Found instrumentation file: $file${NC}"
        FOUND_INSTRUMENTATION=true
        break
    fi
done

if [ "$FOUND_INSTRUMENTATION" = false ]; then
    echo -e "${RED}✗ No instrumentation file found${NC}"
    echo "  Expected one of: ${INSTRUMENTATION_FILES[*]}"
    ERRORS=$((ERRORS + 1))
fi

echo ""

# Summary
echo "=== Validation Summary ==="
if [ $ERRORS -eq 0 ] && [ $WARNINGS -eq 0 ]; then
    echo -e "${GREEN}All checks passed!${NC}"
elif [ $ERRORS -eq 0 ]; then
    echo -e "${YELLOW}$WARNINGS warning(s), 0 errors${NC}"
else
    echo -e "${RED}$ERRORS error(s), $WARNINGS warning(s)${NC}"
    exit 1
fi
