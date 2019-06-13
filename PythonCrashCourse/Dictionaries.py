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
print("\nTracking the alien moving at different speeds:\n")
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
print("\nRemoving key-value pairs:\n")
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
print("\nSarah's favorite language is " + favoriteLanguages['sarah'].title() + ".")

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

# Looping through the "favoriteLanguages dictionary"
print("\nPrinting the items in the favorite language dictionary:\n")
for name, language in favoriteLanguages.items():
    print(name.title() + "'s favorite language is " + language.title() + ".")

# Looping through all the keys in a dictionary:
print("\nPrinting the KEYS in the favoriteLanguages dictionary:\n")
for name in favoriteLanguages.keys():
    print(name.title())

friends = ['phil', 'sarah']
for name in favoriteLanguages.keys():
    print(name.title())

    if name in friends:
        print(" Hi " + name.title() + ", I see your favorite language is " + favoriteLanguages[name].title() + "!")

if 'erin' not in favoriteLanguages.keys():
    print("Erin, please take our poll!")

# Looping through a dictionary's keys in order:
print("\nLooping through a dictionary's keys in order:\n")
for name in sorted(favoriteLanguages.keys()):
    print(name.title() + ", thank you for taking the poll!")

# Looping through all values in a dictionary:
print("\nLooping through all values in a dictionary:\n")
print("The following languages have been mentioned:")
for language in favoriteLanguages.values():
    print(language.title())

# Use a set for large lists instead of the above, like so:
print("\nUsing a set:")
print("The following languages have been mentioned:")
for language in set(favoriteLanguages.values()):
    print(language.title())

# Nesting - storing a set of dictionaries in a list or a list of items as a value in a dictionary
# A list of dictionaries, the following builds a list of 3 aliens:
alien0 = {'color' : 'green', 'points' : 5}
alien1 = {'color' : 'yellow', 'points' : 10}
alien2 = {'color' : 'red', 'points' : 15}

aliens = [alien0, alien1, alien2]

print("\nPrinting a list of dictionaries:")
for alien in aliens:
    print(alien)

# Using range() to create a fleet of 30 aliens:
print("\nUsing range() to create a fleet of 30 aliens:")

# Begin with an empty list to store all of the aliens:
aliens = []
# Making 30 green aliens:
for numberOfAliens in range(30):
    newAlien = {'color' : 'green', 'points' : 5, 'speed' : 'slow'}
    aliens.append(newAlien)

# Modifying an alien object:
for alien in aliens [0:3]:
    if alien['color'] == 'green':
        alien['color'] == 'yellow'
        alien['speed'] == 'medium'
        alien['points'] == '10'

# Show the first 5 aliens:
for alien in aliens[0:5]:
    print(alien)
print("...")

# Show how many aliens have been created:
print("Total number of aliens: " + str(len(aliens)))

# A list in a dictionary:
