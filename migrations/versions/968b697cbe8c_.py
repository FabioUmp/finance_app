"""empty message

Revision ID: 968b697cbe8c
Revises: ad7edced12cc
Create Date: 2024-02-28 21:39:23.964026

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '968b697cbe8c'
down_revision = 'ad7edced12cc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('operation', sa.Column('account_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'operation', 'account', ['account_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'operation', type_='foreignkey')
    op.drop_column('operation', 'account_id')
    # ### end Alembic commands ###
