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

# Using a flag
print("\nUsing a flag below: ")
active = True
while active:
    message = input(newPrompt)
    if message == "quit":
        active = False
    else:
        print(message)

# Using break to exit a for loop:
print("\nUsing break to exit a for loop: ")
cityPrompt = "\nPlease enter the name of a city you have visited "
cityPrompt += "\n(Enter 'quit' when you are finished): "

while True:
    city = input(cityPrompt)
    if city == "quit":
        break
    else:
        print("I'd like to go to " + city.title() + "!")

# Using continue in a loop:
print("\nUsing continue in a loop: ")
currentNumber = 0
while currentNumber <= 10:
    currentNumber += 1
    if currentNumber % 2 == 0:
        continue

    print(currentNumber)

# Using a while loop with lists and dictionaries:

print("\nMoving items from one list to another: ")
# Start with a list of users that need to be verified, and an empty list to hold the users:
unconfirmedUsers = ['alice', 'bob', 'brian']
confirmedUsers = []

# Verify each user until there are no more unconfirmed users
# Move each unverified user into the list of confirmed users

while unconfirmedUsers:
    currentUser = unconfirmedUsers.pop()

    print("Verifying user: " + currentUser.title())
    confirmedUsers.append(currentUser)
# Display all confirmed users:
print("\nThe following users have been confirmed: ")
for confirmedUser in confirmedUsers:
    print(confirmedUser.title())

# Removing all instances of specific values from a list:
print("\nRemoving all instances of specific values from a list: ")
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)
while "cat" in pets:
    pets.remove("cat")
print(pets)

# Filing a dictionary with user input:
print("\nFiling a dictionary with user input: ")

responses = {}
# Set a flag to indicate that polling is active
pollingActive = True

while pollingActive:
    # Prompt for a person's name and response:
    name = input("\nWhat is your name? ")
    response = input("\nWhich mountain would you like to climb one day? ")
    
    # Store the responses in a dictionary:
    responses[name] = response

    # Find out if anyone else is going to take the poll:
    repeat = input("\nWould you like to let someone else take the poll? (yes/no)? ")
    if repeat == "no":
        pollingActive = False

# Polling is complete. Show the results:
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(name + " would like to climb " + response + ".")