"""empty message

Revision ID: d95d79d1be33
Revises: e41cfa9e15dc
Create Date: 2024-07-24 17:03:27.097009

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd95d79d1be33'
down_revision = 'e41cfa9e15dc'
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
    sa.Column('rss_id', sa.VARCHAR(), nullable=False),
    sa.Column('summary', sa.VARCHAR(length=120), nullable=False),
    sa.Column('created_at', sa.DATETIME(), nullable=False),
    sa.ForeignKeyConstraint(['rss_id'], ['rss.id'], name='fk_content_rss_id_rss'),
    sa.PrimaryKeyConstraint('id', name='pk_content')
    )
    # ### end Alembic commands ###