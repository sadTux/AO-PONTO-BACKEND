from datetime import date, datetime
from uuid import UUID

from fastapi import File, Form, UploadFile
from pydantic import BaseModel, Field, validator

from app import db, error, models, util

# from .user_role_schema import GetUserRole


__all__ = [
    "PostUser",
    "GetUser",
    "PutUser",
]


class PostUser(BaseModel):
    """_summary_

    Attributes:
        username (str): descrever username.
        email (str): descrever email.
        password (bytes): descrever password.
        active (bool): descrever active.

    """

    username: str = Field(
        ..., description="Username Documentar", max_length=255
    )
    email: str = Field(..., description="Email Documentar", max_length=255)
    password: bytes = Field(..., description="Password Documentar")
    active: bool = Field(None, description="Active Documentar")

    #     validate_username= validator("username", allow_reuse=True)(...)
    #     validate_email= validator("email", allow_reuse=True)(...)
    validate_password = validator("password", allow_reuse=True)(
        util.normalize_password
    )
    #     validate_active= validator("active", allow_reuse=True)(...)

    @validator(
        "username",
    )
    def _validate_username(cls, value):
        try:
            _db = db.SessionLocal()
            if not value:
                return value
            value = util.normalize_lower(value)
            if models.Usuario.get("username", value):
                raise error.CustomException(422, f"'{value}' ja Cadastrado")
            return value
        except Exception as e:
            error.custom_HTTPException(e)
        finally:
            _db.close()

    @validator(
        "email",
    )
    def _validate_email(cls, value):
        try:
            _db = db.SessionLocal()
            if not value:
                return value
            value = util.normalize_lower(value)
            if models.Usuario.get("email", value):
                raise error.CustomException(422, f"'{value}' ja Cadastrado")
            return value
        except Exception as e:
            error.custom_HTTPException(e)
        finally:
            _db.close()

    class Config:
        json_schema_extra = {
            "examples": [
                {
                    "username": "string",
                    "email": "string",
                    "password": "bytes",
                    "active": True,
                }
            ]
        }

    @classmethod
    def as_form(
        cls,
        username: str = Form(
            ..., description="Username Documentar", max_length=255
        ),
        email: str = Form(..., description="Email Documentar", max_length=255),
        password: bytes = Form(..., description="Password Documentar"),
        active: bool | None = Form(None, description="Active Documentar"),
    ):
        return cls(
            username=username,
            email=email,
            password=password,
            active=active,
        )


class GetUser(BaseModel):
    """_summary_

    Attributes:
        username (str): descrever username.
        email (str): descrever email.
        active (bool): descrever active.
        uuid (UUID): descrever uuid.
        created_at (datetime): descrever created_at.
        updated_at (datetime): descrever updated_at.

    """

    username: str = Field(
        ..., description="Username Documentar", max_length=255
    )
    email: str = Field(..., description="Email Documentar", max_length=255)
    active: bool | None = Field(None, description="Active Documentar")
    uuid: UUID = Field(..., description="Uuid Documentar")
    created_at: datetime = Field(..., description="Created_at Documentar")
    updated_at: datetime | None = Field(
        None, description="Updated_at Documentar"
    )

    #    user_roles: list[GetUserRole | None]

    class Config:
        from_attributes = True


class PutUser(BaseModel):
    """_summary_

    Attributes:
        username (str): descrever username.
        email (str): descrever email.
        password (bytes): descrever password.
        active (bool): descrever active.

    """

    username: str | None = Field(
        None, description="Username Documentar", max_length=255
    )
    email: str | None = Field(
        None, description="Email Documentar", max_length=255
    )
    password: bytes | None = Field(None, description="Password Documentar")
    active: bool | None = Field(None, description="Active Documentar")

    #     validate_username= validator("username", allow_reuse=True)(...)
    #     validate_email= validator("email", allow_reuse=True)(...)
    validate_password = validator("password", allow_reuse=True)(
        util.normalize_password
    )
    #     validate_active= validator("active", allow_reuse=True)(...)

    @classmethod
    def as_form(
        cls,
        username: str
        | None = Form(None, description="Username Documentar", max_length=255),
        email: str
        | None = Form(None, description="Email Documentar", max_length=255),
        password: bytes | None = Form(None, description="Password Documentar"),
        active: bool | None = Form(None, description="Active Documentar"),
    ):
        return cls(
            username=username,
            email=email,
            password=password,
            active=active,
        )
