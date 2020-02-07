import importlib

import grpc
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

from anilius.utils.singleton import Singleton

_sym_db = _symbol_database.Default()


class Service(metaclass=Singleton):
    _services = {}

    @staticmethod
    def _get_services_from_proto(proto_service_path):
        proto_service_module = importlib.import_module(proto_service_path)

        assert hasattr(
            proto_service_module, "DESCRIPTOR"
        ), "Should gave valid proto service path"

        descriptor = getattr(proto_service_module, "DESCRIPTOR")

        assert hasattr(
            descriptor, "services_by_name"
        ), "Should gave valid proto service path"

        services = getattr(descriptor, "services_by_name")

        explicit_services = list()
        for service in services:
            explicit_services.append(services[service])

        return explicit_services

    def _add_rpc_handler(self, service, rpc_method, controller):
        rpc_handler = self._create_rpc_handler(rpc_method, controller)

        assert (
            service not in self._services
            or rpc_method.name not in self._services[service]
        ), "{} rpc for {} service is already add".format(service, rpc_method.name)

        if service in self._services:
            self._services[service][rpc_method.name] = rpc_handler
        else:
            self._services[service] = {rpc_method.name: rpc_handler}

    @staticmethod
    def _create_controller_wrapper(controller):
        def wrapper(request, context):
            return controller(request, context).get_response()

        return wrapper

    def _create_rpc_handler(self, rpc_method, controller):
        request_deserializer = self._create_reflection_from_method(
            rpc_method.input_type
        )
        response_serializer = self._create_reflection_from_method(
            rpc_method.output_type
        )

        handler = grpc.unary_unary_rpc_method_handler(
            self._create_controller_wrapper(controller),
            request_deserializer=request_deserializer.FromString,
            response_serializer=response_serializer.SerializeToString,
        )

        return handler

    @staticmethod
    def _convert_file_to_module(file_name):
        return file_name.split(".")[0].replace("/", ".") + "_pb2"

    def _create_reflection_from_method(self, descriptor):
        reflection = _reflection.GeneratedProtocolMessageType(
            descriptor.name,
            (_message.Message,),
            {
                "DESCRIPTOR": descriptor,
                "__module__": self._convert_file_to_module(descriptor.file.name),
            },
        )
        _sym_db.RegisterMessage(reflection)

        return reflection

    def get_generic_handlers(self):
        generic_handlers = []

        for service in self._services:
            generic_handler = grpc.method_handlers_generic_handler(
                service, self._services[service]
            )
            generic_handlers.append(generic_handler)

        return generic_handlers

    def add_handlers_to_server(self, server):
        generic_handlers = self.get_generic_handlers()
        server.add_generic_rpc_handlers(generic_handlers)

    def add(self, proto_service_path, rpc_method, controller):
        services = self._get_services_from_proto(proto_service_path)

        for service in services:
            methods = getattr(service, "methods_by_name")

            if rpc_method in methods:
                self._add_rpc_handler(
                    service.full_name, methods[rpc_method], controller
                )
