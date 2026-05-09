# Pynventory

Pynventory is a collaborative, invite-only learning project where contributors can build software together, practice real development workflow, and gain useful work skills.

The application mimics an inventory management system, and gives contributors a place to practice development, branching, pull requests, code reviews, and team collaboration. It starts simple on purpose so people can focus on learning and growing in a shared project.

## Current project phase

The current focus is improving the terminal-based inventory app before expanding into a complete full-stack version.

Near-term priorities include:

- tracking product quantities
- selling products and reducing stock
- searching products by name or brand
- improving list output formatting
- adding basic automated tests
- keeping the contributor workflow simple and beginner-friendly
- reworking the database
- and more to come!

## Getting started

The full setup and contribution guide lives in the [Pynventory wiki](https://github.com/blomma-dev/pynventory/wiki).

Quick local setup:

```bash
git clone https://github.com/blomma-dev/pynventory.git
cd pynventory
python -m venv .venv
```

Activate the virtual environment:

```bash
# Linux / macOS
source .venv/bin/activate

# Windows PowerShell
.venv\Scripts\Activate.ps1
```

Install development tools:

```bash
pip install -r requirements.txt
```

Run the app:

```bash
python main.py
```

For the full workflow, read the [Developer handbook](https://github.com/blomma-dev/pynventory/wiki/Developer-handbook) and [Collaboration guidelines](https://github.com/blomma-dev/pynventory/wiki/Collaboration-guidelines).

The wiki is the main place for setup, contribution guidance, and project documentation.

## What this project is

Pynventory is more than a small Python app. It is a shared project for invited contributors who want to learn by doing, collaborate with others, and build experience that carries over into real software work.

Because the project is invite-only, it can stay focused, supportive, and manageable for the people involved.

## What you gain

By contributing to this project, you can practice:

- object-oriented programming in Python
- working with databases and data models
- front-end and back-end experience
- API:s and frameworks
- planning software features
- using Git branches and pull requests
- reading and giving code reviews
- collaborating in a shared project
- building a portfolio with real commit history
- developing useful work skills through team-based practice that translates to work-related skills

## How we collaborate

GitHub Issues are used to track tasks, bugs, and planned work.

We also use an invite-only progress tracker board (https://github.com/users/blomma-dev/projects/2) to organize progress and keep contributors aligned.

Discord is mainly for direct communication with other collaborators, asking questions, and discussing work in progress.

## What it does

Pynventory lets you:

- add products to inventory
- list saved products
- update existing products
- delete products
- store data between runs using SQLite
- and more to come!

## Commands

| Command | What it does |
|---|---|
| `add` | Add a new product to the inventory |
| `list` | Show all products |
| `mod` | Update a product by ID |
| `del` | Remove a product by ID |
| `help` | Print the list of commands |
| `exit` | Close the program |

## Running the app

Run the program with:

```bash
python main.py
```
