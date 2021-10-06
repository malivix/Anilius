from anilius.core.serializer_field import SerializerField


class StringField(SerializerField):
    def validate(self):
        return type(self._raw_value) is str

    def get_value(self):
        return str(self._raw_value)
