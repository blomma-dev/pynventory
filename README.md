# Pynventory

Pynventory is a collaborative, invite-only learning project built around a small inventory management application.

The goal is to practice real software development workflows in a supportive environment: Python, Git branches, GitHub Issues, pull requests, code review, releases, and teamwork.

The application currently runs in the terminal and uses SQLite for local data storage. It starts simple on purpose so contributors can focus on learning, improving the app step by step, and working together.

## What it does

Pynventory currently lets you:

- add products to inventory
- list saved products
- modify existing products
- delete products
- store data between runs using SQLite

Products track details such as category, brand, product name, buy price, sell price, tax percentage, weight, and stock amount.

The project is currently focused on improving the terminal-based inventory app before moving toward a web interface. For more detail, see [Architecture & roadmap](https://github.com/blomma-dev/pynventory/wiki/Architecture-and-roadmap).

## Requirements

- Python 3.8 or newer
- No app dependencies beyond the Python standard library and SQLite
- `requirements.txt` currently contains Ruff for development checks

## Quick start

For the full setup guide, read [Getting started](https://github.com/blomma-dev/pynventory/wiki/Getting-started).

Run the app from the repository root with:

```bash
python -m pynventory.main
```

## Commands

| Command | What it does |
|---|---|
| `add` | Add a new product to the inventory |
| `list` | Show all products |
| `mod` | Update a product by ID |
| `del` | Remove a product by ID |
| `help` | Print the list of commands |
| `exit` | Close the program |

## Docs & contributing

The wiki is the main place for setup, contribution guidance, and project documentation.

- [Wiki home](https://github.com/blomma-dev/pynventory/wiki)
- [Getting started](https://github.com/blomma-dev/pynventory/wiki/Getting-started)
- [Git & development workflow](https://github.com/blomma-dev/pynventory/wiki/Git-and-development-workflow)
- [Code style guide](https://github.com/blomma-dev/pynventory/wiki/Code-style-guide)
- [Testing guide](https://github.com/blomma-dev/pynventory/wiki/Testing-guide)
- [Architecture & roadmap](https://github.com/blomma-dev/pynventory/wiki/Architecture-and-roadmap)
- [Troubleshooting](https://github.com/blomma-dev/pynventory/wiki/Troubleshooting)
- [FAQ](https://github.com/blomma-dev/pynventory/wiki/FAQ)

Most work starts from a GitHub Issue, happens on a branch, and is merged through a pull request.

- Project planning and roadmap items are tracked in [Architecture & roadmap](https://github.com/blomma-dev/pynventory/wiki/Architecture-and-roadmap).
- Concrete tasks, bugs, and feature ideas are tracked in [GitHub Issues](https://github.com/blomma-dev/pynventory/issues).

- [Issues](https://github.com/blomma-dev/pynventory/issues)
- [Project board](https://github.com/users/blomma-dev/projects/2)

## Local database note

Pynventory uses a local SQLite database file named `data/products.db`.

This file is local development data and should not be included in pull requests.
