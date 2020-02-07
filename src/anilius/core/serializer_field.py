class SerializerField:
    _creation_counter = 0
    _raw_value = None

    def __init__(self):
        self._creation_counter = SerializerField._creation_counter
        SerializerField._creation_counter += 1

    def get_creation_counter(self):
        return self._creation_counter

    def validate(self):
        raise NotImplementedError()

    def get_value(self):
        raise NotImplementedError()

    def set_raw_value(self, raw):
        self._raw_value = raw
