"""drop fk

Revision ID: 309c93dd0050
Revises: 54825a348b4f
Create Date: 2020-07-17 18:41:08.149896

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '309c93dd0050'
down_revision = '54825a348b4f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('table_a', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('table_b')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('table_a', schema=None) as batch_op:
        batch_op.add_column(sa.Column('table_b', sa.INTEGER(), nullable=False))
        batch_op.create_foreign_key(None, 'table_b', ['table_b'], ['id'])

    # ### end Alembic commands ###
