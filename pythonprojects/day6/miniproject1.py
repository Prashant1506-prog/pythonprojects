#mini project 1 : library management system
class Book:

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

    def display(self):
        print("Title:", self.title)
        print("Author:", self.author)

    def borrow(self):
        if self.available:
            self.available = False
            print("Book borrowed")
        else:
            print("Book is already borrowed")

    def return_book(self):
        self.available = True
        print("Book returned")

x = input("Enter the name of the book: ")
y = input("Enter the name of the book author:")
book1 = Book(x, y)

book1.display()

book1.borrow()
book1.borrow()

book1.return_book()
book1.borrow()
