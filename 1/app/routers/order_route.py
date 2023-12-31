from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException

from app.models.order import Order
from app.services.order_service import OrderService

order_router = APIRouter(prefix='/order', tags=['Order'])


@order_router.get('/')
def get_tasks(order_service: OrderService = Depends(OrderService)) -> list[Order]:
    return order_service.get_orders()


@order_router.post('/{id}/done')
def done_order(id: UUID, order_service: OrderService = Depends(OrderService)) -> Order:
    try:
        order = order_service.done_order(id)
        return order
    except KeyError:
        raise HTTPException(404, f'Заказ {id} не создан')
    except ValueError:
        raise HTTPException(400, f'Заказ {id} не может быть выполнен')
    
@order_router.post('/{id}/change/{order_status}')
def done_order(id: UUID, order_status: str, order_service: OrderService = Depends(OrderService)) -> Order:
    try:
        order = order_service.change_order_status(id, order_status)
        return order
    except KeyError:
        raise HTTPException(404, f'Заказ {id} не создан')
    except ValueError:
        raise HTTPException(400, f'Заказ {id} не может быть выполнен')