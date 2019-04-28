# using sort() method to sort a list of cars:
# sort() changes the list PERMANENTLY, can't ever go back
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

#sorting in reverse order
cars_reversed = ['bmw', 'audi', 'toyota', 'subaru']
cars_reversed.sort(reverse = True)
print("Reverse sorted list:", cars_reversed)

# sorting temporarily with sorted()
cars_temporary = ['bmw', 'audi', 'toyota', 'subaru']
print("Original cars_temporary list:", cars_temporary)
print("Here is temporary sort:", sorted(cars_temporary))
print("Back to original cars_temporary list", cars_temporary)

#printing in reverse order - not a sorted reverse list:
cars_unsorted_reverse = ['bmw', 'audi', 'toyota', 'subaru', 'mercedes']
cars_unsorted_reverse.reverse()
print("Reverse unsorted list:", cars_unsorted_reverse)

# finding the length of a list:
print("Length of the list cars is:", len(cars))
# NOTE - length count starts at 1, NOT 0