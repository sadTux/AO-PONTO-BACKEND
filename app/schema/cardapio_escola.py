from datetime import datetime
from uuid import UUID

from fastapi import Form
from pydantic import BaseModel, Field, validator, model_validator

from app import error, models, util




__all__ = [
    "PostCardapioEscola",
    "GetCardapioEscola",
    "PutCardapioEscola",
]


class PostCardapioEscola(BaseModel):
    """__summary__

    Attributes:
        escola_uuid (UUID): descrever escola_uuid.
        cardapio_uuid (UUID): descrever cardapio_uuid.
        cardapio_name (str): descrever cardapio_name.
        cardapio_descricao (str): descrever cardapio_descricao.
        dia_da_semana (str): descrever dia_da_semana.
        turno (str): descrever turno.
    """
    
    escola_uuid: UUID = Field(None, description="escola_uuid Documentar")
    cardapio_uuid: UUID = Field(None, description="cardapio_uuid Documentar")
    cardapio_name: str = Field(None, description="cardapio_name Documentar")
    cardapio_descricao: str = Field(None, description="cardapio_descricao Documentar")
    dia_da_semana: str = Field(None, description="dia_da_semana Documentar")
    turno: str = Field(None, description="turno Documentar")
    
    #     validate_escola_uuid= validator("escola_uuid", allow_reuse=True)(...)
    #     validate_cardapio_uuid= validator("cardapio_uuid", allow_reuse=True)(...)
    #     validate_cardapio_name= validator("cardapio_name", allow_reuse=True)(...)
    #     validate_cardapio_descricao= validator("cardapio_descricao", allow_reuse=True)(...)
    #     validate_dia_da_semana= validator("dia_da_semana", allow_reuse=True)(...)
    #     validate_turno= validator("turno", allow_reuse=True)(...)

    @model_validator(mode="before")
    def validators_cardapio_escola(self) -> "PostCardapioEscola":
        try:
            False
            pass
            return self
        except Exception as e:
            raise error.custom_HTTPException(e)

    class Config:
        json_schema_extra = {
            "examples": [
                {
                    "escola_uuid": "9162bad7-fa0c-44c2-9e47-ce8887994f9b",
                    "cardapio_uuid": "32fde14b-78fb-46a9-ba70-8f2e0452e0fc",
                    "cardapio_name": "VUEsmug",
                    "cardapio_descricao": "CyVDIuO",
                    "dia_da_semana": "IeNUATCqinybLRNwibp",
                    "turno": "QJmCNZHEAOU",
                    "uuid": "b5c234d7-01b0-4e97-8faf-df48bdbf71eb",
                    "created_at": "2021-11-26 11:17:57",
                    "updated_at": "2004-02-15 11:14:22",
                }
            ]
        }

    @classmethod
    def as_form(
        cls,
        escola_uuid: UUID = Form(None, description="escola_uuid Documentar"),
        cardapio_uuid: UUID = Form(None, description="cardapio_uuid Documentar"),
        cardapio_name: str = Form(None, description="cardapio_name Documentar"),
        cardapio_descricao: str = Form(None, description="cardapio_descricao Documentar"),
        dia_da_semana: str = Form(None, description="dia_da_semana Documentar"),
        turno: str = Form(None, description="turno Documentar"),
        uuid: UUID = Form(..., description="uuid Documentar"),
        created_at: datetime = Form(..., description="created_at Documentar"),
        updated_at: datetime = Form(None, description="updated_at Documentar"),
    ):
        return cls(
            escola_uuid=escola_uuid,
            cardapio_uuid=cardapio_uuid,
            cardapio_name=cardapio_name,
            cardapio_descricao=cardapio_descricao,
            dia_da_semana=dia_da_semana,
            turno=turno,
            uuid=uuid,
            created_at=created_at,
            updated_at=updated_at,
        )


class GetCardapioEscola(BaseModel):
    """__summary__

    Attributes:
        escola_uuid (UUID): descrever escola_uuid.
        cardapio_uuid (UUID): descrever cardapio_uuid.
        cardapio_name (str): descrever cardapio_name.
        cardapio_descricao (str): descrever cardapio_descricao.
        dia_da_semana (str): descrever dia_da_semana.
        turno (str): descrever turno.
        uuid (UUID): descrever uuid.
        created_at (datetime): descrever created_at.
        updated_at (datetime): descrever updated_at.
    """
    
    escola_uuid: UUID | None = Field(None, description="escola_uuid Documentar")
    cardapio_uuid: UUID | None = Field(None, description="cardapio_uuid Documentar")
    cardapio_name: str | None = Field(None, description="cardapio_name Documentar")
    cardapio_descricao: str | None = Field(None, description="cardapio_descricao Documentar")
    dia_da_semana: str | None = Field(None, description="dia_da_semana Documentar")
    turno: str | None = Field(None, description="turno Documentar")
    uuid: UUID = Field(..., description="uuid Documentar")
    created_at: datetime = Field(..., description="created_at Documentar")
    updated_at: datetime | None = Field(None, description="updated_at Documentar")
    
    class Config:
        from_attributes = True


class PutCardapioEscola(BaseModel):
    """__summary__

    Attributes:
        escola_uuid (UUID): descrever escola_uuid.
        cardapio_uuid (UUID): descrever cardapio_uuid.
        cardapio_name (str): descrever cardapio_name.
        cardapio_descricao (str): descrever cardapio_descricao.
        dia_da_semana (str): descrever dia_da_semana.
        turno (str): descrever turno.
    """
    
    escola_uuid: UUID = Field(None, description="escola_uuid Documentar")
    cardapio_uuid: UUID = Field(None, description="cardapio_uuid Documentar")
    cardapio_name: str = Field(None, description="cardapio_name Documentar")
    cardapio_descricao: str = Field(None, description="cardapio_descricao Documentar")
    dia_da_semana: str = Field(None, description="dia_da_semana Documentar")
    turno: str = Field(None, description="turno Documentar")