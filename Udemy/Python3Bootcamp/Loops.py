# for loop syntax:
# for item in iterable_object:
#     do something with item

# iterable object = collection of data

for x in range(1, 10):
    print(x)

for letter in "coffee":
    print(letter)
    print(letter * 10)

for num in range(10):
    print(num)

for num in range(10, 20, 2):
    print(num)

# add up all odd numbers between 10 and 20 (inclusive):
x = 0
for n in range (10, 21):
    if n % 2 != 0:
        x += n

print(f"The sum is {x}")
# OR by using range:
x = 0
for i in range(11, 21, 2):
    x += i
print(f"The sum using range is {x}")