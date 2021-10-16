from anilius.core.serializer_field import SerializerField


class ListField(SerializerField):
    def __init__(self, list_type=None):
        super().__init__()
        self.list_type = list_type

    def validate(self):
        result = type(self._raw_value) is list

        if self.list_type and result:
            for item in self._raw_value:
                result = result and item.validate()

        return result

    def get_value(self):
        return self._raw_value
