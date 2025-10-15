from infrastructure.persistence.conflict_repository import MongoConflictRepository
from infrastructure.persistence.event_repository import MongoEventRepository
from application.services.event_service import EventService
from application.services.conflict_service import ConflictService
from presentation.dependencies.config_mongoDB import settings


def get_event_service() -> EventService:
    """Фабрика для создания EventService"""
    return EventService(
        repo=MongoEventRepository(settings.MONGO_URI, settings.MONGO_DB)
    )


def get_conflict_service() -> ConflictService:
    """Фабрика для создания ConflictService"""
    return ConflictService(
        repo=MongoConflictRepository(settings.MONGO_URI, settings.MONGO_DB)
    )
