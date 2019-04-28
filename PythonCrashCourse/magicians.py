magicians = ['alice', 'bob', 'matt', 'dalila', 'bailey']
for magician in magicians: # use a new variable, store it, then print it
    print(magician)

print(" ")

#just a quick note - I can't believe how different this is from an array in Java or C

magicians = ['alice', 'bob', 'matt', 'dalila', 'bailey']
for magician in magicians: # use a new variable, store it, then print it
    print(magician.title() + ", that was a great trick!")
    print("I can't wait to see your next trick " + magician.title() + ".\n")

print("Thank you everyone, that was a great magic show")

# only indent when the line of code above it "belongs" to it i.e.:
# message = 'hello'
#   print(message)
# we'll get an error on the above because print(message) doesn't "belong" to the line above it