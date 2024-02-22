from fastapi import APIRouter
from fastapi.param_functions import Depends
from pydantic.types import UUID4
from app import auth, error, models, schema
from app.util import QueryParametersDep

router = APIRouter(prefix="/frequencias", tags=["Frequencias"])


@router.get(
    "/",
    response_model=list[schema.GetFrequencias] | schema.GetFrequencias,
    status_code=200,
)
def get_frequencias(
    query_parameters: QueryParametersDep,
    authorization: str = Depends(auth.Key.n1),
) -> list[schema.GetFrequencias] | schema.GetFrequencias:
    """Realiza requisiçoes tipo **GET** em **Frequencias** models

    Args:
        query_parameters (object): Parâmetros de consulta 'QueryParametersDep'.

    Raises:
        HTTPException: {"status_code": "code" , "msg": "message"}

    Returns:
        Retorna os dados da consulta em lista do schema `GetFrequencias` ou somente um GetFrequencias.
    """
    try:
        return models.Frequencias.query_params(
            query_parameters.all_data,
            query_parameters.attribute,
            query_parameters.value,
            query_parameters.skip,
            query_parameters.limit,
        )
    except Exception as e:
        error.custom_HTTPException(e)


@router.post("/", response_model=schema.GetFrequencias, status_code=201)
def create_frequencias(
    json_data: schema.PostFrequencias,
    authorization: str = Depends(auth.Key.n1),
) -> schema.GetFrequencias:
    """Recebe uma requisição tipo `POST` contendo dados referente a **Frequencias**

    Args:
        json_data (schema.PostFrequencias): schema de dados para serem criados **Frequencias**
        authorization (str, optional): **OAuth 2.0**. Defaults to None.

    Raises:
        HTTPException: {"status_code": "code" , "msg": "message"}

    Returns:
        GetFrequencias: Retorna o dado com as informaçoes de criaçao atualizadas.
    """
    try:
        data = models.Frequencias(**json_data.model_dump())
        return data.create()
    except Exception as e:
        error.custom_HTTPException(e)


@router.put("/", response_model=schema.GetFrequencias, status_code=200)
def update_frequencias_by_uuid(
    uuid: UUID4,
    json_data: schema.PutFrequencias,
    authorization: str = Depends(auth.Key.n1),
) -> schema.GetFrequencias:
    """Atualiza um dado na tabela **Frequencias** a partir de um UUID valido

    Args:
        uuid (UUID4): UUID do dado a ser atualizado
        json_data (schema.PutFrequencias): Schema de dados que pode ser atualizados.
        authorization (str, optional): **OAuth 2.0**. Defaults to None.

    Raises:
        HTTPException: {"status_code": "code" , "msg": "message"}

    Returns:
        schema.GetFrequencias: Retorna os dado com as informaçoes atualizadas.
    """
    try:
        return models.Frequencias.update(
            uuid,
            **json_data.model_dump(
                exclude_unset=True,
            )
        )
    except Exception as e:
        error.custom_HTTPException(e)


@router.delete("/")
def delete_frequencias_by_uuid(
    uuid: UUID4,
    authorization: str = Depends(auth.Key.n1),
) -> str:
    """Deleta um dado na tabela **Frequencias** a partir do seu UUID

    Args:
        uuid (UUID4): UUID do dado a ser deletado
        authorization (str, optional): **OAuth 2.0**. Defaults to None.

    Raises:
        HTTPException: {"status_code": "code" , "msg": "message"}

    Returns:
        str: "Ok"
    """
    try:
        return models.Frequencias.remove(uuid)
    except Exception as e:
        error.custom_HTTPException(e)