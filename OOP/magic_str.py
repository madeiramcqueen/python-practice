# LinkedIn Learning: "Python Object Oriented Programming" Course, Ch. 3
# Magic strings

class Book:
    def __init__(self, title, author, price):
        super().__init__()
        self.title = title
        self.author = author
        self.price = price

    # Use the __str__ method to return a string of the object to the user
    def __str__(self):
        return f"{self.title} by {self.author} costs {self.price}"

    # Use the __repr__ method to return an object representation
    def __repr__(self):
        return f"title={self.title}, author={self.author}, price={self.price}"

    # Use the __eq__ method to compare and check for equality between two diff objects
    def __eq__(self, value):
        if not isinstance(value, Book):
            raise ValueError("Can't compare book to a non-book!")

        return (self.title == value.title and self.author == value.author and self.price == value.price)

b1 = Book("Python Crash Course", "Eric Matthes", 25.00)
b2 = Book("The Scent Keeper", "Erica Bauermeister", 15.00
)
b3 = Book("Python Crash Course", "Eric Matthes", 25.00)

# Check for equality
print(b1 == b3) # should result in True
print(b1 == b2) # should result in False
print(b1 == 100) # should print ValueError message

# Check for a greater than or lesser than value

print(b1)
print(repr(b1))