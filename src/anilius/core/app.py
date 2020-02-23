import importlib
import inspect
import logging
from importlib.util import find_spec

from anilius.core.module import Module
from anilius.core.service import Service
from anilius.core.settings import settings
from anilius.server.grpcio import GRPCIOServer
from anilius.utils.singleton import Singleton
from prometheus_client import start_http_server
from sentry_sdk import init as sentry_init

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class App(metaclass=Singleton):
    _modules = {}

    def __init__(self):
        self.service = Service()

        self.enable_modules = settings.get("ENABLE_MODULES", [])

        assert (
                type(self.enable_modules) is tuple or type(self.enable_modules) is list
        ), "ENABLE_MODULES should be iterable"

        self._initialize_modules()

        self.server = GRPCIOServer([], self.service)

        start_http_server(8081)
        # sentry_init(dsn=settings.get("SENTRY_DSN", ""))

    def _initialize_module(self, module):
        self._modules[module.name] = module()

    def _initialize_modules(self):
        root_of_module = "modules"

        for module in self.enable_modules:
            module_path = root_of_module + "." + module + ".module"

            assert find_spec(module_path) is not None, "Enabled modules should exist"

            mod = importlib.import_module(module_path)

            for entity_key in dir(mod):
                entity = getattr(mod, entity_key)

                if (
                        inspect.isclass(entity)
                        and issubclass(entity, Module)
                        and entity is not Module
                ):
                    self._initialize_module(entity)

    async def run(self):
        await self.server.start()
