from dataclasses import dataclass
from datetime import datetime
from uuid import UUID
from typing import Optional

@dataclass
class Event:
    conflict_id: UUID
    event_type: str
    user_id: Optional[UUID]
    item_id: Optional[UUID]
    old_value: Optional[str]
    new_value: Optional[str]
    timestamp: datetime