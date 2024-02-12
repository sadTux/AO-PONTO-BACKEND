import http
import logging

from fastapi import HTTPException

__all__ = ["CustomException", "custom_HTTPException"]


class ConstructException(Exception):
    """
    Classe base de exceção para construir exceções personalizadas com um código de status
    e uma mensagem de detalhe opcional.

    Atributos:
        status_code (int): O código de status HTTP associado a esta exceção.
        detail (any): A mensagem de detalhe opcional associada a esta exceção.
    """

    def __init__(
        self,
        status_code: int,
        detail: any = None,
    ) -> None:
        if detail is None:
            detail = http.HTTPStatus(status_code).phrase
        self.status_code = status_code
        self.detail = detail


class CustomException(ConstructException):
    """
    Classe de exceção personalizada que herda de ConstructException,
    permitindo a criação de exceções com um código de status e uma mensagem de detalhe.

    Atributos:
        status_code (int): O código de status HTTP associado a esta exceção.
        detail (any): A mensagem de detalhe opcional associada a esta exceção.
    """

    def __init__(
        self,
        status_code: int,
        detail: any = None,
    ) -> None:
        super().__init__(status_code, detail)


def custom_HTTPException(e: any) -> HTTPException:
    """
    Função para manipular exceções personalizadas, logar um aviso se a exceção
    não tiver um código de status, e lançar uma HTTPException com um código de status
    e uma mensagem de detalhe.

    Args:
        e (any): A exceção a ser manipulada.

    Raises:
        HTTPException: Uma exceção HTTP com um código de status e uma mensagem de detalhe.

    Returns:
        HTTPException: Uma exceção HTTP lançada.
    """
    logging.warning(e) if not hasattr(e, "status_code") else ...
    raise HTTPException(
        status_code=e.status_code if hasattr(e, "status_code") else 555,
        detail=e.detail if hasattr(e, "status_code") else "Erro Interno API",
    )
