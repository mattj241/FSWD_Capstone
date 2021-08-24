"""empty message

Revision ID: db7746b7cceb
Revises: 951d8aa069a2
Create Date: 2021-08-23 21:29:13.920798

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'db7746b7cceb'
down_revision = '951d8aa069a2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('vehicle', 'lic_plate')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('vehicle', sa.Column('lic_plate', sa.VARCHAR(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
