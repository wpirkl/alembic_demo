"""drop fk

Revision ID: 6a3fbc16171d
Revises: 1827ea7e2a90
Create Date: 2020-07-20 09:23:54.843925

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '6a3fbc16171d'
down_revision = '1827ea7e2a90'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('table_b', schema=None) as batch_op:
        # batch_op.drop_index('uq_table_b_name')
        batch_op.drop_column('name')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('table_b', schema=None) as batch_op:
        batch_op.add_column(sa.Column('name', mysql.VARCHAR(length=30), nullable=False))
        # batch_op.create_index('uq_table_b_name', ['name'], unique=True)

    # ### end Alembic commands ###