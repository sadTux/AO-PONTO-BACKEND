import pytest
from faker import Faker
from sqlalchemy import create_engine
from sqlalchemy.exc import DataError, IntegrityError
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy_utils import create_database, database_exists

from app import db, error, models

fake = Faker()
Base = declarative_base()


@pytest.fixture(scope="class")
def name():
    yield fake.name()


class TestModels:
    def setup_class(self):
        engine = create_engine(
            "postgresql+psycopg2://postgres:123@localhost/test_fast_gen"
        )
        if not database_exists(engine.url):
            create_database(engine.url)
        SessionLocal = sessionmaker(bind=engine)
        db.Base.metadata.create_all(engine)
        self.session = SessionLocal()

    def teardown_class(self):
        engine = create_engine(
            "postgresql+psycopg2://postgres:123@localhost/test_fast_gen"
        )
        self.session.rollback()
        self.session.close()
        db.Base.metadata.drop_all(engine)

    def test_role_criado_com_sucesso(self, name):
        role = models.Role(name=name, permission_level=5)
        role.create()
        assert role != None

    def test_role_permission_level_data_error(self, name):
        role = models.Role(name=name, permission_level="jaca")
        with pytest.raises(error.CustomException) as e:
            role.create()

    def test_role_query_params(self, name):
        role = models.Role.query_params(False, "name", name)
        assert role.name == name

    def test_role_query_params_atributo_nao_encontrado(self, name):
        # with pytest.raises(DataError) as error:
        role = models.Role.query_params(False, "name", "N0M&")
