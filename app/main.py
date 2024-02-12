from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app import api, core

if core.settings.DEBUG:
    app = FastAPI(title=core.settings.PROJECT_NAME)
else:
    app = FastAPI(docs_url=None, redocs_url=None, openapi_url=None)


origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(api.routers, prefix=core.settings.API_URL_PREFIX)
