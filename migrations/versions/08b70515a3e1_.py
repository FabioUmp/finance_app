"""empty message

Revision ID: 08b70515a3e1
Revises: 0b1c7d1c2aa1
Create Date: 2024-03-15 19:59:44.884300

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '08b70515a3e1'
down_revision = '0b1c7d1c2aa1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('account', sa.Column('user_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'account', 'user', ['user_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'account', type_='foreignkey')
    op.drop_column('account', 'user_id')
    # ### end Alembic commands ###
