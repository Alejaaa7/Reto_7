# Payment.py

from ..Order import Order

class Payment:
    def __init__(self):
        pass

    def pay(self, amount: Order):
        raise NotImplementedError("Subclasses must implement Pay()!")
    
