# SPDX-FileCopyrightText: 2025-present MTS PJSC
# SPDX-License-Identifier: Apache-2.0
"""Add celery_*_date_done indexex

Revision ID: 0013
Revises: 0012
Create Date: 2026-04-02 11:06:44.293882

"""

from alembic import op

# revision identifiers, used by Alembic.
revision = "0013"
down_revision = "0012"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_index(
        op.f("ix_celery_taskmeta_date_done"),
        "celery_taskmeta",
        ["date_done"],
        unique=False,
        if_not_exists=True,
    )
    op.create_index(
        op.f("ix_celery_tasksetmeta_date_done"),
        "celery_tasksetmeta",
        ["date_done"],
        unique=False,
        if_not_exists=True,
    )


def downgrade() -> None:
    op.drop_index(op.f("ix_celery_tasksetmeta_date_done"), table_name="celery_tasksetmeta", if_exists=True)
    op.drop_index(op.f("ix_celery_taskmeta_date_done"), table_name="celery_taskmeta", if_exists=True)
