import json
import traceback
from asyncio import AbstractEventLoop
from uuid import UUID

from aio_pika import connect_robust, IncomingMessage
from aio_pika.abc import AbstractRobustConnection

from app.services.order_service import OrderService
from app.settings import settings


async def process_created_order(msg: IncomingMessage):
    try:
        data = json.loads(msg.body.decode())
        OrderService().create_order(data['title'], data['description'], UUID(data['user_id']))
        await msg.ack()
    except:
        traceback.print_exc()
        await msg.ack()


async def consume(loop: AbstractEventLoop) -> AbstractRobustConnection:
    connection = await connect_robust(settings.amqp_url, loop=loop)
    channel = await connection.channel()

    task_created_queue = await channel.declare_queue('created_order', durable=True)

    await task_created_queue.consume(process_created_order)
    print('Ура победа оно запустилось спустя 100500 миллионов лет')

    return connection