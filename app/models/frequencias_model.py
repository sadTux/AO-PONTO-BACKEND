from app import db
from app.db.base_class import Base


class Frequencias(Base):
    __tablename__ = "frequencias"

    aluno_turmas_uuid = db.Column(
        db.UUID(as_uuid=True), db.ForeignKey("aluno_turmas.uuid"), primary_key=True
    )
    chamada = db.Column(db.Boolean)
    data = db.Column(db.Integer)
    aluno_turma = db.relationship("AlunoTurmas", back_populates="frequencia")
