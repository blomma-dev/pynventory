from datetime import datetime

class Product:
    def __init__(self, id, type, category, brand_name, product_name, price_buy, price_sell, tax_percentage):
        self.id = id
        self.type = type
        self.category = category
        self.brand_name = brand_name
        self.product_name = product_name
        self.price_buy = price_buy
        self.price_sell = price_sell
        self.tax_percentage = tax_percentage
        self.profit = price_sell - price_sell

products = []

def list_commands():
    command = input("Enter command:\n")

    if command not in  ("add", "del", "modify", "list", "help"):
        print("Invalid command, type \"help\" to see all available commands.")
    
    if command == "add":
        print("Enter product:\n")
        id = int(input("Enter product ID:\n"))
        if not isinstance(id, int):
            print("ID can only be integer.") 
        else:
            products.append(id)

        print("Enter product type (physical / digital)")

def main():
    print("Welcome to Pynventory!\n")
    print("Type \"help\" to see available commands.\n")
    list_commands()

main()