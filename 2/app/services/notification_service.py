import uuid
from uuid import UUID

from app.models.notification import Notification
from app.repositories.notifications_repo import NotificationRepo


class NotificationService:
    notification_repo: NotificationRepo

    def __init__(self) -> None:
        self.notification_repo = NotificationRepo()

    def get_notifications(self) -> list[Notification]:
        return self.notification_repo.get_notifications()
    
    def create_notification(self, message: str, user_id: UUID):
        new_notification = Notification(id=uuid.uuid4(), message=message, user_id=user_id)

        return self.notification_repo.create_notification(new_notification)