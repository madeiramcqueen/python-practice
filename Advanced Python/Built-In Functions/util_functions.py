# LinkedIn Learning Course: Advanced Python by Joe Marini
# Demonstrate built-in utility functions

def main():
    # use any() and all() to test sequences for boolean values
    list1 = [1, 2, 3, 0, 5, 6]

    # any() will return True if any of the sequence values are True
    print(any(list1)) # should print True

    # all() will return True only if ALL values are True
    print(all(list1)) # should print False because it has 0

    # min and max will return minimum and maximum values in a sequence
    print("Min:", min(list1)) # should print 0
    print("Max:", max(list1)) # should print 6

    # use (sum) to sum up all of the values in a sequence
    print("Sum:", sum(list1)) # should print the sum

main()