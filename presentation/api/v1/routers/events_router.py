from fastapi import APIRouter, Depends
from application.dtos.event_dto import EventDTO
from application.services.event_service import EventService
from presentation.dependencies.service_factories import get_event_service


router = APIRouter(prefix="/events")


@router.post("/", summary="Сохранить событие")
async def save_event_endpoint(
    event: EventDTO, service: EventService = Depends(get_event_service)
):
    await service.save_event(event)
    return {"status": "ok"}


