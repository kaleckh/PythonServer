"""Initial migration

Revision ID: ebee27139c00
Revises: 
Create Date: 2024-11-21 15:38:25.195589

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = 'ebee27139c00'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('conversations',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('username', sa.String(), nullable=False),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.Column('blurhash', sa.String(), nullable=True),
    sa.Column('location', sa.String(), nullable=True),
    sa.Column('bio', sa.String(), nullable=True),
    sa.Column('color', sa.String(), nullable=True),
    sa.Column('links', sa.String(), nullable=True),
    sa.Column('followers', postgresql.ARRAY(sa.String()), nullable=True),
    sa.Column('following', postgresql.ARRAY(sa.String()), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_table('messages',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('conversation_id', sa.String(), nullable=True),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.Column('message', sa.String(), nullable=False),
    sa.Column('user_id', sa.String(), nullable=True),
    sa.Column('status', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['conversation_id'], ['conversations.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('posts',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('content', sa.String(), nullable=True),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('user_name', sa.String(), nullable=False),
    sa.Column('likes', postgresql.ARRAY(sa.String()), nullable=True),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['email'], ['users.email'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user_followers',
    sa.Column('user_id', sa.String(), nullable=False),
    sa.Column('follower_id', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['follower_id'], ['users.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('user_id', 'follower_id')
    )
    op.create_table('users_in_conversations',
    sa.Column('conversation_id', sa.String(), nullable=False),
    sa.Column('user_id', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['conversation_id'], ['conversations.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('conversation_id', 'user_id')
    )
    op.create_table('comments',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('content', sa.String(), nullable=False),
    sa.Column('post_id', sa.String(), nullable=True),
    sa.Column('likes', postgresql.ARRAY(sa.String()), nullable=True),
    sa.Column('user_id', sa.String(), nullable=True),
    sa.Column('user_name', sa.String(), nullable=False),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.Column('parent_id', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['parent_id'], ['comments.id'], ),
    sa.ForeignKeyConstraint(['post_id'], ['posts.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('reposts',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('post_id', sa.String(), nullable=True),
    sa.Column('comment_id', sa.String(), nullable=True),
    sa.Column('user_id', sa.String(), nullable=False),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['comment_id'], ['comments.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['post_id'], ['posts.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('reposts')
    op.drop_table('comments')
    op.drop_table('users_in_conversations')
    op.drop_table('user_followers')
    op.drop_table('posts')
    op.drop_table('messages')
    op.drop_table('users')
    op.drop_table('conversations')
    # ### end Alembic commands ###