---
name: aflpp
description: >
  AFL++ is a fork of AFL with better fuzzing performance and advanced features.
  Use for multi-core fuzzing of C/C++ projects.
metadata:
  type: fuzzer
---

# AFL++

AFL++ is a fork of the original AFL fuzzer that offers better fuzzing performance and more advanced features while maintaining stability. A major benefit over libFuzzer is that AFL++ has stable support for running fuzzing campaigns on multiple cores, making it ideal for large-scale fuzzing efforts.

## When to Use

| Fuzzer | Best For | Complexity |
|--------|----------|------------|
| AFL++ | Multi-core fuzzing, diverse mutations, mature projects | Medium |
| libFuzzer | Quick setup, single-threaded, simple harnesses | Low |
| LibAFL | Custom fuzzers, research, advanced use cases | High |

**Choose AFL++ when:**
- You need multi-core fuzzing to maximize throughput
- Your project can be compiled with Clang or GCC
- You want diverse mutation strategies and mature tooling
- libFuzzer has plateaued and you need more coverage
- You're fuzzing production codebases that benefit from parallel execution

## Quick Start

```c++
extern "C" int LLVMFuzzerTestOneInput(const uint8_t *data, size_t size) {
    // Call your code with fuzzer-provided data
    check_buf((char*)data, size);
    return 0;
}
```

Compile and run:
```bash
# Setup AFL++ wrapper script first (see Installation)
./afl++ docker afl-clang-fast++ -DNO_MAIN=1 -O2 -fsanitize=fuzzer harness.cc main.cc -o fuzz
mkdir seeds && echo "aaaa" > seeds/minimal_seed
./afl++ docker afl-fuzz -i seeds -o out -- ./fuzz
```

## Installation

AFL++ has many dependencies including LLVM, Python, and Rust. We recommend using a current Debian or Ubuntu distribution for fuzzing with AFL++.

| Method | When to Use | Supported Compilers |
|--------|-------------|---------------------|
| Ubuntu/Debian repos | Recent Ubuntu, basic features only | Ubuntu 23.10: Clang 14 & GCC 13<br>Debian 12: Clang 14 & GCC 12 |
| Docker (from Docker Hub) | Specific AFL++ version, Apple Silicon support | As of 4.35c: Clang 19 & GCC 11 |
| Docker (from source) | Test unreleased features, apply patches | Configurable in Dockerfile |
| From source | Avoid Docker, need specific patches | Adjustable via `LLVM_CONFIG` env var |

### Ubuntu/Debian

Prior to installing afl++, check the clang version dependency of the packge with `apt-cache show afl++`, and install the matching `lld` version (e.g., `lld-17`).


```bash
apt install afl++ lld-17
```


### Docker (from Docker Hub)

```bash
docker pull aflplusplus/aflplusplus:stable
```

### Docker (from source)

```bash
git clone --depth 1 --branch stable https://github.com/AFLplusplus/AFLplusplus
cd AFLplusplus
docker build -t aflplusplus .
```

### From source

Refer to the [Dockerfile](https://github.com/AFLplusplus/AFLplusplus/blob/stable/Dockerfile) for Ubuntu version requirements and dependencies. Set `LLVM_CONFIG` to specify Clang version (e.g., `llvm-config-18`).

### Wrapper Script Setup

Create a wrapper script to run AFL++ on host or Docker:

```bash
cat <<'EOF' > ./afl++
#!/bin/sh
AFL_VERSION="${AFL_VERSION:-"stable"}"
case "$1" in
   host)
        shift
        bash -c "$*"
        ;;
    docker)
        shift
        /usr/bin/env docker run -ti \
            --privileged \
            -v ./:/src \
            --rm \
            --name afl_fuzzing \
            "aflplusplus/aflplusplus:$AFL_VERSION" \
            bash -c "cd /src && bash -c \"$*\""
        ;;
    *)
        echo "Usage: $0 {host|docker}"
        exit 1
        ;;
esac
EOF
chmod +x ./afl++
```

**Security Warning:** The `afl-system-config` and `afl-persistent-config` scripts require root privileges and disable OS security features. Do not fuzz on production systems or your development environment. Use a dedicated VM instead.

### System Configuration

Run after each reboot for up to 15% more executions per second:

```bash
./afl++ <host/docker> afl-system-config
```

For maximum performance, disable kernel security mitigations (requires grub bootloader, not supported in Docker):

```bash
./afl++ host afl-persistent-config
update-grub
reboot
./afl++ <host/docker> afl-system-config
```

Verify with `cat /proc/cmdline` - output should include `mitigations=off`.

## Writing a Harness

### Harness Structure

AFL++ supports libFuzzer-style harnesses:

```c++
#include <stdint.h>
#include <stddef.h>

extern "C" int LLVMFuzzerTestOneInput(const uint8_t *data, size_t size) {
    // 1. Validate input size if needed
    if (size < MIN_SIZE || size > MAX_SIZE) return 0;

    // 2. Call target function with fuzz data
    target_function(data, size);

    // 3. Return 0 (non-zero reserved for future use)
    return 0;
}
```

### Harness Rules

| Do | Don't |
|----|-------|
| Reset global state between runs | Rely on state from previous runs |
| Handle edge cases gracefully | Exit on invalid input |
| Keep harness deterministic | Use random number generators |
| Free allocated memory | Create memory leaks |
| Validate input sizes | Process unbounded input |

> **See Also:** For detailed harness writing techniques, patterns for handling complex inputs,
> and advanced strategies, see the **fuzz-harness-writing** technique skill.

## Compilation

AFL++ offers multiple compilation modes with different trade-offs.

### Compilation Mode Decision Tree

Choose your compilation mode:
- **LTO mode** (`afl-clang-lto`): Best performance and instrumentation. Try this first.
- **LLVM mode** (`afl-clang-fast`): Fall back if LTO fails to compile.
- **GCC plugin** (`afl-gcc-fast`): For projects requiring GCC.

### Basic Compilation (LLVM mode)

```bash
./afl++ <host/docker> afl-clang-fast++ -DNO_MAIN=1 -O2 -fsanitize=fuzzer harness.cc main.cc -o fuzz
```

### GCC Compilation

```bash
./afl++ <host/docker> afl-g++-fast -DNO_MAIN=1 -O2 -fsanitize=fuzzer harness.cc main.cc -o fuzz
```

**Important:** GCC version must match the version used to compile the AFL++ GCC plugin.

### With Sanitizers

```bash
./afl++ <host/docker> AFL_USE_ASAN=1 afl-clang-fast++ -DNO_MAIN=1 -O2 -fsanitize=fuzzer harness.cc main.cc -o fuzz
```

> **See Also:** For detailed sanitizer configuration, common issues, and advanced flags,
> see the **address-sanitizer** and **undefined-behavior-sanitizer** technique skills.

### Build Flags

Note that `-g` is not necessary, it is added by default by the AFL++ compilers.

| Flag | Purpose |
|------|---------|
| `-DNO_MAIN=1` | Skip main function when using libFuzzer harness |
| `-O2` | Production optimization level (recommended for fuzzing) |
| `-fsanitize=fuzzer` | Enable libFuzzer compatibility mode and adds the fuzzer runtime when linking executable |
| `-fsanitize=fuzzer-no-link` | Instrument without linking fuzzer runtime (for static libraries and object files) |

## Corpus Management

### Creating Initial Corpus

AFL++ requires at least one non-empty seed file:

```bash
mkdir seeds
echo "aaaa" > seeds/minimal_seed
```

For real projects, gather representative inputs:
- Download example files for the format you're fuzzing
- Extract test cases from the project's test suite
- Use minimal valid inputs for your file format

### Corpus Minimization

After a campaign, minimize the corpus to keep only unique coverage:

```bash
./afl++ <host/docker> afl-cmin -i out/default/queue -o minimized_corpus -- ./fuzz
```

> **See Also:** For corpus creation strategies, dictionaries, and seed selection,
> see the **fuzzing-corpus** technique skill.

## Running Campaigns

### Basic Run

```bash
./afl++ <host/docker> afl-fuzz -i seeds -o out -- ./fuzz
```

### Setting Environment Variables

```bash
./afl++ <host/docker> AFL_FAST_CAL=1 afl-fuzz -i seeds -o out -- ./fuzz
```

### Interpreting Output

The AFL++ UI shows real-time fuzzing statistics:

| Output | Meaning |
|--------|---------|
| **execs/sec** | Execution speed - higher is better |
| **cycles done** | Number of queue passes completed |
| **corpus count** | Number of unique test cases in queue |
| **saved crashes** | Number of unique crashes found |
| **stability** | % of stable edges (should be near 100%) |

### Output Directory Structure

```text
out/default/
├── cmdline          # How was the SUT invoked?
├── crashes/         # Inputs that crash the SUT
│   └── id:000000,sig:06,src:000002,time:286,execs:13105,op:havoc,rep:4
├── hangs/           # Inputs that hang the SUT
├── queue/           # Test cases reproducing final fuzzer state
│   ├── id:000000,time:0,execs:0,orig:minimal_seed
│   └── id:000001,src:000000,time:0,execs:8,op:havoc,rep:6,+cov
├── fuzzer_stats     # Campaign statistics
└── plot_data        # Data for plotting
```

### Analyzing Results

View live campaign statistics:

```bash
./afl++ <host/docker> afl-whatsup out
```

Create coverage plots:

```bash
apt install gnuplot
./afl++ <host/docker> afl-plot out/default out_graph/
```

### Re-executing Test Cases

```bash
./afl++ <host/docker> ./fuzz out/default/crashes/<test_case>
```

### Fuzzer Options

| Option | Purpose |
|--------|---------|
| `-G 4000` | Maximum test input length (default: 1048576 bytes) |
| `-t 1000` | Timeout in milliseconds for each test case (default: 1000ms) |
| `-m 1000` | Memory limit in megabytes (default: 0 = unlimited) |
| `-x ./dict.dict` | Use dictionary file to guide mutations |

## Environment Variables That Matter

AFL++ has [many environment variables](https://aflplus.plus/docs/env_variables/), but most are niche. These are the ones that matter in practice.

### Always Set These

```bash
# Every campaign should use tmpfs — SSDs will thank you, and it's faster
AFL_TMPDIR=/dev/shm
```

`AFL_TMPDIR` is a free performance win with no downsides — not setting it wears out your SSD and slows fuzzing.

### Slow Targets

```bash
# Speeds up calibration ~2.5x — use when targets are slow (e.g., >10 ms/exec)
AFL_FAST_CAL=1
```

`AFL_FAST_CAL` reduces calibration time with negligible precision loss. Recommended specifically for slow targets where calibration would otherwise take a long time.

### Multi-Core Campaigns

```bash
# On the primary (-M) instance only — needed for afl-cmin, not for fuzzing itself
AFL_FINAL_SYNC=1

# On all instances — cache test cases in memory (default: 50 MB, good range: 50-250 MB)
AFL_TESTCACHE_SIZE=100
```

`AFL_FINAL_SYNC` tells the primary instance to do a final import from all secondaries when stopping. This does not affect the fuzzing process itself — it only matters when you later run `afl-cmin` for corpus minimization, ensuring the primary's queue has the full combined corpus. `AFL_TESTCACHE_SIZE` caches test cases in memory to reduce disk I/O; the default is 50 MB and values between 50-250 MB work well for most campaigns.

### CI/Automated Fuzzing

```bash
# Fail fast if fuzzing isn't finding anything
AFL_EXIT_ON_TIME=3600  # 1 hour with no new paths = stop

# Or run until "done" (all queue entries processed)
AFL_EXIT_WHEN_DONE=1

# Headless environments
AFL_NO_UI=1
```

Unbounded fuzzing in CI wastes resources. Set time limits or use exit conditions.

### Variables to Avoid

| Variable | Why Skip It |
|----------|-------------|
| `AFL_NO_ARITH` | Can hurt coverage on binary formats, but may be useful for text-based targets |
| `AFL_SHUFFLE_QUEUE` | Only for exotic setups, usually harmful |
| `AFL_DISABLE_TRIM` | Trimming is valuable, don't disable without reason |

## Multi-Core Fuzzing

AFL++ excels at multi-core fuzzing with two major advantages:
1. More executions per second (scales linearly with physical cores)
2. Asymmetrical fuzzing (e.g., one ASan job, rest without sanitizers)

### Starting a Campaign

Start the primary fuzzer (in background):

```bash
./afl++ <host/docker> afl-fuzz -M primary -i seeds -o state -- ./fuzz 1>primary.log 2>primary.error &
```

Start secondary fuzzers (as many as you have cores):

```bash
./afl++ <host/docker> afl-fuzz -S secondary01 -i seeds -o state -- ./fuzz 1>secondary01.log 2>secondary01.error &
./afl++ <host/docker> afl-fuzz -S secondary02 -i seeds -o state -- ./fuzz 1>secondary02.log 2>secondary02.error &
```

### Monitoring Multi-Core Campaigns

List all running jobs:

```bash
jobs
```

View live statistics (updates every second):

```bash
./afl++ <host/docker> watch -n1 --color afl-whatsup state/
```

### Stopping All Fuzzers

```bash
kill $(jobs -p)
```

## Coverage Analysis

AFL++ automatically tracks coverage through edge instrumentation. Coverage information is stored in `fuzzer_stats` and `plot_data`.

### Measuring Coverage

Use `afl-plot` to visualize coverage over time:

```bash
./afl++ <host/docker> afl-plot out/default out_graph/
```

### Improving Coverage

- Use dictionaries for format-aware fuzzing
- Run longer campaigns (cycles_wo_finds indicates plateau)
- Try different mutation strategies with multi-core fuzzing
- Analyze coverage gaps and add targeted seed inputs

> **See Also:** For detailed coverage analysis techniques, identifying coverage gaps,
> and systematic coverage improvement, see the **coverage-analysis** technique skill.

## CMPLOG

CMPLOG/RedQueen is the best path constraint solving mechanism available in any fuzzer.
To enable it, the fuzz target needs to be instrumented for it.
Before building the fuzzing target set the environment variable:

```bash
./afl++ <host/docker> AFL_LLVM_CMPLOG=1 make
```

No special action is needed for compiling and linking the harness.

To run a fuzzer instance with a CMPLOG instrumented fuzzing target, add `-c0` to the command like arguments:

```bash
./afl++ <host/docker> afl-fuzz -c0 -S cmplog -i seeds -o state -- ./fuzz 1>secondary02.log 2>secondary02.error &
```

## Sanitizer Integration

Sanitizers are essential for finding memory corruption bugs that don't cause immediate crashes.

### AddressSanitizer (ASan)

```bash
./afl++ <host/docker> AFL_USE_ASAN=1 afl-clang-fast++ -DNO_MAIN=1 -O2 -fsanitize=fuzzer harness.cc main.cc -o fuzz
```

**Note:** Memory limit (`-m`) is not supported with ASan due to 20TB virtual memory reservation.

### UndefinedBehaviorSanitizer (UBSan)

```bash
./afl++ <host/docker> AFL_USE_UBSAN=1 afl-clang-fast++ -DNO_MAIN=1 -O2 -fsanitize=fuzzer,undefined harness.cc main.cc -o fuzz
```

### Common Sanitizer Issues

| Issue | Solution |
|-------|----------|
| ASan slows fuzzing | Use only 1 ASan job in multi-core setup |
| Stack exhaustion | Increase stack with `ASAN_OPTIONS=stack_size=...` |
| GCC version mismatch | Ensure system GCC matches AFL++ plugin version |

> **See Also:** For comprehensive sanitizer configuration and troubleshooting,
> see the **address-sanitizer** technique skill.

## Advanced Usage, Troubleshooting, and Resources

Advanced fuzzing configurations including stdin, file input, and argument fuzzing patterns, performance tuning settings (CPU core count, persistent mode, input size, ASan ratio), a troubleshooting table for common issues (low exec/sec, stability, GCC plugin errors, crashes, memory limits, Docker performance), related technique skills (harness-writing, sanitizers, corpus, dictionaries), related fuzzers (libfuzzer, libafl), and key external resources (AFL++ GitHub, Fuzzing in Depth, Under the Hood, original paper, video tutorials).

See [references/advanced-usage-and-resources.md](references/advanced-usage-and-resources.md)

---

## Reference Files

| Resource | Purpose |
|----------|---------|
| `references/advanced-usage-and-resources.md` | Advanced fuzzing patterns (stdin/file/argument), performance tuning, troubleshooting, related skills, and external resources |
