# Reassigning new values to variables one after another
num = 14
print(num)

# Reassign to a new number
num = 3
print(num) #expected output = 3

# Checking data types using the type() function
type(14) #expected output = <class 'int'>
type("hello") #expected output = <class 'str'>
type(True) #expected output = <class 'bool'>
num = 14
type(num) #expected output = <class 'int'>

# Python differentiates between an int and a float (a decimal)
pi = 3.141
type(pi) #expected output = <class 'float'>

# JS 'null' is equivalent to 'None' in Python
my_nothing = None
print(my_nothing) #expected output = None

# Difference b/w / and // when dividing two numbers
# To result in an integer, divide with //
int = 6 // 2
print(int)

# To result in a decimal (a 'float'), divide with /
int2 = 6 / 2
print(int2)

# Shortcut assignment operators
# to add 1
num = num + 1
# is the same
num += 1

#to multiply by 2
num = num * 2
#is the same as
num *= 2

#to subtract 1
num = num - 1
num -= 1

# Ternery expressions
x = "Is true" if True else "Is false"
print(x)

t = 90
print("Water is boiling" if t >= 100 else "Water is not boiling")

# if, elif, else statements
# color = input('Enter "green", "yellow", or "red": ').lower()
# print(f'The user entered {color}')

# if color == 'green':
#     print("Go!")
# elif color == 'yellow':
#     print("Slow down!")
# elif color == 'red':
#     print("Stop!")
# else:
#     print("Bogus!")

# Basic for looping
colors = ["yellow", "red", "purple", "pink", "blue"]

for color in colors:
    print(color, end=" ")

# Basic while looping
count = 0
while count <= 10:
    count += 1
    print(f"The number is: {count}")

# Range
for num in range(0,5):
    print(num) # should print 0-4

# Range by 2s
for num in range(0,5,2):
    print(num) # should print 0, 2, 4

# Use range to create a list and a tuple
nums = list(range(10))
print(nums) # should print [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

odds = tuple(range(1, 10, 2))
print(odds) # should print (1, 3, 5, 7, 9)

# Use range and a negative number as step to count down
for num in range(5, 0, -1):
    print(num) # should print 5, 4, 3, 2, 1

