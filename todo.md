# todo

stuff already working and what still needs doing.

## done

- sqlite database setup with product table
- product model with profit auto-calculated on creation
- add command with validation (no empty fields, no negative numbers, type must be p or d)
- list command that prints every product
- help and exit commands
- basic command loop in main.py

## core features to add

these are the essentials that make the inventory actually usable.

- [ ] **delete** — remove a product by id. needs a confirmation prompt so you do not wipe something by accident.
- [ ] **modify** — update fields of an existing product. ask for id first, show current values, let user overwrite.
- [ ] **search** — find products by name or brand. partial matches, case insensitive.
- [ ] **validate sell price** — warn or block if sell price is lower than buy price.

## useful additions

- [ ] **inventory value report** — total value of all stock, total potential profit.
- [ ] **filter by category** — list only products in a chosen category.
- [ ] **sort list** — sort by brand, category, profit, or price.
- [ ] **low-stock alerts** — only makes sense if quantity tracking is added to the model.
- [ ] **better formatted output** — align columns, cleaner spacing.
- [ ] **edit product details** — similar to modify, maybe combined.

## data and export

- [ ] **export to csv** — dump inventory to a file for spreadsheets.
- [ ] **date added field** — track when a product was first entered.
- [ ] **last updated field** — track when a product was last modified.

## more advanced stuff

- [ ] **supplier info** — add a supplier name or a separate supplier table.
- [ ] **restock history** — log every time stock increases with date and quantity.
- [ ] **sales / stock movement history** — log decreases too, so you know what moved.
- [ ] **stock quantity tracking** — right now there is no quantity field. adding this enables low-stock alerts and movement history.

## interface ideas

these are long-term options, pick one if the project ever grows past the terminal.

- [ ] **gui version** — desktop interface with tkinter, forms and buttons, product table view.
- [ ] **web version** — rebuild with flask, web forms, browser display.

## code quality

- [ ] **simple tests** — so refactoring later does not break things.
- [ ] **better error messages** — tell the user exactly what went wrong.
- [ ] **unique id generation** — sqlite already handles this, but good to keep in mind if storage ever changes.

## learning goals

check these off as you build:

- [ ] understand how classes and objects work
- [ ] know how methods use self
- [ ] be comfortable with sqlite connections and cursors
- [ ] know how to validate input and keep asking until it is right
- [ ] understand how to structure a small app across multiple files
- [ ] know how to expand a project cleanly without making a mess

## rules for building

- keep classes small and clear
- do not add too many features at once
- test each feature before moving on
- refactor when code starts feeling repetitive
- focus on understanding, not speed
