"""v1.6.5

Revision ID: 39a1671217f0
Revises: 2a0a9fcb610b
Create Date: 2024-05-06 22:03:28.236044

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

import sqlmodel


# revision identifiers, used by Alembic.
revision: str = '39a1671217f0'
down_revision: Union[str, None] = '2a0a9fcb610b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###