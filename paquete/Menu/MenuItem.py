# MenuItem.py

# Se vuelven a organizar las clases de la misma forma que en las 
# anteriores versiones de Restaurant, pero esta vez organizadas en 
# paquetes como se ha aprendido, y con atributos y métodos nuevamente 
# públicos, para mayor brevedad: 

class MenuItem:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price
    
    def calculate_total_price(self, quantity = int):
        return self.price * quantity
    
    
from collections import namedtuple

# se crea la namedtuple
MenuEntry = namedtuple('MenuEntry', ['name', 'price', 'category'])
# Beverage = namedtuple("Beverage", ["name", "price", "size"])
# Appetizer = namedtuple("Beverage", ["name", "price", "flavor"])
# Dessert = namedtuple("Beverage", ["name", "price", "type_of_dessert"])
# MainCourse = namedtuple("Beverage", ["name", "price", "type_of_cooking"])

# beverage = MenuEntry("Coca Cola", "$5000", "beverage")