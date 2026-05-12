"""add tenants table and tenant_id FK on workspaces

Add multi-tenancy support:
1. Create tenants table with id, name, metadata, configuration, admin_jwt_secret.
2. Add tenant_id FK column to workspaces referencing tenants(id).
"""

import sqlalchemy as sa
from alembic import op

revision: str = "c8d9e0f1a2b3"
down_revision: str | None = "337bd43f4b0d"  # merges the two document index branches
branch_labels: tuple[str, ...] | None = None
depends_on: tuple[str, ...] | None = None


def upgrade() -> None:
    op.create_table(
        "tenants",
        sa.Column("id", sa.Text(), primary_key=True),
        sa.Column("name", sa.Text(), unique=True, nullable=False),
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            server_default=sa.func.now(),
            nullable=False,
        ),
        sa.Column(
            "metadata",
            sa.dialects.postgresql.JSONB(),
            server_default=sa.text("'{}'::jsonb"),
            nullable=False,
        ),
        sa.Column(
            "configuration",
            sa.dialects.postgresql.JSONB(),
            server_default=sa.text("'{}'::jsonb"),
            nullable=False,
        ),
        sa.Column("admin_jwt_secret", sa.Text(), nullable=True),
        sa.CheckConstraint("length(id) = 21", name="tenant_id_length"),
        sa.CheckConstraint("length(name) <= 512", name="tenant_name_length"),
        sa.CheckConstraint("id ~ '^[A-Za-z0-9_-]+$'", name="tenant_id_format"),
    )

    op.create_index("ix_tenants_created_at", "tenants", ["created_at"])

    op.add_column(
        "workspaces",
        sa.Column(
            "tenant_id",
            sa.Text(),
            sa.ForeignKey("tenants.id"),
            nullable=True,
        ),
    )
    op.create_index("ix_workspaces_tenant_id", "workspaces", ["tenant_id"])


def downgrade() -> None:
    op.drop_index("ix_workspaces_tenant_id", table_name="workspaces")
    op.drop_column("workspaces", "tenant_id")
    op.drop_index("ix_tenants_created_at", table_name="tenants")
    op.drop_table("tenants")
