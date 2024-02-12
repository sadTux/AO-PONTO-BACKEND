from fastapi import APIRouter
from fastapi.param_functions import Depends
from pydantic.types import UUID4
from app import auth, error, models, schema
from app.util import QueryParametersDep

router = APIRouter(prefix="/disciplinas", tags=["Disciplinas"])


@router.get(
    "/",
    response_model=list[schema.GetDisciplinas] | schema.GetDisciplinas,
    status_code=200,
)
def get_disciplinas(
    query_parameters: QueryParametersDep,
    authorization: str = Depends(auth.Key.n0),
) -> list[schema.GetDisciplinas] | schema.GetDisciplinas:
    """Realiza requisiçoes tipo **GET** em **Disciplinas** models

    Args:
        query_parameters (object): Parâmetros de consulta 'QueryParametersDep'.

    Raises:
        HTTPException: {"status_code": "code" , "msg": "message"}

    Returns:
        Retorna os dados da consulta em lista do schema `GetDisciplinas` ou somente um GetDisciplinas.
    """
    try:
        return models.Disciplinas.query_params(
            query_parameters.all_data,
            query_parameters.attribute,
            query_parameters.value,
            query_parameters.skip,
            query_parameters.limit,
        )
    except Exception as e:
        error.custom_HTTPException(e)


@router.post("/", response_model=schema.GetDisciplinas, status_code=201)
def create_disciplinas(
    json_data: schema.PostDisciplinas,
    authorization: str = Depends(auth.Key.n0),
) -> schema.GetDisciplinas:
    """Recebe uma requisição tipo `POST` contendo dados referente a **Disciplinas**

    Args:
        json_data (schema.PostDisciplinas): schema de dados para serem criados **Disciplinas**
        authorization (str, optional): **OAuth 2.0**. Defaults to None.

    Raises:
        HTTPException: {"status_code": "code" , "msg": "message"}

    Returns:
        GetDisciplinas: Retorna o dado com as informaçoes de criaçao atualizadas.
    """
    try:
        data = models.Disciplinas(**json_data.model_dump())
        return data.create()
    except Exception as e:
        error.custom_HTTPException(e)


@router.put("/", response_model=schema.GetDisciplinas, status_code=200)
def update_disciplinas_by_uuid(
    uuid: UUID4,
    json_data: schema.PutDisciplinas,
    authorization: str = Depends(auth.Key.n0),
) -> schema.GetDisciplinas:
    """Atualiza um dado na tabela **Disciplinas** a partir de um UUID valido

    Args:
        uuid (UUID4): UUID do dado a ser atualizado
        json_data (schema.PutDisciplinas): Schema de dados que pode ser atualizados.
        authorization (str, optional): **OAuth 2.0**. Defaults to None.

    Raises:
        HTTPException: {"status_code": "code" , "msg": "message"}

    Returns:
        schema.GetDisciplinas: Retorna os dado com as informaçoes atualizadas.
    """
    try:
        return models.Disciplinas.update(
            uuid,
            **json_data.model_dump(
                exclude_unset=True,
            )
        )
    except Exception as e:
        error.custom_HTTPException(e)


@router.delete("/")
def delete_disciplinas_by_uuid(
    uuid: UUID4,
    authorization: str = Depends(auth.Key.n0),
) -> str:
    """Deleta um dado na tabela **Disciplinas** a partir do seu UUID

    Args:
        uuid (UUID4): UUID do dado a ser deletado
        authorization (str, optional): **OAuth 2.0**. Defaults to None.

    Raises:
        HTTPException: {"status_code": "code" , "msg": "message"}

    Returns:
        str: "Ok"
    """
    try:
        return models.Disciplinas.remove(uuid)
    except Exception as e:
        error.custom_HTTPException(e)