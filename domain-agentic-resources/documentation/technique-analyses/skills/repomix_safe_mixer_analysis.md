# Technique Analysis: repomix-safe-mixer

**Resource Type:** Skill
**Path:** `claude-code-resources/skills/developer-tools/repomix-safe-mixer/`
**Date Analyzed:** 2025-12-22
**Bundled Resources:** 2 scripts (scan_secrets.py, safe_pack.py), 1 reference (common_secrets.md)
**Total Lines:** ~570 lines (316 SKILL.md + 202 scripts + 253 reference)
**Complexity:** 4/5

## Summary

repomix-safe-mixer is a **security-gated packaging skill** that prevents credential exposure when using repomix to package codebases. It implements a multi-phase workflow (scan → report → block/allow) with pattern-based credential detection, false positive filtering, and comprehensive remediation guidance. The skill exemplifies security-first development practices with 15+ credential patterns, risk classification, and automated enforcement gates.

## Identified Techniques

### Technique 1: Security Gate Enforcement
- **Category:** QA (Quality Assurance) - **NEW**
- **Pattern:** Block operations until security conditions are met
  ```python
  # scan_directory() → findings
  if findings:
      if not force:
          print("❌ Cannot pack: Secrets detected!")
          sys.exit(1)  # Blocks packaging
  # run_repomix() only if no secrets found
  ```
- **Example from resource:** `safe_pack.py` lines 131-148 - Scans first, blocks if secrets found, only packs if clean
- **Maps to existing:** **NEW** - Not in MASTER_TECHNIQUE_INDEX
- **Effectiveness:** Prevents accidental credential exposure at the tool level, not just warning level
- **Proposed code:** QA-19

### Technique 2: Pattern-Based Credential Detection
- **Category:** DS (Domain-Specific - Security) - **NEW**
- **Pattern:** Regex pattern library for identifying credential types
  ```python
  SECRET_PATTERNS = {
      'aws_access_key': r'(?i)AKIA[0-9A-Z]{16}',
      'stripe_key': r'(?:sk|pk)_(live|test)_[0-9a-zA-Z]{24,}',
      'jwt_token': r'eyJ[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}',
      # 15+ more patterns...
  }
  ```
- **Example from resource:** `scan_secrets.py` lines 16-29 - 15+ credential patterns
- **Maps to existing:** **NEW** - Security pattern detection at this depth not documented
- **Effectiveness:** Detects diverse credential types (cloud, API keys, auth tokens)
- **Proposed code:** DS-82

### Technique 3: Context-Aware False Positive Filtering
- **Category:** QA (Quality Assurance) - **NEW**
- **Pattern:** Multi-layer filtering to reduce false positives
  ```python
  def should_skip_match(line: str, match: str) -> bool:
      # Skip placeholders: 'your-', 'example', 'xxx', '${', 'TODO'
      # Skip comments: //, #, /*, *
      # Skip env var references: process.env.X, import.meta.env.X
  ```
- **Example from resource:** `scan_secrets.py` lines 89-108 + SKILL.md lines 208-227
- **Maps to existing:** **NEW** - Context-aware filtering at this sophistication
- **Effectiveness:** Reduces noise while maintaining high detection rate
- **Proposed code:** QA-20

### Technique 4: Multi-Mode Security Tooling
- **Category:** IT (Interaction Techniques) - Related to IT-30
- **Pattern:** Same scanner, multiple execution modes
  - **Standalone Mode:** `scan_secrets.py` for audits, pre-commit hooks
  - **Integrated Mode:** `safe_pack.py` for end-to-end workflow
  - **JSON Mode:** `--json` for programmatic consumption
- **Example from resource:**
  - Standalone: `scan_secrets.py ./project --json` (lines 89-119 in SKILL.md)
  - Integrated: `safe_pack.py ./project` (lines 19-56 in SKILL.md)
- **Maps to existing:** IT-30 (Multi-Mode CLI Design) - **EXTENSION**
- **Effectiveness:** Same core logic, different user workflows
- **Proposed code:** IT-30 (already identified, this confirms pattern)

### Technique 5: Risk-Stratified Documentation
- **Category:** ST (Structural Techniques) - **NEW**
- **Pattern:** Credential patterns documented with risk levels
  ```markdown
  **Stripe Secret Key**:
  - Risk: **CRITICAL** - Payment processing, refunds, customer data

  **Stripe Publishable Key**:
  - Risk: Low (public by design, but reveals account)

  **Supabase Service Role Key**:
  - Risk: **CRITICAL** - Full database admin access, bypasses RLS
  ```
- **Example from resource:** `common_secrets.md` lines 73-84, 59-61
- **Maps to existing:** **NEW** - Risk stratification in documentation
- **Effectiveness:** Helps users prioritize which findings to address first
- **Proposed code:** ST-33

### Technique 6: Remediation Template Provision
- **Category:** DS (Domain-Specific - Security) - **NEW**
- **Pattern:** Provide before/after code examples for secure conversion
  ```markdown
  ### Before (hardcoded):
  const SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...";

  ### After (environment variables):
  const SUPABASE_KEY = import.meta.env.VITE_SUPABASE_KEY || "your-anon-key-here";

  // Validation
  if (!import.meta.env.VITE_SUPABASE_KEY) {
    console.error("Missing VITE_SUPABASE_KEY");
  }
  ```
- **Example from resource:** SKILL.md lines 153-168, common_secrets.md lines 199-216
- **Maps to existing:** **NEW** - Security remediation templates
- **Effectiveness:** Shows exact transformation, reducing implementation friction
- **Proposed code:** DS-83

### Technique 7: Post-Incident Response Checklist
- **Category:** DS (Domain-Specific - Security) - **NEW**
- **Pattern:** Structured response steps for credential exposure
  ```markdown
  If credentials were already exposed:
  1. Rotate credentials immediately
  2. Revoke old credentials
  3. Audit usage
  4. Monitor for unusual activity
  5. Update deployment
  6. Document incident
  ```
- **Example from resource:** SKILL.md lines 197-206, common_secrets.md lines 235-245
- **Maps to existing:** **NEW** - Incident response as part of skill documentation
- **Effectiveness:** Reduces panic, ensures comprehensive response
- **Proposed code:** DS-84

### Technique 8: Grouped Reporting by Pattern Type
- **Category:** OT (Output Techniques) - **NEW**
- **Pattern:** Group findings by credential type, not by file
  ```python
  # Group by type
  by_type = {}
  for finding in findings:
      type_name = finding['type']
      if type_name not in by_type:
          by_type[type_name] = []
      by_type[type_name].append(finding)

  # Print: "🔴 stripe_key: 3 instance(s)"
  ```
- **Example from resource:** `safe_pack.py` lines 43-61
- **Maps to existing:** **NEW** - Security findings grouped by attack surface
- **Effectiveness:** Users understand credential blast radius (e.g., "3 Stripe keys exposed")
- **Proposed code:** OT-11

### Technique 9: Force Override with Explicit Warning
- **Category:** IT (Interaction Techniques) - **NEW**
- **Pattern:** Allow dangerous operations but with loud warnings
  ```bash
  safe_pack.py ./project --force  # ⚠️ NOT RECOMMENDED

  # Output:
  ⚠️  WARNING: --force flag set, packing anyway despite secrets found!
  ⚠️  WARNING: Package contains secrets (--force was used)
     DO NOT share this package publicly!
  ```
- **Example from resource:** SKILL.md lines 82-86, safe_pack.py lines 138-160
- **Maps to existing:** **NEW** - Dangerous operation pattern with warnings
- **Effectiveness:** Supports edge cases while making danger explicit
- **Proposed code:** IT-31

### Technique 10: Progressive Disclosure Security Reference
- **Category:** IT (Interaction Techniques) - Related to IT-14
- **Pattern:** SKILL.md provides overview, `common_secrets.md` provides deep reference
  - **SKILL.md:** Lists high-level credential types (lines 121-141)
  - **Reference:** Full patterns, regex, risk levels, remediation (253 lines)
- **Example from resource:**
  - Overview: "See `references/common_secrets.md` for complete list and patterns"
  - Reference: 13 credential categories with detection strategies, remediation patterns
- **Maps to existing:** IT-14 (Progressive Disclosure) - **CONFIRMATION**
- **Effectiveness:** Quick overview for common cases, deep reference for complex scenarios

## Novel Patterns (Not in MASTER_TECHNIQUE_INDEX)

### Pattern 1: Security Gate Enforcement (QA-19)
- **Description:** Block operations programmatically until security conditions are met
- **Implementation:**
  1. Run security scan
  2. Collect findings
  3. Exit with error code if findings exist (blocks downstream operations)
  4. Only proceed if clean OR explicit force override
- **Use case:** Pre-commit hooks, CI/CD pipelines, packaging tools, deployment gates
- **Example:**
  ```python
  findings = run_security_scan(directory)
  if findings and not force_flag:
      print("❌ Cannot proceed: Security issues detected!")
      sys.exit(1)  # Blocks operation
  # Operation only runs if clean
  ```
- **Proposed category:** QA (Quality Assurance)
- **Proposed code:** QA-19

### Pattern 2: Pattern-Based Credential Detection (DS-82)
- **Description:** Regex library for identifying diverse credential types in code
- **Implementation:**
  - Define patterns for credential types (AWS, Stripe, JWT, etc.)
  - Scan files line-by-line
  - Match against pattern library
  - Context-aware filtering for false positives
- **Use case:** Security audits, pre-commit scanning, package validation
- **Example:**
  ```python
  SECRET_PATTERNS = {
      'aws_access_key': r'(?i)AKIA[0-9A-Z]{16}',
      'stripe_key': r'(?:sk|pk)_(live|test)_[0-9a-zA-Z]{24,}',
      'jwt_token': r'eyJ[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}',
  }
  for line in file:
      for pattern_name, pattern in SECRET_PATTERNS.items():
          if re.search(pattern, line):
              # Potential credential found
  ```
- **Proposed category:** DS (Domain-Specific - Security)
- **Proposed code:** DS-82

### Pattern 3: Context-Aware False Positive Filtering (QA-20)
- **Description:** Multi-layer filtering to reduce security scan noise
- **Implementation:**
  1. **Placeholder detection:** Skip 'example', 'your-', 'xxx', '${VAR}', 'TODO'
  2. **Comment detection:** Skip lines starting with //, #, /*, *
  3. **Env var detection:** Skip process.env.X, import.meta.env.X references
  4. **File type filtering:** Lower priority for test files, example files
- **Use case:** Security scanning, credential detection, static analysis
- **Example:**
  ```python
  def should_skip_match(line: str, match: str) -> bool:
      # Skip placeholders
      if any(p in match.lower() for p in ['example', 'your-', '${', 'TODO']):
          return True
      # Skip comments
      if re.match(r'^\s*(?://|#|/\*)', line):
          return True
      # Skip env var references
      if 'process.env.' in line or 'import.meta.env.' in line:
          return True
      return False
  ```
- **Proposed category:** QA (Quality Assurance)
- **Proposed code:** QA-20

### Pattern 4: Risk-Stratified Documentation (ST-33)
- **Description:** Document patterns/options with explicit risk levels
- **Implementation:**
  - Classify items by risk (Low, Medium, High, CRITICAL)
  - Use visual indicators (bold, colors, emojis)
  - Explain risk impact for each level
- **Use case:** Security documentation, configuration guides, API documentation
- **Example:**
  ```markdown
  **Stripe Secret Key**:
  - Risk: **CRITICAL** - Payment processing, refunds, customer data access

  **Turnstile Site Key**:
  - Risk: Low (public by design), but enables testing

  **Force Pack Flag**:
  ⚠️ NOT RECOMMENDED - Skips security scan, may expose credentials
  ```
- **Proposed category:** ST (Structural Techniques)
- **Proposed code:** ST-33

### Pattern 5: Remediation Template Provision (DS-83)
- **Description:** Provide before/after code examples for secure transformation
- **Implementation:**
  1. Show problematic code (Before)
  2. Show corrected code (After)
  3. Explain the transformation
  4. Provide validation/testing examples
- **Use case:** Security guidance, refactoring instructions, migration guides
- **Example:**
  ```markdown
  ### Before (insecure):
  const API_KEY = "sk-live-abc123...";

  ### After (secure):
  const API_KEY = import.meta.env.VITE_API_KEY || "your-api-key-here";

  if (!import.meta.env.VITE_API_KEY) {
    console.error("⚠️ Missing VITE_API_KEY environment variable");
  }
  ```
- **Proposed category:** DS (Domain-Specific - Security)
- **Proposed code:** DS-83

### Pattern 6: Post-Incident Response Checklist (DS-84)
- **Description:** Structured response steps for security incidents
- **Implementation:**
  - Provide ordered checklist (1, 2, 3, 4...)
  - Cover immediate actions (rotate, revoke)
  - Cover investigation (audit, monitor)
  - Cover long-term actions (document, update processes)
- **Use case:** Security incident response, disaster recovery, postmortem procedures
- **Example:**
  ```markdown
  If credentials were exposed:
  1. **Rotate immediately** - Generate new keys/tokens
  2. **Revoke old credentials** - Disable compromised credentials
  3. **Audit usage** - Check logs for unauthorized access
  4. **Monitor** - Set up alerts for unusual activity
  5. **Update deployment** - Deploy code with new credentials
  6. **Document incident** - Record what was exposed and actions taken
  ```
- **Proposed category:** DS (Domain-Specific - Security)
- **Proposed code:** DS-84

### Pattern 7: Grouped Reporting by Attack Surface (OT-11)
- **Description:** Group security findings by credential type, not by location
- **Implementation:**
  - Collect all findings
  - Group by credential type (aws_access_key, stripe_key, etc.)
  - Report count per type
  - Show blast radius (e.g., "3 Stripe keys exposed")
- **Use case:** Security reporting, vulnerability aggregation, risk assessment
- **Example:**
  ```python
  by_type = {}
  for finding in findings:
      type_name = finding['type']
      by_type.setdefault(type_name, []).append(finding)

  for secret_type, instances in by_type.items():
      print(f"🔴 {secret_type}: {len(instances)} instance(s)")
      for instance in instances[:3]:  # Show first 3
          print(f"   - {instance['file']}:{instance['line']}")
  ```
- **Proposed category:** OT (Output Techniques)
- **Proposed code:** OT-11

### Pattern 8: Force Override with Explicit Warning (IT-31)
- **Description:** Allow dangerous operations but with loud, repeated warnings
- **Implementation:**
  - Provide `--force` flag for override
  - Add warnings in documentation (⚠️ NOT RECOMMENDED)
  - Print warnings during execution
  - Print warnings in final output
- **Use case:** Dangerous operations, destructive commands, security bypasses
- **Example:**
  ```bash
  # Documentation
  --force  # ⚠️ NOT RECOMMENDED - Skip security scan

  # During execution
  ⚠️  WARNING: --force flag set, packing anyway despite secrets found!

  # Final output
  ⚠️  WARNING: Package contains secrets (--force was used)
     DO NOT share this package publicly!
  ```
- **Proposed category:** IT (Interaction Techniques)
- **Proposed code:** IT-31

## Multi-Technique Combinations

### Combination 1: Security-Gated Workflow
**Techniques:** QA-19 (Security Gate) + DS-82 (Pattern Detection) + QA-20 (False Positive Filtering)
- **Pattern:** Comprehensive security scanning before allowing operations
- **Example:** `safe_pack.py` workflow:
  1. Pattern-based scanning (DS-82)
  2. False positive filtering (QA-20)
  3. Gate enforcement - block if secrets found (QA-19)

### Combination 2: Progressive Disclosure Security Knowledge
**Techniques:** IT-14 (Progressive Disclosure) + ST-33 (Risk Stratification) + DS-83 (Remediation Templates)
- **Pattern:** Layered security documentation from overview to deep reference
- **Example:**
  - SKILL.md: Overview with risk indicators (ST-33)
  - common_secrets.md: Full patterns, risk levels, remediation templates (DS-83)
  - Load reference only when needed (IT-14)

### Combination 3: Multi-Mode Security Operations
**Techniques:** IT-30 (Multi-Mode CLI) + OT-11 (Grouped Reporting) + IT-31 (Force Override)
- **Pattern:** Same scanner, multiple execution contexts with appropriate output
- **Example:**
  - Standalone mode: `scan_secrets.py --json` for CI/CD (IT-30)
  - Integrated mode: `safe_pack.py` with grouped reporting (OT-11)
  - Force mode: `--force` with explicit warnings (IT-31)

## Notes for Integration

### Integration with MASTER_TECHNIQUE_INDEX.md
1. **Add 8 new techniques:**
   - QA-19: Security Gate Enforcement
   - QA-20: Context-Aware False Positive Filtering
   - DS-82: Pattern-Based Credential Detection
   - DS-83: Remediation Template Provision
   - DS-84: Post-Incident Response Checklist
   - ST-33: Risk-Stratified Documentation
   - OT-11: Grouped Reporting by Attack Surface
   - IT-31: Force Override with Explicit Warning

2. **Confirm existing technique:**
   - IT-14: Progressive Disclosure (SKILL.md + bundled reference)
   - IT-30: Multi-Mode CLI Design (standalone + integrated + JSON modes)

### Integration with USE_CASE_LOOKUP.md
1. **Add to "Security Analysis" use case:**
   - Pre-commit scanning: DS-82 + QA-20 + QA-19
   - Credential detection: DS-82 + ST-33 (risk stratification)
   - Security remediation: DS-83 + DS-84

2. **Add to "DevOps/CI-CD" use case:**
   - Security gates: QA-19 + IT-30 (JSON mode for programmatic use)
   - Pre-deployment validation: DS-82 + OT-11 (grouped reporting)

### Key Insights
1. **Security gates at tool level:** Unlike warnings, this skill blocks operations programmatically
2. **15+ credential patterns:** Comprehensive coverage of cloud, API, and auth credentials
3. **Context-aware filtering:** Sophisticated false positive reduction
4. **Risk stratification:** Helps users prioritize critical findings
5. **Remediation templates:** Reduces friction in fixing security issues
6. **Multi-mode operation:** Same scanner for different workflows (audit, CI/CD, packaging)

### Real-World Applications
1. **Pre-commit hooks:** Block commits containing hardcoded credentials
2. **CI/CD pipelines:** Security gate before deployment
3. **Code packaging:** Prevent credential exposure in distributed packages
4. **Security audits:** Comprehensive codebase scanning
5. **Developer education:** Remediation templates teach secure practices

---

**Analysis Metadata:**
- **Complexity:** 4/5 (sophisticated pattern matching + workflow orchestration)
- **Novel Techniques:** 8 (QA-19, QA-20, DS-82, DS-83, DS-84, ST-33, OT-11, IT-31)
- **Confirmed Techniques:** 2 (IT-14, IT-30)
- **Bundled Knowledge:** 570+ lines (scripts + reference documentation)
- **Production Readiness:** High - Includes error handling, JSON output, CI/CD integration
- **Educational Value:** High - Teaches security patterns through remediation templates
