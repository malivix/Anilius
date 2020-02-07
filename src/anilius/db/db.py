from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

from anilius.core.settings import settings
from anilius.utils.singleton import Singleton


class DB(metaclass=Singleton):
    engine = None
    Model = None

    def __init__(self):
        self.engine = create_engine(
            settings["DATABASE_URI"],
            convert_unicode=True,
            **settings["DATABASE_CONNECT_OPTIONS"]
        )
        self.Model = declarative_base(name="Model")

    def get_model(self):
        return self.Model

    def get_engine(self):
        return self.engine

    def add(self, model):
        pass


DB = DB()
Model = DB.get_model()
