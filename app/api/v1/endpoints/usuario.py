from fastapi import APIRouter
from fastapi.param_functions import Depends
from pydantic.types import UUID4
from app import auth, error, models, schema
from app.util import QueryParametersDep

router = APIRouter(prefix="/usuario", tags=["Usuario"])


@router.get(
    "/",
    response_model=list[schema.GetUsuario] | schema.GetUsuario,
    status_code=200,
)
def get_usuario(
    query_parameters: QueryParametersDep,
    authorization: str = Depends(auth.Key.n0),
) -> list[schema.GetUsuario] | schema.GetUsuario:
    """Realiza requisiçoes tipo **GET** em **Usuario** models

    Args:
        query_parameters (object): Parâmetros de consulta 'QueryParametersDep'.

    Raises:
        HTTPException: {"status_code": "code" , "msg": "message"}

    Returns:
        Retorna os dados da consulta em lista do schema `GetUsuario` ou somente um GetUsuario.
    """
    try:
        return models.Usuario.query_params(
            query_parameters.all_data,
            query_parameters.attribute,
            query_parameters.value,
            query_parameters.skip,
            query_parameters.limit,
        )
    except Exception as e:
        error.custom_HTTPException(e)


@router.post("/", response_model=schema.GetUsuario, status_code=201)
def create_usuario(
    json_data: schema.PostUsuario,
    authorization: str = Depends(auth.Key.n0),
) -> schema.GetUsuario:
    """Recebe uma requisição tipo `POST` contendo dados referente a **Usuario**

    Args:
        json_data (schema.PostUsuario): schema de dados para serem criados **Usuario**
        authorization (str, optional): **OAuth 2.0**. Defaults to None.

    Raises:
        HTTPException: {"status_code": "code" , "msg": "message"}

    Returns:
        GetUsuario: Retorna o dado com as informaçoes de criaçao atualizadas.
    """
    try:
        data = models.Usuario(**json_data.model_dump())
        return data.create()
    except Exception as e:
        error.custom_HTTPException(e)


@router.put("/", response_model=schema.GetUsuario, status_code=200)
def update_usuario_by_uuid(
    uuid: UUID4,
    json_data: schema.PutUsuario,
    authorization: str = Depends(auth.Key.n0),
) -> schema.GetUsuario:
    """Atualiza um dado na tabela **Usuario** a partir de um UUID valido

    Args:
        uuid (UUID4): UUID do dado a ser atualizado
        json_data (schema.PutUsuario): Schema de dados que pode ser atualizados.
        authorization (str, optional): **OAuth 2.0**. Defaults to None.

    Raises:
        HTTPException: {"status_code": "code" , "msg": "message"}

    Returns:
        schema.GetUsuario: Retorna os dado com as informaçoes atualizadas.
    """
    try:
        return models.Usuario.update(
            uuid,
            **json_data.model_dump(
                exclude_unset=True,
            )
        )
    except Exception as e:
        error.custom_HTTPException(e)


@router.delete("/")
def delete_usuario_by_uuid(
    uuid: UUID4,
    authorization: str = Depends(auth.Key.n0),
) -> str:
    """Deleta um dado na tabela **Usuario** a partir do seu UUID

    Args:
        uuid (UUID4): UUID do dado a ser deletado
        authorization (str, optional): **OAuth 2.0**. Defaults to None.

    Raises:
        HTTPException: {"status_code": "code" , "msg": "message"}

    Returns:
        str: "Ok"
    """
    try:
        return models.Usuario.remove(uuid)
    except Exception as e:
        error.custom_HTTPException(e)