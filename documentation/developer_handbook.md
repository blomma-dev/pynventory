# Developer handbook

Everything you need to set up, write code, and contribute to this project.

---

## 1. Prerequisites

Make sure these are installed on your machine:

- **Python** 3.8 or newer
- **Git**

Check with:

```bash
python --version
git --version
```

---

## 2. Dev environment setup

Read below why we use virtual environments

[Why do we use virtual environments?](https://pythonforengineers.com/blog/python-tip-always-use-a-virtual-environment/index.html)

### Create a virtual environment in project root folder

```bash
python -m venv .venv
```
OR

```bash
python3 -m venv .venv
```

This creates a `.venv` folder in the project root. It is already in `.gitignore` so it will never be committed.

### Allow creation of virtual environments (Windows only)
Run PowerShell as admin and enter:

```
set-executionpolicy remotesigned
```



### Activate the virtual environment

**Linux / macOS:**

```bash
source .venv/bin/activate
```

**Windows (Command Prompt):**

```cmd
.venv\Scripts\activate
```

**Windows (PowerShell):**

```powershell
.venv\Scripts\Activate.ps1
```

Your terminal should now show `(.venv)` before the prompt. That means it is active.

### Deactivate when done

```bash
deactivate
```

### Install dependencies

[Click here to read about dependencies](https://realpython.com/ref/glossary/dependency/)

Install the project's dev tools:

```bash
pip install -r requirements.txt
```

Currently this only includes Ruff, the formatter and linter. The project itself uses only the Python standard library.

---

## 3. Git workflow — full tutorial

This walks you through the full process, from cloning to having your code merged. If you already know git, skip ahead to the [quick reference](#4-git-workflow--quick-reference).

### 3.1 Clone the repository

```bash
git clone <repo-url>
cd pynventory
```

### 3.2 Make sure you are on master

```bash
git checkout master
git pull origin master
```

Always start new work from an up-to-date `master`.

### 3.3 Create a branch

Name it after what you are doing. Use one of the prefixes below:

- `feature/` — new functionality
- `fix/` — bug fixes
- `chore/` — cleanup, refactoring, docs

Examples:

```bash
git checkout -b feature/search-by-name
git checkout -b fix/delete-confirmation
git checkout -b chore/refactor-functions
```

### 3.4 Your work

Write code, test it manually, and commit as you go. Commit often with clear messages. You can use either VScode git, git through terminal or for example GitHub desktop. Whatever works for you.

### 3.5 Stage and commit

```bash
git add main.py
git commit -m "add search command"
```

Or stage everything:

```bash
git add .
git commit -m "add search command with partial name matching"
```

More on commit messages in [section 6](#6-commit-messages).

### 3.6 Keep your branch up to date

If someone merged something to `master` while you were working:

```bash
git checkout master
git pull origin master
git checkout your-branch
git merge master
```

Fix any conflicts, then commit the merge.

### 3.7 Push your branch

```bash
git push origin your-branch
```

### 3.8 Open a pull request

Go to the repository on GitHub. You will see a banner suggesting you open a pull request for your recently pushed branch. Click it.

Fill in the description (see [section 8](#8-pull-request-expectations)) and submit.

### 3.9 Address review feedback

If the reviewer requests changes, make them on the same branch, commit, and push again. The pull request updates automatically.

### 3.10 Done

Once approved and merged by the maintainer, your branch can be deleted. GitHub offers a button for this right on the merged PR page.

Locally, switch back to master and pull:

```bash
git checkout master
git pull origin master
```

---

## 4. Git workflow — quick reference

Read below more about branches

[Why we use branches?](https://www.w3schools.com/git/git_branch.asp)

```bash
# Start fresh
git checkout master
git pull origin master

# Branch and work
git checkout -b feature/your-thing
# ... write code ...
git add .
git commit -m "what you did"

# Push and PR
git push origin feature/your-thing
# ... open pull request on GitHub ...

# After merge
git checkout master
git pull origin master
```

---

## 5. Branch naming

Stick to these prefixes so anyone can tell what a branch is for at a glance:

| Prefix | Use for |
|--------|---------|
| `feature/` | New functionality |
| `fix/` | Bug fixes |
| `chore/` | Refactoring, cleanup, docs |

Keep the name short and descriptive. Lowercase, hyphens for spaces.

Good:
- `feature/search-by-brand`
- `fix/empty-name-crash`
- `chore/split-functions-file`

Bad:
- `mybranch`
- `stuff`
- `FeatureSearchByBrand`

---

## 6. Commit messages

### Format

A good commit message has:

- A short subject line (50 characters or less).
- Written in the imperative mood: "add search" not "added search" or "adds search".
- A blank line, then a longer description if the change needs explaining.

### Examples

```
add search command with partial name matching
```

```
fix crash when deleting a product that does not exist

The program would raise an IndexError if you tried to
delete an ID that was not in the table. Now it checks
first and shows a clear message.
```

### What to avoid

- Vague messages like "update code" or "fix bug".
- Messages longer than 50 characters for the subject.
- Messages in past tense.

---

## 7. Code style

### Formatter

We use [Ruff](https://docs.astral.sh/ruff/) for formatting and linting. It is fast, minimal, and the built-in formatter in Zed. VSCode users can install the [Ruff extension](https://marketplace.visualstudio.com/items?itemName=charliermarsh.ruff).

Install Ruff:

```bash
pip install -r requirements.txt
```

Or directly:

```bash
pip install ruff
```

### Using Ruff

Format your code:

```bash
ruff format .
```

Check for issues:

```bash
ruff check .
```

Fix issues automatically:

```bash
ruff check --fix .
```

### Editor setup

**VSCode** — Install the Ruff extension and add this to your settings:

```json
{
  "[python]": {
    "editor.defaultFormatter": "charliermarsh.ruff",
    "editor.formatOnSave": true
  }
}
```

**Zed** — Ruff is the default formatter for Python. No setup needed.

**PyCharm** — Install the [Ruff plugin](https://plugins.jetbrains.com/plugin/20574-ruff):

1. Go to **Settings → Plugins** and search for "Ruff".
2. Install and restart PyCharm.
3. Go to **Settings → Tools → Ruff**.
4. Check **Enabled** and set **Run on save** to `true`.
5. PyCharm will auto-detect the project's `ruff.toml`.

The project's `ruff.toml` file keeps formatting the same across all editors.

### Consistency

Look at what is already in the project and follow the same patterns:

- How functions are named: `snake_case`
- How classes are named: `PascalCase`
- How indentation works: 4 spaces
- How input validation is structured

When you add new code, match what is around it.

### Comments

Code should explain itself most of the time. Add a comment only when something is not obvious at first glance. Keep them short.

Avoid leaving commented-out code. If it is not used, delete it.

---

## 8. Pull request expectations

[Click here to read about pull requests](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests)

When you open a pull request, include:

1. **What you did** — a short summary of the change.
2. **Why** — what problem does it solve?
3. **Link to the `todo.md` item** — if your change relates to one.
4. **How you tested it** — what did you try to make sure it works?

Self-review checklist before submitting:

- [ ] I tested the change manually and it works.
- [ ] I checked for leftover debug prints.
- [ ] My branch is up to date with `master`.
- [ ] The code follows the project's style.

---

## 9. Testing

Right now testing is manual. Before opening a pull request:

- Run `python main.py` and try your feature.
- Try edge cases: empty input, wrong input, fast typing, whatever you can think of.
- Make sure existing commands still work.

Automated tests may be added later. When they are, they must pass before merging.

---

## 10. Database notes

The project uses SQLite for now as database, read  more about SQLite: [click here to read more about SQLite](https://www.sqlitetutorial.net/what-is-sqlite/).

- The database file is `products.db`. It is already in `.gitignore`. Do not commit it.
- To create a fresh database, run:

```bash
python database.py
```

- If you ever need to start over, delete `products.db` and run that command again.
