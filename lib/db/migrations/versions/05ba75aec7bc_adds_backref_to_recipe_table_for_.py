"""Adds backref to Recipe table for instructions and ingredients

Revision ID: 05ba75aec7bc
Revises: f7044c2d551c
Create Date: 2023-08-21 13:35:09.118125

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '05ba75aec7bc'
down_revision: Union[str, None] = 'f7044c2d551c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###
