from anilius.core.service import Service


class ServiceWrapper:
    proto_service_path = None

    def __init__(self, proto_service_path):
        self.proto_service_path = proto_service_path
        self.service = Service()

    def add(self, rpc_method, controller):
        self.service.add(self.proto_service_path, rpc_method, controller)
