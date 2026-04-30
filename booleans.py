a = 10
b = 3

# print(a > b) #true
# print(a < b) #false
# print(a==b) #false
# print(a != b) #true
# print(a >= 10)   # greater than or equal to
# print(a <= 10)   # less than or equal to

# Real world examples
age = 20
has_id = True
ticket_price = 50
wallet = 45

# print(age >= 18)           # is this person old enough?
# print(wallet >= ticket_price)  # can they afford the ticket?
# print(age >= 18 and has_id)    # old enough AND has ID?

# Logical operators
is_old_enough = True
has_id = False
is_banned = True

# and — both must be True
print(is_old_enough and has_id) #false

# or — at least one must be True
print(is_old_enough or has_id) #true

# not — flips the result
print(not is_banned) #false

# combining them
print(is_old_enough and has_id and not is_banned) #false


