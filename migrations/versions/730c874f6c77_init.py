"""init

Revision ID: 730c874f6c77
Revises: 
Create Date: 2023-06-29 17:30:19.138904

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '730c874f6c77'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('url_map',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('original', sa.String(), nullable=False),
    sa.Column('short', sa.String(length=16), nullable=False),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_url_map_short'), 'url_map', ['short'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_url_map_short'), table_name='url_map')
    op.drop_table('url_map')
    # ### end Alembic commands ###
