from application.dtos.event_dto import EventDTO
from core.entities.event_entity import Event
from core.interfaces.event_interface import EventRepository
from typing import Optional
from bson import ObjectId


class EventService:
    """Сервис для обработки событий и передачи их в репозиторий."""

    def __init__(self, repo: EventRepository):
        self.repo = repo

    async def save_event(self, event_dto: EventDTO) -> None:
        """Преобразует DTO в Entity и сохраняет."""
        event: Event = self._to_entity(event_dto)
        inserted_id: Optional[ObjectId] = await self.repo.save(event)
        if inserted_id is None:
            # add custom error
            raise 

    def _to_entity(self, event_dto: EventDTO) -> Event:
        return Event(
            conflict_id=event_dto.conflict_id,
            event_type=event_dto.event_type,
            user_id=event_dto.user_id,
            item_id=event_dto.item_id,
            old_value=event_dto.old_value,
            new_value=event_dto.new_value,
            timestamp=event_dto.timestamp,
        )
