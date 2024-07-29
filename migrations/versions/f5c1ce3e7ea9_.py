"""empty message

Revision ID: f5c1ce3e7ea9
Revises: 09e155e8fc10
Create Date: 2024-07-24 17:26:14.867325

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f5c1ce3e7ea9'
down_revision = '09e155e8fc10'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('_alembic_tmp_content')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('_alembic_tmp_content',
    sa.Column('id', sa.VARCHAR(), nullable=False),
    sa.Column('summary', sa.VARCHAR(), nullable=False),
    sa.Column('created_at', sa.DATETIME(), nullable=False),
    sa.Column('rss_link', sa.VARCHAR(), nullable=False),
    sa.ForeignKeyConstraint(['rss_link'], ['rss.id'], name='fk_content_rss_link_rss'),
    sa.PrimaryKeyConstraint('id', name='pk_content')
    )
    # ### end Alembic commands ###
