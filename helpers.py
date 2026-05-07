
# print options as helper function
# remember to import the function at functions.py

def show_help():
    print("""
    Available commands:
        add  - Add products to inventory database
        del  - Delete products from inventory database
        mod  - Modify product data
        list - List all product data
        help - Show help
        exit - Exit the program 
    """)

def print_options(title, options):
    print(title)
    for option in options:
        print(f"- {option}")
    print()


