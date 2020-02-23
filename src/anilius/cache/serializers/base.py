class BaseSerializer:
    def __init__(self, options=None):
        pass

    def dumps(self, value):
        raise NotImplementedError

    def loads(self, value):
        raise NotImplementedError
