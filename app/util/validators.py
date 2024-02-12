import re
from itertools import cycle

from email_validator import EmailNotValidError, validate_email

from app import core, error

__all__ = [
    "validate_cpf",
    "normalize_capitalize",
    "normalize_lower",
    "normalize_password",
    "normalize_telefone",
    "validate_cnpj",
    "validate_cnpj_cpf",
    "normalize_email",
    "normalize_uper",
]


# validador de CPF
def validate_cpf(key: str):
    try:
        if not key:
            return key
        if len(key) != 11:
            raise error.CustomException(
                422,
                "CPF invalido, O campo deve conter exatamente 11 digitos numericos",
            )

        if key in (c * 11 for c in "1234567890"):
            raise error.CustomException(status_code=422, detail="CPF invalido")

        cpf_reverso = key[::-1]
        for i in range(2, 0, -1):
            cpf_enumerado = enumerate(cpf_reverso[i:], start=2)
            dv_calculado = (
                sum(map(lambda x: int(x[1]) * x[0], cpf_enumerado)) * 10 % 11
            )
        return key
    except Exception as e:
        error.custom_HTTPException(e)


# validador de CNPJ
def validate_cnpj(key: str):
    if not key:
        return key
    if len(key) != 14:
        raise error.CustomException(
            422,
            "CNPJ invalido, O campo deve conter exatamente 14 digitos numericos",
        )

    if key in (c * 14 for c in "1234567890"):
        raise error.CustomException(422, "CNPJ invalido")

    cnpj_r = key[::-1]
    for i in range(2, 0, -1):
        cnpj_enum = zip(cycle(range(2, 10)), cnpj_r[i:])
        dv = sum(map(lambda x: int(x[1]) * x[0], cnpj_enum)) * 10 % 11
    return key


# Valida um dado que pode ser CPF OU CNPJ
def validate_cnpj_cpf(key: str):
    if not key:
        return key
    if len(key) == 11:
        return validate_cnpj(key)
    if len(key) == 14:
        return validate_cpf(key)
    else:
        raise error.CustomException(422, "Deve conter um CPF ou CNPJ valido")


# Aplica Primeria letra maiuscula em uma string
def normalize_capitalize(key: str):
    if not key:
        return key
    key = key.lower()
    return " ".join((word.capitalize()) for word in key.split(" "))


def normalize_uper(key: str):
    if not key:
        return key
    return " ".join((word.upper()) for word in key.split(" "))


def normalize_password(key: bytes):
    if not key:
        return key
    return core.get_password_hash(key)


def normalize_lower(key: str):
    if not key:
        return key
    return " ".join((word.lower()) for word in key.split(" "))


def normalize_telefone(key: str):
    if not key:
        return key
    key = re.sub("[^0-9]+", "", key)
    if len(key) != 13:
        raise error.CustomException(
            status_code=422,
            detail="Formato de telefone invalido, deve conter no minimo 11 e no maximo 13 digitos",
        )
    return key


def normalize_email(key: str) -> str:
    if not key:
        return key
    try:
        valid = validate_email(key)
        key = valid.email
    except EmailNotValidError:
        raise error.CustomException(
            status_code=422,
            detail="Formato de email invalido",
        )
    return key.lower()
