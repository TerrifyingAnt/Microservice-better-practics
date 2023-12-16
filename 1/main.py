import asyncio
from fastapi import FastAPI
from app import rabbitmq_consume
from app.routers.order_route import order_router

app = FastAPI(title='Orders')


@app.on_event('startup')
async def startup():
    loop = asyncio.get_event_loop()
    asyncio.ensure_future(rabbitmq_consume.consume(loop))


app.include_router(order_router, prefix='/api')