"""empty message

Revision ID: 04542b5063bb
Revises: 
Create Date: 2021-08-29 23:11:09.537471

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '04542b5063bb'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('customer', 'currently_renting')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('customer', sa.Column('currently_renting', sa.BOOLEAN(), autoincrement=False, nullable=False))
    # ### end Alembic commands ###