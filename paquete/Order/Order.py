# Order.py

from ..Menu.MenuItem import MenuItem

class Order:
    def __init__(self):
        self.items = []

    def add_item(self, item: MenuItem, quantity: int):
        self.items.append((item, quantity))

    def calculate_total_bill(self):
        total = 0
        for item, quantity in self.items:
            total += item.calculate_total_price(quantity)
        
        return total
    
    def apply_discount(self, discount_percentaje: float):
        discount_percentaje = 0
        total = self.calculate_total_bill()
        if total > 100000:
            discount_percentaje += 10
        elif total > 50000:
            discount_percentaje += 5

        discount = total * (discount_percentaje / 100)

        return total - discount
    
    def print_order(self):
        print("Los detalles del pedido son:")

        for item, quantity in self.items:
            print(f"{item.name}(x{quantity}): "
        f"${item.calculate_total_price(quantity): .2f}")
            
        print(f"Total without discount: ${self.calculate_total_bill(): .2f}")

        print(f"Total: ${self.apply_discount(): .2f}")

