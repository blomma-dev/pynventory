from models import Product
from database import get_connection


# create a list of commands
available_commands = ["add", "del", "modify", "list", "help", "exit"]


# create function to list commands
def list_commands():
    print("Incorrect command, available commands below:\n")
    print(*available_commands, sep=", ")
    print()


# function to add a new product
def add_item():
    # connecting to sqlite database
    conn = get_connection()

    # creating a cursor object using the cursor() method
    cursor = conn.cursor()

    print("Enter product details below.\n")

    # asking for item type until correct value is entered
    while True:
        item_type = input("Enter product type (physical = p / digital = d): ").strip().lower()
        if item_type in ["p", "d"]:
            break
        print("Invalid input. Enter 'p' or 'd'.\n")

    # asking for category until something is entered
    while True:
        category = input("Enter category: ").strip()
        if category:
            break
        print("Category cannot be empty.\n")

    # asking for brand name until something is entered
    while True:
        brand_name = input("Enter brand name: ").strip()
        if brand_name:
            break
        print("Brand name cannot be empty.\n")

    # asking for product name until something is entered
    while True:
        product_name = input("Enter product name: ").strip()
        if product_name:
            break
        print("Product name cannot be empty.\n")

    # asking for buy price until a valid number is entered
    while True:
        try:
            price_buy = float(input("Enter buy price: ").strip())
            if price_buy < 0:
                print("Buy price cannot be negative.\n")
                continue
            break
        except ValueError:
            print("Buy price must be a number.\n")

    # asking for sell price until a valid number is entered
    while True:
        try:
            price_sell = float(input("Enter sell price: ").strip())
            if price_sell < 0:
                print("Sell price cannot be negative.\n")
                continue
            break
        except ValueError:
            print("Sell price must be a number.\n")

    # asking for tax percentage until a valid number is entered
    while True:
        try:
            tax_percentage = float(input("Enter tax percentage: ").strip())
            if tax_percentage < 0:
                print("Tax percentage cannot be negative.\n")
                continue
            break
        except ValueError:
            print("Tax percentage must be a number.\n")

    # creating product object only after all required fields are valid
    product = Product(
        item_type,
        category,
        brand_name,
        product_name,
        price_buy,
        price_sell,
        tax_percentage
    )

    # inserting the product into the database only after everything is complete
    cursor.execute("""
        INSERT INTO product (
            item_type,
            category,
            brand_name,
            product_name,
            price_buy,
            price_sell,
            tax_percentage
        )
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        product.item_type,
        product.category,
        product.brand_name,
        product.product_name,
        product.price_buy,
        product.price_sell,
        product.tax_percentage
    ))

    # storing the automatically generated id in the product object
    product.id = cursor.lastrowid

    # commit changes in the database
    conn.commit()

    print("\nProduct added successfully.")
    print(f"Assigned ID: {product.id}")
    print(f"Profit: {product.profit:.2f} not including tax.\n")

    # closing the connection
    conn.close()

def del_item():
    # connecting to sqlite database
    conn = get_connection()

    # creating a cursor object using the cursor() method
    cursor = conn.cursor()

    # ask user for row ID to delete
    row_to_delete = input("Enter product ID to delete: ")

    # fetch the product by id and print the row information
    cursor.execute("SELECT id, brand_name, product_name FROM product WHERE id =?", (row_to_delete))
    print(f"Selected ID is: {cursor.fetchone()}")
    
    # init action to None as default and while action is not true
    # ask user for confirmation if the selected row should be deleted
    # if yes, delete -> return true -> exit
    # else/incorrect answer -> loop again
    action = None
    while action != True:
        answer = input("Are you sure you want to delete this product? yes/no: ")
        if answer == "yes":
            cursor.execute("DELETE FROM product WHERE id=?", (row_to_delete))
            print(f"Product for ID {row_to_delete} is removed.")
            conn.commit()
            conn.close()
            return True
            
        else: 
            print("Incorrect answer: yes/no")
            return False
    


# function to list all products in the database
def list_items():
    # connecting to sqlite database
    conn = get_connection()

    # creating a cursor object using the cursor() method
    cursor = conn.cursor()

    # selecting all products from the table
    cursor.execute("""
        SELECT id, item_type, category, brand_name, product_name, price_buy, price_sell, tax_percentage
        FROM product
    """)

    # fetching all rows from the query result
    products = cursor.fetchall()

    # checking if there are no products in the database
    if not products:
        print("No products found.\n")
    else:
        print("\nProducts:\n")
        for product in products:
            print(
                f"ID: {product[0]}, "
                f"Type: {product[1]}, "
                f"Category: {product[2]}, "
                f"Brand: {product[3]}, "
                f"Name: {product[4]}, "
                f"Buy: {product[5]:.2f}, "
                f"Sell: {product[6]:.2f}, "
                f"Tax: {product[7]:.2f}%"
            )
        print()

    # closing the connection
    conn.close()