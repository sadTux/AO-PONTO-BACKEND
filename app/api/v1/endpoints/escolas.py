from fastapi import APIRouter
from fastapi.param_functions import Depends
from pydantic.types import UUID4
from app import auth, error, models, schema
from app.util import QueryParametersDep

router = APIRouter(prefix="/escolas", tags=["Escolas"])


@router.get(
    "/",
    response_model=list[schema.GetEscolas] | schema.GetEscolas,
    status_code=200,
)
def get_escolas(
    query_parameters: QueryParametersDep,
    authorization: str = Depends(auth.Key.n0),
) -> list[schema.GetEscolas] | schema.GetEscolas:
    """Realiza requisiçoes tipo **GET** em **Escolas** models

    Args:
        query_parameters (object): Parâmetros de consulta 'QueryParametersDep'.

    Raises:
        HTTPException: {"status_code": "code" , "msg": "message"}

    Returns:
        Retorna os dados da consulta em lista do schema `GetEscolas` ou somente um GetEscolas.
    """
    try:
        return models.Escolas.query_params(
            query_parameters.all_data,
            query_parameters.attribute,
            query_parameters.value,
            query_parameters.skip,
            query_parameters.limit,
        )
    except Exception as e:
        error.custom_HTTPException(e)


@router.post("/", response_model=schema.GetEscolas, status_code=201)
def create_escolas(
    json_data: schema.PostEscolas,
    authorization: str = Depends(auth.Key.n0),
) -> schema.GetEscolas:
    """Recebe uma requisição tipo `POST` contendo dados referente a **Escolas**

    Args:
        json_data (schema.PostEscolas): schema de dados para serem criados **Escolas**
        authorization (str, optional): **OAuth 2.0**. Defaults to None.

    Raises:
        HTTPException: {"status_code": "code" , "msg": "message"}

    Returns:
        GetEscolas: Retorna o dado com as informaçoes de criaçao atualizadas.
    """
    try:
        data = models.Escolas(**json_data.model_dump())
        return data.create()
    except Exception as e:
        error.custom_HTTPException(e)


@router.put("/", response_model=schema.GetEscolas, status_code=200)
def update_escolas_by_uuid(
    uuid: UUID4,
    json_data: schema.PutEscolas,
    authorization: str = Depends(auth.Key.n0),
) -> schema.GetEscolas:
    """Atualiza um dado na tabela **Escolas** a partir de um UUID valido

    Args:
        uuid (UUID4): UUID do dado a ser atualizado
        json_data (schema.PutEscolas): Schema de dados que pode ser atualizados.
        authorization (str, optional): **OAuth 2.0**. Defaults to None.

    Raises:
        HTTPException: {"status_code": "code" , "msg": "message"}

    Returns:
        schema.GetEscolas: Retorna os dado com as informaçoes atualizadas.
    """
    try:
        return models.Escolas.update(
            uuid,
            **json_data.model_dump(
                exclude_unset=True,
            )
        )
    except Exception as e:
        error.custom_HTTPException(e)


@router.delete("/")
def delete_escolas_by_uuid(
    uuid: UUID4,
    authorization: str = Depends(auth.Key.n0),
) -> str:
    """Deleta um dado na tabela **Escolas** a partir do seu UUID

    Args:
        uuid (UUID4): UUID do dado a ser deletado
        authorization (str, optional): **OAuth 2.0**. Defaults to None.

    Raises:
        HTTPException: {"status_code": "code" , "msg": "message"}

    Returns:
        str: "Ok"
    """
    try:
        return models.Escolas.remove(uuid)
    except Exception as e:
        error.custom_HTTPException(e)