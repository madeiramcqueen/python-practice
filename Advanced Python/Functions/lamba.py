# LinkedIn Learning Course: Advanced Python by Joe Marini
# Practice the use of lambda functions, AKA anonymous functions in JS -- lambdas can help code become more readable

def celsiusToFahrenheit(temp):
    return (temp * 9/5) + 32


def fahrenheitToCelsius(temp):
    return (temp-32) * 5/9

def main():
    ctemps = [0, 12, 34, 100]
    ftemps = [32, 65, 100, 212]

    # use regular functions to convert temps
    print(list(map(fahrenheitToCelsius, ftemps)))
    print(list(map(celsiusToFahrenheit, ctemps)))
    

    # use lambdas convert temps
    print(list(map(lambda t: (t-32) * 5/9, ftemps)))
    print(list(map(lambda t: (t * 9/5) + 32, ctemps)))

main()