from anilius.core.serializer_field import SerializerField


class BooleanField(SerializerField):
    def validate(self):
        return type(self._raw_value) is bool

    def get_value(self):
        return bool(self._raw_value)
