# Python Crash Course exercises Ch. 4

players = ['Madeira', 'Caroline', 'Azima', 'Kayla', 'Meredith', 'Noel']

# Use slice method to print players Madeira-Azima
print(players[0:3]) # index to the right of : is not included

# Use slice method to print players Caroline onwards
print(players[1:])

# Use slice method to print from beginning of list to a certain index -- always starts with :
print(players[:3])

# Use slice method to print last 2 players
print(players[-2:])

# User slice method to skip numbers by 3
print(players[:6:2])

#Loop through a slice
print('Here are the first three players:')

for player in players[:3]:
    print(player)

# Make a copy of the list
players_list = players[:]
print(players_list)

# Add a name to players_list then compare to make sure players_list is still a copy of player list but with added name
players_list.append('Sean')
print(players_list)
print(players)

foods = ['pizza', 'thai food', 'pasta', 'tacos']
print(foods)

# Append oysters to foods list
foods.append('oysters')
print(foods)

# Make a copy of foods list for friends
friends_foods = foods[:]
print(friends_foods)
# Append a food item to friends_foods
friends_foods.append('burger and fries')
print(friends_foods)

# Use string interpolation using the two foods lists
print(f"My favorite foods are {foods} and my friends' favorites foods are {friends_foods}")
