from typing import Annotated

from fastapi import Depends
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from app import core

__all__ = ["SessionLocal", "engine", "get_db", "_db"]

engine = create_engine(core.settings.SQLALCHEMY_DATABASE_URI)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

from typing import Generator


async def get_db() -> Session:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


_db = Annotated[Session, Depends(get_db)]
