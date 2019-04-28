motorcycles = ['honda', 'harley', 'yamaha', 'suzuki']
print(motorcycles)

# below replaces whatever index spot with a different value
motorcycles[0] = 'ducati'

print(motorcycles)

#to add an element to a list, use .append()
motorcycles.append('kawasaki')

print(motorcycles)

#could also add elements to a list by appending them to an empty list:
new_motorcycles = []

new_motorcycles.append('new bike 1')
new_motorcycles.append('new bike 2')
new_motorcycles.append('new bike 3')

print(new_motorcycles)

#can insert items into a list with .insert()
motorcycles.insert(0, 'BMW')
print("Inserting BMW into the motorcycles list:", motorcycles)

# deleting elements from a list:
del motorcycles[0]
print ("Deleting the first element at index 0:", motorcycles)

# using the pop() method to remove the last item in a list
# pop() allows us to still work with the item that we removed, delete does not
popped_motorcycle = motorcycles.pop()
print("List without the pop() method", motorcycles)
print("popped_motorcycle will be the last item in the list that is removed", popped_motorcycle)

# can also pop any item in the list by using its index:
popped_idex1 = motorcycles.pop(1)
print("Popping index 1:", popped_idex1.title())

# removing an item in the list with .remove() and using the value instead of index (i.e. 'ducati')
# NOTE - remove only removes the first instance of the value specified. If there are dups, need to use a loop
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print("\nA " + too_expensive.title() + " is too expensive for me")