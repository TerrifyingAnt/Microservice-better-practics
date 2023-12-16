import traceback
from uuid import UUID
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.order import Order, OrderStatuses
from app.schemas.order import Order as DBOrder


class OrderRepo:
    db: Session

    def __init__(self) -> None:
        self.db = next(get_db())

    def _map_to_model(self, order: DBOrder) -> Order:
        result = dict(Order.model_validate(order))
        result = Order(id=result["id"], title=result["title"], description=result["description"], status=result["status"], user_id=result["user_id"])
        return result

    def _map_to_schema(self, order: Order) -> DBOrder:
        data = dict(order)
        data['user_id'] = order.id if order != None else None
        result = DBOrder(**data)

        return result

    def get_orders(self) -> list[Order]:
        orders = []
        for t in self.db.query(DBOrder).all():
            orders.append(self._map_to_model(t))
        return orders

    def get_order_by_id(self, id: UUID) -> Order:
        order = self.db \
            .query(DBOrder) \
            .filter(DBOrder.id == id) \
            .first()
        if order == None:
            raise KeyError
        return self._map_to_model(order)

    def create_order(self, order: Order) -> Order:
        try:
            db_order = self._map_to_schema(order)
            self.db.add(db_order)
            self.db.commit()
            return order
        except:
            traceback.print_exc()
            raise KeyError

    def done_order(self, order: Order) -> Order:
        db_order = self.db.query(DBOrder).filter(
            DBOrder.id == order.id).first()
        db_order.status = OrderStatuses.DONE
        self.db.commit()
        return self._map_to_model(db_order)
    
    def change_order_status(self, order_id: UUID, order_status: OrderStatuses) -> Order:
        db_order = self.db.query(DBOrder).filter(
            DBOrder.id == order_id).first()
        db_order.status = order_status
        self.db.commit()
        return self._map_to_model(db_order)
