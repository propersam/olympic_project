"""empty message

Revision ID: a6ce6ed97615
Revises: 7eae3af45e37
Create Date: 2018-06-14 20:23:27.852092

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a6ce6ed97615'
down_revision = '7eae3af45e37'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('result', sa.Column('stadium_id', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'result', 'stadium', ['stadium_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'result', type_='foreignkey')
    op.drop_column('result', 'stadium_id')
    # ### end Alembic commands ###