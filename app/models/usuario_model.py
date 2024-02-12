from app import db
from app.db.base_class import Base


class Usuario(Base):
    __tablename__ = "usuarios"

    cpf = db.Column(db.String, unique=True, nullable=False)
    senha = db.Column(db.LargeBinary(), nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    data_nascimento = db.Column(db.Date)
    active = db.Column(db.Boolean)
    escola_uuid = db.Column(db.UUID(as_uuid=True), db.ForeignKey("escolas.uuid"))
    papel_uuid = db.Column(db.UUID(as_uuid=True), db.ForeignKey("papeis.uuid"))
    escola_name = db.Column(db.String)
    papel_name = db.Column(db.String)
    access_level = db.Column(db.String)
    
    papel = db.relationship("Papel", back_populates="usuarios")
    escola = db.relationship("Escolas", back_populates="usuarios")
