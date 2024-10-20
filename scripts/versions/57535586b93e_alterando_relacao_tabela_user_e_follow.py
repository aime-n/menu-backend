"""alterando relacao tabela user e follow

Revision ID: 57535586b93e
Revises: 0af0301ea94a
Create Date: 2024-10-18 15:00:22.156810

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql
import sqlmodel


# revision identifiers, used by Alembic.
revision: str = '57535586b93e'
down_revision: Union[str, None] = '0af0301ea94a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('categories',
    sa.Column('category_id', sa.Integer(), nullable=False),
    sa.Column('name', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('parent_id', sa.Integer(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['parent_id'], ['categories.category_id'], ),
    sa.PrimaryKeyConstraint('category_id')
    )
    op.create_table('users',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('username', sqlmodel.sql.sqltypes.AutoString(length=50), nullable=False),
    sa.Column('email', sqlmodel.sql.sqltypes.AutoString(length=100), nullable=False),
    sa.Column('password_hash', sqlmodel.sql.sqltypes.AutoString(length=255), nullable=False),
    sa.Column('profile_pic', sqlmodel.sql.sqltypes.AutoString(length=255), nullable=True),
    sa.Column('bio', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('user_id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_table('folders',
    sa.Column('folder_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('name', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('description', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.user_id'], ),
    sa.PrimaryKeyConstraint('folder_id')
    )
    op.create_table('follows',
    sa.Column('follower_id', sa.Integer(), nullable=False),
    sa.Column('followed_id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['followed_id'], ['users.user_id'], ),
    sa.ForeignKeyConstraint(['follower_id'], ['users.user_id'], ),
    sa.PrimaryKeyConstraint('follower_id', 'followed_id')
    )
    op.create_table('ingredients',
    sa.Column('ingredient_id', sa.Integer(), nullable=False),
    sa.Column('openfoodfacts_id', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('openfoodfacts_content', postgresql.JSONB(astext_type=sa.Text()), nullable=False),
    sa.Column('name', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('category_id', sa.Integer(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['category_id'], ['categories.category_id'], ),
    sa.PrimaryKeyConstraint('ingredient_id')
    )
    op.create_table('recipes',
    sa.Column('recipe_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('title', sqlmodel.sql.sqltypes.AutoString(length=255), nullable=False),
    sa.Column('description', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('instructions', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('prep_time', sa.Integer(), nullable=True),
    sa.Column('cook_time', sa.Integer(), nullable=True),
    sa.Column('servings', sa.Integer(), nullable=True),
    sa.Column('image_url', sqlmodel.sql.sqltypes.AutoString(length=255), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.user_id'], ),
    sa.PrimaryKeyConstraint('recipe_id')
    )
    op.create_table('user_preferences',
    sa.Column('preference_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('preference_type', sqlmodel.sql.sqltypes.AutoString(length=50), nullable=False),
    sa.Column('value', sqlmodel.sql.sqltypes.AutoString(length=100), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.user_id'], ),
    sa.PrimaryKeyConstraint('preference_id')
    )
    op.create_table('comments',
    sa.Column('comment_id', sa.Integer(), nullable=False),
    sa.Column('recipe_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('parent_comment_id', sa.Integer(), nullable=True),
    sa.Column('content', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['parent_comment_id'], ['comments.comment_id'], ),
    sa.ForeignKeyConstraint(['recipe_id'], ['recipes.recipe_id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.user_id'], ),
    sa.PrimaryKeyConstraint('comment_id')
    )
    op.create_table('folder_recipes',
    sa.Column('folder_id', sa.Integer(), nullable=False),
    sa.Column('recipe_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['folder_id'], ['folders.folder_id'], ),
    sa.ForeignKeyConstraint(['recipe_id'], ['recipes.recipe_id'], ),
    sa.PrimaryKeyConstraint('folder_id', 'recipe_id')
    )
    op.create_table('ingredient_synonyms',
    sa.Column('synonym_id', sa.Integer(), nullable=False),
    sa.Column('ingredient_id', sa.Integer(), nullable=False),
    sa.Column('synonym', sqlmodel.sql.sqltypes.AutoString(length=100), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['ingredient_id'], ['ingredients.ingredient_id'], ),
    sa.PrimaryKeyConstraint('synonym_id')
    )
    op.create_table('likes',
    sa.Column('like_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('recipe_id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['recipe_id'], ['recipes.recipe_id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.user_id'], ),
    sa.PrimaryKeyConstraint('like_id')
    )
    op.create_table('recipe_ingredients',
    sa.Column('recipe_id', sa.Integer(), nullable=False),
    sa.Column('ingredient_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['ingredient_id'], ['ingredients.ingredient_id'], ),
    sa.ForeignKeyConstraint(['recipe_id'], ['recipes.recipe_id'], ),
    sa.PrimaryKeyConstraint('recipe_id', 'ingredient_id')
    )
    op.create_table('user_inventory',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('ingredient_id', sa.Integer(), nullable=False),
    sa.Column('added_date', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['ingredient_id'], ['ingredients.ingredient_id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.user_id'], ),
    sa.PrimaryKeyConstraint('user_id', 'ingredient_id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_inventory')
    op.drop_table('recipe_ingredients')
    op.drop_table('likes')
    op.drop_table('ingredient_synonyms')
    op.drop_table('folder_recipes')
    op.drop_table('comments')
    op.drop_table('user_preferences')
    op.drop_table('recipes')
    op.drop_table('ingredients')
    op.drop_table('follows')
    op.drop_table('folders')
    op.drop_table('users')
    op.drop_table('categories')
    # ### end Alembic commands ###
