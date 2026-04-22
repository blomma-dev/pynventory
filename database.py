import sqlite3


# function to create and return a database connection
def get_connection():
    return sqlite3.connect("products.db")


# function to create the product table if it does not exist
def create_table():
    # connecting to sqlite database
    conn = get_connection()

    # creating a cursor object using the cursor() method
    cursor = conn.cursor()

    # creating table as per requirement
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS product (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        item_type TEXT NOT NULL,
        category TEXT NOT NULL,
        brand_name TEXT NOT NULL,
        product_name TEXT NOT NULL,
        price_buy REAL NOT NULL,
        price_sell REAL NOT NULL,
        tax_percentage REAL NOT NULL
    )
    """)

    print("Table checked/created successfully.")

    # commit changes in the database
    conn.commit()

    # closing the connection
    conn.close()