from abc import ABC

import grpc
from anilius.core.serializer import Serializer

from anilius.core.serializer_field import SerializerField

from anilius.core.permission import Permission


class Controller(ABC):
    permissions = ()
    request_serializer = None
    reply_serializer = None
    _serialized_data = None
    meta = {}

    def __init__(self, request, context):
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
        self._serialized_data = self.get_request_serializer(self.request).to_dict()

        for data in self.metadata:
            self.meta[data.key] = data.value

        for permission in self.permissions:
            assert isinstance(
                permission, Permission
            ), "permissions should be type of Permission"

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

    @property
    def client_id(self):
        return self.meta.get("client-id", None)

    @property
    def client_secret(self):
        return self.meta.get("client-secret", None)

    @property
    def sdk_id(self):
        return self.meta.get("sdk-secret", None)

    @property
    def sdk_secret(self):
        return self.meta.get("sdk-secret", None)

    @property
    def authorization(self):
        return self.meta.get("authorization ", None)

    def get_response(self):
        self.check_permissions()
