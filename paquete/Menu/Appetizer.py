# Apetizer.py

from .MenuItem import MenuItem

class Appetizer(MenuItem):
    def __init__(self, name: str, price: float, flavor: str):
        super().__init__(name, price)
        self.flavor = flavor
        