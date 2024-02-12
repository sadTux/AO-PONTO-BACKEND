from app import db
from app.db.base_class import Base


class CardapioEscola(Base):
    __tablename__ = "cardapio_escola"

    escola_uuid = db.Column(db.UUID(as_uuid=True), db.ForeignKey("escolas.uuid"))
    cardapio_uuid = db.Column(db.UUID(as_uuid=True), db.ForeignKey("cardapios.uuid"))
    cardapio_name = db.Column(db.String)
    cardapio_descricao = db.Column(db.String)
    dia_da_semana = db.Column(db.String)
    turno = db.Column(db.String)
    cardapio = db.relationship("Cardapio", back_populates="cardapio_escola")
    escola = db.relationship("Escolas", back_populates="cardapio_escola")
