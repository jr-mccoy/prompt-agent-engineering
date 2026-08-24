#!/usr/bin/env python3
"""
SLSA Level Checker

Assesses the current SLSA compliance level of a project by analyzing:
- CI/CD configuration
- Build process characteristics
- Provenance generation
- SBOM availability
- Security controls

Usage:
    python slsa_level_checker.py [OPTIONS]

Options:
    --path PATH         Path to project (default: current directory)
    --output FORMAT     Output format: text, json, markdown (default: text)
    --verbose          Enable detailed output
    --help             Show this help message
"""

import argparse
import json
import os
import sys
from dataclasses import dataclass, field, asdict
from enum import Enum
from pathlib import Path
from typing import Optional


class SLSALevel(Enum):
    """SLSA compliance levels."""
    LEVEL_0 = 0
    LEVEL_1 = 1
    LEVEL_2 = 2
    LEVEL_3 = 3
    LEVEL_4 = 4  # Future


class CheckStatus(Enum):
    """Status of a compliance check."""
    PASS = "pass"
    FAIL = "fail"
    WARN = "warn"
    UNKNOWN = "unknown"


@dataclass
class Check:
    """Individual compliance check result."""
    id: str
    name: str
    description: str
    level: int
    status: CheckStatus
    details: str = ""
    remediation: str = ""


@dataclass
class ComplianceReport:
    """Complete SLSA compliance report."""
    project_path: str
    detected_level: SLSALevel
    checks: list = field(default_factory=list)
    ci_system: Optional[str] = None
    package_managers: list = field(default_factory=list)
    sbom_found: bool = False
    provenance_found: bool = False
    recommendations: list = field(default_factory=list)

    def to_dict(self):
        """Convert report to dictionary."""
        return {
            "project_path": self.project_path,
            "detected_level": self.detected_level.value,
            "detected_level_name": f"SLSA Level {self.detected_level.value}",
            "checks": [
                {
                    "id": c.id,
                    "name": c.name,
                    "description": c.description,
                    "level": c.level,
                    "status": c.status.value,
                    "details": c.details,
                    "remediation": c.remediation,
                }
                for c in self.checks
            ],
            "ci_system": self.ci_system,
            "package_managers": self.package_managers,
            "sbom_found": self.sbom_found,
            "provenance_found": self.provenance_found,
            "recommendations": self.recommendations,
            "summary": {
                "total_checks": len(self.checks),
                "passed": sum(1 for c in self.checks if c.status == CheckStatus.PASS),
                "failed": sum(1 for c in self.checks if c.status == CheckStatus.FAIL),
                "warnings": sum(1 for c in self.checks if c.status == CheckStatus.WARN),
            },
        }


class SLSAChecker:
    """Checks SLSA compliance for a project."""

    # CI/CD configuration files
    CI_CONFIGS = {
        ".github/workflows": "GitHub Actions",
        ".gitlab-ci.yml": "GitLab CI",
        "Jenkinsfile": "Jenkins",
        ".circleci/config.yml": "CircleCI",
        "azure-pipelines.yml": "Azure DevOps",
        ".travis.yml": "Travis CI",
        "bitbucket-pipelines.yml": "Bitbucket Pipelines",
        ".buildkite": "Buildkite",
    }

    # Package manager files
    PACKAGE_MANAGERS = {
        "package.json": "npm/Node.js",
        "package-lock.json": "npm (locked)",
        "yarn.lock": "Yarn",
        "pnpm-lock.yaml": "pnpm",
        "requirements.txt": "pip/Python",
        "Pipfile": "Pipenv",
        "Pipfile.lock": "Pipenv (locked)",
        "pyproject.toml": "Python (PEP 517)",
        "poetry.lock": "Poetry (locked)",
        "go.mod": "Go modules",
        "go.sum": "Go modules (locked)",
        "Cargo.toml": "Cargo/Rust",
        "Cargo.lock": "Cargo (locked)",
        "Gemfile": "Bundler/Ruby",
        "Gemfile.lock": "Bundler (locked)",
        "pom.xml": "Maven/Java",
        "build.gradle": "Gradle/Java",
        "build.gradle.kts": "Gradle Kotlin",
        "composer.json": "Composer/PHP",
        "composer.lock": "Composer (locked)",
    }

    # SBOM file patterns
    SBOM_PATTERNS = [
        "sbom.json",
        "sbom.spdx",
        "sbom.spdx.json",
        "sbom.cdx.json",
        "bom.json",
        "bom.xml",
        "*.sbom.json",
        "*.spdx.json",
        "*.cdx.json",
    ]

    # Provenance file patterns
    PROVENANCE_PATTERNS = [
        "*.intoto.jsonl",
        "*.sigstore",
        "provenance.json",
        ".attestations",
        "*.att",
    ]

    def __init__(self, project_path: str, verbose: bool = False):
        """Initialize checker with project path."""
        self.project_path = Path(project_path).resolve()
        self.verbose = verbose
        self.checks: list[Check] = []

    def log(self, message: str):
        """Print verbose log message."""
        if self.verbose:
            print(f"[DEBUG] {message}")

    def check_file_exists(self, *paths: str) -> bool:
        """Check if any of the given paths exist."""
        for path in paths:
            full_path = self.project_path / path
            if full_path.exists():
                self.log(f"Found: {path}")
                return True
        return False

    def check_dir_exists(self, path: str) -> bool:
        """Check if directory exists."""
        full_path = self.project_path / path
        return full_path.is_dir()

    def find_files_matching(self, pattern: str) -> list[Path]:
        """Find files matching a glob pattern."""
        return list(self.project_path.rglob(pattern))

    def read_file_content(self, path: str, max_size: int = 1_000_000) -> Optional[str]:
        """Read file content if it exists and isn't too large."""
        full_path = self.project_path / path
        if not full_path.exists():
            return None
        if full_path.stat().st_size > max_size:
            self.log(f"File too large to read: {path}")
            return None
        try:
            return full_path.read_text()
        except Exception as e:
            self.log(f"Error reading {path}: {e}")
            return None

    def detect_ci_system(self) -> Optional[str]:
        """Detect which CI/CD system is configured."""
        for path, name in self.CI_CONFIGS.items():
            if self.check_file_exists(path) or self.check_dir_exists(path):
                self.log(f"Detected CI system: {name}")
                return name
        return None

    def detect_package_managers(self) -> list[str]:
        """Detect which package managers are in use."""
        managers = []
        for path, name in self.PACKAGE_MANAGERS.items():
            if self.check_file_exists(path):
                managers.append(name)
        return list(set(managers))  # Deduplicate

    def check_sbom_exists(self) -> tuple[bool, list[Path]]:
        """Check if SBOM files exist."""
        found = []
        for pattern in self.SBOM_PATTERNS:
            found.extend(self.find_files_matching(pattern))
        return len(found) > 0, found

    def check_provenance_exists(self) -> tuple[bool, list[Path]]:
        """Check if provenance files exist."""
        found = []
        for pattern in self.PROVENANCE_PATTERNS:
            found.extend(self.find_files_matching(pattern))
        return len(found) > 0, found

    def check_github_actions_slsa(self) -> dict:
        """Check GitHub Actions for SLSA-related configurations."""
        results = {
            "slsa_generator": False,
            "sigstore_cosign": False,
            "sbom_action": False,
            "provenance_action": False,
            "id_token_permission": False,
        }

        workflows_dir = self.project_path / ".github" / "workflows"
        if not workflows_dir.exists():
            return results

        for workflow_file in workflows_dir.glob("*.yml"):
            content = workflow_file.read_text()

            # Check for SLSA generator
            if "slsa-framework/slsa-github-generator" in content:
                results["slsa_generator"] = True

            # Check for Sigstore/Cosign
            if "sigstore/cosign" in content or "cosign-installer" in content:
                results["sigstore_cosign"] = True

            # Check for SBOM action
            if "sbom-action" in content or "anchore/sbom-action" in content:
                results["sbom_action"] = True

            # Check for provenance action
            if "attest-build-provenance" in content:
                results["provenance_action"] = True

            # Check for id-token permission
            if "id-token: write" in content:
                results["id_token_permission"] = True

        return results

    def check_version_control(self) -> bool:
        """Check if project uses version control."""
        return self.check_dir_exists(".git")

    def check_lockfile_exists(self) -> bool:
        """Check if dependency lockfiles exist."""
        lockfiles = [
            "package-lock.json",
            "yarn.lock",
            "pnpm-lock.yaml",
            "Pipfile.lock",
            "poetry.lock",
            "go.sum",
            "Cargo.lock",
            "Gemfile.lock",
            "composer.lock",
        ]
        return any(self.check_file_exists(lf) for lf in lockfiles)

    def check_protected_branches(self) -> Optional[bool]:
        """Check for branch protection indicators (limited without API)."""
        # Check for CODEOWNERS file
        codeowners = self.check_file_exists(
            "CODEOWNERS", ".github/CODEOWNERS", "docs/CODEOWNERS"
        )
        return codeowners  # Returns indicator, not definitive

    def run_level_1_checks(self):
        """Run SLSA Level 1 checks."""
        # L1.1: Build process documented
        doc_exists = self.check_file_exists(
            "README.md",
            "BUILDING.md",
            "BUILD.md",
            "docs/building.md",
            "CONTRIBUTING.md",
        )
        self.checks.append(
            Check(
                id="L1.1",
                name="Build Documentation",
                description="Build process is documented",
                level=1,
                status=CheckStatus.PASS if doc_exists else CheckStatus.WARN,
                details="Documentation file found" if doc_exists else "No build documentation found",
                remediation="Add README.md or BUILDING.md with build instructions",
            )
        )

        # L1.2: Provenance exists (any form)
        prov_exists, prov_files = self.check_provenance_exists()
        sbom_exists, sbom_files = self.check_sbom_exists()

        self.checks.append(
            Check(
                id="L1.2",
                name="Provenance Generation",
                description="Provenance is generated for artifacts",
                level=1,
                status=CheckStatus.PASS if prov_exists else CheckStatus.FAIL,
                details=f"Found: {[str(f.name) for f in prov_files]}" if prov_exists else "No provenance files found",
                remediation="Configure CI/CD to generate provenance using SLSA GitHub Generator or similar",
            )
        )

        # L1.3: Builder identity in provenance
        self.checks.append(
            Check(
                id="L1.3",
                name="Builder Identity",
                description="Provenance contains builder identity",
                level=1,
                status=CheckStatus.UNKNOWN if not prov_exists else CheckStatus.PASS,
                details="Cannot verify without provenance" if not prov_exists else "Builder identity expected in provenance",
                remediation="Ensure provenance includes builder.id field",
            )
        )

        # L1.4: Build instructions in provenance
        self.checks.append(
            Check(
                id="L1.4",
                name="Build Instructions",
                description="Provenance contains build instructions",
                level=1,
                status=CheckStatus.UNKNOWN if not prov_exists else CheckStatus.PASS,
                details="Cannot verify without provenance" if not prov_exists else "Build instructions expected in provenance",
                remediation="Ensure provenance includes invocation and configuration fields",
            )
        )

    def run_level_2_checks(self):
        """Run SLSA Level 2 checks."""
        # L2.1: Version control
        vcs_exists = self.check_version_control()
        self.checks.append(
            Check(
                id="L2.1",
                name="Version Control",
                description="Source code is under version control",
                level=2,
                status=CheckStatus.PASS if vcs_exists else CheckStatus.FAIL,
                details="Git repository detected" if vcs_exists else "No version control detected",
                remediation="Initialize Git repository: git init",
            )
        )

        # L2.2: Hosted build service
        ci_system = self.detect_ci_system()
        self.checks.append(
            Check(
                id="L2.2",
                name="Hosted Build Service",
                description="Builds run on hosted CI/CD service (not local)",
                level=2,
                status=CheckStatus.PASS if ci_system else CheckStatus.FAIL,
                details=f"CI system: {ci_system}" if ci_system else "No CI/CD configuration found",
                remediation="Configure GitHub Actions, GitLab CI, or another hosted CI service",
            )
        )

        # L2.3: Authenticated provenance
        gh_checks = self.check_github_actions_slsa()
        auth_prov = gh_checks.get("slsa_generator") or gh_checks.get("sigstore_cosign")

        self.checks.append(
            Check(
                id="L2.3",
                name="Authenticated Provenance",
                description="Provenance is signed/authenticated",
                level=2,
                status=CheckStatus.PASS if auth_prov else CheckStatus.FAIL,
                details="SLSA generator or Sigstore signing configured" if auth_prov else "No authenticated provenance configuration found",
                remediation="Use slsa-framework/slsa-github-generator or sigstore/cosign for signing",
            )
        )

    def run_level_3_checks(self):
        """Run SLSA Level 3 checks."""
        gh_checks = self.check_github_actions_slsa()

        # L3.1: Non-falsifiable provenance
        uses_slsa_gen = gh_checks.get("slsa_generator", False)
        self.checks.append(
            Check(
                id="L3.1",
                name="Non-falsifiable Provenance",
                description="Provenance cannot be modified by build job",
                level=3,
                status=CheckStatus.PASS if uses_slsa_gen else CheckStatus.FAIL,
                details="SLSA GitHub Generator provides isolated provenance" if uses_slsa_gen else "Standard provenance can be tampered with",
                remediation="Use slsa-framework/slsa-github-generator reusable workflow",
            )
        )

        # L3.2: id-token permission (for keyless signing)
        id_token = gh_checks.get("id_token_permission", False)
        self.checks.append(
            Check(
                id="L3.2",
                name="OIDC Identity",
                description="Build uses OIDC identity for signing",
                level=3,
                status=CheckStatus.PASS if id_token else CheckStatus.WARN,
                details="id-token: write permission configured" if id_token else "OIDC identity not configured",
                remediation="Add 'permissions: id-token: write' to workflow",
            )
        )

        # L3.3: Isolated build environment indicator
        self.checks.append(
            Check(
                id="L3.3",
                name="Isolated Build Environment",
                description="Build runs in ephemeral, isolated environment",
                level=3,
                status=CheckStatus.UNKNOWN,
                details="Cannot verify build isolation from static analysis",
                remediation="Use GitHub-hosted runners or verified self-hosted runners with ephemeral VMs",
            )
        )

        # L3.4: Hermetic builds indicator
        self.checks.append(
            Check(
                id="L3.4",
                name="Hermetic Builds",
                description="Build has no network access during execution",
                level=3,
                status=CheckStatus.UNKNOWN,
                details="Cannot verify network isolation from static analysis",
                remediation="Configure build to use pre-fetched dependencies and disable network",
            )
        )

    def run_additional_checks(self):
        """Run additional best-practice checks."""
        # SBOM generation
        sbom_exists, sbom_files = self.check_sbom_exists()
        gh_checks = self.check_github_actions_slsa()

        self.checks.append(
            Check(
                id="BP.1",
                name="SBOM Generation",
                description="Software Bill of Materials is generated",
                level=0,
                status=CheckStatus.PASS if (sbom_exists or gh_checks.get("sbom_action")) else CheckStatus.WARN,
                details=f"SBOM files: {[f.name for f in sbom_files]}" if sbom_exists else "No SBOM found",
                remediation="Add SBOM generation using Syft, cdxgen, or anchore/sbom-action",
            )
        )

        # Dependency lockfiles
        lockfile = self.check_lockfile_exists()
        self.checks.append(
            Check(
                id="BP.2",
                name="Dependency Pinning",
                description="Dependencies are pinned with lockfiles",
                level=0,
                status=CheckStatus.PASS if lockfile else CheckStatus.WARN,
                details="Lockfile found" if lockfile else "No lockfile found",
                remediation="Generate and commit lockfiles (package-lock.json, go.sum, etc.)",
            )
        )

        # CODEOWNERS for review
        codeowners = self.check_protected_branches()
        self.checks.append(
            Check(
                id="BP.3",
                name="Code Review Configuration",
                description="CODEOWNERS configured for mandatory review",
                level=0,
                status=CheckStatus.PASS if codeowners else CheckStatus.WARN,
                details="CODEOWNERS file found" if codeowners else "No CODEOWNERS file",
                remediation="Add CODEOWNERS file to enforce code review for critical paths",
            )
        )

    def determine_level(self) -> SLSALevel:
        """Determine the achieved SLSA level based on checks."""
        def level_checks_pass(level: int) -> bool:
            level_checks = [c for c in self.checks if c.level == level]
            # All required checks must pass (not FAIL)
            return all(c.status != CheckStatus.FAIL for c in level_checks)

        if level_checks_pass(3) and level_checks_pass(2) and level_checks_pass(1):
            return SLSALevel.LEVEL_3
        if level_checks_pass(2) and level_checks_pass(1):
            return SLSALevel.LEVEL_2
        if level_checks_pass(1):
            return SLSALevel.LEVEL_1
        return SLSALevel.LEVEL_0

    def generate_recommendations(self) -> list[str]:
        """Generate prioritized recommendations."""
        recommendations = []
        failed_checks = [c for c in self.checks if c.status == CheckStatus.FAIL]

        # Sort by level (lower levels first)
        failed_checks.sort(key=lambda c: c.level)

        for check in failed_checks[:5]:  # Top 5 recommendations
            recommendations.append(f"[{check.id}] {check.name}: {check.remediation}")

        return recommendations

    def run(self) -> ComplianceReport:
        """Run all SLSA compliance checks."""
        self.log(f"Checking project: {self.project_path}")

        # Run all checks
        self.run_level_1_checks()
        self.run_level_2_checks()
        self.run_level_3_checks()
        self.run_additional_checks()

        # Determine level and generate report
        ci_system = self.detect_ci_system()
        pkg_managers = self.detect_package_managers()
        sbom_exists, _ = self.check_sbom_exists()
        prov_exists, _ = self.check_provenance_exists()
        level = self.determine_level()
        recommendations = self.generate_recommendations()

        return ComplianceReport(
            project_path=str(self.project_path),
            detected_level=level,
            checks=self.checks,
            ci_system=ci_system,
            package_managers=pkg_managers,
            sbom_found=sbom_exists,
            provenance_found=prov_exists,
            recommendations=recommendations,
        )


def format_text(report: ComplianceReport) -> str:
    """Format report as text."""
    lines = [
        "=" * 60,
        "SLSA COMPLIANCE REPORT",
        "=" * 60,
        "",
        f"Project: {report.project_path}",
        f"CI System: {report.ci_system or 'Not detected'}",
        f"Package Managers: {', '.join(report.package_managers) or 'None detected'}",
        "",
        "-" * 60,
        f"DETECTED LEVEL: SLSA Level {report.detected_level.value}",
        "-" * 60,
        "",
        "CHECK RESULTS:",
        "",
    ]

    # Group checks by level
    for level in range(1, 4):
        level_checks = [c for c in report.checks if c.level == level]
        if level_checks:
            lines.append(f"Level {level} Requirements:")
            for check in level_checks:
                status_icon = {
                    CheckStatus.PASS: "[PASS]",
                    CheckStatus.FAIL: "[FAIL]",
                    CheckStatus.WARN: "[WARN]",
                    CheckStatus.UNKNOWN: "[????]",
                }[check.status]
                lines.append(f"  {status_icon} {check.id}: {check.name}")
                lines.append(f"           {check.details}")
            lines.append("")

    # Best practices
    bp_checks = [c for c in report.checks if c.level == 0]
    if bp_checks:
        lines.append("Best Practices:")
        for check in bp_checks:
            status_icon = "[PASS]" if check.status == CheckStatus.PASS else "[WARN]"
            lines.append(f"  {status_icon} {check.id}: {check.name}")
        lines.append("")

    # Recommendations
    if report.recommendations:
        lines.append("-" * 60)
        lines.append("RECOMMENDATIONS (prioritized):")
        lines.append("")
        for i, rec in enumerate(report.recommendations, 1):
            lines.append(f"  {i}. {rec}")
        lines.append("")

    # Summary
    summary = report.to_dict()["summary"]
    lines.extend([
        "-" * 60,
        "SUMMARY:",
        f"  Total Checks: {summary['total_checks']}",
        f"  Passed: {summary['passed']}",
        f"  Failed: {summary['failed']}",
        f"  Warnings: {summary['warnings']}",
        "=" * 60,
    ])

    return "\n".join(lines)


def format_markdown(report: ComplianceReport) -> str:
    """Format report as Markdown."""
    lines = [
        "# SLSA Compliance Report",
        "",
        "## Overview",
        "",
        f"- **Project:** `{report.project_path}`",
        f"- **Detected Level:** SLSA Level {report.detected_level.value}",
        f"- **CI System:** {report.ci_system or 'Not detected'}",
        f"- **Package Managers:** {', '.join(report.package_managers) or 'None detected'}",
        "",
        "## Check Results",
        "",
    ]

    # Table header
    lines.extend([
        "| Level | ID | Check | Status | Details |",
        "|-------|-----|-------|--------|---------|",
    ])

    for check in sorted(report.checks, key=lambda c: (c.level, c.id)):
        status_emoji = {
            CheckStatus.PASS: "PASS",
            CheckStatus.FAIL: "FAIL",
            CheckStatus.WARN: "WARN",
            CheckStatus.UNKNOWN: "?",
        }[check.status]
        level_str = f"L{check.level}" if check.level > 0 else "BP"
        lines.append(f"| {level_str} | {check.id} | {check.name} | {status_emoji} | {check.details} |")

    lines.append("")

    # Recommendations
    if report.recommendations:
        lines.extend([
            "## Recommendations",
            "",
        ])
        for i, rec in enumerate(report.recommendations, 1):
            lines.append(f"{i}. {rec}")
        lines.append("")

    return "\n".join(lines)


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="Check SLSA compliance level for a project"
    )
    parser.add_argument(
        "--path",
        default=".",
        help="Path to project directory (default: current directory)",
    )
    parser.add_argument(
        "--output",
        choices=["text", "json", "markdown"],
        default="text",
        help="Output format (default: text)",
    )
    parser.add_argument(
        "--verbose", "-v",
        action="store_true",
        help="Enable verbose output",
    )

    args = parser.parse_args()

    # Run checker
    checker = SLSAChecker(args.path, verbose=args.verbose)
    report = checker.run()

    # Output
    if args.output == "json":
        print(json.dumps(report.to_dict(), indent=2))
    elif args.output == "markdown":
        print(format_markdown(report))
    else:
        print(format_text(report))

    # Exit code based on level
    sys.exit(0 if report.detected_level.value >= 1 else 1)


if __name__ == "__main__":
    main()
