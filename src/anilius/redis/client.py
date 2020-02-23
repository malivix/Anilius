import logging
from time import sleep

import redis
from anilius.core.settings import settings
from anilius.utils.singleton import Singleton
from redis.exceptions import ConnectionError

logger = logging.getLogger(__name__)


class RedisClientPool(metaclass=Singleton):
    pool = None
    redis_instance = None

    def __init__(self):
        self.pool = redis.ConnectionPool(
            host=settings.get("REDIS_HOST", "localhost"),
            port=settings.get("REDIS_HOST", 6379),
        )
        self.is_ready()

    def is_ready(self):
        self.redis_instance = redis.Redis(connection_pool=self.pool)
        logger.info("Check redis is ready...")

        while True:
            try:
                result = self.redis_instance.ping()
            except ConnectionError:
                logger.warning("Wait for ready redis")
                sleep(2)
                continue

            if result:
                break

        self.redis_instance.close()

    def __call__(self):
        self.redis_instance = redis.Redis(connection_pool=self.pool)
        return self.redis_instance

    def __enter__(self):
        return self.redis_instance

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.redis_instance.close()
        return False


RedisClient = RedisClientPool()
