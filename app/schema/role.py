from datetime import datetime
from uuid import UUID

from fastapi import Form
from pydantic import BaseModel, Field, model_validator, validator

from app import error, models, util

__all__ = [
    "PostRole",
    "GetRole",
    "PutRole",
]


class PostRole(BaseModel):
    """__summary__

    Attributes:
        name (str): descrever name.
        access_level (int): descrever access_level.
        description (str): descrever description.
    """

    name: str = Field(..., description="name Documentar")
    access_level: int = Field(..., description="access_level Documentar")
    description: str = Field(None, description="description Documentar")

    #     validate_name= validator("name", allow_reuse=True)(...)
    #     validate_access_level= validator("access_level", allow_reuse=True)(...)
    #     validate_description= validator("description", allow_reuse=True)(...)

    @model_validator(mode="before")
    def validators_role(self) -> "PostRole":
        try:
            if not "name" in self:
                raise error.CustomException(
                    422,
                    "É necessário informar o name para prosseguir.",
                )
            if models.Role.get("name", self["name"]):
                raise error.CustomException(
                    422,
                    f"'{self['name']}' já está cadastrado.",
                )
            False
            pass
            return self
        except Exception as e:
            raise error.custom_HTTPException(e)

    class Config:
        json_schema_extra = {
            "examples": [
                {
                    "name": "Lucas Barros",
                    "access_level": "10",
                    "description": "tgsRnpgJmHtMyqXSmMbLaDdlmphswvZNIIBhqHuonjMzHQFnpVXijSPSTwRGsJmmMI",
                    "uuid": "fe40ef9c-8800-4688-bc0a-7327e6c6b63d",
                    "created_at": "2021-06-13 23:00:57",
                    "updated_at": "2020-10-18 13:27:08",
                }
            ]
        }

    @classmethod
    def as_form(
        cls,
        name: str = Form(..., description="name Documentar"),
        access_level: int = Form(..., description="access_level Documentar"),
        description: str = Form(None, description="description Documentar"),
        uuid: UUID = Form(..., description="uuid Documentar"),
        created_at: datetime = Form(..., description="created_at Documentar"),
        updated_at: datetime = Form(None, description="updated_at Documentar"),
    ):
        return cls(
            name=name,
            access_level=access_level,
            description=description,
            uuid=uuid,
            created_at=created_at,
            updated_at=updated_at,
        )


class GetRole(BaseModel):
    """__summary__

    Attributes:
        name (str): descrever name.
        access_level (int): descrever access_level.
        description (str): descrever description.
        uuid (UUID): descrever uuid.
        created_at (datetime): descrever created_at.
        updated_at (datetime): descrever updated_at.
    """

    name: str = Field(..., description="name Documentar")
    access_level: int = Field(..., description="access_level Documentar")
    description: str | None = Field(None, description="description Documentar")
    uuid: UUID = Field(..., description="uuid Documentar")
    created_at: datetime = Field(..., description="created_at Documentar")
    updated_at: datetime | None = Field(
        None, description="updated_at Documentar"
    )

    class Config:
        from_attributes = True


class PutRole(BaseModel):
    """__summary__

    Attributes:
        name (str): descrever name.
        access_level (int): descrever access_level.
        description (str): descrever description.
    """

    name: str = Field(None, description="name Documentar")
    access_level: int = Field(None, description="access_level Documentar")
    description: str = Field(None, description="description Documentar")
