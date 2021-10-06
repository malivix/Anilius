import threading


class Singleton(type):
    _instances = {}
    _locks = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            if cls.__name__ not in cls._locks:
                cls._locks[cls.__name__] = threading.Lock()

            with cls._locks[cls.__name__]:
                if cls not in cls._instances:
                    cls._instances[cls] = super(Singleton, cls).__call__(
                        *args, **kwargs
                    )
        return cls._instances[cls]
