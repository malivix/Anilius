import signal
import threading
from concurrent import futures

import grpc
from anilius.server.server import BaseServe

NUM_SECS_TO_WAIT = 10


class GRPCIOServer(BaseServe):

    def __init__(self, interceptors, service):
        super().__init__(interceptors, service)

        self.server = self.server = grpc.server(
            futures.ThreadPoolExecutor(max_workers=10),
            interceptors=interceptors,
        )

        self.event_shutting_down = threading.Event()

        self.service.add_handlers_to_server(self.server)
        self.server.add_insecure_port(self._address)

        signal.signal(signal.SIGTERM, self.on_stop)

    def on_stop(self, signum, frame):
        self.event_shutting_down.set()

    def graceful_stop(self):
        self.server.stop(NUM_SECS_TO_WAIT).wait()
        self.server.wait_for_termination()

    def run(self):
        try:
            self.server.start()
            self.event_shutting_down.wait()
            self.graceful_stop()
        except KeyboardInterrupt:
            self.graceful_stop()

    async def start(self):
        self.run()

    def stop(self):
        self.graceful_stop()
