from abc import ABC, abstractmethod


class Permission(ABC):
    @abstractmethod
    def has_perm(self, controller):
        raise NotImplemented
