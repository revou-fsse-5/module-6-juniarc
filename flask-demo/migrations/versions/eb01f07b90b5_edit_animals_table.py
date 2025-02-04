"""edit animals table

Revision ID: eb01f07b90b5
Revises: add78c484407
Create Date: 2024-10-09 23:28:15.441991

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'eb01f07b90b5'
down_revision = 'add78c484407'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('animals', schema=None) as batch_op:
        batch_op.add_column(sa.Column('enclosure_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(None, 'enclosures', ['enclosure_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('animals', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('enclosure_id')

    # ### end Alembic commands ###
