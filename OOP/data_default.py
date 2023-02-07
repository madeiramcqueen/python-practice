# LinkedIn Learning: "Python Object Oriented Programming" Course, Ch. 4
# Implementing default values in data classes

from dataclasses import dataclass, field
import random

def price_func():
    return float(random.randrange(20, 40))

@dataclass
class Book:
    # Define default values when attributes are declared
    title : str = "No title"
    author : str = "No author"
    pages : int = 0
    price : float = field(default_factory=price_func)


b1 = Book("Python Crash Course", "Eric Matthes", 345, 25.00)
b2 = Book("The Scent Keeper", "Erica Bauermeister", 250)

print(b1)
print(b2)
