# Demonstrate the usage of counter objects

from collections import Counter

def main():
    # list of students in class 1
    class1 = ["Bob", "Becky", "Chad", "Chad", "Pheobe", "Star", "John", "Snow"]

    # list of students in class 2
    class2 = ["Aria", "Ross", "Rachel", "Mila", "Sam", "Gabby", "Liz"]

    # create a counter for class1 and class2
    c1 = Counter(class1)
    c2 = Counter(class2)

    # how many students in class1 are named Chad?
    print(c1["Chad"])

    # how many students are in class1?
    print(sum(c1.values()), "students in class 1")

    # how many students are there total in class1 and class2?
    print(sum(c1.values()) + sum(c2.values()))

    # combine the two classes using update to update class1 to have total
    c1.update(class2)
    print(sum(c1.values()), "students in class 1")

    # what's the most common name in the two classes?
    print(c1.most_common(2))

    # separate the two classes again
    c1.subtract(class2)

main()