"""pop

Revision ID: 18d5eeb66a89
Revises: 6e945276d216
Create Date: 2024-02-07 16:47:49.710684

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '18d5eeb66a89'
down_revision = '6e945276d216'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    from app.db import pop_db
    pop_db()
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###
