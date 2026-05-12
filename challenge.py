try:
    user_name = input("Enter your username: ").strip()
    if len(user_name) < 3:
        raise ValueError("User name must be at least 3 characters")   
    user_age = int(input("Enter your age: ").strip())
    if user_age < 18 or user_age > 100:
        raise ValueError("Age must be between 18 and 100")
    user_pw = input("Enter your password: ").strip()
    if len(user_pw) < 8:
        raise ValueError("Password must be at least 8 characters")
except ValueError as e:
    print(f"Error caught: {e}")
else:
    print("Everything is successful")
finally:
    print("Registration attempt complete.")
