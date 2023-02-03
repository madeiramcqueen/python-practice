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

b1 = Book("Python Crash Course", "Eric Matthes", 25.00)

print(b1)
print(repr(b1))