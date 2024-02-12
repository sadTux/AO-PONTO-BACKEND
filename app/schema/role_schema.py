from datetime import date, datetime
from uuid import UUID

from fastapi import File, Form, UploadFile
from pydantic import BaseModel, Field, validator

from app import db, error, models, util

__all__ = [
    "PostRole",
    "GetRole",
    "PutRole",
]


class PostRole(BaseModel):
    """_summary_

    Attributes:
        name (str): descrever name.
        access_level (int): descrever access_level.
        description (str): descrever description.

    """

    name: str = Field(..., description="Name Documentar", max_length=45)
    access_level: int = Field(..., description="Access_level Documentar")
    description: str | None = Field(
        None, description="Description Documentar", max_length=250
    )

    #     validate_name= validator("name", allow_reuse=True)(...)
    #     validate_access_level= validator("access_level", allow_reuse=True)(...)
    #     validate_description= validator("description", allow_reuse=True)(...)

    @validator(
        "name",
    )
    def _validate_name(cls, value):
        try:
            _db = db.SessionLocal()
            if not value:
                return value
            value = util.normalize_lower(value)
            if models.Role.get("name", value):
                raise error.CustomException(422, f"'{value}' ja Cadastrado")
            return value
        except Exception as e:
            error.custom_HTTPException(e)
        finally:
            _db.close()

    class Config:
        json_schema_extra = {
            "examples": [
                {"name": "string", "access_level": 3, "description": "string"}
            ]
        }

    @classmethod
    def as_form(
        cls,
        name: str = Form(..., description="Name Documentar", max_length=45),
        access_level: int = Form(..., description="Access_level Documentar"),
        description: str
        | None = Form(
            None, description="Description Documentar", max_length=250
        ),
    ):
        return cls(
            name=name,
            access_level=access_level,
            description=description,
        )


class GetRole(BaseModel):
    """_summary_

    Attributes:
        name (str): descrever name.
        access_level (int): descrever access_level.
        description (str): descrever description.
        uuid (UUID): descrever uuid.
        created_at (datetime): descrever created_at.
        updated_at (datetime): descrever updated_at.

    """

    name: str = Field(..., description="Name Documentar", max_length=45)
    access_level: int = Field(..., description="Access_level Documentar")
    description: str | None = Field(
        None, description="Description Documentar", max_length=250
    )
    uuid: UUID = Field(..., description="Uuid Documentar")
    created_at: datetime = Field(..., description="Created_at Documentar")
    updated_at: datetime | None = Field(
        None, description="Updated_at Documentar"
    )

    class Config:
        from_attributes = True


class PutRole(BaseModel):
    """_summary_

    Attributes:
        name (str): descrever name.
        access_level (int): descrever access_level.
        description (str): descrever description.

    """

    name: str | None = Field(
        None, description="Name Documentar", max_length=45
    )
    access_level: int | None = Field(
        None, description="Access_level Documentar"
    )
    description: str | None = Field(
        None, description="Description Documentar", max_length=250
    )

    #     validate_name= validator("name", allow_reuse=True)(...)
    #     validate_access_level= validator("access_level", allow_reuse=True)(...)
    #     validate_description= validator("description", allow_reuse=True)(...)

    @classmethod
    def as_form(
        cls,
        name: str
        | None = Form(None, description="Name Documentar", max_length=45),
        access_level: int
        | None = Form(None, description="Access_level Documentar"),
        description: str
        | None = Form(
            None, description="Description Documentar", max_length=250
        ),
    ):
        return cls(
            name=name,
            access_level=access_level,
            description=description,
        )
