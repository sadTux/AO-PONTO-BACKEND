from datetime import datetime, time, date
from uuid import UUID

from fastapi import Form
from pydantic import BaseModel, Field, validator, model_validator

from app import error, models, util




__all__ = [
    "PostTurmas",
    "GetTurmas",
    "PutTurmas",
]


class PostTurmas(BaseModel):
    """__summary__

    Attributes:
        disciplina (str): descrever disciplina.
        sala (UUID): descrever sala.
        nome_professor (str): descrever nome_professor.
        turno (str): descrever turno.
        horario (time): descrever horario.
        ano (date): descrever ano.
    """
    
    disciplina: str = Field(None, description="disciplina Documentar")
    sala: UUID = Field(None, description="sala Documentar")
    nome_professor: str = Field(None, description="usuário do tipo professor")
    turno: str = Field(None, description="turno Documentar")
    horario: time = Field(None, description="horario Documentar")
    ano: date = Field(None, description="ano Documentar")
    
    #     validate_disciplina= validator("disciplina", allow_reuse=True)(...)
    #     validate_sala= validator("sala", allow_reuse=True)(...)
    #     validate_nome_professor= validator("nome_professor", allow_reuse=True)(...)
    #     validate_turno= validator("turno", allow_reuse=True)(...)
    #     validate_horario= validator("horario", allow_reuse=True)(...)
    #     validate_ano= validator("ano", allow_reuse=True)(...)

    @model_validator(mode="before")
    def validators_turmas(self) -> "PostTurmas":
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
                    "disciplina": "EbKoHEhoPPBfwiWpa",
                    "sala": "bf7bd2a1-09be-4b58-b10d-f74c63b3c972",
                    "nome_professor": "nOoyVChWc",
                    "turno": "UDZZaJeCBEoOri",
                    "horario": "None",
                    "ano": "2023-12-21",
                    "uuid": "99c1c8e2-ede3-458b-ae16-99866a43fcaf",
                    "created_at": "2007-11-20 03:15:24",
                    "updated_at": "2018-11-17 23:01:30",
                }
            ]
        }

    @classmethod
    def as_form(
        cls,
        disciplina: str = Form(None, description="disciplina Documentar"),
        sala: UUID = Form(None, description="sala Documentar"),
        nome_professor: str = Form(None, description="usuário do tipo professor"),
        turno: str = Form(None, description="turno Documentar"),
        horario: time = Form(None, description="horario Documentar"),
        ano: date = Form(None, description="ano Documentar"),
        uuid: UUID = Form(..., description="uuid Documentar"),
        created_at: datetime = Form(..., description="created_at Documentar"),
        updated_at: datetime = Form(None, description="updated_at Documentar"),
    ):
        return cls(
            disciplina=disciplina,
            sala=sala,
            nome_professor=nome_professor,
            turno=turno,
            horario=horario,
            ano=ano,
            uuid=uuid,
            created_at=created_at,
            updated_at=updated_at,
        )


class GetTurmas(BaseModel):
    """__summary__

    Attributes:
        disciplina (str): descrever disciplina.
        sala (UUID): descrever sala.
        nome_professor (str): descrever nome_professor.
        turno (str): descrever turno.
        horario (time): descrever horario.
        ano (date): descrever ano.
        uuid (UUID): descrever uuid.
        created_at (datetime): descrever created_at.
        updated_at (datetime): descrever updated_at.
    """
    
    disciplina: str | None = Field(None, description="disciplina Documentar")
    sala: UUID | None = Field(None, description="sala Documentar")
    nome_professor: str | None = Field(None, description="usuário do tipo professor")
    turno: str | None = Field(None, description="turno Documentar")
    horario: time | None = Field(None, description="horario Documentar")
    ano: date | None = Field(None, description="ano Documentar")
    uuid: UUID = Field(..., description="uuid Documentar")
    created_at: datetime = Field(..., description="created_at Documentar")
    updated_at: datetime | None = Field(None, description="updated_at Documentar")
    
    class Config:
        from_attributes = True


class PutTurmas(BaseModel):
    """__summary__

    Attributes:
        disciplina (str): descrever disciplina.
        sala (UUID): descrever sala.
        nome_professor (str): descrever nome_professor.
        turno (str): descrever turno.
        horario (time): descrever horario.
        ano (date): descrever ano.
    """
    
    disciplina: str = Field(None, description="disciplina Documentar")
    sala: UUID = Field(None, description="sala Documentar")
    nome_professor: str = Field(None, description="usuário do tipo professor")
    turno: str = Field(None, description="turno Documentar")
    horario: time = Field(None, description="horario Documentar")
    ano: date = Field(None, description="ano Documentar")