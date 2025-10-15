from dataclasses import dataclass
from datetime import datetime
from typing import Optional
from uuid import  UUID


@dataclass
class Conflict:
    title: str
    creator_id: UUID
    partner_id: Optional[UUID]  
    id: UUID
    
    status: str
    slug: str
    progress: float
    created_at: datetime 
    resolved_at: Optional[datetime]

    deleted_by_creator: bool
    deleted_by_partner: bool

    truce_status: str
    truce_initiator_id: Optional[UUID]

    items: list[dict]
    events: list[dict]