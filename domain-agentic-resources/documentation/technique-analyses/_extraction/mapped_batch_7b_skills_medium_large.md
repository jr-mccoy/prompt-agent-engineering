# Mapped Technique Inventory — Batch 7b (Skills Medium-Large, Files 7-11)

**Date:** 2026-02-09
**Input:** `_extraction/batch_7_skills_medium_large.md` (Files 7-11) + `_extraction/master_index_reference.md`
**Techniques Mapped:** 51
**Master Reference Version:** 193 active techniques

---

## File 7: llm_icon_finder_analysis.md (8 techniques)

| # | Source File | Technique Name | Code | Family | Original Mapping | Verified Mapping | Status | Notes |
|---|------------|----------------|------|--------|-----------------|-----------------|--------|-------|
| 84 | llm_icon_finder_analysis.md | URL Pattern Templates | DS-50 | DS | No — NEW | CODE COLLISION — DS-50 is "STRIDE-Per-Interaction Matrix" in master | CONFIRMED-NOVEL | URL construction templates with placeholders for dynamic generation. No match in master. Code DS-50 collides with master (STRIDE threat model). Also collides with #45 in Batch 7a. Needs new code assignment. |
| 85 | llm_icon_finder_analysis.md | Multi-Language Entity Mapping | IT-28 | IT | No — NEW | No match found | CONFIRMED-NOVEL | Map cross-language queries (Chinese/English) to canonical identifiers. IT family only has IT-19, IT-35 in master. No technique covers multilingual entity resolution. |
| 86 | llm_icon_finder_analysis.md | Fallback Strategy Pattern | DS-51 | DS | No — NEW | No match found | CONFIRMED-NOVEL | Progressive fallback strategies with increasing generality when primary approach fails. DS-51 not in master. QA-13 (Failure Recovery Specification) is about handling repeated failures, not progressive fallback chains — different concept. |
| 87 | llm_icon_finder_analysis.md | Reference Catalog Pattern | IT-29 | IT | No — NEW | No match found | CONFIRMED-NOVEL | Extensive catalog in bundled reference for quick lookup organized by category. IT-19 (Three-Tier Information Loading) covers the loading pattern; this is about the catalog's internal structure and organization — a complementary but distinct concern. |
| 88 | llm_icon_finder_analysis.md | Convention Documentation | DS-52 | DS | No — NEW | No match found | CONFIRMED-NOVEL | Document naming conventions and variant patterns to enable inference. No direct match in master. Collides with #48 (Risk Score Matrix Calculation) in Batch 7a. Needs new code. |
| 89 | llm_icon_finder_analysis.md | Example-Driven Workflow | — | IT | Yes — ST-04 / IT-06 | ST-04 exists but poor semantic match; IT-06 not in master | NEEDS-REVIEW | "Show concrete examples for each use case with expected inputs and outputs." ST-04 is "Delimited Sections" (structural separators) — poor match. IT-06 doesn't exist. Closest matches: ED-05 (Reference Class Priming — show excellent output example) or AG-05 (Concrete Deliverable Templates). Suggest remapping to ED-05. |
| 90 | llm_icon_finder_analysis.md | Three-Tier Progressive Loading | — | IT | Yes — IT-19 | Matches IT-19 (Three-Tier Information Loading) | CONFIRMED-EXISTING | EXACT MATCH. "Metadata > Core > References progressive loading" directly maps to IT-19 "Metadata → SKILL.md → Bundled resources (progressive disclosure)." |
| 91 | llm_icon_finder_analysis.md | Multi-Format Support Documentation | — | DS | Yes — DS-07 | DS-07 not in master | NEEDS-REVIEW | "Document all supported formats with format-specific guidance." DS-07 does not exist in master (DS jumps from DS-06 to DS-13). Closest matches: ST-03 (Output Format Specification — format requirements) or OC-08 (Multi-Mode Prompt Architecture — multiple modes). Suggest remapping to ST-03. |

---

## File 8: prompt_optimizer_analysis.md (12 techniques)

| # | Source File | Technique Name | Code | Family | Original Mapping | Verified Mapping | Status | Notes |
|---|------------|----------------|------|--------|-----------------|-----------------|--------|-------|
| 92 | prompt_optimizer_analysis.md | EARS Syntax Transformation | DS-21 | DS | No — NEW | CODE COLLISION — DS-21 is "Proximity Assessment"; matches DS-22 (EARS Requirements Transformation) | MATCHED-EXISTING | Batch marked as novel but DS-22 in master is "EARS Requirements Transformation" — EXACT conceptual match. Code DS-21 was incorrectly assigned (collides with master's "Proximity Assessment"). Maps to DS-22. |
| 93 | prompt_optimizer_analysis.md | Domain Theory Grounding | ST-26 | ST | No — NEW | Matches DS-23 (Domain Theory Grounding) | MATCHED-EXISTING | Batch marked as novel but DS-23 in master is "Domain Theory Grounding" — EXACT match. Was incorrectly assigned to ST family with code ST-26 (doesn't exist). Maps to DS-23. |
| 94 | prompt_optimizer_analysis.md | Four-Layer Enhancement Process | MP-06 | MP | No — NEW | CODE COLLISION — MP-06 is "Fallback Question Protocol" in master | CONFIRMED-NOVEL | "Systematic refinement: EARS transformation > Domain grounding > Example extraction > Structured generation." MP-06 in master is "Fallback Question Protocol" — completely different. NE-02 (Phased Workflow Architecture) and DT-03 (Iterative Refinement) are related but this is a specific 4-layer prompt optimization process. Needs new code. |
| 95 | prompt_optimizer_analysis.md | Role/Skills/Workflows/Examples/Formats Framework | — | ST | Yes — ST-04 | Matches ST-04 (Delimited Sections) | CONFIRMED-EXISTING | "Standard five-section prompt structure" is a prompt organized with named delimited sections. ST-04 covers this pattern broadly. |
| 96 | prompt_optimizer_analysis.md | Transformation Checklist | — | QA | Yes — QA-01 | Matches QA-01 (Self-Verification) | CONFIRMED-EXISTING | "Systematic checklist for requirement transformation quality gates." QA-01 is "Built-in self-critique step requiring review" — a transformation checklist is a specific form of self-verification. |
| 97 | prompt_optimizer_analysis.md | Theory Citation for Credibility | ST-27 | ST | No — NEW | Extends DS-23 (Domain Theory Grounding) | EXTENDS-EXISTING | "Explicitly reference established frameworks/theories in prompts for authority." DS-23 is about systematic framework integration (40+ theories). This extends by focusing on the credibility/authority angle of citing established theories. Related but distinct emphasis. |
| 98 | prompt_optimizer_analysis.md | Concrete Example Extraction | — | RT | Yes — RT-07 | RT-07 exists but poor semantic match | NEEDS-REVIEW | "Generate specific examples with real data, not placeholders." RT-07 in master is "Cascade Effect Analysis" (mapping first/second/third-order effects) — POOR match. Closest matches: ED-05 (Reference Class Priming — show example of excellent output) or AG-05 (Concrete Deliverable Templates — actual working code). Suggest remapping to ED-05 or AG-05. |
| 99 | prompt_optimizer_analysis.md | Progressive Reference Loading | — | IT | Yes — IT-06 / IT-15 | Neither IT-06 nor IT-15 in master | NEEDS-REVIEW | "Four reference files loaded only when needed." IT-06 and IT-15 do not exist in master (only IT-19, IT-35). IT-19 (Three-Tier Information Loading) is the closest match. CM-07 (Token-Budget-Aware Progressive Loading) also related. Suggest remapping to IT-19. |
| 100 | prompt_optimizer_analysis.md | Measurable Success Criteria | — | DS | Yes — DS-02 | Matches DS-02 (Metric Specification) | CONFIRMED-EXISTING | EXACT MATCH. "Require quantifiable metrics in specifications" maps directly to DS-02 "Define specific, measurable criteria." |
| 101 | prompt_optimizer_analysis.md | Atomic Requirement Decomposition | DS-22 | DS | No — NEW | CODE COLLISION — DS-22 is "EARS Requirements Transformation" in master | CONFIRMED-NOVEL | "Break compound requirements into single-action, independently testable statements." DS-22 in master is EARS methodology — related domain but distinct technique. DT-01 (Hierarchical Task Breakdown) is about task decomposition, not requirement atomization. Genuinely novel. Needs new code. |
| 102 | prompt_optimizer_analysis.md | Multi-Stakeholder Requirements | — | NE | No — NEW | Extends DS-22 (EARS Requirements Transformation) | EXTENDS-EXISTING | "Create EARS statements for each user type/role in complex systems." This extends DS-22 by adding the multi-stakeholder dimension — applying EARS methodology per user role rather than as a single set. |
| 103 | prompt_optimizer_analysis.md | Before/After Transformation Examples | — | OT | Yes — OT-04 | OT family not in master | NEEDS-REVIEW | "Show original requirement and optimized version side-by-side." OT (Output Techniques) family does not exist in master. Closest match: NE-04 (Good vs Bad Example Calibration — explicit contrast pairs bad → good). Suggest remapping to NE-04. |

---

## File 9: youtube_downloader_analysis.md (11 techniques)

| # | Source File | Technique Name | Code | Family | Original Mapping | Verified Mapping | Status | Notes |
|---|------------|----------------|------|--------|-----------------|-----------------|--------|-------|
| 104 | youtube_downloader_analysis.md | Quality Expectation Matrix | OT-09 | OT | No — NEW | Matches ST-22 (Multi-Solution Comparison Matrix) | MATCHED-EXISTING | "Upfront matrix showing what each method/setup achieves including negative capabilities." ST-22 is "Side-by-side comparison of competing approaches with objective criteria" — direct conceptual match. OT family doesn't exist in master. |
| 105 | youtube_downloader_analysis.md | Fallback Strategy Chain | — | DS | Yes — DS-51 | DS-51 not in master | NEEDS-REVIEW | "Ordered sequence of methods from ideal to acceptable with transition criteria." DS-51 does not exist in master. QA-13 (Failure Recovery Specification) is related but broader. Also likely a duplicate of #86 (Fallback Strategy Pattern) from File 7. Suggest mapping to QA-13 or marking as duplicate of #86. |
| 106 | youtube_downloader_analysis.md | Verification-Driven Workflow | — | QA | Yes — QA-01 | Matches QA-01 (Self-Verification) | CONFIRMED-EXISTING | "Check > Execute > Verify cycle at each stage with domain-specific checks." QA-01 is "Built-in self-critique step requiring review after initial response." The verify cycle maps to self-verification. |
| 107 | youtube_downloader_analysis.md | Warning Triage Classification | DS-77 | DS | No — NEW | Matches QA-12 (False Positives Identification) | MATCHED-EXISTING | "Classify warnings as Harmless vs Action Required." QA-12 is "Explicit section to identify what NOT to pay attention to." Classifying harmless warnings is essentially false positive identification. Direct conceptual match. |
| 108 | youtube_downloader_analysis.md | Environment-Specific Guidance | — | DS | Yes — DS-60 | DS-60 not in master | NEEDS-REVIEW | "Identify geographic/network contexts requiring special handling." DS-60 does not exist in master. CM-01 (Explicit Context Framing) and CM-03 (Scope Definition) are tangentially related. DS-107 (Version-Specific Expertise) covers version-specific but not environment-specific contexts. No strong match. |
| 109 | youtube_downloader_analysis.md | Isolated Environment Dependency Installation | DS-78 | DS | No — NEW | No match found | CONFIRMED-NOVEL | "Workflow to identify tool's isolated environment and install dependencies into it." Very specific DevOps/tooling technique. DS-03 (Tool and Methodology Suggestions) recommends tools but doesn't cover isolated environment management. No match in master. |
| 110 | youtube_downloader_analysis.md | Command Pattern Library with Inline Documentation | — | OT | Yes — OT-01 / DS-02 | OT-01 not in master; DS-02 poor semantic match | NEEDS-REVIEW | "Ready-to-use commands with parameter explanations inline." OT family doesn't exist in master. DS-02 is "Metric Specification" — poor match. Better matches: DS-80 (Multi-Tiered Template Library — quick examples → complete references) or AG-05 (Concrete Deliverable Templates — actual working code). Suggest remapping to AG-05 or DS-80. |
| 111 | youtube_downloader_analysis.md | Problem-Symptom-Solution Mapping | — | DS | Yes — DS-03 | DS-03 exists but weak semantic match | NEEDS-REVIEW | "Structured troubleshooting with symptoms, cause, and ordered solutions." DS-03 is "Tool and Methodology Suggestions" (recommend specific tools) — related but not the same as structured troubleshooting. RT-02 (Multi-Dimensional Analysis Framework) could apply. Consider also DS-04 (Pattern Recognition Requests). Weak match overall. |
| 112 | youtube_downloader_analysis.md | Bundled Wrapper Script with Automatic Workarounds | — | DS | Yes — IT-14 / AG-19 | Neither IT-14 nor AG-19 in master | NEEDS-REVIEW | "Python wrapper that applies common workarounds by default." IT-14 not in master (only IT-19, IT-35). AG-19 not in master (AG goes ...AG-18, AG-26). Closest matches: AG-05 (Concrete Deliverable Templates — actual working code) for the wrapper script aspect, or IT-19 (bundled resources) for the bundling aspect. |
| 113 | youtube_downloader_analysis.md | Progressive Complexity Disclosure | — | IT | Yes — IT-01 | IT-01 not in master | NEEDS-REVIEW | "Start basic, then add advanced content progressively." IT-01 does not exist in master (only IT-19, IT-35). IT-19 (Three-Tier Information Loading) is the closest conceptual match — progressive disclosure of increasing detail. Suggest remapping to IT-19. |
| 114 | youtube_downloader_analysis.md | Criticality Labeling | ST-32 | ST | No — NEW | No match found | CONFIRMED-NOVEL | "Use semantic bold prefixes (Critical, Verification, Cause, Benefits, Requirement)." ST-32 not in master. DS-06 (Prioritization and Severity Guidance) is about ranking findings, not inline semantic labeling. ST-04 (Delimited Sections) is structural but doesn't cover semantic criticality prefixes. Novel formatting technique. |

---

## File 10: github_ops_analysis.md (10 techniques)

| # | Source File | Technique Name | Code | Family | Original Mapping | Verified Mapping | Status | Notes |
|---|------------|----------------|------|--------|-----------------|-----------------|--------|-------|
| 115 | github_ops_analysis.md | Comprehensive API Reference Bundling | DS-97 | DS | No — NEW | Matches DS-24 (API Reference Bundling) | MATCHED-EXISTING | Batch marked as novel but DS-24 in master is "API Reference Bundling" — "Include comprehensive API documentation to enable autonomous tool usage." EXACT conceptual match. DS-97 was incorrectly assigned as new. |
| 116 | github_ops_analysis.md | Convention-Based Validation Bypass | DS-98 | DS | No — NEW | No match found | CONFIRMED-NOVEL | "Use explicit prefixes (JIRA ticket ID vs NOJIRA) to signal validation bypass." No match in master. Using naming conventions/prefixes as bypass signals is a distinct pattern not covered by existing techniques. |
| 117 | github_ops_analysis.md | Output Format Adapter Pattern | DS-99 | DS | No — NEW | No match found | CONFIRMED-NOVEL | "Multiple output formats (JSON, template, human-readable) for different consumption." OC-08 (Multi-Mode Prompt Architecture) is about user-triggered modes, not consumer-based format adaptation. ST-03 (Output Format Specification) defines format requirements but not multi-format adapters. Distinct pattern. |
| 118 | github_ops_analysis.md | CLI Tool Pipeline Pattern | DS-100 | DS | No — NEW | No match found | CONFIRMED-NOVEL | "UNIX-style tool composition (gh + jq + xargs) for complex operations." No existing technique covers CLI tool composition patterns. Novel implementation technique. |
| 119 | github_ops_analysis.md | Exponential Backoff Retry Pattern | QA-23 | QA | No — NEW | Extends QA-13 (Failure Recovery Specification) | EXTENDS-EXISTING | "Production-grade retry logic with exponential backoff for API resilience." QA-13 is "Explicit rules for handling repeated failures." Exponential backoff is a specific, well-known implementation of failure recovery. Extends QA-13 with a concrete retry strategy. |
| 120 | github_ops_analysis.md | Conditional Reference Loading | IT-33 | IT | No — NEW | No match found | CONFIRMED-NOVEL | "Load specific documentation references only when needed for particular operations." IT-19 (Three-Tier Information Loading) is about progressive disclosure tiers. CM-07 (Token-Budget-Aware Progressive Loading) is about token budget. This uses operation type as the trigger — a distinct mechanism from both. |
| 121 | github_ops_analysis.md | Multi-Strategy Pagination | DS-101 | DS | No — NEW | No match found | CONFIRMED-NOVEL | "Multiple pagination approaches (limit-based, page-based, sentinel loop)." No pagination-related techniques exist in master. Novel API data retrieval pattern. |
| 122 | github_ops_analysis.md | Multi-Instance Authentication Pattern | DS-102 | DS | No — NEW | No match found | CONFIRMED-NOVEL | "Support both public and enterprise instances with instance-aware authentication." No authentication-related patterns in master. Novel integration technique. |
| 123 | github_ops_analysis.md | Selective Field Loading | IT-34 | IT | No — NEW | No match found | CONFIRMED-NOVEL | "Allow selective field retrieval to minimize API payload and processing." CM-07 (Token-Budget-Aware Progressive Loading) is about token management, not API field selection. Novel API optimization pattern. |
| 124 | github_ops_analysis.md | Bulk Operation Safety Patterns | — | QA | Yes — QA-02 | QA-02 exists but poor semantic match | NEEDS-REVIEW | "Safe bulk operation patterns with xargs and JSON output." QA-02 is "Adversarial Stress-Test" (attack your own answer) — poor match. Better candidates: QA-09 (Reversibility Assessment — can actions be undone), AG-04 (Behavioral Guardrails — explicit constraints), or CM-09 (Authority Boundary Specification — permission model). Suggest remapping to AG-04 or QA-09. |

---

## File 11: k8s_security_policies_analysis.md (10 techniques)

| # | Source File | Technique Name | Code | Family | Original Mapping | Verified Mapping | Status | Notes |
|---|------------|----------------|------|--------|-----------------|-----------------|--------|-------|
| 125 | k8s_security_policies_analysis.md | Security Tier Classification | DS-61 | DS | No — NEW | Matches DS-61 (Security Tier Classification) | CONFIRMED-EXISTING | EXACT MATCH. Batch marked as "NEW" but DS-61 already exists in master: "Defense-in-depth with 6 security layers." Same technique, same code. |
| 126 | k8s_security_policies_analysis.md | Default Deny + Selective Allow Pattern | DS-62 | DS | No — NEW | No match found | CONFIRMED-NOVEL | "Start with default deny, then add selective allow policies for defense-in-depth." DS-118 (Security-Default Behavioral Traits) is about agent behavioral defaults, not network/policy deny-allow patterns. DS-61 covers security layers but not deny/allow policy patterns specifically. Novel infrastructure security technique. |
| 127 | k8s_security_policies_analysis.md | Template Library Organization | DS-63 | DS | No — NEW | Extends DS-80 (Multi-Tiered Template Library) | EXTENDS-EXISTING | "Organize templates by use case with priority annotations (Start Here, Essential)." DS-80 is "Quick examples → complete references → production templates." This extends with use-case-based organization and priority annotations for template discovery. |
| 128 | k8s_security_policies_analysis.md | Compliance Framework Mapping | DS-64 | DS | No — NEW | Extends DS-111 (External Methodology Compliance) | EXTENDS-EXISTING | "Map technical controls to compliance framework requirements (CIS, NIST)." DS-111 is "Strict adherence to external standards (C4, OWASP, SRE)." This extends by adding explicit mapping from controls TO framework requirements — the reverse direction (mapping vs. adhering). |
| 129 | k8s_security_policies_analysis.md | Policy Enforcement Layer Documentation | DS-65 | DS | No — NEW | No match found | CONFIRMED-NOVEL | "Document admission control with policy-as-code (ConstraintTemplate + Constraint)." Very specific to Kubernetes/OPA/Gatekeeper policy enforcement. No match in master for policy-as-code patterns. |
| 130 | k8s_security_policies_analysis.md | Service Mesh Security Integration | DS-66 | DS | No — NEW | Extends DS-61 (Security Tier Classification) | EXTENDS-EXISTING | "Layered security: network layer + transport layer (mTLS) + application layer." DS-61 is "Defense-in-depth with 6 security layers." This is a service-mesh-specific application of the security tier pattern, extending with mTLS and mesh-specific layers. |
| 131 | k8s_security_policies_analysis.md | Resource-Scoped Permissions | DS-67 | DS | No — NEW | No match found | CONFIRMED-NOVEL | "RBAC with resourceNames for fine-grained access to specific named resources." CM-09 (Authority Boundary Specification) defines three permission zones for agents — different scope. No Kubernetes RBAC-specific pattern in master. |
| 132 | k8s_security_policies_analysis.md | Troubleshooting Command Sequences | — | DS | Yes — DS-59 | DS-59 not in master | NEEDS-REVIEW | "Diagnostic command > Fix command pattern for debugging." DS-59 does not exist in master (DS jumps from DS-56 to DS-61). Closest matches: DS-03 (Tool and Methodology Suggestions) or ST-02 (Structured Sequential Instructions). Also appears in Batch 7a (#32, #33 mapped to same non-existent codes). |
| 133 | k8s_security_policies_analysis.md | Best Practices Enumeration | — | DS | Yes — DS-58 | DS-58 not in master | NEEDS-REVIEW | "Numbered lists of security best practices (10 general + 10 RBAC-specific)." DS-58 does not exist in master. Closest matches: DT-02 (Specific Focus Areas with Examples) or ST-02 (Structured Sequential Instructions). Also appeared in Batch 7a (#32, #64) with same unverifiable code. |
| 134 | k8s_security_policies_analysis.md | Bundled Templates with Placeholders | — | IT | Yes — IT-23 | IT-23 not in master | NEEDS-REVIEW | "Ready-to-use YAML templates with placeholder variables." IT-23 does not exist in master (only IT-19, IT-35). Closest matches: IT-19 (Three-Tier Information Loading — templates as bundled resources) or DS-80 (Multi-Tiered Template Library). Note: AG-05 (Concrete Deliverable Templates) explicitly says "NOT placeholder templates" so it's a poor match. |

---

## Batch Summary

### Status Distribution

| Status | Count | Technique #s |
|--------|-------|-------------|
| CONFIRMED-EXISTING | 6 | #90, #95, #96, #100, #106, #125 |
| MATCHED-EXISTING | 5 | #92 → DS-22, #93 → DS-23, #104 → ST-22, #107 → QA-12, #115 → DS-24 |
| EXTENDS-EXISTING | 6 | #97 → DS-23, #102 → DS-22, #119 → QA-13, #127 → DS-80, #128 → DS-111, #130 → DS-61 |
| CONFIRMED-NOVEL | 19 | #84, #85, #86, #87, #88, #94, #101, #109, #114, #116, #117, #118, #120, #121, #122, #123, #126, #129, #131 |
| NEEDS-REVIEW | 15 | #89, #91, #98, #99, #103, #105, #108, #110, #111, #112, #113, #124, #132, #133, #134 |
| **TOTAL** | **51** | |

### NEEDS-REVIEW Detail

| # | Issue | Suggested Resolution |
|---|-------|---------------------|
| 89 | ST-04 exists but poor semantic match for "Example-Driven Workflow"; IT-06 not in master | Remap to ED-05 (Reference Class Priming) |
| 91 | DS-07 not found in master | Remap to ST-03 (Output Format Specification) |
| 98 | RT-07 exists but is "Cascade Effect Analysis", not "Concrete Example Extraction" | Remap to ED-05 (Reference Class Priming) or AG-05 (Concrete Deliverable Templates) |
| 99 | Neither IT-06 nor IT-15 exist in master | Remap to IT-19 (Three-Tier Information Loading) |
| 103 | OT-04 not in master; OT family doesn't exist | Remap to NE-04 (Good vs Bad Example Calibration) |
| 105 | DS-51 not in master; likely duplicate of #86 (Fallback Strategy Pattern) | Map to QA-13 or mark as duplicate of #86 |
| 108 | DS-60 not in master | No strong match found; may be genuinely novel or very niche |
| 110 | OT-01 not in master; DS-02 poor semantic match | Remap to AG-05 (Concrete Deliverable Templates) or DS-80 (Multi-Tiered Template Library) |
| 111 | DS-03 exists but weak semantic match | Consider DS-04 (Pattern Recognition) or RT-02 (Multi-Dimensional Analysis); may warrant novel status |
| 112 | Neither IT-14 nor AG-19 exist in master | Remap to AG-05 (Concrete Deliverable Templates) for the code artifact aspect |
| 113 | IT-01 not in master | Remap to IT-19 (Three-Tier Information Loading) |
| 124 | QA-02 exists but is "Adversarial Stress-Test", not "Bulk Operation Safety" | Remap to AG-04 (Behavioral Guardrails) or QA-09 (Reversibility Assessment) |
| 132 | DS-59 not in master | Remap to ST-02 (Structured Sequential Instructions) or DS-03 (Tool Suggestions) |
| 133 | DS-58 not in master | Remap to DT-02 (Specific Focus Areas with Examples) or ST-02 |
| 134 | IT-23 not in master | Remap to IT-19 (Three-Tier Information Loading) or DS-80 (Multi-Tiered Template Library) |

### Code Collisions Detected (with master)

| Code | Batch Assignment | Master Assignment | Resolution |
|------|-----------------|-------------------|------------|
| DS-50 | URL Pattern Templates (#84) | STRIDE-Per-Interaction Matrix | Batch technique needs new code |
| DS-21 | EARS Syntax Transformation (#92) | Proximity Assessment | Technique matches DS-22; remap to DS-22 |
| MP-06 | Four-Layer Enhancement Process (#94) | Fallback Question Protocol | Batch technique needs new code |
| DS-22 | Atomic Requirement Decomposition (#101) | EARS Requirements Transformation | Batch technique needs new code |

### Code Collisions Detected (intra-batch, across 7a and 7b)

| Code | Batch 7b Assignment | Batch 7a Assignment | Notes |
|------|---------------------|---------------------|-------|
| DS-50 | URL Pattern Templates (#84) | STRIDE-Per-Interaction Matrix (#45) | Both also collide with master DS-50 |
| DS-51 | Fallback Strategy Pattern (#86) | Control Effectiveness Scoring (#47) | Neither in master |
| DS-52 | Convention Documentation (#88) | Risk Score Matrix Calculation (#48) | Neither in master |

### Most-Referenced Master Techniques

| Master Code | Master Name | Times Referenced |
|-------------|-------------|-----------------|
| IT-19 | Three-Tier Information Loading | 4 (#90 direct, #99 suggested, #113 suggested, #134 suggested) |
| DS-22 | EARS Requirements Transformation | 3 (#92 matched, #101 collision, #102 extends) |
| DS-23 | Domain Theory Grounding | 2 (#93 matched, #97 extends) |
| QA-01 | Self-Verification | 2 (#96 confirmed, #106 confirmed) |
| ED-05 | Reference Class Priming | 2 (#89 suggested, #98 suggested) |
| AG-05 | Concrete Deliverable Templates | 3 (#98 suggested, #110 suggested, #112 suggested) |
| DS-61 | Security Tier Classification | 2 (#125 confirmed, #130 extends) |

### Novel Techniques by Family

| Family | Count | Technique #s |
|--------|-------|-------------|
| DS | 10 | #84, #86, #88, #101, #109, #116, #117, #118, #121, #122 |
| IT | 3 | #85, #87, #120 |
| ST | 1 | #114 |
| QA | 0 | (none confirmed novel in this batch) |
| MP | 1 | #94 |
| DS (K8s-specific) | 3 | #126, #129, #131 |
| IT (API-specific) | 1 | #123 |
| **Total Novel** | **19** | |

### Observations

1. **OT family orphans:** 4 techniques (#89 via IT-06, #103, #104, #110) reference an OT (Output Techniques) family that does not exist in the master index. All need remapping to existing families.

2. **IT family sparse in master:** Many batch techniques reference IT-xx codes (IT-06, IT-14, IT-23, IT-28, IT-29, IT-33, IT-34) but the master only has IT-19 and IT-35. Either the IT family needs expansion or these techniques need remapping to other families.

3. **DS-58 and DS-59 phantom codes:** Both are referenced in Files 9 and 11 as existing mappings but don't exist in the master. They also appear in Batch 7a with the same issue. These codes may have been defined in analysis files but never added to the master index.

4. **Cross-batch duplicate:** #105 (Fallback Strategy Chain) is likely a duplicate of #86 (Fallback Strategy Pattern) — same concept described from different analysis files.

5. **High novel rate in infrastructure files:** Files 10 (github_ops) and 11 (k8s_security_policies) have high novel technique rates because they cover specific infrastructure tooling patterns not represented in the conceptual/prompt-engineering-focused master index.
