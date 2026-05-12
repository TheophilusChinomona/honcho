"""merge document indexes branches

Revision ID: 337bd43f4b0d
Revises: b2c3d4e5f6a7, e4eba9cfaa6f
Create Date: 2026-05-12 14:45:03.060150

"""

from collections.abc import Sequence

from migrations.utils import get_schema

# revision identifiers, used by Alembic.
revision: str = "337bd43f4b0d"
down_revision: str | None = ("b2c3d4e5f6a7", "e4eba9cfaa6f")
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None

schema = get_schema()


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
