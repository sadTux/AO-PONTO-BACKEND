from pydantic import BaseModel, Field, validator

from app import core, util

from .usuario import GetUsuario

# from .user_schema import GetUser


__all__ = [
    "Login",
    "LoginResponse",
    "ForgotPassword",
    "ForgotPasswordResponse",
    "ChangePassword",
]


class Login(BaseModel):
    """Schema utilizado no Login

    Attributes:
        username (str): Nome do Usuario.
        password(str): Senha.
    """

    username: str
    password: str

    validator_normalize_nome = validator("username", allow_reuse=True)(
        util.normalize_lower
    )


class LoginResponse(BaseModel):
    token: str
    user: GetUsuario

    class Config:
        from_attributes = True


class ForgotPassword(BaseModel):
    email: str


class ForgotPasswordResponse(BaseModel):
    token: str

    class Config:
        from_attributes = True


class ChangePassword(BaseModel):
    password: bytes = Field(description="Senha", min_length=6)

    _password_hash = validator("password", allow_reuse=True)(
        core.get_password_hash
    )
