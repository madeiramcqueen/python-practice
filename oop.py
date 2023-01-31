# LinkedIn Learning: "Python Object Oriented Programming" Course, Ch. 1

# # Create a basic class
# class Newspaper:
#     def __init__(self, name):
#         self.name = name

# # Create a basic class
# class Book:
#     def __init__(self, title, author, pages, price): # initializer function, initializing its attributes
#         self.title = title
#         self.author = author
#         self.pages = pages
#         self.price = price
#         self.__secret = 'This is a secret attribute' # __ = cannot be seen outsdie the class, will produce error if tried to be called
# # Create instance methods
#     def getPrice(self):
#         if hasattr(self, '_discount'):
#             return self.price - (self.price * self._discount)
#         else:
#             return self.price

#     def setDiscount(self, amount):
#         self._discount = amount # _ = intended to only be used by the class

# # Create instances of the class
# b1 = Book('Once There Were Wolves','Charlotte McConaghy', 272, 15.75)
# b2 = Book('Our Missing Hearts', 'Celeste Ng', 352, 14.50)
# n1 = Newspaper('The Seattle Times')

# # Print the class and property
# print(b1)
# print(b1.title) # printing the title with dot notation
# print(b1.getPrice())
# print(n1)
# print(n1.name)

# # Set discount for b2
# print(b2.getPrice())
# b2.setDiscount(0.25)
# print(b2.getPrice())

# # print(b1.__secret) # should produce error

# # Print the type of the object
# print(type(b2))

# # Compare two types together
# print(type(b1) == type(b2))
# print(type(b1) == type(n1))

# # Use isinstance() to compare a specific instance to a known type
# print(isinstance(b1, Book))
# print(isinstance(n1, Newspaper))
# print(isinstance(b1, Newspaper))

# LinkedIn Learning: "Python Object Oriented Programming" Course, Ch. 2

class Publication:
    def __init__(self, title, price):
        self.title = title
        self.price = price

# Periodical class inheriting from Publication
class Periodical(Publication):
    def __init__(self, title, price, period, publisher):
        super().__init__(title, price)
        self.period = period
        self.publisher = publisher

# Book class inheriting from Publication (title and price)
class Book(Publication):
    def __init__(self, title, author, pages, price):
        super().__init__(title, price)
        self.author = author
        self.pages = pages

class Magazine(Periodical):
    def __init__(self, title, publisher, price, period):
        super().__init__(title, price, period, publisher)

class Newspaper(Periodical):
    def __init__(self, title, publisher, price, period):
        super().__init__(title, price, period, publisher)

# Create instances
b1 = Book('Once There Were Wolves','Charlotte McConaghy', 272, 15.75)
m1 = Magazine('EdTech', 'EdTech Co', 5.99, 'Monthy')
n1 = Newspaper('New York Times', 'New York Times Company', 6.0, 'Daily' )

print(b1.author)
print(n1.publisher)
print(b1.price, m1.price, n1.price)