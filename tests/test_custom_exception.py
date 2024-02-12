import os

from fastapi.testclient import TestClient
from pytest import fixture, raises

from app import app, core, error, util


@fixture
def exception_422():
    yield error.CustomException(422)


def test_custom_exception():
    e = error.CustomException(422)

    assert e.detail == "Unprocessable Entity"


from fastapi.testclient import TestClient

from app import app, core, error, util

client = TestClient(app)


def test_custom_http_exception(exception_422):
    from fastapi import HTTPException

    with raises(HTTPException) as e:
        error.custom_HTTPException(exception_422)

    assert e.value.detail == "Unprocessable Entity"
