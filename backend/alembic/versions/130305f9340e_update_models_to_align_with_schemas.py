"""Update models to align with schemas

Revision ID: 130305f9340e
Revises: bb04448d7c49
Create Date: 2024-09-26 13:03:44.937333

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '130305f9340e'
down_revision: Union[str, None] = 'bb04448d7c49'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
