from anilius.core.serializer_field import SerializerField


class IntegerField(SerializerField):
    def validate(self):
        return type(self._raw_value) is int

    def get_value(self):
        return int(self._raw_value)
