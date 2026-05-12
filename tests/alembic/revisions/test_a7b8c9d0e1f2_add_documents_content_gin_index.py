"""Hooks for revision a7b8c9d0e1f2 (add_documents_content_gin_index)."""

from __future__ import annotations

from tests.alembic.registry import register_after_upgrade, register_before_upgrade
from tests.alembic.verifier import MigrationVerifier


@register_before_upgrade("a7b8c9d0e1f2")
def prepare_add_documents_content_gin_index(_verifier: MigrationVerifier) -> None:
    """Seed state and assertions before upgrading to a7b8c9d0e1f2."""


@register_after_upgrade("a7b8c9d0e1f2")
def verify_add_documents_content_gin_index(_verifier: MigrationVerifier) -> None:
    """Add assertions validating the effects of a7b8c9d0e1f2."""
