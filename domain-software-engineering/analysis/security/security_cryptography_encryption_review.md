---
title: "Cryptography and Encryption Security Review"
category: code-analysis
description: "Cryptography and Encryption Security Review"
tags:
  - code-analysis
  - review
  - security
updated: "2026-03-19"
---

# Cryptography and Encryption Security Review

**Objective:** Analyze cryptographic implementations, encryption practices, and key management to identify weak algorithms, implementation flaws, and cryptographic vulnerabilities that could compromise data confidentiality and integrity.

**Instructions:**

1. **Identify all cryptographic operations in the codebase:**

   a. **Data Encryption/Decryption**
      - Locate symmetric encryption usage (AES, ChaCha20, 3DES)
      - Identify asymmetric encryption (RSA, ECC, ElGamal)
      - Find authenticated encryption (AES-GCM, ChaCha20-Poly1305)
      - Check for disk/database encryption
      - Review file encryption implementations
      - Analyze end-to-end encryption mechanisms

   b. **Hashing and Message Authentication**
      - Identify password hashing (bcrypt, Argon2, scrypt, PBKDF2)
      - Locate message digest usage (SHA-256, SHA-3, BLAKE2)
      - Find HMAC implementations
      - Check digital signature usage (RSA, ECDSA, EdDSA)
      - Review message authentication codes (MAC)

   c. **Key Derivation and Exchange**
      - Analyze key derivation functions (KDF)
      - Check Diffie-Hellman key exchange
      - Review ECDH implementations
      - Identify HKDF usage
      - Check password-based key derivation

   d. **Random Number Generation**
      - Identify CSPRNG (Cryptographically Secure Pseudo-Random Number Generator) usage
      - Check for weak random number generators (Math.random(), rand())
      - Review entropy sources
      - Analyze nonce and IV generation

2. **Analyze cryptographic algorithm choices:**

   a. **Weak or Deprecated Algorithms**
      - Identify MD5 usage (except for non-security purposes)
      - Check for SHA-1 (deprecated for signatures)
      - Find DES or 3DES usage (deprecated)
      - Locate RC4 (broken)
      - Check for ECB mode (insecure)
      - Identify custom/homebrew cryptography

   b. **Algorithm Configuration**
      - Review key sizes (RSA ≥ 2048 bits, AES ≥ 128 bits, ECC ≥ 256 bits)
      - Check cipher modes (prefer GCM, CCM, avoid ECB)
      - Analyze padding schemes (OAEP for RSA, PKCS#7)
      - Review iteration counts for KDFs (PBKDF2 ≥ 100,000)
      - Check password hashing cost factors (bcrypt ≥ 10, Argon2 parameters)

   c. **Modern Algorithm Usage**
      - Verify use of AES-GCM or ChaCha20-Poly1305 for encryption
      - Check for Argon2 or bcrypt for password hashing
      - Review Ed25519 or ECDSA for signatures
      - Verify TLS 1.3 or TLS 1.2 with strong cipher suites
      - Check for post-quantum cryptography considerations

3. **Review cryptographic implementations:**

   a. **Implementation Flaws**
      - Check for timing attacks (constant-time comparisons)
      - Identify padding oracle vulnerabilities
      - Review IV/nonce reuse issues
      - Check for insufficient randomness
      - Analyze key derivation weaknesses
      - Identify truncated HMAC or hash outputs

   b. **Initialization Vector (IV) and Nonce Handling**
      - Verify IV uniqueness for each encryption
      - Check for predictable or reused IVs
      - Review nonce generation and storage
      - Analyze counter mode implementations
      - Check for IV/nonce transmission security

   c. **Padding and Modes of Operation**
      - Review padding scheme implementations
      - Check for padding oracle attack vectors
      - Analyze cipher modes (CBC, CTR, GCM)
      - Verify authenticated encryption usage
      - Check for unauthenticated encryption modes

4. **Assess key management practices:**

   a. **Key Generation**
      - Review key generation methods
      - Check randomness quality for key generation
      - Verify sufficient key length
      - Analyze key derivation from passwords
      - Check for deterministic key generation issues

   b. **Key Storage**
      - Identify hardcoded encryption keys
      - Review key storage locations (files, environment, database)
      - Check for encrypted key storage
      - Analyze key encryption keys (KEK) protection
      - Review hardware security module (HSM) usage
      - Check for key storage in version control

   c. **Key Distribution and Exchange**
      - Review key exchange protocols
      - Check for secure key transmission
      - Analyze certificate validation
      - Review public key infrastructure (PKI)
      - Check for man-in-the-middle protections

   d. **Key Rotation and Lifecycle**
      - Identify key rotation policies
      - Check for key expiration handling
      - Review key retirement procedures
      - Analyze key backup and recovery
      - Check for cryptoperiod enforcement
      - Verify key versioning

5. **Review TLS/SSL configuration:**

   a. **TLS Version and Cipher Suites**
      - Verify TLS 1.2 or 1.3 usage (TLS 1.0/1.1 deprecated)
      - Review cipher suite configuration
      - Check for weak ciphers (RC4, DES, export ciphers)
      - Verify forward secrecy (ECDHE, DHE)
      - Check for cipher suite preference order
      - Review TLS downgrade protections

   b. **Certificate Management**
      - Review certificate validation implementation
      - Check for certificate pinning
      - Analyze certificate expiration handling
      - Review self-signed certificate usage
      - Check for proper certificate chain validation
      - Verify hostname verification

6. **Analyze sensitive data protection:**

   a. **Data at Rest**
      - Review database encryption (transparent encryption, column-level)
      - Check file system encryption
      - Analyze backup encryption
      - Review encrypted disk/volume usage
      - Check for memory encryption considerations

   b. **Data in Transit**
      - Verify TLS/SSL for all network communications
      - Check for encrypted API communications
      - Review WebSocket encryption
      - Analyze encrypted messaging
      - Check for VPN or secure tunneling

   c. **Data in Use**
      - Review memory protection for sensitive data
      - Check for secure memory clearing
      - Analyze sensitive data in logs
      - Review clipboard protection
      - Check for screen capture protection

7. **For each identified issue, provide:**
   - Code location (file, function, line numbers)
   - Cryptographic issue type
   - Severity rating (Critical, High, Medium, Low)
   - Vulnerability explanation
   - Attack scenarios and exploitation methods
   - Impact assessment (data breach, integrity compromise)
   - Recommended algorithms and configurations
   - Secure code examples
   - Migration strategy for algorithm updates

**Expected Output:** A comprehensive cryptography security review including:

- **Executive Summary:**
  - Overall cryptographic security posture
  - Critical cryptographic vulnerabilities
  - Weak algorithm usage
  - Key management maturity
  - Compliance with cryptographic standards (FIPS 140-2, NIST)

- **Cryptographic Algorithm Analysis:**

  **Weak or Deprecated Algorithms:**
  - MD5, SHA-1, DES, 3DES, RC4 usage
  - Code locations and purposes
  - Severity and exploitability
  - Modern algorithm replacements
  - Migration recommendations

  **Algorithm Configuration Issues:**
  - Insufficient key lengths
  - Weak KDF parameters
  - Insecure cipher modes (ECB)
  - Improper padding
  - Recommendations for hardening

- **Implementation Vulnerability Analysis:**
  - Timing attacks
  - Padding oracle vulnerabilities
  - IV/nonce reuse
  - Weak random number generation
  - Custom cryptography issues
  - Remediation guidance

- **Key Management Assessment:**

  **Key Generation:**
  - Generation method review
  - Randomness quality
  - Key length analysis
  - Recommendations

  **Key Storage:**
  - Hardcoded keys identified
  - Storage security evaluation
  - Key encryption key protection
  - HSM usage recommendations

  **Key Lifecycle:**
  - Rotation policy assessment
  - Expiration handling
  - Key retirement procedures
  - Recommendations for improvement

- **TLS/SSL Configuration Review:**
  - TLS version analysis
  - Cipher suite recommendations
  - Certificate management review
  - Forward secrecy assessment
  - Configuration hardening guidance

- **Sensitive Data Protection:**
  - Data at rest encryption
  - Data in transit encryption
  - Data in use protection
  - Gaps and recommendations

- **Remediation Roadmap:**

  **Immediate (Critical):**
  - Replace broken algorithms (MD5, RC4, DES)
  - Fix hardcoded encryption keys
  - Implement strong password hashing
  - Disable weak TLS cipher suites

  **Short-term:**
  - Implement key rotation
  - Upgrade to TLS 1.3
  - Fix IV/nonce reuse
  - Improve key storage security
  - Implement constant-time comparisons

  **Long-term:**
  - Deploy HSM or key management service
  - Implement comprehensive key lifecycle management
  - Cryptographic library modernization
  - Post-quantum cryptography preparation
  - Regular cryptographic audits

- **Best Practices Recommendations:**
  - Use vetted cryptographic libraries (OpenSSL, libsodium, NaCl, cryptography.io)
  - Never implement custom cryptography
  - Use authenticated encryption (AES-GCM, ChaCha20-Poly1305)
  - Implement proper key management
  - Regular cryptographic updates
  - Follow NIST/OWASP cryptographic guidelines

**Example Output Format:**

```
CRITICAL: Weak Password Hashing with MD5
Location: src/auth/password.js:34
Algorithm: MD5

Vulnerable Code:
  const hash = crypto.createHash('md5')
    .update(password)
    .digest('hex');

Issue:
  Passwords are hashed using MD5 without salt, making them
  vulnerable to rainbow table attacks and collision attacks.
  MD5 can hash billions of passwords per second on modern hardware.

Attack Scenario:
  1. Attacker obtains password hash database (SQL injection, breach)
  2. Attacker uses rainbow tables or GPU cracking (hashcat)
  3. Common passwords cracked in seconds/minutes
  4. Account takeover and credential reuse attacks

Impact:
  - Mass account compromise
  - Compliance violations (NIST, OWASP, PCI-DSS)
  - Reputation damage
  - Legal liability

Remediation:
  const bcrypt = require('bcrypt');
  const saltRounds = 12;

  // Hashing
  const hash = await bcrypt.hash(password, saltRounds);

  // Verification
  const match = await bcrypt.compare(password, hash);

Migration Strategy:
  1. Update password hashing to bcrypt/Argon2
  2. On user login, verify old MD5 hash, then rehash with bcrypt
  3. Gradual migration as users authenticate
  4. Force password reset for inactive accounts after 90 days

Compliance:
  - NIST 800-63B: Use approved password hashing (bcrypt, PBKDF2, Argon2)
  - OWASP: Use adaptive hashing with cost factor ≥ 10
  - PCI-DSS: Render passwords unreadable using strong cryptography
```

**Related Prompts:**
- security_owasp_top_10_analysis.md - Includes cryptographic failures
- security_secret_credential_detection.md - Key and credential detection
- security_authentication_authorization_review.md - Auth security including tokens
- security_compliance_analysis.md - Cryptographic compliance requirements

**When to Use:**
Use this prompt when auditing cryptographic implementations, reviewing security-critical applications, investigating data breaches, preparing for compliance audits (PCI-DSS, HIPAA, FIPS), before cryptographic library migrations, or as part of regular security assessments. Essential for applications handling sensitive data.

**Techniques Used:**
- ST-01 (Clear Objective Statement) - Opens with concise, unambiguous objective
- ST-02 (Structured Sequential Instructions) - Numbered steps for systematic analysis
- DT-02 (Specific Focus Areas with Examples) - Comprehensive cryptographic categories
- RT-02 (Multi-Dimensional Analysis Framework) - Algorithm, Issue, Severity, Attack, Remediation
- DS-01 (Framework Application) - Applies NIST and OWASP cryptographic standards
- DS-02 (Metric Specification) - Key sizes, iteration counts, cost factors
- DS-06 (Prioritization and Severity Guidance) - Severity ratings and migration roadmap
- AG-05 (Concrete Deliverable Templates) - Secure code examples with bcrypt/Argon2
