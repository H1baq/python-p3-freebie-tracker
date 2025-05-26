"""create freebie table

Revision ID: 51dda38663fe
Revises: 5f72c58bf48c
Create Date: 2025-05-25 09:11:47.123660

"""
from alembic import op
import sqlalchemy as sa

from alembic import op
import sqlalchemy as sa

def upgrade():
    op.create_table('freebies',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('item_name', sa.String(), nullable=False),
        sa.Column('value', sa.Integer(), nullable=False),
        sa.Column('dev_id', sa.Integer(), sa.ForeignKey('devs.id'), nullable=False),
        sa.Column('company_id', sa.Integer(), sa.ForeignKey('companies.id'), nullable=False)
    )

def downgrade():
    op.drop_table('freebies')


# revision identifiers, used by Alembic.
revision = '51dda38663fe'
down_revision = '5f72c58bf48c'
branch_labels = None
depends_on = None



