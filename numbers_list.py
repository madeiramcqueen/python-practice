# Python Crash Course exercises

# printing out a range
for value in range(1,5):
    print(value) # result will not include 5

# converting a range of numbers into a list using the list() function
numbers = list(range(1,5))
print(numbers)

# skipping a number by 2s in a list
numbers = list(range(2,11,2))
print(numbers)

# append square roots to an empty list
squares = []
# for value in range(1, 11):
#     square = value ** 2
#     squares.append(square)
# print(squares)

# refactored to more concise code
for value in range(1,11):
    squares.append(value ** 2)
print(squares)

# finding the min, max, or sum of a list of numbers
digits = [1, 3, 5, 7, 9]
sum(digits)
print(f"This is the sum: {sum(digits)}")
print(f"This is the smallest number: {min(digits)}")
print(f"This is the largest number: {max(digits)}")

# print numbers 1-20 inclusive
for value in range(1,21):
    print(value)

# make a list of numbers 1-50, appending to an empty list --> then find the min, max, and sum
long_list = []
for value in range(0,50):
    long_list.append(value + 1)
print(long_list)
print(f"This is the sum: {sum(long_list)}")
print(f"This is the smallest number: {min(long_list)}")
print(f"This is the largest number: {max(long_list)}")

# print odd numbers in a loop, numbers 1-10
for value in range(1,11,2):
    print(value)
