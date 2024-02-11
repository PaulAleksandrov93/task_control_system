"""Initial migration

Revision ID: 9539241bd7ba
Revises: 
Create Date: 2024-02-11 18:50:04.240937

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '9539241bd7ba'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('products', sa.Column('task_shift_id', sa.Integer(), nullable=True))
    op.alter_column('products', 'unique_code',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.drop_index('ix_products_unique_code', table_name='products')
    op.create_unique_constraint(None, 'products', ['unique_code'])
    op.create_foreign_key(None, 'products', 'task_shifts', ['task_shift_id'], ['id'])
    op.drop_column('products', 'task_id')
    op.alter_column('task_shifts', 'task_description',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('task_shifts', 'work_center',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('task_shifts', 'shift',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('task_shifts', 'brigade',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('task_shifts', 'batch_number',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('task_shifts', 'batch_date',
               existing_type=sa.DATE(),
               nullable=False)
    op.alter_column('task_shifts', 'product_name',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('task_shifts', 'ecn_code',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('task_shifts', 'rc_identifier',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('task_shifts', 'start_time',
               existing_type=postgresql.TIMESTAMP(),
               nullable=False)
    op.alter_column('task_shifts', 'end_time',
               existing_type=postgresql.TIMESTAMP(),
               nullable=False)
    op.drop_index('ix_task_shifts_priority', table_name='task_shifts')
    op.create_unique_constraint(None, 'task_shifts', ['batch_number'])
    op.drop_column('task_shifts', 'priority')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('task_shifts', sa.Column('priority', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'task_shifts', type_='unique')
    op.create_index('ix_task_shifts_priority', 'task_shifts', ['priority'], unique=False)
    op.alter_column('task_shifts', 'end_time',
               existing_type=postgresql.TIMESTAMP(),
               nullable=True)
    op.alter_column('task_shifts', 'start_time',
               existing_type=postgresql.TIMESTAMP(),
               nullable=True)
    op.alter_column('task_shifts', 'rc_identifier',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('task_shifts', 'ecn_code',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('task_shifts', 'product_name',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('task_shifts', 'batch_date',
               existing_type=sa.DATE(),
               nullable=True)
    op.alter_column('task_shifts', 'batch_number',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('task_shifts', 'brigade',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('task_shifts', 'shift',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('task_shifts', 'work_center',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('task_shifts', 'task_description',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.add_column('products', sa.Column('task_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'products', type_='foreignkey')
    op.drop_constraint(None, 'products', type_='unique')
    op.create_index('ix_products_unique_code', 'products', ['unique_code'], unique=True)
    op.alter_column('products', 'unique_code',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.drop_column('products', 'task_shift_id')
    # ### end Alembic commands ###
