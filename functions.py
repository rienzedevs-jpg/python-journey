# Functions — write once, use anywhere

# def greet(name, messages):
#     print(f"Welcome {name}!")
#     print(f"You have {messages} new messages.")
#     print("---")

# greet("Rienze", 3)
# greet("John", 5)
# greet("Maria", 1)

# Functions with return values

# def add(a, b):
#     return a + b

# def multiply(a, b):
#     return a * b

# result1 = add(10, 5)
# result2 = multiply(10, 5)

# print(result1) #15
# print(result2) #50
# print(add(100, 200)) #300
# print(multiply(result1, result2)) #15*50
# print vs return — important distinction

# def add_with_print(a, b):
#     print(a + b)

# def add_with_return(a, b):
#     return a + b

# result1 = add_with_print(3, 4)
# result2 = add_with_return(3, 4)

# print(f"result1 is: {result1}")
# print(f"result2 is: {result2}")

# # Default parameters

# def greet(name, greeting="Hello"):
#     return f"{greeting} {name}!"

# print(greet("Rienze"))
# print(greet("Rienze", "Good morning"))
# print(greet("Rienze", "Mabuhay"))

def calculate(num1, num2, operation="add"):
    num1 = float(num1)
    num2 = float(num2)
    operation = operation.lower()
    if operation== 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            return "Cannot divide by zero"
            
        return num1 / num2
    else:
        return "Unknown operation"


# Functions calling other functions

def get_user_input():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    operation = input("Enter operation (add, subtract, multiply, divide): ")
    return num1, num2, operation

def display_result(num1, num2, operation, result):
    print(f"\n{num1} {operation} {num2} = {result}")

def run_calculator():
    num1, num2, operation = get_user_input()
    result = calculate(num1, num2, operation)
    display_result(num1, num2, operation, result)

run_calculator()
