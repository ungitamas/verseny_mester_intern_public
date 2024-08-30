"""is ended

Revision ID: c752edcc6c60
Revises: b989e6f884f4
Create Date: 2024-08-28 09:36:07.058365

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c752edcc6c60'
down_revision = 'b989e6f884f4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('events', schema=None) as batch_op:
        batch_op.add_column(sa.Column('is_ended', sa.Boolean(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('events', schema=None) as batch_op:
        batch_op.drop_column('is_ended')

    # ### end Alembic commands ###
