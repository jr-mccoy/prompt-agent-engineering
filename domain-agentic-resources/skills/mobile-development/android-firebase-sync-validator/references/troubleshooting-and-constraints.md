# Android Firebase Sync Validator — Troubleshooting and Constraints

## Common Issues

### Issue: "Firebase SDK usage found but no sync map entry"

**Quick Diagnosis:**
```bash
grep -r "FirebaseDatabase\|FirebaseFirestore" app/src/main/java | grep -v ".class"
python scripts/analyze_data_models.py /path/to/app --verbose
```

**Root Causes:**
1. New feature added after sync map created
2. Data model not following expected patterns
3. Firebase path constructed dynamically

**Resolution:**
```bash
# Re-run analysis to detect new code
python scripts/analyze_data_models.py /path/to/app \
  --output .firebase-sync-validator/app_analysis.json

# Update sync map
python scripts/validate_sync_coverage.py \
  --app-analysis .firebase-sync-validator/app_analysis.json \
  --sync-map .firebase-sync-validator/sync_map.json \
  --update-map
```

### Issue: "Overly permissive Firebase rule detected"

**Quick Diagnosis:**
Look for rules that allow access without proper auth checks:
```bash
grep -E "allow read, write: if true|allow read, write: if auth != null" firestore.rules database.rules.json
```

**Root Causes:**
1. Developer used placeholder rule and forgot to tighten
2. Rules not updated when privacy requirements changed
3. Misunderstanding of Firebase security model

**Resolution:**
The validator will flag these and propose more restrictive rules:
```bash
python scripts/validate_sync_coverage.py \
  --sync-map .firebase-sync-validator/sync_map.json \
  --rtdb-rules database.rules.json \
  --firestore-rules firestore.rules \
  --security-audit
```

### Issue: "Cloud Function missing for data cascade"

**Quick Diagnosis:**
```bash
# Search for delete operations in app code
grep -r "delete()" app/src/main/java --include="*.kt" --include="*.java"

# Check if corresponding Cloud Functions exist
ls functions/src/ | grep -i delete
```

**Root Causes:**
1. App assumes cascade delete but no function implements it
2. Cloud Function exists but not triggered on correct path
3. Function exists but has bugs

**Resolution:**
The fix generator will create Cloud Function templates:
```bash
python scripts/fix_sync_issues.py \
  --coverage-report .firebase-sync-validator/coverage_report.json \
  --functions-dir functions/src \
  --generate-function-templates
```

### Issue: "Sync map out of date after refactoring"

**Quick Diagnosis:**
```bash
# Compare sync map data points with current codebase
python scripts/validate_sync_coverage.py \
  --sync-map .firebase-sync-validator/sync_map.json \
  --verify-code-locations
```

**Root Causes:**
1. Files moved during refactoring
2. Data models renamed
3. Firebase paths changed

**Resolution:**
```bash
# Regenerate sync map from scratch
mv .firebase-sync-validator/sync_map.json .firebase-sync-validator/sync_map.json.old

python scripts/analyze_data_models.py /path/to/app \
  --output .firebase-sync-validator/app_analysis.json

python scripts/validate_sync_coverage.py \
  --app-analysis .firebase-sync-validator/app_analysis.json \
  --create-map .firebase-sync-validator/sync_map.json

# Compare old and new to understand changes
diff .firebase-sync-validator/sync_map.json.old .firebase-sync-validator/sync_map.json
```

---

## Edge Cases & Failure Modes

### Missing App Code
**Symptom:** Validator can't find Android app source code
**Handling:** Prompt user for correct path to app directory

### Dynamic Firebase Paths
**Symptom:** App constructs Firebase paths at runtime (e.g., from user input)
**Handling:**
- Detect path patterns from code analysis
- Add to sync map with placeholders
- Flag for manual review in coverage report

### Firebase Config Files Not Found
**Symptom:** database.rules.json or firestore.rules missing
**Handling:**
- Check common locations (root, firebase/, config/)
- Prompt user for file paths
- Offer to generate template files

### Partial Success in Fix Application
**Symptom:** Some fixes apply successfully, others fail
**Handling:**
- Report which fixes succeeded
- Report which fixes failed with error details
- Update sync map only for successful fixes
- Allow user to retry failed fixes

### Ambiguous Privacy Requirements
**Symptom:** Can't determine if data should be private, shared, or public
**Handling:**
- Default to most restrictive (private)
- Flag in coverage report for user decision
- Provide options for different privacy levels

---

## Safety & Constraints

**NEVER:**
- Modify Firebase rules without creating backups
- Apply fixes without user review and approval
- Deploy to production Firebase automatically
- Delete or overwrite sync map without user confirmation
- Make rules more permissive than required

**ALWAYS:**
- Create timestamped backups before any modifications
- Show diffs of all proposed changes before applying
- Validate syntax after each change
- Default to most restrictive security rules
- Document reasoning for each generated rule/function
- Preserve user comments in Firebase rules files
- Update sync map after successful fixes
- Prompt for confirmation before destructive operations
