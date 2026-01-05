class FakePaymentGateway:
    def __init__(self):
        self.calls = []

    def charge(self, order_id, money):
        self.calls.append((order_id, money))
        return True
