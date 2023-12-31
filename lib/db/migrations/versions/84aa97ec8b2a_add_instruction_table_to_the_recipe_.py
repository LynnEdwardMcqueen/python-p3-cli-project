"""Add Instruction table to the recipe databasse

Revision ID: 84aa97ec8b2a
Revises: 798451b62321
Create Date: 2023-08-19 18:02:20.353991

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '84aa97ec8b2a'
down_revision: Union[str, None] = '798451b62321'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('instruction',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('instruction', sa.String(), nullable=True),
    sa.Column('recipe_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['recipe_id'], ['recipe.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('instruction')
    # ### end Alembic commands ###
