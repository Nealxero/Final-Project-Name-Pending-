"""empty message

Revision ID: 6885f0f2d846
Revises: c9211f0012f8
Create Date: 2022-09-26 20:42:05.989743

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6885f0f2d846'
down_revision = 'c9211f0012f8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'daily_plan', ['id'])
    op.alter_column('meal', 'sumarize',
               existing_type=sa.VARCHAR(length=120),
               nullable=True)
    op.alter_column('meal', 'nutrients',
               existing_type=sa.VARCHAR(length=80),
               nullable=True)
    op.alter_column('meal', 'ingredients',
               existing_type=sa.VARCHAR(length=80),
               nullable=True)
    op.create_unique_constraint(None, 'meal', ['id'])
    op.create_unique_constraint(None, 'user', ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'user', type_='unique')
    op.drop_constraint(None, 'meal', type_='unique')
    op.alter_column('meal', 'ingredients',
               existing_type=sa.VARCHAR(length=80),
               nullable=False)
    op.alter_column('meal', 'nutrients',
               existing_type=sa.VARCHAR(length=80),
               nullable=False)
    op.alter_column('meal', 'sumarize',
               existing_type=sa.VARCHAR(length=120),
               nullable=False)
    op.drop_constraint(None, 'daily_plan', type_='unique')
    # ### end Alembic commands ###