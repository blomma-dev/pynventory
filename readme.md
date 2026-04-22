# Pynventory

A small inventory tracker built with python and sqlite, nothing fancy.

## What it does

Keeps track of products you buy and sell. Calculates profit for each item automatically.
Stores everything in a local sqlite database so data persists between runs.

## How it works

### main.py
Main program, it makes sure the database table exists, then drops into a command loop that keeps running until you type `exit`.

### models.py
Holds the `Product` class. Stores all the usual fields (type, category, brand, name, prices, tax) and calculates profit right away when the object is created. Profit is just `sell price - buy price`.

### database.py
Handles the sqlite stuff. `get_connection()` opens the database, `create_table()` builds the product table if it is missing. this is why the app does not crash on first run.

### functions.py
where the actual commands live:

- **add_item** — asks for each field one by one. it does not let you skip required fields or enter garbage. keeps asking until the input makes sense. only when everything checks out does it create the `Product` object and save it to the database. also shows you the assigned id and profit after saving.
- **list_items** — pulls every product from the database and prints them. if the table is empty, it just says so.

## commands

| command | what it does |
|---------|-------------|
| `add` | add a new product to the inventory |
| `list` | show all products |
| `help` | print the list of commands |
| `exit` | close the program |
| `del` | placeholder — not implemented yet |
| `modify` | placeholder — not implemented yet |

## quick start

```bash
python main.py
```

then type `help` to see what you can do.

```bash
python database.py
```

to init the database

## notes

- product type accepts `p` for physical or `d` for digital.
- prices and tax cannot be negative.
- sqlite file `products.db` gets created in the same folder on first run.
