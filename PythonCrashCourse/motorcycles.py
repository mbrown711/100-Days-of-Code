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
print("Inserting BMW into the motorcycles list: ", motorcycles)