# using range() function to go through a list
# starts at first value, stops at second, so prints 1, 2, 3, 4 but not 5
for value in range(1, 5):
    print(value)

# using the range() function to MAKE a list of numbers:
numbers = list(range(1, 6))
print("Printing numbers list:", numbers)

# using range to print even numbers:
even_numbers = list(range(2, 11, 2)) # the last value states the increment in the range
print("Printing even_numbers:", even_numbers)

squares = []
for square_values in range(1, 11):
    # exponents shown by **
    # each value is raised to the second power
    square = square_values**2
    # appending the squared number to the squares list
    squares.append(square)
print("Squares list:", squares)

# a more efficient version of the code above:
squares2 = []
for square_values2 in range(1, 11):
    squares2.append(square_values2**2)
print("Squares2 list:", squares2)

# some statistics in python:
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

min = min(digits)
print("Min in digits = ", min)

max = max(digits)
print("Max in digits = ", max)

sum = sum(digits)
print("Sum in digits = ", sum)

# list comprehension example below - combines for loop and creation in one line
# and automatically appends them
squares_comprehension = [value**2 for value in range (1, 11)]
print("Squares made via list comprehension:", squares_comprehension)