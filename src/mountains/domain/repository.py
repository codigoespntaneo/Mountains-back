from abc import ABC, abstractmethod

from src.mountains.domain.models import Mountain

class MountainRepository(ABC):
    @abstractmethod
    def all(self)->list[Mountain]: ...

    @abstractmethod
    def save(self, mountain: Mountain) -> None: ...
