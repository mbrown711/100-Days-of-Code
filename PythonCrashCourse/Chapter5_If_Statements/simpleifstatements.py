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