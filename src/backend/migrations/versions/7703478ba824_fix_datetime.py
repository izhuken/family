"""fix_datetime

Revision ID: 7703478ba824
Revises: e44bc19914c4
Create Date: 2024-06-05 16:49:05.547178

"""

from __future__ import annotations

from typing import Sequence

import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = "7703478ba824"
down_revision: str = "e44bc19914c4"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, "event", ["id"])
    op.create_unique_constraint(None, "family", ["id"])
    op.alter_column(
        "task",
        "finish_date",
        existing_type=postgresql.TIMESTAMP(),
        type_=sa.DateTime(timezone=True),
        existing_nullable=True,
    )
    op.alter_column(
        "event",
        "finish_date",
        existing_type=postgresql.TIMESTAMP(),
        type_=sa.DateTime(timezone=True),
        existing_nullable=True,
    )
    op.create_unique_constraint(None, "task", ["id"])
    op.create_unique_constraint(None, "user", ["id"])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, "user", type_="unique")
    op.drop_constraint(None, "task", type_="unique")
    op.alter_column(
        "task",
        "finish_date",
        existing_type=sa.DateTime(timezone=True),
        type_=postgresql.TIMESTAMP(),
        existing_nullable=True,
    )
    op.drop_constraint(None, "family", type_="unique")
    op.drop_constraint(None, "event", type_="unique")
    # ### end Alembic commands ###
