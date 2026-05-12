"""Hooks for revision b2c3d4e5f6a7 (add_documents_collection_level_index)."""

from __future__ import annotations

from tests.alembic.registry import register_after_upgrade, register_before_upgrade
from tests.alembic.verifier import MigrationVerifier


@register_before_upgrade("b2c3d4e5f6a7")
def prepare_add_documents_collection_level_index(_verifier: MigrationVerifier) -> None:
    """Seed state and assertions before upgrading to b2c3d4e5f6a7."""


@register_after_upgrade("b2c3d4e5f6a7")
def verify_add_documents_collection_level_index(_verifier: MigrationVerifier) -> None:
    """Add assertions validating the effects of b2c3d4e5f6a7."""
