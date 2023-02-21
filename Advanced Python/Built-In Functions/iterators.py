# LinkedIn Learning Course: Advanced Python by Joe Marini
# Use iterator functions like enumerate, zip, iter, next

def main():
    # define a list of days in English and French
    days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
    daysFr = ["Dim", "Lun", "Mer", "Jeu", "Ven", "Sam"]

    # use iter method to create an iterator over a collection
    # i = iter(days)
    # print(next(i))
    # print(next(i))
    # print(next(i))
    # print(next(i))

    # iterate using a function and a sentinel
    with open("Advanced Python/Built-In Functions/testfile.txt", "r") as fp:
        for line in iter(fp.readline, ''):
            print(line)

    # use regular interation over the days
    for day in range(len(days)):
        print(day+1, days[day])

    # use enumerate to reduce code and provide a counter
    for i, day in enumerate(days, start=1):
        print(i, day)

    # use zip to combine sequences and create tuples
    for day in zip(days, daysFr):
        print(day)

print(main())