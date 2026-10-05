# Security Skills

> Skills for threat modeling, security testing, attack analysis, supply chain security, and security requirement extraction.

## Skills in This Category

| Skill | Description |
|-------|-------------|
| [agentic-actions-auditor](agentic-actions-auditor/) | Audits GitHub Actions workflows for security vulnerabilities in AI agent integrations including Claude Code Action, Gemini CLI, OpenAI Codex, and GitHub AI Inference. |
| [attack-tree-construction](attack-tree-construction/) | Build comprehensive attack trees to visualize threat paths and identify defense gaps |
| [audit-augmentation](audit-augmentation/) | Augments Trailmark code graphs with external audit findings from SARIF static analysis results and weAudit annotation files. |
| [audit-context-building](audit-context-building/) | Enables ultra-granular, line-by-line code analysis to build deep architectural context before vulnerability or bug finding. |
| [burpsuite-project-parser](burpsuite-project-parser/) | Searches and explores Burp Suite project files (.burp) from the command line. |
| [codeql](codeql/) | Scans a codebase for security vulnerabilities using CodeQL's interprocedural data flow and taint tracking analysis. |
| [constant-time-analysis](constant-time-analysis/) | Detects timing side-channel vulnerabilities in cryptographic code. |
| [crypto-protocol-diagram](crypto-protocol-diagram/) | Extracts protocol message flow from source code, RFCs, academic papers, pseudocode, informal prose, ProVerif (.pv), or Tamarin (.spthy) models and generates Mermaid sequenceDiagrams with cryptographic annotations. |
| [diagramming-code](diagramming-code/) | Generates Mermaid diagrams from Trailmark code graphs. |
| [entry-point-analyzer](entry-point-analyzer/) | Analyzes smart contract codebases to identify state-changing entry points for security auditing. |
| [firebase-apk-scanner](firebase-apk-scanner/) | Scans Android APKs for Firebase security misconfigurations including open databases, storage buckets, authentication issues, and exposed cloud functions. |
| [gdpr-data-handling](gdpr-data-handling/) | Implement GDPR-compliant data handling with consent management, data subject rights, and privacy by design. |
| [genotoxic](genotoxic/) | Graph-informed mutation testing triage. Parses codebases with Trailmark, runs mutation testing and necessist, then uses survived mutants, unnecessary test statements, and call graph data to identify false positives,… |
| [graph-evolution](graph-evolution/) | Compares Trailmark code graphs at two source code snapshots (git commits, tags, or directories) to surface security-relevant structural changes. |
| [insecure-defaults](insecure-defaults/) | Detects fail-open insecure defaults (hardcoded secrets, weak auth, permissive security) that allow apps to run insecurely in production. |
| [mermaid-to-proverif](mermaid-to-proverif/) | Translates Mermaid sequenceDiagrams describing cryptographic protocols into ProVerif formal verification models (.pv files). |
| [sarif-parsing](sarif-parsing/) | Parses and processes SARIF files from static analysis tools like CodeQL, Semgrep, or other scanners. |
| [sast-configuration](sast-configuration/) | Configure Static Application Security Testing (SAST) tools for automated vulnerability detection |
| [seatbelt-sandboxer](seatbelt-sandboxer/) | Generates minimal macOS Seatbelt sandbox configurations. Use when sandboxing, isolating, or restricting macOS applications with allowlist-based profiles. |
| [security-requirement-extraction](security-requirement-extraction/) | Derive security requirements from threat models and business context for actionable specifications |
| [semgrep-rule-creator](semgrep-rule-creator/) | Creates custom Semgrep rules for detecting security vulnerabilities, bug patterns, and code patterns. Use when writing Semgrep rules or building custom static analysis detections. |
| [semgrep-rule-variant-creator](semgrep-rule-variant-creator/) | Creates language variants of existing Semgrep rules. |
| [semgrep](semgrep/) | Run Semgrep static analysis scan on a codebase using parallel subagents. |
| [sharp-edges](sharp-edges/) | Identifies error-prone APIs, dangerous configurations, and footgun designs that enable security mistakes. |
| [slsa-compliance](slsa-compliance/) | Expert guidance for SLSA framework compliance including SBOM generation, provenance attestation, and supply chain security |
| [spec-to-code-compliance](spec-to-code-compliance/) | Verifies code implements exactly what documentation specifies for blockchain audits. |
| [stride-analysis-patterns](stride-analysis-patterns/) | Apply STRIDE methodology to systematically identify threats in system security analysis |
| [supply-chain-risk-auditor](supply-chain-risk-auditor/) | Identifies dependencies at heightened risk of exploitation or takeover. Use when assessing supply chain attack surface, evaluating dependency health, or scoping security engagements. |
| [threat-mitigation-mapping](threat-mitigation-mapping/) | Map identified threats to appropriate security controls and mitigations for effective planning |
| [trailmark-structural](trailmark-structural/) | Runs full Trailmark structural analysis on Trailmark 0.2.x by building a graph, running `preanalysis()`, and reporting hotspots, taint, blast radius, privilege boundaries, and attack surface. |
| [trailmark-summary](trailmark-summary/) | Runs a Trailmark summary analysis on a codebase. |
| [trailmark](trailmark/) | Builds and queries multi-language source code graphs for security analysis. |
| [variant-analysis](variant-analysis/) | Find similar vulnerabilities and bugs across codebases using pattern-based analysis. |
| [vector-forge](vector-forge/) | Mutation-driven test vector generation. Finds implementations of a cryptographic algorithm or protocol, runs mutation testing to identify escaped mutants, then generates new test vectors that deliberately exercise… |
| [yara-rule-authoring](yara-rule-authoring/) | Guides authoring of high-quality YARA-X detection rules for malware identification. |
| [zeroize-audit](zeroize-audit/) | Detects missing zeroization of sensitive data in source code and identifies zeroization removed by compiler optimizations, with assembly-level analysis, and control-flow verification. |

## Usage

These skills provide specialized knowledge for Claude Code. They are automatically invoked when relevant to your task, or can be explicitly referenced.

## Related Resources

- [Skills Index](../README.md) - Complete skills catalog
- [Agents Index](../../agents/README.md) - Task-specific agents
