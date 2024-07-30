"""empty message

Revision ID: 8bcdec402d02
Revises: 876eb4cbd187
Create Date: 2024-07-19 23:17:45.949203

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8bcdec402d02'
down_revision = '876eb4cbd187'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('content', schema=None) as batch_op:
        batch_op.add_column(sa.Column('content', sa.String(length=120), nullable=False))
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('summarized_content')
        batch_op.drop_column('rss_id')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('content', schema=None) as batch_op:
        batch_op.add_column(sa.Column('rss_id', sa.INTEGER(), nullable=False))
        batch_op.add_column(sa.Column('summarized_content', sa.VARCHAR(length=120), nullable=False))
        batch_op.create_foreign_key(None, 'rss', ['rss_id'], ['id'])
        batch_op.drop_column('content')

    # ### end Alembic commands ###