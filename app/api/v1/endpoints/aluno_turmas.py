from fastapi import APIRouter
from fastapi.param_functions import Depends
from pydantic.types import UUID4
from app import auth, error, models, schema
from app.util import QueryParametersDep

router = APIRouter(prefix="/aluno-turmas", tags=["AlunoTurmas"])


@router.get(
    "/",
    response_model=list[schema.GetAlunoTurmas] | schema.GetAlunoTurmas,
    status_code=200,
)
def get_aluno_turmas(
    query_parameters: QueryParametersDep,
    authorization: str = Depends(auth.Key.n1),
) -> list[schema.GetAlunoTurmas] | schema.GetAlunoTurmas:
    """Realiza requisiçoes tipo **GET** em **AlunoTurmas** models

    Args:
        query_parameters (object): Parâmetros de consulta 'QueryParametersDep'.

    Raises:
        HTTPException: {"status_code": "code" , "msg": "message"}

    Returns:
        Retorna os dados da consulta em lista do schema `GetAlunoTurmas` ou somente um GetAlunoTurmas.
    """
    try:
        return models.AlunoTurmas.query_params(
            query_parameters.all_data,
            query_parameters.attribute,
            query_parameters.value,
            query_parameters.skip,
            query_parameters.limit,
        )
    except Exception as e:
        error.custom_HTTPException(e)


@router.post("/", response_model=schema.GetAlunoTurmas, status_code=201)
def create_aluno_turmas(
    json_data: schema.PostAlunoTurmas,
    authorization: str = Depends(auth.Key.n1),
) -> schema.GetAlunoTurmas:
    """Recebe uma requisição tipo `POST` contendo dados referente a **AlunoTurmas**

    Args:
        json_data (schema.PostAlunoTurmas): schema de dados para serem criados **AlunoTurmas**
        authorization (str, optional): **OAuth 2.0**. Defaults to None.

    Raises:
        HTTPException: {"status_code": "code" , "msg": "message"}

    Returns:
        GetAlunoTurmas: Retorna o dado com as informaçoes de criaçao atualizadas.
    """
    try:
        data = models.AlunoTurmas(**json_data.model_dump())
        return data.create()
    except Exception as e:
        error.custom_HTTPException(e)


@router.put("/", response_model=schema.GetAlunoTurmas, status_code=200)
def update_aluno_turmas_by_uuid(
    uuid: UUID4,
    json_data: schema.PutAlunoTurmas,
    authorization: str = Depends(auth.Key.n1),
) -> schema.GetAlunoTurmas:
    """Atualiza um dado na tabela **AlunoTurmas** a partir de um UUID valido

    Args:
        uuid (UUID4): UUID do dado a ser atualizado
        json_data (schema.PutAlunoTurmas): Schema de dados que pode ser atualizados.
        authorization (str, optional): **OAuth 2.0**. Defaults to None.

    Raises:
        HTTPException: {"status_code": "code" , "msg": "message"}

    Returns:
        schema.GetAlunoTurmas: Retorna os dado com as informaçoes atualizadas.
    """
    try:
        return models.AlunoTurmas.update(
            uuid,
            **json_data.model_dump(
                exclude_unset=True,
            )
        )
    except Exception as e:
        error.custom_HTTPException(e)


@router.delete("/")
def delete_aluno_turmas_by_uuid(
    uuid: UUID4,
    authorization: str = Depends(auth.Key.n1),
) -> str:
    """Deleta um dado na tabela **AlunoTurmas** a partir do seu UUID

    Args:
        uuid (UUID4): UUID do dado a ser deletado
        authorization (str, optional): **OAuth 2.0**. Defaults to None.

    Raises:
        HTTPException: {"status_code": "code" , "msg": "message"}

    Returns:
        str: "Ok"
    """
    try:
        return models.AlunoTurmas.remove(uuid)
    except Exception as e:
        error.custom_HTTPException(e)