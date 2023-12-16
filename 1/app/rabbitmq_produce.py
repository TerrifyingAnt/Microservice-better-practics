import json

import pika

from app.models.order import OrderStatuses
from app.settings import settings


def send_notification(order):
    connection = pika.BlockingConnection(pika.URLParameters(settings.amqp_url))
    channel = connection.channel()

    if order.status == OrderStatuses.CREATED:
        message = f"Создан новый заказ: {order.title}. Нужно сделать: {order.description}"
    elif order.status == OrderStatuses.PROCESSING:
        message = f"Статус заказа \"{order.title}\" изменен: \"Создан\" -> \"Обрабатывается\"."
    elif order.status == OrderStatuses.IN_WORK:
        message = f"Статус заказа \"{order.title}\" изменен: \"Обрабатывается\" -> \"В работе\"."
    else:
        message = f"Статус заказа \"{order.title}\" изменен: \"В работе\" -> \"Выполнен\". Заказ будет передан в доставку в ближайшее время."

    new_notification = {
        "message": message,
        "user_id": str(order.user_id),
        "status": str(order.status)
    }

    channel.exchange_declare(exchange='notifications_exchange', exchange_type='direct', durable=True)
    message_body = json.dumps(new_notification)

    channel.basic_publish(exchange='notifications_exchange', routing_key="notification_service",
                          body=message_body.encode('utf-8'))

    connection.close()