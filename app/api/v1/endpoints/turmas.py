from fastapi import APIRouter
from fastapi.param_functions import Depends
from pydantic.types import UUID4
from app import auth, error, models, schema
from app.util import QueryParametersDep

router = APIRouter(prefix="/turmas", tags=["Turmas"])


@router.get(
    "/",
    response_model=list[schema.GetTurmas] | schema.GetTurmas,
    status_code=200,
)
def get_turmas(
    query_parameters: QueryParametersDep,
    authorization: str = Depends(auth.Key.n1),
) -> list[schema.GetTurmas] | schema.GetTurmas:
    """Realiza requisiçoes tipo **GET** em **Turmas** models

    Args:
        query_parameters (object): Parâmetros de consulta 'QueryParametersDep'.

    Raises:
        HTTPException: {"status_code": "code" , "msg": "message"}

    Returns:
        Retorna os dados da consulta em lista do schema `GetTurmas` ou somente um GetTurmas.
    """
    try:
        return models.Turmas.query_params(
            query_parameters.all_data,
            query_parameters.attribute,
            query_parameters.value,
            query_parameters.skip,
            query_parameters.limit,
        )
    except Exception as e:
        error.custom_HTTPException(e)


@router.post("/", response_model=schema.GetTurmas, status_code=201)
def create_turmas(
    json_data: schema.PostTurmas,
    authorization: str = Depends(auth.Key.n1),
) -> schema.GetTurmas:
    """Recebe uma requisição tipo `POST` contendo dados referente a **Turmas**

    Args:
        json_data (schema.PostTurmas): schema de dados para serem criados **Turmas**
        authorization (str, optional): **OAuth 2.0**. Defaults to None.

    Raises:
        HTTPException: {"status_code": "code" , "msg": "message"}

    Returns:
        GetTurmas: Retorna o dado com as informaçoes de criaçao atualizadas.
    """
    try:
        data = models.Turmas(**json_data.model_dump())
        return data.create()
    except Exception as e:
        error.custom_HTTPException(e)


@router.put("/", response_model=schema.GetTurmas, status_code=200)
def update_turmas_by_uuid(
    uuid: UUID4,
    json_data: schema.PutTurmas,
    authorization: str = Depends(auth.Key.n1),
) -> schema.GetTurmas:
    """Atualiza um dado na tabela **Turmas** a partir de um UUID valido

    Args:
        uuid (UUID4): UUID do dado a ser atualizado
        json_data (schema.PutTurmas): Schema de dados que pode ser atualizados.
        authorization (str, optional): **OAuth 2.0**. Defaults to None.

    Raises:
        HTTPException: {"status_code": "code" , "msg": "message"}

    Returns:
        schema.GetTurmas: Retorna os dado com as informaçoes atualizadas.
    """
    try:
        return models.Turmas.update(
            uuid,
            **json_data.model_dump(
                exclude_unset=True,
            )
        )
    except Exception as e:
        error.custom_HTTPException(e)


@router.delete("/")
def delete_turmas_by_uuid(
    uuid: UUID4,
    authorization: str = Depends(auth.Key.n1),
) -> str:
    """Deleta um dado na tabela **Turmas** a partir do seu UUID

    Args:
        uuid (UUID4): UUID do dado a ser deletado
        authorization (str, optional): **OAuth 2.0**. Defaults to None.

    Raises:
        HTTPException: {"status_code": "code" , "msg": "message"}

    Returns:
        str: "Ok"
    """
    try:
        return models.Turmas.remove(uuid)
    except Exception as e:
        error.custom_HTTPException(e)