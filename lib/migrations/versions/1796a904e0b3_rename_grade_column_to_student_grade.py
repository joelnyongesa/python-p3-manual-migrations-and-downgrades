"""Rename grade column to student_grade

Revision ID: 1796a904e0b3
Revises: 425cd1183367
Create Date: 2023-10-01 13:50:26.166927

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1796a904e0b3'
down_revision = '425cd1183367'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.alter_column('scholars', 'grade', new_column_name='student_grade', existing_type=sa.Integer)


def downgrade() -> None:
    op.alter_column('scholars', 'student_grade', new_column_name='grade', existing_type=sa.Integer)
