"""<Add Data>

Revision ID: a8d1c69ca327
Revises: 9b00e55c8066
Create Date: 2024-07-29 12:20:19.735651

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a8d1c69ca327'
down_revision = '9b00e55c8066'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('adoption_locations',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_adoption_locations'))
    )
    op.create_table('owners',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_owners'))
    )
    op.create_table('dogs',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('breed', sa.String(), nullable=True),
    sa.Column('image', sa.String(), nullable=True),
    sa.Column('owner_id', sa.Integer(), nullable=True),
    sa.Column('adoption_location_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['adoption_location_id'], ['adoption_locations.id'], name=op.f('fk_dogs_adoption_location_id_adoption_locations')),
    sa.ForeignKeyConstraint(['owner_id'], ['owners.id'], name=op.f('fk_dogs_owner_id_owners')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_dogs'))
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('dogs')
    op.drop_table('owners')
    op.drop_table('adoption_locations')
    # ### end Alembic commands ###
