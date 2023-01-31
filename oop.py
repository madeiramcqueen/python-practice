# Create a basic class
class Book:
    def __init__(self, title): # initializer function, initializing its attributes
        self.title = title

# Create instances of the class
b1 = Book('Once There Were Wolves')
b2 = Book('Our Missing Hearts')

# Print the class and property
print(b1)
print(b1.title) # printing the title with dot notation