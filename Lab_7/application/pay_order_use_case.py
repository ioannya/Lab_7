from application.interfaces import OrderRepository, PaymentGateway


class PayOrderUseCase:
    def __init__(self, repo: OrderRepository, gateway: PaymentGateway):
        self.repo = repo
        self.gateway = gateway

    def execute(self, order_id: str):
        order = self.repo.get_by_id(order_id)
        money = order.pay()
        self.gateway.charge(order_id, money)
        self.repo.save(order)
        return money
