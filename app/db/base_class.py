import logging
import uuid
from datetime import datetime
from typing import Any

from sqlalchemy import Column, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.orm import DeclarativeBase, Session

from app import core, error, util

from .session import SessionLocal

__all__ = ["Base"]


def generate_uuid():
    return str(uuid.uuid4())


class Base(DeclarativeBase):
    __name__: str
    uuid = Column(UUID(as_uuid=True), primary_key=True, default=generate_uuid)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    updated_at = Column(DateTime, onupdate=datetime.utcnow)

    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()

    def create(self) -> object:
        try:
            _db = SessionLocal()
            data = self
            _db.add(data)
            _db.flush()
            _db.commit()
            _db.refresh(data)
            return data

        except SQLAlchemyError as e:
            raise error.custom_HTTPException(e)
        finally:
            _db.close()

    @classmethod
    def login(self, attribute: str, value: Any, password: str) -> object:
        """executa login em usuario

        Args:
            attribute (str): Nome do atributo para verificar o valor
            value (str): username para efetuar o login
            password (str): senha para ser verificada

        Raises:
            CustomException: 404 usuario ou senha incorretos
            CustomException: 401 status do usuario inativo
            CustomException: 401 senha incorreta_

        Returns:
            object: _description_
        """
        try:
            _db = SessionLocal()

            data = (
                _db.query(self)
                .filter(getattr(self, attribute) == value)
                .first()
            )
            if not data:
                raise error.CustomException(
                    status_code=404,
                    detail="Usuario ou senha invalidos",
                )
            if hasattr(data, "active"):
                if not data.active:
                    raise error.CustomException(
                        status_code=401, detail="Usuario Inativo"
                    )

            if not core.verify_password(password, data.senha):
                raise error.CustomException(
                    status_code=401,
                    detail="Usuario ou senha invalidos",
                )
            return data
        except SQLAlchemyError as e:
            raise error.custom_HTTPException(e)
        finally:
            _db.close()

    @classmethod
    def query_params(
        self,
        all_data: bool = False,
        attribute: str | None = None,
        value: str | None = None,
        skip: int | None = None,
        limit: int | None = None,
    ) -> object:
        """este metodo realiza querys personalizadas de acordo com a requisiao do front-end.

        Args:
            all_data (bool): se setado true retorna uma lista de todos os dados equivalentes.
            attribute (str | None): nome da chave a ser pesquisada obs tem que ser um attributo valido da tabela a que se chame o methodo.
            value (str | None): conteudo da busca relaciona a chave.
            skip (int | None, optional): numero da pagina em caso de busca paginada.
            limit (int | None, optional): quantidade por pagina.

        Raises:
            CustomException: 404 em caso de busca com um atribulo nao relacionado na tabela
            CustomException: 422 em caso de uma consulta especifica que nao sejam passados atribudos ou valores para busca

        Returns:
            object: retorna um objeto sqlalchemy podendo ser vazio em caso de nao encontrar nenhuma correspondeica
        """
        if attribute:
            if not hasattr(self, attribute):
                raise error.CustomException(
                    status_code=404,
                    detail="Atributo não encontrado",
                )

        try:
            _db = SessionLocal()
            if all_data:
                if not attribute:
                    if skip is not None and limit is not None:
                        _offset = skip * limit
                        data = (
                            _db.query(self).offset(_offset).limit(limit).all()
                        )
                        return data
                    else:
                        data = _db.query(self).all()
                        return data
                else:
                    if skip is not None and limit is not None:
                        _offset = skip * limit
                        data = (
                            _db.query(self)
                            .filter(getattr(self, attribute) == value)
                            .offset(_offset)
                            .limit(limit)
                            .all()
                        )
                    else:
                        data = (
                            _db.query(self)
                            .filter(getattr(self, attribute) == value)
                            .all()
                        )
                        return data
            else:
                if attribute == None or value == None:
                    raise error.CustomException(
                        status_code=422,
                        detail="Atributo e Valor requeridos",
                    )
                data = (
                    _db.query(self)
                    .filter(getattr(self, attribute) == value)
                    .first()
                )
                return data
        except Exception as e:
            raise error.custom_HTTPException(e)
        finally:
            _db.close()

    @classmethod
    def remove(self, uuid: UUID) -> str:
        """metodo utilizado para remover um dado da tabela correspondente

        Args:
            uuid (UUID): Id do dado a ser removido.

        Raises:
            CustomException: 404 em caso de nao encontar dado correspondete ao id remetido.
            CustomException: 400 em caso de um problema durante a exclusão

        Returns:
            str: retorna ok em caso de sucesso.
        """
        try:
            _db = SessionLocal()
            data = _db.query(self).filter_by(uuid=uuid).first()
            if not data:
                raise error.CustomException(
                    status_code=404, detail="Dado não encontrado"
                )
            _db.delete(data)
            _db.commit()
            return "OK"
        except Exception as e:
            raise error.custom_HTTPException(e)
        finally:
            _db.close()

    @classmethod
    def remove_data_and_files(self, uuid: UUID, files: list) -> str:
        """metodo utilizado para remover um dado da tabela correspondente

        Args:
            uuid (UUID): Id do dado a ser removido.

        Raises:
            CustomException: 404 em caso de nao encontar dado correspondete ao id remetido.
            CustomException: 400 em caso de um problema durante a exclusão

        Returns:
            str: retorna ok em caso de sucesso.
        """
        try:
            _db = SessionLocal()
            exclude_files = []
            data = _db.query(self).filter_by(uuid=uuid).first()
            if not data:
                raise error.CustomException(
                    status_code=404, detail="Dado não encontrado"
                )
            for f in files:
                attr = getattr(data, f)
                if attr:
                    exclude_files.append(attr)

            _db.delete(data)
            _db.commit()

            for exclude_f in exclude_files:
                util.delete_file(core.settings.UPLOAD_DIR, exclude_f)
            return "OK"
        except Exception as e:
            raise error.custom_HTTPException(e)
        finally:
            _db.close()

    def flush(self) -> object:
        """Realiza um flush no banco, um processo que verifica toda a transação mas nao salva, util para teste.

        Returns:
            object: retorna um objeto sqlalchemy
        """
        try:
            _db = SessionLocal()
            _db.add(self)
            _db.flush()
            _db.refresh(self)
            _db.close()
            return self
        except Exception as e:
            raise error.custom_HTTPException(e)
        finally:
            _db.close()

    @classmethod
    def update(self, uuid: UUID, **json_data) -> object:
        """funçao para atuilizar dados de uma tabela a partir de um dict

        Args:
            uuid (UUID): UUID do dado a ser atualizado

        Raises:
            CustomException: 404 caso nao haja correspondeica do uuid a dados nesta tabela

        Returns:
            object: retorna o objeto atualizado
        """
        try:
            _db = SessionLocal()
            data = _db.query(self).filter_by(uuid=uuid).first()
            if not data:
                raise error.CustomException(
                    status_code=404,
                    detail="Dado não encontrado",
                )
            for key, value in json_data.items():
                setattr(data, key, value)
            _db.add(data)
            _db.commit()
            _db.refresh(data)
            return data
        except Exception as e:
            raise error.custom_HTTPException(e)
        finally:
            _db.close()

    @classmethod
    async def update_form(self, uuid: UUID, files: list, **form) -> object:
        """funçao para atuilizar dados de uma tabela a partir de um dict

        Args:
            uuid (UUID): UUID do dado a ser atualizado

        Raises:
            CustomException: 404 caso nao haja correspondeica do uuid a dados nesta tabela

        Returns:
            object: retorna o objeto atualizado
        """
        try:
            _db = SessionLocal()
            list_exclude_files = []
            except_exlude_files = []
            data = _db.query(self).filter_by(uuid=uuid).first()
            if not data:
                raise error.CustomException(
                    status_code=404,
                    detail="Dado não encontrado",
                )

            for key, value in form.items():
                if value or str(type(value)) == "<class 'bool'>":
                    if key in files:
                        list_exclude_files.append(getattr(data, key))
                        filename = await util.save_file(value, "image")
                        except_exlude_files.append(filename)
                        setattr(data, key, filename)
                    else:
                        setattr(data, key, value)
            _db.add(data)
            _db.commit()
            _db.refresh(data)
            if list_exclude_files:
                for filename in list_exclude_files:
                    util.delete_file(core.settings.UPLOAD_DIR, filename)
            return data

        except Exception as e:
            if except_exlude_files:
                for filename in except_exlude_files:
                    util.delete_file(core.settings.UPLOAD_DIR, filename)
            raise error.custom_HTTPException(e)

        except:
            if except_exlude_files:
                for filename in except_exlude_files:
                    util.delete_file(core.settings.UPLOAD_DIR, filename)
            raise error.custom_HTTPException(e)

        finally:
            _db.close()

    @classmethod
    async def create_form(self, files: list, **form) -> object:
        try:
            _db = SessionLocal()
            except_exlude_files = []
            data = self()
            for key, value in form.items():
                if value:
                    for f in files:
                        if key in f:
                            filename = await util.save_file(value, f[key])
                            except_exlude_files.append(filename)
                            setattr(data, "uuid", filename)
                        else:
                            setattr(data, key, value)
            _db.add(data)
            _db.commit()
            _db.refresh(data)
            return data

        except Exception as e:
            if except_exlude_files:
                for data in except_exlude_files:
                    util.delete_file(core.settings.UPLOAD_DIR, data)
            raise error.custom_HTTPException(e)

        finally:
            _db.close()

    @classmethod
    def get(
        self,
        attribute: str | None = None,
        value: Any | None = None,
    ) -> object:
        """_summary_

        Args:
            attribute (str): _description_
            value (Any): _description_

        Returns:
            object: _description_
        """
        try:
            _db = SessionLocal()
            data = (
                _db.query(self)
                .filter(getattr(self, attribute) == value)
                .first()
            )

            return data
        except Exception as e:
            raise error.custom_HTTPException(e)
        finally:
            _db.close()

    @classmethod
    def count(
        cls,
        attribute: str | None = None,
        value: Any | None = None,
    ) -> int:
        """Retorna a quantidade de registros que correspondem à condição.

        Args:
            attribute (str): Nome do atributo para filtrar.
            value (Any): Valor a ser usado na condição de filtro.

        Returns:
            int: A quantidade de registros que correspondem à condição.
        """
        try:
            _db = SessionLocal()
            query = _db.query(cls)

            if attribute is not None and value is not None:
                query = query.filter(getattr(cls, attribute) == value)

            count = query.count()
            return count
        except Exception as e:
            raise error.custom_HTTPException(e)
        finally:
            _db.close()

    @classmethod
    def unique_verify(self, attribute, value):
        try:
            _db = SessionLocal()
            data = (
                _db.query(self)
                .filter(getattr(self, attribute) == value)
                .first()
            )
            if data:
                raise error.CustomException(
                    status_code=422, detail=f"{value} ja existe"
                )
            return value
        except Exception as e:
            raise error.custom_HTTPException(e)
        finally:
            _db.close()
