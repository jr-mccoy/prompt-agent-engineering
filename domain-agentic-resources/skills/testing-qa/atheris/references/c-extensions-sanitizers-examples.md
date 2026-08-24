# Atheris — C Extensions, Sanitizer Integration, Advanced Usage, and Real-World Examples

## Fuzzing Python C Extensions

Python C extensions require compilation with specific flags for instrumentation and sanitizer support.

### Environment Configuration

If using the provided Dockerfile, these are already configured. For local setup:

```bash
export CC="clang"
export CFLAGS="-fsanitize=address,fuzzer-no-link"
export CXX="clang++"
export CXXFLAGS="-fsanitize=address,fuzzer-no-link"
export LDSHARED="clang -shared"
```

### Example: Fuzzing cbor2

Install the extension from source:
```bash
CBOR2_BUILD_C_EXTENSION=1 python -m pip install --no-binary cbor2 cbor2==5.6.4
```

The `--no-binary` flag ensures the C extension is compiled locally with instrumentation.

Create `cbor2-fuzz.py`:
```python
import sys
import atheris

# _cbor2 ensures the C library is imported
from _cbor2 import loads

def test_one_input(data: bytes):
    try:
        loads(data)
    except Exception:
        # We're searching for memory corruption, not Python exceptions
        pass

def main():
    atheris.Setup(sys.argv, test_one_input)
    atheris.Fuzz()

if __name__ == "__main__":
    main()
```

Run:
```bash
python cbor2-fuzz.py
```

> **Important:** When running locally (not in Docker), you must [set `LD_PRELOAD` manually](https://github.com/google/atheris/blob/master/native_extension_fuzzing.md#option-a-sanitizerlibfuzzer-preloads).

---

## Sanitizer Integration

### AddressSanitizer (ASan)

AddressSanitizer is automatically integrated when using the provided Docker environment or when compiling with appropriate flags.

For local setup:
```bash
export CFLAGS="-fsanitize=address,fuzzer-no-link"
export CXXFLAGS="-fsanitize=address,fuzzer-no-link"
```

Configure ASan behavior:
```bash
export ASAN_OPTIONS="allocator_may_return_null=1,detect_leaks=0"
```

### LD_PRELOAD Configuration

For native extension fuzzing:
```bash
export LD_PRELOAD="$(python -c 'import atheris; import os; print(os.path.join(os.path.dirname(atheris.__file__), "asan_with_fuzzer.so"))')"
```

> **See Also:** For detailed sanitizer configuration, common issues, and advanced flags,
> see the **address-sanitizer** and **undefined-behavior-sanitizer** technique skills.

### Common Sanitizer Issues

| Issue | Solution |
|-------|----------|
| `LD_PRELOAD` not set | Export `LD_PRELOAD` to point to `asan_with_fuzzer.so` |
| Memory allocation failures | Set `ASAN_OPTIONS=allocator_may_return_null=1` |
| Leak detection noise | Set `ASAN_OPTIONS=detect_leaks=0` |
| Missing symbolizer | Set `ASAN_SYMBOLIZER_PATH` to `llvm-symbolizer` |

---

## Advanced Usage

### Tips and Tricks

| Tip | Why It Helps |
|-----|--------------|
| Use `atheris.instrument_imports()` early | Ensures all imports are instrumented for coverage |
| Start with small `max_len` | Faster initial fuzzing, gradually increase |
| Use dictionaries for structured formats | Helps fuzzer understand format tokens |
| Run multiple parallel instances | Better coverage exploration |

### Custom Instrumentation

Fine-tune what gets instrumented:
```python
import atheris

# Instrument only specific modules
with atheris.instrument_imports():
    import target_module
# Don't instrument test harness code

def test_one_input(data: bytes):
    target_module.parse(data)
```

### Performance Tuning

| Setting | Impact |
|---------|--------|
| `-max_len=N` | Smaller values = faster execution |
| `-workers=N -jobs=N` | Parallel fuzzing for faster coverage |
| `ASAN_OPTIONS=fast_unwind_on_malloc=0` | Better stack traces, slower execution |

### UndefinedBehaviorSanitizer (UBSan)

Add UBSan to catch additional bugs:
```bash
export CFLAGS="-fsanitize=address,undefined,fuzzer-no-link"
export CXXFLAGS="-fsanitize=address,undefined,fuzzer-no-link"
```

Note: Modify flags in Dockerfile if using containerized setup.

---

## Real-World Examples

### Example: Pure Python Parser

```python
import sys
import atheris
import json

@atheris.instrument_func
def test_one_input(data: bytes):
    try:
        # Fuzz Python's JSON parser
        json.loads(data.decode('utf-8', errors='ignore'))
    except (ValueError, UnicodeDecodeError):
        pass

def main():
    atheris.Setup(sys.argv, test_one_input)
    atheris.Fuzz()

if __name__ == "__main__":
    main()
```

### Example: HTTP Request Parsing

```python
import sys
import atheris

with atheris.instrument_imports():
    from urllib3 import HTTPResponse
    from io import BytesIO

def test_one_input(data: bytes):
    try:
        # Fuzz HTTP response parsing
        fake_response = HTTPResponse(
            body=BytesIO(data),
            headers={},
            preload_content=False
        )
        fake_response.read()
    except Exception:
        pass

def main():
    atheris.Setup(sys.argv, test_one_input)
    atheris.Fuzz()

if __name__ == "__main__":
    main()
```
