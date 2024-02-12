from app import db
from app.db.base_class import Base


class Disciplinas(Base):
    __tablename__ = "disciplinas"

    name = db.Column(db.String)
