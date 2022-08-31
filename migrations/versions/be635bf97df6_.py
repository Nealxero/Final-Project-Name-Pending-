"""empty message

Revision ID: be635bf97df6
Revises: 630d3df079e6
Create Date: 2022-08-31 17:52:49.933614

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'be635bf97df6'
down_revision = '630d3df079e6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('meals',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=False),
    sa.Column('nutrients', sa.String(length=120), nullable=False),
    sa.Column('ingredients', sa.String(length=120), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('ingredients'),
    sa.UniqueConstraint('name'),
    sa.UniqueConstraint('nutrients')
    )
    op.create_table('favorites',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('meals_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['meals_id'], ['meals.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('favorites')
    op.drop_table('meals')
    # ### end Alembic commands ###