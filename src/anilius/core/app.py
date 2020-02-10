import importlib
import inspect
import logging
import signal
import threading
from concurrent import futures
from importlib.util import find_spec

import grpc
from anilius.core.module import Module
from anilius.core.service import Service
from anilius.core.settings import settings
from anilius.utils.singleton import Singleton
from prometheus_client import start_http_server
from py_grpc_prometheus.prometheus_server_interceptor import PromServerInterceptor
from sentry_sdk import init as sentry_init

NUM_SECS_TO_WAIT = 10

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class App(metaclass=Singleton):
    _modules = {}

    def __init__(self):
        self.service = Service()

        self.enable_modules = settings["ENABLE_MODULES"]

        assert (
            type(self.enable_modules) is tuple or type(self.enable_modules) is list
        ), "ENABLE_MODULES should be iterable"

        self._initialize_modules()

        self.event_shutting_down = threading.Event()
        self.server = grpc.server(
            futures.ThreadPoolExecutor(max_workers=10),
            interceptors=(PromServerInterceptor(),),
        )
        start_http_server(8081)
        self.set_signals()
        sentry_init(dsn=settings["SENTRY_DSN"])

    def set_signals(self):
        signal.signal(signal.SIGTERM, self.on_done)

    def on_done(self, signum, frame):
        self.logger.info("Got signal {}, {}".format(signum, frame))
        self.event_shutting_down.set()

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

    @property
    def logger(self):
        return logger

    def graceful_stop(self):
        self.logger.info("Stopped RPC server, Waiting for RPCs to complete...")
        self.server.stop(NUM_SECS_TO_WAIT).wait()
        self.logger.info("Done stopping server")
        self.server.wait_for_termination()

    def run(self):
        try:
            self.service.add_handlers_to_server(self.server)
            self.server.add_insecure_port("[::]:8080")
            self.server.start()
            self.logger.info("Started server at " + "8080")
            self.event_shutting_down.wait()
            self.graceful_stop()
        except KeyboardInterrupt:
            self.graceful_stop()
