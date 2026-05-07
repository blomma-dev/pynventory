
# print options as helper function
# remember to import the function at functions.py

# main menu help function
def main_show_help():
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
def modify_show_help():
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

def print_options(title, options):
    print(title)
    for option in options:
        print(f"- {option}")
    print()


