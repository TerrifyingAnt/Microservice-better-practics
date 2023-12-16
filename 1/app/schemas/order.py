from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column

from app.models.order import OrderStatuses
from app.schemas.base_schema import Base


class Order(Base):
    __tablename__ = 'tasks'

    id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True)
    title: Mapped[str]
    description: Mapped[str]
    status: Mapped[OrderStatuses]
    user_id: Mapped[UUID] = mapped_column(UUID(as_uuid=True))