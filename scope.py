# Scope — where variables can be seen

# name = "Rienze"  # global variable

# def greet():
#     print(f"Hello {name}!")  # can it see the global variable?

# greet()
# print(name)

# Local scope — variables inside functions

# def greet():
#     message = "Hello Rienze!"  # local variable
#     print(message)

# greet()
# print(message)  # can we access it outside the function?

# What happens when local and global have the same name?

# name = "Rienze"  # global

# def greet():
#     name = "John"  # local — same name, different variable
#     print(f"Inside function: {name}")

# greet()
# print(f"Outside function: {name}")

# Common mistake — trying to modify a global inside a function

# counter = 0

# def increment():
#     global counter  # tell Python to use the global one
#     counter += 1
#     print(counter)

# increment()
# increment()
# increment()

# Professional approach — no global needed

# def increment(counter):
#     return counter + 1

# counter = 0
# counter = increment(counter)
# counter = increment(counter)
# counter = increment(counter)
# print(counter)

# Enclosing scope — function inside a function

# def outer():
#     message = "I am outer"
    
#     def inner():
#         print(message)  # can inner see outer's variable?
    
#     inner()

# outer()

# name = "Global Rienze"          # G — Global

# def outer():
#     name = "Enclosing Rienze"   # E — Enclosing
    
#     def inner():
#         name = "Local Rienze"   # L — Local
#         print(name)             # which one does Python use?
    
#     inner()

# outer()

name = "Global Rienze"          # G

def outer():
    name = "Enclosing Rienze"   # E
    
    def inner():
        print(name)             # no local — goes up to enclosing
    
    inner()

outer()
print(name)                     # no local or enclosing — goes up to global