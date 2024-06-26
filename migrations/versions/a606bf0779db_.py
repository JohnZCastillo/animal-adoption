"""empty message

Revision ID: a606bf0779db
Revises: f2b542743037
Create Date: 2024-03-20 17:56:52.652888

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a606bf0779db'
down_revision = 'f2b542743037'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('animal', schema=None) as batch_op:
        batch_op.add_column(sa.Column('Type.id', sa.Integer(), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('animal', schema=None) as batch_op:
        batch_op.drop_column('Type.id')

    # ### end Alembic commands ###
