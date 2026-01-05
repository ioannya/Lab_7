from dataclasses import dataclass
from domain.money import Money


@dataclass(frozen=True)
class OrderLine:
    product_id: str
    quantity: int
    price: Money

    def total(self) -> Money:
        return self.price * self.quantity
