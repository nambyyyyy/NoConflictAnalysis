from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional
from uuid import UUID


class EventDTO(BaseModel):
    """Событие изменения анкет или статуса конфликта."""

    conflict_id: UUID = Field(..., description="ID конфликта")
    event_type: str = Field(
        ..., description="Тип события"
    )
    user_id: Optional[UUID] = Field(
        None, description="Пользователь, совершивший действие"
    )
    item_id: Optional[UUID] = Field(
        None, description="ID пункта анкеты, если применимо"
    )
    old_value: Optional[str] = Field(None, description="Старое значение")
    new_value: Optional[str] = Field(None, description="Новое значение")
    timestamp: datetime = Field(
        default_factory=datetime.utcnow, description="Время события"
    )

    class Config:
        anystr_strip_whitespace = True
