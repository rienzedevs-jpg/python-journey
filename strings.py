""""
# String manipulation practice
# Learning how Python handles text data
"""

first_name = "Rienze"
last_name = "Devs"
age = 28

# Joining two strings together — string concatenation
full_name = first_name + " " + last_name

print(full_name)
print(len(full_name))        # count total characters including space
print(full_name.upper())     # convert to uppercase
print(full_name.lower())     # convert to lowercase
print(full_name.replace("Devs", "Anda"))  # swap a word

# f-string — cleaner way to embed variables inside strings
print(f"My name is {first_name} and I am {age} years old.")