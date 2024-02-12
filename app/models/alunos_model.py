from app import db
from app.db.base_class import Base


class Alunos(Base):
    __tablename__ = "alunos"

    escola_uuid = db.Column(db.UUID(as_uuid=True), db.ForeignKey("escolas.uuid"))
    escola_name = db.Column(db.String)
    matricula = db.Column(db.Integer)
    nome = db.Column(db.String)
    data_nascimento = db.Column(db.Date)
    aluno_turmas = db.relationship("AlunoTurmas", back_populates="aluno")
    escola = db.relationship("Escolas", back_populates="alunos")