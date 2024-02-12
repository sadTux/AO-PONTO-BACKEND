from datetime import datetime
from uuid import UUID

from fastapi import Form
from pydantic import BaseModel, Field, model_validator, validator

from app import error, models, util

# from .role_schema import GetRole


__all__ = [
    "PostUserRole",
    "GetUserRole",
    "PutUserRole",
]


class PostUserRole(BaseModel):
    """__summary__

    Attributes:
        user_uuid (UUID): descrever user_uuid.
        role_uuid (UUID): descrever role_uuid.
    """

    user_uuid: UUID = Field(None, description="user_uuid Documentar")
    role_uuid: UUID = Field(None, description="role_uuid Documentar")

    #     validate_user_uuid= validator("user_uuid", allow_reuse=True)(...)
    #     validate_role_uuid= validator("role_uuid", allow_reuse=True)(...)

    @model_validator(mode="before")
    def validators_user_role(self) -> "PostUserRole":
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
                    "user_uuid": "8c3e0ae6-a594-4f24-8855-665f115ce8fb",
                    "role_uuid": "6997e814-8ca2-400f-9650-87056260a224",
                    "uuid": "11342579-bf9a-414c-8f2e-422a3631960d",
                    "created_at": "1997-11-12 07:58:08",
                    "updated_at": "2014-07-13 22:09:56",
                }
            ]
        }

    @classmethod
    def as_form(
        cls,
        user_uuid: UUID = Form(None, description="user_uuid Documentar"),
        role_uuid: UUID = Form(None, description="role_uuid Documentar"),
        uuid: UUID = Form(..., description="uuid Documentar"),
        created_at: datetime = Form(..., description="created_at Documentar"),
        updated_at: datetime = Form(None, description="updated_at Documentar"),
    ):
        return cls(
            user_uuid=user_uuid,
            role_uuid=role_uuid,
            uuid=uuid,
            created_at=created_at,
            updated_at=updated_at,
        )


class GetUserRole(BaseModel):
    """__summary__

    Attributes:
        user_uuid (UUID): descrever user_uuid.
        role_uuid (UUID): descrever role_uuid.
        uuid (UUID): descrever uuid.
        created_at (datetime): descrever created_at.
        updated_at (datetime): descrever updated_at.
    """

    user_uuid: UUID | None = Field(None, description="user_uuid Documentar")
    role_uuid: UUID | None = Field(None, description="role_uuid Documentar")
    uuid: UUID = Field(..., description="uuid Documentar")
    created_at: datetime = Field(..., description="created_at Documentar")
    updated_at: datetime | None = Field(
        None, description="updated_at Documentar"
    )
    #    role: list[GetRole | None]

    class Config:
        from_attributes = True


class PutUserRole(BaseModel):
    """__summary__

    Attributes:
        user_uuid (UUID): descrever user_uuid.
        role_uuid (UUID): descrever role_uuid.
    """

    user_uuid: UUID = Field(None, description="user_uuid Documentar")
    role_uuid: UUID = Field(None, description="role_uuid Documentar")
