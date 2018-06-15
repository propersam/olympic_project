"""empty message

Revision ID: 17fc1cf599a0
Revises: c60c05b88d77
Create Date: 2018-06-14 10:13:25.742310

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '17fc1cf599a0'
down_revision = 'c60c05b88d77'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_result_position', table_name='result')
    op.drop_table('result')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('result',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('athlete_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('sport_event_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('position', sa.VARCHAR(length=20), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['athlete_id'], [u'athlete.id'], name=u'result_athlete_id_fkey'),
    sa.ForeignKeyConstraint(['sport_event_id'], [u'sport_event.id'], name=u'result_sport_event_id_fkey'),
    sa.PrimaryKeyConstraint('id', name=u'result_pkey')
    )
    op.create_index('ix_result_position', 'result', ['position'], unique=False)
    # ### end Alembic commands ###