from datetime import date, datetime
from uuid import UUID

from fastapi import File, Form, UploadFile
from pydantic import BaseModel, Field, validator

from app import db, error, models, util

# from .role_schema import GetRole


__all__ = [
    "PostUserRole",
    "GetUserRole",
    "PutUserRole",
]


class PostUserRole(BaseModel):
    """_summary_

    Attributes:
        user_uuid (UUID): descrever user_uuid.
        role_uuid (UUID): descrever role_uuid.

    """

    user_uuid: UUID | None = Field(None, description="User_uuid Documentar")
    role_uuid: UUID | None = Field(None, description="Role_uuid Documentar")

    #     validate_user_uuid= validator("user_uuid", allow_reuse=True)(...)
    #     validate_role_uuid= validator("role_uuid", allow_reuse=True)(...)

    class Config:
        json_schema_extra = {
            "examples": [
                {
                    "user_uuid": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
                    "role_uuid": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
                }
            ]
        }

    @classmethod
    def as_form(
        cls,
        user_uuid: UUID
        | None = Form(None, description="User_uuid Documentar"),
        role_uuid: UUID
        | None = Form(None, description="Role_uuid Documentar"),
    ):
        return cls(
            user_uuid=user_uuid,
            role_uuid=role_uuid,
        )


class GetUserRole(BaseModel):
    """_summary_

    Attributes:
        user_uuid (UUID): descrever user_uuid.
        role_uuid (UUID): descrever role_uuid.
        uuid (UUID): descrever uuid.
        created_at (datetime): descrever created_at.
        updated_at (datetime): descrever updated_at.

    """

    user_uuid: UUID | None = Field(None, description="User_uuid Documentar")
    role_uuid: UUID | None = Field(None, description="Role_uuid Documentar")
    uuid: UUID = Field(..., description="Uuid Documentar")
    created_at: datetime = Field(..., description="Created_at Documentar")
    updated_at: datetime | None = Field(
        None, description="Updated_at Documentar"
    )

    #    role: list[GetRole | None]

    class Config:
        from_attributes = True


class PutUserRole(BaseModel):
    """_summary_

    Attributes:
        user_uuid (UUID): descrever user_uuid.
        role_uuid (UUID): descrever role_uuid.

    """

    user_uuid: UUID | None = Field(None, description="User_uuid Documentar")
    role_uuid: UUID | None = Field(None, description="Role_uuid Documentar")

    #     validate_user_uuid= validator("user_uuid", allow_reuse=True)(...)
    #     validate_role_uuid= validator("role_uuid", allow_reuse=True)(...)

    @classmethod
    def as_form(
        cls,
        user_uuid: UUID
        | None = Form(None, description="User_uuid Documentar"),
        role_uuid: UUID
        | None = Form(None, description="Role_uuid Documentar"),
    ):
        return cls(
            user_uuid=user_uuid,
            role_uuid=role_uuid,
        )
