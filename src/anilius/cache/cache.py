from anilius.cache.compressors.lz4 import Lz4Compressor
from anilius.cache.exceptions import CompressorError
from anilius.cache.serializers.msgpack import MSGPackSerializer
from anilius.redis.client import RedisClient


class Cache:
    _compressor = Lz4Compressor()
    _serializer = MSGPackSerializer()

    def decode(self, value):
        """
        Decode the given value.
        """

        try:
            value = int(value)
        except (ValueError, TypeError):
            try:
                value = self._compressor.decompress(value)
            except CompressorError:
                # Handle little values, chosen to be not compressed
                pass
            value = self._serializer.loads(value)
        return value

    def encode(self, value):
        """
        Encode the given value.
        """

        if isinstance(value, bool) or not isinstance(value, int):
            value = self._serializer.dumps(value)
            value = self._compressor.compress(value)
            return value

        return value

    @staticmethod
    def set(*args, **kwargs):
        with RedisClient as client:
            return client.set(*args, **kwargs)

    @staticmethod
    def get(key, default=None, version=None, _client=None):
        with RedisClient as client:
            return client.get(key, default=default, version=version, _client=_client)

    @staticmethod
    def delete(*args, **kwargs):
        with RedisClient as client:
            return client.delete(*args, **kwargs)

    @staticmethod
    def incr(*args, **kwargs):
        with RedisClient as client:
            return client.incr(*args, **kwargs)

    @staticmethod
    def decr(*args, **kwargs):
        with RedisClient as client:
            return client.decr(*args, **kwargs)

    @staticmethod
    def keys(*args, **kwargs):
        with RedisClient as client:
            return client.keys(*args, **kwargs)

    @staticmethod
    def ttl(*args, **kwargs):
        with RedisClient as client:
            return client.ttl(*args, **kwargs)

    @staticmethod
    def persist(*args, **kwargs):
        with RedisClient as client:
            return client.persist(*args, **kwargs)

    @staticmethod
    def expire(*args, **kwargs):
        with RedisClient as client:
            return client.expire(*args, **kwargs)

    @staticmethod
    def lock(*args, **kwargs):
        with RedisClient as client:
            return client.lock(*args, **kwargs)

    @staticmethod
    def close(**kwargs):
        with RedisClient as client:
            client.close(**kwargs)

    @staticmethod
    def touch(*args, **kwargs):
        with RedisClient as client:
            return client.touch(*args, **kwargs)
