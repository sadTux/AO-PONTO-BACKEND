from app import db
from app.db.base_class import Base


class Turmas(Base):
    __tablename__ = "turmas"

    disciplina = db.Column(db.String)
    sala = db.Column(db.UUID(as_uuid=True), db.ForeignKey("salas.uuid"))
    nome_professor = db.Column(db.String)
    turno = db.Column(db.String)
    horario = db.Column(db.Time)
    ano = db.Column(db.Date)
    sala_turma = db.relationship("Salas", back_populates="turmas")
    aluno_tumas = db.relationship("AlunoTurmas", back_populates="turmas")
