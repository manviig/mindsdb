"""add knowledge base

Revision ID: 309db3d07cf4
Revises: 6cb02dfd7f61
Create Date: 2023-09-20 13:48:39.422306

"""
import sqlalchemy as sa
from alembic import op

import mindsdb.interfaces.storage.db  # noqa

# revision identifiers, used by Alembic.
revision = "309db3d07cf4"
down_revision = "6cb02dfd7f61"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "knowledge_base",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("project_id", sa.Integer(), nullable=False),
        sa.Column("params", sa.JSON(), nullable=True),
        sa.Column("vector_database_id", sa.Integer(), nullable=True),
        sa.Column("vector_database_table", sa.String(), nullable=True),
        sa.Column("embedding_model_id", sa.Integer(), nullable=True),
        sa.Column("created_at", sa.DateTime(), nullable=True),
        sa.Column("updated_at", sa.DateTime(), nullable=True),
        sa.ForeignKeyConstraint(
            ["embedding_model_id"],
            ["predictor.id"],
            name="fk_knowledge_base_embedding_model_id",
        ),
        sa.ForeignKeyConstraint(
            ["vector_database_id"],
            ["integration.id"],
            name="fk_knowledge_base_vector_database_id",
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint(
            "name", "project_id", name="unique_knowledge_base_name_project_id"
        ),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("knowledge_base")
    # ### end Alembic commands ###