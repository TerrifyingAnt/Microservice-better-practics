from uuid import UUID

from pydantic import BaseModel, ConfigDict


class Notification(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: UUID
    message: str
    user_id: UUID