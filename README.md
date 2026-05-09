# Pynventory

Pynventory is a collaborative, invite-only learning project built around a small inventory management application.

The goal is to practice real software development workflows in a supportive environment: software development, Git branches, GitHub Issues, pull requests, code review, releases, and teamwork.

The application currently runs in the terminal and uses SQLite for local data storage. It starts simple on purpose so contributors can focus on learning, improving the app step by step, and working together.

## Quick start

The setup guide is available here: [Local development setup](https://github.com/blomma-dev/pynventory/wiki/Local-development-setup).

## Current project phase

The current focus is improving the terminal-based inventory app before moving toward a web interface.

Near-term priorities include:

- improving inventory behavior
- adding quantity and selling features
- adding search and better list output
- introducing simple automated tests
- keeping the contributor workflow clear and beginner-friendly

For more detail, see the [Project roadmap](https://github.com/blomma-dev/pynventory/wiki/Project-roadmap).

## Contributing

Most work starts from a GitHub Issue, happens on a branch, and is merged through a pull request.

If you are new to the project, start here:

- [Your first contribution](https://github.com/blomma-dev/pynventory/wiki/Your-first-contribution)
- [Developer handbook](https://github.com/blomma-dev/pynventory/wiki/Developer-handbook)
- [Collaboration guidelines](https://github.com/blomma-dev/pynventory/wiki/Collaboration-guidelines)
- [Manual testing guide](https://github.com/blomma-dev/pynventory/wiki/Manual-testing-guide)
- [Code style and quality guide](https://github.com/blomma-dev/pynventory/wiki/Code-style-and-quality-guide)

Before opening a pull request:

- link the pull request to a GitHub Issue
- test your change manually
- run Ruff if you changed Python code
- make sure `products.db` is not included in your commit

## Project documentation

The wiki is the main place for setup, contribution guidance, and project documentation.

Useful pages:

- [Wiki home](https://github.com/blomma-dev/pynventory/wiki)
- [Local development setup](https://github.com/blomma-dev/pynventory/wiki/Local-development-setup)
- [Project roadmap](https://github.com/blomma-dev/pynventory/wiki/Project-roadmap)
- [Troubleshooting](https://github.com/blomma-dev/pynventory/wiki/Troubleshooting)
- [FAQ](https://github.com/blomma-dev/pynventory/wiki/FAQ)
- [Useful links](https://github.com/blomma-dev/pynventory/wiki/Useful-links)

## Project management

GitHub Issues are used to track tasks, bugs, questions, and planned work.

- [Issues](https://github.com/blomma-dev/pynventory/issues)
- [Project board](https://github.com/users/blomma-dev/projects/2)

Discord is used for quick communication, asking questions, and discussing work in progress.

## Local database note

Pynventory uses a local SQLite database file named `products.db`.

This file is local development data and should not be included in pull requests.
