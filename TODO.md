# ToDo

Currently the application works only via the terminal, and this is fine for now.
To improve the program overall, let's think about the scope of the project below

However, in the future it would be feasible to for example:

### Future plans
- Access the program via a web-browser (Django, React, Vue etc. ?)
- The production software (should) could run in docker?
- Test framework for testing the software (pytest/robot/?)
- For multi-user access SQLite is not feasible, explore other DB:s
- API for connecting front-end and back-end (Django?)

Suggestions are welcome, and users should bring up ideas as [Issues on GitHub](https://github.com/blomma-dev/pynventory/issues).


## Currently done

- SQLite database setup with product table
- product model with profit auto-calculated on creation
- add command with validation (no empty fields, no negative numbers, type must be p or d)
- list command that prints every product
- help and exit commands
- basic command loop in main.py
- delete product by id
- modify product by id and field in product
- collaboration guidelines and developer handbook documentation
- barebones error handling
- delete a product by id. asks for confirmation so you do not wipe something by accident.
- modify fields of an existing product (`mod` command). ask for id first, show current values, let user overwrite. supports list/help/exit inside the modify sub-menu.

## Core features to add
These are the essentials that make the inventory actually usable.

- [ ] **better dev experience** — in ```functions.py``` to their own respective main files take a look at ```helpers.py``` for example.
- [ ] **sell products** — make the system actually usable by implementing a feature that reflects to the database if stock has been sold.
- [ ] **search** — find products by name or brand. partial matches, case insensitive.
- [ ] **validate sell price** — warn or block if sell price is lower than buy price.

## Useful additions

- [ ] **inventory value report** — total value of all stock, total potential profit.
- [ ] **filter by category** — list only products in a chosen category.
- [ ] **sort list** — sort by brand, category, profit, or price.
- [ ] **low-stock alerts** — only makes sense if quantity tracking is added to the model.
- [ ] **better formatted output** — align columns, cleaner spacing.
- [ ] **edit product details** — similar to modify, maybe combined.

## Data and export

- [ ] **export to csv** — dump inventory to a file for spreadsheets.
- [ ] **date added field** — track when a product was first entered.
- [ ] **last updated field** — track when a product was last modified.

## More advanced stuff

- [ ] **supplier info** — add a supplier name or a separate supplier table.
- [ ] **restock history** — log every time stock increases with date and quantity.
- [ ] **sales / stock movement history** — log decreases too, so you know what moved.
- [ ] **stock quantity tracking** — right now there is no quantity field. adding this enables low-stock alerts and movement history.

## Interface ideas

these are long-term options, pick one if the project ever grows past the terminal.

- [ ] **web version** — rebuild with flask, web forms, browser display.

## Code quality

- [ ] **simple tests** — so refactoring later does not break things.
- [ ] **better error messages** — tell the user exactly what went wrong.
- [ ] **unique id generation?** — SQLite already handles this, but good to keep in mind if storage ever changes.


## Rules for building

### [Developer handbook](https://github.com/blomma-dev/pynventory/wiki/Developer-handbook)

### [Collaboration guidelines](https://github.com/blomma-dev/pynventory/wiki/Collaboration-guidelines)