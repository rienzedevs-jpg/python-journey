# Loops — for loop
# Repeating actions without repeating code

# fruits = ["apple", "banana", "mango", "grapes", "orange"]

# for fruit in fruits:
#     print(fruit)


# Three forms of range
# for number in range(5):
#     print(number) #0 1 2 3 4

# print("---")

# for number in range(1, 6): #1 2 3 4
#     print(number)

# print("---")

# for number in range(0, 10, 2):
#     print(number)

# for number in range(1, 11):
#     if number % 2 == 0:
#         print(f"{number} is even")

#     else:
#         print(f"{number} is odd")

# While loop — keeps going until condition is False

# counter = 0

# while counter < 5:
#     print(f"Counter is {counter}")
#     counter += 1

# print("Done!")

# user_input = "";

# while user_input != "quit":
#     user_input = input("Type something (or 'quit' to exit):")
#     print(f"You typed: {user_input}")

# print("Goodbye!")

# break and continue

# for number in range(1, 11):
#     if number == 5:
#         break
#     print(number)

# print("---")

# for number in range(1, 11):
#     if number == 5:
#         continue
#     print(number)

secret_number = 7
attempts = 0
max_attempts = 3

print("Welcome to the number guessing game!")
print(f"You have {max_attempts} attempts to guess the secret number between 1 and 10")

while attempts < max_attempts:

    guess = input("Enter your guess: ")
    if not guess:
        print("Please enter a number!");
        continue
   
    guess_int = int(guess)
    attempts += 1

    if guess_int == secret_number:
        print(f"\nCorrect! You got it in {attempts} attempt(s)!")
        break
    elif guess_int < secret_number:
        print(f"Too low! {max_attempts - attempts} attempt(s) remaining.")
    else:
        print(f"Too high! {max_attempts - attempts} attempt(s) remaining.")

    if attempts == max_attempts and guess_int != secret_number:
        print(f"\nGame over! The secret number was {secret_number}.")