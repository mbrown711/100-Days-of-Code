# How user input works:
message = input("Tell me something and I'll repeat it back to you: ")
print(message)

name = input("Please enter your name: ")
print("Hello, " + name)

# Writing multiple lines:

prompt = "If you tell us who you are, we can personalize the message for you."
prompt += "\nWhat is your first name? "
greeting = input(prompt)
print("\nHello, " + greeting + "!")

# Using int() to convert a string into an integer
age = input("How old are you? ")
age = int(age)
age >= 18

height = input("How tall are you in inches? ")
height = int(height)

if height >= 36:
    print("\nYou are tall enough to ride!")
else:
    print("\nYou'll be able to ride when you're taller")

# Modulo operator practice:
print("\nModulo operator practice")
number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)
if number % 2 == 0:
    print("\nThe number is even.")
else:
    print("\nThe number is odd")

# Introducing while loops:
print("\nWhile loop in python:")
currentNo = 1
while currentNo <= 5:
    print(currentNo)
    currentNo += 1

# Letting the user know how to quit:
print("\nLeting the user know how to quit: ")
newPrompt = "\nTell me something and I will repeat it back to you: "
newPrompt += "\nEnter 'quit' to end the program. "
message = " "
while message != "quit":
    message = input(newPrompt)
    if message != "quit":
        print(message)