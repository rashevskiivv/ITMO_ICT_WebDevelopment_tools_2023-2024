"""v1.6.6

Revision ID: e6e9e98cb43e
Revises: 39a1671217f0
Create Date: 2024-05-06 22:06:27.920451

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

import sqlmodel


# revision identifiers, used by Alembic.
revision: str = 'e6e9e98cb43e'
down_revision: Union[str, None] = '39a1671217f0'
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
