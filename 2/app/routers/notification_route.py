from fastapi import APIRouter, Depends

from app.models.notification import Notification
from app.services.notification_service import NotificationService

notification_router = APIRouter(prefix='/notification', tags=['Notification'])


@notification_router.get('/')
def get_notifications(notification_service: NotificationService = Depends(NotificationService)) -> list[Notification]:
    return notification_service.get_notifications()