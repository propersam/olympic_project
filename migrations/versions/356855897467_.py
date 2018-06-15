"""empty message

Revision ID: 356855897467
Revises: 7f13dbe72a3f
Create Date: 2018-06-14 09:54:28.824144

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '356855897467'
down_revision = '7f13dbe72a3f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('olympic_year',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('year', sa.DateTime(), nullable=True),
    sa.Column('participating_country_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['participating_country_id'], ['country.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_olympic_year_year'), 'olympic_year', ['year'], unique=False)
    op.create_table('result',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('athlete_id', sa.Integer(), nullable=True),
    sa.Column('sport_event_id', sa.Integer(), nullable=True),
    sa.Column('medal_won', sa.String(length=20), nullable=True),
    sa.ForeignKeyConstraint(['athlete_id'], ['athlete.id'], ),
    sa.ForeignKeyConstraint(['sport_event_id'], ['sport_event.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_index('ix_athlete_sport_event_Date', table_name='athlete_sport_event')
    op.drop_table('athlete_sport_event')
    op.drop_index('ix_athlete_olympic_year', table_name='athlete')
    op.drop_column(u'athlete', 'olympic_year')
    op.drop_index('ix_sport_event_olympic_year', table_name='sport_event')
    op.drop_index('ix_sport_event_sport_category', table_name='sport_event')
    op.drop_column(u'sport_event', 'olympic_year')
    op.drop_column(u'sport_event', 'sport_category')
    op.drop_index('ix_stadium_olympic_year', table_name='stadium')
    op.drop_column(u'stadium', 'olympic_year')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(u'stadium', sa.Column('olympic_year', postgresql.TIMESTAMP(), autoincrement=False, nullable=True))
    op.create_index('ix_stadium_olympic_year', 'stadium', ['olympic_year'], unique=False)
    op.add_column(u'sport_event', sa.Column('sport_category', sa.VARCHAR(length=30), autoincrement=False, nullable=True))
    op.add_column(u'sport_event', sa.Column('olympic_year', postgresql.TIMESTAMP(), autoincrement=False, nullable=True))
    op.create_index('ix_sport_event_sport_category', 'sport_event', ['sport_category'], unique=False)
    op.create_index('ix_sport_event_olympic_year', 'sport_event', ['olympic_year'], unique=False)
    op.add_column(u'athlete', sa.Column('olympic_year', postgresql.TIMESTAMP(), autoincrement=False, nullable=True))
    op.create_index('ix_athlete_olympic_year', 'athlete', ['olympic_year'], unique=False)
    op.create_table('athlete_sport_event',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('athlete_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('sport_event_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('Date', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('Position', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['athlete_id'], [u'athlete.id'], name=u'athlete_sport_event_athlete_id_fkey'),
    sa.ForeignKeyConstraint(['sport_event_id'], [u'sport_event.id'], name=u'athlete_sport_event_sport_event_id_fkey'),
    sa.PrimaryKeyConstraint('id', name=u'athlete_sport_event_pkey')
    )
    op.create_index('ix_athlete_sport_event_Date', 'athlete_sport_event', ['Date'], unique=False)
    op.drop_table('result')
    op.drop_index(op.f('ix_olympic_year_year'), table_name='olympic_year')
    op.drop_table('olympic_year')
    # ### end Alembic commands ###