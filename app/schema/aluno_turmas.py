from datetime import datetime
from uuid import UUID

from fastapi import Form
from pydantic import BaseModel, Field, validator, model_validator

from app import error, models, util




__all__ = [
    "PostAlunoTurmas",
    "GetAlunoTurmas",
    "PutAlunoTurmas",
]


class PostAlunoTurmas(BaseModel):
    """__summary__

    Attributes:
        aluno_uuid (UUID): descrever aluno_uuid.
        turma_uuid (UUID): descrever turma_uuid.
        turma_name (str): descrever turma_name.
    """
    
    aluno_uuid: UUID = Field(None, description="aluno_uuid Documentar")
    turma_uuid: UUID = Field(None, description="turma_uuid Documentar")
    turma_name: str = Field(None, description="turma_name Documentar")
    
    #     validate_aluno_uuid= validator("aluno_uuid", allow_reuse=True)(...)
    #     validate_turma_uuid= validator("turma_uuid", allow_reuse=True)(...)
    #     validate_turma_name= validator("turma_name", allow_reuse=True)(...)

    @model_validator(mode="before")
    def validators_aluno_turmas(self) -> "PostAlunoTurmas":
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
                    "aluno_uuid": "960da131-b548-41b3-a54a-267ef12a84d5",
                    "turma_uuid": "304af388-31d9-4404-8319-83efeda9c778",
                    "turma_name": "BFuSdVPEWwEVvyCmq",
                    "uuid": "144e6aeb-10b6-4657-866b-1a742606fba0",
                    "created_at": "2020-06-12 19:16:01",
                    "updated_at": "2020-02-18 03:47:19",
                }
            ]
        }

    @classmethod
    def as_form(
        cls,
        aluno_uuid: UUID = Form(None, description="aluno_uuid Documentar"),
        turma_uuid: UUID = Form(None, description="turma_uuid Documentar"),
        turma_name: str = Form(None, description="turma_name Documentar"),
        uuid: UUID = Form(..., description="uuid Documentar"),
        created_at: datetime = Form(..., description="created_at Documentar"),
        updated_at: datetime = Form(None, description="updated_at Documentar"),
    ):
        return cls(
            aluno_uuid=aluno_uuid,
            turma_uuid=turma_uuid,
            turma_name=turma_name,
            uuid=uuid,
            created_at=created_at,
            updated_at=updated_at,
        )


class GetAlunoTurmas(BaseModel):
    """__summary__

    Attributes:
        aluno_uuid (UUID): descrever aluno_uuid.
        turma_uuid (UUID): descrever turma_uuid.
        turma_name (str): descrever turma_name.
        uuid (UUID): descrever uuid.
        created_at (datetime): descrever created_at.
        updated_at (datetime): descrever updated_at.
    """
    
    aluno_uuid: UUID | None = Field(None, description="aluno_uuid Documentar")
    turma_uuid: UUID | None = Field(None, description="turma_uuid Documentar")
    turma_name: str | None = Field(None, description="turma_name Documentar")
    uuid: UUID = Field(..., description="uuid Documentar")
    created_at: datetime = Field(..., description="created_at Documentar")
    updated_at: datetime | None = Field(None, description="updated_at Documentar")
    
    class Config:
        from_attributes = True


class PutAlunoTurmas(BaseModel):
    """__summary__

    Attributes:
        aluno_uuid (UUID): descrever aluno_uuid.
        turma_uuid (UUID): descrever turma_uuid.
        turma_name (str): descrever turma_name.
    """
    
    aluno_uuid: UUID = Field(None, description="aluno_uuid Documentar")
    turma_uuid: UUID = Field(None, description="turma_uuid Documentar")
    turma_name: str = Field(None, description="turma_name Documentar")