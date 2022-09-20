"""empty message

Revision ID: 4f7c2537d1bc
Revises: 8c33844dbccd
Create Date: 2022-09-20 09:43:06.733717

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '4f7c2537d1bc'
down_revision = '8c33844dbccd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('cars')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cars',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('model', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('doors', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('created_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('updated_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='cars_pkey'),
    sa.UniqueConstraint('name', name='cars_name_key')
    )
    # ### end Alembic commands ###