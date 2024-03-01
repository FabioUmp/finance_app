"""empty message

Revision ID: ad7edced12cc
Revises: 2ca05f4c77b1
Create Date: 2024-02-28 17:08:26.245019

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ad7edced12cc'
down_revision = '2ca05f4c77b1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('operation',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('resume', sa.String(length=100), nullable=False),
    sa.Column('cost', sa.Float(), nullable=False),
    sa.Column('type', sa.Enum('deposit', 'withdrawal', name='typeenum'), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('operation')
    # ### end Alembic commands ###
