"""user table password name edited

Revision ID: b2ff554e5a3a
Revises: 9e493a1e5332
Create Date: 2024-12-01 16:15:44.984297

"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "b2ff554e5a3a"
down_revision: Union[str, None] = "9e493a1e5332"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("users", sa.Column("password", sa.String(), nullable=False))
    op.drop_column("users", "password_hash")
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "users",
        sa.Column("password_hash", sa.VARCHAR(), autoincrement=False, nullable=False),
    )
    op.drop_column("users", "password")
    # ### end Alembic commands ###
