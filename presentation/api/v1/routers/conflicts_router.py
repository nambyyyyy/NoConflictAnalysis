from fastapi import APIRouter, Depends
from application.dtos.conflict_dto import ConflictDTO
from application.services.conflict_service import ConflictService
from presentation.dependencies.service_factories import get_conflict_service

router = APIRouter(prefix="/conflicts")


@router.post("/", summary="Сохранить завершенный конфликт (JSON)")
async def save_conflict_endpoint(
    conflict: ConflictDTO, service: ConflictService = Depends(get_conflict_service)
):
    await service.save_conflict(conflict)
    return {"status": "ok"}


