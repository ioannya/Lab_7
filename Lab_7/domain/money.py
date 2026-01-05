from dataclasses import dataclass


@dataclass(frozen=True)
class Money:
    amount: int
    currency: str = "EUR"

    def __post_init__(self):
        if self.amount < 0:
            raise ValueError("Money cannot be negative")

    def __add__(self, other: "Money") -> "Money":
        if self.currency != other.currency:
            raise ValueError("Currency mismatch")
        return Money(self.amount + other.amount, self.currency)

    def __mul__(self, qty: int) -> "Money":
        return Money(self.amount * qty, self.currency)
