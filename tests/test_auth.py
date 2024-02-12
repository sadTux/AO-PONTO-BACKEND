import os

from fastapi import UploadFile
from pytest import fixture, mark, raises

from app import auth, error, util


@fixture
def sub():
    yield {
        "user_uuid": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
        "key": [1, 2, 3, 4],
    }


@fixture
def sub_invalido():
    yield {"user_uuid": "3fa85f64-5717-4562-b3fc-2c963f66afa6"}


@fixture
def user_token_invalido(sub_invalido):
    yield auth.encode_token(sub_invalido, 20)


@fixture
def user_token(sub):
    yield auth.encode_token(sub, 20)


@fixture
def token():
    yield auth.encode_token("sub", 20)


def test_encode_token_token_valido(sub):
    assert type(auth.encode_token(sub, 20)) == str


def test_encode_token_erro(sub):
    with raises(error.CustomException) as e:
        auth.encode_token(sub, None)
    assert e.value.detail == "Erro Interno API"


def test_dencode_token_token_valido(token):
    assert auth.decode_token(token) == "sub"


def test_dencode_token_token_invalido():
    with raises(error.CustomException) as e:
        auth.decode_token(None)
    assert (
        e.value.detail
        == "Desculpe Você nao tem Permissão, Chave de acesso Invalida"
    )


def test_dencode_token_user_token_invalido(user_token_invalido):
    with raises(error.CustomException) as e:
        auth.decode_token(user_token_invalido)
    assert e.value.detail == "Desculpe Você nao tem Permissão."


def test_dencode_token_user_chave_invalida(user_token):
    with raises(error.CustomException) as e:
        auth.decode_token(user_token, 47)
    assert e.value.detail == "Desculpe Você nao tem Permissão de acesso."


def test_dencode_token_user_nao_encontrado(user_token):
    with raises(error.CustomException) as e:
        auth.decode_token(user_token, 1)
    assert (
        e.value.detail
        == "Desculpe Você nao tem Permissão, Usuario Nao encontrado!"
    )
