# libFuzzer — Running Campaigns & Advanced Usage

## Running Campaigns

### Basic Run

```bash
./fuzz corpus/
```

This runs until a crash is found or you stop it (Ctrl+C).

### Recommended: Continue After Crashes

```bash
./fuzz -fork=1 -ignore_crashes=1 corpus/
```

The `-fork` and `-ignore_crashes` flags (experimental but widely used) allow fuzzing to continue after finding crashes.

### Common Options

**Control input size:**
```bash
./fuzz -max_len=4000 corpus/
```
Rule of thumb: 2x the size of minimal realistic input.

**Set timeout:**
```bash
./fuzz -timeout=2 corpus/
```
Abort test cases that run longer than 2 seconds.

**Use a dictionary:**
```bash
./fuzz -dict=./format.dict corpus/
```

**Close stdout/stderr (speed up fuzzing):**
```bash
./fuzz -close_fd_mask=3 corpus/
```

**See all options:**
```bash
./fuzz -help=1
```

### Multi-Core Fuzzing

**Option 1: Jobs and workers (recommended):**
```bash
./fuzz -jobs=4 -workers=4 -fork=1 -ignore_crashes=1 corpus/
```
- `-jobs=4`: Run 4 sequential campaigns
- `-workers=4`: Process jobs in parallel with 4 processes
- Test cases are shared between jobs

**Option 2: Fork mode:**
```bash
./fuzz -fork=4 -ignore_crashes=1 corpus/
```

**Note:** For serious multi-core fuzzing, consider switching to AFL++, Honggfuzz, or LibAFL.

### Re-executing Test Cases

**Re-run a single crash:**
```bash
./fuzz ./crash-a9993e364706816aba3e25717850c26c9cd0d89d
```

**Test all inputs in a directory without fuzzing:**
```bash
./fuzz -runs=0 corpus/
```

### Interpreting Output

When fuzzing runs, you'll see statistics like:

```
INFO: Seed: 3517090860
INFO: Loaded 1 modules (9 inline 8-bit counters)
#2      INITED cov: 3 ft: 4 corp: 1/1b exec/s: 0 rss: 26Mb
#57     NEW    cov: 4 ft: 5 corp: 2/4b lim: 4 exec/s: 0 rss: 26Mb
```

| Output | Meaning |
|--------|---------|
| `INITED` | Fuzzing initialized |
| `NEW` | New coverage found, added to corpus |
| `REDUCE` | Input minimized while keeping coverage |
| `cov: N` | Number of coverage edges hit |
| `corp: X/Yb` | Corpus size: X entries, Y total bytes |
| `exec/s: N` | Executions per second |
| `rss: NMb` | Resident memory usage |

**On crash:**
```
==11672== ERROR: libFuzzer: deadly signal
artifact_prefix='./'; Test unit written to ./crash-a9993e364706816aba3e25717850c26c9cd0d89d
0x61,0x62,0x63,
abc
Base64: YWJj
```

The crash is saved to `./crash-<hash>` with the input shown in hex, UTF-8, and Base64.

**Reproducibility:** Use `-seed=<value>` to reproduce a fuzzing campaign (single-core only).

---

## Fuzzing Dictionary

Dictionaries help the fuzzer discover interesting inputs faster by providing hints about the input format.

### Dictionary Format

Create a text file with quoted strings (one per line):

```conf
# Lines starting with '#' are comments

# Magic bytes
magic="\x89PNG"
magic2="IEND"

# Keywords
"GET"
"POST"
"Content-Type"

# Hex sequences
delimiter="\xFF\xD8\xFF"
```

### Using a Dictionary

```bash
./fuzz -dict=./format.dict corpus/
```

### Generating a Dictionary

**From header files:**
```bash
grep -o '".*"' header.h > header.dict
```

**From man pages:**
```bash
man curl | grep -oP '^\s*(--|-)\K\S+' | sed 's/[,.]$//' | sed 's/^/"&/; s/$/&"/' | sort -u > man.dict
```

**From binary strings:**
```bash
strings ./binary | sed 's/^/"&/; s/$/&"/' > strings.dict
```

**Using LLMs:** Ask ChatGPT or similar to generate a dictionary for your format (e.g., "Generate a libFuzzer dictionary for a JSON parser").

> **See Also:** For advanced dictionary generation, format-specific dictionaries, and
> dictionary optimization strategies, see the **fuzzing-dictionaries** technique skill.

---

## Coverage Analysis

While libFuzzer shows basic coverage stats (`cov: N`), detailed coverage analysis requires additional tools.

### Source-Based Coverage

**1. Recompile with coverage instrumentation:**
```bash
clang++ -fsanitize=fuzzer -fprofile-instr-generate -fcoverage-mapping harness.cc target.cc -o fuzz
```

**2. Run fuzzer to collect coverage:**
```bash
LLVM_PROFILE_FILE="coverage-%p.profraw" ./fuzz -runs=10000 corpus/
```

**3. Merge coverage data:**
```bash
llvm-profdata merge -sparse coverage-*.profraw -o coverage.profdata
```

**4. Generate coverage report:**
```bash
llvm-cov show ./fuzz -instr-profile=coverage.profdata
```

**5. Generate HTML report:**
```bash
llvm-cov show ./fuzz -instr-profile=coverage.profdata -format=html > coverage.html
```

### Improving Coverage

**Tips:**
- Provide better seed inputs in corpus
- Use dictionaries for format-aware fuzzing
- Check if harness properly exercises target
- Consider structure-aware fuzzing for complex formats
- Run longer campaigns (days/weeks)

> **See Also:** For detailed coverage analysis techniques, identifying coverage gaps,
> systematic coverage improvement, and comparing coverage across fuzzers, see the
> **coverage-analysis** technique skill.

---

## Sanitizer Integration

### AddressSanitizer (ASan)

ASan detects memory errors like buffer overflows and use-after-free bugs. **Highly recommended for fuzzing.**

**Enable ASan:**
```bash
clang++ -fsanitize=fuzzer,address -g -O2 -U_FORTIFY_SOURCE harness.cc target.cc -o fuzz
```

**Example ASan output:**
```
==1276163==ERROR: AddressSanitizer: heap-buffer-overflow on address 0x6020000c4ab1
WRITE of size 1 at 0x6020000c4ab1 thread T0
    #0 0x55555568631a in check_buf(char*, unsigned long) main.cc:13:25
    #1 0x5555556860bf in LLVMFuzzerTestOneInput harness.cc:7:3
```

**Configure ASan with environment variables:**
```bash
ASAN_OPTIONS=verbosity=1:abort_on_error=1 ./fuzz corpus/
```

**Important flags:**
- `verbosity=1`: Show ASan is active
- `detect_leaks=0`: Disable leak detection (leaks reported at end)
- `abort_on_error=1`: Call `abort()` instead of `_exit()` on errors

**Drawbacks:**
- 2-4x slowdown
- Requires ~20TB virtual memory (disable memory limits: `-rss_limit_mb=0`)
- Best supported on Linux

> **See Also:** For comprehensive ASan configuration, common pitfalls, symbolization,
> and combining with other sanitizers, see the **address-sanitizer** technique skill.

### UndefinedBehaviorSanitizer (UBSan)

UBSan detects undefined behavior like integer overflow, null pointer dereference, etc.

**Enable UBSan:**
```bash
clang++ -fsanitize=fuzzer,undefined -g -O2 harness.cc target.cc -o fuzz
```

**Combine with ASan:**
```bash
clang++ -fsanitize=fuzzer,address,undefined -g -O2 harness.cc target.cc -o fuzz
```

### MemorySanitizer (MSan)

MSan detects uninitialized memory reads. More complex to use (requires rebuilding all dependencies).

```bash
clang++ -fsanitize=fuzzer,memory -g -O2 harness.cc target.cc -o fuzz
```

### Common Sanitizer Issues

| Issue | Solution |
|-------|----------|
| ASan slows fuzzing too much | Use `-fsanitize-recover=address` for non-fatal errors |
| Out of memory | Set `ASAN_OPTIONS=rss_limit_mb=0` or `-rss_limit_mb=0` |
| Stack exhaustion | Increase stack size: `ASAN_OPTIONS=stack_size=8388608` |
| False positives with `_FORTIFY_SOURCE` | Use `-U_FORTIFY_SOURCE` flag |
| MSan reports in dependencies | Rebuild all dependencies with `-fsanitize=memory` |

---

## Real-World Examples

### Example 1: Fuzzing libpng

libpng is a widely-used library for reading/writing PNG images. Bugs can lead to security issues.

**1. Get source code:**
```bash
curl -L -O https://downloads.sourceforge.net/project/libpng/libpng16/1.6.37/libpng-1.6.37.tar.xz
tar xf libpng-1.6.37.tar.xz
cd libpng-1.6.37/
```

**2. Install dependencies:**
```bash
apt install zlib1g-dev
```

**3. Compile with fuzzing instrumentation:**
```bash
export CC=clang CFLAGS="-fsanitize=fuzzer-no-link -fsanitize=address"
export CXX=clang++ CXXFLAGS="$CFLAGS"
./configure --enable-shared=no
make
```

**4. Get a harness (or write your own):**
```bash
curl -O https://raw.githubusercontent.com/glennrp/libpng/f8e5fa92b0e37ab597616f554bee254157998227/contrib/oss-fuzz/libpng_read_fuzzer.cc
```

**5. Prepare corpus and dictionary:**
```bash
mkdir corpus/
curl -o corpus/input.png https://raw.githubusercontent.com/glennrp/libpng/acfd50ae0ba3198ad734e5d4dec2b05341e50924/contrib/pngsuite/iftp1n3p08.png
curl -O https://raw.githubusercontent.com/glennrp/libpng/2fff013a6935967960a5ae626fc21432807933dd/contrib/oss-fuzz/png.dict
```

**6. Link and compile fuzzer:**
```bash
clang++ -fsanitize=fuzzer -fsanitize=address libpng_read_fuzzer.cc .libs/libpng16.a -lz -o fuzz
```

**7. Run fuzzing campaign:**
```bash
./fuzz -close_fd_mask=3 -dict=./png.dict corpus/
```

### Example 2: Simple Division Bug

Harness that finds a division-by-zero bug:

```c++
#include <stdint.h>
#include <stddef.h>

double divide(uint32_t numerator, uint32_t denominator) {
    // Bug: No check if denominator is zero
    return numerator / denominator;
}

extern "C" int LLVMFuzzerTestOneInput(const uint8_t *data, size_t size) {
    if(size != 2 * sizeof(uint32_t)) {
        return 0;
    }

    uint32_t numerator = *(uint32_t*)(data);
    uint32_t denominator = *(uint32_t*)(data + sizeof(uint32_t));

    divide(numerator, denominator);

    return 0;
}
```

Compile and fuzz:
```bash
clang++ -fsanitize=fuzzer harness.cc -o fuzz
./fuzz
```

The fuzzer will quickly find inputs causing a crash.

---

## Advanced Usage

### Tips and Tricks

| Tip | Why It Helps |
|-----|--------------|
| Start with single-core, switch to AFL++ for multi-core | libFuzzer harnesses work with AFL++ |
| Use dictionaries for structured formats | 10-100x faster bug discovery |
| Close file descriptors with `-close_fd_mask=3` | Speed boost if SUT writes output |
| Set reasonable `-max_len` | Prevents wasted time on huge inputs |
| Run for days/weeks, not minutes | Coverage plateaus take time to break |
| Use seed corpus from test suites | Starts fuzzing from valid inputs |

### Structure-Aware Fuzzing

For highly structured inputs (e.g., complex protocols, file formats), use libprotobuf-mutator:

- Define input structure using Protocol Buffers
- libFuzzer mutates protobuf messages (structure-preserving mutations)
- Harness converts protobuf to native format

See [structure-aware fuzzing documentation](https://github.com/google/fuzzing/blob/master/docs/structure-aware-fuzzing.md) for details.

### Custom Mutators

libFuzzer allows custom mutators for specialized fuzzing:

```c++
extern "C" size_t LLVMFuzzerCustomMutator(uint8_t *Data, size_t Size,
                                          size_t MaxSize, unsigned int Seed) {
    // Custom mutation logic
    return new_size;
}

extern "C" size_t LLVMFuzzerCustomCrossOver(const uint8_t *Data1, size_t Size1,
                                            const uint8_t *Data2, size_t Size2,
                                            uint8_t *Out, size_t MaxOutSize,
                                            unsigned int Seed) {
    // Custom crossover logic
    return new_size;
}
```

### Performance Tuning

| Setting | Impact |
|---------|--------|
| `-close_fd_mask=3` | Closes stdout/stderr, speeds up fuzzing |
| `-max_len=<reasonable_size>` | Avoids wasting time on huge inputs |
| `-timeout=<seconds>` | Detects hangs, prevents stuck executions |
| Disable ASan for baseline | 2-4x speed boost (but misses memory bugs) |
| Use `-jobs` and `-workers` | Limited multi-core support |
| Run on Linux | Best platform support and performance |

---

## Troubleshooting

| Problem | Cause | Solution |
|---------|-------|----------|
| No crashes found after hours | Poor corpus, low coverage | Add seed inputs, use dictionary, check harness |
| Very slow executions/sec (<100) | Target too complex, excessive logging | Optimize target, use `-close_fd_mask=3`, reduce logging |
| Out of memory | ASan's 20TB virtual memory | Set `-rss_limit_mb=0` to disable RSS limit |
| Fuzzer stops after first crash | Default behavior | Use `-fork=1 -ignore_crashes=1` to continue |
| Can't reproduce crash | Non-determinism in harness/target | Remove random number generation, global state |
| Linking errors with `-fsanitize=fuzzer` | Missing libFuzzer runtime | Ensure using Clang, check LLVM installation |
| GCC project won't compile with Clang | GCC-specific code | Switch to AFL++ with `gcc_plugin` instead |
| Coverage not improving | Corpus plateau | Run longer, add dictionary, improve seeds, check coverage report |
| Crashes but ASan doesn't trigger | Memory error not detected without ASan | Recompile with `-fsanitize=address` |

---

## Related Skills

### Technique Skills

| Skill | Use Case |
|-------|----------|
| **fuzz-harness-writing** | Detailed guidance on writing effective harnesses, structure-aware fuzzing, and FuzzedDataProvider usage |
| **address-sanitizer** | Memory error detection configuration, ASAN_OPTIONS, and troubleshooting |
| **undefined-behavior-sanitizer** | Detecting undefined behavior during fuzzing |
| **coverage-analysis** | Measuring fuzzing effectiveness and identifying untested code paths |
| **fuzzing-corpus** | Building and managing seed corpora, corpus minimization strategies |
| **fuzzing-dictionaries** | Creating format-specific dictionaries for faster bug discovery |

### Related Fuzzers

| Skill | When to Consider |
|-------|------------------|
| **aflpp** | When you need serious multi-core fuzzing, or when libFuzzer coverage plateaus |
| **honggfuzz** | When you want hardware-based coverage feedback on Linux |
| **libafl** | When building custom fuzzers or conducting fuzzing research |

## Resources

### Official Documentation

- [LLVM libFuzzer Documentation](https://llvm.org/docs/LibFuzzer.html) - Official reference
- [libFuzzer Tutorial by Google](https://github.com/google/fuzzing/blob/master/tutorial/libFuzzerTutorial.md) - Step-by-step guide
- [SanitizerCoverage](https://clang.llvm.org/docs/SanitizerCoverage.html) - Coverage instrumentation details

### Advanced Topics

- [Structure-Aware Fuzzing with libprotobuf-mutator](https://github.com/google/fuzzing/blob/master/docs/structure-aware-fuzzing.md)
- [Split Inputs in libFuzzer](https://github.com/google/fuzzing/blob/master/docs/split-inputs.md)
- [FuzzedDataProvider Header](https://github.com/llvm/llvm-project/blob/main/compiler-rt/include/fuzzer/FuzzedDataProvider.h)

### Example Projects

- [OSS-Fuzz](https://github.com/google/oss-fuzz) - Continuous fuzzing for open-source projects (many libFuzzer examples)
- [AFL++ Dictionary Collection](https://github.com/AFLplusplus/AFLplusplus/tree/stable/dictionaries) - Reusable dictionaries
