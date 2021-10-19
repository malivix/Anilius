from abc import ABC

import grpc
from anilius.core.permission import Permission
from anilius.core.serializer import Serializer
from anilius.core.serializer_field import SerializerField
from anilius.utils.jwt import decode_jwt
from jwt import InvalidAlgorithmError, InvalidSignatureError


class Controller(ABC):
    permissions = ()
    payload = {}
    is_authorize = False
    request_serializer = None
    request_deserializer = None
    response_serializer = None
    response_deserializer = None
    _serialized_data = None
    meta = {}

    def __init__(self, request, context, request_deserializer, response_serializer):
        self.request_deserializer = request_deserializer
        self.response_serializer = response_serializer
        self.request = request
        self.context = context

        self.metadata = context.invocation_metadata()

        self.parse()

    def check_permissions(self):
        for permission in self.permissions:
            has_perm = permission.has_perm(self)
            if not has_perm:
                self.raise_permission()
                break

    def raise_permission(self):
        self.context.set_code(grpc.StatusCode.PERMISSION_DENIED)
        self.context.set_details("You have not permission for this action")

    def parse(self):
        self.meta = {}
        self._serialized_data = self.get_request_serializer(self.request).to_dict()

        for data in self.metadata:
            self.meta[data.key] = data.value

        for permission in self.permissions:
            assert isinstance(
                permission, Permission
            ), "permissions should be type of Permission"

        authorization = self.meta.get("authorization", None)
        if authorization is not None:
            self.extract_payload(authorization)
        else:
            self.payload = {}
            self.is_authorize = False

    def extract_payload(self, authorization):
        try:
            self.payload = decode_jwt(authorization)
            self.is_authorize = True
        except (ValueError, InvalidAlgorithmError, InvalidSignatureError):
            pass

    def get_valid_data(self, key, default=None):
        field = self._serialized_data.get(key, None)

        if not isinstance(field, SerializerField):
            return default

        return field.get_value()

    @property
    def get_request_serializer(self):
        return (
            self.request_serializer
            if self.request_serializer is not None
            else Serializer
        )

    def get_response(self):
        self.check_permissions()
