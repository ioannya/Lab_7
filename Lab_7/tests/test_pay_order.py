import pytest

from domain.order import Order
from domain.order_line import OrderLine
from domain.money import Money
from domain.order_status import OrderStatus

from application.pay_order_use_case import PayOrderUseCase
from infr.in_memory_order_repository import InMemoryOrderRepository
from infr.fake_payment_gateway import FakePaymentGateway


def test_success_payment():
    repo = InMemoryOrderRepository()
    gateway = FakePaymentGateway()

    order = Order("1")
    order.add_line(OrderLine("p1", 2, Money(100)))
    repo.add(order)

    use_case = PayOrderUseCase(repo, gateway)
    result = use_case.execute("1")

    assert result.amount == 200
    assert order.status == OrderStatus.PAID


def test_cannot_pay_empty_order():
    repo = InMemoryOrderRepository()
    gateway = FakePaymentGateway()

    order = Order("2")
    repo.add(order)

    use_case = PayOrderUseCase(repo, gateway)

    with pytest.raises(ValueError):
        use_case.execute("2")


def test_cannot_pay_twice():
    order = Order("3")
    order.add_line(OrderLine("p", 1, Money(100)))
    order.pay()

    with pytest.raises(ValueError):
        order.pay()


def test_cannot_modify_after_payment():
    order = Order("4")
    order.add_line(OrderLine("p", 1, Money(100)))
    order.pay()

    with pytest.raises(ValueError):
        order.add_line(OrderLine("x", 1, Money(50)))


def test_total_is_correct():
    order = Order("5")
    order.add_line(OrderLine("a", 2, Money(100)))
    order.add_line(OrderLine("b", 1, Money(50)))

    assert order.total().amount == 250
