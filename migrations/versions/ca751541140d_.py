"""empty message

Revision ID: ca751541140d
Revises: 4e930f54a967
Create Date: 2018-06-01 10:32:03.278880

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ca751541140d'
down_revision = '4e930f54a967'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('sport_event',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('sport_event', sa.String(length=30), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_sport_event_sport_event'), 'sport_event', ['sport_event'], unique=False)
    op.create_table('stadium',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('stadium_name', sa.String(length=30), nullable=True),
    sa.Column('location', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_stadium_stadium_name'), 'stadium', ['stadium_name'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_stadium_stadium_name'), table_name='stadium')
    op.drop_table('stadium')
    op.drop_index(op.f('ix_sport_event_sport_event'), table_name='sport_event')
    op.drop_table('sport_event')
    # ### end Alembic commands ###