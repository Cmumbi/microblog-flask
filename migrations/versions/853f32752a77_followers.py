"""followers

Revision ID: 853f32752a77
Revises: 7f2e032f5cb9
Create Date: 2020-06-08 12:28:40.305627

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '853f32752a77'
down_revision = '7f2e032f5cb9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('followers',
    sa.Column('follower_id', sa.Integer(), nullable=True),
    sa.Column('followed_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['followed_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['follower_id'], ['user.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('followers')
    # ### end Alembic commands ###
