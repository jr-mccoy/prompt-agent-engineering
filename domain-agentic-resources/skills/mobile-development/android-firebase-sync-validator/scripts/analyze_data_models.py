#!/usr/bin/env python3
"""
Android Firebase Data Model Analyzer

Analyzes Android codebase to identify Firebase SDK usage, data models,
and sync requirements. Generates comprehensive analysis for sync validation.

Usage:
    analyze_data_models.py <app-directory> [options]

Options:
    --output PATH           Output JSON file path (default: app_analysis.json)
    --verbose              Show detailed analysis progress
    --include-patterns     Additional file patterns to scan (comma-separated)

Examples:
    analyze_data_models.py /path/to/android/app --output analysis.json
    analyze_data_models.py ./app --verbose
    analyze_data_models.py ./app --include-patterns "*.kt,*.java"

Output:
    JSON file containing:
    - Data models with Firebase integration
    - Firebase paths (RTDB and Firestore)
    - App features and their data dependencies
    - Sync type (realtime db, firestore, or both)
    - Privacy requirements inferred from code
"""

import argparse
import json
import os
import re
from pathlib import Path
from typing import Dict, List, Set, Optional
from dataclasses import dataclass, asdict
from datetime import datetime


@dataclass
class FirebasePath:
    """Represents a Firebase path found in code."""
    path: str
    sync_type: str  # 'rtdb' or 'firestore'
    file: str
    line: int
    context: str  # Surrounding code for context


@dataclass
class DataModel:
    """Represents a data model class that syncs to Firebase."""
    name: str
    file: str
    firebase_paths: List[str]
    sync_type: str  # 'rtdb', 'firestore', or 'both'
    privacy: str  # 'private', 'shared', 'public'
    fields: List[str]
    annotations: List[str]


@dataclass
class AppFeature:
    """Represents an app feature that uses Firebase data."""
    name: str
    files: List[str]
    data_dependencies: List[str]
    firebase_operations: List[str]  # 'read', 'write', 'listen', 'delete'


class AndroidFirebaseAnalyzer:
    """Analyzes Android codebase for Firebase usage patterns."""

    # Patterns to detect Firebase SDK usage
    RTDB_PATTERNS = [
        r'FirebaseDatabase\.getInstance\(\)',
        r'DatabaseReference',
        r'\.child\(["\']([^"\']+)["\']\)',
        r'\.setValue\(',
        r'\.addValueEventListener\(',
        r'\.addListenerForSingleValueEvent\(',
    ]

    FIRESTORE_PATTERNS = [
        r'FirebaseFirestore\.getInstance\(\)',
        r'CollectionReference',
        r'DocumentReference',
        r'\.collection\(["\']([^"\']+)["\']\)',
        r'\.document\(["\']([^"\']+)["\']\)',
        r'\.set\(',
        r'\.update\(',
        r'\.addSnapshotListener\(',
    ]

    # Patterns to detect data models
    DATA_CLASS_PATTERNS = [
        r'data\s+class\s+(\w+)',  # Kotlin data class
        r'class\s+(\w+).*@Entity',  # Room entity
        r'@Parcelize\s+data\s+class\s+(\w+)',  # Parcelable data class
    ]

    # Patterns to infer privacy
    PRIVATE_INDICATORS = ['password', 'token', 'secret', 'private', 'credential', 'ssn', 'email']
    SHARED_INDICATORS = ['group', 'team', 'shared', 'collaboration']
    PUBLIC_INDICATORS = ['public', 'global', 'feed', 'timeline']

    def __init__(self, app_directory: str, verbose: bool = False):
        self.app_directory = Path(app_directory)
        self.verbose = verbose
        self.data_models: List[DataModel] = []
        self.features: List[AppFeature] = []
        self.firebase_paths: List[FirebasePath] = []

    def analyze(self) -> Dict:
        """Run complete analysis and return results."""
        if self.verbose:
            print(f"Analyzing Android app at: {self.app_directory}")

        # Find all source files
        kotlin_files = list(self.app_directory.rglob("*.kt"))
        java_files = list(self.app_directory.rglob("*.java"))
        all_files = kotlin_files + java_files

        if self.verbose:
            print(f"Found {len(kotlin_files)} Kotlin files and {len(java_files)} Java files")

        # Analyze files
        for file_path in all_files:
            self._analyze_file(file_path)

        # Identify features from Activities and Fragments
        self._identify_features(all_files)

        # Build final analysis
        analysis = {
            "timestamp": datetime.now().isoformat(),
            "app_directory": str(self.app_directory),
            "data_models": [asdict(model) for model in self.data_models],
            "features": [asdict(feature) for feature in self.features],
            "firebase_paths": [asdict(path) for path in self.firebase_paths],
            "summary": {
                "total_data_models": len(self.data_models),
                "total_features": len(self.features),
                "total_firebase_paths": len(self.firebase_paths),
                "rtdb_usage": sum(1 for p in self.firebase_paths if p.sync_type == 'rtdb'),
                "firestore_usage": sum(1 for p in self.firebase_paths if p.sync_type == 'firestore'),
            }
        }

        if self.verbose:
            print(f"\nAnalysis Summary:")
            print(f"  Data Models: {analysis['summary']['total_data_models']}")
            print(f"  Features: {analysis['summary']['total_features']}")
            print(f"  Firebase Paths: {analysis['summary']['total_firebase_paths']}")
            print(f"  RTDB Usage: {analysis['summary']['rtdb_usage']}")
            print(f"  Firestore Usage: {analysis['summary']['firestore_usage']}")

        return analysis

    def _analyze_file(self, file_path: Path) -> None:
        """Analyze a single source file for Firebase usage and data models."""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                lines = content.split('\n')

            relative_path = file_path.relative_to(self.app_directory)

            # Detect Firebase paths
            self._detect_firebase_paths(content, lines, str(relative_path))

            # Detect data models
            self._detect_data_models(content, str(relative_path))

        except Exception as e:
            if self.verbose:
                print(f"Warning: Error analyzing {file_path}: {e}")

    def _detect_firebase_paths(self, content: str, lines: List[str], file_path: str) -> None:
        """Detect Firebase paths in code."""
        # RTDB paths
        for pattern in self.RTDB_PATTERNS:
            for match in re.finditer(pattern, content):
                line_num = content[:match.start()].count('\n') + 1
                context = lines[line_num - 1].strip() if line_num <= len(lines) else ""

                # Try to extract path from .child() calls
                if '.child(' in pattern:
                    path = match.group(1) if match.groups() else ""
                    if path:
                        firebase_path = FirebasePath(
                            path=path,
                            sync_type='rtdb',
                            file=file_path,
                            line=line_num,
                            context=context
                        )
                        self.firebase_paths.append(firebase_path)

        # Firestore paths
        collection_pattern = r'\.collection\(["\']([^"\']+)["\']\)'
        for match in re.finditer(collection_pattern, content):
            line_num = content[:match.start()].count('\n') + 1
            context = lines[line_num - 1].strip() if line_num <= len(lines) else ""
            path = match.group(1)

            firebase_path = FirebasePath(
                path=path,
                sync_type='firestore',
                file=file_path,
                line=line_num,
                context=context
            )
            self.firebase_paths.append(firebase_path)

    def _detect_data_models(self, content: str, file_path: str) -> None:
        """Detect data model classes."""
        for pattern in self.DATA_CLASS_PATTERNS:
            for match in re.finditer(pattern, content, re.MULTILINE):
                class_name = match.group(1)

                # Extract fields from class
                fields = self._extract_fields(content, match.start())

                # Determine privacy level
                privacy = self._infer_privacy(class_name.lower(), fields)

                # Find related Firebase paths
                related_paths = [
                    p.path for p in self.firebase_paths
                    if class_name.lower() in p.context.lower() or
                    any(field.lower() in p.path.lower() for field in fields)
                ]

                # Determine sync type
                sync_type = self._determine_sync_type(file_path, content)

                data_model = DataModel(
                    name=class_name,
                    file=file_path,
                    firebase_paths=related_paths if related_paths else [f"/{class_name.lower()}s"],
                    sync_type=sync_type,
                    privacy=privacy,
                    fields=fields,
                    annotations=[]
                )

                self.data_models.append(data_model)

    def _extract_fields(self, content: str, class_start: int) -> List[str]:
        """Extract field names from a class definition."""
        fields = []
        # Simple field extraction - look for 'val' or 'var' declarations
        field_pattern = r'(?:val|var)\s+(\w+)\s*:'
        class_content = content[class_start:class_start + 1000]  # Look ahead 1000 chars
        for match in re.finditer(field_pattern, class_content):
            fields.append(match.group(1))
        return fields

    def _infer_privacy(self, class_name: str, fields: List[str]) -> str:
        """Infer privacy level from class name and fields."""
        text = class_name + ' ' + ' '.join(fields)
        text_lower = text.lower()

        if any(indicator in text_lower for indicator in self.PRIVATE_INDICATORS):
            return 'private'
        elif any(indicator in text_lower for indicator in self.SHARED_INDICATORS):
            return 'shared'
        elif any(indicator in text_lower for indicator in self.PUBLIC_INDICATORS):
            return 'public'
        else:
            return 'private'  # Default to most restrictive

    def _determine_sync_type(self, file_path: str, content: str) -> str:
        """Determine if file uses RTDB, Firestore, or both."""
        has_rtdb = any(re.search(pattern, content) for pattern in self.RTDB_PATTERNS)
        has_firestore = any(re.search(pattern, content) for pattern in self.FIRESTORE_PATTERNS)

        if has_rtdb and has_firestore:
            return 'both'
        elif has_firestore:
            return 'firestore'
        elif has_rtdb:
            return 'rtdb'
        else:
            return 'unknown'

    def _identify_features(self, source_files: List[Path]) -> None:
        """Identify app features from Activities and Fragments."""
        feature_files = [
            f for f in source_files
            if 'Activity.kt' in f.name or 'Activity.java' in f.name or
            'Fragment.kt' in f.name or 'Fragment.java' in f.name
        ]

        for file_path in feature_files:
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()

                relative_path = file_path.relative_to(self.app_directory)

                # Extract feature name from class name
                class_match = re.search(r'class\s+(\w+(?:Activity|Fragment))', content)
                if not class_match:
                    continue

                feature_name = class_match.group(1).replace('Activity', '').replace('Fragment', '')

                # Find data dependencies (referenced data models)
                dependencies = [
                    model.name for model in self.data_models
                    if model.name in content
                ]

                # Identify Firebase operations
                operations = set()
                if 'setValue' in content or '.set(' in content or '.update(' in content:
                    operations.add('write')
                if 'addValueEventListener' in content or 'addSnapshotListener' in content:
                    operations.add('listen')
                if 'addListenerForSingleValueEvent' in content or '.get()' in content:
                    operations.add('read')
                if 'delete()' in content or 'removeValue()' in content:
                    operations.add('delete')

                if dependencies or operations:
                    feature = AppFeature(
                        name=feature_name,
                        files=[str(relative_path)],
                        data_dependencies=dependencies,
                        firebase_operations=list(operations)
                    )
                    self.features.append(feature)

            except Exception as e:
                if self.verbose:
                    print(f"Warning: Error analyzing feature file {file_path}: {e}")


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="Analyze Android codebase for Firebase usage and data models"
    )
    parser.add_argument("app_directory", help="Path to Android app directory")
    parser.add_argument("--output", default="app_analysis.json",
                        help="Output JSON file path")
    parser.add_argument("--verbose", "-v", action="store_true",
                        help="Show detailed analysis progress")
    parser.add_argument("--include-patterns",
                        help="Additional file patterns to scan (comma-separated)")

    args = parser.parse_args()

    # Validate app directory exists
    app_dir = Path(args.app_directory)
    if not app_dir.exists():
        print(f"Error: App directory not found: {app_dir}")
        return 1

    if not app_dir.is_dir():
        print(f"Error: Path is not a directory: {app_dir}")
        return 1

    # Run analysis
    analyzer = AndroidFirebaseAnalyzer(args.app_directory, verbose=args.verbose)
    analysis = analyzer.analyze()

    # Write output
    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(analysis, f, indent=2)

    print(f"\n✓ Analysis complete. Output written to: {output_path}")
    return 0


if __name__ == "__main__":
    exit(main())
