from fastapi import APIRouter
from fastapi.param_functions import Depends
from pydantic.types import UUID4
from app import auth, error, models, schema
from app.util import QueryParametersDep

router = APIRouter(prefix="/cardapio", tags=["Cardapio"])


@router.get(
    "/",
    response_model=list[schema.GetCardapio] | schema.GetCardapio,
    status_code=200,
)
def get_cardapio(
    query_parameters: QueryParametersDep,
    authorization: str = Depends(auth.Key.n1),
) -> list[schema.GetCardapio] | schema.GetCardapio:
    """Realiza requisiçoes tipo **GET** em **Cardapio** models

    Args:
        query_parameters (object): Parâmetros de consulta 'QueryParametersDep'.

    Raises:
        HTTPException: {"status_code": "code" , "msg": "message"}

    Returns:
        Retorna os dados da consulta em lista do schema `GetCardapio` ou somente um GetCardapio.
    """
    try:
        return models.Cardapio.query_params(
            query_parameters.all_data,
            query_parameters.attribute,
            query_parameters.value,
            query_parameters.skip,
            query_parameters.limit,
        )
    except Exception as e:
        error.custom_HTTPException(e)


@router.post("/", response_model=schema.GetCardapio, status_code=201)
def create_cardapio(
    json_data: schema.PostCardapio,
    authorization: str = Depends(auth.Key.n1),
) -> schema.GetCardapio:
    """Recebe uma requisição tipo `POST` contendo dados referente a **Cardapio**

    Args:
        json_data (schema.PostCardapio): schema de dados para serem criados **Cardapio**
        authorization (str, optional): **OAuth 2.0**. Defaults to None.

    Raises:
        HTTPException: {"status_code": "code" , "msg": "message"}

    Returns:
        GetCardapio: Retorna o dado com as informaçoes de criaçao atualizadas.
    """
    try:
        data = models.Cardapio(**json_data.model_dump())
        return data.create()
    except Exception as e:
        error.custom_HTTPException(e)


@router.put("/", response_model=schema.GetCardapio, status_code=200)
def update_cardapio_by_uuid(
    uuid: UUID4,
    json_data: schema.PutCardapio,
    authorization: str = Depends(auth.Key.n1),
) -> schema.GetCardapio:
    """Atualiza um dado na tabela **Cardapio** a partir de um UUID valido

    Args:
        uuid (UUID4): UUID do dado a ser atualizado
        json_data (schema.PutCardapio): Schema de dados que pode ser atualizados.
        authorization (str, optional): **OAuth 2.0**. Defaults to None.

    Raises:
        HTTPException: {"status_code": "code" , "msg": "message"}

    Returns:
        schema.GetCardapio: Retorna os dado com as informaçoes atualizadas.
    """
    try:
        return models.Cardapio.update(
            uuid,
            **json_data.model_dump(
                exclude_unset=True,
            )
        )
    except Exception as e:
        error.custom_HTTPException(e)


@router.delete("/")
def delete_cardapio_by_uuid(
    uuid: UUID4,
    authorization: str = Depends(auth.Key.n1),
) -> str:
    """Deleta um dado na tabela **Cardapio** a partir do seu UUID

    Args:
        uuid (UUID4): UUID do dado a ser deletado
        authorization (str, optional): **OAuth 2.0**. Defaults to None.

    Raises:
        HTTPException: {"status_code": "code" , "msg": "message"}

    Returns:
        str: "Ok"
    """
    try:
        return models.Cardapio.remove(uuid)
    except Exception as e:
        error.custom_HTTPException(e)