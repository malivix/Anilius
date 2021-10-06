class BaseCompressor:
    def __init__(self, options=None):
        self._options = options

    def compress(self, value):
        raise NotImplementedError

    def decompress(self, value):
        raise NotImplementedError
