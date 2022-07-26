"""empty message

Revision ID: 053adb94836e
Revises: 13dd3914e8d9
Create Date: 2022-05-20 00:31:14.085087

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '053adb94836e'
down_revision = '13dd3914e8d9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('account',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('total', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('account')
    # ### end Alembic commands ###
