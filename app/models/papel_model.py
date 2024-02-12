from app import db
from app.db.base_class import Base


class Papel(Base):
    __tablename__ = "papeis"

    nome = db.Column(db.String)
    access_level = db.Column(db.Integer)
    usuarios = db.relationship("Usuario", back_populates="papel")
