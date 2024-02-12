from app import db
from app.db.base_class import Base


class Salas(Base):
    __tablename__ = "salas"

    nome = db.Column(db.String)
    escola_uuid = db.Column(db.UUID(as_uuid=True), db.ForeignKey("escolas.uuid"))
    turmas = db.relationship("Turmas", back_populates="sala_turma")
    escola = db.relationship("Escolas", back_populates="salas")
