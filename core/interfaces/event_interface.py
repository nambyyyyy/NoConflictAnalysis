from abc import ABC, abstractmethod
from core.entities.event_entity import Event


class EventRepository(ABC):
    @abstractmethod
    async def save(self, event: Event) -> None:
        """Сохраняет событие в БД."""
        pass
