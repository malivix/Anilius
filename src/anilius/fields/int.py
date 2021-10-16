from anilius.core.serializer_field import SerializerField


class IntegerField(SerializerField):
    def validate(self):
        return type(self._raw_value) is int

    def get_value(self):
        if type(self._raw_value) is int:
            return self._raw_value
        elif self._raw_value is None:
            return 0

        return int(self._raw_value)
