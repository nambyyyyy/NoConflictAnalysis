from motor.motor_asyncio import AsyncIOMotorClient
from core.interfaces.conflict_interface import ConflictRepository
from core.entities.conflict_entity import Conflict
from typing import Optional
from bson import ObjectId


class MongoConflictRepository(ConflictRepository):
    """Асинхронный репозиторий для записи конфликта в MongoDB."""

    def __init__(self, uri: str, db_name: str = "analytics"):
        self.client = AsyncIOMotorClient(uri)
        self.db = self.client[db_name]
        self.collection = self.db["conflicts"]

    async def save(self, conflict: Conflict) -> Optional[ObjectId]:
        doc = {
            "title": conflict.title,
            "creator_id": str(conflict.creator_id),
            "partner_id": str(conflict.partner_id) if conflict.partner_id else None,
            "id": str(conflict.id),
            "status": conflict.status,
            "slug": conflict.slug,
            "progress": conflict.progress,
            "created_at": conflict.created_at,
            "resolved_at": conflict.resolved_at,
            "deleted_by_creator": conflict.deleted_by_creator,
            "deleted_by_partner": conflict.deleted_by_partner,
            "truce_status": conflict.truce_status,
            "truce_initiator_id": (
                str(conflict.truce_initiator_id)
                if conflict.truce_initiator_id
                else None
            ),
            "items": conflict.items,
            "events": conflict.events,
        }
        try:
            result = await self.collection.insert_one(doc)
            return result.inserted_id
        except Exception:
            return None
