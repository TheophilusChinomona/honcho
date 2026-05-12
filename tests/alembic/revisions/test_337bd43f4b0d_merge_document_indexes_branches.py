"""Hooks for revision 337bd43f4b0d (merge_document_indexes_branches)."""

from __future__ import annotations

from tests.alembic.registry import register_after_upgrade, register_before_upgrade
from tests.alembic.verifier import MigrationVerifier


@register_before_upgrade("337bd43f4b0d")
def prepare_merge_document_indexes_branches(_verifier: MigrationVerifier) -> None:
    """Seed state and assertions before upgrading to 337bd43f4b0d."""


@register_after_upgrade("337bd43f4b0d")
def verify_merge_document_indexes_branches(_verifier: MigrationVerifier) -> None:
    """Add assertions validating the effects of 337bd43f4b0d."""
