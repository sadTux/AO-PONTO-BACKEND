from app import db
from app.db.base_class import Base


class RelatorioMerendeiras(Base):
    __tablename__ = "relatorios_merendeiras"

    escola_uuid = db.Column(db.UUID(as_uuid=True), db.ForeignKey("escolas.uuid"))
    escola_name = db.Column(db.String)
    numero_alunos = db.Column(db.String)
    sobra_limpa = db.Column(db.String)
    sobra_suja = db.Column(db.String)
    data = db.Column(db.Date)
    escola = db.relationship("Escolas", back_populates="relatorios_merendeiras")
