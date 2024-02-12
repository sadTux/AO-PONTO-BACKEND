from datetime import datetime
from uuid import UUID

from fastapi import Form
from pydantic import BaseModel, Field, validator, model_validator

from app import error, models, util




__all__ = [
    "PostEscolas",
    "GetEscolas",
    "PutEscolas",
]


class PostEscolas(BaseModel):
    """__summary__

    Attributes:
        nome (str): descrever nome.
        inep_codigo (str): descrever inep_codigo.
        uf (str): descrever uf.
        municipio (str): descrever municipio.
        cep (str): descrever cep.
        endereco (str): descrever endereco.
        categoria_administrativa (str): descrever categoria_administrativa.
        etapa_ensino (str): descrever etapa_ensino.
    """
    
    nome: str = Field(None, description="nome Documentar")
    inep_codigo: str = Field(None, description="inep_codigo Documentar")
    uf: str = Field(None, description="uf Documentar")
    municipio: str = Field(None, description="municipio Documentar")
    cep: str = Field(None, description="cep Documentar")
    endereco: str = Field(None, description="endereco Documentar")
    categoria_administrativa: str = Field(None, description="categoria_administrativa Documentar")
    etapa_ensino: str = Field(None, description="etapa_ensino Documentar")
    
    #     validate_nome= validator("nome", allow_reuse=True)(...)
    #     validate_inep_codigo= validator("inep_codigo", allow_reuse=True)(...)
    #     validate_uf= validator("uf", allow_reuse=True)(...)
    #     validate_municipio= validator("municipio", allow_reuse=True)(...)
    #     validate_cep= validator("cep", allow_reuse=True)(...)
    #     validate_endereco= validator("endereco", allow_reuse=True)(...)
    #     validate_categoria_administrativa= validator("categoria_administrativa", allow_reuse=True)(...)
    #     validate_etapa_ensino= validator("etapa_ensino", allow_reuse=True)(...)

    @model_validator(mode="before")
    def validators_escolas(self) -> "PostEscolas":
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
                    "nome": "IXfztJeiLFF",
                    "inep_codigo": "csWGYg",
                    "uf": "xEsBxBn",
                    "municipio": "sDlWmdsqAlJVwLFRXX",
                    "cep": "UQsFKAAgCrAIOArfCal",
                    "endereco": "zHQWViwhWlJrVC",
                    "categoria_administrativa": "C",
                    "etapa_ensino": "SvehdkNkRMIqf",
                    "uuid": "4036e7c4-4db9-4566-9a48-65c7a8f8c884",
                    "created_at": "2013-08-08 08:35:10",
                    "updated_at": "2022-05-25 00:51:43",
                }
            ]
        }

    @classmethod
    def as_form(
        cls,
        nome: str = Form(None, description="nome Documentar"),
        inep_codigo: str = Form(None, description="inep_codigo Documentar"),
        uf: str = Form(None, description="uf Documentar"),
        municipio: str = Form(None, description="municipio Documentar"),
        cep: str = Form(None, description="cep Documentar"),
        endereco: str = Form(None, description="endereco Documentar"),
        categoria_administrativa: str = Form(None, description="categoria_administrativa Documentar"),
        etapa_ensino: str = Form(None, description="etapa_ensino Documentar"),
        uuid: UUID = Form(..., description="uuid Documentar"),
        created_at: datetime = Form(..., description="created_at Documentar"),
        updated_at: datetime = Form(None, description="updated_at Documentar"),
    ):
        return cls(
            nome=nome,
            inep_codigo=inep_codigo,
            uf=uf,
            municipio=municipio,
            cep=cep,
            endereco=endereco,
            categoria_administrativa=categoria_administrativa,
            etapa_ensino=etapa_ensino,
            uuid=uuid,
            created_at=created_at,
            updated_at=updated_at,
        )


class GetEscolas(BaseModel):
    """__summary__

    Attributes:
        nome (str): descrever nome.
        inep_codigo (str): descrever inep_codigo.
        uf (str): descrever uf.
        municipio (str): descrever municipio.
        cep (str): descrever cep.
        endereco (str): descrever endereco.
        categoria_administrativa (str): descrever categoria_administrativa.
        etapa_ensino (str): descrever etapa_ensino.
        uuid (UUID): descrever uuid.
        created_at (datetime): descrever created_at.
        updated_at (datetime): descrever updated_at.
    """
    
    nome: str | None = Field(None, description="nome Documentar")
    inep_codigo: str | None = Field(None, description="inep_codigo Documentar")
    uf: str | None = Field(None, description="uf Documentar")
    municipio: str | None = Field(None, description="municipio Documentar")
    cep: str | None = Field(None, description="cep Documentar")
    endereco: str | None = Field(None, description="endereco Documentar")
    categoria_administrativa: str | None = Field(None, description="categoria_administrativa Documentar")
    etapa_ensino: str | None = Field(None, description="etapa_ensino Documentar")
    uuid: UUID = Field(..., description="uuid Documentar")
    created_at: datetime = Field(..., description="created_at Documentar")
    updated_at: datetime | None = Field(None, description="updated_at Documentar")
    
    class Config:
        from_attributes = True


class PutEscolas(BaseModel):
    """__summary__

    Attributes:
        nome (str): descrever nome.
        inep_codigo (str): descrever inep_codigo.
        uf (str): descrever uf.
        municipio (str): descrever municipio.
        cep (str): descrever cep.
        endereco (str): descrever endereco.
        categoria_administrativa (str): descrever categoria_administrativa.
        etapa_ensino (str): descrever etapa_ensino.
    """
    
    nome: str = Field(None, description="nome Documentar")
    inep_codigo: str = Field(None, description="inep_codigo Documentar")
    uf: str = Field(None, description="uf Documentar")
    municipio: str = Field(None, description="municipio Documentar")
    cep: str = Field(None, description="cep Documentar")
    endereco: str = Field(None, description="endereco Documentar")
    categoria_administrativa: str = Field(None, description="categoria_administrativa Documentar")
    etapa_ensino: str = Field(None, description="etapa_ensino Documentar")