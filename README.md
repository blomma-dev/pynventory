# Pynventory

A small inventory tracker built with python and sqlite. A learning project where you gain real-world collaboration experience by building something together — branches, pull requests, code reviews, and a shared codebase, just like a real dev team. No AI for code generation.

## What this project is about

Pynventory is a terminal-based tool that tracks products you buy and sell, calculates profit, and stores everything in a local sqlite database.

But more importantly, it is a sandbox for practicing software development skills. The app itself is simple on purpose — the real value is in how we work on it together.

## What you gain

- **OOP in practice** — classes, methods, `self`, and how to structure code across multiple files.
- **SQLite experience** — real database connections, queries, and schema design.
- **Git workflow** — branching, committing, pushing, pulling, and opening pull requests.
- **Code review** — both giving and receiving constructive feedback.
- **Collaboration skills** — discussing features before coding, working from a shared todo list, and communicating in a team setting.
- **Something for your portfolio** — a real project with a commit history that shows you can work with others.

## What you can expect

- **A low-pressure environment** — this is for learning. Mistakes are expected and part of the process.
- **Constructive feedback** — reviews focus on the code, not the person.
- **A growing codebase** — features get added over time, so there is always something to work on.
- **Real dev tooling** — ruff for formatting/linting, git for version control, and a branch-based workflow.
- **Guidance** — the collaboration guidelines and developer handbook walk you through everything from setup to pull requests.

Read the collaboration guidelines and developer handbook to understand the ways of working on this project.

## Discord

We use Discord for discussing ideas, asking questions, reporting bugs, and sharing work in progress. Check in before coding anything bigger than a small fix.

Ask the project owner for an invite to the server. Once you are in, check the pinned posts in the development and issues forums for posting guides.

## What it does

Keeps track of products you buy and sell. Calculates profit for each item automatically.
Stores everything in a local sqlite database so data persists between runs.

## How it works

### main.py
Main program, it makes sure the database table exists, then drops into a command loop that keeps running until you type `exit`.

### models.py
Holds the `Product` class. Stores all the usual fields (type, category, brand, name, prices, tax, weight and stock amount) and calculates profit right away when the object is created. Profit is just `sell price - buy price` (so far).

### database.py
Handles the sqlite stuff. `get_connection()` opens the database, `create_table()` builds the product table if it is missing. this is why the app does not crash on first run.

### functions.py
where the actual commands live:

- **add_item** — asks for each field one by one. it does not let you skip required fields or enter garbage. keeps asking until the input makes sense. only when everything checks out does it create the `Product` object and save it to the database. also shows you the assigned id and profit after saving.
- **list_items** — pulls every product from the database and prints them. if the table is empty, it just says so.
- **del_item** — removes product by ID. verification safeguard.
- **modify_item** — updates product by id, field selectable

## commands

| command | what it does                              |
|---------|-------------------------------------------|
| `add`   | add a new product to the inventory        |
| `list`  | show all products                         |
| `help`  | print the list of commands                |
| `exit`  | close the program                         |
| `del`   | remove product by ID                      |
| `mod`   | update a product's fields by ID           |

## quick start

```bash
python main.py
```

then type `help` to see what you can do.

```bash
python database.py
```

to init the database

## docs

- `collaboration_guidelines.md` — how we work together, branch rules, code review, merge policy.
- `developer_handbook.md` — dev environment setup, git workflow tutorial, code style, pull request expectations.

## notes

- product type accepts `p` for physical or `d` for digital.
- prices and tax cannot be negative.
- sqlite file `products.db` gets created in the same folder on first run.
