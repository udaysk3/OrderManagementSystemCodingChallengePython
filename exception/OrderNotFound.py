class OrderNotFound(Exception):
    def __init__(self, message="Order not found."):
        self.message = message
        super().__init__(self.message)