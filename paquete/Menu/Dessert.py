# Dessert.py

from .MenuItem import MenuItem

class Dessert(MenuItem):
    def __init__(self, name: str, price: float, type_of_dessert: str):
        super().__init__(name, price)
        self.type_of_dessert = type_of_dessert
        