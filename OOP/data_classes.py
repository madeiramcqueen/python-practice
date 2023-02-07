# LinkedIn Learning: "Python Object Oriented Programming" Course, Ch. 4
# Using data classes to represent data objects

from dataclasses import dataclass

# rewrite this Book class to automate its init function where every attribute will automatically be initialized on the object instance

# data classes also automatically implement repr and eq functions

@dataclass
class Book:
    # each attribute is assigned a type hint eg) str, int, float, etc..
    title : str
    author : str
    pages : int
    price : float

    # Use the __post_init__ function to customize additional properties
    def __post_init__(self):
        self.description = f"{self.title} by {self.author}, {self.pages} pages"

b1 = Book("Python Crash Course", "Eric Matthes", 345, 25.00)
b2 = Book("The Scent Keeper", "Erica Bauermeister", 250, 15.00)
b3 = Book("Python Crash Course", "Eric Matthes", 345, 25.00)

print(b1.description)
print(b1) # printing dataclass automatically implementing __repr__
print(b1 == b3) # comparing datasses automatically implementing __eq__

print(b1.title)
print(b2.author)