# Restaurant.py

# Se crea una nueva clase superior restaurant, que será quien recibe, 
# almacena y despacha pedidos:

from ..Order import Order
from ..Menu.MenuManager import MenuManager
from ..Menu.MenuItem import MenuItem
from queue import Queue

class Restaurant:
    def __init__(self):
        self.order_queue = Queue()
        self.menu_manager = MenuManager()

    def add_order(self, order):
        self.order_queue.put(order) # se van añadiendo las órdenes a la cola

    def show_next_order(self):
        if not self.order_queue.empty():
            next_order = self.order_queue.queue[0] # deja ver el pedido sin quitarlo
            return next_order
        else:
            print("There are no more orders in queue.")
            return None
        
    def process_next_order(self):
        if not self.order_queue.empty():
            return self.order_queue.get()
        else:
            print("There are no orders to process.")
            return None
        
    def show_all_orders(self):
        if self.order_queue.empty():
            print("There are no pending orders.")
            return
        
        print("List of orders in queue: ")
        orders_list = list(self.order_queue.queue)
        for i in range(len(orders_list)):
            print(f"\n Order {i+1}")
            orders_list[i].print_order()

        # if not self.menu_manager.menu:
        #     print("The menu is currently empty.")
        #     return
        # print("MENU: ")
        # for name, data in self.menu_manager.menu.items():
        #     price = data['price']
        #     category = data['category']
        #     print(f"    - {name} - ${price} ({category})")
        # if self.order_queue.empty():
        #     print("There are no orders. :c)")
        #     return # sale
        # print("Pedidos en cola: ")

        # orders_list = list(self.order_queue.queue) # comvertir la cola en lista
        # i = 1 # empezar a contar desde 1 es más normal que desde 0
        # for order in orders_list:
        #     print(f"\nPedido {i}: ")
        #     order.print_order()
        #     i += 1         

    def load_menu(self):
        self.menu_manager.load_from_json()

    def save_menu(self):
        self.menu_manager.save_to_json()

