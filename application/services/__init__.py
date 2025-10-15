from infrastructure.persistence.mongo_event_repo import MongoEventRepository
from core.config import settings
from application.services.event_service import EventService

repo = MongoEventRepository(uri=settings.MONGO_URI, db_name=settings.MONGO_DB)
event_service = EventService(repo=repo)