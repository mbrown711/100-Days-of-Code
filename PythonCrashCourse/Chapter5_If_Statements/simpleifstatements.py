cars = ['bmw', 'mercedes', 'subaru', 'toyota', 'audi']

for car in cars:
    # '==' means "is the car a bmw?"
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
#checking for equality is case sensitive in python

requested_toppings = 'mushrooms'
# != same as java
if requested_toppings != 'anchovies':
    print("Hold the anchovies")

answer = 17
if answer != 42:
    print("Wrong answer, try again!")

# checking if a value is in a list:
toppings = ['pepperoni', 'cheese', 'onions']
is_mushrooms = 'mushrooms' in toppings # boolean here, fals because mushrooms is not in toppings
print(is_mushrooms) # will print false

banned_users = ['matt', 'bailey', 'dalila', 'mom', 'dad']
user = 'chris'

if user not in banned_users:
    print(user.title() + ", you can post a response if you wish")

age = 19
if age >= 18:
    print("Old enough to vote")
    print("Have you registered to vote?")
# think of indents as a code block in java

age = 17
if age >= 18:
    print("Old enough to vote")
    print("Have you registered to vote?")
else:
    print("Sorry, not old enough to vote yet")