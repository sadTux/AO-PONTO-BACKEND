from app import db
from app.db.base_class import Base


class Escolas(Base):
    __tablename__ = "escolas"

    nome = db.Column(db.String)
    inep_codigo = db.Column(db.String)
    uf = db.Column(db.String)
    municipio = db.Column(db.String)
    cep = db.Column(db.String)
    endereco = db.Column(db.String)
    categoria_administrativa = db.Column(db.String)
    etapa_ensino = db.Column(db.String)

    usuarios = db.relationship("Usuario", back_populates="escola")
    alunos = db.relationship("Alunos", back_populates="escola")

    salas = db.relationship("Salas", back_populates="escola")
    cardapio_escola = db.relationship(
        "CardapioEscola", back_populates="escola"
    )
    relatorios_merendeiras = db.relationship(
        "RelatorioMerendeiras", back_populates="escola"
    )
