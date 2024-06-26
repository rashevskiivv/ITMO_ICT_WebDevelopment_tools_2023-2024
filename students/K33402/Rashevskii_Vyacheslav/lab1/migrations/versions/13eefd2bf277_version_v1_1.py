"""version v1.1

Revision ID: 13eefd2bf277
Revises: 9bbf698c4d08
Create Date: 2024-04-14 22:01:27.676548

"""
from typing import Sequence, Union

import sqlmodel
from alembic import op
import sqlalchemy as sa
from sqlmodel import *
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '13eefd2bf277'
down_revision: Union[str, None] = '9bbf698c4d08'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('operation')
    op.add_column('categoryoperationlink', sa.Column('operation', sqlmodel.sql.sqltypes.AutoString(), nullable=True))
    op.add_column('customer', sa.Column('username', sqlmodel.sql.sqltypes.AutoString(), nullable=False))
    op.add_column('customer', sa.Column('password', sqlmodel.sql.sqltypes.AutoString(), nullable=False))
    op.create_index(op.f('ix_customer_username'), 'customer', ['username'], unique=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_customer_username'), table_name='customer')
    op.drop_column('customer', 'password')
    op.drop_column('customer', 'username')
    op.drop_column('categoryoperationlink', 'operation')
    op.create_table('operation',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('operation', postgresql.ENUM('income', 'outcome', name='operationenum'), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='operation_pkey')
    )
    # ### end Alembic commands ###
