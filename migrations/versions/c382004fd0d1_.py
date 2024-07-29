"""empty message

Revision ID: c382004fd0d1
Revises: d87d4fe9f246
Create Date: 2024-07-21 18:29:40.927593

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c382004fd0d1'
down_revision = 'd87d4fe9f246'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('_alembic_tmp_content')
    op.drop_table('content')
    with op.batch_alter_table('rss', schema=None) as batch_op:
        batch_op.add_column(sa.Column('created_at', sa.DateTime(), nullable=False))
        batch_op.drop_column('datetime')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('rss', schema=None) as batch_op:
        batch_op.add_column(sa.Column('datetime', sa.DATETIME(), nullable=False))
        batch_op.drop_column('created_at')

    op.create_table('content',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('title', sa.VARCHAR(length=120), nullable=False),
    sa.Column('rss_id', sa.INTEGER(), nullable=False),
    sa.Column('created_at', sa.DATETIME(), nullable=False),
    sa.Column('content', sa.VARCHAR(length=120), nullable=False),
    sa.ForeignKeyConstraint(['rss_id'], ['rss.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('_alembic_tmp_content',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('summary', sa.VARCHAR(length=120), nullable=False),
    sa.Column('rss_id', sa.INTEGER(), nullable=True),
    sa.Column('created_at', sa.DATETIME(), nullable=False),
    sa.ForeignKeyConstraint(['rss_id'], ['rss.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###
