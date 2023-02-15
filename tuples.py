# Python Crash Course exercises Ch. 4
# A tuple is a list of items that cannot change -- they are immutable.
# Formatted by parenthesis rather than square brackets --> () NOT []

# Example
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

# Example of failed manipulation of a tuple, will return a TypeError
# dimensions[0] = 300
# print(dimensions[0])

# Looping through all values in a tuple, same way as looping through a list
print("\nOriginal dimensions:")
for dimension in dimensions:
    print(dimension)

# Writing over a tuple
dimensions = (500,700)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)