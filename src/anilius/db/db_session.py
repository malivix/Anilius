from sqlalchemy.orm import scoped_session, sessionmaker

from anilius.db.db import DB
from anilius.utils.singleton import Singleton


class DBSession(metaclass=Singleton):
    def __init__(
        self,
        autocommit=False,
        autoflush=False,
        commit=True,
        expire_on_commit=False,
        close=True,
    ):
        self.engine = DB.get_engine()
        self.session = scoped_session(
            sessionmaker(
                autocommit=autocommit,
                autoflush=autoflush,
                bind=self.engine,
                expire_on_commit=expire_on_commit,
            )
        )
        self.model = DB.get_model()
        self.model.query = self.session.query_property()
        self.commit = commit
        self.close = close

    def __call__(self, commit=True, close=True):
        self.commit = commit
        self.close = close

    def __enter__(self):
        return self.session

    def __exit__(self, exc_type=None, exc_val=None, exc_tb=None):

        if exc_val:
            self.session.rollback()
            self.session.close()
            raise exc_type(exc_val)
        elif self.commit:
            self.session.commit()
            if self.close:
                self.session.expunge_all()
                self.session.close()

        return True
