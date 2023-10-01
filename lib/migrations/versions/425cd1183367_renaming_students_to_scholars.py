"""Renaming students to scholars

Revision ID: 425cd1183367
Revises: 791279dd0760
Create Date: 2023-10-01 13:41:59.665420

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '425cd1183367'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students', 'scholars')


def downgrade() -> None:
    op.rename_table('scholars', 'students')
