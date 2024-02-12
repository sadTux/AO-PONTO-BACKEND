from app import db
from app.db.base_class import Base


class AlunoTurmas(Base):
    __tablename__ = "aluno_turmas"

    aluno_uuid = db.Column(db.UUID(as_uuid=True), db.ForeignKey("alunos.uuid"))
    turma_uuid = db.Column(db.UUID(as_uuid=True), db.ForeignKey("turmas.uuid"))
    turma_name = db.Column(db.String)
    aluno = db.relationship("Alunos", back_populates="aluno_turmas")
    turmas = db.relationship("Turmas", back_populates="aluno_tumas")
    frequencia = db.relationship("Frequencias", back_populates="aluno_turma")
