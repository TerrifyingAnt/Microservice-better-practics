from uuid import uuid4, UUID

import pytest

from app.models.order import Order, OrderStatuses
from app.repositories.order_repo import OrderRepo


@pytest.fixture()
def order_repo() -> OrderRepo:
    repo = OrderRepo()
    return repo


@pytest.fixture()
def first_order() -> Order:
    return Order(id=UUID("2174e1ed-b7bb-465f-8b43-4867f44dc9f9"), title="Test", description="description",
                status=OrderStatuses.CREATED, user_id=UUID("2174e1ed-b7bb-465f-8b43-4867f44dc9f9"))


@pytest.fixture()
def second_order() -> Order:
    return Order(id=uuid4(), title="Test", description="description",
                status=OrderStatuses.CREATED, user_id=UUID("2174e1ed-b7bb-465f-8b43-4867f44dc9f9"))


def test_empty_list(order_repo: OrderRepo) -> None:
    assert order_repo.get_orders() == []


def test_add_order(order_repo: OrderRepo, first_order: Order) -> None:
    order_repo.create_order(first_order)
    orders = order_repo.get_orders()
    assert len(orders) == 1
    assert orders[0] == first_order


def test_add_duplicate_order_error(order_repo: OrderRepo, first_order: Order) -> None:
    with pytest.raises(KeyError):
        order_repo.create_order(first_order)


def test_get_order_by_id(order_repo: OrderRepo, first_order: Order) -> None:
    retrieved_order = order_repo.get_order_by_id(first_order.id)
    assert retrieved_order == first_order


def test_done_order(order_repo: OrderRepo, first_order: Order) -> None:
    order_repo.done_order(first_order)
    orders = order_repo.get_orders()
    print(orders[0].status)
    assert orders[0].status == OrderStatuses.DONE


def test_get_order_by_id_error(order_repo: OrderRepo) -> None:
    with pytest.raises(KeyError):
        order_repo.get_order_by_id(uuid4())
