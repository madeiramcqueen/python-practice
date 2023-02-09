# # index 0-101 = 100 doors
# # False doors = closed doors, True doors = open doors
# doors = [False] * 101

# print(doors)

# for i in range(1, 101):
#     # because we are using boolean values, we can use "not" to act as the inverse
#     doors[i] = not doors[i]

# print(doors)

# for i in range(1,6):
#     for j in range(1,4):
#         print("i:", i, "j:", j)

# for i in range(1, 11, 2):
#     print (i)

doors = [False] * 101

for i in range(1, 101):
    for j in range(i, 101, i):
        doors[j] = not doors[j]

for i in range(1, 101):
    if doors[i] is True:
        print(i)
