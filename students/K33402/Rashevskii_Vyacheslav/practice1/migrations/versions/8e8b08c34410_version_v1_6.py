"""version v1.6

Revision ID: 8e8b08c34410
Revises: 4d0bc80d419f
Create Date: 2024-04-24 19:54:00.739095

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

import sqlmodel


# revision identifiers, used by Alembic.
revision: str = '8e8b08c34410'
down_revision: Union[str, None] = '4d0bc80d419f'
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