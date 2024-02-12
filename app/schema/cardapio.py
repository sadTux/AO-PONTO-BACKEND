from datetime import datetime
from uuid import UUID

from fastapi import Form
from pydantic import BaseModel, Field, validator, model_validator

from app import error, models, util




__all__ = [
    "PostCardapio",
    "GetCardapio",
    "PutCardapio",
]


class PostCardapio(BaseModel):
    """__summary__

    Attributes:
        nome (str): descrever nome.
        descricao (str): descrever descricao.
    """
    
    nome: str = Field(None, description="nome Documentar")
    descricao: str = Field(None, description="descricao Documentar")
    
    #     validate_nome= validator("nome", allow_reuse=True)(...)
    #     validate_descricao= validator("descricao", allow_reuse=True)(...)

    @model_validator(mode="before")
    def validators_cardapio(self) -> "PostCardapio":
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
                    "nome": "ZgJcTpSsb",
                    "descricao": "jjIfjnLRbvVwg",
                    "uuid": "fdf0e80b-df49-4615-87b2-6e571e4451ae",
                    "created_at": "2022-09-10 00:43:00",
                    "updated_at": "1998-03-25 21:51:18",
                }
            ]
        }

    @classmethod
    def as_form(
        cls,
        nome: str = Form(None, description="nome Documentar"),
        descricao: str = Form(None, description="descricao Documentar"),
        uuid: UUID = Form(..., description="uuid Documentar"),
        created_at: datetime = Form(..., description="created_at Documentar"),
        updated_at: datetime = Form(None, description="updated_at Documentar"),
    ):
        return cls(
            nome=nome,
            descricao=descricao,
            uuid=uuid,
            created_at=created_at,
            updated_at=updated_at,
        )


class GetCardapio(BaseModel):
    """__summary__

    Attributes:
        nome (str): descrever nome.
        descricao (str): descrever descricao.
        uuid (UUID): descrever uuid.
        created_at (datetime): descrever created_at.
        updated_at (datetime): descrever updated_at.
    """
    
    nome: str | None = Field(None, description="nome Documentar")
    descricao: str | None = Field(None, description="descricao Documentar")
    uuid: UUID = Field(..., description="uuid Documentar")
    created_at: datetime = Field(..., description="created_at Documentar")
    updated_at: datetime | None = Field(None, description="updated_at Documentar")
    
    class Config:
        from_attributes = True


class PutCardapio(BaseModel):
    """__summary__

    Attributes:
        nome (str): descrever nome.
        descricao (str): descrever descricao.
    """
    
    nome: str = Field(None, description="nome Documentar")
    descricao: str = Field(None, description="descricao Documentar")