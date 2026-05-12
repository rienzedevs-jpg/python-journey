# Error handling — try, except

# try:
#     number = int(input("Enter a number: "))
#     print(f"You entered: {number}")
# except ValueError:
#     print("That's not a valid number. Please enter digits only.")

# Catching multiple errors

# try:
#     number = int(input("Enter a number: "))
#     result = 100 / number
#     print(f"100 divided by {number} = {result}")
# except ValueError:
#     print("That's not a valid number.")
# except ZeroDivisionError:
#     print("You can't divide by zero.")

# try, except, else, finally
# try:
#     number = int(input("Enter a number: "))
#     result = 100/number
# except ValueError:
#     print("That's not a valid number.")
# except ZeroDivisionError:
#     print("You can't divide by zero.")
# else:
#     print(f"100 divided by {number} = {result}")
#     print("No errors occurred!")
# finally:
#     print("This always runs no matter what.")

# Raising your own errors

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero — b must be non-zero.")
    return a / b

try:
    print(divide(10, 2))
    print(divide(10, 0))
except ValueError as e:
    print(f"Error caught: {e}")