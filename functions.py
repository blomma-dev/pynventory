from database import get_connection
from models import Product

# create a list of commands
available_commands = ["add", "del", "mod", "list", "help", "exit"]


def print_options(title, options):
    print(title)
    for option in options:
        print(f"- {option}")
    print()


def is_non_negative_number(value):
    text = value.strip()
    if not text:
        return False
    if text.count(".") > 1:
        return False
    if text.startswith("-"):
        return False
    number_part = text.replace(".", "", 1)
    return number_part.isdigit()


def print_product_brief(product):
    print(f"\nCategory: {product[2]}")
    print(f"Brand: {product[3]}")
    print(f"Name: {product[4]}")
    print(f"Buy price: {product[5]}")
    print(f"Sell price: {product[6]}")
    print(f"Tax: {product[7]}\n")


# create function to list commands
def list_commands():
    print_options("Incorrect command. Available commands:", available_commands)


# function to add a new product
def add_item():
    # connecting to sqlite database
    conn = get_connection()

    # creating a cursor object using the cursor() method
    cursor = conn.cursor()

    print("Enter product details below.\n")

    # asking for item type until correct value is entered
    while True:
        item_type = (
            input("Enter product type (physical = p / digital = d): ").strip().lower()
        )
        if item_type == "p":
            item_type = "physical"
        elif item_type == "d":
            item_type = "digital"
        if item_type in ["physical", "digital"]:
            break
        print("Invalid input. Enter 'p' or 'd'.\n")

    # asking for category until something is entered
    while True:
        category = input("Enter category: ").strip().lower()
        if category:
            break
        print("Category cannot be empty.\n")

    # asking for brand name until something is entered
    while True:
        brand_name = input("Enter brand name: ").strip().lower()
        if brand_name:
            break
        print("Brand name cannot be empty.\n")

    # asking for product name until something is entered
    while True:
        product_name = input("Enter product name: ").strip().lower()
        if product_name:
            break
        print("Product name cannot be empty.\n")

    # asking for buy price until a valid number is entered
    while True:
        value = input("Enter buy price: ").strip()
        if not is_non_negative_number(value):
            print("Buy price must be a number.\n")
            continue
        price_buy = float(value)
        break

    # asking for sell price until a valid number is entered
    while True:
        value = input("Enter sell price: ").strip()
        if not is_non_negative_number(value):
            print("Sell price must be a number.\n")
            continue
        price_sell = float(value)
        break

    # asking for tax percentage until a valid number is entered
    while True:
        value = input("Enter tax percentage: ").strip()
        if not is_non_negative_number(value):
            print("Tax percentage must be a number.\n")
            continue
        tax_percentage = float(value)
        break

    # creating product object only after all required fields are valid
    product = Product(
        item_type,
        category,
        brand_name,
        product_name,
        price_buy,
        price_sell,
        tax_percentage,
    )

    # inserting the product into the database only after everything is complete
    cursor.execute(
        """
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
    """,
        (
            product.item_type,
            product.category,
            product.brand_name,
            product.product_name,
            product.price_buy,
            product.price_sell,
            product.tax_percentage,
        ),
    )

    # storing the automatically generated id in the product object
    product.id = cursor.lastrowid

    # commit changes in the database
    conn.commit()

    print("\nProduct added successfully.")
    print(f"Assigned ID: {product.id}")
    print(f"Profit: {product.profit:.2f} not including tax.\n")

    # closing the connection
    conn.close()


# function to delete a product by id
def del_item():
    # connecting to sqlite database
    conn = get_connection()
    # creating a cursor object using the cursor() method
    cursor = conn.cursor()

    # ask user for row id to delete
    row_to_delete = input("Enter product ID to delete: ")

    # fetch the product by id
    cursor.execute(
        "SELECT id, brand_name, product_name FROM product WHERE id = ?",
        (row_to_delete,),
    )
    product = cursor.fetchone()

    result = False

    # if id not found, exit
    if product is None:
        print(f"No product found with ID {row_to_delete}.")
    else:
        print(f"Selected: ID {product[0]} | {product[1]} | {product[2]}")

        # ask for confirmation until yes or no is entered
        while True:
            answer = input("Delete this product? yes/no: ").strip().lower()
            if answer == "yes":
                cursor.execute("DELETE FROM product WHERE id = ?", (row_to_delete,))
                conn.commit()
                print(f"Product with ID: {row_to_delete} deleted.")
                result = True
                break
            if answer == "no":
                print("Cancelled.")
                break
            print("Type yes or no.")

    conn.close()
    return result


# function to modify a product by id and field
def modify_item():
    available_to_update = [
        "category",
        "brand",
        "name",
        "buy price",
        "sell price",
        "tax",
        "list",
        "exit",
        "help",
    ]

    # connecting to sqlite database
    conn = get_connection()
    # creating a cursor object using the cursor() method
    cursor = conn.cursor()

    print('Type "list" to show products, "exit" to close, "help" for options.')

    # ask for which id to modify
    while True:
        row_to_update = input("Enter product ID to update: ").strip().lower()

        if row_to_update == "list":
            list_items()
            continue

        if row_to_update == "help":
            print_options("Available options:", available_to_update)
            continue

        if row_to_update == "exit":
            print("Exiting modification mode...")
            conn.close()
            return

        break

    # fetch the product by id
    cursor.execute("SELECT * FROM product WHERE id = ?", (row_to_update,))
    product = cursor.fetchone()

    # if id not found, exit
    if product is None:
        print(f"No product found with ID {row_to_update}.")
        conn.close()
        return

    # print current product values
    print_product_brief(product)

    # ask user for which field to modify
    while True:
        command = input("Enter field to modify: ").strip().lower()

        if command == "exit":
            print("Exiting modification mode...")
            conn.close()
            return

        if command == "help":
            print_options("Available options:", available_to_update)
            continue

        if command == "list":
            list_items()
            continue

        if command == "category":
            # asking for new category until something is entered
            while True:
                value = input("Enter new category: ").strip().lower()
                if value:
                    break
                print("Category cannot be empty.")
            cursor.execute(
                "UPDATE product SET category = ? WHERE id = ?", (value, row_to_update)
            )

        elif command == "brand":
            # asking for new brand until something is entered
            while True:
                value = input("Enter new brand: ").strip().lower()
                if value:
                    break
                print("Brand cannot be empty.")
            cursor.execute(
                "UPDATE product SET brand_name = ? WHERE id = ?", (value, row_to_update)
            )

        elif command == "name":
            # asking for new product name until something is entered
            while True:
                value = input("Enter new name: ").strip().lower()
                if value:
                    break
                print("Name cannot be empty.")
            cursor.execute(
                "UPDATE product SET product_name = ? WHERE id = ?",
                (value, row_to_update),
            )

        elif command == "buy price":
            # asking for new buy price until a valid number is entered
            while True:
                value = input("Enter new buy price: ").strip()
                if not is_non_negative_number(value):
                    print("Price must be a number.")
                    continue
                value = float(value)
                break
            cursor.execute(
                "UPDATE product SET price_buy = ? WHERE id = ?", (value, row_to_update)
            )

        elif command == "sell price":
            # asking for new sell price until a valid number is entered
            while True:
                value = input("Enter new sell price: ").strip()
                if not is_non_negative_number(value):
                    print("Price must be a number.")
                    continue
                value = float(value)
                break
            cursor.execute(
                "UPDATE product SET price_sell = ? WHERE id = ?", (value, row_to_update)
            )

        elif command == "tax":
            # asking for new tax percentage until a valid number is entered
            while True:
                value = input("Enter new tax: ").strip()
                if not is_non_negative_number(value):
                    print("Tax must be a number.")
                    continue
                value = float(value)
                break
            cursor.execute(
                "UPDATE product SET tax_percentage = ? WHERE id = ?",
                (value, row_to_update),
            )

        else:
            print_options("Unknown option. Available options:", available_to_update)
            continue

        # commit changes and stay in modify mode
        conn.commit()
        print("Updated successfully.")


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
                f"ID: {product[0]} | "
                f"Type: {product[1]} | "
                f"Category: {product[2]} | "
                f"Brand: {product[3]} | "
                f"Name: {product[4]} | "
                f"Buy: {product[5]:.2f} | "
                f"Sell: {product[6]:.2f} | "
                f"Tax: {product[7]:.2f}%"
            )
        print()

    # closing the connection
    conn.close()
