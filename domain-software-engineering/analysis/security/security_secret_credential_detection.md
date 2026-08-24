---
title: "Secret and Credential Detection Analysis"
category: code-analysis
description: "Secret and Credential Detection Analysis"
tags:
  - code-analysis
  - security
updated: "2026-03-19"
---

# Secret and Credential Detection Analysis

**Objective:** Identify hardcoded secrets, credentials, API keys, tokens, and sensitive information in the codebase and version control history to prevent unauthorized access and data breaches.

**Instructions:**

1. **Scan for hardcoded credentials and secrets:**

   a. **API Keys and Access Tokens**
      - Search for AWS access keys (AKIA*, ASIA*)
      - Identify Google Cloud API keys
      - Locate Azure access tokens and connection strings
      - Find Stripe, PayPal, and payment gateway credentials
      - Identify third-party service API keys (SendGrid, Twilio, Slack, etc.)
      - Check for GitHub, GitLab personal access tokens
      - Find CI/CD platform tokens (CircleCI, Travis, Jenkins)

   b. **Database Credentials**
      - Identify database connection strings with passwords
      - Find hardcoded database usernames and passwords
      - Locate MongoDB, PostgreSQL, MySQL credentials
      - Check for Redis authentication passwords
      - Identify database connection URLs with credentials

   c. **Encryption Keys and Certificates**
      - Find JWT secret keys and signing keys
      - Identify encryption keys (AES, RSA)
      - Locate private keys (.pem, .key, .p12 files)
      - Check for SSL/TLS certificates and private keys
      - Find SSH private keys
      - Identify OAuth client secrets

   d. **Authentication Tokens**
      - Find session secrets and cookie signing keys
      - Identify bearer tokens and access tokens
      - Locate refresh tokens
      - Check for SAML/OAuth credentials
      - Find authentication bypass tokens

   e. **Passwords and Passphrases**
      - Identify default or hardcoded passwords
      - Find password hashes in code
      - Locate admin credentials
      - Check for test/development passwords
      - Identify password reset tokens

2. **Analyze configuration files and environment variables:**

   a. **Configuration Files**
      - Review .env files and environment configurations
      - Check config.json, settings.py, application.yml
      - Analyze .properties, .ini, .conf files
      - Review Docker Compose environment sections
      - Check Kubernetes ConfigMaps and Secrets (if in repo)
      - Examine CI/CD configuration files (.github, .gitlab-ci.yml, .circleci)

   b. **Code Comments and Documentation**
      - Search for credentials in comments
      - Review TODO/FIXME comments with sensitive info
      - Check inline documentation for exposed secrets
      - Analyze README files for example credentials used in production

   c. **Test and Development Files**
      - Review test fixtures and mock data
      - Check development seeds and sample data
      - Analyze test configuration files
      - Review example and template files
      - Check for credentials in migration scripts

3. **Search version control history:**

   a. **Git History Analysis**
      - Scan all commits for previously committed secrets
      - Check for deleted files containing credentials
      - Review commit messages for sensitive information
      - Analyze renamed or moved files
      - Check for secrets in merged branches

   b. **Deleted or Renamed Files**
      - Identify removed configuration files
      - Check for deleted .env or credential files
      - Review historical versions of config files
      - Analyze file rename history

4. **Identify secret patterns using regex and entropy analysis:**

   a. **Pattern-Based Detection**
      - API key patterns (32-128 character alphanumeric strings)
      - AWS key patterns (AKIA[0-9A-Z]{16})
      - Private key headers (-----BEGIN PRIVATE KEY-----)
      - Connection string patterns (protocol://user:pass@host:port/db)
      - JWT patterns (eyJ[a-zA-Z0-9_-]*\.eyJ[a-zA-Z0-9_-]*\.[a-zA-Z0-9_-]*)
      - UUID patterns that might be tokens
      - Base64 encoded credentials

   b. **High Entropy Strings**
      - Identify strings with high Shannon entropy (>4.5)
      - Check for random-looking alphanumeric strings
      - Analyze potential encoded secrets
      - Review suspicious string constants

   c. **Provider-Specific Patterns**
      - AWS: AKIA, ASIA, aws_access_key_id, aws_secret_access_key
      - Google: AIza[0-9A-Za-z-_]{35}
      - Slack: xox[baprs]-[0-9a-zA-Z-]{10,48}
      - GitHub: gh[pousr]_[0-9a-zA-Z]{36}
      - Stripe: sk_live_[0-9a-zA-Z]{24}
      - Twilio: SK[0-9a-fA-F]{32}

5. **Analyze credential exposure risks:**

   a. **Public Repository Exposure**
      - Check if repository is public
      - Identify branches pushed to public forks
      - Review pull requests from external contributors
      - Analyze public GitHub Gists or Pastebin links

   b. **Log and Error Message Exposure**
      - Review logging statements for credential leakage
      - Check error messages for sensitive data
      - Analyze debug output and stack traces
      - Review console.log, print statements with credentials

   c. **Client-Side Code Exposure**
      - Identify secrets in frontend JavaScript
      - Check for API keys in mobile app code
      - Review bundled and minified code
      - Analyze source maps for credential exposure

6. **Assess credential management practices:**
   - Review use of environment variables
   - Check secret management solutions (HashiCorp Vault, AWS Secrets Manager, Azure Key Vault)
   - Analyze secret rotation practices
   - Review access control for secrets
   - Check encryption of secrets at rest

7. **For each identified secret or credential, provide:**
   - Type of secret (API key, password, token, etc.)
   - Exact location (file path, line number, commit hash if historical)
   - Severity rating (Critical, High, Medium, Low)
   - Exposure assessment (public, private, historical)
   - Service or system affected
   - Potential impact (account takeover, data breach, financial loss)
   - Remediation steps (rotate, revoke, migrate to secrets manager)
   - Prevention recommendations

**Expected Output:** A comprehensive secret detection report including:

- **Executive Summary:**
  - Total secrets found (active and historical)
  - Critical secrets requiring immediate rotation
  - Repository exposure status (public/private)
  - Overall secrets management maturity
  - Immediate action items

- **Active Secrets (Current Codebase):**
  For each secret:
  - Secret type and provider
  - File path and line number
  - Secret pattern or sample (partially masked)
  - Severity and risk level
  - Service affected
  - Exposure assessment
  - Impact if compromised
  - Remediation priority and steps

- **Historical Secrets (Git History):**
  For each historical secret:
  - Commit hash and date
  - File path (may be deleted)
  - Secret type
  - Exposure timeline
  - Whether still valid (needs rotation)
  - Git history cleanup requirements

- **Credential Management Assessment:**
  - Current practices evaluation
  - Environment variable usage
  - Secret manager implementation status
  - Secret rotation policies
  - Access control for secrets
  - Gaps and weaknesses

- **Remediation Roadmap:**

  **Immediate Actions (Critical):**
  - Rotate exposed API keys and tokens within 1 hour
  - Revoke compromised credentials
  - Change database passwords
  - Enable MFA on affected accounts
  - Monitor for unauthorized access

  **Short-term (High Priority):**
  - Migrate secrets to secret management solution
  - Clean Git history using tools like BFG Repo-Cleaner or git-filter-repo
  - Implement pre-commit hooks (git-secrets, detect-secrets, gitleaks)
  - Add .env to .gitignore
  - Update documentation with secure practices

  **Long-term:**
  - Implement secret scanning in CI/CD pipeline
  - Establish secret rotation policies
  - Deploy secret management solution (Vault, AWS Secrets Manager)
  - Train team on secret management best practices
  - Implement secret scanning for pull requests
  - Set up alerting for secret detection

- **Prevention Strategy:**
  - Pre-commit hook implementation (git-secrets, Talisman, detect-secrets)
  - CI/CD secret scanning integration (TruffleHog, GitGuardian, GitHub secret scanning)
  - Secret management solution deployment
  - Developer training and awareness
  - Code review checklist updates
  - .gitignore configuration

- **Scanning Tools Recommendations:**
  - TruffleHog (Git history scanning)
  - GitGuardian (Real-time secret detection)
  - GitHub secret scanning (for GitHub repos)
  - detect-secrets (Pre-commit hooks)
  - Gitleaks (Git secret scanner)
  - git-secrets (AWS secret prevention)
  - Yelp's detect-secrets (Baseline management)

**Example Output Format:**

```
CRITICAL: AWS Access Key Exposed in Public Repository
Location: src/config/aws.js:12
Commit: a1b2c3d (2024-01-15, still in current code)

Secret Type: AWS Access Key
Pattern: AKIAIOSFODNN7EXAMPLE (masked: AKIA...MPLE)

Severity: CRITICAL
Service: Amazon Web Services (AWS)
Exposure: Public repository, 300+ days exposed

Impact:
  - Unauthorized AWS resource access
  - Potential data exfiltration from S3 buckets
  - EC2 instance manipulation
  - Significant financial costs from resource abuse
  - Possible compliance violations (SOC2, ISO 27001)

Remediation Steps:
  1. IMMEDIATE: Revoke AWS access key via AWS Console/CLI:
     aws iam delete-access-key --access-key-id AKIAIOSFODNN7EXAMPLE

  2. IMMEDIATE: Rotate credentials and generate new access key

  3. Migrate to AWS Secrets Manager:
     - Store credentials in AWS Secrets Manager
     - Update code to retrieve from Secrets Manager
     - Use IAM roles for EC2/Lambda instead of access keys

  4. Clean Git history:
     git filter-repo --path src/config/aws.js --invert-paths
     (Coordinate with team, requires force push)

  5. Add pre-commit hook to prevent future leaks:
     pip install detect-secrets
     detect-secrets scan > .secrets.baseline

Prevention:
  - Add src/config/aws.js to .gitignore
  - Use environment variables or AWS SDK credential chain
  - Enable GitHub secret scanning
```

**Related Prompts:**
- security_owasp_top_10_analysis.md - Comprehensive security including sensitive data exposure
- security_authentication_authorization_review.md - Credential and token security
- security_cryptography_analysis.md - Encryption key management
- quality_code_documentation_coverage_analysis.md - Documentation review including exposed secrets

**When to Use:**
Use this prompt immediately for new codebases, before making repositories public, during security audits, after suspected credential exposure, as part of CI/CD pipeline checks, or when implementing secret management solutions. Critical for preventing unauthorized access and data breaches.

**Techniques Used:**
- ST-01 (Clear Objective Statement) - Opens with concise, unambiguous objective
- ST-02 (Structured Sequential Instructions) - Numbered steps for systematic scanning
- DT-02 (Specific Focus Areas with Examples) - Detailed credential types and patterns
- RT-02 (Multi-Dimensional Analysis Framework) - Type, Location, Severity, Impact, Remediation
- DS-06 (Prioritization and Severity Guidance) - Severity ratings and timeline priorities
- ST-03 (Output Format Templates) - Detailed finding output with masked examples
- DS-03 (Tool and Methodology Suggestions) - Recommends TruffleHog, GitGuardian, detect-secrets
