#Chapter 6 - Dictionaries

# Dictionary below stores info about a particular alien:
alien_0 = {'color': 'green', 'points': 5}

print(alien_0['color'])
print(alien_0['points'])

newPoints = alien_0['points']
print("You just scored " + str(newPoints) + " points!")

# Adding new key-value pairs

print(alien_0)
alien_0['xPosition'] = 0
alien_0['yPosition'] = 25
print(alien_0)

#Python doesn’t care about the order in which you store each key-value pair; it cares only about the connection between each key and its value.

# Starting with an empty dictionary:
print("Starting with an empty dictionary:")
alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = 5
print("Starting with an empty dictionary:")
print(alien_0)

# Modifying value in a dictionary:
print("Modifying value in a dictionary:")
alien_0 = {'color' : 'green'}
print("The alien is " + alien_0['color'] + ".")
alien_0['color'] = 'yellow'
print("The alien is now " + alien_0['color'] + ".")

# Tracking the alien moving at different speeds:
print("Tracking the alien moving at different speeds:")
alien_0 = {'xPosition' : 0, 'yPosition' : 25, 'speed' : 'medium'}
print("Original x-position: " + str(alien_0['xPosition']))

# Moving the alien to the right below
# Determine how far to move the alien based on its current speed
if alien_0['speed'] == 'slow':
    xIncrement = 1
elif alien_0['speed'] == 'medium':
    xIncrement = 2
else:
    # This is a fast alien
    xIncrement = 3

#The new position is the old position plus the increment:
alien_0['xPosition'] = alien_0['xPosition'] + xIncrement
print("New position is: " + str(alien_0['xPosition']))

# Removing key-value pairs:
print("Removing key-value pairs:")
# Removing the key 'points' below:
alien_0 = {'color' : 'green', 'points' : 5}
print(alien_0)
del alien_0['points']
print(alien_0)

# A dictionary of similar objects
favoriteLanguages = {
    'jen' : 'python',
    'sarah' : 'c',
    'edward' : 'ruby',
    'phil' : 'python',
}

# Looking up a person's favorite language:
print("Sarah's favorite language is " + favoriteLanguages['sarah'].title() + ".")

# Looping through a dictionary:
# new dictionary about a user on a website below:
user_0 = {
    'username' : 'mbrown',
    'first' : 'Matt',
    'last' : 'Brown',
}

for key, value in user_0.items():
    print("\nKey: " + key)
    print("Value: " + value)
