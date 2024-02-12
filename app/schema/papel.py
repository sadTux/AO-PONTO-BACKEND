from datetime import datetime
from uuid import UUID

from fastapi import Form
from pydantic import BaseModel, Field, validator, model_validator

from app import error, models, util




__all__ = [
    "PostPapel",
    "GetPapel",
    "PutPapel",
]


class PostPapel(BaseModel):
    """__summary__

    Attributes:
        nome (str): descrever nome.
        access_level (int): descrever access_level.
    """
    
    nome: str = Field(None, description="nome Documentar")
    access_level: int = Field(None, description="access_level Documentar")
    
    #     validate_nome= validator("nome", allow_reuse=True)(...)
    #     validate_access_level= validator("access_level", allow_reuse=True)(...)

    @model_validator(mode="before")
    def validators_papel(self) -> "PostPapel":
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
                    "nome": "fEZ",
                    "access_level": "1207",
                    "uuid": "3808c984-7422-4160-83bb-6a7a0dcd5adc",
                    "created_at": "2021-10-23 12:38:00",
                    "updated_at": "2012-05-11 00:01:55",
                }
            ]
        }

    @classmethod
    def as_form(
        cls,
        nome: str = Form(None, description="nome Documentar"),
        access_level: int = Form(None, description="access_level Documentar"),
        uuid: UUID = Form(..., description="uuid Documentar"),
        created_at: datetime = Form(..., description="created_at Documentar"),
        updated_at: datetime = Form(None, description="updated_at Documentar"),
    ):
        return cls(
            nome=nome,
            access_level=access_level,
            uuid=uuid,
            created_at=created_at,
            updated_at=updated_at,
        )


class GetPapel(BaseModel):
    """__summary__

    Attributes:
        nome (str): descrever nome.
        access_level (int): descrever access_level.
        uuid (UUID): descrever uuid.
        created_at (datetime): descrever created_at.
        updated_at (datetime): descrever updated_at.
    """
    
    nome: str | None = Field(None, description="nome Documentar")
    access_level: int | None = Field(None, description="access_level Documentar")
    uuid: UUID = Field(..., description="uuid Documentar")
    created_at: datetime = Field(..., description="created_at Documentar")
    updated_at: datetime | None = Field(None, description="updated_at Documentar")
    
    class Config:
        from_attributes = True


class PutPapel(BaseModel):
    """__summary__

    Attributes:
        nome (str): descrever nome.
        access_level (int): descrever access_level.
    """
    
    nome: str = Field(None, description="nome Documentar")
    access_level: int = Field(None, description="access_level Documentar")