# Bats Testing: Advanced Patterns and CI/CD Integration

Advanced testing techniques including error condition testing, dependency handling, shell compatibility, parallel execution, test helper utilities, and GitHub Actions / Makefile integration.

## Advanced Patterns

### Testing Error Conditions

```bash
#!/usr/bin/env bats

@test "Function fails with missing file" {
    run my_function "/nonexistent/file.txt"
    [ "$status" -ne 0 ]
    [[ "$output" == *"not found"* ]]
}

@test "Function fails with invalid input" {
    run my_function ""
    [ "$status" -ne 0 ]
}

@test "Function fails with permission denied" {
    touch "$TMPDIR/readonly.txt"
    chmod 000 "$TMPDIR/readonly.txt"
    run my_function "$TMPDIR/readonly.txt"
    [ "$status" -ne 0 ]
    chmod 644 "$TMPDIR/readonly.txt"  # Cleanup
}

@test "Function provides helpful error message" {
    run my_function --invalid-option
    [ "$status" -ne 0 ]
    [[ "$output" == *"Usage:"* ]]
}
```

### Testing with Dependencies

```bash
#!/usr/bin/env bats

setup() {
    # Check for required tools
    if ! command -v jq &>/dev/null; then
        skip "jq is not installed"
    fi

    export SCRIPT="${BATS_TEST_DIRNAME}/../bin/script.sh"
}

@test "JSON parsing works" {
    skip_if ! command -v jq &>/dev/null
    run my_json_parser '{"key": "value"}'
    [ "$status" -eq 0 ]
}
```

### Testing Shell Compatibility

```bash
#!/usr/bin/env bats

@test "Script works in bash" {
    bash "${BATS_TEST_DIRNAME}/../bin/script.sh" arg1
}

@test "Script works in sh (POSIX)" {
    sh "${BATS_TEST_DIRNAME}/../bin/script.sh" arg1
}

@test "Script works in dash" {
    if command -v dash &>/dev/null; then
        dash "${BATS_TEST_DIRNAME}/../bin/script.sh" arg1
    else
        skip "dash not installed"
    fi
}
```

### Parallel Execution

```bash
#!/usr/bin/env bats

@test "Multiple independent operations" {
    run bash -c 'for i in {1..10}; do
        my_operation "$i" &
    done
    wait'
    [ "$status" -eq 0 ]
}

@test "Concurrent file operations" {
    for i in {1..5}; do
        my_function "$TMPDIR/file$i" &
    done
    wait
    [ -f "$TMPDIR/file1" ]
    [ -f "$TMPDIR/file5" ]
}
```

## Test Helper Pattern

### test_helper.sh

```bash
#!/usr/bin/env bash

# Source script under test
export SCRIPT_DIR="${BATS_TEST_DIRNAME%/*}/bin"

# Common test utilities
assert_file_exists() {
    if [ ! -f "$1" ]; then
        echo "Expected file to exist: $1"
        return 1
    fi
}

assert_file_equals() {
    local file="$1"
    local expected="$2"

    if [ ! -f "$file" ]; then
        echo "File does not exist: $file"
        return 1
    fi

    local actual=$(cat "$file")
    if [ "$actual" != "$expected" ]; then
        echo "File contents do not match"
        echo "Expected: $expected"
        echo "Actual: $actual"
        return 1
    fi
}

# Create temporary test directory
setup_test_dir() {
    export TEST_DIR=$(mktemp -d)
}

cleanup_test_dir() {
    rm -rf "$TEST_DIR"
}
```

## Integration with CI/CD

### GitHub Actions Workflow

```yaml
name: Tests

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v3

      - name: Install Bats
        run: |
          npm install --global bats

      - name: Run Tests
        run: |
          bats tests/*.bats

      - name: Run Tests with Tap Reporter
        run: |
          bats tests/*.bats --tap | tee test_output.tap
```

### Makefile Integration

```makefile
.PHONY: test test-verbose test-tap

test:
	bats tests/*.bats

test-verbose:
	bats tests/*.bats --verbose

test-tap:
	bats tests/*.bats --tap

test-parallel:
	bats tests/*.bats --parallel 4

coverage: test
	# Optional: Generate coverage reports
```
