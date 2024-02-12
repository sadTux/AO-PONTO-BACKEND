from datetime import datetime
from uuid import UUID

from fastapi import Form
from pydantic import BaseModel, Field, validator, model_validator

from app import error, models, util




__all__ = [
    "PostFrequencias",
    "GetFrequencias",
    "PutFrequencias",
]


class PostFrequencias(BaseModel):
    """__summary__

    Attributes:
        aluno_turmas_uuid (UUID): descrever aluno_turmas_uuid.
        chamada (bool): descrever chamada.
        data (int): descrever data.
    """
    
    aluno_turmas_uuid: UUID = Field(..., description="aluno_turmas_uuid Documentar")
    chamada: bool = Field(None, description="chamada Documentar")
    data: int = Field(None, description="data Documentar")
    
    #     validate_aluno_turmas_uuid= validator("aluno_turmas_uuid", allow_reuse=True)(...)
    #     validate_chamada= validator("chamada", allow_reuse=True)(...)
    #     validate_data= validator("data", allow_reuse=True)(...)

    @model_validator(mode="before")
    def validators_frequencias(self) -> "PostFrequencias":
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
                    "aluno_turmas_uuid": "9b2eeaf8-9f5b-4051-9013-e9b708bc73a5",
                    "chamada": "False",
                    "data": "396",
                    "uuid": "41ca8c3e-f8b9-4b3f-b368-ed7930d1400d",
                    "created_at": "2018-08-08 04:46:16",
                    "updated_at": "2006-03-07 04:08:48",
                }
            ]
        }

    @classmethod
    def as_form(
        cls,
        aluno_turmas_uuid: UUID = Form(..., description="aluno_turmas_uuid Documentar"),
        chamada: bool = Form(None, description="chamada Documentar"),
        data: int = Form(None, description="data Documentar"),
        uuid: UUID = Form(..., description="uuid Documentar"),
        created_at: datetime = Form(..., description="created_at Documentar"),
        updated_at: datetime = Form(None, description="updated_at Documentar"),
    ):
        return cls(
            aluno_turmas_uuid=aluno_turmas_uuid,
            chamada=chamada,
            data=data,
            uuid=uuid,
            created_at=created_at,
            updated_at=updated_at,
        )


class GetFrequencias(BaseModel):
    """__summary__

    Attributes:
        aluno_turmas_uuid (UUID): descrever aluno_turmas_uuid.
        chamada (bool): descrever chamada.
        data (int): descrever data.
        uuid (UUID): descrever uuid.
        created_at (datetime): descrever created_at.
        updated_at (datetime): descrever updated_at.
    """
    
    aluno_turmas_uuid: UUID = Field(..., description="aluno_turmas_uuid Documentar")
    chamada: bool | None = Field(None, description="chamada Documentar")
    data: int | None = Field(None, description="data Documentar")
    uuid: UUID = Field(..., description="uuid Documentar")
    created_at: datetime = Field(..., description="created_at Documentar")
    updated_at: datetime | None = Field(None, description="updated_at Documentar")
    
    class Config:
        from_attributes = True


class PutFrequencias(BaseModel):
    """__summary__

    Attributes:
        aluno_turmas_uuid (UUID): descrever aluno_turmas_uuid.
        chamada (bool): descrever chamada.
        data (int): descrever data.
    """
    
    aluno_turmas_uuid: UUID = Field(None, description="aluno_turmas_uuid Documentar")
    chamada: bool = Field(None, description="chamada Documentar")
    data: int = Field(None, description="data Documentar")