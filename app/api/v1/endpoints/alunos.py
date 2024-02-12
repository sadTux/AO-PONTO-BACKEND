from fastapi import APIRouter
from fastapi.param_functions import Depends
from pydantic.types import UUID4
from app import auth, error, models, schema
from app.util import QueryParametersDep

router = APIRouter(prefix="/alunos", tags=["Alunos"])


@router.get(
    "/",
    response_model=list[schema.GetAlunos] | schema.GetAlunos,
    status_code=200,
)
def get_alunos(
    query_parameters: QueryParametersDep,
    authorization: str = Depends(auth.Key.n0),
) -> list[schema.GetAlunos] | schema.GetAlunos:
    """Realiza requisiçoes tipo **GET** em **Alunos** models

    Args:
        query_parameters (object): Parâmetros de consulta 'QueryParametersDep'.

    Raises:
        HTTPException: {"status_code": "code" , "msg": "message"}

    Returns:
        Retorna os dados da consulta em lista do schema `GetAlunos` ou somente um GetAlunos.
    """
    try:
        return models.Alunos.query_params(
            query_parameters.all_data,
            query_parameters.attribute,
            query_parameters.value,
            query_parameters.skip,
            query_parameters.limit,
        )
    except Exception as e:
        error.custom_HTTPException(e)


@router.post("/", response_model=schema.GetAlunos, status_code=201)
def create_alunos(
    json_data: schema.PostAlunos,
    authorization: str = Depends(auth.Key.n0),
) -> schema.GetAlunos:
    """Recebe uma requisição tipo `POST` contendo dados referente a **Alunos**

    Args:
        json_data (schema.PostAlunos): schema de dados para serem criados **Alunos**
        authorization (str, optional): **OAuth 2.0**. Defaults to None.

    Raises:
        HTTPException: {"status_code": "code" , "msg": "message"}

    Returns:
        GetAlunos: Retorna o dado com as informaçoes de criaçao atualizadas.
    """
    try:
        data = models.Alunos(**json_data.model_dump())
        return data.create()
    except Exception as e:
        error.custom_HTTPException(e)


@router.put("/", response_model=schema.GetAlunos, status_code=200)
def update_alunos_by_uuid(
    uuid: UUID4,
    json_data: schema.PutAlunos,
    authorization: str = Depends(auth.Key.n0),
) -> schema.GetAlunos:
    """Atualiza um dado na tabela **Alunos** a partir de um UUID valido

    Args:
        uuid (UUID4): UUID do dado a ser atualizado
        json_data (schema.PutAlunos): Schema de dados que pode ser atualizados.
        authorization (str, optional): **OAuth 2.0**. Defaults to None.

    Raises:
        HTTPException: {"status_code": "code" , "msg": "message"}

    Returns:
        schema.GetAlunos: Retorna os dado com as informaçoes atualizadas.
    """
    try:
        return models.Alunos.update(
            uuid,
            **json_data.model_dump(
                exclude_unset=True,
            )
        )
    except Exception as e:
        error.custom_HTTPException(e)


@router.delete("/")
def delete_alunos_by_uuid(
    uuid: UUID4,
    authorization: str = Depends(auth.Key.n0),
) -> str:
    """Deleta um dado na tabela **Alunos** a partir do seu UUID

    Args:
        uuid (UUID4): UUID do dado a ser deletado
        authorization (str, optional): **OAuth 2.0**. Defaults to None.

    Raises:
        HTTPException: {"status_code": "code" , "msg": "message"}

    Returns:
        str: "Ok"
    """
    try:
        return models.Alunos.remove(uuid)
    except Exception as e:
        error.custom_HTTPException(e)