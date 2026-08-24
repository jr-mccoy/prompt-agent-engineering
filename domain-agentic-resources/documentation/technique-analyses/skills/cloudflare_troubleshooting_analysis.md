# Technique Analysis: cloudflare-troubleshooting

**Resource Type:** Skill
**Path:** `skills/web-development/cloudflare-troubleshooting/`
**Category:** Web Development
**Date Analyzed:** 2025-12-22
**Bundled Resources:** 2 scripts, 3 references (1,853 total lines)

## Overview

This skill provides systematic methodology for investigating and resolving Cloudflare configuration issues using API-driven evidence gathering. It demonstrates a mature "evidence-based debugging" pattern that prioritizes actual configuration state over assumptions, with comprehensive reference documentation for common issues.

**Bundled Resources Analysis:**
- **SKILL.md:** 326 lines - Investigation methodology, workflow templates, best practices
- **common_issues.md:** 262 lines - Symptom-based troubleshooting guide with solutions
- **ssl_modes.md:** 247 lines - SSL/TLS mode explanations with decision matrices
- **api_overview.md:** 539 lines - Complete API reference organized by category
- **check_cloudflare_config.py:** 293 lines - Diagnostic script (reference implementation)
- **fix_ssl_mode.py:** 186 lines - SSL mode fix script (reference implementation)

**Total Knowledge:** 1,853 lines of troubleshooting methodology and API reference

---

## Identified Techniques

### Technique 1: Evidence-Based Investigation Methodology (DS-56)

**Category:** DS (Domain-Specific)
**Pattern:** "Investigate with evidence, not assumptions" - systematically query actual state before diagnosis
**Mapping:** NEW technique

**Implementation:**

**Core Principle (stated upfront in SKILL.md):**
```markdown
**Investigate with evidence, not assumptions.** Always query Cloudflare API to examine actual configuration before diagnosing issues. The skill's value is the systematic investigation methodology, not predetermined solutions.
```

**Best Practices Section:**
```markdown
### Evidence-Based Investigation

1. **Query before assuming** - Use API to check actual state
2. **Gather multiple data points** - Cross-reference settings
3. **Check related configurations** - Settings often interact
4. **Verify externally** - Use dig/curl to confirm
5. **Test incrementally** - One change at a time
```

**Example Application:**
```bash
# DON'T assume SSL mode is wrong
# DO query to see actual value

curl -X GET "https://api.cloudflare.com/client/v4/zones/{zone_id}/settings/ssl" \
  -H "X-Auth-Email: email" \
  -H "X-Auth-Key: key"
```

**Effectiveness:**
- Prevents fixing the wrong problem
- Builds understanding of how system actually behaves
- Reduces trial-and-error cycles
- Creates audit trail of investigation

---

### Technique 2: API-First Troubleshooting (DS-57)

**Category:** DS (Domain-Specific)
**Pattern:** Use API calls to inspect actual configuration state rather than UI or assumptions
**Mapping:** NEW technique

**Implementation:**

Every troubleshooting pattern starts with API evidence gathering:

**Redirect Loop Investigation:**
```bash
# 1. Check SSL/TLS mode
curl -X GET "https://api.cloudflare.com/client/v4/zones/{zone_id}/settings/ssl" ...

# 2. Check Always Use HTTPS setting
curl -X GET "https://api.cloudflare.com/client/v4/zones/{zone_id}/settings/always_use_https" ...

# 3. Check Page Rules for redirects
curl -X GET "https://api.cloudflare.com/client/v4/zones/{zone_id}/pagerules" ...

# 4. Test origin server directly
curl -I -H "Host: <domain>" https://<origin_ip>
```

**Why API over UI:**
- API shows exact current state (no caching)
- Scriptable and repeatable
- Can check multiple settings quickly
- Creates documentation trail
- Enables automation

**Effectiveness:**
- Faster than clicking through UI
- More reliable (no UI lag)
- Programmatic access enables scripts and automation

---

### Technique 3: Symptom-Diagnostic-Fix Pattern (DS-58)

**Category:** DS (Domain-Specific)
**Pattern:** Structured troubleshooting flow: Symptom → Evidence gathering → Diagnosis logic → Fix → Verify
**Mapping:** NEW technique

**Implementation:**

From `common_issues.md`:

```markdown
## Redirect Loop Errors (ERR_TOO_MANY_REDIRECTS)

### Symptom
Browser displays "This page isn't working" or "ERR_TOO_MANY_REDIRECTS"

### Common Causes

#### 1. SSL Mode Mismatch (Most Common)
**Scenario:** Origin server enforces HTTPS, but Cloudflare SSL mode is "Flexible"

**Explanation:**
- Browser → HTTPS → Cloudflare
- Cloudflare → HTTP → Origin Server (because of Flexible mode)
- Origin Server → Redirects to HTTPS (because it enforces HTTPS)
- Infinite loop

**Affected Platforms:**
- GitHub Pages
- Netlify
- Vercel
- Heroku

**Solution:**
[Specific API calls to fix]
```

**Structure:**
1. **Symptom:** User-visible error
2. **Cause:** Technical explanation of root cause
3. **Scenario:** When this happens
4. **Explanation:** Step-by-step flow showing how error occurs
5. **Affected Platforms:** Contextual information
6. **Solution:** Concrete fix with code

**Effectiveness:**
- Users can self-diagnose from symptoms
- Explanation builds mental model
- Platform-specific guidance reduces guesswork

---

### Technique 4: Bundled Scripts as Reference Implementations (IT-30)

**Category:** IT (Interaction)
**Pattern:** Scripts serve as examples, not limitations - explicit guidance to prefer flexibility over convenience
**Mapping:** NEW technique

**Implementation:**

From SKILL.md:

```markdown
## When Scripts Are Useful

The bundled scripts (`scripts/check_cloudflare_config.py`, `scripts/fix_ssl_mode.py`) serve as:
- **Reference implementations** of investigation patterns
- **Quick diagnostic tools** when Python is available
- **Examples** of programmatic API usage

However, **prefer direct API calls via Bash/curl** for flexibility and transparency. Scripts should not limit capability - use them when convenient, but use raw API calls when needed for:
- Unfamiliar scenarios
- Edge cases
- Learning/debugging
- Operations not covered by scripts

The investigation methodology and API knowledge is the core skill, not the scripts.
```

**Why This Matters:**
- Prevents over-reliance on scripts
- Encourages learning underlying API
- Scripts as educational tools, not black boxes
- Flexibility when scripts don't cover edge cases

**Effectiveness:**
- Users understand "how it works" not just "how to run it"
- No vendor lock-in to specific tools
- Adaptable to new scenarios

---

### Technique 5: Multi-Perspective Verification (DS-59)

**Category:** DS (Domain-Specific)
**Pattern:** Cross-reference multiple data sources (API + external tools) to confirm diagnosis
**Mapping:** NEW technique

**Implementation:**

**DNS Issue Investigation:**
```bash
# 1. Check Cloudflare's configuration
curl -X GET "https://api.cloudflare.com/client/v4/zones/{zone_id}/dns_records" ...

# 2. Check external DNS resolution
dig <domain>
dig @8.8.8.8 <domain>

# 3. Check DNSSEC status
curl -X GET "https://api.cloudflare.com/client/v4/zones/{zone_id}/dnssec" ...
```

**SSL Certificate Investigation:**
```bash
# 1. Check Cloudflare's SSL configuration
curl -X GET "https://api.cloudflare.com/client/v4/zones/{zone_id}/ssl/certificate_packs" ...

# 2. Check origin certificate directly
openssl s_client -connect <origin_ip>:443 -servername <domain>

# 3. Test from Cloudflare's perspective
curl -I -H "Host: <domain>" https://<origin_ip>
```

**Data Sources:**
1. **Cloudflare API** - Configuration state
2. **External tools** (dig, curl, openssl) - Actual behavior
3. **Direct origin access** - Bypass Cloudflare to isolate issue

**Effectiveness:**
- Catches configuration vs. reality mismatches
- Identifies propagation delays
- Isolates where problem exists (Cloudflare vs. origin vs. DNS)

---

### Technique 6: Learning Methodology for APIs (ST-33)

**Category:** ST (Structural)
**Pattern:** Systematic approach to exploring unfamiliar APIs
**Mapping:** NEW technique

**Implementation:**

From SKILL.md:

```markdown
## Learning New APIs

When encountering issues not covered above, consult Cloudflare API documentation:

1. **Browse API reference:** https://developers.cloudflare.com/api/
2. **Search for relevant endpoints** using issue keywords
3. **Check API schema** to understand available operations
4. **Test with GET requests** first to understand data structure
5. **Make changes with PATCH/POST** after confirming approach

**Pattern for exploring new APIs:**
\```bash
# List available settings for a zone
curl -X GET "https://api.cloudflare.com/client/v4/zones/{zone_id}/settings" \
  -H "X-Auth-Email: email" \
  -H "X-Auth-Key: key"
\```
```

From `api_overview.md`:

```markdown
### Method 1: List All Settings
\```bash
curl -s -X GET "https://api.cloudflare.com/client/v4/zones/{zone_id}/settings" | jq '.result[] | {id, value}'
\```

This returns all available settings with current values. Use setting `id` to construct endpoint:
`/zones/{zone_id}/settings/{id}`

### Method 3: Explore API Interactively

**Pattern:**
1. Start with zone info to understand structure
2. List resources: `GET /zones/{zone_id}/{resource_type}`
3. Get specific item: `GET /zones/{zone_id}/{resource_type}/{id}`
4. Check available operations in docs
5. Make changes: `PATCH/POST/DELETE`
```

**Progression:**
1. Find relevant documentation
2. Understand data structure (GET all)
3. Understand specific resource (GET one)
4. Experiment read-only
5. Make changes carefully

**Effectiveness:**
- Teachable framework for API exploration
- Safe (GET first, modify later)
- Builds comprehensive mental model

---

### Technique 7: Platform-Specific Issue Matrix (DS-60)

**Category:** DS (Domain-Specific)
**Pattern:** Decision matrices showing which platforms have which requirements
**Mapping:** NEW technique

**Implementation:**

From `ssl_modes.md`:

```markdown
## Decision Matrix

| Origin Supports HTTPS? | Origin Certificate Valid? | Recommended Mode | Why |
|------------------------|---------------------------|------------------|-----|
| No | N/A | Flexible | Only option (but upgrade origin ASAP) |
| Yes | Self-signed/Invalid | Full | Encrypts traffic, doesn't validate cert |
| Yes | Valid from trusted CA | Full (Strict) | Maximum security |
| Yes (enforced) | Any | Full or Full (Strict) | Prevents redirect loops |

## Common Platforms and Recommended Modes

| Platform | Enforces HTTPS? | Recommended Mode | Notes |
|----------|-----------------|------------------|-------|
| GitHub Pages | Yes | Full or Full (Strict) | Full (Strict) preferred |
| Netlify | Yes | Full or Full (Strict) | Has valid certificates |
| Vercel | Yes | Full or Full (Strict) | Has valid certificates |
| Heroku | Yes | Full or Full (Strict) | Has valid certificates |
| Custom VPS | Depends | Full (Strict) if possible | Install Let's Encrypt cert |
| Shared Hosting | Varies | Check with host | Usually Full |
| AWS CloudFront | Configurable | Full (Strict) | Use ACM certificates |
```

**Why Matrices Work:**
- Quick lookup by platform
- Shows "why" not just "what"
- Covers 80% of use cases
- Prevents common mistakes

**Effectiveness:**
- Reduces "which setting do I use?" paralysis
- Platform-aware recommendations
- Clear decision criteria

---

### Technique 8: Tool Hierarchy Guidance (IT-31)

**Category:** IT (Interaction)
**Pattern:** Explicit guidance on when to use which tool with rationale
**Mapping:** NEW technique

**Implementation:**

```markdown
However, **prefer direct API calls via Bash/curl** for flexibility and transparency. Scripts should not limit capability - use them when convenient, but use raw API calls when needed for:
- Unfamiliar scenarios
- Edge cases
- Learning/debugging
- Operations not covered by scripts
```

**Tool Hierarchy:**
1. **Direct API calls** (most flexible, transparent, educational)
2. **Bundled scripts** (convenient for common cases)
3. **Cloudflare Dashboard** (visual, but slower)

**When to use each:**
- **API calls:** Learning, edge cases, automation, unfamiliar scenarios
- **Scripts:** Quick diagnostics, common patterns, when Python available
- **Dashboard:** Initial exploration, visual verification

**Effectiveness:**
- Users understand trade-offs
- Not locked into specific tools
- Clear guidance, not confusion

---

### Technique 9: Sequential Evidence Gathering (DS-61)

**Category:** DS (Domain-Specific)
**Pattern:** Ordered investigation sequences for common issues
**Mapping:** NEW technique

**Implementation:**

From SKILL.md:

```markdown
### Redirect Loops (ERR_TOO_MANY_REDIRECTS)

**Evidence gathering sequence:**

1. **Check SSL/TLS mode:**
   [curl command]
   Look for: `result.value` - tells current SSL mode

2. **Check Always Use HTTPS setting:**
   [curl command]

3. **Check Page Rules for redirects:**
   [curl command]
   Look for: `forwarding_url` or `always_use_https` actions

4. **Test origin server directly (if possible):**
   [curl command]

**Diagnosis logic:**
- SSL mode "flexible" + origin enforces HTTPS = redirect loop
- Multiple redirect rules can conflict
- Check browser vs curl behavior differences
```

**Order matters because:**
1. SSL mode is most common cause (check first)
2. Always Use HTTPS compounds SSL mode issues
3. Page Rules can override both
4. Origin server test isolates Cloudflare vs. origin

**Effectiveness:**
- Prioritizes most likely causes
- Systematic elimination
- Builds understanding of how settings interact

---

### Technique 10: Multi-Stage Verification Pattern (QA-16)

**Category:** QA (Quality Assurance)
**Pattern:** After making changes, verify at multiple levels with timing guidance
**Mapping:** NEW technique

**Implementation:**

From SKILL.md:

```markdown
### Making Changes

1. **Gather evidence first** - Understand current state
2. **Identify root cause** - Don't guess
3. **Apply targeted fix** - Change only what's needed
4. **Purge cache if needed** - Especially for SSL/redirect changes
5. **Verify fix** - Re-query API to confirm
6. **Inform user of wait times:**
   - Edge server propagation: 30-60 seconds
   - DNS propagation: Up to 48 hours
   - Browser cache: Requires manual clear
```

**Verification Stages:**
```bash
# 1. Apply fix
curl -X PATCH "https://api.cloudflare.com/client/v4/zones/ZONE_ID/settings/ssl" \
  --data '{"value":"full"}'

# 2. Purge cache
curl -X POST "https://api.cloudflare.com/client/v4/zones/ZONE_ID/purge_cache" \
  -d '{"purge_everything":true}'

# 3. Verify via API
curl -X GET "https://api.cloudflare.com/client/v4/zones/ZONE_ID/settings/ssl"

# 4. Wait and test externally
# Wait 60 seconds, clear browser cache, retry
```

**Timing Expectations:**
- API change: Immediate
- Edge propagation: 30-60 seconds
- DNS changes: Up to 48 hours
- Browser cache: Manual clear required

**Effectiveness:**
- Sets realistic expectations
- Prevents premature "it's not working" conclusions
- Complete verification at all layers

---

## Novel Patterns (Not in MASTER_TECHNIQUE_INDEX)

### Pattern 1: Evidence-Based Investigation Methodology (DS-56)

**Description:** "Investigate with evidence, not assumptions" - systematically query actual state before diagnosis

**Implementation:**
1. State core principle upfront ("never assume, always query")
2. Provide API calls to gather evidence
3. Show how to interpret evidence
4. Apply diagnosis based on evidence
5. Verify fix with evidence

**Use case:** Complex distributed systems where configuration != behavior

**Proposed category:** DS (Domain-Specific)
**Proposed code:** DS-56

---

### Pattern 2: API-First Troubleshooting (DS-57)

**Description:** Use API calls to inspect actual configuration state rather than UI or assumptions

**Implementation:**
- Every troubleshooting workflow starts with API queries
- Prefer programmatic access over UI
- Create audit trail of investigation
- Enable automation and repeatability

**Use case:** Cloud services, SaaS platforms, any system with API access

**Proposed category:** DS (Domain-Specific)
**Proposed code:** DS-57

---

### Pattern 3: Symptom-Diagnostic-Fix Pattern (DS-58)

**Description:** Structured troubleshooting flow: Symptom → Evidence → Diagnosis → Fix → Verify

**Implementation:**
```markdown
### Symptom
User-visible error

### Common Causes
Technical explanation

### Resolution Steps
1. Gather evidence
2. Diagnose
3. Fix
4. Verify
```

**Use case:** Troubleshooting guides, debugging workflows, support documentation

**Proposed category:** DS (Domain-Specific)
**Proposed code:** DS-58

---

### Pattern 4: Bundled Scripts as Reference Implementations (IT-30)

**Description:** Scripts serve as examples, not limitations - prefer flexibility over convenience

**Implementation:**
- Include scripts for common patterns
- Explicitly state: "These are reference implementations"
- Encourage using raw API for edge cases
- Scripts as learning tools, not black boxes

**Use case:** Skills that could be over-automated, educational contexts

**Proposed category:** IT (Interaction)
**Proposed code:** IT-30

---

### Pattern 5: Multi-Perspective Verification (DS-59)

**Description:** Cross-reference multiple data sources (API + external tools) to confirm diagnosis

**Data Sources:**
1. Service API (configuration state)
2. External tools (actual behavior)
3. Direct access (bypass service to isolate)

**Use case:** Distributed systems, CDNs, DNS, any multi-layer system

**Proposed category:** DS (Domain-Specific)
**Proposed code:** DS-59

---

### Pattern 6: Learning Methodology for APIs (ST-33)

**Description:** Systematic approach to exploring unfamiliar APIs

**Steps:**
1. Find documentation
2. List all resources (GET all)
3. Inspect specific resource (GET one)
4. Understand schema
5. Experiment read-only
6. Make changes carefully

**Use case:** Working with new APIs, self-service troubleshooting

**Proposed category:** ST (Structural)
**Proposed code:** ST-33

---

### Pattern 7: Platform-Specific Issue Matrix (DS-60)

**Description:** Decision matrices showing which platforms have which requirements

**Structure:**
| Platform | Requirement 1 | Requirement 2 | Recommended Setting | Notes |
|----------|---------------|---------------|---------------------|-------|

**Use case:** Multi-platform configurations, platform migrations

**Proposed category:** DS (Domain-Specific)
**Proposed code:** DS-60

---

### Pattern 8: Tool Hierarchy Guidance (IT-31)

**Description:** Explicit guidance on when to use which tool with rationale

**Implementation:**
- List available tools
- Rank by flexibility/power/learning value
- Specify "use X when Y" criteria
- Prevent tool over-reliance

**Use case:** Skills with multiple ways to accomplish tasks

**Proposed category:** IT (Interaction)
**Proposed code:** IT-31

---

### Pattern 9: Sequential Evidence Gathering (DS-61)

**Description:** Ordered investigation sequences prioritizing most likely causes

**Implementation:**
1. Most likely cause first
2. Each step eliminates possibilities
3. Build understanding of interactions
4. End with comprehensive diagnostic

**Use case:** Debugging, troubleshooting, root cause analysis

**Proposed category:** DS (Domain-Specific)
**Proposed code:** DS-61

---

### Pattern 10: Multi-Stage Verification Pattern (QA-16)

**Description:** After changes, verify at multiple levels with timing guidance

**Stages:**
1. Apply change
2. Purge relevant caches
3. Verify via API
4. Wait for propagation
5. Verify externally
6. Inform user of expected timings

**Use case:** Distributed systems, CDNs, DNS, any system with propagation delays

**Proposed category:** QA (Quality Assurance)
**Proposed code:** QA-16

---

## Multi-Technique Combinations

### Combination 1: Complete Investigation Workflow

**Techniques:** DS-56 (Evidence-Based) + DS-57 (API-First) + DS-61 (Sequential Gathering) + DS-59 (Multi-Perspective Verification)

**How they work together:**
1. Evidence-based mindset (DS-56)
2. Use API calls to gather evidence (DS-57)
3. Follow ordered sequence (DS-61)
4. Cross-reference with external tools (DS-59)
5. Arrive at diagnosis with confidence

**Effectiveness:** Systematic, thorough, builds understanding

---

### Combination 2: Safe Change Application

**Techniques:** DS-56 (Evidence-Based) + QA-16 (Multi-Stage Verification) + IT-30 (Tool Flexibility)

**How they work together:**
1. Gather evidence before changing (DS-56)
2. Apply fix with appropriate tool (IT-30)
3. Verify at multiple stages (QA-16)
4. Confirm resolution

**Effectiveness:** Prevents breaking things, ensures fix works

---

### Combination 3: Self-Service Troubleshooting

**Techniques:** DS-58 (Symptom-Diagnostic-Fix) + DS-60 (Platform Matrix) + ST-33 (Learning Methodology)

**How they work together:**
1. User identifies symptom (DS-58)
2. Checks platform-specific guidance (DS-60)
3. Learns to use API for edge cases (ST-33)

**Effectiveness:** Users can self-diagnose and fix issues

---

## Notes for Integration

### Impact on MASTER_TECHNIQUE_INDEX.md

**New Techniques to Add:**
- DS-56: Evidence-Based Investigation Methodology
- DS-57: API-First Troubleshooting
- DS-58: Symptom-Diagnostic-Fix Pattern
- DS-59: Multi-Perspective Verification
- DS-60: Platform-Specific Issue Matrix
- DS-61: Sequential Evidence Gathering
- IT-30: Bundled Scripts as Reference Implementations
- IT-31: Tool Hierarchy Guidance
- ST-33: Learning Methodology for APIs
- QA-16: Multi-Stage Verification Pattern

**Total:** 10 novel techniques

---

### Key Insights

1. **Evidence Over Assumptions:** The entire skill is built around "query, don't guess" philosophy

2. **API as Source of Truth:** Prefer programmatic access for accuracy and automation

3. **Education Over Automation:** Scripts as examples, not crutches - teach understanding

4. **Multi-Layer Verification:** Don't trust one source - cross-reference configuration, behavior, and external validation

5. **Systematic Methodology:** Reproducible investigation patterns that work across issues

---

### Recommended Use Cases

**Use DS-56 (Evidence-Based Investigation) when:**
- Configuration doesn't match expected behavior
- Users report issues that "should work"
- Debugging distributed systems

**Use DS-57 (API-First Troubleshooting) when:**
- System has API access
- Need repeatable diagnostics
- Building troubleshooting automation

**Use DS-58 (Symptom-Diagnostic-Fix) when:**
- Creating troubleshooting documentation
- Common support issues
- Knowledge base articles

**Use IT-30 (Scripts as Reference) when:**
- Could over-automate a skill
- Want users to learn, not just execute
- Edge cases exist beyond scripts

**Use DS-60 (Platform Matrix) when:**
- Multiple platforms with different requirements
- Common configuration questions
- Preventing platform-specific mistakes

---

## Summary

The cloudflare-troubleshooting skill is a masterclass in **systematic debugging methodology**. With 1,853 lines of bundled documentation across 6 files, it provides:

1. **Evidence-based philosophy** - Never assume, always query actual state
2. **API-first approach** - Programmatic access for accuracy and automation
3. **Multi-perspective verification** - Cross-reference API, external tools, direct access
4. **Educational mindset** - Scripts as examples, not black boxes

The 10 novel techniques identified focus on **investigation methodology** rather than Cloudflare-specific knowledge, making them broadly applicable to troubleshooting any API-driven service.

**Complexity Score:** 4/5 (Sophisticated debugging methodology with comprehensive reference docs)

**Novel Technique Count:** 10

**Primary Innovation:** Evidence-based API-first troubleshooting methodology that teaches diagnostic thinking, not just fixes
