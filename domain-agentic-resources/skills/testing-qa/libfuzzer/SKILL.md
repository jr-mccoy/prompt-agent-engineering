---
name: libfuzzer
description: >
  Coverage-guided fuzzer built into LLVM for C/C++ projects. Use for fuzzing
  C/C++ code that can be compiled with Clang.
metadata:
  type: fuzzer
---

# libFuzzer

libFuzzer is an in-process, coverage-guided fuzzer that is part of the LLVM project. It's the recommended starting point for fuzzing C/C++ projects due to its simplicity and integration with the LLVM toolchain. While libFuzzer has been in maintenance-only mode since late 2022, it is easier to install and use than its alternatives, has wide support, and will be maintained for the foreseeable future.

## When to Use

| Fuzzer | Best For | Complexity |
|--------|----------|------------|
| libFuzzer | Quick setup, single-project fuzzing | Low |
| AFL++ | Multi-core fuzzing, diverse mutations | Medium |
| LibAFL | Custom fuzzers, research projects | High |
| Honggfuzz | Hardware-based coverage | Medium |

**Choose libFuzzer when:**
- You need a simple, quick setup for C/C++ code
- Project uses Clang for compilation
- Single-core fuzzing is sufficient initially
- Transitioning to AFL++ later is an option (harnesses are compatible)

**Note:** Fuzzing harnesses written for libFuzzer are compatible with AFL++, making it easy to transition if you need more advanced features like better multi-core support.

## Quick Start

```c++
#include <stdint.h>
#include <stddef.h>

extern "C" int LLVMFuzzerTestOneInput(const uint8_t *data, size_t size) {
    // Validate input if needed
    if (size < 1) return 0;

    // Call your target function with fuzzer-provided data
    my_target_function(data, size);

    return 0;
}
```

Compile and run:
```bash
clang++ -fsanitize=fuzzer,address -g -O2 harness.cc target.cc -o fuzz
mkdir corpus/
./fuzz corpus/
```

## Installation

### Prerequisites

- LLVM/Clang compiler (includes libFuzzer)
- LLVM tools for coverage analysis (optional)

### Linux (Ubuntu/Debian)

```bash
apt install clang llvm
```

For the latest LLVM version:
```bash
# Add LLVM repository from apt.llvm.org
# Then install specific version, e.g.:
apt install clang-18 llvm-18
```

### macOS

```bash
# Using Homebrew
brew install llvm

# Or using Nix
nix-env -i clang
```

### Windows

Install Clang through Visual Studio. Refer to [Microsoft's documentation](https://learn.microsoft.com/en-us/cpp/build/clang-support-msbuild?view=msvc-170) for setup instructions.

**Recommendation:** If possible, fuzz on a local x86_64 VM or rent one on DigitalOcean, AWS, or Hetzner. Linux provides the best support for libFuzzer.

### Verification

```bash
clang++ --version
# Should show LLVM version information
```

## Writing a Harness

### Harness Structure

The harness is the entry point for the fuzzer. libFuzzer calls the `LLVMFuzzerTestOneInput` function repeatedly with different inputs.

```c++
#include <stdint.h>
#include <stddef.h>

extern "C" int LLVMFuzzerTestOneInput(const uint8_t *data, size_t size) {
    // 1. Optional: Validate input size
    if (size < MIN_REQUIRED_SIZE) {
        return 0;  // Reject inputs that are too small
    }

    // 2. Optional: Convert raw bytes to structured data
    // Example: Parse two integers from byte array
    if (size >= 2 * sizeof(uint32_t)) {
        uint32_t a = *(uint32_t*)(data);
        uint32_t b = *(uint32_t*)(data + sizeof(uint32_t));
        my_function(a, b);
    }

    // 3. Call target function
    target_function(data, size);

    // 4. Always return 0 (non-zero reserved for future use)
    return 0;
}
```

### Harness Rules

| Do | Don't |
|----|-------|
| Handle all input types (empty, huge, malformed) | Call `exit()` - stops fuzzing process |
| Join all threads before returning | Leave threads running |
| Keep harness fast and simple | Add excessive logging or complexity |
| Maintain determinism | Use random number generators or read `/dev/random` |
| Reset global state between runs | Rely on state from previous executions |
| Use narrow, focused targets | Mix unrelated data formats (PNG + TCP) in one harness |

**Rationale:**
- **Speed matters:** Aim for 100s-1000s executions per second per core
- **Reproducibility:** Crashes must be reproducible after fuzzing completes
- **Isolation:** Each execution should be independent

### Using FuzzedDataProvider for Complex Inputs

For complex inputs (strings, multiple parameters), use the `FuzzedDataProvider` helper:

```c++
#include <stdint.h>
#include <stddef.h>
#include "FuzzedDataProvider.h"  // From LLVM project

extern "C" int LLVMFuzzerTestOneInput(const uint8_t *data, size_t size) {
    FuzzedDataProvider fuzzed_data(data, size);

    // Extract structured data
    size_t allocation_size = fuzzed_data.ConsumeIntegral<size_t>();
    std::vector<char> str1 = fuzzed_data.ConsumeBytesWithTerminator<char>(32, 0xFF);
    std::vector<char> str2 = fuzzed_data.ConsumeBytesWithTerminator<char>(32, 0xFF);

    // Call target with extracted data
    char* result = concat(&str1[0], str1.size(), &str2[0], str2.size(), allocation_size);
    if (result != NULL) {
        free(result);
    }

    return 0;
}
```

Download `FuzzedDataProvider.h` from the [LLVM repository](https://github.com/llvm/llvm-project/blob/main/compiler-rt/include/fuzzer/FuzzedDataProvider.h).

### Interleaved Fuzzing

Use a single harness to test multiple related functions:

```c++
extern "C" int LLVMFuzzerTestOneInput(const uint8_t *data, size_t size) {
    if (size < 1 + 2 * sizeof(int32_t)) {
        return 0;
    }

    uint8_t mode = data[0];
    int32_t numbers[2];
    memcpy(numbers, data + 1, 2 * sizeof(int32_t));

    // Select function based on first byte
    switch (mode % 4) {
        case 0: add(numbers[0], numbers[1]); break;
        case 1: subtract(numbers[0], numbers[1]); break;
        case 2: multiply(numbers[0], numbers[1]); break;
        case 3: divide(numbers[0], numbers[1]); break;
    }

    return 0;
}
```

> **See Also:** For detailed harness writing techniques, patterns for handling complex inputs,
> structure-aware fuzzing, and protobuf-based fuzzing, see the **fuzz-harness-writing** technique skill.

## Compilation

### Basic Compilation

The key flag is `-fsanitize=fuzzer`, which:
- Links the libFuzzer runtime (provides `main` function)
- Enables SanitizerCoverage instrumentation for coverage tracking
- Disables built-in functions like `memcmp`

```bash
clang++ -fsanitize=fuzzer -g -O2 harness.cc target.cc -o fuzz
```

**Flags explained:**
- `-fsanitize=fuzzer`: Enable libFuzzer
- `-g`: Add debug symbols (helpful for crash analysis)
- `-O2`: Production-level optimizations (recommended for fuzzing)
- `-DNO_MAIN`: Define macro if your code has a `main` function

### With Sanitizers

**AddressSanitizer (recommended):**
```bash
clang++ -fsanitize=fuzzer,address -g -O2 -U_FORTIFY_SOURCE harness.cc target.cc -o fuzz
```

**Multiple sanitizers:**
```bash
clang++ -fsanitize=fuzzer,address,undefined -g -O2 harness.cc target.cc -o fuzz
```

> **See Also:** For detailed sanitizer configuration, common issues, ASAN_OPTIONS flags,
> and advanced sanitizer usage, see the **address-sanitizer** and **undefined-behavior-sanitizer**
> technique skills.

### Build Flags

| Flag | Purpose |
|------|---------|
| `-fsanitize=fuzzer` | Enable libFuzzer runtime and instrumentation |
| `-fsanitize=address` | Enable AddressSanitizer (memory error detection) |
| `-fsanitize=undefined` | Enable UndefinedBehaviorSanitizer |
| `-fsanitize=fuzzer-no-link` | Instrument without linking fuzzer (for libraries) |
| `-g` | Include debug symbols |
| `-O2` | Production optimization level |
| `-U_FORTIFY_SOURCE` | Disable fortification (can interfere with ASan) |

### Building Static Libraries

For projects that produce static libraries:

1. Build the library with fuzzing instrumentation:
```bash
export CC=clang CFLAGS="-fsanitize=fuzzer-no-link -fsanitize=address"
export CXX=clang++ CXXFLAGS="$CFLAGS"
./configure --enable-shared=no
make
```

2. Link the static library with your harness:
```bash
clang++ -fsanitize=fuzzer -fsanitize=address harness.cc libmylib.a -o fuzz
```

### CMake Integration

```cmake
project(FuzzTarget)
cmake_minimum_required(VERSION 3.0)

add_executable(fuzz main.cc harness.cc)
target_compile_definitions(fuzz PRIVATE NO_MAIN=1)
target_compile_options(fuzz PRIVATE -g -O2 -fsanitize=fuzzer -fsanitize=address)
target_link_libraries(fuzz -fsanitize=fuzzer -fsanitize=address)
```

Build with:
```bash
cmake -DCMAKE_C_COMPILER=clang -DCMAKE_CXX_COMPILER=clang++ .
cmake --build .
```

## Corpus Management

### Creating Initial Corpus

Create a directory for the corpus (can start empty):

```bash
mkdir corpus/
```

**Optional but recommended:** Provide seed inputs (valid example files):

```bash
# For a PNG parser:
cp examples/*.png corpus/

# For a protocol parser:
cp test_packets/*.bin corpus/
```

**Benefits of seed inputs:**
- Fuzzer doesn't start from scratch
- Reaches valid code paths faster
- Significantly improves effectiveness

### Corpus Structure

The corpus directory contains:
- Input files that trigger unique code paths
- Minimized versions (libFuzzer automatically minimizes)
- Named by content hash (e.g., `a9993e364706816aba3e25717850c26c9cd0d89d`)

### Corpus Minimization

libFuzzer automatically minimizes corpus entries during fuzzing. To explicitly minimize:

```bash
mkdir minimized_corpus/
./fuzz -merge=1 minimized_corpus/ corpus/
```

This creates a deduplicated, minimized corpus in `minimized_corpus/`.

> **See Also:** For corpus creation strategies, seed selection, format-specific corpus building,
> and corpus maintenance, see the **fuzzing-corpus** technique skill.

## Running Campaigns, Sanitizers, Real-World Examples & Advanced Usage

Campaign execution (basic/fork/multi-core runs, interpreting output table), fuzzing dictionaries (format syntax, generating from headers/man pages/strings/LLMs), source-based coverage analysis (5-step llvm-profdata/llvm-cov process), sanitizer integration (ASan/UBSan/MSan with ASAN_OPTIONS and common issues table), real-world examples (libpng step-by-step, division-bug harness), advanced usage (custom mutators, structure-aware fuzzing with libprotobuf-mutator, performance tuning table), troubleshooting table, related skills/fuzzers, and official resources.

See [references/running-campaigns-and-advanced.md](references/running-campaigns-and-advanced.md)

---

## Reference Files

| Resource | Purpose |
|----------|---------|
| `references/running-campaigns-and-advanced.md` | Running campaigns, dictionaries, coverage, sanitizers, real-world examples, advanced usage, troubleshooting, resources |
