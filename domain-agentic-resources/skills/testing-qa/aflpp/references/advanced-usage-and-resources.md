# AFL++ — Advanced Usage and Resources

## Advanced Usage

### Tips and Tricks

| Tip | Why It Helps |
|-----|--------------|
| Use LLVMFuzzerTestOneInput harnesses where possible | If a fuzzing campaign has at least 85% stability then this is the most efficient fuzzing style. If not then try standard input or file input fuzzing |
| Use dictionaries | Helps fuzzer discover format-specific keywords and magic bytes |
| Set realistic timeouts | Prevents false positives from system load |
| Limit input size | Larger inputs don't necessarily explore more space |
| Monitor stability | Low stability indicates non-deterministic behavior |

### Standard Input Fuzzing

AFL++ can fuzz programs reading from stdin without a libFuzzer harness:

```bash
./afl++ <host/docker> afl-clang-fast++ -O2 main_stdin.c -o fuzz_stdin
./afl++ <host/docker> afl-fuzz -i seeds -o out -- ./fuzz_stdin
```

This is slower than persistent mode but requires no harness code.

### File Input Fuzzing

For programs that read files, use `@@` placeholder:

```bash
./afl++ <host/docker> afl-clang-fast++ -O2 main_file.c -o fuzz_file
./afl++ <host/docker> afl-fuzz -i seeds -o out -- ./fuzz_file @@
```

For better performance, use `fmemopen` to create file descriptors from memory.

### Argument Fuzzing

Fuzz command-line arguments using `argv-fuzz-inl.h`:

```c++
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#ifdef __AFL_COMPILER
#include "argv-fuzz-inl.h"
#endif

void check_buf(char *buf, size_t buf_len) {
    if(buf_len > 0 && buf[0] == 'a') {
        if(buf_len > 1 && buf[1] == 'b') {
            if(buf_len > 2 && buf[2] == 'c') {
                abort();
            }
        }
    }
}

int main(int argc, char *argv[]) {
#ifdef __AFL_COMPILER
    AFL_INIT_ARGV();
#endif

    if (argc < 2) {
        fprintf(stderr, "Usage: %s <input_string>\n", argv[0]);
        return 1;
    }

    char *input_buf = argv[1];
    size_t len = strlen(input_buf);
    check_buf(input_buf, len);
    return 0;
}
```

Download the header:

```bash
curl -O https://raw.githubusercontent.com/AFLplusplus/AFLplusplus/stable/utils/argv_fuzzing/argv-fuzz-inl.h
```

Compile and run:

```bash
./afl++ <host/docker> afl-clang-fast++ -O2 main_arg.c -o fuzz_arg
./afl++ <host/docker> afl-fuzz -i seeds -o out -- ./fuzz_arg
```

### Performance Tuning

| Setting | Impact |
|---------|--------|
| CPU core count | Linear scaling with physical cores |
| Persistent mode | 10-20x faster than fork server |
| `-G` input size limit | Smaller = faster, but may miss bugs |
| ASan ratio | 1 ASan job per 4-8 non-ASan jobs |

---

## Troubleshooting

| Problem | Cause | Solution |
|---------|-------|----------|
| Low exec/sec (<1k) | Not using persistent mode | Create a LLVMFuzzerTestOneInput style harness |
| Low stability (<85%) | Non-deterministic code | Fuzz a program via stdin or file inputs, or create such a harness |
| GCC plugin error | GCC version mismatch | Ensure system GCC matches AFL++ build and install gcc-$GCC_VERSION-plugin-dev |
| No crashes found | Need sanitizers | Recompile with `AFL_USE_ASAN=1` |
| Memory limit exceeded | ASan uses 20TB virtual | Remove `-m` flag when using ASan |
| Docker performance loss | Virtualization overhead | Use bare metal or VM for production fuzzing |

## Related Skills

### Technique Skills

| Skill | Use Case |
|-------|----------|
| **fuzz-harness-writing** | Detailed guidance on writing effective harnesses |
| **address-sanitizer** | Memory error detection during fuzzing |
| **undefined-behavior-sanitizer** | Detect undefined behavior bugs |
| **fuzzing-corpus** | Building and managing seed corpora |
| **fuzzing-dictionaries** | Creating dictionaries for format-aware fuzzing |

### Related Fuzzers

| Skill | When to Consider |
|-------|------------------|
| **libfuzzer** | Quick prototyping, single-threaded fuzzing is sufficient |
| **libafl** | Need custom mutators or research-grade features |

## Resources

### Key External Resources

**[AFL++ GitHub Repository](https://github.com/AFLplusplus/AFLplusplus)**
Official repository with comprehensive documentation, examples, and issue tracker.

**[Fuzzing in Depth](https://raw.githubusercontent.com/AFLplusplus/AFLplusplus/refs/heads/stable/docs/fuzzing_in_depth.md)**
Advanced documentation by the AFL++ team covering instrumentation modes, optimization techniques, and advanced use cases.

**[AFL++ Under The Hood](https://blog.ritsec.club/posts/afl-under-hood/)**
Technical deep-dive into AFL++ internals, mutation strategies, and coverage tracking mechanisms.

**[AFL++: Combining Incremental Steps of Fuzzing Research](https://www.usenix.org/system/files/woot20-paper-fioraldi.pdf)**
Research paper describing AFL++ architecture and performance improvements over original AFL.

### Video Resources

- [Fuzzing cURL](https://blog.trailofbits.com/2023/02/14/curl-audit-fuzzing-libcurl-command-line-interface/) - Trail of Bits blog post on using AFL++ argument fuzzing for cURL
- [Sudo Vulnerability Walkthrough](https://www.youtube.com/playlist?list=PLhixgUqwRTjy0gMuT4C3bmjeZjuNQyqdx) - LiveOverflow series on rediscovering CVE-2021-3156
- [Rediscovery of libpng bug](https://www.youtube.com/watch?v=PJLWlmp8CDM) - LiveOverflow video on finding CVE-2023-4863
