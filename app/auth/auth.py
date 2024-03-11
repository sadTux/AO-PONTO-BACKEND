import datetime
import logging
from typing import Optional, Union

import jwt
from fastapi import Header

from app import core, error, models

__all__ = ["Key", "encode_token", "decode_token"]


def validate_token(token: str) -> str:
    print(token)
    if not token or not "Bearer" in token:
        raise error.CustomException(
            status_code=401, detail="Desculpe, você não tem permissão."
        )
    token_parts = token.split(" ")
    if len(token_parts) != 2:
        raise error.CustomException(
            status_code=401, detail="Desculpe, você não tem permissão."
        )
    return token_parts[1]


def get_user_from_payload(payload: dict) -> models.Usuario:
    user_uuid = payload["sub"].get("user_uuid")
    print(user_uuid)
    if not user_uuid:
        raise error.CustomException(
            status_code=401, detail="Desculpe, você não tem permissão."
        )
    user = models.Usuario.get("uuid", user_uuid)
    if not user:
        raise error.CustomException(
            status_code=401, detail="Desculpe, usuário não encontrado."
        )
    if not user.active:
        raise error.CustomException(
            status_code=401, detail="Desculpe, usuário desativado ou excluído."
        )
    return user


def decode_token(token: str, key: Union[int, None] = None) -> dict:
    try:
        token = validate_token(token)
        print(token)
        payload = jwt.decode(
            token, core.settings.SECRET_KEY, algorithms="HS256"
        )
        print(payload["sub"])
        if "user_uuid" in payload["sub"]:
            user = get_user_from_payload(payload)
        if key and key not in payload["sub"].get("key", []):
            raise error.CustomException(
                status_code=401, detail="Desculpe, você não tem permissão."
            )
        return payload["sub"]
    except Exception as e:
        raise error.custom_HTTPException(e)


def encode_token(sub, exp):
    """
    Codifica um token JWT.

    Args:
        sub (Any): O assunto do token.
        exp (Union[int, float]): O tempo de expiração do token em minutos.

    Returns:
        str: O token JWT codificado.
    """
    try:
        payload = {
            "exp": datetime.datetime.utcnow()
            + datetime.timedelta(minutes=exp),
            "iat": datetime.datetime.utcnow(),
            "sub": sub,
        }
        result = f"Bearer {jwt.encode(payload, core.settings.SECRET_KEY, algorithm='HS256')}"
        return result
    except Exception as e:
        raise error.custom_HTTPException(e)


class Key:
    # vefifica se o usuario tem o nivel de permissao Maximo N5
    async def n5(
        token: Optional[str] = Header(
            None, description="Token OAuth2 'Bearer token'"
        )
    ):
        payload = decode_token(token, 5)
        return payload

    # vefifica se o usuario tem o nivel de permissao N4
    async def n4(
        token: Optional[str] = Header(
            None, description="Token OAuth2 'Bearer token'"
        )
    ):
        payload = decode_token(token, 4)
        return payload

    # vefifica se o usuario tem o nivel de permissao N3
    async def n3(
        token: Optional[str] = Header(
            None, description="Token OAuth2 'Bearer token'"
        )
    ):
        payload = decode_token(token, 3)
        return payload

    # vefifica se o usuario tem o nivel de permissao N2
    async def n2(
        token: Optional[str] = Header(
            None, description="Token OAuth2 'Bearer token'"
        )
    ):
        payload = decode_token(token, 2)
        if not models.Usuario.exist("uuid", payload["user_uuid"]):
            raise error.CustomException(
                status_code=401, detail="Usuario nao encontrado"
            )
        return payload

    # vefifica se o usuario tem o nivel de permissao minima N1
    async def n1(
        token: Optional[str] = Header(
            None, description="Token OAuth2 **'Bearer token'**"
        )
    ):

        payload = decode_token(token)
        return payload

    async def n0():
        return
