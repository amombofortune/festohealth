"""create post table

Revision ID: d3a8b0603aaf
Revises: 
Create Date: 2023-06-01 13:02:16.585607

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd3a8b0603aaf'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table("posts", sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
                    sa.Column('title', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_table("posts")
    pass
