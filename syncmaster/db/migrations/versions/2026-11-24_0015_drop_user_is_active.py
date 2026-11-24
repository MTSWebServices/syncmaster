# SPDX-FileCopyrightText: 2025-present MTS PJSC
# SPDX-License-Identifier: Apache-2.0
"""Drop user.is_active

Revision ID: 0015
Revises: 0014
Create Date: 2026-11-24 15:36:19.463692

"""

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "0015"
down_revision = "0014"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.drop_column("user", "is_active")


def downgrade() -> None:
    op.add_column("user", sa.Column("is_active", sa.BOOLEAN(), autoincrement=False, nullable=True))
    op.execute("UPDATE 'user' SET is_active=true")
    op.alter_column("user", "is_active", nullable=False, existing_nullable=True)
