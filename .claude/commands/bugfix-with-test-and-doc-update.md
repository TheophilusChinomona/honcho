---
name: bugfix-with-test-and-doc-update
description: Workflow command scaffold for bugfix-with-test-and-doc-update in honcho.
allowed_tools: ["Bash", "Read", "Write", "Grep", "Glob"]
---

# /bugfix-with-test-and-doc-update

Use this workflow when working on **bugfix-with-test-and-doc-update** in `honcho`.

## Goal

Fixes a bug or regression, often updating logic, configuration, tests, and sometimes documentation or migration scripts.

## Common Files

- `src/utils/*.py`
- `src/crud/*.py`
- `src/models.py`
- `tests/*.py`
- `migrations/versions/*.py`
- `DEPLOYMENT.md`

## Suggested Sequence

1. Understand the current state and failure mode before editing.
2. Make the smallest coherent change that satisfies the workflow goal.
3. Run the most relevant verification for touched files.
4. Summarize what changed and what still needs review.

## Typical Commit Signals

- Modify affected logic in src/utils/, src/crud/, or src/models.py
- Update or add related tests in tests/
- Update configuration or migration scripts if schema/index is involved
- Update documentation or deployment guides if needed

## Notes

- Treat this as a scaffold, not a hard-coded script.
- Update the command if the workflow evolves materially.