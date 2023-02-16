# Python Crash Course exercises Ch. 5

cars = ['audi', 'bmw', 'subaru', 'toyota']

# If statement looping through list of cars to print only bmw all upercase, otherwise all cars should just have first letter as uppercase
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

# A conditional test is an if statement that can be evaluated as True or False
car = 'bmw'
car == 'bmw' # Should evaluate to True

# Testing for equality is CASE SENSITIVE
car = 'Audi'
car == 'audi' # Should evaluate to False

# Checking for inequality
number = 10
if number != 9:
    print('Try again!')

# Simple elif statements
age = 20
if age < 4:
    print("Your admission cost is $0")

elif age > 18:
    print("Your admission cost is $25")

else:
    print("Your admission cost is $40")

# More efficient way: Putting the price inside each statement
age = 12
if age < 4:
    price = 0

elif age > 18:
    price = 25

else:
    price = 40

print(f"Your admission cost is ${price}")