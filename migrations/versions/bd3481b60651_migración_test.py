"""Migración test

Revision ID: bd3481b60651
Revises: 5427bea9f81b
Create Date: 2024-05-24 21:22:40.126074

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bd3481b60651'
down_revision = '5427bea9f81b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('username', sa.String(length=80), nullable=False),
    sa.Column('password', sa.String(length=120), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_table('workouts',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('date_time', sa.DateTime(), nullable=False),
    sa.Column('name_workout', sa.String(length=120), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('excercises',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('description', sa.Text(), nullable=False),
    sa.Column('workout_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['workout_id'], ['workouts.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('repetitions',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('workout_id', sa.Integer(), nullable=False),
    sa.Column('excercise_id', sa.Integer(), nullable=False),
    sa.Column('series_number', sa.Integer(), nullable=False),
    sa.Column('num_repetitions', sa.PickleType(), nullable=False),
    sa.Column('peso', sa.Float(), nullable=True),
    sa.ForeignKeyConstraint(['excercise_id'], ['excercises.id'], ),
    sa.ForeignKeyConstraint(['workout_id'], ['workouts.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('repetitions')
    op.drop_table('excercises')
    op.drop_table('workouts')
    op.drop_table('users')
    # ### end Alembic commands ###
