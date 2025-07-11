# main.py

from paquete.Restaurant.Restaurant import Restaurant
from paquete.Menu.MenuManager import MenuManager

def show_menu():
    print("\n --- MENU ---")
    print("1. Show menu.")
    print("2. Add item to menu.")
    print("3. Update price.")
    print("4. Delete item from menu.")
    print("5. Add new order.")
    print("6. Save and close.")
    

def main():
    restaurant = Restaurant()
    restaurant.load_menu()

    while True:
        show_menu()
        option = input("Choose an option: ")

        if option == "1":
            restaurant.menu_manager.show_menu()

        elif option == "2":
            nombre = input("Name: ")
            precio = float(input("Price: "))
            categoria = input("Category (beverage, appetizeer, maincourse, dessert): ")
            restaurant.menu_manager.add_item(nombre, precio, categoria)

        elif option == "3":
            nombre = input("Name of the item to be updated: ")
            nuevo_precio = float(input("New price: "))
            restaurant.menu_manager.update_price(nombre, nuevo_precio)

        elif option == "4":
            nombre = input("Name of the item to be deleted: ")
            restaurant.menu_manager.delete_item(nombre)

        elif option == "5":
            restaurant.menu_manager.show_menu()
            order = []
            while True:
                nombre = input("Name of the new item (or 'end' to finish): ")
                if nombre.lower() == "end":
                    break
                elif nombre in restaurant.menu_manager.menu:
                    cantidad = int(input("Quantity: "))
                    order.append((nombre, cantidad))
                else:
                    print("This item is not on the menu.")
            restaurant.add_order(order)

        elif option == "6":
            restaurant.save_menu()
            print("Menu saved.")
            break
        
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()