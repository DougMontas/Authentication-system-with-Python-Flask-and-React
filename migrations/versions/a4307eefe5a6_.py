"""empty message

Revision ID: a4307eefe5a6
Revises: 86a89c9dbb4a
Create Date: 2022-05-20 13:51:23.375718

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a4307eefe5a6'
down_revision = '86a89c9dbb4a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'password')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('password', sa.VARCHAR(length=200), autoincrement=False, nullable=False))
    # ### end Alembic commands ###
