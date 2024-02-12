from typing import Annotated

from fastapi import Depends, HTTPException, Query

__all__ = [
    "QueryParametersDep",
]


class QueryParameters:
    def __init__(
        self,
        all_data: bool = Query(
            False,
            alias="all",
            description="Tipo de busca. **true**: todas as correspondencias, **false**: somente a primeira",
        ),
        attribute: str
        | None = Query(
            None,
            description='Em caso de busca especifica enviar nome do atributo a ser buscado ***obs: caso utilizado "value" obrigatorio***',
        ),
        value: str
        | None = Query(
            None,
            description='Em caso de busca especifica enviar valor do atributo a ser buscado ***obs: caso utilizado "atributo" obrigatorio***',
        ),
        skip: int
        | None = Query(
            None,
            description='Busca por pagina, **obs: "0" (zero) indica à primeira pagina, caso utilizado "limit" obrigatorio**',
        ),
        limit: int
        | None = Query(
            None,
            description="Quantidade de itens por pagina. **obs: skip obigatorio**",
        ),
    ):
        # Verificando a condição de all_data, atributo e value
        if not all_data and (not attribute or not value):
            raise HTTPException(
                status_code=422,
                detail="Quando all é 'false', 'atributo' e 'value' são obrigatórios!",
            )

        # Verificando a condição de skip e limit
        if (skip is not None and limit is None) or (
            limit is not None and skip is None
        ):
            raise HTTPException(
                status_code=422,
                detail="Se 'skip' ou 'limit' for fornecido, ambos devem ser fornecidos!",
            )

        self.all_data = all_data
        self.attribute = attribute
        self.value = value
        self.skip = skip
        self.limit = limit


QueryParametersDep = Annotated[dict, Depends(QueryParameters)]
