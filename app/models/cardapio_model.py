from app import db
from app.db.base_class import Base


class Cardapio(Base):
    __tablename__ = "cardapios"

    nome = db.Column(db.String)
    descricao = db.Column(db.String)
    cardapio_escola = db.relationship("CardapioEscola", back_populates="cardapio")