```markdown
# honcho Development Patterns

> Auto-generated skill from repository analysis

## Overview

This skill teaches the core development patterns, coding conventions, and workflows used in the **honcho** Python codebase. You will learn how to add features, fix bugs, manage database migrations, update deployment documentation, and modify CI/CD pipelines, all while following the repository's established conventions and processes.

---

## Coding Conventions

**File Naming**
- Use **camelCase** for file names.
  - Example: `userProfile.py`, `dataLoader.py`

**Imports**
- Use **relative imports** within the codebase.
  - Example:
    ```python
    from .utils import calculateSum
    from ..crud import userOperations
    ```

**Exports**
- Use **named exports** (explicitly define what is exported).
  - Example:
    ```python
    def fetchData():
        pass

    __all__ = ["fetchData"]
    ```

**Commit Messages**
- Follow **conventional commit** style.
- Prefixes: `docs`, `fix`, `feat`, `ci`, `test`
- Example:  
  ```
  feat: add user profile endpoint for onboarding flow
  fix: resolve off-by-one error in pagination logic
  ```

---

## Workflows

### Feature Development with Tests and Config
**Trigger:** When adding a new capability or algorithm to the backend  
**Command:** `/new-feature`

1. Update or add configuration in `src/config.py`.
2. Implement or modify logic in `src/crud/` or `src/utils/`.
3. Update or add unit tests in `tests/crud/` or `tests/`.
4. Optionally update related documentation.

**Example:**
```python
# src/config.py
NEW_FEATURE_FLAG = True

# src/crud/userProfile.py
def create_user_profile(data):
    # core logic here
    pass

# tests/crud/test_userProfile.py
def test_create_user_profile():
    # test logic here
    pass
```

---

### Bugfix with Test and Doc Update
**Trigger:** When addressing a bug, regression, or review feedback  
**Command:** `/bugfix`

1. Modify affected logic in `src/utils/`, `src/crud/`, or `src/models.py`.
2. Update or add related tests in `tests/`.
3. Update configuration or migration scripts if schema/index is involved.
4. Update documentation or deployment guides if needed.

**Example:**
```python
# src/utils/dateParser.py
def parse_date(date_str):
    # fixed parsing logic
    pass

# tests/test_dateParser.py
def test_parse_date():
    # test for the bugfix
    pass
```

---

### Database Index or Schema Migration
**Trigger:** When optimizing DB performance or changing schema  
**Command:** `/new-index`

1. Create or modify migration script in `migrations/versions/`.
2. Update models in `src/models.py`.
3. Optionally update related logic in `src/crud/` or `src/utils/`.
4. Update documentation if deployment steps change.

**Example:**
```python
# migrations/versions/20240601_add_index.py
def upgrade():
    op.create_index('ix_user_email', 'user', ['email'])

# src/models.py
class User(Base):
    __tablename__ = 'user'
    email = Column(String, index=True)
```

---

### Deployment and Branch Strategy Documentation
**Trigger:** When deployment process, integration, or branch strategy changes  
**Command:** `/update-deployment-docs`

1. Edit `DEPLOYMENT.md` or `CLAUDE.md` with new instructions.
2. Update `.kilo/plans/*.md` with promotion or deployment plans.
3. Optionally update `README.md`.

**Example:**
```markdown
# DEPLOYMENT.md
## New Deployment Steps
- Run migrations
- Deploy to staging
- Validate health checks
```

---

### CI/CD Workflow Update
**Trigger:** When CI/CD process or deployment infrastructure changes  
**Command:** `/update-ci`

1. Edit or remove files in `.github/workflows/`.
2. Update triggers or job definitions as needed.

**Example:**
```yaml
# .github/workflows/ci.yml
on:
  push:
    branches:
      - main
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Run tests
        run: pytest
```

---

## Testing Patterns

- **Framework:** Unknown (likely `pytest` or similar for Python)
- **Test File Pattern:** `*.test.ts` (note: this may be a legacy or placeholder pattern; Python tests typically use `test_*.py`)
- **Location:** `tests/`, `tests/crud/`
- **Typical Structure:**
  ```python
  # tests/crud/test_userProfile.py
  def test_create_user_profile():
      # Arrange
      # Act
      # Assert
      pass
  ```

---

## Commands

| Command                | Purpose                                                      |
|------------------------|--------------------------------------------------------------|
| /new-feature           | Start a new feature with config, logic, and tests            |
| /bugfix                | Fix a bug with tests and documentation updates               |
| /new-index             | Add or modify a database index or schema migration           |
| /update-deployment-docs| Update deployment or branch strategy documentation           |
| /update-ci             | Modify CI/CD workflow definitions                            |
```
