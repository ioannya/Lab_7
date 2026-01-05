from domain.order import Order
from domain.money import Money


class OrderRepository:
    def get_by_id(self, order_id: str) -> Order:
        raise NotImplementedError

    def save(self, order: Order):
        raise NotImplementedError


class PaymentGateway:
    def charge(self, order_id: str, money: Money) -> bool:
        raise NotImplementedError
