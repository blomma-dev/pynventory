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

## Roadmap

The project is intentionally simple right now. The goal is to improve the CLI inventory app first, then move toward larger architecture changes later.

### Phase 1: Make the CLI inventory useful

These are the next core features that make the inventory more practical.

- [ ] **stock quantity tracking** - add quantity to products so inventory levels can be tracked.
- [ ] **sell products** - reduce stock when products are sold.
- [ ] **search** - find products by name or brand using partial, case-insensitive matches.
- [ ] **validate sell price** - warn or block if sell price is lower than buy price.
- [ ] **better formatted output** - align columns and improve spacing when listing products.

### Phase 2: Improve safety and contributor confidence

These make the project easier to work on without breaking existing behavior.

- [ ] **simple tests** - add basic automated tests for product creation, validation, and database operations.
- [ ] **better error messages** - tell the user clearly what went wrong and how to fix it.
- [ ] **cleaner developer experience** - keep files focused and easy to understand as the project grows.
- [ ] **database reset guidance** - document how to safely create or reset local development data.

### Phase 3: Add useful inventory features

These features build on quantity tracking and make the app more realistic.

- [ ] **inventory value report** - show total stock value and total potential profit.
- [ ] **filter by category** - list only products in a chosen category.
- [ ] **sort list** - sort by brand, category, profit, price, or quantity.
- [ ] **low-stock alerts** - show products where quantity is below a chosen limit.
- [ ] **export to CSV** - export inventory data for use in spreadsheets.
- [ ] **date added field** - track when a product was first entered.
- [ ] **last updated field** - track when a product was last modified.

### Phase 4: Larger future ideas

These should wait until the CLI behavior and data model are clearer.

- [ ] **supplier info** - add supplier details to products or a separate supplier table.
- [ ] **restock history** - log when stock increases.
- [ ] **sales / stock movement history** - log stock decreases and sales.
- [ ] **API layer** - expose inventory functionality for a future front end.
- [ ] **web version** - build a browser-based interface using a framework chosen by the team.
- [ ] **production environment** - explore Docker or another deployment approach if the project grows.
- [ ] **database upgrade** - explore alternatives to SQLite if multi-user access becomes necessary.


## Code quality

- [ ] **simple tests** — so refactoring later does not break things.
- [ ] **better error messages** — tell the user exactly what went wrong.
- [ ] **unique id generation?** — SQLite already handles this, but good to keep in mind if storage ever changes.


## Rules for building

### [Developer handbook](https://github.com/blomma-dev/pynventory/wiki/Developer-handbook)

### [Collaboration guidelines](https://github.com/blomma-dev/pynventory/wiki/Collaboration-guidelines)
