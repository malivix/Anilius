import msgpack

from anilius.cache.serializers.base import BaseSerializer


class MSGPackSerializer(BaseSerializer):
    def dumps(self, value):
        return msgpack.dumps(value)

    def loads(self, value):
        return msgpack.loads(value, raw=False)
