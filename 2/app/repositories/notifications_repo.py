from typing import List
from uuid import UUID

from app.models.notification import Notification

notifications: List[Notification] = []


class NotificationRepo:
    def get_notifications(self) -> list[Notification]:
        return notifications
    
    def create_notification(self, new_notification: Notification) -> Notification:
        if len([t for t in notifications if t.id == new_notification.id]) > 0:
            raise KeyError

        notifications.append(new_notification)

        return new_notification