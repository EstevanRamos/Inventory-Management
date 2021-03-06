"""users table and Commodity table

Revision ID: c404a37debe1
Revises: 
Create Date: 2022-01-27 22:20:10.002798

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c404a37debe1'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_email'), 'user', ['email'], unique=True)
    op.create_index(op.f('ix_user_username'), 'user', ['username'], unique=True)
    op.create_table('commodity',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('item', sa.String(length=60), nullable=True),
    sa.Column('entry_type', sa.String(length=10), nullable=True),
    sa.Column('quantity', sa.String(length=10), nullable=True),
    sa.Column('datein', sa.DateTime(), nullable=True),
    sa.Column('dateout', sa.DateTime(), nullable=True),
    sa.Column('shipper', sa.String(length=60), nullable=True),
    sa.Column('consignee', sa.String(length=60), nullable=True),
    sa.Column('customer', sa.String(length=60), nullable=True),
    sa.Column('notes', sa.Text(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_commodity_consignee'), 'commodity', ['consignee'], unique=False)
    op.create_index(op.f('ix_commodity_customer'), 'commodity', ['customer'], unique=False)
    op.create_index(op.f('ix_commodity_datein'), 'commodity', ['datein'], unique=False)
    op.create_index(op.f('ix_commodity_dateout'), 'commodity', ['dateout'], unique=False)
    op.create_index(op.f('ix_commodity_entry_type'), 'commodity', ['entry_type'], unique=False)
    op.create_index(op.f('ix_commodity_item'), 'commodity', ['item'], unique=False)
    op.create_index(op.f('ix_commodity_quantity'), 'commodity', ['quantity'], unique=False)
    op.create_index(op.f('ix_commodity_shipper'), 'commodity', ['shipper'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_commodity_shipper'), table_name='commodity')
    op.drop_index(op.f('ix_commodity_quantity'), table_name='commodity')
    op.drop_index(op.f('ix_commodity_item'), table_name='commodity')
    op.drop_index(op.f('ix_commodity_entry_type'), table_name='commodity')
    op.drop_index(op.f('ix_commodity_dateout'), table_name='commodity')
    op.drop_index(op.f('ix_commodity_datein'), table_name='commodity')
    op.drop_index(op.f('ix_commodity_customer'), table_name='commodity')
    op.drop_index(op.f('ix_commodity_consignee'), table_name='commodity')
    op.drop_table('commodity')
    op.drop_index(op.f('ix_user_username'), table_name='user')
    op.drop_index(op.f('ix_user_email'), table_name='user')
    op.drop_table('user')
    # ### end Alembic commands ###
