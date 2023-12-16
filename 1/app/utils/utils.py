from app.models.order import OrderStatuses

def order_string_status_to_enum(order_status_str: str) -> OrderStatuses:
    if order_status_str == OrderStatuses.CREATED:
        return OrderStatuses.CREATED
    elif order_status_str == OrderStatuses.PROCESSING:
        return OrderStatuses.PROCESSING
    elif order_status_str == OrderStatuses.IN_WORK:
        return OrderStatuses.IN_WORK
    else:
        return OrderStatuses.DONE
