# Inventory Manager Project TODO

## Goal
Build a beginner-friendly **Python Inventory Manager** to learn:
- objects and classes
- methods and attributes
- lists of objects
- file handling
- program structure
- real-world problem solving

---

# Version 1 = Core Inventory Manager
## Objective
Create a simple terminal-based inventory app with basic product management.

## Features
- [ ] Create a `Product` class
- [ ] Create an `Inventory` class
- [ ] Add new products
- [ ] View all products
- [ ] Search for a product by name
- [ ] Update product quantity
- [ ] Remove a product
- [ ] Show total number of products

## Steps
### 1. Plan the data
- [ ] Decide what information a product should store
- [ ] Choose basic fields:
  - [ ] product ID
  - [ ] name
  - [ ] price
  - [ ] quantity
  - [ ] category

### 2. Build the `Product` class
- [ ] Write the `Product` class
- [ ] Add an `__init__` method
- [ ] Store product details as attributes
- [ ] Add a method to display product info
- [ ] Add a method to calculate total value for that product

### 3. Build the `Inventory` class
- [ ] Create a list to store `Product` objects
- [ ] Add a method to add a product
- [ ] Add a method to remove a product
- [ ] Add a method to search for a product
- [ ] Add a method to list all products
- [ ] Add a method to update stock quantity

### 4. Build the terminal menu
- [ ] Show a text menu with numbered options
- [ ] Let user choose actions
- [ ] Connect each menu option to an `Inventory` method
- [ ] Add an option to exit the program

### 5. Test Version 1
- [ ] Add sample products
- [ ] Search for existing and non-existing products
- [ ] Update quantity
- [ ] Remove a product
- [ ] Make sure menu flow works correctly

---

# Version 2 = Better Inventory Features
## Objective
Make the app more useful and realistic.

## Features
- [ ] Low-stock alerts
- [ ] Total inventory value report
- [ ] Filter by category
- [ ] Better formatted output
- [ ] Input validation

## Steps
### 1. Low-stock logic
- [ ] Decide a low-stock threshold
- [ ] Add a method to show products below the threshold

### 2. Inventory value
- [ ] Add a method to calculate total inventory value
- [ ] Show each product’s value
- [ ] Show combined inventory value

### 3. Categories
- [ ] Allow assigning categories to products
- [ ] Add a method to filter by category

### 4. Input validation
- [ ] Prevent empty product names
- [ ] Prevent negative prices
- [ ] Prevent negative quantities
- [ ] Handle invalid menu choices safely

### 5. Improve display
- [ ] Make product listing easier to read
- [ ] Align columns clearly
- [ ] Show helpful messages for success/errors

---

# Version 3 = Save and Load Data
## Objective
Make the data persistent using JSON.

## Features
- [ ] Save products to a JSON file
- [ ] Load products from a JSON file when program starts
- [ ] Convert objects to dictionaries
- [ ] Rebuild objects from saved data

## Steps
### 1. Prepare `Product` for saving
- [ ] Add a method to convert a product into a dictionary
- [ ] Add a method or approach to create a product from saved dictionary data

### 2. Save inventory
- [ ] Write a method to save all products to JSON
- [ ] Save automatically when products change, or through a menu option

### 3. Load inventory
- [ ] Load JSON data at startup
- [ ] Recreate `Product` objects from the file
- [ ] Handle missing file case safely

### 4. Test persistence
- [ ] Add products
- [ ] Save data
- [ ] Restart program
- [ ] Confirm products still exist

---

# Version 4 = Realistic Business Features
## Objective
Add features that make the project stronger for your CV.

## Features
- [ ] Supplier info
- [ ] Restock history
- [ ] Sales / stock movement history
- [ ] Export report to CSV

## Steps
### 1. Supplier support
- [ ] Decide whether each product should have a supplier
- [ ] Create a `Supplier` class or store supplier name first
- [ ] Link suppliers to products

### 2. Stock movement history
- [ ] Record every stock increase
- [ ] Record every stock decrease
- [ ] Store date, action, quantity, and product name

### 3. Exporting
- [ ] Export inventory data to CSV
- [ ] Export low-stock report
- [ ] Export stock movement report

---

# Version 5 = Advanced Upgrade Path
## Objective
Turn the project into something even more professional.

## Choose one path
### Option A = SQLite version
- [ ] Replace JSON storage with SQLite
- [ ] Learn basic SQL queries
- [ ] Store products in database tables

### Option B = GUI version
- [ ] Build a desktop interface with Tkinter
- [ ] Add forms and buttons
- [ ] Show product list in a table

### Option C = Web version
- [ ] Rebuild with Flask
- [ ] Add web forms
- [ ] Display products in browser

---

# Recommended File Structure
- [ ] `main.py`
- [ ] `product.py`
- [ ] `inventory.py`
- [ ] `data.json`
- [ ] `README.md`

Later:
- [ ] `supplier.py`
- [ ] `utils.py`
- [ ] `reports.py`

---

# Learning Goals by Version

## After Version 1
You should understand:
- [ ] what a class is
- [ ] what an object is
- [ ] how `__init__` works
- [ ] how methods use `self`
- [ ] how to store objects in a list

## After Version 2
You should understand:
- [ ] how to organize logic inside classes
- [ ] how to validate input
- [ ] how to add useful business rules

## After Version 3
You should understand:
- [ ] how to save and load program data
- [ ] how to convert objects into dictionaries
- [ ] how persistence works in simple apps

## After Version 4+
You should understand:
- [ ] how to expand a project cleanly
- [ ] how to model more real-world entities
- [ ] how to make a project more CV-worthy

---

# Suggested Order of Work
- [ ] Finish Version 1 completely
- [ ] Refactor messy code before starting Version 2
- [ ] Add Version 2 features one by one
- [ ] Save/load with JSON in Version 3
- [ ] Choose one advanced direction after that

---

# Rules for Building
- [ ] Keep classes small and clear
- [ ] Do not add too many features too early
- [ ] Test each feature before moving on
- [ ] Refactor when code starts feeling repetitive
- [ ] Focus on understanding, not speed

---

# CV Notes
When project is finished, aim to say something like:

- [ ] Built a Python inventory management application using object-oriented programming
- [ ] Implemented product tracking, stock updates, low-stock alerts, and inventory reports
- [ ] Added persistent storage using JSON / SQLite
- [ ] Structured the application using reusable classes and clean program design

---

# Final Milestone Checklist
- [ ] App runs without crashing
- [ ] Products can be added, updated, searched, and removed
- [ ] Low-stock items can be identified
- [ ] Inventory value can be calculated
- [ ] Data can be saved and loaded
- [ ] Code is organized into multiple files
- [ ] README explains how to run the project

---

# Nice-to-Have Extras
- [ ] Sort products by price or quantity
- [ ] Search by category
- [ ] Unique ID generation
- [ ] Edit product details
- [ ] Date added field
- [ ] Last updated field
- [ ] Simple test functions
- [ ] Better error messages