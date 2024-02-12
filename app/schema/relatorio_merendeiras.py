from datetime import datetime, date
from uuid import UUID

from fastapi import Form
from pydantic import BaseModel, Field, validator, model_validator

from app import error, models, util




__all__ = [
    "PostRelatorioMerendeiras",
    "GetRelatorioMerendeiras",
    "PutRelatorioMerendeiras",
]


class PostRelatorioMerendeiras(BaseModel):
    """__summary__

    Attributes:
        escola_uuid (UUID): descrever escola_uuid.
        escola_name (str): descrever escola_name.
        numero_alunos (str): descrever numero_alunos.
        sobra_limpa (str): descrever sobra_limpa.
        sobra_suja (str): descrever sobra_suja.
        data (date): descrever data.
    """
    
    escola_uuid: UUID = Field(None, description="escola_uuid Documentar")
    escola_name: str = Field(None, description="escola_name Documentar")
    numero_alunos: str = Field(None, description="numero_alunos Documentar")
    sobra_limpa: str = Field(None, description="sobra_limpa Documentar")
    sobra_suja: str = Field(None, description="sobra_suja Documentar")
    data: date = Field(None, description="data Documentar")
    
    #     validate_escola_uuid= validator("escola_uuid", allow_reuse=True)(...)
    #     validate_escola_name= validator("escola_name", allow_reuse=True)(...)
    #     validate_numero_alunos= validator("numero_alunos", allow_reuse=True)(...)
    #     validate_sobra_limpa= validator("sobra_limpa", allow_reuse=True)(...)
    #     validate_sobra_suja= validator("sobra_suja", allow_reuse=True)(...)
    #     validate_data= validator("data", allow_reuse=True)(...)

    @model_validator(mode="before")
    def validators_relatorio_merendeiras(self) -> "PostRelatorioMerendeiras":
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
                    "escola_uuid": "3bee0790-b0cb-4aab-a718-e5dc2be6f573",
                    "escola_name": "MQRMH",
                    "numero_alunos": "vnToLDvMblofgLm",
                    "sobra_limpa": "fiVnZdH",
                    "sobra_suja": "j",
                    "data": "2023-05-25",
                    "uuid": "52eff09d-a4c0-4f8e-9c8a-a5eee5230d19",
                    "created_at": "2003-03-29 00:00:44",
                    "updated_at": "2006-03-06 21:01:07",
                }
            ]
        }

    @classmethod
    def as_form(
        cls,
        escola_uuid: UUID = Form(None, description="escola_uuid Documentar"),
        escola_name: str = Form(None, description="escola_name Documentar"),
        numero_alunos: str = Form(None, description="numero_alunos Documentar"),
        sobra_limpa: str = Form(None, description="sobra_limpa Documentar"),
        sobra_suja: str = Form(None, description="sobra_suja Documentar"),
        data: date = Form(None, description="data Documentar"),
        uuid: UUID = Form(..., description="uuid Documentar"),
        created_at: datetime = Form(..., description="created_at Documentar"),
        updated_at: datetime = Form(None, description="updated_at Documentar"),
    ):
        return cls(
            escola_uuid=escola_uuid,
            escola_name=escola_name,
            numero_alunos=numero_alunos,
            sobra_limpa=sobra_limpa,
            sobra_suja=sobra_suja,
            data=data,
            uuid=uuid,
            created_at=created_at,
            updated_at=updated_at,
        )


class GetRelatorioMerendeiras(BaseModel):
    """__summary__

    Attributes:
        escola_uuid (UUID): descrever escola_uuid.
        escola_name (str): descrever escola_name.
        numero_alunos (str): descrever numero_alunos.
        sobra_limpa (str): descrever sobra_limpa.
        sobra_suja (str): descrever sobra_suja.
        data (date): descrever data.
        uuid (UUID): descrever uuid.
        created_at (datetime): descrever created_at.
        updated_at (datetime): descrever updated_at.
    """
    
    escola_uuid: UUID | None = Field(None, description="escola_uuid Documentar")
    escola_name: str | None = Field(None, description="escola_name Documentar")
    numero_alunos: str | None = Field(None, description="numero_alunos Documentar")
    sobra_limpa: str | None = Field(None, description="sobra_limpa Documentar")
    sobra_suja: str | None = Field(None, description="sobra_suja Documentar")
    data: date | None = Field(None, description="data Documentar")
    uuid: UUID = Field(..., description="uuid Documentar")
    created_at: datetime = Field(..., description="created_at Documentar")
    updated_at: datetime | None = Field(None, description="updated_at Documentar")
    
    class Config:
        from_attributes = True


class PutRelatorioMerendeiras(BaseModel):
    """__summary__

    Attributes:
        escola_uuid (UUID): descrever escola_uuid.
        escola_name (str): descrever escola_name.
        numero_alunos (str): descrever numero_alunos.
        sobra_limpa (str): descrever sobra_limpa.
        sobra_suja (str): descrever sobra_suja.
        data (date): descrever data.
    """
    
    escola_uuid: UUID = Field(None, description="escola_uuid Documentar")
    escola_name: str = Field(None, description="escola_name Documentar")
    numero_alunos: str = Field(None, description="numero_alunos Documentar")
    sobra_limpa: str = Field(None, description="sobra_limpa Documentar")
    sobra_suja: str = Field(None, description="sobra_suja Documentar")
    data: date = Field(None, description="data Documentar")