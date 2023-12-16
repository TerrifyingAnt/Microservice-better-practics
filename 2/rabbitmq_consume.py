import json
import traceback
from uuid import UUID
from asyncio import AbstractEventLoop
from aio_pika.abc import AbstractRobustConnection
from aio_pika import connect_robust, IncomingMessage

from app.rabbitmq_produce import send_notification
from app.settings import settings
from app.services.notification_service import NotificationService


async def process_created_notification(msg: IncomingMessage):
    try:
        data = json.loads(msg.body.decode())
        NotificationService().create_notification(data['message'], UUID(data['user_id']))
        send_notification(data)
        await msg.ack()
    except:
        traceback.print_exc()
        await msg.ack()


async def consume(loop: AbstractEventLoop) -> AbstractRobustConnection:
    connection = await connect_robust(settings.amqp_url, loop=loop)
    channel = await connection.channel()

    notification_created_queue = await channel.declare_queue('orlov_notification_created_queue', durable=True)

    await notification_created_queue.bind('orlov_notification_created_exchange', routing_key="notification_service")

    await notification_created_queue.consume(process_created_notification)
    print('Started RabbitMQ consuming...')

    return connection