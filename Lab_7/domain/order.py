from domain.money import Money
from domain.order_line import OrderLine
from domain.order_status import OrderStatus


class Order:
    def __init__(self, order_id: str):
        self.order_id = order_id
        self.lines: list[OrderLine] = []
        self.status = OrderStatus.DRAFT

    def add_line(self, line: OrderLine):
        if self.status == OrderStatus.PAID:
            raise ValueError("Cannot modify paid order")
        self.lines.append(line)

    def total(self) -> Money:
        total = Money(0)
        for line in self.lines:
            total += line.total()
        return total

    def pay(self) -> Money:
        if not self.lines:
            raise ValueError("Cannot pay empty order")
        if self.status == OrderStatus.PAID:
            raise ValueError("Order already paid")

        self.status = OrderStatus.PAID
        return self.total()
