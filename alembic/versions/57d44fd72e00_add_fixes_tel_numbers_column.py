"""add fixes tel_numbers column

Revision ID: 57d44fd72e00
Revises: 
Create Date: 2017-09-12 15:03:03.581830

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '57d44fd72e00'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('orders', sa.Column('edited_contact_phone', sa.Numeric))


def downgrade():
    op.drop_column('orders', 'edited_contact_phone')
