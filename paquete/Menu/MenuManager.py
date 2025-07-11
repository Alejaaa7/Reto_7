# MenuManager.py

# esta nueva clase es para usar el namedtuple creado, poder almacenar el
# menú como diccionario, agregar las funciones de add, update, delete, 
# items. Y hacerlo como JSON

import json
from .MenuItem import MenuEntry

class MenuManager:
    def __init__(self):
        self.menu = {} # usar un diccionario

    def add_item(self, name: str, price: float, category: str):
        self.menu[name] = {
            'price': price,
            'category': category 
        }
        print(f"Added: {name} - ${price} -> {category}.")

    def update_price(self, name: str, new_price: float):
        if name in self.menu:
            self.menu[name]["price"] = new_price
            print(f"Price of {name} updated to: ${new_price: .2f}")
        else:
            print("Item not found.")

    def delete_item(self, name:str):
        removed = self.menu.pop(name, None)
        if removed:
            print(f"{name} eliminated.")
        else:
            print("Item not found.")
    
    def show_menu(self):
        print("Menu: ")
        if not self.menu:
            print("Empty menu.")
            return
        
        for name, data in self.menu.items(): 
            # data es el subdiccionario con price y category
            print(f"{name} - ${data['price']} ({data['category']})")

    def save_to_json(self, filename = "menu.json"):
        archivo = open(filename, "w") # para abrir el archivo en modo escritura
        contenido = json.dumps(self.menu) # para convertir el diccionario a texto JSON
        archivo.write(contenido) #escribir el texto en el archivo
        archivo.close() 

        print("Menu saved successfully.")

    def load_from_json(self, filename = "menu.json"):
        try:
            archivo = open(filename, "r") # para abrirlo en modo lectura
            contenido = archivo.read() # para leet el texto completo
            self.menu = json.loads(contenido) # convertir el texto a diccionario
            archivo.close()

            print("Menu loaded successfully.")
        except FileNotFoundError:
            print("The file does not exist.")