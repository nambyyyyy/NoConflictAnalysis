from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional, List, Dict
from uuid import UUID


class ConflictDTO(BaseModel):
    """Полный снимок конфликта передан из Django."""

    id: UUID = Field(..., description="ID конфликта")
    creator_id: UUID = Field(..., description="Создатель конфликта")
    partner_id: Optional[UUID] = Field(None, description="Партнёр по конфликту")
    title: str
    status: str
    slug: str
    progress: float
    created_at: datetime
    resolved_at: Optional[datetime]
    deleted_by_creator: bool
    deleted_by_partner: bool
    truce_status: str
    truce_initiator_id: Optional[UUID] = None
    items: List[Dict] = Field(default_factory=list, description="Список пунктов анкеты")
    events: List[Dict] = Field(
        default_factory=list, description="Список связанных событий"
    )

    class Config:
        anystr_strip_whitespace = True
