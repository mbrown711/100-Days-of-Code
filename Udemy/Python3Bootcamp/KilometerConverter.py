# 1 mile = 1.60934km

print("How many kilometers to convert?")
kilometers = float(input())
miles = kilometers/1.60934
miles = round(miles, 2)
# need to use f to format an int into a string
print(f"Ok, you said {kilometers}")
print(f"That is equal to {miles} miles")