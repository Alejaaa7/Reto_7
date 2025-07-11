# Beverage.py

from .MenuItem import MenuItem

class Beverage(MenuItem):
    def __init__(self, name: str, price: float, size: str):
        super().__init__(name, price)
        self.size = size

    def calculate_total_price(self, quantity: int):
        return super().calculate_total_price(quantity) * 0.8
