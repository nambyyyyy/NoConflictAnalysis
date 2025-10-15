from application.dtos.conflict_dto import ConflictDTO
from core.entities.conflict_entity import Conflict
from core.interfaces.conflict_interface import ConflictRepository
from typing import Optional
from bson import ObjectId


class ConflictService:

    def __init__(self, repo: ConflictRepository) -> None:
        self.repo = repo

    async def save_conflict(self, conflict_dto: ConflictDTO) -> None:
        conflict: Conflict = self._to_entity(conflict_dto)
        inserted_id: Optional[ObjectId] = await self.repo.save(conflict)
        if inserted_id is None:
            # add custom error
            raise

    def _to_entity(self, conflict_dto: ConflictDTO) -> Conflict:
        return Conflict(
            title=conflict_dto.title,
            creator_id=conflict_dto.creator_id,
            partner_id=conflict_dto.partner_id,
            id=conflict_dto.id,
            status=conflict_dto.status,
            slug=conflict_dto.slug,
            progress=conflict_dto.progress,
            created_at=conflict_dto.created_at,
            resolved_at=conflict_dto.resolved_at,
            deleted_by_creator=conflict_dto.deleted_by_creator,
            deleted_by_partner=conflict_dto.deleted_by_partner,
            truce_status=conflict_dto.truce_status,
            truce_initiator_id=conflict_dto.truce_initiator_id,
            items=conflict_dto.items,
            events=conflict_dto.events,
        )
