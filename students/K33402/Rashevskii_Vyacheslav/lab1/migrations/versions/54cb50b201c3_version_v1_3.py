"""version v1.3

Revision ID: 54cb50b201c3
Revises: f7d58cb6ae26
Create Date: 2024-04-14 22:07:55.635525

"""
from typing import Sequence, Union

import sqlmodel
from alembic import op
import sqlalchemy as sa
from sqlmodel import *

# revision identifiers, used by Alembic.
revision: str = '54cb50b201c3'
down_revision: Union[str, None] = 'f7d58cb6ae26'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('operation',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('operation', sa.Enum('income', 'outcome', name='operationenum'), nullable=False),
                    sa.Column('limit', sa.Float(), nullable=False),
                    sa.Column('alias', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.drop_column('categoryoperationlink', 'operation')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('categoryoperationlink', sa.Column('operation', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.drop_table('operation')
    # ### end Alembic commands ###