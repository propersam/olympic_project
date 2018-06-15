"""empty message

Revision ID: 2bad15d1fdea
Revises: 3044d596d02b
Create Date: 2018-06-14 10:04:16.671522

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2bad15d1fdea'
down_revision = '3044d596d02b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('sport_category',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('sport_category', sa.String(length=30), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_sport_category_sport_category'), 'sport_category', ['sport_category'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_sport_category_sport_category'), table_name='sport_category')
    op.drop_table('sport_category')
    # ### end Alembic commands ###