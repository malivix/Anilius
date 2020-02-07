from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

from anilius.core.settings import settings
from anilius.utils.singleton import Singleton


class DB(metaclass=Singleton):
    engine = None
    Model = None
    session = None

    def __init__(self):
        self.engine = create_engine(
            settings["DATABASE_URI"],
            convert_unicode=True,
            **settings["DATABASE_CONNECT_OPTIONS"]
        )
        self.session = scoped_session(
            sessionmaker(autocommit=False, autoflush=False, bind=self.engine)
        )
        self.Model = declarative_base(name="Model")
        self.Model.query = self.session.query_property()

    def get_model(self):
        return self.Model


DB = DB()
db_session = DB.session
Model = DB.get_model()
