# Rienze's Dev Notes

## Terminal Commands

| Command | What it does                  |
| ------- | ----------------------------- |
| pwd     | Shows your current location   |
| cd      | Navigate into a folder        |
| ls      | List files in current folder  |
| mkdir   | Create a new folder           |
| clear   | Clean up the terminal screen  |
| rm -rf  | Delete a file or folder       |
| touch   | Create a new empty file       |
| code .  | Open current folder in VSCode |

## Git Commands

| Command                  | What it does                       |
| ------------------------ | ---------------------------------- |
| git init                 | Initialize Git in a project folder |
| git status               | Check what Git is currently seeing |
| git add filename         | Stage a specific file              |
| git add .                | Stage all changes at once          |
| git commit -m "message"  | Save a snapshot with a description |
| git push                 | Send your commits to GitHub        |
| git pull                 | Bring code down from GitHub        |
| git rm --cached filename | Remove a file from Git tracking    |

## Python Concepts

### Data Types

| Type    | Example    | What it is               |
| ------- | ---------- | ------------------------ |
| String  | "Rienze"   | Text in quotes           |
| Integer | 28         | Whole number             |
| Float   | 5.11       | Decimal number           |
| Boolean | True/False | Only two possible values |

### Built-in Functions

| Function | What it does                     |
| -------- | -------------------------------- |
| print()  | Displays output in the terminal  |
| type()   | Returns the data type of a value |

## Errors & How I Fixed Them

| Error                                      | Cause                              | Fix                                            |
| ------------------------------------------ | ---------------------------------- | ---------------------------------------------- |
| TypeError: can only concatenate str to str | Mixed string and integer in math   | Remove quotes from number variable             |
| fatal: not a git repository                | git init not run in project folder | cd into project folder first, then git init    |
| zsh: command not found: code               | VSCode shell command not installed | Command palette → Install code command in PATH |

## Key Reminders

- Always run pwd before git commands to check your location
- Always run git init from INSIDE your project folder
- Every project needs a .gitignore file
- Add .DS_Store to .gitignore on every Mac project
