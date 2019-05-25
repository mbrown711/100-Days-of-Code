age = 19
if age >= 18:
    print("You are old enough to vote")
else:
    print("Sorry, not old enough to vote")

# Using if-elif-else chain - amusement park example below

age = 12
if age < 4:
    print("Your admission cost is $0")
elif age < 18:
    print("Your admission cost is $5")
else:
    print("Your admission cost is $10")

age = 13 
if age < 4:
    price = 0
elif age < 18:
    price = 5
else:
    price = 10
print("Your cost for admission is $" + str(price) + ".")

# checking if items are in a list:

requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("sorry, we are out of green peppers right now")
    else:
        print("Adding " + requested_topping + ".")

print("\nFinished making your pizza!")