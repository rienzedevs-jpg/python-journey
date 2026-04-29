# Numbers and math operations in Python

a = 10
b = 3

print(a + b)   # addition
print(a - b)   # subtraction
print(a * b)   # multiplication
print(a / b)   # division
print(a // b)  # floor division
print(a % b)   # modulo
print(a ** b)  # exponent

print(10 / 2)    # regular division
print(10 // 2)   # floor division
print(type(10 / 2))
print(type(10 // 2))

print(2 + 3 * 4)      # what do you think this prints? 14
print((2 + 3) * 4)    # what about this? 20

# Built in math functions
print(round(3.14159, 2))   # round to 2 decimal places
print(abs(-42))             # absolute value
print(max(10, 3, 7, 25, 1)) # largest number
print(min(10, 3, 7, 25, 1)) # smallest number
print(sum([10, 3, 7, 25, 1])) # add them all up

# Augmented assignment
score = 0
print(score)

score = score + 10
print(score)

score += 10
print(score) #30

score -= 5
print(score) #25

score *= 2
print(score) #50