# slicing a list:
players = ['matt', 'dalila', 'bailey', 'kelly', 'chris']
print(players[0:3])

# can do any subset of players:
print(players[1:4])

# if no starting number, prints from the beginning of the list:
print(players[:4])

# looping through a slice:
print("Here are the first 3 players on my team:")
for player in players[:3]:
    print(player.title())