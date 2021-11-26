"""admin table

Revision ID: ac5ececae517
Revises: d02c53b4cabd
Create Date: 2021-11-26 05:58:41.191665

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ac5ececae517'
down_revision = 'd02c53b4cabd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('admin',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.Column('email', sa.String(length=128), nullable=True),
    sa.Column('age', sa.Integer(), nullable=True),
    sa.Column('address', sa.String(length=256), nullable=True),
    sa.Column('phone', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_admin_address'), 'admin', ['address'], unique=False)
    op.create_index(op.f('ix_admin_age'), 'admin', ['age'], unique=False)
    op.create_index(op.f('ix_admin_email'), 'admin', ['email'], unique=False)
    op.create_index(op.f('ix_admin_phone'), 'admin', ['phone'], unique=False)
    op.create_index(op.f('ix_admin_username'), 'admin', ['username'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_admin_username'), table_name='admin')
    op.drop_index(op.f('ix_admin_phone'), table_name='admin')
    op.drop_index(op.f('ix_admin_email'), table_name='admin')
    op.drop_index(op.f('ix_admin_age'), table_name='admin')
    op.drop_index(op.f('ix_admin_address'), table_name='admin')
    op.drop_table('admin')
    # ### end Alembic commands ###
