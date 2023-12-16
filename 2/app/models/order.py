import enum
from uuid import UUID

from pydantic import BaseModel, ConfigDict


class OrderStatuses(enum.Enum):
    CREATED = 'CREATED'
    PROCESSING = 'PROCESSING'
    IN_WORK = 'IN_WORK'
    DONE = 'DONE'




class Order(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: UUID
    title: str
    description: str
    status: OrderStatuses
    user_id: UUID

