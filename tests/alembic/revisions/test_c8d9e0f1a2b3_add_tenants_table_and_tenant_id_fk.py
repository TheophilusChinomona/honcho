"""Hooks for revision c8d9e0f1a2b3 (add_tenants_table_and_tenant_id_fk)."""

from __future__ import annotations

from tests.alembic.registry import register_after_upgrade, register_before_upgrade
from tests.alembic.verifier import MigrationVerifier


@register_before_upgrade("c8d9e0f1a2b3")
def prepare_add_tenants_table_and_tenant_id_fk(_verifier: MigrationVerifier) -> None:
    """Seed state and assertions before upgrading to c8d9e0f1a2b3."""


@register_after_upgrade("c8d9e0f1a2b3")
def verify_add_tenants_table_and_tenant_id_fk(_verifier: MigrationVerifier) -> None:
    """Add assertions validating the effects of c8d9e0f1a2b3."""
