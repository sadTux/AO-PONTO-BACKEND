from fastapi import APIRouter

from .cardapio_escola import router as cardapio_escola_router
from .salas import router as salas_router
from .usuario import router as usuario_router
from .escolas import router as escolas_router
from .turmas import router as turmas_router
from .login import router as login_router
from .aluno_turmas import router as aluno_turmas_router
from .papel import router as papel_router
from .cardapio import router as cardapio_router
from .alunos import router as alunos_router
from .frequencias import router as frequencias_router
from .disciplinas import router as disciplinas_router
from .relatorio_merendeiras import router as relatorio_merendeiras_router


routers = APIRouter()

routers.include_router(cardapio_escola_router)
routers.include_router(salas_router)
routers.include_router(usuario_router)
routers.include_router(escolas_router)
routers.include_router(turmas_router)
routers.include_router(login_router)
routers.include_router(aluno_turmas_router)
routers.include_router(papel_router)
routers.include_router(cardapio_router)
routers.include_router(alunos_router)
routers.include_router(frequencias_router)
routers.include_router(disciplinas_router)
routers.include_router(relatorio_merendeiras_router)
