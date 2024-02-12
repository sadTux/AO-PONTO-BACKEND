import logging

import bcrypt

from app import error

__all__ = ["get_password_hash", "verify_password"]


def verify_password(
    plain_password: str | bytes, hashed_password: str | bytes
) -> bool:
    try:
        if str(type(plain_password)) != "<class 'bytes'>":
            plain_password = plain_password.encode()
        if str(type(hashed_password)) != "<class 'bytes'>":
            hashed_password = hashed_password.encode()
        return bcrypt.checkpw(plain_password, hashed_password)
    except Exception as e:
        logging.warning(e) if not hasattr(e, "status_code") else ...
        raise error.CustomException(
            status_code=555,
            detail="Erro Interno API",
        )


def get_password_hash(password: str | bytes) -> bytes:
    try:
        if str(type(password)) != "<class 'bytes'>":
            password = password.encode()
        return bcrypt.hashpw(password, bcrypt.gensalt())
    except Exception as e:
        logging.warning(e) if not hasattr(e, "status_code") else ...
        raise error.CustomException(
            status_code=555,
            detail="Erro Interno API",
        )
