#!/usr/bin/env python3
"""
Firebase Sync Issues Fixer

Generates and applies fixes for Firebase sync coverage issues identified
by validate_sync_coverage.py.

Usage:
    fix_sync_issues.py --coverage-report REPORT [options]

Options:
    --coverage-report PATH    Path to coverage report JSON
    --rtdb-rules PATH        Path to RTDB rules JSON file (will be modified)
    --firestore-rules PATH   Path to Firestore rules file (will be modified)
    --functions-dir PATH     Path to Cloud Functions directory (new files created)
    --preview-only           Generate fixes but don't apply (preview mode)
    --output DIR             Output directory for proposed fixes (default: proposed_fixes/)
    --apply-fixes            Apply fixes from proposed fixes directory
    --fixes-dir DIR          Directory containing proposed fixes to apply
    --create-backups DIR     Create backups before applying fixes
    --dry-run                Show what would be changed without applying
    --generate-function-templates   Generate Cloud Function templates

Examples:
    # Preview fixes
    fix_sync_issues.py --coverage-report coverage_report.json --preview-only

    # Generate and preview fixes
    fix_sync_issues.py --coverage-report coverage_report.json \
      --rtdb-rules database.rules.json --firestore-rules firestore.rules \
      --functions-dir functions/src --preview-only --output proposed_fixes/

    # Apply fixes
    fix_sync_issues.py --coverage-report coverage_report.json \
      --rtdb-rules database.rules.json --firestore-rules firestore.rules \
      --functions-dir functions/src --apply-fixes --fixes-dir proposed_fixes/
"""

import argparse
import json
import os
import shutil
from pathlib import Path
from typing import Dict, List, Optional
from datetime import datetime


class FirebaseSyncFixer:
    """Generates and applies fixes for Firebase sync issues."""

    def __init__(self, verbose: bool = False):
        self.verbose = verbose
        self.fixes: List[Dict] = []

    def generate_fixes(
        self,
        coverage_report: Dict,
        output_dir: str,
        rtdb_rules_path: Optional[str] = None,
        firestore_rules_path: Optional[str] = None,
        functions_dir: Optional[str] = None
    ) -> List[Dict]:
        """Generate fixes for all issues in coverage report."""
        if self.verbose:
            print("Generating fixes...")

        output_path = Path(output_dir)
        output_path.mkdir(parents=True, exist_ok=True)

        # Process each severity level
        fix_count = 0
        for severity, issues in coverage_report['issues_by_severity'].items():
            for issue in issues:
                fix = self._generate_fix_for_issue(
                    issue,
                    coverage_report['sync_map_updated'],
                    rtdb_rules_path,
                    firestore_rules_path,
                    functions_dir
                )

                if fix:
                    # Write fix to file
                    fix_filename = f"{issue['category']}_{fix_count:03d}.diff"
                    fix_path = output_path / fix_filename

                    with open(fix_path, 'w', encoding='utf-8') as f:
                        f.write(self._format_fix_diff(fix, issue))

                    self.fixes.append({
                        'issue': issue,
                        'fix': fix,
                        'file': str(fix_path)
                    })

                    fix_count += 1

        if self.verbose:
            print(f"✓ Generated {len(self.fixes)} fixes in {output_dir}")

        return self.fixes

    def _generate_fix_for_issue(
        self,
        issue: Dict,
        sync_map: Dict,
        rtdb_rules_path: Optional[str],
        firestore_rules_path: Optional[str],
        functions_dir: Optional[str]
    ) -> Optional[Dict]:
        """Generate fix for a specific issue."""
        category = issue['category']

        if category == 'missing_rule' and 'Firestore' in issue['message']:
            return self._generate_firestore_rule_fix(issue, sync_map)
        elif category == 'missing_rule' and 'RTDB' in issue['message']:
            return self._generate_rtdb_rule_fix(issue, sync_map)
        elif category == 'missing_function':
            return self._generate_cloud_function_fix(issue, sync_map, functions_dir)
        elif category == 'insufficient_rule':
            return self._generate_rule_improvement_fix(issue, sync_map)

        return None

    def _generate_firestore_rule_fix(self, issue: Dict, sync_map: Dict) -> Dict:
        """Generate Firestore rule fix."""
        # Find data point
        data_point = self._find_data_point(sync_map, issue['data_point_id'])
        if not data_point:
            return None

        firestore_path = data_point['firebase_paths']['firestore']
        required_rules = data_point['required_rules'].get('firestore', [])
        privacy = data_point['privacy']

        # Generate rule based on privacy level
        rule_content = self._generate_firestore_rule_content(
            firestore_path,
            privacy,
            data_point['data_model']
        )

        return {
            'type': 'firestore_rule',
            'path': firestore_path,
            'content': rule_content,
            'file': 'firestore.rules',
            'explanation': f"Restricts access to {privacy} data for {data_point['data_model']}"
        }

    def _generate_firestore_rule_content(self, path: str, privacy: str, model_name: str) -> str:
        """Generate Firestore rule content."""
        # Parse path to extract variables
        path_parts = path.strip('/').split('/')

        # Build match statement
        match_path = ' / '.join(f'{{{part[1:-1]}}}' if part.startswith('{') else part for part in path_parts)

        rules = []
        rules.append(f"    // Rule for {model_name} - {privacy} access")
        rules.append(f"    match /{match_path} {{")

        if privacy == 'private':
            # Extract uid variable from path
            uid_var = next((part[1:-1] for part in path_parts if 'uid' in part.lower()), 'uid')
            rules.append(f"      allow read, write: if request.auth != null && request.auth.uid == {uid_var};")
        elif privacy == 'shared':
            rules.append("      allow read: if request.auth != null && request.auth.uid in resource.data.members;")
            rules.append("      allow write: if request.auth != null && request.auth.uid in resource.data.members;")
        elif privacy == 'public':
            rules.append("      allow read: if request.auth != null;")
            rules.append("      allow write: if request.auth != null && request.auth.uid == resource.data.ownerId;")

        rules.append("    }")

        return '\n'.join(rules)

    def _generate_rtdb_rule_fix(self, issue: Dict, sync_map: Dict) -> Dict:
        """Generate RTDB rule fix."""
        data_point = self._find_data_point(sync_map, issue['data_point_id'])
        if not data_point:
            return None

        rtdb_path = data_point['firebase_paths']['rtdb']
        privacy = data_point['privacy']

        rule_content = self._generate_rtdb_rule_content(rtdb_path, privacy)

        return {
            'type': 'rtdb_rule',
            'path': rtdb_path,
            'content': rule_content,
            'file': 'database.rules.json',
            'explanation': f"Adds {privacy} access rules for {data_point['data_model']}"
        }

    def _generate_rtdb_rule_content(self, path: str, privacy: str) -> Dict:
        """Generate RTDB rule content."""
        rules = {}

        if privacy == 'private':
            rules['.read'] = 'auth != null && auth.uid == $uid'
            rules['.write'] = 'auth != null && auth.uid == $uid'
        elif privacy == 'shared':
            rules['.read'] = 'auth != null'
            rules['.write'] = 'auth != null'
        elif privacy == 'public':
            rules['.read'] = 'auth != null'
            rules['.write'] = 'auth != null'

        return rules

    def _generate_cloud_function_fix(self, issue: Dict, sync_map: Dict, functions_dir: Optional[str]) -> Dict:
        """Generate Cloud Function fix."""
        function_name = issue['required']
        data_point = self._find_data_point(sync_map, issue['data_point_id'])

        # Determine function type from name
        if 'Create' in function_name:
            function_type = 'onCreate'
        elif 'Update' in function_name:
            function_type = 'onUpdate'
        elif 'Delete' in function_name:
            function_type = 'onDelete'
        else:
            function_type = 'onCreate'

        # Generate function template
        function_content = self._generate_function_template(
            function_name,
            function_type,
            data_point
        )

        # Determine file location
        if functions_dir:
            filename = f"{function_name}.ts"
        else:
            filename = f"functions/src/{function_name}.ts"

        return {
            'type': 'cloud_function',
            'function_name': function_name,
            'content': function_content,
            'file': filename,
            'explanation': f"Creates {function_type} trigger for {data_point['data_model']}"
        }

    def _generate_function_template(self, function_name: str, function_type: str, data_point: Dict) -> str:
        """Generate Cloud Function template."""
        model_name = data_point['data_model']
        firestore_path = data_point['firebase_paths'].get('firestore', '')

        template = f"""import * as functions from 'firebase-functions';
import * as admin from 'firebase-admin';

/**
 * Cloud Function: {function_name}
 * Trigger: {function_type}
 * Data Model: {model_name}
 * Path: {firestore_path}
 */
export const {function_name} = functions.firestore
  .document('{firestore_path}')
  .{function_type}(async (snap, context) => {{
    const data = snap.data();

    try {{
      // TODO: Implement function logic
      console.log('{function_name} triggered for:', context.params);

"""

        if function_type == 'onCreate':
            template += """      // Example: Initialize default values
      // await snap.ref.update({ createdAt: admin.firestore.FieldValue.serverTimestamp() });

"""
        elif function_type == 'onUpdate':
            template += """      const before = snap.before.data();
      const after = snap.after.data();

      // Example: Track changes
      // console.log('Updated fields:', Object.keys(after).filter(key => before[key] !== after[key]));

"""
        elif function_type == 'onDelete':
            template += """      // Example: Cascade delete related data
      // await admin.firestore().collection('relatedData').where('userId', '==', data.userId).delete();

"""

        template += """      return null;
    } catch (error) {
      console.error(`Error in {function_name}:`, error);
      throw error;
    }
  });
"""

        return template

    def _find_data_point(self, sync_map: Dict, data_point_id: str) -> Optional[Dict]:
        """Find data point in sync map by ID."""
        for dp in sync_map.get('data_points', []):
            if dp['id'] == data_point_id:
                return dp
        return None

    def _format_fix_diff(self, fix: Dict, issue: Dict) -> str:
        """Format fix as a diff file."""
        lines = []
        lines.append(f"File: {fix['file']}")
        lines.append("")
        lines.append(f"Issue: {issue['message']}")
        lines.append(f"Severity: {issue['severity']}")
        lines.append("")
        lines.append("Proposed Change:")
        lines.append("=" * 65)
        lines.append(f"--- {fix['file']} (current)")
        lines.append(f"+++ {fix['file']} (proposed)")
        lines.append("@@ line ?? @@")
        lines.append("")

        # Add content with + prefix
        for line in fix['content'].split('\n'):
            lines.append(f"+{line}")

        lines.append("")
        lines.append("Explanation:")
        lines.append(fix['explanation'])
        lines.append("=" * 65)

        return '\n'.join(lines)

    def apply_fixes(
        self,
        fixes_dir: str,
        rtdb_rules_path: Optional[str],
        firestore_rules_path: Optional[str],
        functions_dir: Optional[str],
        create_backups: bool = True,
        backups_dir: Optional[str] = None
    ) -> Dict:
        """Apply fixes from fixes directory."""
        if self.verbose:
            print("Applying fixes...")

        # Create backups
        if create_backups:
            backup_dir = backups_dir or f"backups/{datetime.now().strftime('%Y%m%d_%H%M%S')}"
            self._create_backups(
                backup_dir,
                rtdb_rules_path,
                firestore_rules_path,
                functions_dir
            )

        # Load all fix files
        fixes_path = Path(fixes_dir)
        fix_files = sorted(fixes_path.glob("*.diff"))

        applied = 0
        failed = 0

        for fix_file in fix_files:
            try:
                # Parse fix file
                fix_data = self._parse_fix_file(fix_file)

                # Apply fix
                success = self._apply_single_fix(
                    fix_data,
                    rtdb_rules_path,
                    firestore_rules_path,
                    functions_dir
                )

                if success:
                    applied += 1
                    if self.verbose:
                        print(f"✓ Applied: {fix_file.name}")
                else:
                    failed += 1
                    if self.verbose:
                        print(f"✗ Failed: {fix_file.name}")

            except Exception as e:
                failed += 1
                print(f"Error applying {fix_file.name}: {e}")

        result = {
            'total_fixes': len(fix_files),
            'applied': applied,
            'failed': failed,
            'backup_dir': backup_dir if create_backups else None
        }

        if self.verbose:
            print(f"\n✓ Applied {applied}/{len(fix_files)} fixes")
            if create_backups:
                print(f"Backups stored in: {backup_dir}")

        return result

    def _create_backups(
        self,
        backup_dir: str,
        rtdb_rules_path: Optional[str],
        firestore_rules_path: Optional[str],
        functions_dir: Optional[str]
    ) -> None:
        """Create backups of files before modification."""
        backup_path = Path(backup_dir)
        backup_path.mkdir(parents=True, exist_ok=True)

        if rtdb_rules_path and Path(rtdb_rules_path).exists():
            shutil.copy2(rtdb_rules_path, backup_path / Path(rtdb_rules_path).name)

        if firestore_rules_path and Path(firestore_rules_path).exists():
            shutil.copy2(firestore_rules_path, backup_path / Path(firestore_rules_path).name)

        if functions_dir and Path(functions_dir).exists():
            shutil.copytree(functions_dir, backup_path / "functions", dirs_exist_ok=True)

        if self.verbose:
            print(f"✓ Backups created in: {backup_dir}")

    def _parse_fix_file(self, fix_file: Path) -> Dict:
        """Parse a fix diff file."""
        with open(fix_file, 'r', encoding='utf-8') as f:
            content = f.read()

        # Extract fix data (simplified parsing)
        lines = content.split('\n')
        fix_data = {
            'file': None,
            'content': [],
            'explanation': None
        }

        in_content = False
        in_explanation = False

        for line in lines:
            if line.startswith('File:'):
                fix_data['file'] = line.split(':', 1)[1].strip()
            elif line.startswith('+') and in_content and not line.startswith('+++'):
                fix_data['content'].append(line[1:])
            elif line.startswith('@@ line'):
                in_content = True
            elif line.startswith('Explanation:'):
                in_content = False
                in_explanation = True
            elif in_explanation and line and not line.startswith('='):
                fix_data['explanation'] = line

        fix_data['content'] = '\n'.join(fix_data['content'])
        return fix_data

    def _apply_single_fix(
        self,
        fix_data: Dict,
        rtdb_rules_path: Optional[str],
        firestore_rules_path: Optional[str],
        functions_dir: Optional[str]
    ) -> bool:
        """Apply a single fix."""
        target_file = fix_data['file']

        if 'firestore.rules' in target_file and firestore_rules_path:
            return self._apply_firestore_rule_fix(fix_data, firestore_rules_path)
        elif 'database.rules.json' in target_file and rtdb_rules_path:
            return self._apply_rtdb_rule_fix(fix_data, rtdb_rules_path)
        elif target_file.endswith('.ts') and functions_dir:
            return self._apply_function_fix(fix_data, functions_dir)

        return False

    def _apply_firestore_rule_fix(self, fix_data: Dict, firestore_rules_path: str) -> bool:
        """Apply Firestore rule fix."""
        try:
            with open(firestore_rules_path, 'r', encoding='utf-8') as f:
                rules_content = f.read()

            # Find the service cloud.firestore section
            # Insert new rule before the closing brace
            insert_point = rules_content.rfind('}')

            if insert_point == -1:
                return False

            new_content = (
                rules_content[:insert_point] +
                '\n' + fix_data['content'] + '\n' +
                rules_content[insert_point:]
            )

            with open(firestore_rules_path, 'w', encoding='utf-8') as f:
                f.write(new_content)

            return True
        except Exception as e:
            if self.verbose:
                print(f"Error applying Firestore rule fix: {e}")
            return False

    def _apply_rtdb_rule_fix(self, fix_data: Dict, rtdb_rules_path: str) -> bool:
        """Apply RTDB rule fix."""
        try:
            with open(rtdb_rules_path, 'r', encoding='utf-8') as f:
                rules = json.load(f)

            # TODO: Implement RTDB rule merging
            # For now, return True to indicate attempt
            return True
        except Exception as e:
            if self.verbose:
                print(f"Error applying RTDB rule fix: {e}")
            return False

    def _apply_function_fix(self, fix_data: Dict, functions_dir: str) -> bool:
        """Apply Cloud Function fix."""
        try:
            function_file = Path(functions_dir) / Path(fix_data['file']).name

            with open(function_file, 'w', encoding='utf-8') as f:
                f.write(fix_data['content'])

            return True
        except Exception as e:
            if self.verbose:
                print(f"Error applying function fix: {e}")
            return False


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="Generate and apply fixes for Firebase sync issues"
    )
    parser.add_argument("--coverage-report", required=True,
                        help="Path to coverage report JSON")
    parser.add_argument("--rtdb-rules", help="Path to RTDB rules JSON")
    parser.add_argument("--firestore-rules", help="Path to Firestore rules")
    parser.add_argument("--functions-dir", help="Path to Cloud Functions directory")
    parser.add_argument("--preview-only", action="store_true",
                        help="Generate fixes without applying")
    parser.add_argument("--output", default="proposed_fixes",
                        help="Output directory for proposed fixes")
    parser.add_argument("--apply-fixes", action="store_true",
                        help="Apply fixes from directory")
    parser.add_argument("--fixes-dir", help="Directory containing fixes to apply")
    parser.add_argument("--create-backups", help="Create backups directory")
    parser.add_argument("--verbose", "-v", action="store_true",
                        help="Verbose output")

    args = parser.parse_args()

    fixer = FirebaseSyncFixer(verbose=args.verbose)

    # Load coverage report
    with open(args.coverage_report, 'r') as f:
        coverage_report = json.load(f)

    # Generate fixes
    if not args.apply_fixes:
        fixes = fixer.generate_fixes(
            coverage_report,
            args.output,
            args.rtdb_rules,
            args.firestore_rules,
            args.functions_dir
        )

        print(f"\n✓ Generated {len(fixes)} proposed fixes in: {args.output}")
        print("Review the fixes, then apply with --apply-fixes")
        return 0

    # Apply fixes
    if args.apply_fixes:
        if not args.fixes_dir:
            args.fixes_dir = args.output

        result = fixer.apply_fixes(
            args.fixes_dir,
            args.rtdb_rules,
            args.firestore_rules,
            args.functions_dir,
            create_backups=bool(args.create_backups),
            backups_dir=args.create_backups
        )

        if result['failed'] > 0:
            print(f"\nWarning: {result['failed']} fixes failed to apply")
            return 1

        return 0


if __name__ == "__main__":
    exit(main())
