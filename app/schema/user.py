from datetime import datetime
from uuid import UUID

from fastapi import Form
from pydantic import BaseModel, Field, model_validator, validator

from app import error, models, util

# from .user_role_schema import GetUserRole


__all__ = [
    "PostUser",
    "GetUser",
    "PutUser",
]


class PostUser(BaseModel):
    """__summary__

    Attributes:
        username (str): descrever username.
        email (str): descrever email.
        password (bytes): descrever password.
        active (bool): descrever active.
    """

    username: str = Field(..., description="username Documentar")
    email: str = Field(..., description="email Documentar")
    password: bytes = Field(..., description="password Documentar")
    active: bool = Field(None, description="active Documentar")

    #     validate_username= validator("username", allow_reuse=True)(...)
    #     validate_email= validator("email", allow_reuse=True)(...)
    #     validate_password= validator("password", allow_reuse=True)(...)
    #     validate_active= validator("active", allow_reuse=True)(...)

    @model_validator(mode="before")
    def validators_user(self) -> "PostUser":
        try:
            if not "username" in self:
                raise error.CustomException(
                    422,
                    "É necessário informar o username para prosseguir.",
                )
            if models.Usuario.get("username", self["username"]):
                raise error.CustomException(
                    422,
                    f"'{self['username']}' já está cadastrado.",
                )
            if not "email" in self:
                raise error.CustomException(
                    422,
                    "É necessário informar o email para prosseguir.",
                )
            if models.Usuario.get("email", self["email"]):
                raise error.CustomException(
                    422,
                    f"'{self['email']}' já está cadastrado.",
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
                    "username": "Sra. Ana Lívia Jesus",
                    "email": "barbaramendes@example.net",
                    "password": "nNTVwacQvkUCeuVSjhZN",
                    "active": "False",
                    "uuid": "9ff9c363-2bb1-47cc-a91e-e89ad2cf2ed3",
                    "created_at": "2003-01-06 09:24:46",
                    "updated_at": "2005-01-18 20:17:09",
                }
            ]
        }

    @classmethod
    def as_form(
        cls,
        username: str = Form(..., description="username Documentar"),
        email: str = Form(..., description="email Documentar"),
        password: bytes = Form(..., description="password Documentar"),
        active: bool = Form(None, description="active Documentar"),
        uuid: UUID = Form(..., description="uuid Documentar"),
        created_at: datetime = Form(..., description="created_at Documentar"),
        updated_at: datetime = Form(None, description="updated_at Documentar"),
    ):
        return cls(
            username=username,
            email=email,
            password=password,
            active=active,
            uuid=uuid,
            created_at=created_at,
            updated_at=updated_at,
        )


class GetUser(BaseModel):
    """__summary__

    Attributes:
        username (str): descrever username.
        email (str): descrever email.
        active (bool): descrever active.
        uuid (UUID): descrever uuid.
        created_at (datetime): descrever created_at.
        updated_at (datetime): descrever updated_at.
    """

    username: str = Field(..., description="username Documentar")
    email: str = Field(..., description="email Documentar")
    active: bool | None = Field(None, description="active Documentar")
    uuid: UUID = Field(..., description="uuid Documentar")
    created_at: datetime = Field(..., description="created_at Documentar")
    updated_at: datetime | None = Field(
        None, description="updated_at Documentar"
    )
    #    user_roles: list[GetUserRole | None]

    class Config:
        from_attributes = True


class PutUser(BaseModel):
    """__summary__

    Attributes:
        username (str): descrever username.
        email (str): descrever email.
        password (bytes): descrever password.
        active (bool): descrever active.
    """

    username: str = Field(None, description="username Documentar")
    email: str = Field(None, description="email Documentar")
    password: bytes = Field(None, description="password Documentar")
    active: bool = Field(None, description="active Documentar")
