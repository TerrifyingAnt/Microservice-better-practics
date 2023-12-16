import asyncio
from fastapi import FastAPI
from app import rabbitmq_consume
from app.routers.notification_route import notification_router

app = FastAPI(title='Notification service')


@app.on_event('startup')
async def startup():
    loop = asyncio.get_event_loop()
    asyncio.ensure_future(rabbitmq_consume.consume(loop))


app.include_router(notification_router, prefix='/api')