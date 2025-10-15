from motor.motor_asyncio import AsyncIOMotorClient
from core.interfaces.event_interface import EventRepository
from core.entities.event_entity import Event
from typing import Optional
from bson import ObjectId


class MongoEventRepository(EventRepository):
    """Асинхронный репозиторий для записи событий в MongoDB."""

    def __init__(self, uri: str, db_name: str = "analytics"):
        self.client = AsyncIOMotorClient(uri)
        self.db = self.client[db_name]
        self.collection = self.db["events"]

    async def save(self, event: Event) -> Optional[ObjectId]:
        doc = {           
            "conflict_id": str(event.conflict_id),
            "event_type": event.event_type,
            "user_id": str(event.user_id) if event.user_id else None,
            "item_id": str(event.item_id) if event.item_id else None,
            "old_value": event.old_value,
            "new_value": event.new_value,
            "timestamp": event.timestamp,
        }
        try:
            result = await self.collection.insert_one(doc)
            return result.inserted_id
        except Exception as e:
            return None