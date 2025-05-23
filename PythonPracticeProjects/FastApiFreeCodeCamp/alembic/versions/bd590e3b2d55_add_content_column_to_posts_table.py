"""add content column to posts table

Revision ID: bd590e3b2d55
Revises: 86861596dfc8
Create Date: 2025-05-23 11:10:23.679180

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'bd590e3b2d55'
down_revision: Union[str, None] = '86861596dfc8'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
