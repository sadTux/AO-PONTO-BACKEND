from fastapi import APIRouter
from fastapi.param_functions import Depends
from pydantic.types import UUID4
from app import auth, error, models, schema
from app.util import QueryParametersDep

router = APIRouter(prefix="/papel", tags=["Papel"])


@router.get(
    "/",
    response_model=list[schema.GetPapel] | schema.GetPapel,
    status_code=200,
)
def get_papel(
    query_parameters: QueryParametersDep,
    authorization: str = Depends(auth.Key.n0),
) -> list[schema.GetPapel] | schema.GetPapel:
    """Realiza requisiçoes tipo **GET** em **Papel** models

    Args:
        query_parameters (object): Parâmetros de consulta 'QueryParametersDep'.

    Raises:
        HTTPException: {"status_code": "code" , "msg": "message"}

    Returns:
        Retorna os dados da consulta em lista do schema `GetPapel` ou somente um GetPapel.
    """
    try:
        return models.Papel.query_params(
            query_parameters.all_data,
            query_parameters.attribute,
            query_parameters.value,
            query_parameters.skip,
            query_parameters.limit,
        )
    except Exception as e:
        error.custom_HTTPException(e)


@router.post("/", response_model=schema.GetPapel, status_code=201)
def create_papel(
    json_data: schema.PostPapel,
    authorization: str = Depends(auth.Key.n0),
) -> schema.GetPapel:
    """Recebe uma requisição tipo `POST` contendo dados referente a **Papel**

    Args:
        json_data (schema.PostPapel): schema de dados para serem criados **Papel**
        authorization (str, optional): **OAuth 2.0**. Defaults to None.

    Raises:
        HTTPException: {"status_code": "code" , "msg": "message"}

    Returns:
        GetPapel: Retorna o dado com as informaçoes de criaçao atualizadas.
    """
    try:
        data = models.Papel(**json_data.model_dump())
        return data.create()
    except Exception as e:
        error.custom_HTTPException(e)


@router.put("/", response_model=schema.GetPapel, status_code=200)
def update_papel_by_uuid(
    uuid: UUID4,
    json_data: schema.PutPapel,
    authorization: str = Depends(auth.Key.n0),
) -> schema.GetPapel:
    """Atualiza um dado na tabela **Papel** a partir de um UUID valido

    Args:
        uuid (UUID4): UUID do dado a ser atualizado
        json_data (schema.PutPapel): Schema de dados que pode ser atualizados.
        authorization (str, optional): **OAuth 2.0**. Defaults to None.

    Raises:
        HTTPException: {"status_code": "code" , "msg": "message"}

    Returns:
        schema.GetPapel: Retorna os dado com as informaçoes atualizadas.
    """
    try:
        return models.Papel.update(
            uuid,
            **json_data.model_dump(
                exclude_unset=True,
            )
        )
    except Exception as e:
        error.custom_HTTPException(e)


@router.delete("/")
def delete_papel_by_uuid(
    uuid: UUID4,
    authorization: str = Depends(auth.Key.n0),
) -> str:
    """Deleta um dado na tabela **Papel** a partir do seu UUID

    Args:
        uuid (UUID4): UUID do dado a ser deletado
        authorization (str, optional): **OAuth 2.0**. Defaults to None.

    Raises:
        HTTPException: {"status_code": "code" , "msg": "message"}

    Returns:
        str: "Ok"
    """
    try:
        return models.Papel.remove(uuid)
    except Exception as e:
        error.custom_HTTPException(e)