from fastapi import APIRouter
from fastapi.param_functions import Depends
from pydantic.types import UUID4
from app import auth, error, models, schema
from app.util import QueryParametersDep

router = APIRouter(prefix="/cardapio-escola", tags=["CardapioEscola"])


@router.get(
    "/",
    response_model=list[schema.GetCardapioEscola] | schema.GetCardapioEscola,
    status_code=200,
)
def get_cardapio_escola(
    query_parameters: QueryParametersDep,
    authorization: str = Depends(auth.Key.n1),
) -> list[schema.GetCardapioEscola] | schema.GetCardapioEscola:
    """Realiza requisiçoes tipo **GET** em **CardapioEscola** models

    Args:
        query_parameters (object): Parâmetros de consulta 'QueryParametersDep'.

    Raises:
        HTTPException: {"status_code": "code" , "msg": "message"}

    Returns:
        Retorna os dados da consulta em lista do schema `GetCardapioEscola` ou somente um GetCardapioEscola.
    """
    try:
        return models.CardapioEscola.query_params(
            query_parameters.all_data,
            query_parameters.attribute,
            query_parameters.value,
            query_parameters.skip,
            query_parameters.limit,
        )
    except Exception as e:
        error.custom_HTTPException(e)


@router.post("/", response_model=schema.GetCardapioEscola, status_code=201)
def create_cardapio_escola(
    json_data: schema.PostCardapioEscola,
    authorization: str = Depends(auth.Key.n1),
) -> schema.GetCardapioEscola:
    """Recebe uma requisição tipo `POST` contendo dados referente a **CardapioEscola**

    Args:
        json_data (schema.PostCardapioEscola): schema de dados para serem criados **CardapioEscola**
        authorization (str, optional): **OAuth 2.0**. Defaults to None.

    Raises:
        HTTPException: {"status_code": "code" , "msg": "message"}

    Returns:
        GetCardapioEscola: Retorna o dado com as informaçoes de criaçao atualizadas.
    """
    try:
        data = models.CardapioEscola(**json_data.model_dump())
        return data.create()
    except Exception as e:
        error.custom_HTTPException(e)


@router.put("/", response_model=schema.GetCardapioEscola, status_code=200)
def update_cardapio_escola_by_uuid(
    uuid: UUID4,
    json_data: schema.PutCardapioEscola,
    authorization: str = Depends(auth.Key.n1),
) -> schema.GetCardapioEscola:
    """Atualiza um dado na tabela **CardapioEscola** a partir de um UUID valido

    Args:
        uuid (UUID4): UUID do dado a ser atualizado
        json_data (schema.PutCardapioEscola): Schema de dados que pode ser atualizados.
        authorization (str, optional): **OAuth 2.0**. Defaults to None.

    Raises:
        HTTPException: {"status_code": "code" , "msg": "message"}

    Returns:
        schema.GetCardapioEscola: Retorna os dado com as informaçoes atualizadas.
    """
    try:
        return models.CardapioEscola.update(
            uuid,
            **json_data.model_dump(
                exclude_unset=True,
            )
        )
    except Exception as e:
        error.custom_HTTPException(e)


@router.delete("/")
def delete_cardapio_escola_by_uuid(
    uuid: UUID4,
    authorization: str = Depends(auth.Key.n1),
) -> str:
    """Deleta um dado na tabela **CardapioEscola** a partir do seu UUID

    Args:
        uuid (UUID4): UUID do dado a ser deletado
        authorization (str, optional): **OAuth 2.0**. Defaults to None.

    Raises:
        HTTPException: {"status_code": "code" , "msg": "message"}

    Returns:
        str: "Ok"
    """
    try:
        return models.CardapioEscola.remove(uuid)
    except Exception as e:
        error.custom_HTTPException(e)