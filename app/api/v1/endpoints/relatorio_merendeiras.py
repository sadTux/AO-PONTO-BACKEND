from fastapi import APIRouter
from fastapi.param_functions import Depends
from pydantic.types import UUID4
from app import auth, error, models, schema
from app.util import QueryParametersDep

router = APIRouter(prefix="/relatorio-merendeiras", tags=["RelatorioMerendeiras"])


@router.get(
    "/",
    response_model=list[schema.GetRelatorioMerendeiras] | schema.GetRelatorioMerendeiras,
    status_code=200,
)
def get_relatorio_merendeiras(
    query_parameters: QueryParametersDep,
    authorization: str = Depends(auth.Key.n1),
) -> list[schema.GetRelatorioMerendeiras] | schema.GetRelatorioMerendeiras:
    """Realiza requisiçoes tipo **GET** em **RelatorioMerendeiras** models

    Args:
        query_parameters (object): Parâmetros de consulta 'QueryParametersDep'.

    Raises:
        HTTPException: {"status_code": "code" , "msg": "message"}

    Returns:
        Retorna os dados da consulta em lista do schema `GetRelatorioMerendeiras` ou somente um GetRelatorioMerendeiras.
    """
    try:
        return models.RelatorioMerendeiras.query_params(
            query_parameters.all_data,
            query_parameters.attribute,
            query_parameters.value,
            query_parameters.skip,
            query_parameters.limit,
        )
    except Exception as e:
        error.custom_HTTPException(e)


@router.post("/", response_model=schema.GetRelatorioMerendeiras, status_code=201)
def create_relatorio_merendeiras(
    json_data: schema.PostRelatorioMerendeiras,
    authorization: str = Depends(auth.Key.n1),
) -> schema.GetRelatorioMerendeiras:
    """Recebe uma requisição tipo `POST` contendo dados referente a **RelatorioMerendeiras**

    Args:
        json_data (schema.PostRelatorioMerendeiras): schema de dados para serem criados **RelatorioMerendeiras**
        authorization (str, optional): **OAuth 2.0**. Defaults to None.

    Raises:
        HTTPException: {"status_code": "code" , "msg": "message"}

    Returns:
        GetRelatorioMerendeiras: Retorna o dado com as informaçoes de criaçao atualizadas.
    """
    try:
        data = models.RelatorioMerendeiras(**json_data.model_dump())
        return data.create()
    except Exception as e:
        error.custom_HTTPException(e)


@router.put("/", response_model=schema.GetRelatorioMerendeiras, status_code=200)
def update_relatorio_merendeiras_by_uuid(
    uuid: UUID4,
    json_data: schema.PutRelatorioMerendeiras,
    authorization: str = Depends(auth.Key.n1),
) -> schema.GetRelatorioMerendeiras:
    """Atualiza um dado na tabela **RelatorioMerendeiras** a partir de um UUID valido

    Args:
        uuid (UUID4): UUID do dado a ser atualizado
        json_data (schema.PutRelatorioMerendeiras): Schema de dados que pode ser atualizados.
        authorization (str, optional): **OAuth 2.0**. Defaults to None.

    Raises:
        HTTPException: {"status_code": "code" , "msg": "message"}

    Returns:
        schema.GetRelatorioMerendeiras: Retorna os dado com as informaçoes atualizadas.
    """
    try:
        return models.RelatorioMerendeiras.update(
            uuid,
            **json_data.model_dump(
                exclude_unset=True,
            )
        )
    except Exception as e:
        error.custom_HTTPException(e)


@router.delete("/")
def delete_relatorio_merendeiras_by_uuid(
    uuid: UUID4,
    authorization: str = Depends(auth.Key.n1),
) -> str:
    """Deleta um dado na tabela **RelatorioMerendeiras** a partir do seu UUID

    Args:
        uuid (UUID4): UUID do dado a ser deletado
        authorization (str, optional): **OAuth 2.0**. Defaults to None.

    Raises:
        HTTPException: {"status_code": "code" , "msg": "message"}

    Returns:
        str: "Ok"
    """
    try:
        return models.RelatorioMerendeiras.remove(uuid)
    except Exception as e:
        error.custom_HTTPException(e)