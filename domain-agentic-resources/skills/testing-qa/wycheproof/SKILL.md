---
name: wycheproof
description: >
  Wycheproof provides test vectors for validating cryptographic implementations.
  Use when testing crypto code for known attacks and edge cases.
metadata:
  type: domain
---

# Wycheproof

Wycheproof is an extensive collection of test vectors designed to verify the correctness of cryptographic implementations and test against known attacks. Originally developed by Google, it is now a community-managed project where contributors can add test vectors for specific cryptographic constructions.

## Background

### Key Concepts

| Concept | Description |
|---------|-------------|
| Test vector | Input/output pair for validating crypto implementation correctness |
| Test group | Collection of test vectors sharing attributes (key size, IV size, curve) |
| Result flag | Indicates if test should pass (valid), fail (invalid), or is acceptable |
| Edge case testing | Testing for known vulnerabilities and attack patterns |

### Why This Matters

Cryptographic implementations are notoriously difficult to get right. Even small bugs can:
- Expose private keys
- Allow signature forgery
- Enable message decryption
- Create consensus problems when different implementations accept/reject the same inputs

Wycheproof has found vulnerabilities in major libraries including OpenJDK's SHA1withDSA, Bouncy Castle's ECDHC, and the elliptic npm package.

## When to Use

**Apply Wycheproof when:**
- Testing cryptographic implementations (AES-GCM, ECDSA, ECDH, RSA, etc.)
- Validating that crypto code handles edge cases correctly
- Verifying implementations against known attack vectors
- Setting up CI/CD for cryptographic libraries
- Auditing third-party crypto code for correctness

**Consider alternatives when:**
- Testing for timing side-channels (use constant-time testing tools instead)
- Finding new unknown bugs (use fuzzing instead)
- Testing custom/experimental cryptographic algorithms (Wycheproof only covers established algorithms)

## Quick Reference

| Scenario | Recommended Approach | Notes |
|----------|---------------------|-------|
| AES-GCM implementation | Use `aes_gcm_test.json` | 316 test vectors across 44 test groups |
| ECDSA verification | Use `ecdsa_*_test.json` for specific curves | Tests signature malleability, DER encoding |
| ECDH key exchange | Use `ecdh_*_test.json` | Tests invalid curve attacks |
| RSA signatures | Use `rsa_*_test.json` | Tests padding oracle attacks |
| ChaCha20-Poly1305 | Use `chacha20_poly1305_test.json` | Tests AEAD implementation |

## Testing Workflow

```
Phase 1: Setup                 Phase 2: Parse Test Vectors
┌─────────────────┐          ┌─────────────────┐
│ Add Wycheproof  │    →     │ Load JSON file  │
│ as submodule    │          │ Filter by params│
└─────────────────┘          └─────────────────┘
         ↓                            ↓
Phase 4: CI Integration        Phase 3: Write Harness
┌─────────────────┐          ┌─────────────────┐
│ Auto-update     │    ←     │ Test valid &    │
│ test vectors    │          │ invalid cases   │
└─────────────────┘          └─────────────────┘
```

## Repository Structure

The Wycheproof repository is organized as follows:

```text
┣ 📜 README.md       : Project overview
┣ 📂 doc             : Documentation
┣ 📂 java            : Java JCE interface testing harness
┣ 📂 javascript      : JavaScript testing harness
┣ 📂 schemas         : Test vector schemas
┣ 📂 testvectors     : Test vectors
┗ 📂 testvectors_v1  : Updated test vectors (more detailed)
```

The essential folders are `testvectors` and `testvectors_v1`. While both contain similar files, `testvectors_v1` includes more detailed information and is recommended for new integrations.

## Supported Algorithms

Wycheproof provides test vectors for a wide range of cryptographic algorithms:

| Category | Algorithms |
|----------|------------|
| **Symmetric Encryption** | AES-GCM, AES-EAX, ChaCha20-Poly1305 |
| **Signatures** | ECDSA, EdDSA, RSA-PSS, RSA-PKCS1 |
| **Key Exchange** | ECDH, X25519, X448 |
| **Hashing** | HMAC, HKDF |
| **Curves** | secp256k1, secp256r1, secp384r1, secp521r1, ed25519, ed448 |

## Test File Structure

Each JSON test file tests a specific cryptographic construction. All test files share common attributes:

```json
"algorithm"         : The name of the algorithm tested
"schema"            : The JSON schema (found in schemas folder)
"generatorVersion"  : The version number
"numberOfTests"     : The total number of test vectors in this file
"header"            : Detailed description of test vectors
"notes"             : In-depth explanation of flags in test vectors
"testGroups"        : Array of one or multiple test groups
```

### Test Groups

Test groups group sets of tests based on shared attributes such as:
- Key sizes
- IV sizes
- Public keys
- Curves

This classification allows extracting tests that meet specific criteria relevant to the construction being tested.

### Test Vector Attributes

#### Shared Attributes

All test vectors contain four common fields:

- **tcId**: Unique identifier for the test vector within a file
- **comment**: Additional information about the test case
- **flags**: Descriptions of specific test case types and potential dangers (referenced in `notes` field)
- **result**: Expected outcome of the test

The `result` field can take three values:

| Result | Meaning |
|--------|---------|
| **valid** | Test case should succeed |
| **acceptable** | Test case is allowed to succeed but contains non-ideal attributes |
| **invalid** | Test case should fail |

#### Unique Attributes

Unique attributes are specific to the algorithm being tested:

| Algorithm | Unique Attributes |
|-----------|-------------------|
| AES-GCM | `key`, `iv`, `aad`, `msg`, `ct`, `tag` |
| ECDH secp256k1 | `public`, `private`, `shared` |
| ECDSA | `msg`, `sig`, `result` |
| EdDSA | `msg`, `sig`, `pk` |

## Implementation Guide

### Phase 1: Add Wycheproof to Your Project

**Option 1: Git Submodule (Recommended)**

Adding Wycheproof as a git submodule ensures automatic updates:

```bash
git submodule add https://github.com/C2SP/wycheproof.git
```

**Option 2: Fetch Specific Test Vectors**

If submodules aren't possible, fetch specific JSON files:

```bash
#!/bin/bash

TMP_WYCHEPROOF_FOLDER=".wycheproof/"
TEST_VECTORS=('aes_gcm_test.json' 'aes_eax_test.json')
BASE_URL="https://raw.githubusercontent.com/C2SP/wycheproof/master/testvectors_v1/"

# Create wycheproof folder
mkdir -p $TMP_WYCHEPROOF_FOLDER

# Request all test vector files if they don't exist
for i in "${TEST_VECTORS[@]}"; do
  if [ ! -f "${TMP_WYCHEPROOF_FOLDER}${i}" ]; then
    curl -o "${TMP_WYCHEPROOF_FOLDER}${i}" "${BASE_URL}${i}"
    if [ $? -ne 0 ]; then
      echo "Failed to download ${i}"
      exit 1
    fi
  fi
done
```

Phase 2 (Parse Test Vectors, Python + JavaScript), Phase 3 (Write Testing Harness, Python pytest + JavaScript Mocha), Common Vulnerabilities Detected, the Elliptic npm Package case study (3 CVEs), Advanced Usage tips/mistakes, Related Skills, and Resources are in the reference file.

See [references/test-harness-vulnerabilities-case-study.md](references/test-harness-vulnerabilities-case-study.md)

### Phase 4: CI Integration

Ensure test vectors stay up to date by:

1. **Using git submodules**: Update submodule in CI before running tests
2. **Fetching latest vectors**: Run fetch script before test execution
3. **Scheduled updates**: Set up weekly/monthly updates to catch new test vectors

## Summary

Wycheproof is an essential tool for validating cryptographic implementations against known attack vectors and edge cases. By integrating Wycheproof test vectors into your testing workflow:

1. Catch subtle encoding and validation bugs
2. Prevent signature malleability issues
3. Ensure consistent behavior across implementations
4. Benefit from community-contributed test vectors
5. Protect against known cryptographic vulnerabilities

The investment in writing a reusable testing harness pays dividends through continuous validation as new test vectors are added to the Wycheproof repository.

## Reference Files

| Resource | Purpose |
|----------|---------|
| `references/test-harness-vulnerabilities-case-study.md` | Phase 2 (Parse Test Vectors Python + JavaScript), Phase 3 (Write Testing Harness pytest + Mocha), Common Vulnerabilities table, Elliptic npm Package case study (CVE-2024-42459/42460/42461), Advanced Usage tips and common mistakes, Related Skills dependency map, Resources |
