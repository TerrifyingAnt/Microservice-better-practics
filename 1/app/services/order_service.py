import traceback
import uuid
from uuid import UUID

import requests

from app.models.order import Order, OrderStatuses
from app.repositories.order_repo import OrderRepo
from app.rabbitmq_produce import send_notification
from app.utils.utils import order_string_status_to_enum


class OrderService:
    order_repo: OrderRepo

    def __init__(self) -> None:
        """конструктор"""
        self.order_repo = OrderRepo()

    def get_orders(self) -> list[Order]:
        """метод для получения всех заказов"""
        return self.order_repo.get_orders()

    def create_order(self, title: str, description: str, user_id: UUID):
        """метод создания заказа"""
        new_order = Order(id=uuid.uuid4(), title=title, description=description, user_id=user_id,
                            status=OrderStatuses.CREATED)
        send_notification(new_order)
        return self.order_repo.create_order(new_order)

    def done_order(self, order_id: UUID) -> Order:
        """метод устанавливает статус завершенного заказа"""
        order = self.order_repo.get_order_by_id(order_id)

        if order.status == OrderStatuses.DONE:
            raise ValueError

        order.status = OrderStatuses.DONE
        send_notification(order)
        return self.order_repo.done_order(order)
    
    def change_order_status(self, order_id: UUID, order_status: str) -> Order:
        """метод меняет статус заказа на произвольный"""
        order_status_enum = order_string_status_to_enum(order_status)
        order = self.order_repo.get_order_by_id(order_id, order_status_enum)
        send_notification(order)
        return self.order_repo.change_order_status(order_id, order_status_enum)

