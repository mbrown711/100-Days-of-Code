# for loop syntax:
# for item in iterable_object:
#     do something with item

# iterable object = collection of data

for x in range(1, 10):
    print(x)

for letter in "coffee":
    print(letter)
    print(letter * 10)

for num in range(10):
    print(num)

for num in range(10, 20, 2):
    print(num)

# add up all odd numbers between 10 and 20 (inclusive):
x = 0
for n in range (10, 21):
    if n % 2 != 0:
        x += n

print(f"The sum is {x}")
# OR by using range:
x = 0
for i in range(11, 21, 2):
    x += i
print(f"The sum using range is {x}")

#repeating question exercise
askingQuestions = input ("How many times do you want to repeat? ")
askingQuestions = int(askingQuestions)
for askingQuestion in range(askingQuestions):
    print(f"Ok, repeating question. Repeat number: {askingQuestion + 1}")

# loop through numbers 1 - 20 (inclusive)
# for 4 and 13, print "x is unlucky"
# for odd numbers, print "x is odd"

for num in range (1, 21):
    if num == 4 or num == 13:
        state = "unlucky"
    elif num % 2 == 0:
        state = "even"
    else:
        state = "odd"
    print(f"{num} is {state}")

# while loops:

msg = input("What's the secret password? ")
while msg != "bananas":
    print("Wrong!")
    msg = input("What's the secret password? ")
print("Correct!")

number = 1
while number <= 10:
    print(number)
    number += 1