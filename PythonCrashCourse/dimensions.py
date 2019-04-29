# tuples - immutable and use () instead of []
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

# if we try to change, we get an error:
# dimensions[0] = 250
# print(dimensions)

# looping through a tuple:
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)

# writing over tuples:
dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)