# Collaboration guidelines

How we work together on this project. Keep it simple, keep it friendly.

---

## Branch-based development

All work happens on branches. Never code directly on `master` or `development`. 

Create a branch for each task:

```
git checkout -b "feature/your-new-feature"
```

When the work is done, open a pull request to merge it back.

[Why we use branches?](https://www.w3schools.com/git/git_branch.asp)

---

## No direct pushes to master or development

`master` stays clean and stable. Every change goes through a pull request. Development happens on development.

- Push your branch to the remote.
- Open a pull request.
- Wait for review before merging.

---

## Code review

At least one other contributor must review your pull request before it can be merged.

Reviews should check for:

- Does the code do what it says it does?
- Is it easy to follow?
- Are there any obvious bugs or edge cases?
- Does it follow the project's code style?
- Is the code well documented?

Use GitHub's review comments. Be clear and constructive.

---

## Who can merge

Right now only the maintainer merges pull requests. This keeps things controlled while the project is young.

As contributors gain experience, they may earn merge access too. If that sounds like you, just keep contributing and we will talk about it when the time is right.

---

## Communication

- **Ideas, bugs, and feature requests** → post in appropriate channel on discord (to be specified).
- **Pull request discussions** → keep them on the PR page.
- **Quick questions** → post in appropriate channel on discord (to be specified).

Tag relevant people so nothing gets missed.

---

## Discuss before coding

For anything bigger than a small fix, post on discord. Describe what you want to do and why.

This gives everyone a chance to weigh in before time is spent on code. It avoids wasted work and keeps the project moving in one direction.

---

## Constructive feedback

Code reviews are about the code, not the person.

- Be kind and specific in your feedback.
- Ask questions if something is unclear.
- Accept feedback graciously.

We are all here to learn and build something useful.
