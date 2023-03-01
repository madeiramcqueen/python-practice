# LinkedIn Learning Course: Advanced Python by Joe Marini
# Demonstrate the use of key-words only arguments

def myFunction(arg1, arg2, *, suppressExceptions=False):
    pass


def main():
    myFunction(1,2, suppressExceptions=True)

if __name__ == "__main__":
    main()