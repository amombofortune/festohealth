"""add content column to posts table

Revision ID: 2049ae854609
Revises: d3a8b0603aaf
Create Date: 2023-06-01 13:15:16.633532

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2049ae854609'
down_revision = 'd3a8b0603aaf'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
