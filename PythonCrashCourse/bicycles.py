bicycles = ['trek', 'cannondale', 'redline', 'specialized']
# if you print the entire list, prints out ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

# want to show a better interface to the user
# printing out an index in bicycles list:
print(bicycles[0])

# can implement string methods seen earlier:
print(bicycles[0].title())

# printing a certain element in a sentence:
print("My first bike was a " + bicycles[0].title() + ".")

names = ['Matt', 'Rob', 'Cesar']
print(names)
print("Hi " + names[0] + " how are you?")