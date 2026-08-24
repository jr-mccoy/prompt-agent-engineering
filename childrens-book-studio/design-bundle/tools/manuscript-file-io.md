# Tool Spec — manuscript-file-io

## Purpose
Read the manuscript-in-progress and write revisions. The carried state of the pipeline lives here.

## Signature
- `read-manuscript(path) → text`
- `write-manuscript-version(base, content) → new versioned path`  (e.g., `manuscript-v3.md`)

## Behavior
- Reads are non-destructive.
- **Writes always create a new version**; they never overwrite an existing file. This makes every state change reversible (the rollback path) and keeps the author in control of their files.

## Idempotency / safety
- Write is the only state-modifying operation in the system. It is made safe by versioning: re-running a stage produces a new version, never a clobbered one.
- The author owns all files and approves each version at the gate.

## Errors as guidance
- Target exists → bump the version number rather than overwrite; report the new path.
- Author has not approved the prior version → surface that the stage is pending a gate, do not auto-advance.

## Least privilege
Limited to the author's project directory; no network; no deletion (old versions are retained for rollback).
