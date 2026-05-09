---
name: feature-development-with-tests-and-config
description: Workflow command scaffold for feature-development-with-tests-and-config in honcho.
allowed_tools: ["Bash", "Read", "Write", "Grep", "Glob"]
---

# /feature-development-with-tests-and-config

Use this workflow when working on **feature-development-with-tests-and-config** in `honcho`.

## Goal

Implements a new feature or enhancement, including configuration, core logic, and corresponding unit tests.

## Common Files

- `src/config.py`
- `src/crud/*.py`
- `src/utils/*.py`
- `tests/crud/*.py`
- `tests/*.py`

## Suggested Sequence

1. Understand the current state and failure mode before editing.
2. Make the smallest coherent change that satisfies the workflow goal.
3. Run the most relevant verification for touched files.
4. Summarize what changed and what still needs review.

## Typical Commit Signals

- Update or add configuration in src/config.py
- Implement or modify logic in src/crud/ or src/utils/
- Update or add unit tests in tests/crud/ or tests/
- Optionally update related documentation

## Notes

- Treat this as a scaffold, not a hard-coded script.
- Update the command if the workflow evolves materially.