# SPDX-FileCopyrightText: 2025-present MTS PJSC
# SPDX-License-Identifier: Apache-2.0
"""Add celery_taskmeta new columns

Revision ID: 0014
Revises: 0013
Create Date: 2026-11-24 14:04:45.135366

"""

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "0014"
down_revision = "0013"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("celery_taskmeta", sa.Column("children", sa.LargeBinary(), nullable=True))
    op.add_column("celery_taskmeta", sa.Column("stamps", sa.LargeBinary(), nullable=True))


def downgrade() -> None:
    op.drop_column("celery_taskmeta", "stamps")
    op.drop_column("celery_taskmeta", "children")
