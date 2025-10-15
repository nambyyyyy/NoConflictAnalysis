from abc import ABC, abstractmethod
from core.entities.conflict_entity import Conflict


class ConflictRepository(ABC):
    @abstractmethod
    async def save(self, conflict: Conflict) -> None:
        """Сохраняет конфликт в БД."""
        pass
