from abc import abstractmethod

from anilius.core.settings import settings


class BaseServe(object):
    server = None
    service = None
    interceptors = None
    host = "0.0.0.0"
    port = "8080"

    def __init__(self, interceptors, service):
        self.host = settings.get("GRPC_SERVER_HOST", "0.0.0.0")
        self.port = settings.get("GRPC_SERVER_PORT", "8080")

        self.service = service
        self.interceptors = interceptors

    @property
    def _address(self):
        return self.host + ":" + self.port

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass
