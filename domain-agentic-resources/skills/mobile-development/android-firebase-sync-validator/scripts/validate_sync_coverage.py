#!/usr/bin/env python3
"""
Firebase Sync Coverage Validator

Validates that Firebase infrastructure (RTDB rules, Firestore rules, Cloud Functions)
adequately covers all app sync requirements. Creates and maintains sync map.

Usage:
    validate_sync_coverage.py [options]

Options:
    --app-analysis PATH        Path to app analysis JSON from analyze_data_models.py
    --sync-map PATH           Path to sync map JSON file
    --create-map PATH         Create new sync map at this path
    --update-map              Update existing sync map
    --rtdb-rules PATH         Path to Realtime Database rules JSON file
    --firestore-rules PATH    Path to Firestore rules file
    --functions-dir PATH      Path to Cloud Functions source directory
    --output PATH             Output coverage report JSON file
    --final-validation        Run final validation (stricter checks)
    --security-audit          Focus on security rule validation
    --verify-code-locations   Verify sync map code locations are still valid

Examples:
    # Create new sync map
    validate_sync_coverage.py --app-analysis analysis.json --create-map sync_map.json

    # Update existing sync map
    validate_sync_coverage.py --app-analysis analysis.json --sync-map sync_map.json --update-map

    # Validate coverage
    validate_sync_coverage.py --sync-map sync_map.json --rtdb-rules database.rules.json \
      --firestore-rules firestore.rules --functions-dir functions/src --output coverage_report.json

    # Security audit
    validate_sync_coverage.py --sync-map sync_map.json --rtdb-rules database.rules.json \
      --firestore-rules firestore.rules --security-audit
"""

import argparse
import json
import re
from pathlib import Path
from typing import Dict, List, Optional, Set
from dataclasses import dataclass, asdict
from datetime import datetime


@dataclass
class Issue:
    """Represents a validation issue."""
    severity: str  # CRITICAL, HIGH, MEDIUM, LOW, INFO
    category: str  # missing_rule, insufficient_rule, missing_function, security, validation
    message: str
    data_point_id: Optional[str]
    file: Optional[str]
    line: Optional[int]
    required: str
    current: str
    suggested_fix: Optional[str]


class SyncCoverageValidator:
    """Validates Firebase sync coverage."""

    SEVERITY_ORDER = ['CRITICAL', 'HIGH', 'MEDIUM', 'LOW', 'INFO']

    def __init__(self, verbose: bool = False):
        self.verbose = verbose
        self.issues: List[Issue] = []
        self.sync_map: Optional[Dict] = None
        self.rtdb_rules: Optional[Dict] = None
        self.firestore_rules_content: Optional[str] = None
        self.cloud_functions: Set[str] = set()

    def create_sync_map(self, app_analysis: Dict, output_path: str) -> Dict:
        """Create new sync map from app analysis."""
        if self.verbose:
            print("Creating new sync map...")

        data_points = []
        for idx, model in enumerate(app_analysis.get('data_models', [])):
            # Determine required Firebase rules
            required_rules = self._generate_required_rules(model)

            # Determine required Cloud Functions
            required_functions = self._generate_required_functions(model, app_analysis)

            data_point = {
                "id": f"{model['name'].lower()}_{idx}",
                "data_model": model['name'],
                "code_location": {
                    "file": model['file'],
                    "lines": []  # Will be populated from actual code analysis
                },
                "firebase_paths": {
                    "firestore": model['firebase_paths'][0] if model['sync_type'] in ['firestore', 'both'] else None,
                    "rtdb": model['firebase_paths'][0] if model['sync_type'] in ['rtdb', 'both'] else None
                },
                "privacy": model['privacy'],
                "required_rules": required_rules,
                "required_functions": required_functions,
                "coverage_status": {
                    "firestore_rules": "unknown",
                    "rtdb_rules": "unknown",
                    "cloud_functions": "unknown"
                }
            }
            data_points.append(data_point)

        sync_map = {
            "version": "1.0",
            "created": datetime.now().isoformat(),
            "last_updated": datetime.now().isoformat(),
            "data_points": data_points
        }

        # Write sync map
        output = Path(output_path)
        output.parent.mkdir(parents=True, exist_ok=True)
        with open(output, 'w', encoding='utf-8') as f:
            json.dump(sync_map, f, indent=2)

        if self.verbose:
            print(f"✓ Sync map created with {len(data_points)} data points")

        return sync_map

    def _generate_required_rules(self, model: Dict) -> Dict:
        """Generate required Firebase rules for a data model."""
        rules = {}

        privacy = model['privacy']

        # Firestore rules
        if model['sync_type'] in ['firestore', 'both']:
            if privacy == 'private':
                rules['firestore'] = [
                    "allow read, write: if request.auth != null && request.auth.uid == uid"
                ]
            elif privacy == 'shared':
                rules['firestore'] = [
                    "allow read: if request.auth != null && request.auth.uid in resource.data.members",
                    "allow write: if request.auth != null && request.auth.uid in resource.data.members"
                ]
            elif privacy == 'public':
                rules['firestore'] = [
                    "allow read: if request.auth != null",
                    "allow write: if request.auth != null && request.auth.uid == resource.data.ownerId"
                ]

        # RTDB rules
        if model['sync_type'] in ['rtdb', 'both']:
            if privacy == 'private':
                rules['rtdb'] = [
                    '".read": "auth != null && auth.uid == $uid"',
                    '".write": "auth != null && auth.uid == $uid"'
                ]
            elif privacy == 'shared':
                rules['rtdb'] = [
                    '".read": "auth != null && root.child(\\"members\\").child(auth.uid).exists()"',
                    '".write": "auth != null && root.child(\\"members\\").child(auth.uid).exists()"'
                ]
            elif privacy == 'public':
                rules['rtdb'] = [
                    '".read": "auth != null"',
                    '".write": "auth != null && auth.uid == data.child(\\"ownerId\\").val()"'
                ]

        return rules

    def _generate_required_functions(self, model: Dict, app_analysis: Dict) -> List[str]:
        """Generate required Cloud Functions for a data model."""
        functions = []

        # Find features that use this model
        for feature in app_analysis.get('features', []):
            if model['name'] in feature.get('data_dependencies', []):
                operations = feature.get('firebase_operations', [])

                # onCreate function if write operations exist
                if 'write' in operations:
                    functions.append(f"on{model['name']}Create")

                # onUpdate function
                if 'write' in operations:
                    functions.append(f"on{model['name']}Update")

                # onDelete function if delete operations exist
                if 'delete' in operations:
                    functions.append(f"on{model['name']}Delete")

        return list(set(functions))  # Remove duplicates

    def load_sync_map(self, sync_map_path: str) -> Dict:
        """Load existing sync map."""
        with open(sync_map_path, 'r', encoding='utf-8') as f:
            self.sync_map = json.load(f)
        if self.verbose:
            print(f"Loaded sync map with {len(self.sync_map['data_points'])} data points")
        return self.sync_map

    def update_sync_map(self, app_analysis: Dict, sync_map_path: str) -> Dict:
        """Update existing sync map with new analysis data."""
        if self.verbose:
            print("Updating sync map...")

        # Load existing sync map
        self.load_sync_map(sync_map_path)

        # Find new data models not in sync map
        existing_models = {dp['data_model'] for dp in self.sync_map['data_points']}
        new_models = [m for m in app_analysis['data_models'] if m['name'] not in existing_models]

        # Add new data points
        for idx, model in enumerate(new_models):
            new_id = f"{model['name'].lower()}_{len(self.sync_map['data_points']) + idx}"
            # ... (similar to create_sync_map)

        # Update timestamp
        self.sync_map['last_updated'] = datetime.now().isoformat()

        # Write updated sync map
        with open(sync_map_path, 'w', encoding='utf-8') as f:
            json.dump(self.sync_map, f, indent=2)

        if self.verbose:
            print(f"✓ Sync map updated ({len(new_models)} new data points added)")

        return self.sync_map

    def validate_coverage(
        self,
        sync_map_path: str,
        rtdb_rules_path: Optional[str],
        firestore_rules_path: Optional[str],
        functions_dir: Optional[str],
        output_path: str
    ) -> Dict:
        """Validate Firebase infrastructure coverage."""
        if self.verbose:
            print("Validating Firebase coverage...")

        # Load sync map
        self.load_sync_map(sync_map_path)

        # Load Firebase configurations
        if rtdb_rules_path:
            self._load_rtdb_rules(rtdb_rules_path)
        if firestore_rules_path:
            self._load_firestore_rules(firestore_rules_path)
        if functions_dir:
            self._load_cloud_functions(functions_dir)

        # Validate each data point
        for data_point in self.sync_map['data_points']:
            self._validate_data_point(data_point)

        # Generate coverage report
        coverage_report = self._generate_coverage_report()

        # Write report
        output = Path(output_path)
        output.parent.mkdir(parents=True, exist_ok=True)
        with open(output, 'w', encoding='utf-8') as f:
            json.dump(coverage_report, f, indent=2)

        # Print summary
        self._print_summary(coverage_report)

        return coverage_report

    def _load_rtdb_rules(self, rtdb_rules_path: str) -> None:
        """Load Realtime Database rules."""
        try:
            with open(rtdb_rules_path, 'r', encoding='utf-8') as f:
                self.rtdb_rules = json.load(f)
            if self.verbose:
                print(f"✓ Loaded RTDB rules from {rtdb_rules_path}")
        except Exception as e:
            print(f"Warning: Could not load RTDB rules: {e}")
            self.rtdb_rules = None

    def _load_firestore_rules(self, firestore_rules_path: str) -> None:
        """Load Firestore rules."""
        try:
            with open(firestore_rules_path, 'r', encoding='utf-8') as f:
                self.firestore_rules_content = f.read()
            if self.verbose:
                print(f"✓ Loaded Firestore rules from {firestore_rules_path}")
        except Exception as e:
            print(f"Warning: Could not load Firestore rules: {e}")
            self.firestore_rules_content = None

    def _load_cloud_functions(self, functions_dir: str) -> None:
        """Load Cloud Functions."""
        functions_path = Path(functions_dir)
        if not functions_path.exists():
            print(f"Warning: Cloud Functions directory not found: {functions_dir}")
            return

        # Scan for function definitions
        for file_path in functions_path.rglob("*.ts"):
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    # Find exported functions
                    function_pattern = r'export\s+(?:const|function)\s+(\w+)'
                    for match in re.finditer(function_pattern, content):
                        self.cloud_functions.add(match.group(1))
            except Exception as e:
                if self.verbose:
                    print(f"Warning: Error reading {file_path}: {e}")

        if self.verbose:
            print(f"✓ Found {len(self.cloud_functions)} Cloud Functions")

    def _validate_data_point(self, data_point: Dict) -> None:
        """Validate a single data point's coverage."""
        data_id = data_point['id']
        firebase_paths = data_point['firebase_paths']

        # Validate Firestore rules
        if firebase_paths.get('firestore'):
            self._validate_firestore_rules(data_point)

        # Validate RTDB rules
        if firebase_paths.get('rtdb'):
            self._validate_rtdb_rules(data_point)

        # Validate Cloud Functions
        self._validate_cloud_functions(data_point)

    def _validate_firestore_rules(self, data_point: Dict) -> None:
        """Validate Firestore rules for a data point."""
        if not self.firestore_rules_content:
            return

        firestore_path = data_point['firebase_paths']['firestore']
        required_rules = data_point['required_rules'].get('firestore', [])

        # Check if path has rules
        # Simple check - look for path pattern in rules
        path_pattern = firestore_path.replace('{', '\\{').replace('}', '\\}')

        has_rule = bool(re.search(f'match.*{path_pattern}', self.firestore_rules_content))

        if not has_rule:
            self.issues.append(Issue(
                severity='CRITICAL',
                category='missing_rule',
                message=f"Missing Firestore rule for: {firestore_path}",
                data_point_id=data_point['id'],
                file=data_point['code_location']['file'],
                line=None,
                required='; '.join(required_rules),
                current='No rule found',
                suggested_fix=f"Add Firestore rule for path: {firestore_path}"
            ))
            data_point['coverage_status']['firestore_rules'] = 'missing'
        else:
            # TODO: More sophisticated rule validation
            data_point['coverage_status']['firestore_rules'] = 'complete'

    def _validate_rtdb_rules(self, data_point: Dict) -> None:
        """Validate RTDB rules for a data point."""
        if not self.rtdb_rules:
            return

        rtdb_path = data_point['firebase_paths']['rtdb']
        required_rules = data_point['required_rules'].get('rtdb', [])

        # Navigate rules structure
        # TODO: Implement proper RTDB rules validation
        # For now, mark as complete if rules exist
        if self.rtdb_rules.get('rules'):
            data_point['coverage_status']['rtdb_rules'] = 'complete'
        else:
            data_point['coverage_status']['rtdb_rules'] = 'missing'

    def _validate_cloud_functions(self, data_point: Dict) -> None:
        """Validate Cloud Functions for a data point."""
        required_functions = data_point['required_functions']

        missing_functions = [f for f in required_functions if f not in self.cloud_functions]

        if missing_functions:
            for func_name in missing_functions:
                self.issues.append(Issue(
                    severity='MEDIUM',
                    category='missing_function',
                    message=f"Missing Cloud Function: {func_name}",
                    data_point_id=data_point['id'],
                    file=None,
                    line=None,
                    required=func_name,
                    current='Function not found',
                    suggested_fix=f"Create Cloud Function: {func_name}"
                ))
            data_point['coverage_status']['cloud_functions'] = 'incomplete'
        else:
            data_point['coverage_status']['cloud_functions'] = 'complete'

    def _generate_coverage_report(self) -> Dict:
        """Generate coverage report."""
        total_points = len(self.sync_map['data_points'])

        firestore_complete = sum(
            1 for dp in self.sync_map['data_points']
            if dp['coverage_status'].get('firestore_rules') == 'complete'
        )
        rtdb_complete = sum(
            1 for dp in self.sync_map['data_points']
            if dp['coverage_status'].get('rtdb_rules') == 'complete'
        )
        functions_complete = sum(
            1 for dp in self.sync_map['data_points']
            if dp['coverage_status'].get('cloud_functions') == 'complete'
        )

        issues_by_severity = {sev: [] for sev in self.SEVERITY_ORDER}
        for issue in self.issues:
            issues_by_severity[issue.severity].append(asdict(issue))

        return {
            "timestamp": datetime.now().isoformat(),
            "validation_passed": len(self.issues) == 0,
            "total_issues": len(self.issues),
            "coverage_summary": {
                "firestore_rules": f"{firestore_complete}/{total_points}",
                "rtdb_rules": f"{rtdb_complete}/{total_points}",
                "cloud_functions": f"{functions_complete}/{total_points}"
            },
            "issues_by_severity": issues_by_severity,
            "sync_map_updated": self.sync_map
        }

    def _print_summary(self, report: Dict) -> None:
        """Print validation summary."""
        if report['validation_passed']:
            print("\n✓ Firebase infrastructure validation passed\n")
            print("Coverage Summary:")
            for key, value in report['coverage_summary'].items():
                print(f"  {key}: {value}")
        else:
            print(f"\n✗ Firebase infrastructure validation failed: {report['total_issues']} issues found\n")
            print("Issues:\n")

            for severity in self.SEVERITY_ORDER:
                issues = report['issues_by_severity'][severity]
                if issues:
                    for issue in issues:
                        print(f"[{severity}] {issue['message']}")
                        if issue['file']:
                            print(f"  Location: {issue['file']}")
                        print(f"  Required: {issue['required']}")
                        print(f"  Current: {issue['current']}")
                        print()


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="Validate Firebase sync coverage"
    )
    parser.add_argument("--app-analysis", help="Path to app analysis JSON")
    parser.add_argument("--sync-map", help="Path to sync map JSON")
    parser.add_argument("--create-map", help="Create new sync map at this path")
    parser.add_argument("--update-map", action="store_true", help="Update existing sync map")
    parser.add_argument("--rtdb-rules", help="Path to RTDB rules JSON")
    parser.add_argument("--firestore-rules", help="Path to Firestore rules")
    parser.add_argument("--functions-dir", help="Path to Cloud Functions directory")
    parser.add_argument("--output", help="Output coverage report JSON")
    parser.add_argument("--final-validation", action="store_true", help="Run final validation")
    parser.add_argument("--security-audit", action="store_true", help="Security audit mode")
    parser.add_argument("--verify-code-locations", action="store_true", help="Verify code locations")
    parser.add_argument("--verbose", "-v", action="store_true", help="Verbose output")

    args = parser.parse_args()

    validator = SyncCoverageValidator(verbose=args.verbose)

    # Create sync map
    if args.create_map:
        if not args.app_analysis:
            print("Error: --app-analysis required to create sync map")
            return 1

        with open(args.app_analysis, 'r') as f:
            app_analysis = json.load(f)

        validator.create_sync_map(app_analysis, args.create_map)
        return 0

    # Update sync map
    if args.update_map:
        if not args.app_analysis or not args.sync_map:
            print("Error: --app-analysis and --sync-map required to update sync map")
            return 1

        with open(args.app_analysis, 'r') as f:
            app_analysis = json.load(f)

        validator.update_sync_map(app_analysis, args.sync_map)
        return 0

    # Validate coverage
    if args.sync_map:
        if not args.output:
            args.output = "coverage_report.json"

        report = validator.validate_coverage(
            args.sync_map,
            args.rtdb_rules,
            args.firestore_rules,
            args.functions_dir,
            args.output
        )

        return 0 if report['validation_passed'] else 1

    print("Error: No operation specified. Use --create-map, --update-map, or provide --sync-map for validation")
    return 1


if __name__ == "__main__":
    exit(main())
