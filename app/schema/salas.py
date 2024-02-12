from datetime import datetime
from uuid import UUID

from fastapi import Form
from pydantic import BaseModel, Field, validator, model_validator

from app import error, models, util




__all__ = [
    "PostSalas",
    "GetSalas",
    "PutSalas",
]


class PostSalas(BaseModel):
    """__summary__

    Attributes:
        nome (str): descrever nome.
        escola_uuid (UUID): descrever escola_uuid.
    """
    
    nome: str = Field(None, description="nome Documentar")
    escola_uuid: UUID = Field(None, description="escola_uuid Documentar")
    
    #     validate_nome= validator("nome", allow_reuse=True)(...)
    #     validate_escola_uuid= validator("escola_uuid", allow_reuse=True)(...)

    @model_validator(mode="before")
    def validators_salas(self) -> "PostSalas":
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
                    "nome": "GRUMWY",
                    "escola_uuid": "1b1846b8-3d73-423a-bff5-88b7138229e6",
                    "uuid": "cb1c5bd1-9d34-4482-9204-eaa2ec701d6b",
                    "created_at": "2002-11-18 22:00:26",
                    "updated_at": "2017-05-02 06:50:20",
                }
            ]
        }

    @classmethod
    def as_form(
        cls,
        nome: str = Form(None, description="nome Documentar"),
        escola_uuid: UUID = Form(None, description="escola_uuid Documentar"),
        uuid: UUID = Form(..., description="uuid Documentar"),
        created_at: datetime = Form(..., description="created_at Documentar"),
        updated_at: datetime = Form(None, description="updated_at Documentar"),
    ):
        return cls(
            nome=nome,
            escola_uuid=escola_uuid,
            uuid=uuid,
            created_at=created_at,
            updated_at=updated_at,
        )


class GetSalas(BaseModel):
    """__summary__

    Attributes:
        nome (str): descrever nome.
        escola_uuid (UUID): descrever escola_uuid.
        uuid (UUID): descrever uuid.
        created_at (datetime): descrever created_at.
        updated_at (datetime): descrever updated_at.
    """
    
    nome: str | None = Field(None, description="nome Documentar")
    escola_uuid: UUID | None = Field(None, description="escola_uuid Documentar")
    uuid: UUID = Field(..., description="uuid Documentar")
    created_at: datetime = Field(..., description="created_at Documentar")
    updated_at: datetime | None = Field(None, description="updated_at Documentar")
    
    class Config:
        from_attributes = True


class PutSalas(BaseModel):
    """__summary__

    Attributes:
        nome (str): descrever nome.
        escola_uuid (UUID): descrever escola_uuid.
    """
    
    nome: str = Field(None, description="nome Documentar")
    escola_uuid: UUID = Field(None, description="escola_uuid Documentar")