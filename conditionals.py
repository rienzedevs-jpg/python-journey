# A simple login system - improved

print("Welcome to the system.\n")

username = input("Enter your username: ")
password = input("Enter your password: ")

correct_username = "rienze"
correct_password = "python123"
is_banned = False

if is_banned:
    print("You are banned from this system.")
elif username == correct_username and password == correct_password:
    age = int(input("Enter your age: "))
    if age >= 18:
        print(f"\nWelcome back {username}! Access granted.")
    else:
        print(f"\nSorry {username}. You must be 18 or older.")
else:
    print("\nIncorrect username or password. Access denied.")