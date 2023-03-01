# Demonstrate the usage of default dict objects

from collections import defaultdict

def main():
    # define a list of items we want to count
    fruits = ["apple", "mango", "orange", "banana", "apple", "grape", "banana", "banana"]

    # use a dictionary to count each element in list
    fruit_counter = defaultdict(int)

    # count the elements in the list
    for fruit in fruits:
        fruit_counter[fruit] += 1

    # print the result
    for (k, v) in fruit_counter.items():
        print(k + ":" + str(v))

main()