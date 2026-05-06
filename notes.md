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

## Booleans & Comparison Operators

| Operator | Meaning                  | Example |
| -------- | ------------------------ | ------- |
| >        | Greater than             | a > b   |
| <        | Less than                | a < b   |
| ==       | Equal to                 | a == b  |
| !=       | Not equal to             | a != b  |
| >=       | Greater than or equal to | a >= 10 |
| <=       | Less than or equal to    | a <= 10 |

## Logical Operators

| Operator | Returns True when       | Example              |
| -------- | ----------------------- | -------------------- |
| and      | ALL conditions are True | age >= 18 and has_id |
| or       | ANY condition is True   | cash or card         |
| not      | Condition is False      | not is_banned        |

## Key Reminders

- Single = assigns a value
- Double == compares two values
- and is like a chain — one False breaks everything
- or is like doors — only one needs to be open
- Trace logical expressions step by step when debugging

## VSCode Shortcuts

| Shortcut    | What it does                             |
| ----------- | ---------------------------------------- |
| Command + / | Toggle comment on/off for selected lines |

## User Input

- input() pauses the program and waits for the user to type
- input() ALWAYS returns a string — even if the user types a number
- Use int() or float() to convert input to a number
- Can combine in one line: age = int(input("How old are you? "))

## Escape Characters

| Character | What it does                  |
| --------- | ----------------------------- |
| \n        | New line                      |
| \t        | Tab indentation               |
| \\        | Literal backslash             |
| \"        | Literal quote inside a string |

## How to push to Github

1. git add notes.md README.md
2. git commit -m "updated notes and README for day 3"
3. git push

## Conditionals

- if — first condition, always required
- elif — additional conditions, optional, as many as needed
- else — catches everything that didn't match, optional

## Syntax

if condition: # code runs if True
elif another_condition: # code runs if this is True
else: # code runs if nothing above matched

## Key Reminders

- Colon : opens the block
- 4 spaces indentation — PEP 8 standard
- Python reads top to bottom and stops at first True condition
- Nested conditionals — if inside an if — keep shallow
- Defensive programming — never trust user input
- Only collect information when you actually need it

## Loops

### For Loop

for item in collection: # runs for each item

for number in range(1, 6): # runs for numbers 1 to 5

### Range

range(5) # 0, 1, 2, 3, 4
range(1, 6) # 1, 2, 3, 4, 5
range(0, 10, 2) # 0, 2, 4, 6, 8 — step

### While Loop

while condition: # runs until condition is False # always needs an increment or way to become False

### Loop Control

- break — exits the loop completely
- continue — skips current iteration, continues loop

### Three ingredients of a safe while loop

1. Starting value
2. Condition that will eventually be False
3. Something that changes each loop

### Infinite Loop

- Missing increment = infinite loop
- Control + C to kill a running program

## Key Reminders

- for loop — use when you know how many times to repeat
- while loop — use when you don't know, just repeat until something changes
- Always validate user input before converting with int()
- if not variable — checks if input is empty
- Consistent 4 space indentation — mixing causes IndentationError

## Functions

### Basic Structure

def function_name(parameter1, parameter2): # function body
return value

### Key Concepts

- def — keyword to define a function
- Parameters — placeholders defined in the function
- Arguments — actual values passed when calling
- return — sends a value back to the caller
- None — what a function returns if no return statement

### Default Parameters

def greet(name, greeting="Hello"):
return f"{greeting} {name}!"

# If no greeting passed — uses "Hello" as default

### print vs return

- print — displays something, returns Nothing
- return — gives a value back to be used elsewhere
- In real programs almost everything uses return

### DRY Principle

Don't Repeat Yourself

- If you write the same thing more than once — refactor
- Convert/clean variables once at the top of the function

### Single Responsibility Principle

- Each function should do ONE thing and do it well
- Break big functions into smaller focused ones
- Makes code readable, testable, and maintainable

### Returning Multiple Values

def get_values():
return num1, num2, operation

# Unpack in one line

num1, num2, operation = get_values()
