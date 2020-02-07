from abc import ABC, abstractmethod

from anilius.db.db import DB
from anilius.wrappers.service import ServiceWrapper


class Module(ABC):
    service_proto_module = None
    name = None
    service_wrapper = None
    db_wrapper = None

    def __init__(self):
        if self.name is None:
            self.name = self.__class__.__name__

        assert (
            self.service_proto_module is not None
        ), "Should gave valid proto path of service descriptor"

        self.service_wrapper = ServiceWrapper(self.service_proto_module)
        self.db = DB

        self.initialise(self.service_wrapper, self.db)

    @abstractmethod
    def initialise(self, service, db):
        raise NotImplemented
