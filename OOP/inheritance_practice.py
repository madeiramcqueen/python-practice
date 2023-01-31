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