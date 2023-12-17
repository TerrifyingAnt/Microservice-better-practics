import pytest
from uuid import uuid4
from pydantic import ValidationError
from app.models.order import Order, OrderStatuses


@pytest.fixture()
def any_order() -> Order:
    return Order(
        id=uuid4(),
        title='Test Order',
        description='Order description',
        status=OrderStatuses.CREATED,
        user_id=uuid4()
    )


def test_order_creation(any_order: Order):
    assert dict(any_order) == {
        'id': any_order.id,
        'title': any_order.title,
        'description': any_order.description,
        'status': any_order.status,
        'user_id': any_order.user_id
    }


def test_order_invalid_status(any_order: Order):
    with pytest.raises(ValidationError):
        Order(
            id=uuid4(),
            title='Test Order',
            description='Order description',
            status='invalid_status',
            user_id=uuid4()
        )
