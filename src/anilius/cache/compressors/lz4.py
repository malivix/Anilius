from anilius.cache.compressors.base import BaseCompressor
from anilius.cache.exceptions import CompressorError
from lz4.frame import compress as _compress, decompress as _decompress


class Lz4Compressor(BaseCompressor):
    min_length = 15

    def compress(self, value):
        if len(value) > self.min_length:
            return _compress(value)
        return value

    def decompress(self, value):
        try:
            return _decompress(value)
        except Exception as e:
            raise CompressorError(e)
