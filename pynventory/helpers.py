
# print options as helper function
# remember to import the function at functions.py

# main menu help function
def main_help_dialog():
    print("""
    Available commands:
        add  - Add products to inventory database
        del  - Delete products from inventory database
        mod  - Modify product data
        list - List all product data
        help - Show help
        exit - Exit the program
    """)

# modify menu help function
def modify_help_dialog():
    print("""
    Modifiable columns:
        category
        brand
        name
        buy price
        sell price
        tax
        weigh
        stock

    Commands:
        list - List all product data
        help - Show help
        exit - Exit to main menu
    """)

# delete menu help function
def delete_help_dialog():
    print("""
    List product ID's with 'list' command.

    Commands:
        list - List all product data
        help - Show help
        exit - Exit to main menu
    """)

# create a list of commands
available_commands = ["add", "del", "mod", "list", "help", "exit"]

# create function to list commands
def list_commands():
    print("Incorrect command.")
    main_help_dialog()

def print_options(title, options):
    print(title)
    for option in options:
        print(f"- {option}")
    print()

def print_product_brief(product):
    print(f"\nCategory: {product[2]}")
    print(f"Brand: {product[3]}")
    print(f"Name: {product[4]}")
    print(f"Buy price: {product[5]}")
    print(f"Sell price: {product[6]}")
    print(f"Tax: {product[7]}")
    print(f"Weight: {product[8]}")
    print(f"Stock: {product[9]}\n")
