from datetime import datetime
from uuid import UUID

from fastapi import Form
from pydantic import BaseModel, Field, validator, model_validator

from app import error, models, util




__all__ = [
    "PostDisciplinas",
    "GetDisciplinas",
    "PutDisciplinas",
]


class PostDisciplinas(BaseModel):
    """__summary__

    Attributes:
        name (str): descrever name.
    """
    
    name: str = Field(None, description="name Documentar")
    
    #     validate_name= validator("name", allow_reuse=True)(...)

    @model_validator(mode="before")
    def validators_disciplinas(self) -> "PostDisciplinas":
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
                    "name": "Enrico Novaes",
                    "uuid": "654f458f-a3bf-4452-84dd-3f5f554e5a14",
                    "created_at": "2011-06-06 10:23:44",
                    "updated_at": "2016-05-06 08:12:21",
                }
            ]
        }

    @classmethod
    def as_form(
        cls,
        name: str = Form(None, description="name Documentar"),
        uuid: UUID = Form(..., description="uuid Documentar"),
        created_at: datetime = Form(..., description="created_at Documentar"),
        updated_at: datetime = Form(None, description="updated_at Documentar"),
    ):
        return cls(
            name=name,
            uuid=uuid,
            created_at=created_at,
            updated_at=updated_at,
        )


class GetDisciplinas(BaseModel):
    """__summary__

    Attributes:
        name (str): descrever name.
        uuid (UUID): descrever uuid.
        created_at (datetime): descrever created_at.
        updated_at (datetime): descrever updated_at.
    """
    
    name: str | None = Field(None, description="name Documentar")
    uuid: UUID = Field(..., description="uuid Documentar")
    created_at: datetime = Field(..., description="created_at Documentar")
    updated_at: datetime | None = Field(None, description="updated_at Documentar")
    
    class Config:
        from_attributes = True


class PutDisciplinas(BaseModel):
    """__summary__

    Attributes:
        name (str): descrever name.
    """
    
    name: str = Field(None, description="name Documentar")