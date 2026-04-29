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

## String Methods

| Method/Function    | What it does                                |
| ------------------ | ------------------------------------------- |
| len()              | Counts total characters in a string         |
| .upper()           | Converts string to uppercase                |
| .lower()           | Converts string to lowercase                |
| .replace(old, new) | Swaps one value for another                 |
| str()              | Converts a value to a string — type casting |

## F-strings

Cleaner way to embed variables inside strings
Example: f"My name is {first_name} and I am {age} years old."

## Comments

# Single line comment

""" Multi line comment / docstring """
Good comments explain WHY not WHAT

## Key Concepts

- String concatenation — joining strings with +
- Methods belong to data types and are called with a dot — full_name.upper()
- Functions are standalone — len(), print(), str(), type()
- Type casting — converting one data type to another using str(), int(), float()

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

## Numbers & Math

| Operator     | What it does                     | Example          |
| ------------ | -------------------------------- | ---------------- |
| + - \*       | Basic math                       | 10 + 3 = 13      |
| /            | Division — always returns float  | 10 / 2 = 5.0     |
| //           | Floor division — returns integer | 10 // 3 = 3      |
| %            | Modulo — returns remainder       | 10 % 3 = 1       |
| \*\*         | Exponent                         | 10 \*\* 3 = 1000 |
| += -= \*= /= | Augmented assignment             | score += 10      |

## Built-in Math Functions

| Function           | What it does                      |
| ------------------ | --------------------------------- |
| round(n, decimals) | Round to decimal places           |
| abs(n)             | Absolute value — removes negative |
| max(...)           | Largest value                     |
| min(...)           | Smallest value                    |
| sum([...])         | Adds everything up                |

## Key Reminders

- / always returns float even if result is whole number
- // returns integer — strips decimal completely
- When in doubt use parentheses for order of operations
- PEMDAS — Parentheses, Exponents, Multiplication/Division, Addition/Subtraction

## Key Reminders

- Always run pwd before git commands to check your location
- Always run git init from INSIDE your project folder
- Every project needs a .gitignore file
- Add .DS_Store to .gitignore on every Mac project
