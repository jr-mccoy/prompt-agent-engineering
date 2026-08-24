# Coverage Analysis — Tool-Specific Guidance and Resources

## Tool-Specific Guidance

### libFuzzer

libFuzzer uses LLVM's SanitizerCoverage by default for guiding fuzzing, but you need separate instrumentation for generating reports.

**Build for coverage:**
```bash
clang++ -fprofile-instr-generate -fcoverage-mapping \
  -O2 -DNO_MAIN \
  main.cc harness.cc execute-rt.cc -o fuzz_exec
```

**Execute corpus and generate report:**
```bash
LLVM_PROFILE_FILE=fuzz.profraw ./fuzz_exec corpus/
llvm-profdata merge -sparse fuzz.profraw -o fuzz.profdata
llvm-cov show ./fuzz_exec -instr-profile=fuzz.profdata -format=html -output-dir html/
```

**Integration tips:**
- Don't use `-fsanitize=fuzzer` for coverage builds (it conflicts with profile instrumentation)
- Reuse the same harness function (`LLVMFuzzerTestOneInput`) with a different main function
- Use the `-ignore-filename-regex` flag to exclude harness code from coverage reports
- Consider using llvm-cov's `-show-instantiation` flag for template-heavy C++ code

### AFL++

AFL++ provides its own coverage feedback mechanism, but for detailed reports use standard LLVM/GCC tools.

**Build for coverage with LLVM:**
```bash
clang++ -fprofile-instr-generate -fcoverage-mapping \
  -O2 main.cc harness.cc execute-rt.cc -o fuzz_exec
```

**Build for coverage with GCC:**
```bash
AFL_USE_ASAN=0 afl-gcc -ftest-coverage -fprofile-arcs \
  main.cc harness.cc execute-rt.cc -o fuzz_exec_gcov
```

**Execute and generate report:**
```bash
# LLVM approach
LLVM_PROFILE_FILE=fuzz.profraw ./fuzz_exec afl_output/queue/
llvm-profdata merge -sparse fuzz.profraw -o fuzz.profdata
llvm-cov report ./fuzz_exec -instr-profile=fuzz.profdata

# GCC approach
./fuzz_exec_gcov afl_output/queue/
gcovr --html-details -o coverage.html
```

**Integration tips:**
- Don't use AFL++'s instrumentation (`afl-clang-fast`) for coverage builds
- Use standard compilers with coverage flags instead
- AFL++'s `queue/` directory contains your corpus
- AFL++'s built-in coverage statistics are useful for real-time monitoring but not for detailed analysis

### cargo-fuzz (Rust)

cargo-fuzz provides built-in coverage generation using LLVM tools.

**Install prerequisites:**
```bash
rustup toolchain install nightly --component llvm-tools-preview
cargo install cargo-binutils rustfilt
```

**Generate coverage data:**
```bash
cargo +nightly fuzz coverage fuzz_target_1
```

**Create HTML report script:**
```bash
cat <<'EOF' > ./generate_html
#!/bin/sh
FUZZ_TARGET="$1"
shift
SRC_FILTER="$@"
TARGET=$(rustc -vV | sed -n 's|host: ||p')
cargo +nightly cov -- show -Xdemangler=rustfilt \
  "target/$TARGET/coverage/$TARGET/release/$FUZZ_TARGET" \
  -instr-profile="fuzz/coverage/$FUZZ_TARGET/coverage.profdata" \
  -show-line-counts-or-regions -show-instantiations \
  -format=html -o fuzz_html/ $SRC_FILTER
EOF
chmod +x ./generate_html
```

**Generate report:**
```bash
./generate_html fuzz_target_1 src/lib.rs
```

**Integration tips:**
- Always use the nightly toolchain for coverage
- The `-Xdemangler=rustfilt` flag makes function names readable
- Filter by source files (e.g., `src/lib.rs`) to focus on crate code
- Use `-show-line-counts-or-regions` and `-show-instantiations` for better Rust-specific output
- Corpus is located in `fuzz/corpus/<target>/`

### honggfuzz

honggfuzz works with standard LLVM/GCC coverage instrumentation.

**Build for coverage:**
```bash
# Use standard compiler, not honggfuzz compiler
clang -fprofile-instr-generate -fcoverage-mapping \
  -O2 harness.c execute-rt.c -o fuzz_exec
```

**Execute corpus:**
```bash
LLVM_PROFILE_FILE=fuzz.profraw ./fuzz_exec honggfuzz_workspace/
```

**Integration tips:**
- Don't use `hfuzz-clang` for coverage builds
- honggfuzz corpus is typically in a workspace directory
- Use the same LLVM workflow as libFuzzer

---

## Troubleshooting

| Issue | Cause | Solution |
|-------|-------|----------|
| `error: no profile data available` | Profile wasn't generated or wrong path | Verify `LLVM_PROFILE_FILE` was set and `.profraw` file exists |
| `Failed to load coverage` | Mismatch between binary and profile data | Rebuild binary with same flags used during execution |
| Coverage reports show 0% | Wrong binary used for report generation | Use the instrumented binary, not the fuzzing binary |
| `no_working_dir_found` error (gcovr) | `.gcda` files in unexpected location | Add `--gcov-ignore-errors=no_working_dir_found` flag |
| Crashes prevent coverage generation | Corpus contains crashing inputs | Filter crashes or use forking approach to isolate failures |
| Coverage decreases after harness change | Harness now skips certain code paths | Review harness logic; may need to support more input formats |
| HTML report is flat file list | Using older LLVM version | Upgrade to LLVM 18+ and use `-show-directory-coverage` |
| `incompatible instrumentation` | Mixing LLVM and GCC coverage | Rebuild everything with same toolchain |

---

## Related Skills

### Tools That Use This Technique

| Skill | How It Applies |
|-------|----------------|
| **libfuzzer** | Uses SanitizerCoverage for feedback; coverage analysis evaluates harness effectiveness |
| **aflpp** | Uses edge coverage for feedback; detailed analysis requires separate instrumentation |
| **cargo-fuzz** | Built-in `cargo fuzz coverage` command for Rust projects |
| **honggfuzz** | Uses edge coverage; analyze with standard LLVM/GCC tools |

### Related Techniques

| Skill | Relationship |
|-------|--------------|
| **fuzz-harness-writing** | Coverage reveals which code paths harness reaches; guides harness improvements |
| **fuzzing-dictionaries** | Coverage identifies magic value checks that need dictionary entries |
| **corpus-management** | Coverage analysis helps curate corpora by identifying redundant test cases |
| **sanitizers** | Coverage helps verify sanitizer-instrumented code is actually executed |

---

## Resources

**[LLVM Source-Based Code Coverage](https://clang.llvm.org/docs/SourceBasedCodeCoverage.html)**
Comprehensive guide to LLVM's profile instrumentation, including advanced features like branch coverage, region coverage, and integration with existing build systems. Covers compiler flags, runtime behavior, and profile data formats.

**[llvm-cov Command Guide](https://llvm.org/docs/CommandGuide/llvm-cov.html)**
Detailed CLI reference for llvm-cov commands including `show`, `report`, and `export`. Documents all filtering options, output formats, and integration with llvm-profdata.

**[gcovr Documentation](https://gcovr.com/)**
Complete guide to gcovr tool for generating coverage reports from gcov data. Covers HTML themes, filtering options, multi-directory projects, and CI/CD integration patterns.

**[SanitizerCoverage Documentation](https://clang.llvm.org/docs/SanitizerCoverage.html)**
Low-level documentation for LLVM's SanitizerCoverage instrumentation. Explains inline 8-bit counters, PC tables, and how fuzzers use coverage feedback for guidance.

**[On the Evaluation of Fuzzer Performance](https://arxiv.org/abs/1808.09700)**
Research paper examining limitations of coverage as a fuzzing performance metric. Argues for more nuanced evaluation methods beyond simple code coverage percentages.
