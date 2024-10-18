"""Inserindo demais tabelas

Revision ID: 457206d37e6d
Revises: b3971c50b114
Create Date: 2024-10-18 14:15:33.018028

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql
import sqlmodel

# revision identifiers, used by Alembic.
revision: str = '457206d37e6d'
down_revision: Union[str, None] = 'b3971c50b114'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('ingredient_synonyms', 'updated_at',
               existing_type=postgresql.TIMESTAMP(),
               nullable=True)
    op.add_column('user_preferences', sa.Column('updated_at', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user_preferences', 'updated_at')
    op.alter_column('ingredient_synonyms', 'updated_at',
               existing_type=postgresql.TIMESTAMP(),
               nullable=False)
    # ### end Alembic commands ###
