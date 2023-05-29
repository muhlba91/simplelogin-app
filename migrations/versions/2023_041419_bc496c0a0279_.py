"""empty message

Revision ID: bc496c0a0279
Revises: 893c0d18475f
Create Date: 2023-04-14 19:09:38.540514

"""
import sqlalchemy_utils
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bc496c0a0279'
down_revision = '893c0d18475f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index(op.f('ix_alias_used_on_alias_id'), 'alias_used_on', ['alias_id'], unique=False)
    op.create_index(op.f('ix_client_user_alias_id'), 'client_user', ['alias_id'], unique=False)
    op.create_index(op.f('ix_hibp_notified_alias_alias_id'), 'hibp_notified_alias', ['alias_id'], unique=False)
    op.create_index(op.f('ix_users_newsletter_alias_id'), 'users', ['newsletter_alias_id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_users_newsletter_alias_id'), table_name='users')
    op.drop_index(op.f('ix_hibp_notified_alias_alias_id'), table_name='hibp_notified_alias')
    op.drop_index(op.f('ix_client_user_alias_id'), table_name='client_user')
    op.drop_index(op.f('ix_alias_used_on_alias_id'), table_name='alias_used_on')
    # ### end Alembic commands ###