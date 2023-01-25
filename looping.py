# looping through lists practice
names = ["madeira", "clyde", "colleen", "sean"]

# loop through each name in the list using a FOR LOOP
for name in names:
   # print(name)
# print f string looping through names
    print(f'{name.title()} is so cool!')
print(f'Have a great weekend, {names[0]}, {names[1]}, {names[2]}, and {names[3]}!')

# pizza looping practice
pizzas = ["pepperoni", "sausage", "veggie"]

for pizza in pizzas: 
    print(f"I'd like a {pizza} pizza please. Thank you!")
    #print a statement after the loop completes
print("I love pizza SO much. I could eat it every day if I had to!")

# animals looping practice
animals = ["elephant", "whale", "giraffe", "cheetah"]

print("These are my favorite animals:")
for animal in animals:
    print(animal.title())
    # f string in a loop
    print(f"It would be so cool to see a {animal}")
print("All of these animals are wild animals. You definitely cannot have them as pets!")