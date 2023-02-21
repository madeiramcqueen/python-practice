# LinkedIn Learning Course: Advanced Python by Joe Marini
# Advanced iteration functions in the itertools package

import itertools

def testFunction(x):
    return x < 40


def main():
    # cycle iterator can be used to cycle over a collection
    seq1 = ["Madeira", "Devi", "McQueen"]
    cycle1 = itertools.cycle(seq1)
    print(next(cycle1), end=' ') # end makes sure to put results next to each other in one string rather than on a separate line each print statement
    print(next(cycle1), end=' ')
    print(next(cycle1), end=' ')
    print(next(cycle1), end=' ')

    # use count to create a simple counter
    count1 = itertools.count(100, 10)
    print(next(count1))
    print(next(count1))
    print(next(count1))

    # accumulate creates an iterator that accumulates values
    vals = [10, 20, 30, 40, 50, 40, 30]
    acc = itertools.accumulate(vals)
    print(list(acc))

    # use chain to connect sequences together, separated into individual characters
    x = itertools.chain("ABCD", "1234")
    print(list(x))


    # dropwhile and takewhile will return values until a certain condition is met that stops them
    print(list(itertools.dropwhile(testFunction, vals)))
    print(list(itertools.takewhile(testFunction, vals)))
    

main()