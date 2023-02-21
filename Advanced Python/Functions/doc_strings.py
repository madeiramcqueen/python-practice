# LinkedIn Learning Course: Advanced Python by Joe Marini
# Practice using function docstrings

def myFunction(arg1, arg2=None):
    """myFunction(arg1, arg2=None) --> Don't do much, just prints

    Parameters:
    arg1: first argument
    arg2: second argument, defaulted to None
    """
    print(arg1, arg2)


def main():
    print(myFunction.__doc__)


if __name__ == "__main__":
    main()