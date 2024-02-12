from fastapi import APIRouter
from fastapi.param_functions import Depends
from pydantic.types import UUID4
from app import auth, error, models, schema
from app.util import QueryParametersDep

router = APIRouter(prefix="/salas", tags=["Salas"])


@router.get(
    "/",
    response_model=list[schema.GetSalas] | schema.GetSalas,
    status_code=200,
)
def get_salas(
    query_parameters: QueryParametersDep,
    authorization: str = Depends(auth.Key.n0),
) -> list[schema.GetSalas] | schema.GetSalas:
    """Realiza requisiçoes tipo **GET** em **Salas** models

    Args:
        query_parameters (object): Parâmetros de consulta 'QueryParametersDep'.

    Raises:
        HTTPException: {"status_code": "code" , "msg": "message"}

    Returns:
        Retorna os dados da consulta em lista do schema `GetSalas` ou somente um GetSalas.
    """
    try:
        return models.Salas.query_params(
            query_parameters.all_data,
            query_parameters.attribute,
            query_parameters.value,
            query_parameters.skip,
            query_parameters.limit,
        )
    except Exception as e:
        error.custom_HTTPException(e)


@router.post("/", response_model=schema.GetSalas, status_code=201)
def create_salas(
    json_data: schema.PostSalas,
    authorization: str = Depends(auth.Key.n0),
) -> schema.GetSalas:
    """Recebe uma requisição tipo `POST` contendo dados referente a **Salas**

    Args:
        json_data (schema.PostSalas): schema de dados para serem criados **Salas**
        authorization (str, optional): **OAuth 2.0**. Defaults to None.

    Raises:
        HTTPException: {"status_code": "code" , "msg": "message"}

    Returns:
        GetSalas: Retorna o dado com as informaçoes de criaçao atualizadas.
    """
    try:
        data = models.Salas(**json_data.model_dump())
        return data.create()
    except Exception as e:
        error.custom_HTTPException(e)


@router.put("/", response_model=schema.GetSalas, status_code=200)
def update_salas_by_uuid(
    uuid: UUID4,
    json_data: schema.PutSalas,
    authorization: str = Depends(auth.Key.n0),
) -> schema.GetSalas:
    """Atualiza um dado na tabela **Salas** a partir de um UUID valido

    Args:
        uuid (UUID4): UUID do dado a ser atualizado
        json_data (schema.PutSalas): Schema de dados que pode ser atualizados.
        authorization (str, optional): **OAuth 2.0**. Defaults to None.

    Raises:
        HTTPException: {"status_code": "code" , "msg": "message"}

    Returns:
        schema.GetSalas: Retorna os dado com as informaçoes atualizadas.
    """
    try:
        return models.Salas.update(
            uuid,
            **json_data.model_dump(
                exclude_unset=True,
            )
        )
    except Exception as e:
        error.custom_HTTPException(e)


@router.delete("/")
def delete_salas_by_uuid(
    uuid: UUID4,
    authorization: str = Depends(auth.Key.n0),
) -> str:
    """Deleta um dado na tabela **Salas** a partir do seu UUID

    Args:
        uuid (UUID4): UUID do dado a ser deletado
        authorization (str, optional): **OAuth 2.0**. Defaults to None.

    Raises:
        HTTPException: {"status_code": "code" , "msg": "message"}

    Returns:
        str: "Ok"
    """
    try:
        return models.Salas.remove(uuid)
    except Exception as e:
        error.custom_HTTPException(e)