# single responsiblity principle

class Books():
    def __init__(self):
        self.books = {}
        self.number = 0
    
    def add_book(self, book):
        self.number += 1
        self.books[self.number] = book
    
    def __str__(self):
        return str(self.books)

class StoreBooks():
    @staticmethod
    def save_books(filename,books):
        with open(filename,"w") as f:
            f.write(str(books))

b = Books()
b.add_book("Books A")
b.add_book("Books B")
print(f"The books I have read are: {b}")

s = StoreBooks()
s.save_books("filename_b.txt",b)